'''
# AWS Security Hub Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_securityhub as securityhub
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for SecurityHub construct libraries](https://constructs.dev/search?q=securityhub)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::SecurityHub resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SecurityHub.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::SecurityHub](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SecurityHub.html).

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
    ITaggable as _ITaggable_36806126,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnAutomationRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_securityhub.CfnAutomationRule",
):
    '''The ``AWS::SecurityHub::AutomationRule`` resource specifies an automation rule based on input parameters.

    For more information, see `Automation rules <https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html>`_ in the *AWS Security Hub User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-automationrule.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_securityhub as securityhub
        
        # id: Any
        # updated_by: Any
        
        cfn_automation_rule = securityhub.CfnAutomationRule(self, "MyCfnAutomationRule",
            actions=[securityhub.CfnAutomationRule.AutomationRulesActionProperty(
                finding_fields_update=securityhub.CfnAutomationRule.AutomationRulesFindingFieldsUpdateProperty(
                    confidence=123,
                    criticality=123,
                    note=securityhub.CfnAutomationRule.NoteUpdateProperty(
                        text="text",
                        updated_by=updated_by
                    ),
                    related_findings=[securityhub.CfnAutomationRule.RelatedFindingProperty(
                        id=id,
                        product_arn="productArn"
                    )],
                    severity=securityhub.CfnAutomationRule.SeverityUpdateProperty(
                        label="label",
                        normalized=123,
                        product=123
                    ),
                    types=["types"],
                    user_defined_fields={
                        "user_defined_fields_key": "userDefinedFields"
                    },
                    verification_state="verificationState",
                    workflow=securityhub.CfnAutomationRule.WorkflowUpdateProperty(
                        status="status"
                    )
                ),
                type="type"
            )],
            criteria=securityhub.CfnAutomationRule.AutomationRulesFindingFiltersProperty(
                aws_account_id=[securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                company_name=[securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                compliance_associated_standards_id=[securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                compliance_security_control_id=[securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                compliance_status=[securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                confidence=[securityhub.CfnAutomationRule.NumberFilterProperty(
                    eq=123,
                    gte=123,
                    lte=123
                )],
                created_at=[securityhub.CfnAutomationRule.DateFilterProperty(
                    date_range=securityhub.CfnAutomationRule.DateRangeProperty(
                        unit="unit",
                        value=123
                    ),
                    end="end",
                    start="start"
                )],
                criticality=[securityhub.CfnAutomationRule.NumberFilterProperty(
                    eq=123,
                    gte=123,
                    lte=123
                )],
                description=[securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                first_observed_at=[securityhub.CfnAutomationRule.DateFilterProperty(
                    date_range=securityhub.CfnAutomationRule.DateRangeProperty(
                        unit="unit",
                        value=123
                    ),
                    end="end",
                    start="start"
                )],
                generator_id=[securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                id=[securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                last_observed_at=[securityhub.CfnAutomationRule.DateFilterProperty(
                    date_range=securityhub.CfnAutomationRule.DateRangeProperty(
                        unit="unit",
                        value=123
                    ),
                    end="end",
                    start="start"
                )],
                note_text=[securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                note_updated_at=[securityhub.CfnAutomationRule.DateFilterProperty(
                    date_range=securityhub.CfnAutomationRule.DateRangeProperty(
                        unit="unit",
                        value=123
                    ),
                    end="end",
                    start="start"
                )],
                note_updated_by=[securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                product_arn=[securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                product_name=[securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                record_state=[securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                related_findings_id=[securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                related_findings_product_arn=[securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_details_other=[securityhub.CfnAutomationRule.MapFilterProperty(
                    comparison="comparison",
                    key="key",
                    value="value"
                )],
                resource_id=[securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_partition=[securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_region=[securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_tags=[securityhub.CfnAutomationRule.MapFilterProperty(
                    comparison="comparison",
                    key="key",
                    value="value"
                )],
                resource_type=[securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                severity_label=[securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                source_url=[securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                title=[securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                type=[securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                updated_at=[securityhub.CfnAutomationRule.DateFilterProperty(
                    date_range=securityhub.CfnAutomationRule.DateRangeProperty(
                        unit="unit",
                        value=123
                    ),
                    end="end",
                    start="start"
                )],
                user_defined_fields=[securityhub.CfnAutomationRule.MapFilterProperty(
                    comparison="comparison",
                    key="key",
                    value="value"
                )],
                verification_state=[securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                workflow_status=[securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )]
            ),
            description="description",
            is_terminal=False,
            rule_name="ruleName",
            rule_order=123,
            rule_status="ruleStatus",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.AutomationRulesActionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        criteria: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.AutomationRulesFindingFiltersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        is_terminal: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        rule_name: typing.Optional[builtins.str] = None,
        rule_order: typing.Optional[jsii.Number] = None,
        rule_status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param actions: One or more actions to update finding fields if a finding matches the defined criteria of the rule.
        :param criteria: A set of `AWS Security Finding Format <https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html>`_ finding field attributes and corresponding expected values that Security Hub uses to filter findings. If a rule is enabled and a finding matches the conditions specified in this parameter, Security Hub applies the rule action to the finding.
        :param description: A description of the rule.
        :param is_terminal: Specifies whether a rule is the last to be applied with respect to a finding that matches the rule criteria. This is useful when a finding matches the criteria for multiple rules, and each rule has different actions. If a rule is terminal, Security Hub applies the rule action to a finding that matches the rule criteria and doesn't evaluate other rules for the finding. By default, a rule isn't terminal.
        :param rule_name: The name of the rule.
        :param rule_order: An integer ranging from 1 to 1000 that represents the order in which the rule action is applied to findings. Security Hub applies rules with lower values for this parameter first.
        :param rule_status: Whether the rule is active after it is created. If this parameter is equal to ``ENABLED`` , Security Hub applies the rule to findings and finding updates after the rule is created.
        :param tags: User-defined tags that help you label the purpose of a rule.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90c663d2946359b509542feafdcb3d89f11ca9e30a214aae02ea3d6b354c9846)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAutomationRuleProps(
            actions=actions,
            criteria=criteria,
            description=description,
            is_terminal=is_terminal,
            rule_name=rule_name,
            rule_order=rule_order,
            rule_status=rule_status,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae48eeaea63d372697a62c6052793e6367e3201b42f9513f1f0132b59dc350b0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cc6a8a522560219490822e00b9ec3810152de6616cf975f073c37fc9d8af31fc)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''A timestamp that indicates when the rule was created.

        Uses the ``date-time`` format specified in `RFC 3339 section 5.6, Internet Date/Time Format <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc3339#section-5.6>`_ . The value cannot contain spaces. For example, ``2020-03-22T13:22:13.933Z`` .

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedBy")
    def attr_created_by(self) -> builtins.str:
        '''The principal that created the rule.

        For example, ``arn:aws:sts::123456789012:assumed-role/Developer-Role/JaneDoe`` .

        :cloudformationAttribute: CreatedBy
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedBy"))

    @builtins.property
    @jsii.member(jsii_name="attrRuleArn")
    def attr_rule_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the automation rule that you create.

        For example, ``arn:aws:securityhub:us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`` .

        :cloudformationAttribute: RuleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRuleArn"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''A timestamp that indicates when the rule was most recently updated.

        Uses the ``date-time`` format specified in `RFC 3339 section 5.6, Internet Date/Time Format <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc3339#section-5.6>`_ . The value cannot contain spaces. For example, ``2020-03-22T13:22:13.933Z`` .

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="actions")
    def actions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.AutomationRulesActionProperty"]]]]:
        '''One or more actions to update finding fields if a finding matches the defined criteria of the rule.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.AutomationRulesActionProperty"]]]], jsii.get(self, "actions"))

    @actions.setter
    def actions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.AutomationRulesActionProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90988dc6b536563439917056373f7379ca48a864b5a3471a7b3552f6c9b40897)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actions", value)

    @builtins.property
    @jsii.member(jsii_name="criteria")
    def criteria(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.AutomationRulesFindingFiltersProperty"]]:
        '''A set of `AWS Security Finding Format <https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html>`_ finding field attributes and corresponding expected values that Security Hub uses to filter findings. If a rule is enabled and a finding matches the conditions specified in this parameter, Security Hub applies the rule action to the finding.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.AutomationRulesFindingFiltersProperty"]], jsii.get(self, "criteria"))

    @criteria.setter
    def criteria(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.AutomationRulesFindingFiltersProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc91daff88300654f2c8a9e4e5aad76fd0c26ae9c62e118febc7d1bff9733c5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "criteria", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the rule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13e710145ba6564ce42bac7fc3465ec7406a15699f473acd70e62bf605c1f259)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="isTerminal")
    def is_terminal(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether a rule is the last to be applied with respect to a finding that matches the rule criteria.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "isTerminal"))

    @is_terminal.setter
    def is_terminal(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11031a77a18a3180e3bf703420372155750c7001d9c920558ff50230e0111537)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isTerminal", value)

    @builtins.property
    @jsii.member(jsii_name="ruleName")
    def rule_name(self) -> typing.Optional[builtins.str]:
        '''The name of the rule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleName"))

    @rule_name.setter
    def rule_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffff694fc9dee0bbe561a13e56455e4e3a3b12c8c47e7c20a7fe2e8c13c0725c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleName", value)

    @builtins.property
    @jsii.member(jsii_name="ruleOrder")
    def rule_order(self) -> typing.Optional[jsii.Number]:
        '''An integer ranging from 1 to 1000 that represents the order in which the rule action is applied to findings.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ruleOrder"))

    @rule_order.setter
    def rule_order(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db37e60211fd885d4c7d0aa9af521faa3786061d7fa1712b86f54f3646a4738b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleOrder", value)

    @builtins.property
    @jsii.member(jsii_name="ruleStatus")
    def rule_status(self) -> typing.Optional[builtins.str]:
        '''Whether the rule is active after it is created.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleStatus"))

    @rule_status.setter
    def rule_status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0c77fc16c58c2d94764bb0b74df80e4884ec2c3948c0a364a0d9c75a4e9c79a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleStatus", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''User-defined tags that help you label the purpose of a rule.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a7d0579ca491d9adc050f0e2036942728d9db8e3d190f067473714a8ce9fd4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityhub.CfnAutomationRule.AutomationRulesActionProperty",
        jsii_struct_bases=[],
        name_mapping={"finding_fields_update": "findingFieldsUpdate", "type": "type"},
    )
    class AutomationRulesActionProperty:
        def __init__(
            self,
            *,
            finding_fields_update: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.AutomationRulesFindingFieldsUpdateProperty", typing.Dict[builtins.str, typing.Any]]],
            type: builtins.str,
        ) -> None:
            '''One or more actions to update finding fields if a finding matches the defined criteria of the rule.

            :param finding_fields_update: Specifies that the automation rule action is an update to a finding field.
            :param type: Specifies that the rule action should update the ``Types`` finding field. The ``Types`` finding field classifies findings in the format of namespace/category/classifier. For more information, see `Types taxonomy for ASFF <https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format-type-taxonomy.html>`_ in the *AWS Security Hub User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityhub as securityhub
                
                # id: Any
                # updated_by: Any
                
                automation_rules_action_property = securityhub.CfnAutomationRule.AutomationRulesActionProperty(
                    finding_fields_update=securityhub.CfnAutomationRule.AutomationRulesFindingFieldsUpdateProperty(
                        confidence=123,
                        criticality=123,
                        note=securityhub.CfnAutomationRule.NoteUpdateProperty(
                            text="text",
                            updated_by=updated_by
                        ),
                        related_findings=[securityhub.CfnAutomationRule.RelatedFindingProperty(
                            id=id,
                            product_arn="productArn"
                        )],
                        severity=securityhub.CfnAutomationRule.SeverityUpdateProperty(
                            label="label",
                            normalized=123,
                            product=123
                        ),
                        types=["types"],
                        user_defined_fields={
                            "user_defined_fields_key": "userDefinedFields"
                        },
                        verification_state="verificationState",
                        workflow=securityhub.CfnAutomationRule.WorkflowUpdateProperty(
                            status="status"
                        )
                    ),
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7d50f418e733dbb988d29d8dcedccc6faf2d022e32893189d084bb04a8c231ba)
                check_type(argname="argument finding_fields_update", value=finding_fields_update, expected_type=type_hints["finding_fields_update"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "finding_fields_update": finding_fields_update,
                "type": type,
            }

        @builtins.property
        def finding_fields_update(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.AutomationRulesFindingFieldsUpdateProperty"]:
            '''Specifies that the automation rule action is an update to a finding field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesaction.html#cfn-securityhub-automationrule-automationrulesaction-findingfieldsupdate
            '''
            result = self._values.get("finding_fields_update")
            assert result is not None, "Required property 'finding_fields_update' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.AutomationRulesFindingFieldsUpdateProperty"], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''Specifies that the rule action should update the ``Types`` finding field.

            The ``Types`` finding field classifies findings in the format of namespace/category/classifier. For more information, see `Types taxonomy for ASFF <https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format-type-taxonomy.html>`_ in the *AWS Security Hub User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesaction.html#cfn-securityhub-automationrule-automationrulesaction-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutomationRulesActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityhub.CfnAutomationRule.AutomationRulesFindingFieldsUpdateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "confidence": "confidence",
            "criticality": "criticality",
            "note": "note",
            "related_findings": "relatedFindings",
            "severity": "severity",
            "types": "types",
            "user_defined_fields": "userDefinedFields",
            "verification_state": "verificationState",
            "workflow": "workflow",
        },
    )
    class AutomationRulesFindingFieldsUpdateProperty:
        def __init__(
            self,
            *,
            confidence: typing.Optional[jsii.Number] = None,
            criticality: typing.Optional[jsii.Number] = None,
            note: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.NoteUpdateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            related_findings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.RelatedFindingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            severity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.SeverityUpdateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            types: typing.Optional[typing.Sequence[builtins.str]] = None,
            user_defined_fields: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
            verification_state: typing.Optional[builtins.str] = None,
            workflow: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.WorkflowUpdateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Identifies the finding fields that the automation rule action updates when a finding matches the defined criteria.

            :param confidence: The rule action updates the ``Confidence`` field of a finding.
            :param criticality: The rule action updates the ``Criticality`` field of a finding.
            :param note: The rule action will update the ``Note`` field of a finding.
            :param related_findings: The rule action will update the ``RelatedFindings`` field of a finding.
            :param severity: The rule action will update the ``Severity`` field of a finding.
            :param types: The rule action updates the ``Types`` field of a finding.
            :param user_defined_fields: The rule action updates the ``UserDefinedFields`` field of a finding.
            :param verification_state: The rule action updates the ``VerificationState`` field of a finding.
            :param workflow: The rule action will update the ``Workflow`` field of a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityhub as securityhub
                
                # id: Any
                # updated_by: Any
                
                automation_rules_finding_fields_update_property = securityhub.CfnAutomationRule.AutomationRulesFindingFieldsUpdateProperty(
                    confidence=123,
                    criticality=123,
                    note=securityhub.CfnAutomationRule.NoteUpdateProperty(
                        text="text",
                        updated_by=updated_by
                    ),
                    related_findings=[securityhub.CfnAutomationRule.RelatedFindingProperty(
                        id=id,
                        product_arn="productArn"
                    )],
                    severity=securityhub.CfnAutomationRule.SeverityUpdateProperty(
                        label="label",
                        normalized=123,
                        product=123
                    ),
                    types=["types"],
                    user_defined_fields={
                        "user_defined_fields_key": "userDefinedFields"
                    },
                    verification_state="verificationState",
                    workflow=securityhub.CfnAutomationRule.WorkflowUpdateProperty(
                        status="status"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__46649258d4db7d36012fa064d0d3a3c3e3937ea1364fbd532ef0e84d437b6833)
                check_type(argname="argument confidence", value=confidence, expected_type=type_hints["confidence"])
                check_type(argname="argument criticality", value=criticality, expected_type=type_hints["criticality"])
                check_type(argname="argument note", value=note, expected_type=type_hints["note"])
                check_type(argname="argument related_findings", value=related_findings, expected_type=type_hints["related_findings"])
                check_type(argname="argument severity", value=severity, expected_type=type_hints["severity"])
                check_type(argname="argument types", value=types, expected_type=type_hints["types"])
                check_type(argname="argument user_defined_fields", value=user_defined_fields, expected_type=type_hints["user_defined_fields"])
                check_type(argname="argument verification_state", value=verification_state, expected_type=type_hints["verification_state"])
                check_type(argname="argument workflow", value=workflow, expected_type=type_hints["workflow"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if confidence is not None:
                self._values["confidence"] = confidence
            if criticality is not None:
                self._values["criticality"] = criticality
            if note is not None:
                self._values["note"] = note
            if related_findings is not None:
                self._values["related_findings"] = related_findings
            if severity is not None:
                self._values["severity"] = severity
            if types is not None:
                self._values["types"] = types
            if user_defined_fields is not None:
                self._values["user_defined_fields"] = user_defined_fields
            if verification_state is not None:
                self._values["verification_state"] = verification_state
            if workflow is not None:
                self._values["workflow"] = workflow

        @builtins.property
        def confidence(self) -> typing.Optional[jsii.Number]:
            '''The rule action updates the ``Confidence`` field of a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate.html#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-confidence
            '''
            result = self._values.get("confidence")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def criticality(self) -> typing.Optional[jsii.Number]:
            '''The rule action updates the ``Criticality`` field of a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate.html#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-criticality
            '''
            result = self._values.get("criticality")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def note(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.NoteUpdateProperty"]]:
            '''The rule action will update the ``Note`` field of a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate.html#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-note
            '''
            result = self._values.get("note")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.NoteUpdateProperty"]], result)

        @builtins.property
        def related_findings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.RelatedFindingProperty"]]]]:
            '''The rule action will update the ``RelatedFindings`` field of a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate.html#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-relatedfindings
            '''
            result = self._values.get("related_findings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.RelatedFindingProperty"]]]], result)

        @builtins.property
        def severity(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.SeverityUpdateProperty"]]:
            '''The rule action will update the ``Severity`` field of a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate.html#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-severity
            '''
            result = self._values.get("severity")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.SeverityUpdateProperty"]], result)

        @builtins.property
        def types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The rule action updates the ``Types`` field of a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate.html#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-types
            '''
            result = self._values.get("types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def user_defined_fields(
            self,
        ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]]:
            '''The rule action updates the ``UserDefinedFields`` field of a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate.html#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-userdefinedfields
            '''
            result = self._values.get("user_defined_fields")
            return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]], result)

        @builtins.property
        def verification_state(self) -> typing.Optional[builtins.str]:
            '''The rule action updates the ``VerificationState`` field of a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate.html#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-verificationstate
            '''
            result = self._values.get("verification_state")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def workflow(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.WorkflowUpdateProperty"]]:
            '''The rule action will update the ``Workflow`` field of a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate.html#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-workflow
            '''
            result = self._values.get("workflow")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.WorkflowUpdateProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutomationRulesFindingFieldsUpdateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityhub.CfnAutomationRule.AutomationRulesFindingFiltersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aws_account_id": "awsAccountId",
            "company_name": "companyName",
            "compliance_associated_standards_id": "complianceAssociatedStandardsId",
            "compliance_security_control_id": "complianceSecurityControlId",
            "compliance_status": "complianceStatus",
            "confidence": "confidence",
            "created_at": "createdAt",
            "criticality": "criticality",
            "description": "description",
            "first_observed_at": "firstObservedAt",
            "generator_id": "generatorId",
            "id": "id",
            "last_observed_at": "lastObservedAt",
            "note_text": "noteText",
            "note_updated_at": "noteUpdatedAt",
            "note_updated_by": "noteUpdatedBy",
            "product_arn": "productArn",
            "product_name": "productName",
            "record_state": "recordState",
            "related_findings_id": "relatedFindingsId",
            "related_findings_product_arn": "relatedFindingsProductArn",
            "resource_details_other": "resourceDetailsOther",
            "resource_id": "resourceId",
            "resource_partition": "resourcePartition",
            "resource_region": "resourceRegion",
            "resource_tags": "resourceTags",
            "resource_type": "resourceType",
            "severity_label": "severityLabel",
            "source_url": "sourceUrl",
            "title": "title",
            "type": "type",
            "updated_at": "updatedAt",
            "user_defined_fields": "userDefinedFields",
            "verification_state": "verificationState",
            "workflow_status": "workflowStatus",
        },
    )
    class AutomationRulesFindingFiltersProperty:
        def __init__(
            self,
            *,
            aws_account_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            company_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            compliance_associated_standards_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            compliance_security_control_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            compliance_status: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            confidence: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.NumberFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            created_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.DateFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            criticality: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.NumberFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            description: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            first_observed_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.DateFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            generator_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            last_observed_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.DateFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            note_text: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            note_updated_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.DateFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            note_updated_by: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            product_arn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            product_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            record_state: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            related_findings_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            related_findings_product_arn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_details_other: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.MapFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_partition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_region: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.MapFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            severity_label: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            source_url: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            title: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            updated_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.DateFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            user_defined_fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.MapFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            verification_state: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            workflow_status: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The criteria that determine which findings a rule applies to.

            :param aws_account_id: The AWS account ID in which a finding was generated.
            :param company_name: The name of the company for the product that generated the finding. For control-based findings, the company is AWS .
            :param compliance_associated_standards_id: The unique identifier of a standard in which a control is enabled. This field consists of the resource portion of the Amazon Resource Name (ARN) returned for a standard in the `DescribeStandards <https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html>`_ API response.
            :param compliance_security_control_id: The security control ID for which a finding was generated. Security control IDs are the same across standards.
            :param compliance_status: The result of a security check. This field is only used for findings generated from controls.
            :param confidence: The likelihood that a finding accurately identifies the behavior or issue that it was intended to identify. ``Confidence`` is scored on a 0–100 basis using a ratio scale. A value of ``0`` means 0 percent confidence, and a value of ``100`` means 100 percent confidence. For example, a data exfiltration detection based on a statistical deviation of network traffic has low confidence because an actual exfiltration hasn't been verified. For more information, see `Confidence <https://docs.aws.amazon.com/securityhub/latest/userguide/asff-top-level-attributes.html#asff-confidence>`_ in the *AWS Security Hub User Guide* .
            :param created_at: A timestamp that indicates when this finding record was created. Uses the ``date-time`` format specified in `RFC 3339 section 5.6, Internet Date/Time Format <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc3339#section-5.6>`_ . The value cannot contain spaces. For example, ``2020-03-22T13:22:13.933Z`` .
            :param criticality: The level of importance that is assigned to the resources that are associated with a finding. ``Criticality`` is scored on a 0–100 basis, using a ratio scale that supports only full integers. A score of ``0`` means that the underlying resources have no criticality, and a score of ``100`` is reserved for the most critical resources. For more information, see `Criticality <https://docs.aws.amazon.com/securityhub/latest/userguide/asff-top-level-attributes.html#asff-criticality>`_ in the *AWS Security Hub User Guide* .
            :param description: A finding's description.
            :param first_observed_at: A timestamp that indicates when the potential security issue captured by a finding was first observed by the security findings product. Uses the ``date-time`` format specified in `RFC 3339 section 5.6, Internet Date/Time Format <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc3339#section-5.6>`_ . The value cannot contain spaces. For example, ``2020-03-22T13:22:13.933Z`` .
            :param generator_id: The identifier for the solution-specific component that generated a finding.
            :param id: The product-specific identifier for a finding.
            :param last_observed_at: A timestamp that indicates when the potential security issue captured by a finding was most recently observed by the security findings product. Uses the ``date-time`` format specified in `RFC 3339 section 5.6, Internet Date/Time Format <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc3339#section-5.6>`_ . The value cannot contain spaces. For example, ``2020-03-22T13:22:13.933Z`` .
            :param note_text: The text of a user-defined note that's added to a finding.
            :param note_updated_at: The timestamp of when the note was updated. Uses the date-time format specified in `RFC 3339 section 5.6, Internet Date/Time Format <https://docs.aws.amazon.com/https://www.rfc-editor.org/rfc/rfc3339#section-5.6>`_ . The value cannot contain spaces. For example, ``2020-03-22T13:22:13.933Z`` .
            :param note_updated_by: The principal that created a note.
            :param product_arn: The Amazon Resource Name (ARN) for a third-party product that generated a finding in Security Hub.
            :param product_name: Provides the name of the product that generated the finding. For control-based findings, the product name is Security Hub.
            :param record_state: Provides the current state of a finding.
            :param related_findings_id: The product-generated identifier for a related finding.
            :param related_findings_product_arn: The ARN for the product that generated a related finding.
            :param resource_details_other: Custom fields and values about the resource that a finding pertains to.
            :param resource_id: The identifier for the given resource type. For AWS resources that are identified by Amazon Resource Names (ARNs), this is the ARN. For AWS resources that lack ARNs, this is the identifier as defined by the AWS service that created the resource. For non- AWS resources, this is a unique identifier that is associated with the resource.
            :param resource_partition: The partition in which the resource that the finding pertains to is located. A partition is a group of AWS Regions . Each AWS account is scoped to one partition.
            :param resource_region: The AWS Region where the resource that a finding pertains to is located.
            :param resource_tags: A list of AWS tags associated with a resource at the time the finding was processed.
            :param resource_type: A finding's title.
            :param severity_label: The severity value of the finding.
            :param source_url: Provides a URL that links to a page about the current finding in the finding product.
            :param title: A finding's title.
            :param type: One or more finding types in the format of namespace/category/classifier that classify a finding. For a list of namespaces, classifiers, and categories, see `Types taxonomy for ASFF <https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format-type-taxonomy.html>`_ in the *AWS Security Hub User Guide* .
            :param updated_at: A timestamp that indicates when the finding record was most recently updated. Uses the ``date-time`` format specified in `RFC 3339 section 5.6, Internet Date/Time Format <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc3339#section-5.6>`_ . The value cannot contain spaces. For example, ``2020-03-22T13:22:13.933Z`` .
            :param user_defined_fields: A list of user-defined name and value string pairs added to a finding.
            :param verification_state: Provides the veracity of a finding.
            :param workflow_status: Provides information about the status of the investigation into a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityhub as securityhub
                
                automation_rules_finding_filters_property = securityhub.CfnAutomationRule.AutomationRulesFindingFiltersProperty(
                    aws_account_id=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    company_name=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    compliance_associated_standards_id=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    compliance_security_control_id=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    compliance_status=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    confidence=[securityhub.CfnAutomationRule.NumberFilterProperty(
                        eq=123,
                        gte=123,
                        lte=123
                    )],
                    created_at=[securityhub.CfnAutomationRule.DateFilterProperty(
                        date_range=securityhub.CfnAutomationRule.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    criticality=[securityhub.CfnAutomationRule.NumberFilterProperty(
                        eq=123,
                        gte=123,
                        lte=123
                    )],
                    description=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    first_observed_at=[securityhub.CfnAutomationRule.DateFilterProperty(
                        date_range=securityhub.CfnAutomationRule.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    generator_id=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    id=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    last_observed_at=[securityhub.CfnAutomationRule.DateFilterProperty(
                        date_range=securityhub.CfnAutomationRule.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    note_text=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    note_updated_at=[securityhub.CfnAutomationRule.DateFilterProperty(
                        date_range=securityhub.CfnAutomationRule.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    note_updated_by=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    product_arn=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    product_name=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    record_state=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    related_findings_id=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    related_findings_product_arn=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_details_other=[securityhub.CfnAutomationRule.MapFilterProperty(
                        comparison="comparison",
                        key="key",
                        value="value"
                    )],
                    resource_id=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_partition=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_region=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_tags=[securityhub.CfnAutomationRule.MapFilterProperty(
                        comparison="comparison",
                        key="key",
                        value="value"
                    )],
                    resource_type=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    severity_label=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    source_url=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    title=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    type=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    updated_at=[securityhub.CfnAutomationRule.DateFilterProperty(
                        date_range=securityhub.CfnAutomationRule.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    user_defined_fields=[securityhub.CfnAutomationRule.MapFilterProperty(
                        comparison="comparison",
                        key="key",
                        value="value"
                    )],
                    verification_state=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    workflow_status=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2f1ea2f0c8b7a77a075035fe359b4018192a7fe37d13a835705cccc22b3887fa)
                check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
                check_type(argname="argument company_name", value=company_name, expected_type=type_hints["company_name"])
                check_type(argname="argument compliance_associated_standards_id", value=compliance_associated_standards_id, expected_type=type_hints["compliance_associated_standards_id"])
                check_type(argname="argument compliance_security_control_id", value=compliance_security_control_id, expected_type=type_hints["compliance_security_control_id"])
                check_type(argname="argument compliance_status", value=compliance_status, expected_type=type_hints["compliance_status"])
                check_type(argname="argument confidence", value=confidence, expected_type=type_hints["confidence"])
                check_type(argname="argument created_at", value=created_at, expected_type=type_hints["created_at"])
                check_type(argname="argument criticality", value=criticality, expected_type=type_hints["criticality"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument first_observed_at", value=first_observed_at, expected_type=type_hints["first_observed_at"])
                check_type(argname="argument generator_id", value=generator_id, expected_type=type_hints["generator_id"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument last_observed_at", value=last_observed_at, expected_type=type_hints["last_observed_at"])
                check_type(argname="argument note_text", value=note_text, expected_type=type_hints["note_text"])
                check_type(argname="argument note_updated_at", value=note_updated_at, expected_type=type_hints["note_updated_at"])
                check_type(argname="argument note_updated_by", value=note_updated_by, expected_type=type_hints["note_updated_by"])
                check_type(argname="argument product_arn", value=product_arn, expected_type=type_hints["product_arn"])
                check_type(argname="argument product_name", value=product_name, expected_type=type_hints["product_name"])
                check_type(argname="argument record_state", value=record_state, expected_type=type_hints["record_state"])
                check_type(argname="argument related_findings_id", value=related_findings_id, expected_type=type_hints["related_findings_id"])
                check_type(argname="argument related_findings_product_arn", value=related_findings_product_arn, expected_type=type_hints["related_findings_product_arn"])
                check_type(argname="argument resource_details_other", value=resource_details_other, expected_type=type_hints["resource_details_other"])
                check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
                check_type(argname="argument resource_partition", value=resource_partition, expected_type=type_hints["resource_partition"])
                check_type(argname="argument resource_region", value=resource_region, expected_type=type_hints["resource_region"])
                check_type(argname="argument resource_tags", value=resource_tags, expected_type=type_hints["resource_tags"])
                check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
                check_type(argname="argument severity_label", value=severity_label, expected_type=type_hints["severity_label"])
                check_type(argname="argument source_url", value=source_url, expected_type=type_hints["source_url"])
                check_type(argname="argument title", value=title, expected_type=type_hints["title"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument updated_at", value=updated_at, expected_type=type_hints["updated_at"])
                check_type(argname="argument user_defined_fields", value=user_defined_fields, expected_type=type_hints["user_defined_fields"])
                check_type(argname="argument verification_state", value=verification_state, expected_type=type_hints["verification_state"])
                check_type(argname="argument workflow_status", value=workflow_status, expected_type=type_hints["workflow_status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if aws_account_id is not None:
                self._values["aws_account_id"] = aws_account_id
            if company_name is not None:
                self._values["company_name"] = company_name
            if compliance_associated_standards_id is not None:
                self._values["compliance_associated_standards_id"] = compliance_associated_standards_id
            if compliance_security_control_id is not None:
                self._values["compliance_security_control_id"] = compliance_security_control_id
            if compliance_status is not None:
                self._values["compliance_status"] = compliance_status
            if confidence is not None:
                self._values["confidence"] = confidence
            if created_at is not None:
                self._values["created_at"] = created_at
            if criticality is not None:
                self._values["criticality"] = criticality
            if description is not None:
                self._values["description"] = description
            if first_observed_at is not None:
                self._values["first_observed_at"] = first_observed_at
            if generator_id is not None:
                self._values["generator_id"] = generator_id
            if id is not None:
                self._values["id"] = id
            if last_observed_at is not None:
                self._values["last_observed_at"] = last_observed_at
            if note_text is not None:
                self._values["note_text"] = note_text
            if note_updated_at is not None:
                self._values["note_updated_at"] = note_updated_at
            if note_updated_by is not None:
                self._values["note_updated_by"] = note_updated_by
            if product_arn is not None:
                self._values["product_arn"] = product_arn
            if product_name is not None:
                self._values["product_name"] = product_name
            if record_state is not None:
                self._values["record_state"] = record_state
            if related_findings_id is not None:
                self._values["related_findings_id"] = related_findings_id
            if related_findings_product_arn is not None:
                self._values["related_findings_product_arn"] = related_findings_product_arn
            if resource_details_other is not None:
                self._values["resource_details_other"] = resource_details_other
            if resource_id is not None:
                self._values["resource_id"] = resource_id
            if resource_partition is not None:
                self._values["resource_partition"] = resource_partition
            if resource_region is not None:
                self._values["resource_region"] = resource_region
            if resource_tags is not None:
                self._values["resource_tags"] = resource_tags
            if resource_type is not None:
                self._values["resource_type"] = resource_type
            if severity_label is not None:
                self._values["severity_label"] = severity_label
            if source_url is not None:
                self._values["source_url"] = source_url
            if title is not None:
                self._values["title"] = title
            if type is not None:
                self._values["type"] = type
            if updated_at is not None:
                self._values["updated_at"] = updated_at
            if user_defined_fields is not None:
                self._values["user_defined_fields"] = user_defined_fields
            if verification_state is not None:
                self._values["verification_state"] = verification_state
            if workflow_status is not None:
                self._values["workflow_status"] = workflow_status

        @builtins.property
        def aws_account_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The AWS account ID in which a finding was generated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-awsaccountid
            '''
            result = self._values.get("aws_account_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def company_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The name of the company for the product that generated the finding.

            For control-based findings, the company is AWS .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-companyname
            '''
            result = self._values.get("company_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def compliance_associated_standards_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The unique identifier of a standard in which a control is enabled.

            This field consists of the resource portion of the Amazon Resource Name (ARN) returned for a standard in the `DescribeStandards <https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html>`_ API response.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-complianceassociatedstandardsid
            '''
            result = self._values.get("compliance_associated_standards_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def compliance_security_control_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The security control ID for which a finding was generated.

            Security control IDs are the same across standards.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-compliancesecuritycontrolid
            '''
            result = self._values.get("compliance_security_control_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def compliance_status(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The result of a security check.

            This field is only used for findings generated from controls.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-compliancestatus
            '''
            result = self._values.get("compliance_status")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def confidence(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.NumberFilterProperty"]]]]:
            '''The likelihood that a finding accurately identifies the behavior or issue that it was intended to identify.

            ``Confidence`` is scored on a 0–100 basis using a ratio scale. A value of ``0`` means 0 percent confidence, and a value of ``100`` means 100 percent confidence. For example, a data exfiltration detection based on a statistical deviation of network traffic has low confidence because an actual exfiltration hasn't been verified. For more information, see `Confidence <https://docs.aws.amazon.com/securityhub/latest/userguide/asff-top-level-attributes.html#asff-confidence>`_ in the *AWS Security Hub User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-confidence
            '''
            result = self._values.get("confidence")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.NumberFilterProperty"]]]], result)

        @builtins.property
        def created_at(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.DateFilterProperty"]]]]:
            '''A timestamp that indicates when this finding record was created.

            Uses the ``date-time`` format specified in `RFC 3339 section 5.6, Internet Date/Time Format <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc3339#section-5.6>`_ . The value cannot contain spaces. For example, ``2020-03-22T13:22:13.933Z`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-createdat
            '''
            result = self._values.get("created_at")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.DateFilterProperty"]]]], result)

        @builtins.property
        def criticality(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.NumberFilterProperty"]]]]:
            '''The level of importance that is assigned to the resources that are associated with a finding.

            ``Criticality`` is scored on a 0–100 basis, using a ratio scale that supports only full integers. A score of ``0`` means that the underlying resources have no criticality, and a score of ``100`` is reserved for the most critical resources. For more information, see `Criticality <https://docs.aws.amazon.com/securityhub/latest/userguide/asff-top-level-attributes.html#asff-criticality>`_ in the *AWS Security Hub User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-criticality
            '''
            result = self._values.get("criticality")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.NumberFilterProperty"]]]], result)

        @builtins.property
        def description(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''A finding's description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def first_observed_at(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.DateFilterProperty"]]]]:
            '''A timestamp that indicates when the potential security issue captured by a finding was first observed by the security findings product.

            Uses the ``date-time`` format specified in `RFC 3339 section 5.6, Internet Date/Time Format <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc3339#section-5.6>`_ . The value cannot contain spaces. For example, ``2020-03-22T13:22:13.933Z`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-firstobservedat
            '''
            result = self._values.get("first_observed_at")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.DateFilterProperty"]]]], result)

        @builtins.property
        def generator_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The identifier for the solution-specific component that generated a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-generatorid
            '''
            result = self._values.get("generator_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The product-specific identifier for a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def last_observed_at(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.DateFilterProperty"]]]]:
            '''A timestamp that indicates when the potential security issue captured by a finding was most recently observed by the security findings product.

            Uses the ``date-time`` format specified in `RFC 3339 section 5.6, Internet Date/Time Format <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc3339#section-5.6>`_ . The value cannot contain spaces. For example, ``2020-03-22T13:22:13.933Z`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-lastobservedat
            '''
            result = self._values.get("last_observed_at")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.DateFilterProperty"]]]], result)

        @builtins.property
        def note_text(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The text of a user-defined note that's added to a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-notetext
            '''
            result = self._values.get("note_text")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def note_updated_at(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.DateFilterProperty"]]]]:
            '''The timestamp of when the note was updated.

            Uses the date-time format specified in `RFC 3339 section 5.6, Internet Date/Time Format <https://docs.aws.amazon.com/https://www.rfc-editor.org/rfc/rfc3339#section-5.6>`_ . The value cannot contain spaces. For example, ``2020-03-22T13:22:13.933Z`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-noteupdatedat
            '''
            result = self._values.get("note_updated_at")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.DateFilterProperty"]]]], result)

        @builtins.property
        def note_updated_by(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The principal that created a note.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-noteupdatedby
            '''
            result = self._values.get("note_updated_by")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def product_arn(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The Amazon Resource Name (ARN) for a third-party product that generated a finding in Security Hub.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-productarn
            '''
            result = self._values.get("product_arn")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def product_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''Provides the name of the product that generated the finding.

            For control-based findings, the product name is Security Hub.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-productname
            '''
            result = self._values.get("product_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def record_state(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''Provides the current state of a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-recordstate
            '''
            result = self._values.get("record_state")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def related_findings_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The product-generated identifier for a related finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-relatedfindingsid
            '''
            result = self._values.get("related_findings_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def related_findings_product_arn(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The ARN for the product that generated a related finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-relatedfindingsproductarn
            '''
            result = self._values.get("related_findings_product_arn")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_details_other(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.MapFilterProperty"]]]]:
            '''Custom fields and values about the resource that a finding pertains to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-resourcedetailsother
            '''
            result = self._values.get("resource_details_other")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.MapFilterProperty"]]]], result)

        @builtins.property
        def resource_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The identifier for the given resource type.

            For AWS resources that are identified by Amazon Resource Names (ARNs), this is the ARN. For AWS resources that lack ARNs, this is the identifier as defined by the AWS service that created the resource. For non- AWS resources, this is a unique identifier that is associated with the resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-resourceid
            '''
            result = self._values.get("resource_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_partition(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The partition in which the resource that the finding pertains to is located.

            A partition is a group of AWS Regions . Each AWS account is scoped to one partition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-resourcepartition
            '''
            result = self._values.get("resource_partition")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_region(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The AWS Region where the resource that a finding pertains to is located.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-resourceregion
            '''
            result = self._values.get("resource_region")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_tags(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.MapFilterProperty"]]]]:
            '''A list of AWS tags associated with a resource at the time the finding was processed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-resourcetags
            '''
            result = self._values.get("resource_tags")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.MapFilterProperty"]]]], result)

        @builtins.property
        def resource_type(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''A finding's title.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-resourcetype
            '''
            result = self._values.get("resource_type")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def severity_label(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The severity value of the finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-severitylabel
            '''
            result = self._values.get("severity_label")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def source_url(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''Provides a URL that links to a page about the current finding in the finding product.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-sourceurl
            '''
            result = self._values.get("source_url")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def title(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''A finding's title.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-title
            '''
            result = self._values.get("title")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def type(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''One or more finding types in the format of namespace/category/classifier that classify a finding.

            For a list of namespaces, classifiers, and categories, see `Types taxonomy for ASFF <https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format-type-taxonomy.html>`_ in the *AWS Security Hub User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def updated_at(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.DateFilterProperty"]]]]:
            '''A timestamp that indicates when the finding record was most recently updated.

            Uses the ``date-time`` format specified in `RFC 3339 section 5.6, Internet Date/Time Format <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc3339#section-5.6>`_ . The value cannot contain spaces. For example, ``2020-03-22T13:22:13.933Z`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-updatedat
            '''
            result = self._values.get("updated_at")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.DateFilterProperty"]]]], result)

        @builtins.property
        def user_defined_fields(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.MapFilterProperty"]]]]:
            '''A list of user-defined name and value string pairs added to a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-userdefinedfields
            '''
            result = self._values.get("user_defined_fields")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.MapFilterProperty"]]]], result)

        @builtins.property
        def verification_state(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''Provides the veracity of a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-verificationstate
            '''
            result = self._values.get("verification_state")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def workflow_status(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''Provides information about the status of the investigation into a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-workflowstatus
            '''
            result = self._values.get("workflow_status")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutomationRulesFindingFiltersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityhub.CfnAutomationRule.DateFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"date_range": "dateRange", "end": "end", "start": "start"},
    )
    class DateFilterProperty:
        def __init__(
            self,
            *,
            date_range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAutomationRule.DateRangeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            end: typing.Optional[builtins.str] = None,
            start: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A date filter for querying findings.

            :param date_range: A date range for the date filter.
            :param end: A timestamp that provides the end date for the date filter. A correctly formatted example is ``2020-05-21T20:16:34.724Z`` . The value cannot contain spaces, and date and time should be separated by ``T`` . For more information, see `RFC 3339 section 5.6, Internet Date/Time Format <https://docs.aws.amazon.com/https://www.rfc-editor.org/rfc/rfc3339#section-5.6>`_ .
            :param start: A timestamp that provides the start date for the date filter. A correctly formatted example is ``2020-05-21T20:16:34.724Z`` . The value cannot contain spaces, and date and time should be separated by ``T`` . For more information, see `RFC 3339 section 5.6, Internet Date/Time Format <https://docs.aws.amazon.com/https://www.rfc-editor.org/rfc/rfc3339#section-5.6>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-datefilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityhub as securityhub
                
                date_filter_property = securityhub.CfnAutomationRule.DateFilterProperty(
                    date_range=securityhub.CfnAutomationRule.DateRangeProperty(
                        unit="unit",
                        value=123
                    ),
                    end="end",
                    start="start"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a3a0031cd590c4fc4c1cc1b567254acf98a8abce8663cfb8d1619b78415afbda)
                check_type(argname="argument date_range", value=date_range, expected_type=type_hints["date_range"])
                check_type(argname="argument end", value=end, expected_type=type_hints["end"])
                check_type(argname="argument start", value=start, expected_type=type_hints["start"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if date_range is not None:
                self._values["date_range"] = date_range
            if end is not None:
                self._values["end"] = end
            if start is not None:
                self._values["start"] = start

        @builtins.property
        def date_range(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.DateRangeProperty"]]:
            '''A date range for the date filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-datefilter.html#cfn-securityhub-automationrule-datefilter-daterange
            '''
            result = self._values.get("date_range")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.DateRangeProperty"]], result)

        @builtins.property
        def end(self) -> typing.Optional[builtins.str]:
            '''A timestamp that provides the end date for the date filter.

            A correctly formatted example is ``2020-05-21T20:16:34.724Z`` . The value cannot contain spaces, and date and time should be separated by ``T`` . For more information, see `RFC 3339 section 5.6, Internet Date/Time Format <https://docs.aws.amazon.com/https://www.rfc-editor.org/rfc/rfc3339#section-5.6>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-datefilter.html#cfn-securityhub-automationrule-datefilter-end
            '''
            result = self._values.get("end")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def start(self) -> typing.Optional[builtins.str]:
            '''A timestamp that provides the start date for the date filter.

            A correctly formatted example is ``2020-05-21T20:16:34.724Z`` . The value cannot contain spaces, and date and time should be separated by ``T`` . For more information, see `RFC 3339 section 5.6, Internet Date/Time Format <https://docs.aws.amazon.com/https://www.rfc-editor.org/rfc/rfc3339#section-5.6>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-datefilter.html#cfn-securityhub-automationrule-datefilter-start
            '''
            result = self._values.get("start")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DateFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityhub.CfnAutomationRule.DateRangeProperty",
        jsii_struct_bases=[],
        name_mapping={"unit": "unit", "value": "value"},
    )
    class DateRangeProperty:
        def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
            '''A date range for the date filter.

            :param unit: A date range unit for the date filter.
            :param value: A date range value for the date filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-daterange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityhub as securityhub
                
                date_range_property = securityhub.CfnAutomationRule.DateRangeProperty(
                    unit="unit",
                    value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__36ae8c17dfe76daaeb266eeb694027401c6b86fa8ecdc8744eaa6e092d24f29d)
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "unit": unit,
                "value": value,
            }

        @builtins.property
        def unit(self) -> builtins.str:
            '''A date range unit for the date filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-daterange.html#cfn-securityhub-automationrule-daterange-unit
            '''
            result = self._values.get("unit")
            assert result is not None, "Required property 'unit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> jsii.Number:
            '''A date range value for the date filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-daterange.html#cfn-securityhub-automationrule-daterange-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DateRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityhub.CfnAutomationRule.MapFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"comparison": "comparison", "key": "key", "value": "value"},
    )
    class MapFilterProperty:
        def __init__(
            self,
            *,
            comparison: builtins.str,
            key: builtins.str,
            value: builtins.str,
        ) -> None:
            '''A map filter for filtering AWS Security Hub findings.

            Each map filter provides the field to check for, the value to check for, and the comparison operator.

            :param comparison: The condition to apply to the key value when filtering Security Hub findings with a map filter. To search for values that have the filter value, use one of the following comparison operators: - To search for values that include the filter value, use ``CONTAINS`` . For example, for the ``ResourceTags`` field, the filter ``Department CONTAINS Security`` matches findings that include the value ``Security`` for the ``Department`` tag. In the same example, a finding with a value of ``Security team`` for the ``Department`` tag is a match. - To search for values that exactly match the filter value, use ``EQUALS`` . For example, for the ``ResourceTags`` field, the filter ``Department EQUALS Security`` matches findings that have the value ``Security`` for the ``Department`` tag. ``CONTAINS`` and ``EQUALS`` filters on the same field are joined by ``OR`` . A finding matches if it matches any one of those filters. For example, the filters ``Department CONTAINS Security OR Department CONTAINS Finance`` match a finding that includes either ``Security`` , ``Finance`` , or both values. To search for values that don't have the filter value, use one of the following comparison operators: - To search for values that exclude the filter value, use ``NOT_CONTAINS`` . For example, for the ``ResourceTags`` field, the filter ``Department NOT_CONTAINS Finance`` matches findings that exclude the value ``Finance`` for the ``Department`` tag. - To search for values other than the filter value, use ``NOT_EQUALS`` . For example, for the ``ResourceTags`` field, the filter ``Department NOT_EQUALS Finance`` matches findings that don’t have the value ``Finance`` for the ``Department`` tag. ``NOT_CONTAINS`` and ``NOT_EQUALS`` filters on the same field are joined by ``AND`` . A finding matches only if it matches all of those filters. For example, the filters ``Department NOT_CONTAINS Security AND Department NOT_CONTAINS Finance`` match a finding that excludes both the ``Security`` and ``Finance`` values. ``CONTAINS`` filters can only be used with other ``CONTAINS`` filters. ``NOT_CONTAINS`` filters can only be used with other ``NOT_CONTAINS`` filters. You can’t have both a ``CONTAINS`` filter and a ``NOT_CONTAINS`` filter on the same field. Similarly, you can’t have both an ``EQUALS`` filter and a ``NOT_EQUALS`` filter on the same field. Combining filters in this way returns an error. ``CONTAINS`` and ``NOT_CONTAINS`` operators can be used only with automation rules. For more information, see `Automation rules <https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html>`_ in the *AWS Security Hub User Guide* .
            :param key: The key of the map filter. For example, for ``ResourceTags`` , ``Key`` identifies the name of the tag. For ``UserDefinedFields`` , ``Key`` is the name of the field.
            :param value: The value for the key in the map filter. Filter values are case sensitive. For example, one of the values for a tag called ``Department`` might be ``Security`` . If you provide ``security`` as the filter value, then there's no match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-mapfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityhub as securityhub
                
                map_filter_property = securityhub.CfnAutomationRule.MapFilterProperty(
                    comparison="comparison",
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__91f36875bd267215fe022e63a4ce087a699536cdc1b9f8b3c84b53aa838e7074)
                check_type(argname="argument comparison", value=comparison, expected_type=type_hints["comparison"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "comparison": comparison,
                "key": key,
                "value": value,
            }

        @builtins.property
        def comparison(self) -> builtins.str:
            '''The condition to apply to the key value when filtering Security Hub findings with a map filter.

            To search for values that have the filter value, use one of the following comparison operators:

            - To search for values that include the filter value, use ``CONTAINS`` . For example, for the ``ResourceTags`` field, the filter ``Department CONTAINS Security`` matches findings that include the value ``Security`` for the ``Department`` tag. In the same example, a finding with a value of ``Security team`` for the ``Department`` tag is a match.
            - To search for values that exactly match the filter value, use ``EQUALS`` . For example, for the ``ResourceTags`` field, the filter ``Department EQUALS Security`` matches findings that have the value ``Security`` for the ``Department`` tag.

            ``CONTAINS`` and ``EQUALS`` filters on the same field are joined by ``OR`` . A finding matches if it matches any one of those filters. For example, the filters ``Department CONTAINS Security OR Department CONTAINS Finance`` match a finding that includes either ``Security`` , ``Finance`` , or both values.

            To search for values that don't have the filter value, use one of the following comparison operators:

            - To search for values that exclude the filter value, use ``NOT_CONTAINS`` . For example, for the ``ResourceTags`` field, the filter ``Department NOT_CONTAINS Finance`` matches findings that exclude the value ``Finance`` for the ``Department`` tag.
            - To search for values other than the filter value, use ``NOT_EQUALS`` . For example, for the ``ResourceTags`` field, the filter ``Department NOT_EQUALS Finance`` matches findings that don’t have the value ``Finance`` for the ``Department`` tag.

            ``NOT_CONTAINS`` and ``NOT_EQUALS`` filters on the same field are joined by ``AND`` . A finding matches only if it matches all of those filters. For example, the filters ``Department NOT_CONTAINS Security AND Department NOT_CONTAINS Finance`` match a finding that excludes both the ``Security`` and ``Finance`` values.

            ``CONTAINS`` filters can only be used with other ``CONTAINS`` filters. ``NOT_CONTAINS`` filters can only be used with other ``NOT_CONTAINS`` filters.

            You can’t have both a ``CONTAINS`` filter and a ``NOT_CONTAINS`` filter on the same field. Similarly, you can’t have both an ``EQUALS`` filter and a ``NOT_EQUALS`` filter on the same field. Combining filters in this way returns an error.

            ``CONTAINS`` and ``NOT_CONTAINS`` operators can be used only with automation rules. For more information, see `Automation rules <https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html>`_ in the *AWS Security Hub User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-mapfilter.html#cfn-securityhub-automationrule-mapfilter-comparison
            '''
            result = self._values.get("comparison")
            assert result is not None, "Required property 'comparison' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''The key of the map filter.

            For example, for ``ResourceTags`` , ``Key`` identifies the name of the tag. For ``UserDefinedFields`` , ``Key`` is the name of the field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-mapfilter.html#cfn-securityhub-automationrule-mapfilter-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value for the key in the map filter.

            Filter values are case sensitive. For example, one of the values for a tag called ``Department`` might be ``Security`` . If you provide ``security`` as the filter value, then there's no match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-mapfilter.html#cfn-securityhub-automationrule-mapfilter-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MapFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityhub.CfnAutomationRule.NoteUpdateProperty",
        jsii_struct_bases=[],
        name_mapping={"text": "text", "updated_by": "updatedBy"},
    )
    class NoteUpdateProperty:
        def __init__(self, *, text: builtins.str, updated_by: typing.Any) -> None:
            '''The updated note.

            :param text: The updated note text.
            :param updated_by: The principal that updated the note.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-noteupdate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityhub as securityhub
                
                # updated_by: Any
                
                note_update_property = securityhub.CfnAutomationRule.NoteUpdateProperty(
                    text="text",
                    updated_by=updated_by
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1f01ce6428aaccb76a4dd3111c6a58270f1129efa37f87f346378055261a8a01)
                check_type(argname="argument text", value=text, expected_type=type_hints["text"])
                check_type(argname="argument updated_by", value=updated_by, expected_type=type_hints["updated_by"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "text": text,
                "updated_by": updated_by,
            }

        @builtins.property
        def text(self) -> builtins.str:
            '''The updated note text.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-noteupdate.html#cfn-securityhub-automationrule-noteupdate-text
            '''
            result = self._values.get("text")
            assert result is not None, "Required property 'text' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def updated_by(self) -> typing.Any:
            '''The principal that updated the note.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-noteupdate.html#cfn-securityhub-automationrule-noteupdate-updatedby
            '''
            result = self._values.get("updated_by")
            assert result is not None, "Required property 'updated_by' is missing"
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NoteUpdateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityhub.CfnAutomationRule.NumberFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"eq": "eq", "gte": "gte", "lte": "lte"},
    )
    class NumberFilterProperty:
        def __init__(
            self,
            *,
            eq: typing.Optional[jsii.Number] = None,
            gte: typing.Optional[jsii.Number] = None,
            lte: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''A number filter for querying findings.

            :param eq: The equal-to condition to be applied to a single field when querying for findings.
            :param gte: The greater-than-equal condition to be applied to a single field when querying for findings.
            :param lte: The less-than-equal condition to be applied to a single field when querying for findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-numberfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityhub as securityhub
                
                number_filter_property = securityhub.CfnAutomationRule.NumberFilterProperty(
                    eq=123,
                    gte=123,
                    lte=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__000b578e595fbfb6609bb2cf3b90f42c91b01240906d31c22b9f1dd9869a214e)
                check_type(argname="argument eq", value=eq, expected_type=type_hints["eq"])
                check_type(argname="argument gte", value=gte, expected_type=type_hints["gte"])
                check_type(argname="argument lte", value=lte, expected_type=type_hints["lte"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if eq is not None:
                self._values["eq"] = eq
            if gte is not None:
                self._values["gte"] = gte
            if lte is not None:
                self._values["lte"] = lte

        @builtins.property
        def eq(self) -> typing.Optional[jsii.Number]:
            '''The equal-to condition to be applied to a single field when querying for findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-numberfilter.html#cfn-securityhub-automationrule-numberfilter-eq
            '''
            result = self._values.get("eq")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def gte(self) -> typing.Optional[jsii.Number]:
            '''The greater-than-equal condition to be applied to a single field when querying for findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-numberfilter.html#cfn-securityhub-automationrule-numberfilter-gte
            '''
            result = self._values.get("gte")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def lte(self) -> typing.Optional[jsii.Number]:
            '''The less-than-equal condition to be applied to a single field when querying for findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-numberfilter.html#cfn-securityhub-automationrule-numberfilter-lte
            '''
            result = self._values.get("lte")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NumberFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityhub.CfnAutomationRule.RelatedFindingProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id", "product_arn": "productArn"},
    )
    class RelatedFindingProperty:
        def __init__(self, *, id: typing.Any, product_arn: builtins.str) -> None:
            '''Provides details about a list of findings that the current finding relates to.

            :param id: The product-generated identifier for a related finding.
            :param product_arn: The Amazon Resource Name (ARN) for the product that generated a related finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-relatedfinding.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityhub as securityhub
                
                # id: Any
                
                related_finding_property = securityhub.CfnAutomationRule.RelatedFindingProperty(
                    id=id,
                    product_arn="productArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9df6b75e5070bcb08d999a08b3bd84da05079be466527b5ce60bbe470f59dd64)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument product_arn", value=product_arn, expected_type=type_hints["product_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
                "product_arn": product_arn,
            }

        @builtins.property
        def id(self) -> typing.Any:
            '''The product-generated identifier for a related finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-relatedfinding.html#cfn-securityhub-automationrule-relatedfinding-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def product_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) for the product that generated a related finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-relatedfinding.html#cfn-securityhub-automationrule-relatedfinding-productarn
            '''
            result = self._values.get("product_arn")
            assert result is not None, "Required property 'product_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RelatedFindingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityhub.CfnAutomationRule.SeverityUpdateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "label": "label",
            "normalized": "normalized",
            "product": "product",
        },
    )
    class SeverityUpdateProperty:
        def __init__(
            self,
            *,
            label: typing.Optional[builtins.str] = None,
            normalized: typing.Optional[jsii.Number] = None,
            product: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Updates to the severity information for a finding.

            :param label: The severity value of the finding. The allowed values are the following. - ``INFORMATIONAL`` - No issue was found. - ``LOW`` - The issue does not require action on its own. - ``MEDIUM`` - The issue must be addressed but not urgently. - ``HIGH`` - The issue must be addressed as a priority. - ``CRITICAL`` - The issue must be remediated immediately to avoid it escalating.
            :param normalized: The normalized severity for the finding. This attribute is to be deprecated in favor of ``Label`` . If you provide ``Normalized`` and do not provide ``Label`` , ``Label`` is set automatically as follows. - 0 - ``INFORMATIONAL`` - 1–39 - ``LOW`` - 40–69 - ``MEDIUM`` - 70–89 - ``HIGH`` - 90–100 - ``CRITICAL``
            :param product: The native severity as defined by the AWS service or integrated partner product that generated the finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-severityupdate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityhub as securityhub
                
                severity_update_property = securityhub.CfnAutomationRule.SeverityUpdateProperty(
                    label="label",
                    normalized=123,
                    product=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6ace3bf23a0eaa2083fc92b1b678856a77f120445f059b287841d7351fd7232b)
                check_type(argname="argument label", value=label, expected_type=type_hints["label"])
                check_type(argname="argument normalized", value=normalized, expected_type=type_hints["normalized"])
                check_type(argname="argument product", value=product, expected_type=type_hints["product"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if label is not None:
                self._values["label"] = label
            if normalized is not None:
                self._values["normalized"] = normalized
            if product is not None:
                self._values["product"] = product

        @builtins.property
        def label(self) -> typing.Optional[builtins.str]:
            '''The severity value of the finding. The allowed values are the following.

            - ``INFORMATIONAL`` - No issue was found.
            - ``LOW`` - The issue does not require action on its own.
            - ``MEDIUM`` - The issue must be addressed but not urgently.
            - ``HIGH`` - The issue must be addressed as a priority.
            - ``CRITICAL`` - The issue must be remediated immediately to avoid it escalating.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-severityupdate.html#cfn-securityhub-automationrule-severityupdate-label
            '''
            result = self._values.get("label")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def normalized(self) -> typing.Optional[jsii.Number]:
            '''The normalized severity for the finding. This attribute is to be deprecated in favor of ``Label`` .

            If you provide ``Normalized`` and do not provide ``Label`` , ``Label`` is set automatically as follows.

            - 0 - ``INFORMATIONAL``
            - 1–39 - ``LOW``
            - 40–69 - ``MEDIUM``
            - 70–89 - ``HIGH``
            - 90–100 - ``CRITICAL``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-severityupdate.html#cfn-securityhub-automationrule-severityupdate-normalized
            '''
            result = self._values.get("normalized")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def product(self) -> typing.Optional[jsii.Number]:
            '''The native severity as defined by the AWS service or integrated partner product that generated the finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-severityupdate.html#cfn-securityhub-automationrule-severityupdate-product
            '''
            result = self._values.get("product")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SeverityUpdateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityhub.CfnAutomationRule.StringFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"comparison": "comparison", "value": "value"},
    )
    class StringFilterProperty:
        def __init__(self, *, comparison: builtins.str, value: builtins.str) -> None:
            '''A string filter for filtering AWS Security Hub findings.

            :param comparison: The condition to apply to a string value when filtering Security Hub findings. To search for values that have the filter value, use one of the following comparison operators: - To search for values that include the filter value, use ``CONTAINS`` . For example, the filter ``Title CONTAINS CloudFront`` matches findings that have a ``Title`` that includes the string CloudFront. - To search for values that exactly match the filter value, use ``EQUALS`` . For example, the filter ``AwsAccountId EQUALS 123456789012`` only matches findings that have an account ID of ``123456789012`` . - To search for values that start with the filter value, use ``PREFIX`` . For example, the filter ``ResourceRegion PREFIX us`` matches findings that have a ``ResourceRegion`` that starts with ``us`` . A ``ResourceRegion`` that starts with a different value, such as ``af`` , ``ap`` , or ``ca`` , doesn't match. ``CONTAINS`` , ``EQUALS`` , and ``PREFIX`` filters on the same field are joined by ``OR`` . A finding matches if it matches any one of those filters. For example, the filters ``Title CONTAINS CloudFront OR Title CONTAINS CloudWatch`` match a finding that includes either ``CloudFront`` , ``CloudWatch`` , or both strings in the title. To search for values that don’t have the filter value, use one of the following comparison operators: - To search for values that exclude the filter value, use ``NOT_CONTAINS`` . For example, the filter ``Title NOT_CONTAINS CloudFront`` matches findings that have a ``Title`` that excludes the string CloudFront. - To search for values other than the filter value, use ``NOT_EQUALS`` . For example, the filter ``AwsAccountId NOT_EQUALS 123456789012`` only matches findings that have an account ID other than ``123456789012`` . - To search for values that don't start with the filter value, use ``PREFIX_NOT_EQUALS`` . For example, the filter ``ResourceRegion PREFIX_NOT_EQUALS us`` matches findings with a ``ResourceRegion`` that starts with a value other than ``us`` . ``NOT_CONTAINS`` , ``NOT_EQUALS`` , and ``PREFIX_NOT_EQUALS`` filters on the same field are joined by ``AND`` . A finding matches only if it matches all of those filters. For example, the filters ``Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch`` match a finding that excludes both ``CloudFront`` and ``CloudWatch`` in the title. You can’t have both a ``CONTAINS`` filter and a ``NOT_CONTAINS`` filter on the same field. Similarly, you can't provide both an ``EQUALS`` filter and a ``NOT_EQUALS`` or ``PREFIX_NOT_EQUALS`` filter on the same field. Combining filters in this way returns an error. ``CONTAINS`` filters can only be used with other ``CONTAINS`` filters. ``NOT_CONTAINS`` filters can only be used with other ``NOT_CONTAINS`` filters. You can combine ``PREFIX`` filters with ``NOT_EQUALS`` or ``PREFIX_NOT_EQUALS`` filters for the same field. Security Hub first processes the ``PREFIX`` filters, and then the ``NOT_EQUALS`` or ``PREFIX_NOT_EQUALS`` filters. For example, for the following filters, Security Hub first identifies findings that have resource types that start with either ``AwsIam`` or ``AwsEc2`` . It then excludes findings that have a resource type of ``AwsIamPolicy`` and findings that have a resource type of ``AwsEc2NetworkInterface`` . - ``ResourceType PREFIX AwsIam`` - ``ResourceType PREFIX AwsEc2`` - ``ResourceType NOT_EQUALS AwsIamPolicy`` - ``ResourceType NOT_EQUALS AwsEc2NetworkInterface`` ``CONTAINS`` and ``NOT_CONTAINS`` operators can be used only with automation rules. For more information, see `Automation rules <https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html>`_ in the *AWS Security Hub User Guide* .
            :param value: The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is ``Security Hub`` . If you provide ``security hub`` as the filter value, there's no match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-stringfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityhub as securityhub
                
                string_filter_property = securityhub.CfnAutomationRule.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7823f53010fc7a0056009b7cd0b999565e169d405ec7bb2b879614bff4f5f676)
                check_type(argname="argument comparison", value=comparison, expected_type=type_hints["comparison"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "comparison": comparison,
                "value": value,
            }

        @builtins.property
        def comparison(self) -> builtins.str:
            '''The condition to apply to a string value when filtering Security Hub findings.

            To search for values that have the filter value, use one of the following comparison operators:

            - To search for values that include the filter value, use ``CONTAINS`` . For example, the filter ``Title CONTAINS CloudFront`` matches findings that have a ``Title`` that includes the string CloudFront.
            - To search for values that exactly match the filter value, use ``EQUALS`` . For example, the filter ``AwsAccountId EQUALS 123456789012`` only matches findings that have an account ID of ``123456789012`` .
            - To search for values that start with the filter value, use ``PREFIX`` . For example, the filter ``ResourceRegion PREFIX us`` matches findings that have a ``ResourceRegion`` that starts with ``us`` . A ``ResourceRegion`` that starts with a different value, such as ``af`` , ``ap`` , or ``ca`` , doesn't match.

            ``CONTAINS`` , ``EQUALS`` , and ``PREFIX`` filters on the same field are joined by ``OR`` . A finding matches if it matches any one of those filters. For example, the filters ``Title CONTAINS CloudFront OR Title CONTAINS CloudWatch`` match a finding that includes either ``CloudFront`` , ``CloudWatch`` , or both strings in the title.

            To search for values that don’t have the filter value, use one of the following comparison operators:

            - To search for values that exclude the filter value, use ``NOT_CONTAINS`` . For example, the filter ``Title NOT_CONTAINS CloudFront`` matches findings that have a ``Title`` that excludes the string CloudFront.
            - To search for values other than the filter value, use ``NOT_EQUALS`` . For example, the filter ``AwsAccountId NOT_EQUALS 123456789012`` only matches findings that have an account ID other than ``123456789012`` .
            - To search for values that don't start with the filter value, use ``PREFIX_NOT_EQUALS`` . For example, the filter ``ResourceRegion PREFIX_NOT_EQUALS us`` matches findings with a ``ResourceRegion`` that starts with a value other than ``us`` .

            ``NOT_CONTAINS`` , ``NOT_EQUALS`` , and ``PREFIX_NOT_EQUALS`` filters on the same field are joined by ``AND`` . A finding matches only if it matches all of those filters. For example, the filters ``Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch`` match a finding that excludes both ``CloudFront`` and ``CloudWatch`` in the title.

            You can’t have both a ``CONTAINS`` filter and a ``NOT_CONTAINS`` filter on the same field. Similarly, you can't provide both an ``EQUALS`` filter and a ``NOT_EQUALS`` or ``PREFIX_NOT_EQUALS`` filter on the same field. Combining filters in this way returns an error. ``CONTAINS`` filters can only be used with other ``CONTAINS`` filters. ``NOT_CONTAINS`` filters can only be used with other ``NOT_CONTAINS`` filters.

            You can combine ``PREFIX`` filters with ``NOT_EQUALS`` or ``PREFIX_NOT_EQUALS`` filters for the same field. Security Hub first processes the ``PREFIX`` filters, and then the ``NOT_EQUALS`` or ``PREFIX_NOT_EQUALS`` filters.

            For example, for the following filters, Security Hub first identifies findings that have resource types that start with either ``AwsIam`` or ``AwsEc2`` . It then excludes findings that have a resource type of ``AwsIamPolicy`` and findings that have a resource type of ``AwsEc2NetworkInterface`` .

            - ``ResourceType PREFIX AwsIam``
            - ``ResourceType PREFIX AwsEc2``
            - ``ResourceType NOT_EQUALS AwsIamPolicy``
            - ``ResourceType NOT_EQUALS AwsEc2NetworkInterface``

            ``CONTAINS`` and ``NOT_CONTAINS`` operators can be used only with automation rules. For more information, see `Automation rules <https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html>`_ in the *AWS Security Hub User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-stringfilter.html#cfn-securityhub-automationrule-stringfilter-comparison
            '''
            result = self._values.get("comparison")
            assert result is not None, "Required property 'comparison' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The string filter value.

            Filter values are case sensitive. For example, the product name for control-based findings is ``Security Hub`` . If you provide ``security hub`` as the filter value, there's no match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-stringfilter.html#cfn-securityhub-automationrule-stringfilter-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StringFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityhub.CfnAutomationRule.WorkflowUpdateProperty",
        jsii_struct_bases=[],
        name_mapping={"status": "status"},
    )
    class WorkflowUpdateProperty:
        def __init__(self, *, status: builtins.str) -> None:
            '''Used to update information about the investigation into the finding.

            :param status: The status of the investigation into the finding. The workflow status is specific to an individual finding. It does not affect the generation of new findings. For example, setting the workflow status to ``SUPPRESSED`` or ``RESOLVED`` does not prevent a new finding for the same issue. The allowed values are the following. - ``NEW`` - The initial state of a finding, before it is reviewed. Security Hub also resets ``WorkFlowStatus`` from ``NOTIFIED`` or ``RESOLVED`` to ``NEW`` in the following cases: - The record state changes from ``ARCHIVED`` to ``ACTIVE`` . - The compliance status changes from ``PASSED`` to either ``WARNING`` , ``FAILED`` , or ``NOT_AVAILABLE`` . - ``NOTIFIED`` - Indicates that you notified the resource owner about the security issue. Used when the initial reviewer is not the resource owner, and needs intervention from the resource owner. - ``RESOLVED`` - The finding was reviewed and remediated and is now considered resolved. - ``SUPPRESSED`` - Indicates that you reviewed the finding and do not believe that any action is needed. The finding is no longer updated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-workflowupdate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityhub as securityhub
                
                workflow_update_property = securityhub.CfnAutomationRule.WorkflowUpdateProperty(
                    status="status"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e47be336b722bb880cce3edf7d5752dceac8f243282fcb2bc5094d82b71dc6b8)
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "status": status,
            }

        @builtins.property
        def status(self) -> builtins.str:
            '''The status of the investigation into the finding.

            The workflow status is specific to an individual finding. It does not affect the generation of new findings. For example, setting the workflow status to ``SUPPRESSED`` or ``RESOLVED`` does not prevent a new finding for the same issue.

            The allowed values are the following.

            - ``NEW`` - The initial state of a finding, before it is reviewed.

            Security Hub also resets ``WorkFlowStatus`` from ``NOTIFIED`` or ``RESOLVED`` to ``NEW`` in the following cases:

            - The record state changes from ``ARCHIVED`` to ``ACTIVE`` .
            - The compliance status changes from ``PASSED`` to either ``WARNING`` , ``FAILED`` , or ``NOT_AVAILABLE`` .
            - ``NOTIFIED`` - Indicates that you notified the resource owner about the security issue. Used when the initial reviewer is not the resource owner, and needs intervention from the resource owner.
            - ``RESOLVED`` - The finding was reviewed and remediated and is now considered resolved.
            - ``SUPPRESSED`` - Indicates that you reviewed the finding and do not believe that any action is needed. The finding is no longer updated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-workflowupdate.html#cfn-securityhub-automationrule-workflowupdate-status
            '''
            result = self._values.get("status")
            assert result is not None, "Required property 'status' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkflowUpdateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_securityhub.CfnAutomationRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "actions": "actions",
        "criteria": "criteria",
        "description": "description",
        "is_terminal": "isTerminal",
        "rule_name": "ruleName",
        "rule_order": "ruleOrder",
        "rule_status": "ruleStatus",
        "tags": "tags",
    },
)
class CfnAutomationRuleProps:
    def __init__(
        self,
        *,
        actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.AutomationRulesActionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        criteria: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.AutomationRulesFindingFiltersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        is_terminal: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        rule_name: typing.Optional[builtins.str] = None,
        rule_order: typing.Optional[jsii.Number] = None,
        rule_status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAutomationRule``.

        :param actions: One or more actions to update finding fields if a finding matches the defined criteria of the rule.
        :param criteria: A set of `AWS Security Finding Format <https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html>`_ finding field attributes and corresponding expected values that Security Hub uses to filter findings. If a rule is enabled and a finding matches the conditions specified in this parameter, Security Hub applies the rule action to the finding.
        :param description: A description of the rule.
        :param is_terminal: Specifies whether a rule is the last to be applied with respect to a finding that matches the rule criteria. This is useful when a finding matches the criteria for multiple rules, and each rule has different actions. If a rule is terminal, Security Hub applies the rule action to a finding that matches the rule criteria and doesn't evaluate other rules for the finding. By default, a rule isn't terminal.
        :param rule_name: The name of the rule.
        :param rule_order: An integer ranging from 1 to 1000 that represents the order in which the rule action is applied to findings. Security Hub applies rules with lower values for this parameter first.
        :param rule_status: Whether the rule is active after it is created. If this parameter is equal to ``ENABLED`` , Security Hub applies the rule to findings and finding updates after the rule is created.
        :param tags: User-defined tags that help you label the purpose of a rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-automationrule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_securityhub as securityhub
            
            # id: Any
            # updated_by: Any
            
            cfn_automation_rule_props = securityhub.CfnAutomationRuleProps(
                actions=[securityhub.CfnAutomationRule.AutomationRulesActionProperty(
                    finding_fields_update=securityhub.CfnAutomationRule.AutomationRulesFindingFieldsUpdateProperty(
                        confidence=123,
                        criticality=123,
                        note=securityhub.CfnAutomationRule.NoteUpdateProperty(
                            text="text",
                            updated_by=updated_by
                        ),
                        related_findings=[securityhub.CfnAutomationRule.RelatedFindingProperty(
                            id=id,
                            product_arn="productArn"
                        )],
                        severity=securityhub.CfnAutomationRule.SeverityUpdateProperty(
                            label="label",
                            normalized=123,
                            product=123
                        ),
                        types=["types"],
                        user_defined_fields={
                            "user_defined_fields_key": "userDefinedFields"
                        },
                        verification_state="verificationState",
                        workflow=securityhub.CfnAutomationRule.WorkflowUpdateProperty(
                            status="status"
                        )
                    ),
                    type="type"
                )],
                criteria=securityhub.CfnAutomationRule.AutomationRulesFindingFiltersProperty(
                    aws_account_id=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    company_name=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    compliance_associated_standards_id=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    compliance_security_control_id=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    compliance_status=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    confidence=[securityhub.CfnAutomationRule.NumberFilterProperty(
                        eq=123,
                        gte=123,
                        lte=123
                    )],
                    created_at=[securityhub.CfnAutomationRule.DateFilterProperty(
                        date_range=securityhub.CfnAutomationRule.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    criticality=[securityhub.CfnAutomationRule.NumberFilterProperty(
                        eq=123,
                        gte=123,
                        lte=123
                    )],
                    description=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    first_observed_at=[securityhub.CfnAutomationRule.DateFilterProperty(
                        date_range=securityhub.CfnAutomationRule.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    generator_id=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    id=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    last_observed_at=[securityhub.CfnAutomationRule.DateFilterProperty(
                        date_range=securityhub.CfnAutomationRule.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    note_text=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    note_updated_at=[securityhub.CfnAutomationRule.DateFilterProperty(
                        date_range=securityhub.CfnAutomationRule.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    note_updated_by=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    product_arn=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    product_name=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    record_state=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    related_findings_id=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    related_findings_product_arn=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_details_other=[securityhub.CfnAutomationRule.MapFilterProperty(
                        comparison="comparison",
                        key="key",
                        value="value"
                    )],
                    resource_id=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_partition=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_region=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_tags=[securityhub.CfnAutomationRule.MapFilterProperty(
                        comparison="comparison",
                        key="key",
                        value="value"
                    )],
                    resource_type=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    severity_label=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    source_url=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    title=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    type=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    updated_at=[securityhub.CfnAutomationRule.DateFilterProperty(
                        date_range=securityhub.CfnAutomationRule.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    user_defined_fields=[securityhub.CfnAutomationRule.MapFilterProperty(
                        comparison="comparison",
                        key="key",
                        value="value"
                    )],
                    verification_state=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    workflow_status=[securityhub.CfnAutomationRule.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )]
                ),
                description="description",
                is_terminal=False,
                rule_name="ruleName",
                rule_order=123,
                rule_status="ruleStatus",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__221241b44c93ea569fcf69aaaade0ce7cf31b7343bc3d072d74ccd16895d9a2d)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument criteria", value=criteria, expected_type=type_hints["criteria"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument is_terminal", value=is_terminal, expected_type=type_hints["is_terminal"])
            check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            check_type(argname="argument rule_order", value=rule_order, expected_type=type_hints["rule_order"])
            check_type(argname="argument rule_status", value=rule_status, expected_type=type_hints["rule_status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if actions is not None:
            self._values["actions"] = actions
        if criteria is not None:
            self._values["criteria"] = criteria
        if description is not None:
            self._values["description"] = description
        if is_terminal is not None:
            self._values["is_terminal"] = is_terminal
        if rule_name is not None:
            self._values["rule_name"] = rule_name
        if rule_order is not None:
            self._values["rule_order"] = rule_order
        if rule_status is not None:
            self._values["rule_status"] = rule_status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def actions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAutomationRule.AutomationRulesActionProperty]]]]:
        '''One or more actions to update finding fields if a finding matches the defined criteria of the rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-automationrule.html#cfn-securityhub-automationrule-actions
        '''
        result = self._values.get("actions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAutomationRule.AutomationRulesActionProperty]]]], result)

    @builtins.property
    def criteria(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAutomationRule.AutomationRulesFindingFiltersProperty]]:
        '''A set of `AWS Security Finding Format <https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html>`_ finding field attributes and corresponding expected values that Security Hub uses to filter findings. If a rule is enabled and a finding matches the conditions specified in this parameter, Security Hub applies the rule action to the finding.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-automationrule.html#cfn-securityhub-automationrule-criteria
        '''
        result = self._values.get("criteria")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAutomationRule.AutomationRulesFindingFiltersProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-automationrule.html#cfn-securityhub-automationrule-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_terminal(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether a rule is the last to be applied with respect to a finding that matches the rule criteria.

        This is useful when a finding matches the criteria for multiple rules, and each rule has different actions. If a rule is terminal, Security Hub applies the rule action to a finding that matches the rule criteria and doesn't evaluate other rules for the finding. By default, a rule isn't terminal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-automationrule.html#cfn-securityhub-automationrule-isterminal
        '''
        result = self._values.get("is_terminal")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def rule_name(self) -> typing.Optional[builtins.str]:
        '''The name of the rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-automationrule.html#cfn-securityhub-automationrule-rulename
        '''
        result = self._values.get("rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule_order(self) -> typing.Optional[jsii.Number]:
        '''An integer ranging from 1 to 1000 that represents the order in which the rule action is applied to findings.

        Security Hub applies rules with lower values for this parameter first.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-automationrule.html#cfn-securityhub-automationrule-ruleorder
        '''
        result = self._values.get("rule_order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def rule_status(self) -> typing.Optional[builtins.str]:
        '''Whether the rule is active after it is created.

        If this parameter is equal to ``ENABLED`` , Security Hub applies the rule to findings and finding updates after the rule is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-automationrule.html#cfn-securityhub-automationrule-rulestatus
        '''
        result = self._values.get("rule_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''User-defined tags that help you label the purpose of a rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-automationrule.html#cfn-securityhub-automationrule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAutomationRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnHub(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_securityhub.CfnHub",
):
    '''The ``AWS::SecurityHub::Hub`` resource specifies the enablement of the AWS Security Hub service in your AWS account .

    The service is enabled in the current AWS Region or the specified Region. You create a separate ``Hub`` resource in each Region in which you want to enable Security Hub .

    When you use this resource to enable Security Hub , default security standards are enabled. To disable default standards, set the ``EnableDefaultStandards`` property to ``false`` . You can use the ```AWS::SecurityHub::Standard`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-standard.html>`_ resource to enable additional standards.

    When you use this resource to enable Security Hub , new controls are automatically enabled for your enabled standards. To disable automatic enablement of new controls, set the ``AutoEnableControls`` property to ``false`` .

    You must create an ``AWS::SecurityHub::Hub`` resource for an account before you can create other types of Security Hub resources for the account through AWS CloudFormation . Use a `DependsOn attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html>`_ , such as ``"DependsOn": "Hub"`` , to ensure that you've created an ``AWS::SecurityHub::Hub`` resource before creating other Security Hub resources for an account.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-hub.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_securityhub as securityhub
        
        # tags: Any
        
        cfn_hub = securityhub.CfnHub(self, "MyCfnHub",
            auto_enable_controls=False,
            control_finding_generator="controlFindingGenerator",
            enable_default_standards=False,
            tags=tags
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        auto_enable_controls: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        control_finding_generator: typing.Optional[builtins.str] = None,
        enable_default_standards: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param auto_enable_controls: Whether to automatically enable new controls when they are added to standards that are enabled. By default, this is set to ``true`` , and new controls are enabled automatically. To not automatically enable new controls, set this to ``false`` .
        :param control_finding_generator: Specifies whether an account has consolidated control findings turned on or off. If the value for this field is set to ``SECURITY_CONTROL`` , Security Hub generates a single finding for a control check even when the check applies to multiple enabled standards. If the value for this field is set to ``STANDARD_CONTROL`` , Security Hub generates separate findings for a control check when the check applies to multiple enabled standards. The value for this field in a member account matches the value in the administrator account. For accounts that aren't part of an organization, the default value of this field is ``SECURITY_CONTROL`` if you enabled Security Hub on or after February 23, 2023.
        :param enable_default_standards: Whether to enable the security standards that Security Hub has designated as automatically enabled. If you don't provide a value for ``EnableDefaultStandards`` , it is set to ``true`` , and the designated standards are automatically enabled in each AWS Region where you enable Security Hub . If you don't want to enable the designated standards, set ``EnableDefaultStandards`` to ``false`` . Currently, the automatically enabled standards are the Center for Internet Security (CIS) AWS Foundations Benchmark v1.2.0 and AWS Foundational Security Best Practices (FSBP).
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5258d6906cbc8ea3b7ed82ec2c832e2751a0a1255445e6f3e81ea5935e2defb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnHubProps(
            auto_enable_controls=auto_enable_controls,
            control_finding_generator=control_finding_generator,
            enable_default_standards=enable_default_standards,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afc1b02284691f4fac4c50413d7e6e3c86b4db4f8702643ba4c85dd68b5cb0b4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__db4b61e6830fa5a7557c941ad1ea7690d59d4d1ea7c453b10a17081c25ba2e27)
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
    @jsii.member(jsii_name="autoEnableControls")
    def auto_enable_controls(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to automatically enable new controls when they are added to standards that are enabled.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "autoEnableControls"))

    @auto_enable_controls.setter
    def auto_enable_controls(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8111fb2c58ed3e1e0c85928b084d60f2c8b02b604055e3087ce38f249967a54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoEnableControls", value)

    @builtins.property
    @jsii.member(jsii_name="controlFindingGenerator")
    def control_finding_generator(self) -> typing.Optional[builtins.str]:
        '''Specifies whether an account has consolidated control findings turned on or off.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "controlFindingGenerator"))

    @control_finding_generator.setter
    def control_finding_generator(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6647ce06efe713d1b36ec98af92808e5bf616a683fa68b2fb4fe64fafe92bf35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "controlFindingGenerator", value)

    @builtins.property
    @jsii.member(jsii_name="enableDefaultStandards")
    def enable_default_standards(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to enable the security standards that Security Hub has designated as automatically enabled.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enableDefaultStandards"))

    @enable_default_standards.setter
    def enable_default_standards(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d118847a7bb58b794458a6afe88e0a8324a3a4e1590aba4f028de455ee8c624)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableDefaultStandards", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e17fb796b4e0971555823ae1c97a99f19e5677ae303ff0ef984cd00ac919ea87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_securityhub.CfnHubProps",
    jsii_struct_bases=[],
    name_mapping={
        "auto_enable_controls": "autoEnableControls",
        "control_finding_generator": "controlFindingGenerator",
        "enable_default_standards": "enableDefaultStandards",
        "tags": "tags",
    },
)
class CfnHubProps:
    def __init__(
        self,
        *,
        auto_enable_controls: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        control_finding_generator: typing.Optional[builtins.str] = None,
        enable_default_standards: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnHub``.

        :param auto_enable_controls: Whether to automatically enable new controls when they are added to standards that are enabled. By default, this is set to ``true`` , and new controls are enabled automatically. To not automatically enable new controls, set this to ``false`` .
        :param control_finding_generator: Specifies whether an account has consolidated control findings turned on or off. If the value for this field is set to ``SECURITY_CONTROL`` , Security Hub generates a single finding for a control check even when the check applies to multiple enabled standards. If the value for this field is set to ``STANDARD_CONTROL`` , Security Hub generates separate findings for a control check when the check applies to multiple enabled standards. The value for this field in a member account matches the value in the administrator account. For accounts that aren't part of an organization, the default value of this field is ``SECURITY_CONTROL`` if you enabled Security Hub on or after February 23, 2023.
        :param enable_default_standards: Whether to enable the security standards that Security Hub has designated as automatically enabled. If you don't provide a value for ``EnableDefaultStandards`` , it is set to ``true`` , and the designated standards are automatically enabled in each AWS Region where you enable Security Hub . If you don't want to enable the designated standards, set ``EnableDefaultStandards`` to ``false`` . Currently, the automatically enabled standards are the Center for Internet Security (CIS) AWS Foundations Benchmark v1.2.0 and AWS Foundational Security Best Practices (FSBP).
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-hub.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_securityhub as securityhub
            
            # tags: Any
            
            cfn_hub_props = securityhub.CfnHubProps(
                auto_enable_controls=False,
                control_finding_generator="controlFindingGenerator",
                enable_default_standards=False,
                tags=tags
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a38c34c1f2742403521eb4af2098475d7afb878d3f9aba37048ae543b43e29c)
            check_type(argname="argument auto_enable_controls", value=auto_enable_controls, expected_type=type_hints["auto_enable_controls"])
            check_type(argname="argument control_finding_generator", value=control_finding_generator, expected_type=type_hints["control_finding_generator"])
            check_type(argname="argument enable_default_standards", value=enable_default_standards, expected_type=type_hints["enable_default_standards"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auto_enable_controls is not None:
            self._values["auto_enable_controls"] = auto_enable_controls
        if control_finding_generator is not None:
            self._values["control_finding_generator"] = control_finding_generator
        if enable_default_standards is not None:
            self._values["enable_default_standards"] = enable_default_standards
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def auto_enable_controls(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to automatically enable new controls when they are added to standards that are enabled.

        By default, this is set to ``true`` , and new controls are enabled automatically. To not automatically enable new controls, set this to ``false`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-hub.html#cfn-securityhub-hub-autoenablecontrols
        '''
        result = self._values.get("auto_enable_controls")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def control_finding_generator(self) -> typing.Optional[builtins.str]:
        '''Specifies whether an account has consolidated control findings turned on or off.

        If the value for this field is set to ``SECURITY_CONTROL`` , Security Hub generates a single finding for a control check even when the check applies to multiple enabled standards.

        If the value for this field is set to ``STANDARD_CONTROL`` , Security Hub generates separate findings for a control check when the check applies to multiple enabled standards.

        The value for this field in a member account matches the value in the administrator account. For accounts that aren't part of an organization, the default value of this field is ``SECURITY_CONTROL`` if you enabled Security Hub on or after February 23, 2023.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-hub.html#cfn-securityhub-hub-controlfindinggenerator
        '''
        result = self._values.get("control_finding_generator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_default_standards(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Whether to enable the security standards that Security Hub has designated as automatically enabled.

        If you don't provide a value for ``EnableDefaultStandards`` , it is set to ``true`` , and the designated standards are automatically enabled in each AWS Region where you enable Security Hub . If you don't want to enable the designated standards, set ``EnableDefaultStandards`` to ``false`` .

        Currently, the automatically enabled standards are the Center for Internet Security (CIS) AWS Foundations Benchmark v1.2.0 and AWS Foundational Security Best Practices (FSBP).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-hub.html#cfn-securityhub-hub-enabledefaultstandards
        '''
        result = self._values.get("enable_default_standards")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-hub.html#cfn-securityhub-hub-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHubProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnStandard(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_securityhub.CfnStandard",
):
    '''The ``AWS::SecurityHub::Standard`` resource specifies the enablement of a security standard.

    The standard is identified by the ``StandardsArn`` property. To view a list of Security Hub standards and their Amazon Resource Names (ARNs), use the ```DescribeStandards`` <https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html>`_ API operation.

    You must create a separate ``AWS::SecurityHub::Standard`` resource for each standard that you want to enable.

    For more information about Security Hub standards, see `Security Hub standards reference <https://docs.aws.amazon.com/securityhub/latest/userguide/standards-reference.html>`_ in the *AWS Security Hub User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-standard.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_securityhub as securityhub
        
        cfn_standard = securityhub.CfnStandard(self, "MyCfnStandard",
            standards_arn="standardsArn",
        
            # the properties below are optional
            disabled_standards_controls=[securityhub.CfnStandard.StandardsControlProperty(
                standards_control_arn="standardsControlArn",
        
                # the properties below are optional
                reason="reason"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        standards_arn: builtins.str,
        disabled_standards_controls: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStandard.StandardsControlProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param standards_arn: The ARN of the standard that you want to enable. To view a list of available Security Hub standards and their ARNs, use the ```DescribeStandards`` <https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html>`_ API operation.
        :param disabled_standards_controls: Specifies which controls are to be disabled in a standard. *Maximum* : ``100``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__561d4df3cc67420b6eb1bedde6e0c0dfd6f3e64e2787adbaf250b63890914f1f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStandardProps(
            standards_arn=standards_arn,
            disabled_standards_controls=disabled_standards_controls,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41379479f5bf8cc9e157587f8663e5fa189d44fccbb0d2903f35086cf4fd639f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f1c025435faf1ab429f76ae44cb8672e4fe14ba11bbe310487d6a3a6bd53ae7e)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrStandardsSubscriptionArn")
    def attr_standards_subscription_arn(self) -> builtins.str:
        '''The ARN of a resource that represents your subscription to a supported standard.

        :cloudformationAttribute: StandardsSubscriptionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStandardsSubscriptionArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="standardsArn")
    def standards_arn(self) -> builtins.str:
        '''The ARN of the standard that you want to enable.'''
        return typing.cast(builtins.str, jsii.get(self, "standardsArn"))

    @standards_arn.setter
    def standards_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f003fbeecd432c822b1f4490f85902feb985eef57ec347d64e831f0a337b479)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "standardsArn", value)

    @builtins.property
    @jsii.member(jsii_name="disabledStandardsControls")
    def disabled_standards_controls(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStandard.StandardsControlProperty"]]]]:
        '''Specifies which controls are to be disabled in a standard.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStandard.StandardsControlProperty"]]]], jsii.get(self, "disabledStandardsControls"))

    @disabled_standards_controls.setter
    def disabled_standards_controls(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStandard.StandardsControlProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e923480bf5c5fa4fccb5bf4b4fb34ecf10ca3accba9f2a4f7b1b6ad7ad9437c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabledStandardsControls", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityhub.CfnStandard.StandardsControlProperty",
        jsii_struct_bases=[],
        name_mapping={
            "standards_control_arn": "standardsControlArn",
            "reason": "reason",
        },
    )
    class StandardsControlProperty:
        def __init__(
            self,
            *,
            standards_control_arn: builtins.str,
            reason: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides details about an individual security control.

            For a list of Security Hub controls, see `Security Hub controls reference <https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-controls-reference.html>`_ in the *AWS Security Hub User Guide* .

            :param standards_control_arn: The Amazon Resource Name (ARN) of the control.
            :param reason: A user-defined reason for changing a control's enablement status in a specified standard. If you are disabling a control, then this property is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-standard-standardscontrol.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityhub as securityhub
                
                standards_control_property = securityhub.CfnStandard.StandardsControlProperty(
                    standards_control_arn="standardsControlArn",
                
                    # the properties below are optional
                    reason="reason"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6ef5462ffb9eee57944c11caa687907b4e26d622e7e133c3335b59694bfcc483)
                check_type(argname="argument standards_control_arn", value=standards_control_arn, expected_type=type_hints["standards_control_arn"])
                check_type(argname="argument reason", value=reason, expected_type=type_hints["reason"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "standards_control_arn": standards_control_arn,
            }
            if reason is not None:
                self._values["reason"] = reason

        @builtins.property
        def standards_control_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the control.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-standard-standardscontrol.html#cfn-securityhub-standard-standardscontrol-standardscontrolarn
            '''
            result = self._values.get("standards_control_arn")
            assert result is not None, "Required property 'standards_control_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def reason(self) -> typing.Optional[builtins.str]:
            '''A user-defined reason for changing a control's enablement status in a specified standard.

            If you are disabling a control, then this property is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-standard-standardscontrol.html#cfn-securityhub-standard-standardscontrol-reason
            '''
            result = self._values.get("reason")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StandardsControlProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_securityhub.CfnStandardProps",
    jsii_struct_bases=[],
    name_mapping={
        "standards_arn": "standardsArn",
        "disabled_standards_controls": "disabledStandardsControls",
    },
)
class CfnStandardProps:
    def __init__(
        self,
        *,
        standards_arn: builtins.str,
        disabled_standards_controls: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStandard.StandardsControlProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnStandard``.

        :param standards_arn: The ARN of the standard that you want to enable. To view a list of available Security Hub standards and their ARNs, use the ```DescribeStandards`` <https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html>`_ API operation.
        :param disabled_standards_controls: Specifies which controls are to be disabled in a standard. *Maximum* : ``100``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-standard.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_securityhub as securityhub
            
            cfn_standard_props = securityhub.CfnStandardProps(
                standards_arn="standardsArn",
            
                # the properties below are optional
                disabled_standards_controls=[securityhub.CfnStandard.StandardsControlProperty(
                    standards_control_arn="standardsControlArn",
            
                    # the properties below are optional
                    reason="reason"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c125ac887ee3a111d19b82adf6b2639cf7fa812a424f7c788a920efcfdf1c39)
            check_type(argname="argument standards_arn", value=standards_arn, expected_type=type_hints["standards_arn"])
            check_type(argname="argument disabled_standards_controls", value=disabled_standards_controls, expected_type=type_hints["disabled_standards_controls"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "standards_arn": standards_arn,
        }
        if disabled_standards_controls is not None:
            self._values["disabled_standards_controls"] = disabled_standards_controls

    @builtins.property
    def standards_arn(self) -> builtins.str:
        '''The ARN of the standard that you want to enable.

        To view a list of available Security Hub standards and their ARNs, use the ```DescribeStandards`` <https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html>`_ API operation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-standard.html#cfn-securityhub-standard-standardsarn
        '''
        result = self._values.get("standards_arn")
        assert result is not None, "Required property 'standards_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disabled_standards_controls(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStandard.StandardsControlProperty]]]]:
        '''Specifies which controls are to be disabled in a standard.

        *Maximum* : ``100``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-standard.html#cfn-securityhub-standard-disabledstandardscontrols
        '''
        result = self._values.get("disabled_standards_controls")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStandard.StandardsControlProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStandardProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAutomationRule",
    "CfnAutomationRuleProps",
    "CfnHub",
    "CfnHubProps",
    "CfnStandard",
    "CfnStandardProps",
]

publication.publish()

def _typecheckingstub__90c663d2946359b509542feafdcb3d89f11ca9e30a214aae02ea3d6b354c9846(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.AutomationRulesActionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    criteria: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.AutomationRulesFindingFiltersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    is_terminal: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    rule_name: typing.Optional[builtins.str] = None,
    rule_order: typing.Optional[jsii.Number] = None,
    rule_status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae48eeaea63d372697a62c6052793e6367e3201b42f9513f1f0132b59dc350b0(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc6a8a522560219490822e00b9ec3810152de6616cf975f073c37fc9d8af31fc(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90988dc6b536563439917056373f7379ca48a864b5a3471a7b3552f6c9b40897(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAutomationRule.AutomationRulesActionProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc91daff88300654f2c8a9e4e5aad76fd0c26ae9c62e118febc7d1bff9733c5f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAutomationRule.AutomationRulesFindingFiltersProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13e710145ba6564ce42bac7fc3465ec7406a15699f473acd70e62bf605c1f259(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11031a77a18a3180e3bf703420372155750c7001d9c920558ff50230e0111537(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffff694fc9dee0bbe561a13e56455e4e3a3b12c8c47e7c20a7fe2e8c13c0725c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db37e60211fd885d4c7d0aa9af521faa3786061d7fa1712b86f54f3646a4738b(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0c77fc16c58c2d94764bb0b74df80e4884ec2c3948c0a364a0d9c75a4e9c79a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a7d0579ca491d9adc050f0e2036942728d9db8e3d190f067473714a8ce9fd4b(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d50f418e733dbb988d29d8dcedccc6faf2d022e32893189d084bb04a8c231ba(
    *,
    finding_fields_update: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.AutomationRulesFindingFieldsUpdateProperty, typing.Dict[builtins.str, typing.Any]]],
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46649258d4db7d36012fa064d0d3a3c3e3937ea1364fbd532ef0e84d437b6833(
    *,
    confidence: typing.Optional[jsii.Number] = None,
    criticality: typing.Optional[jsii.Number] = None,
    note: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.NoteUpdateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    related_findings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.RelatedFindingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    severity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.SeverityUpdateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    types: typing.Optional[typing.Sequence[builtins.str]] = None,
    user_defined_fields: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    verification_state: typing.Optional[builtins.str] = None,
    workflow: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.WorkflowUpdateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f1ea2f0c8b7a77a075035fe359b4018192a7fe37d13a835705cccc22b3887fa(
    *,
    aws_account_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    company_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    compliance_associated_standards_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    compliance_security_control_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    compliance_status: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    confidence: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.NumberFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    created_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.DateFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    criticality: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.NumberFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    first_observed_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.DateFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    generator_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    last_observed_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.DateFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    note_text: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    note_updated_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.DateFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    note_updated_by: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    product_arn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    product_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    record_state: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    related_findings_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    related_findings_product_arn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_details_other: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.MapFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_partition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_region: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.MapFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    severity_label: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    source_url: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    title: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    updated_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.DateFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    user_defined_fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.MapFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    verification_state: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    workflow_status: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3a0031cd590c4fc4c1cc1b567254acf98a8abce8663cfb8d1619b78415afbda(
    *,
    date_range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.DateRangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    end: typing.Optional[builtins.str] = None,
    start: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36ae8c17dfe76daaeb266eeb694027401c6b86fa8ecdc8744eaa6e092d24f29d(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91f36875bd267215fe022e63a4ce087a699536cdc1b9f8b3c84b53aa838e7074(
    *,
    comparison: builtins.str,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f01ce6428aaccb76a4dd3111c6a58270f1129efa37f87f346378055261a8a01(
    *,
    text: builtins.str,
    updated_by: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__000b578e595fbfb6609bb2cf3b90f42c91b01240906d31c22b9f1dd9869a214e(
    *,
    eq: typing.Optional[jsii.Number] = None,
    gte: typing.Optional[jsii.Number] = None,
    lte: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9df6b75e5070bcb08d999a08b3bd84da05079be466527b5ce60bbe470f59dd64(
    *,
    id: typing.Any,
    product_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ace3bf23a0eaa2083fc92b1b678856a77f120445f059b287841d7351fd7232b(
    *,
    label: typing.Optional[builtins.str] = None,
    normalized: typing.Optional[jsii.Number] = None,
    product: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7823f53010fc7a0056009b7cd0b999565e169d405ec7bb2b879614bff4f5f676(
    *,
    comparison: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e47be336b722bb880cce3edf7d5752dceac8f243282fcb2bc5094d82b71dc6b8(
    *,
    status: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__221241b44c93ea569fcf69aaaade0ce7cf31b7343bc3d072d74ccd16895d9a2d(
    *,
    actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.AutomationRulesActionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    criteria: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.AutomationRulesFindingFiltersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    is_terminal: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    rule_name: typing.Optional[builtins.str] = None,
    rule_order: typing.Optional[jsii.Number] = None,
    rule_status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5258d6906cbc8ea3b7ed82ec2c832e2751a0a1255445e6f3e81ea5935e2defb(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    auto_enable_controls: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    control_finding_generator: typing.Optional[builtins.str] = None,
    enable_default_standards: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afc1b02284691f4fac4c50413d7e6e3c86b4db4f8702643ba4c85dd68b5cb0b4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db4b61e6830fa5a7557c941ad1ea7690d59d4d1ea7c453b10a17081c25ba2e27(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8111fb2c58ed3e1e0c85928b084d60f2c8b02b604055e3087ce38f249967a54(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6647ce06efe713d1b36ec98af92808e5bf616a683fa68b2fb4fe64fafe92bf35(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d118847a7bb58b794458a6afe88e0a8324a3a4e1590aba4f028de455ee8c624(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e17fb796b4e0971555823ae1c97a99f19e5677ae303ff0ef984cd00ac919ea87(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a38c34c1f2742403521eb4af2098475d7afb878d3f9aba37048ae543b43e29c(
    *,
    auto_enable_controls: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    control_finding_generator: typing.Optional[builtins.str] = None,
    enable_default_standards: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__561d4df3cc67420b6eb1bedde6e0c0dfd6f3e64e2787adbaf250b63890914f1f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    standards_arn: builtins.str,
    disabled_standards_controls: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStandard.StandardsControlProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41379479f5bf8cc9e157587f8663e5fa189d44fccbb0d2903f35086cf4fd639f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1c025435faf1ab429f76ae44cb8672e4fe14ba11bbe310487d6a3a6bd53ae7e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f003fbeecd432c822b1f4490f85902feb985eef57ec347d64e831f0a337b479(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e923480bf5c5fa4fccb5bf4b4fb34ecf10ca3accba9f2a4f7b1b6ad7ad9437c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStandard.StandardsControlProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ef5462ffb9eee57944c11caa687907b4e26d622e7e133c3335b59694bfcc483(
    *,
    standards_control_arn: builtins.str,
    reason: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c125ac887ee3a111d19b82adf6b2639cf7fa812a424f7c788a920efcfdf1c39(
    *,
    standards_arn: builtins.str,
    disabled_standards_controls: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStandard.StandardsControlProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
