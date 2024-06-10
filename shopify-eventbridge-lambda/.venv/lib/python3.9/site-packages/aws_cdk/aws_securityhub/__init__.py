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
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggable as _ITaggable_36806126,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnAutomationRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_securityhub.CfnAutomationRule",
):
    '''The ``AWS::SecurityHub::AutomationRule`` resource specifies an automation rule based on input parameters.

    For more information, see `Automation rules <https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html>`_ in the *AWS Security Hub User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-automationrule.html
    :cloudformationResource: AWS::SecurityHub::AutomationRule
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
        :param actions: One or more actions to update finding fields if a finding matches the conditions specified in ``Criteria`` .
        :param criteria: A set of `AWS Security Finding Format (ASFF) <https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html>`_ finding field attributes and corresponding expected values that Security Hub uses to filter findings. If a rule is enabled and a finding matches the criteria specified in this parameter, Security Hub applies the rule action to the finding.
        :param description: A description of the rule.
        :param is_terminal: Specifies whether a rule is the last to be applied with respect to a finding that matches the rule criteria. This is useful when a finding matches the criteria for multiple rules, and each rule has different actions. If a rule is terminal, Security Hub applies the rule action to a finding that matches the rule criteria and doesn't evaluate other rules for the finding. By default, a rule isn't terminal.
        :param rule_name: The name of the rule.
        :param rule_order: An integer ranging from 1 to 1000 that represents the order in which the rule action is applied to findings. Security Hub applies rules with lower values for this parameter first.
        :param rule_status: Whether the rule is active after it is created. If this parameter is equal to ``ENABLED`` , Security Hub applies the rule to findings and finding updates after the rule is created.
        :param tags: User-defined tags associated with an automation rule.
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
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="actions")
    def actions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.AutomationRulesActionProperty"]]]]:
        '''One or more actions to update finding fields if a finding matches the conditions specified in ``Criteria`` .'''
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
        '''A set of `AWS Security Finding Format (ASFF) <https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html>`_ finding field attributes and corresponding expected values that Security Hub uses to filter findings. If a rule is enabled and a finding matches the criteria specified in this parameter, Security Hub applies the rule action to the finding.'''
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
        '''User-defined tags associated with an automation rule.'''
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
            user_defined_fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
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
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''The rule action updates the ``UserDefinedFields`` field of a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfieldsupdate.html#cfn-securityhub-automationrule-automationrulesfindingfieldsupdate-userdefinedfields
            '''
            result = self._values.get("user_defined_fields")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

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

            :param aws_account_id: The AWS account ID in which a finding was generated. Array Members: Minimum number of 1 item. Maximum number of 100 items.
            :param company_name: The name of the company for the product that generated the finding. For control-based findings, the company is AWS . Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param compliance_associated_standards_id: The unique identifier of a standard in which a control is enabled. This field consists of the resource portion of the Amazon Resource Name (ARN) returned for a standard in the `DescribeStandards <https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html>`_ API response. Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param compliance_security_control_id: The security control ID for which a finding was generated. Security control IDs are the same across standards. Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param compliance_status: The result of a security check. This field is only used for findings generated from controls. Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param confidence: The likelihood that a finding accurately identifies the behavior or issue that it was intended to identify. ``Confidence`` is scored on a 0–100 basis using a ratio scale. A value of ``0`` means 0 percent confidence, and a value of ``100`` means 100 percent confidence. For example, a data exfiltration detection based on a statistical deviation of network traffic has low confidence because an actual exfiltration hasn't been verified. For more information, see `Confidence <https://docs.aws.amazon.com/securityhub/latest/userguide/asff-top-level-attributes.html#asff-confidence>`_ in the *AWS Security Hub User Guide* . Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param created_at: A timestamp that indicates when this finding record was created. This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples: - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` ) - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` ) - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` ) Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param criticality: The level of importance that is assigned to the resources that are associated with a finding. ``Criticality`` is scored on a 0–100 basis, using a ratio scale that supports only full integers. A score of ``0`` means that the underlying resources have no criticality, and a score of ``100`` is reserved for the most critical resources. For more information, see `Criticality <https://docs.aws.amazon.com/securityhub/latest/userguide/asff-top-level-attributes.html#asff-criticality>`_ in the *AWS Security Hub User Guide* . Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param description: A finding's description. Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param first_observed_at: A timestamp that indicates when the potential security issue captured by a finding was first observed by the security findings product. This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples: - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` ) - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` ) - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` ) Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param generator_id: The identifier for the solution-specific component that generated a finding. Array Members: Minimum number of 1 item. Maximum number of 100 items.
            :param id: The product-specific identifier for a finding. Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param last_observed_at: A timestamp that indicates when the potential security issue captured by a finding was most recently observed by the security findings product. This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples: - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` ) - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` ) - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` ) Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param note_text: The text of a user-defined note that's added to a finding. Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param note_updated_at: The timestamp of when the note was updated. This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples: - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` ) - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` ) - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` ) Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param note_updated_by: The principal that created a note. Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param product_arn: The Amazon Resource Name (ARN) for a third-party product that generated a finding in Security Hub. Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param product_name: Provides the name of the product that generated the finding. For control-based findings, the product name is Security Hub. Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param record_state: Provides the current state of a finding. Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param related_findings_id: The product-generated identifier for a related finding. Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param related_findings_product_arn: The ARN for the product that generated a related finding. Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param resource_details_other: Custom fields and values about the resource that a finding pertains to. Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param resource_id: The identifier for the given resource type. For AWS resources that are identified by Amazon Resource Names (ARNs), this is the ARN. For AWS resources that lack ARNs, this is the identifier as defined by the AWS service that created the resource. For non- AWS resources, this is a unique identifier that is associated with the resource. Array Members: Minimum number of 1 item. Maximum number of 100 items.
            :param resource_partition: The partition in which the resource that the finding pertains to is located. A partition is a group of AWS Regions . Each AWS account is scoped to one partition. Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param resource_region: The AWS Region where the resource that a finding pertains to is located. Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param resource_tags: A list of AWS tags associated with a resource at the time the finding was processed. Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param resource_type: A finding's title. Array Members: Minimum number of 1 item. Maximum number of 100 items.
            :param severity_label: The severity value of the finding. Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param source_url: Provides a URL that links to a page about the current finding in the finding product. Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param title: A finding's title. Array Members: Minimum number of 1 item. Maximum number of 100 items.
            :param type: One or more finding types in the format of namespace/category/classifier that classify a finding. For a list of namespaces, classifiers, and categories, see `Types taxonomy for ASFF <https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format-type-taxonomy.html>`_ in the *AWS Security Hub User Guide* . Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param updated_at: A timestamp that indicates when the finding record was most recently updated. This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples: - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` ) - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` ) - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` ) Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param user_defined_fields: A list of user-defined name and value string pairs added to a finding. Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param verification_state: Provides the veracity of a finding. Array Members: Minimum number of 1 item. Maximum number of 20 items.
            :param workflow_status: Provides information about the status of the investigation into a finding. Array Members: Minimum number of 1 item. Maximum number of 20 items.

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

            Array Members: Minimum number of 1 item. Maximum number of 100 items.

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

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

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

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-complianceassociatedstandardsid
            '''
            result = self._values.get("compliance_associated_standards_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def compliance_security_control_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The security control ID for which a finding was generated. Security control IDs are the same across standards.

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-compliancesecuritycontrolid
            '''
            result = self._values.get("compliance_security_control_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def compliance_status(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The result of a security check. This field is only used for findings generated from controls.

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

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

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-confidence
            '''
            result = self._values.get("confidence")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.NumberFilterProperty"]]]], result)

        @builtins.property
        def created_at(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.DateFilterProperty"]]]]:
            '''A timestamp that indicates when this finding record was created.

            This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples:

            - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` )
            - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` )
            - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

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

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-criticality
            '''
            result = self._values.get("criticality")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.NumberFilterProperty"]]]], result)

        @builtins.property
        def description(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''A finding's description.

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def first_observed_at(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.DateFilterProperty"]]]]:
            '''A timestamp that indicates when the potential security issue captured by a finding was first observed by the security findings product.

            This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples:

            - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` )
            - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` )
            - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-firstobservedat
            '''
            result = self._values.get("first_observed_at")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.DateFilterProperty"]]]], result)

        @builtins.property
        def generator_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The identifier for the solution-specific component that generated a finding.

            Array Members: Minimum number of 1 item. Maximum number of 100 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-generatorid
            '''
            result = self._values.get("generator_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The product-specific identifier for a finding.

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def last_observed_at(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.DateFilterProperty"]]]]:
            '''A timestamp that indicates when the potential security issue captured by a finding was most recently observed by the security findings product.

            This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples:

            - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` )
            - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` )
            - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-lastobservedat
            '''
            result = self._values.get("last_observed_at")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.DateFilterProperty"]]]], result)

        @builtins.property
        def note_text(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The text of a user-defined note that's added to a finding.

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-notetext
            '''
            result = self._values.get("note_text")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def note_updated_at(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.DateFilterProperty"]]]]:
            '''The timestamp of when the note was updated.

            This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples:

            - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` )
            - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` )
            - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-noteupdatedat
            '''
            result = self._values.get("note_updated_at")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.DateFilterProperty"]]]], result)

        @builtins.property
        def note_updated_by(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The principal that created a note.

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-noteupdatedby
            '''
            result = self._values.get("note_updated_by")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def product_arn(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The Amazon Resource Name (ARN) for a third-party product that generated a finding in Security Hub.

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-productarn
            '''
            result = self._values.get("product_arn")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def product_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''Provides the name of the product that generated the finding. For control-based findings, the product name is Security Hub.

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-productname
            '''
            result = self._values.get("product_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def record_state(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''Provides the current state of a finding.

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-recordstate
            '''
            result = self._values.get("record_state")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def related_findings_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The product-generated identifier for a related finding.

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-relatedfindingsid
            '''
            result = self._values.get("related_findings_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def related_findings_product_arn(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The ARN for the product that generated a related finding.

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-relatedfindingsproductarn
            '''
            result = self._values.get("related_findings_product_arn")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_details_other(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.MapFilterProperty"]]]]:
            '''Custom fields and values about the resource that a finding pertains to.

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

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

            Array Members: Minimum number of 1 item. Maximum number of 100 items.

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

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-resourcepartition
            '''
            result = self._values.get("resource_partition")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_region(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The AWS Region where the resource that a finding pertains to is located.

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-resourceregion
            '''
            result = self._values.get("resource_region")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_tags(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.MapFilterProperty"]]]]:
            '''A list of AWS tags associated with a resource at the time the finding was processed.

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-resourcetags
            '''
            result = self._values.get("resource_tags")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.MapFilterProperty"]]]], result)

        @builtins.property
        def resource_type(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''A finding's title.

            Array Members: Minimum number of 1 item. Maximum number of 100 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-resourcetype
            '''
            result = self._values.get("resource_type")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def severity_label(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''The severity value of the finding.

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-severitylabel
            '''
            result = self._values.get("severity_label")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def source_url(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''Provides a URL that links to a page about the current finding in the finding product.

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-sourceurl
            '''
            result = self._values.get("source_url")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def title(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''A finding's title.

            Array Members: Minimum number of 1 item. Maximum number of 100 items.

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

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def updated_at(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.DateFilterProperty"]]]]:
            '''A timestamp that indicates when the finding record was most recently updated.

            This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples:

            - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` )
            - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` )
            - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-updatedat
            '''
            result = self._values.get("updated_at")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.DateFilterProperty"]]]], result)

        @builtins.property
        def user_defined_fields(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.MapFilterProperty"]]]]:
            '''A list of user-defined name and value string pairs added to a finding.

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-userdefinedfields
            '''
            result = self._values.get("user_defined_fields")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.MapFilterProperty"]]]], result)

        @builtins.property
        def verification_state(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''Provides the veracity of a finding.

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-automationrulesfindingfilters.html#cfn-securityhub-automationrule-automationrulesfindingfilters-verificationstate
            '''
            result = self._values.get("verification_state")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]], result)

        @builtins.property
        def workflow_status(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAutomationRule.StringFilterProperty"]]]]:
            '''Provides information about the status of the investigation into a finding.

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

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
            :param end: A timestamp that provides the end date for the date filter. This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples: - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` ) - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` ) - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )
            :param start: A timestamp that provides the start date for the date filter. This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples: - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` ) - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` ) - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )

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

            This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples:

            - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` )
            - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` )
            - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-automationrule-datefilter.html#cfn-securityhub-automationrule-datefilter-end
            '''
            result = self._values.get("end")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def start(self) -> typing.Optional[builtins.str]:
            '''A timestamp that provides the start date for the date filter.

            This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples:

            - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` )
            - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` )
            - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )

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

            :param id: The product-generated identifier for a related finding. Array Members: Minimum number of 1 item. Maximum number of 20 items.
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

            Array Members: Minimum number of 1 item. Maximum number of 20 items.

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

        :param actions: One or more actions to update finding fields if a finding matches the conditions specified in ``Criteria`` .
        :param criteria: A set of `AWS Security Finding Format (ASFF) <https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html>`_ finding field attributes and corresponding expected values that Security Hub uses to filter findings. If a rule is enabled and a finding matches the criteria specified in this parameter, Security Hub applies the rule action to the finding.
        :param description: A description of the rule.
        :param is_terminal: Specifies whether a rule is the last to be applied with respect to a finding that matches the rule criteria. This is useful when a finding matches the criteria for multiple rules, and each rule has different actions. If a rule is terminal, Security Hub applies the rule action to a finding that matches the rule criteria and doesn't evaluate other rules for the finding. By default, a rule isn't terminal.
        :param rule_name: The name of the rule.
        :param rule_order: An integer ranging from 1 to 1000 that represents the order in which the rule action is applied to findings. Security Hub applies rules with lower values for this parameter first.
        :param rule_status: Whether the rule is active after it is created. If this parameter is equal to ``ENABLED`` , Security Hub applies the rule to findings and finding updates after the rule is created.
        :param tags: User-defined tags associated with an automation rule.

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
        '''One or more actions to update finding fields if a finding matches the conditions specified in ``Criteria`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-automationrule.html#cfn-securityhub-automationrule-actions
        '''
        result = self._values.get("actions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAutomationRule.AutomationRulesActionProperty]]]], result)

    @builtins.property
    def criteria(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAutomationRule.AutomationRulesFindingFiltersProperty]]:
        '''A set of `AWS Security Finding Format (ASFF) <https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html>`_ finding field attributes and corresponding expected values that Security Hub uses to filter findings. If a rule is enabled and a finding matches the criteria specified in this parameter, Security Hub applies the rule action to the finding.

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
        '''User-defined tags associated with an automation rule.

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


@jsii.implements(_IInspectable_c2943556)
class CfnDelegatedAdmin(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_securityhub.CfnDelegatedAdmin",
):
    '''The ``AWS::SecurityHub::DelegatedAdmin`` resource designates the delegated AWS Security Hub administrator account for an organization.

    You must enable the integration between Security Hub and AWS Organizations before you can designate a delegated Security Hub administrator. Only the management account for an organization can designate the delegated Security Hub administrator account. For more information, see `Designating the delegated Security Hub administrator <https://docs.aws.amazon.com/securityhub/latest/userguide/designate-orgs-admin-account.html#designate-admin-instructions>`_ in the *AWS Security Hub User Guide* .

    To change the delegated administrator account, remove the current delegated administrator account, and then designate the new account.

    To designate multiple delegated administrators in different organizations and AWS Regions , we recommend using `AWS CloudFormation mappings <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/mappings-section-structure.html>`_ .

    Tags aren't supported for this resource.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-delegatedadmin.html
    :cloudformationResource: AWS::SecurityHub::DelegatedAdmin
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_securityhub as securityhub
        
        cfn_delegated_admin = securityhub.CfnDelegatedAdmin(self, "MyCfnDelegatedAdmin",
            admin_account_id="adminAccountId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        admin_account_id: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param admin_account_id: The AWS account identifier of the account to designate as the Security Hub administrator account.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e27e329e801cb67f6ec71f03a054a574103f5946def22c1bfdcd99ba50827d58)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDelegatedAdminProps(admin_account_id=admin_account_id)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baaaa369299b88b2085a28b2af39aa2abf07ab6772dc8c3ce8044a9ef9ea4df7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2c0e442efc9a3d07aaf74da8d8d9132c602da0b1c240bc4589e6ce7e3e2459a3)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDelegatedAdminIdentifier")
    def attr_delegated_admin_identifier(self) -> builtins.str:
        '''The ID of the delegated Security Hub administrator account, in the format of ``accountID/Region`` .

        :cloudformationAttribute: DelegatedAdminIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDelegatedAdminIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''Whether the delegated Security Hub administrator is set for the organization.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="adminAccountId")
    def admin_account_id(self) -> builtins.str:
        '''The AWS account identifier of the account to designate as the Security Hub administrator account.'''
        return typing.cast(builtins.str, jsii.get(self, "adminAccountId"))

    @admin_account_id.setter
    def admin_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5fdd5db8baf5624dbb4185acb8020d5499aa459d03967b97375912c3e6844c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adminAccountId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_securityhub.CfnDelegatedAdminProps",
    jsii_struct_bases=[],
    name_mapping={"admin_account_id": "adminAccountId"},
)
class CfnDelegatedAdminProps:
    def __init__(self, *, admin_account_id: builtins.str) -> None:
        '''Properties for defining a ``CfnDelegatedAdmin``.

        :param admin_account_id: The AWS account identifier of the account to designate as the Security Hub administrator account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-delegatedadmin.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_securityhub as securityhub
            
            cfn_delegated_admin_props = securityhub.CfnDelegatedAdminProps(
                admin_account_id="adminAccountId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bccd0acf2d461662eef1addff325ba8fe883439d680f7762ea393681a481c0ca)
            check_type(argname="argument admin_account_id", value=admin_account_id, expected_type=type_hints["admin_account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "admin_account_id": admin_account_id,
        }

    @builtins.property
    def admin_account_id(self) -> builtins.str:
        '''The AWS account identifier of the account to designate as the Security Hub administrator account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-delegatedadmin.html#cfn-securityhub-delegatedadmin-adminaccountid
        '''
        result = self._values.get("admin_account_id")
        assert result is not None, "Required property 'admin_account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDelegatedAdminProps(%s)" % ", ".join(
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
    :cloudformationResource: AWS::SecurityHub::Hub
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
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the ``Hub`` resource that was retrieved.

        :cloudformationAttribute: ARN
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSubscribedAt")
    def attr_subscribed_at(self) -> builtins.str:
        '''The date and time when Security Hub was enabled in your account.

        :cloudformationAttribute: SubscribedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSubscribedAt"))

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
class CfnInsight(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_securityhub.CfnInsight",
):
    '''The ``AWS::SecurityHub::Insight`` resource creates a custom insight in AWS Security Hub .

    An insight is a collection of findings that relate to a security issue that requires attention or remediation. For more information, see `Insights in AWS Security Hub <https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-insights.html>`_ in the *AWS Security Hub User Guide* .

    Tags aren't supported for this resource.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-insight.html
    :cloudformationResource: AWS::SecurityHub::Insight
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_securityhub as securityhub
        
        cfn_insight = securityhub.CfnInsight(self, "MyCfnInsight",
            filters=securityhub.CfnInsight.AwsSecurityFindingFiltersProperty(
                aws_account_id=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                aws_account_name=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                company_name=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                compliance_associated_standards_id=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                compliance_security_control_id=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                compliance_security_control_parameters_name=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                compliance_security_control_parameters_value=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                compliance_status=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                confidence=[securityhub.CfnInsight.NumberFilterProperty(
                    eq=123,
                    gte=123,
                    lte=123
                )],
                created_at=[securityhub.CfnInsight.DateFilterProperty(
                    date_range=securityhub.CfnInsight.DateRangeProperty(
                        unit="unit",
                        value=123
                    ),
                    end="end",
                    start="start"
                )],
                criticality=[securityhub.CfnInsight.NumberFilterProperty(
                    eq=123,
                    gte=123,
                    lte=123
                )],
                description=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                finding_provider_fields_confidence=[securityhub.CfnInsight.NumberFilterProperty(
                    eq=123,
                    gte=123,
                    lte=123
                )],
                finding_provider_fields_criticality=[securityhub.CfnInsight.NumberFilterProperty(
                    eq=123,
                    gte=123,
                    lte=123
                )],
                finding_provider_fields_related_findings_id=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                finding_provider_fields_related_findings_product_arn=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                finding_provider_fields_severity_label=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                finding_provider_fields_severity_original=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                finding_provider_fields_types=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                first_observed_at=[securityhub.CfnInsight.DateFilterProperty(
                    date_range=securityhub.CfnInsight.DateRangeProperty(
                        unit="unit",
                        value=123
                    ),
                    end="end",
                    start="start"
                )],
                generator_id=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                id=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                keyword=[securityhub.CfnInsight.KeywordFilterProperty(
                    value="value"
                )],
                last_observed_at=[securityhub.CfnInsight.DateFilterProperty(
                    date_range=securityhub.CfnInsight.DateRangeProperty(
                        unit="unit",
                        value=123
                    ),
                    end="end",
                    start="start"
                )],
                malware_name=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                malware_path=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                malware_state=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                malware_type=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                network_destination_domain=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                network_destination_ip_v4=[securityhub.CfnInsight.IpFilterProperty(
                    cidr="cidr"
                )],
                network_destination_ip_v6=[securityhub.CfnInsight.IpFilterProperty(
                    cidr="cidr"
                )],
                network_destination_port=[securityhub.CfnInsight.NumberFilterProperty(
                    eq=123,
                    gte=123,
                    lte=123
                )],
                network_direction=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                network_protocol=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                network_source_domain=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                network_source_ip_v4=[securityhub.CfnInsight.IpFilterProperty(
                    cidr="cidr"
                )],
                network_source_ip_v6=[securityhub.CfnInsight.IpFilterProperty(
                    cidr="cidr"
                )],
                network_source_mac=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                network_source_port=[securityhub.CfnInsight.NumberFilterProperty(
                    eq=123,
                    gte=123,
                    lte=123
                )],
                note_text=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                note_updated_at=[securityhub.CfnInsight.DateFilterProperty(
                    date_range=securityhub.CfnInsight.DateRangeProperty(
                        unit="unit",
                        value=123
                    ),
                    end="end",
                    start="start"
                )],
                note_updated_by=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                process_launched_at=[securityhub.CfnInsight.DateFilterProperty(
                    date_range=securityhub.CfnInsight.DateRangeProperty(
                        unit="unit",
                        value=123
                    ),
                    end="end",
                    start="start"
                )],
                process_name=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                process_parent_pid=[securityhub.CfnInsight.NumberFilterProperty(
                    eq=123,
                    gte=123,
                    lte=123
                )],
                process_path=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                process_pid=[securityhub.CfnInsight.NumberFilterProperty(
                    eq=123,
                    gte=123,
                    lte=123
                )],
                process_terminated_at=[securityhub.CfnInsight.DateFilterProperty(
                    date_range=securityhub.CfnInsight.DateRangeProperty(
                        unit="unit",
                        value=123
                    ),
                    end="end",
                    start="start"
                )],
                product_arn=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                product_fields=[securityhub.CfnInsight.MapFilterProperty(
                    comparison="comparison",
                    key="key",
                    value="value"
                )],
                product_name=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                recommendation_text=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                record_state=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                region=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                related_findings_id=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                related_findings_product_arn=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_application_arn=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_application_name=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_aws_ec2_instance_iam_instance_profile_arn=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_aws_ec2_instance_image_id=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_aws_ec2_instance_ip_v4_addresses=[securityhub.CfnInsight.IpFilterProperty(
                    cidr="cidr"
                )],
                resource_aws_ec2_instance_ip_v6_addresses=[securityhub.CfnInsight.IpFilterProperty(
                    cidr="cidr"
                )],
                resource_aws_ec2_instance_key_name=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_aws_ec2_instance_launched_at=[securityhub.CfnInsight.DateFilterProperty(
                    date_range=securityhub.CfnInsight.DateRangeProperty(
                        unit="unit",
                        value=123
                    ),
                    end="end",
                    start="start"
                )],
                resource_aws_ec2_instance_subnet_id=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_aws_ec2_instance_type=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_aws_ec2_instance_vpc_id=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_aws_iam_access_key_created_at=[securityhub.CfnInsight.DateFilterProperty(
                    date_range=securityhub.CfnInsight.DateRangeProperty(
                        unit="unit",
                        value=123
                    ),
                    end="end",
                    start="start"
                )],
                resource_aws_iam_access_key_principal_name=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_aws_iam_access_key_status=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_aws_iam_access_key_user_name=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_aws_iam_user_user_name=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_aws_s3_bucket_owner_id=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_aws_s3_bucket_owner_name=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_container_image_id=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_container_image_name=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_container_launched_at=[securityhub.CfnInsight.DateFilterProperty(
                    date_range=securityhub.CfnInsight.DateRangeProperty(
                        unit="unit",
                        value=123
                    ),
                    end="end",
                    start="start"
                )],
                resource_container_name=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_details_other=[securityhub.CfnInsight.MapFilterProperty(
                    comparison="comparison",
                    key="key",
                    value="value"
                )],
                resource_id=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_partition=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_region=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_tags=[securityhub.CfnInsight.MapFilterProperty(
                    comparison="comparison",
                    key="key",
                    value="value"
                )],
                resource_type=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                sample=[securityhub.CfnInsight.BooleanFilterProperty(
                    value=False
                )],
                severity_label=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                severity_normalized=[securityhub.CfnInsight.NumberFilterProperty(
                    eq=123,
                    gte=123,
                    lte=123
                )],
                severity_product=[securityhub.CfnInsight.NumberFilterProperty(
                    eq=123,
                    gte=123,
                    lte=123
                )],
                source_url=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                threat_intel_indicator_category=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                threat_intel_indicator_last_observed_at=[securityhub.CfnInsight.DateFilterProperty(
                    date_range=securityhub.CfnInsight.DateRangeProperty(
                        unit="unit",
                        value=123
                    ),
                    end="end",
                    start="start"
                )],
                threat_intel_indicator_source=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                threat_intel_indicator_source_url=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                threat_intel_indicator_type=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                threat_intel_indicator_value=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                title=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                type=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                updated_at=[securityhub.CfnInsight.DateFilterProperty(
                    date_range=securityhub.CfnInsight.DateRangeProperty(
                        unit="unit",
                        value=123
                    ),
                    end="end",
                    start="start"
                )],
                user_defined_fields=[securityhub.CfnInsight.MapFilterProperty(
                    comparison="comparison",
                    key="key",
                    value="value"
                )],
                verification_state=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                vulnerabilities_exploit_available=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                vulnerabilities_fix_available=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                workflow_state=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                workflow_status=[securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )]
            ),
            group_by_attribute="groupByAttribute",
            name="name"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        filters: typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.AwsSecurityFindingFiltersProperty", typing.Dict[builtins.str, typing.Any]]],
        group_by_attribute: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param filters: One or more attributes used to filter the findings included in the insight. The insight only includes findings that match the criteria defined in the filters. You can filter by up to ten finding attributes. For each attribute, you can provide up to 20 filter values.
        :param group_by_attribute: The grouping attribute for the insight's findings. Indicates how to group the matching findings, and identifies the type of item that the insight applies to. For example, if an insight is grouped by resource identifier, then the insight produces a list of resource identifiers.
        :param name: The name of a Security Hub insight.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d671d628902c96b28f2d378ea3f0a99fe19e13873725f86dd92bbe36b4c9a166)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnInsightProps(
            filters=filters, group_by_attribute=group_by_attribute, name=name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12375a912637f8bdf52366060d1f39a683bdba181f295acc48a50989fdd81232)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7a18620bef3bfa4a37ce6dbea7bd1e144bc38b0403e564d72f00f996c67a180a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrInsightArn")
    def attr_insight_arn(self) -> builtins.str:
        '''The ARN of a Security Hub insight.

        :cloudformationAttribute: InsightArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrInsightArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="filters")
    def filters(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnInsight.AwsSecurityFindingFiltersProperty"]:
        '''One or more attributes used to filter the findings included in the insight.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnInsight.AwsSecurityFindingFiltersProperty"], jsii.get(self, "filters"))

    @filters.setter
    def filters(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnInsight.AwsSecurityFindingFiltersProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40bc93b289fd6fbe5ea66bbe5f8eca6d1371fec0a59789022949021156c016a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filters", value)

    @builtins.property
    @jsii.member(jsii_name="groupByAttribute")
    def group_by_attribute(self) -> builtins.str:
        '''The grouping attribute for the insight's findings.'''
        return typing.cast(builtins.str, jsii.get(self, "groupByAttribute"))

    @group_by_attribute.setter
    def group_by_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__645260a48ef5fcfdb2acc56551dd1e6897e309e4feef6d7b81e9aa50ad0cc353)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupByAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of a Security Hub insight.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__766e42c726b2c502b30c5c9ccf965e83324fe1b106e1918e14b49c7f3b6cb61c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityhub.CfnInsight.AwsSecurityFindingFiltersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aws_account_id": "awsAccountId",
            "aws_account_name": "awsAccountName",
            "company_name": "companyName",
            "compliance_associated_standards_id": "complianceAssociatedStandardsId",
            "compliance_security_control_id": "complianceSecurityControlId",
            "compliance_security_control_parameters_name": "complianceSecurityControlParametersName",
            "compliance_security_control_parameters_value": "complianceSecurityControlParametersValue",
            "compliance_status": "complianceStatus",
            "confidence": "confidence",
            "created_at": "createdAt",
            "criticality": "criticality",
            "description": "description",
            "finding_provider_fields_confidence": "findingProviderFieldsConfidence",
            "finding_provider_fields_criticality": "findingProviderFieldsCriticality",
            "finding_provider_fields_related_findings_id": "findingProviderFieldsRelatedFindingsId",
            "finding_provider_fields_related_findings_product_arn": "findingProviderFieldsRelatedFindingsProductArn",
            "finding_provider_fields_severity_label": "findingProviderFieldsSeverityLabel",
            "finding_provider_fields_severity_original": "findingProviderFieldsSeverityOriginal",
            "finding_provider_fields_types": "findingProviderFieldsTypes",
            "first_observed_at": "firstObservedAt",
            "generator_id": "generatorId",
            "id": "id",
            "keyword": "keyword",
            "last_observed_at": "lastObservedAt",
            "malware_name": "malwareName",
            "malware_path": "malwarePath",
            "malware_state": "malwareState",
            "malware_type": "malwareType",
            "network_destination_domain": "networkDestinationDomain",
            "network_destination_ip_v4": "networkDestinationIpV4",
            "network_destination_ip_v6": "networkDestinationIpV6",
            "network_destination_port": "networkDestinationPort",
            "network_direction": "networkDirection",
            "network_protocol": "networkProtocol",
            "network_source_domain": "networkSourceDomain",
            "network_source_ip_v4": "networkSourceIpV4",
            "network_source_ip_v6": "networkSourceIpV6",
            "network_source_mac": "networkSourceMac",
            "network_source_port": "networkSourcePort",
            "note_text": "noteText",
            "note_updated_at": "noteUpdatedAt",
            "note_updated_by": "noteUpdatedBy",
            "process_launched_at": "processLaunchedAt",
            "process_name": "processName",
            "process_parent_pid": "processParentPid",
            "process_path": "processPath",
            "process_pid": "processPid",
            "process_terminated_at": "processTerminatedAt",
            "product_arn": "productArn",
            "product_fields": "productFields",
            "product_name": "productName",
            "recommendation_text": "recommendationText",
            "record_state": "recordState",
            "region": "region",
            "related_findings_id": "relatedFindingsId",
            "related_findings_product_arn": "relatedFindingsProductArn",
            "resource_application_arn": "resourceApplicationArn",
            "resource_application_name": "resourceApplicationName",
            "resource_aws_ec2_instance_iam_instance_profile_arn": "resourceAwsEc2InstanceIamInstanceProfileArn",
            "resource_aws_ec2_instance_image_id": "resourceAwsEc2InstanceImageId",
            "resource_aws_ec2_instance_ip_v4_addresses": "resourceAwsEc2InstanceIpV4Addresses",
            "resource_aws_ec2_instance_ip_v6_addresses": "resourceAwsEc2InstanceIpV6Addresses",
            "resource_aws_ec2_instance_key_name": "resourceAwsEc2InstanceKeyName",
            "resource_aws_ec2_instance_launched_at": "resourceAwsEc2InstanceLaunchedAt",
            "resource_aws_ec2_instance_subnet_id": "resourceAwsEc2InstanceSubnetId",
            "resource_aws_ec2_instance_type": "resourceAwsEc2InstanceType",
            "resource_aws_ec2_instance_vpc_id": "resourceAwsEc2InstanceVpcId",
            "resource_aws_iam_access_key_created_at": "resourceAwsIamAccessKeyCreatedAt",
            "resource_aws_iam_access_key_principal_name": "resourceAwsIamAccessKeyPrincipalName",
            "resource_aws_iam_access_key_status": "resourceAwsIamAccessKeyStatus",
            "resource_aws_iam_access_key_user_name": "resourceAwsIamAccessKeyUserName",
            "resource_aws_iam_user_user_name": "resourceAwsIamUserUserName",
            "resource_aws_s3_bucket_owner_id": "resourceAwsS3BucketOwnerId",
            "resource_aws_s3_bucket_owner_name": "resourceAwsS3BucketOwnerName",
            "resource_container_image_id": "resourceContainerImageId",
            "resource_container_image_name": "resourceContainerImageName",
            "resource_container_launched_at": "resourceContainerLaunchedAt",
            "resource_container_name": "resourceContainerName",
            "resource_details_other": "resourceDetailsOther",
            "resource_id": "resourceId",
            "resource_partition": "resourcePartition",
            "resource_region": "resourceRegion",
            "resource_tags": "resourceTags",
            "resource_type": "resourceType",
            "sample": "sample",
            "severity_label": "severityLabel",
            "severity_normalized": "severityNormalized",
            "severity_product": "severityProduct",
            "source_url": "sourceUrl",
            "threat_intel_indicator_category": "threatIntelIndicatorCategory",
            "threat_intel_indicator_last_observed_at": "threatIntelIndicatorLastObservedAt",
            "threat_intel_indicator_source": "threatIntelIndicatorSource",
            "threat_intel_indicator_source_url": "threatIntelIndicatorSourceUrl",
            "threat_intel_indicator_type": "threatIntelIndicatorType",
            "threat_intel_indicator_value": "threatIntelIndicatorValue",
            "title": "title",
            "type": "type",
            "updated_at": "updatedAt",
            "user_defined_fields": "userDefinedFields",
            "verification_state": "verificationState",
            "vulnerabilities_exploit_available": "vulnerabilitiesExploitAvailable",
            "vulnerabilities_fix_available": "vulnerabilitiesFixAvailable",
            "workflow_state": "workflowState",
            "workflow_status": "workflowStatus",
        },
    )
    class AwsSecurityFindingFiltersProperty:
        def __init__(
            self,
            *,
            aws_account_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            aws_account_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            company_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            compliance_associated_standards_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            compliance_security_control_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            compliance_security_control_parameters_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            compliance_security_control_parameters_value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            compliance_status: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            confidence: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.NumberFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            created_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.DateFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            criticality: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.NumberFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            description: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            finding_provider_fields_confidence: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.NumberFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            finding_provider_fields_criticality: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.NumberFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            finding_provider_fields_related_findings_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            finding_provider_fields_related_findings_product_arn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            finding_provider_fields_severity_label: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            finding_provider_fields_severity_original: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            finding_provider_fields_types: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            first_observed_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.DateFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            generator_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            keyword: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.KeywordFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            last_observed_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.DateFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            malware_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            malware_path: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            malware_state: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            malware_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            network_destination_domain: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            network_destination_ip_v4: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.IpFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            network_destination_ip_v6: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.IpFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            network_destination_port: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.NumberFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            network_direction: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            network_protocol: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            network_source_domain: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            network_source_ip_v4: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.IpFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            network_source_ip_v6: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.IpFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            network_source_mac: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            network_source_port: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.NumberFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            note_text: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            note_updated_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.DateFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            note_updated_by: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            process_launched_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.DateFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            process_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            process_parent_pid: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.NumberFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            process_path: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            process_pid: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.NumberFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            process_terminated_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.DateFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            product_arn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            product_fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.MapFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            product_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            recommendation_text: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            record_state: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            region: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            related_findings_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            related_findings_product_arn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_application_arn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_application_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_aws_ec2_instance_iam_instance_profile_arn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_aws_ec2_instance_image_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_aws_ec2_instance_ip_v4_addresses: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.IpFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_aws_ec2_instance_ip_v6_addresses: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.IpFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_aws_ec2_instance_key_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_aws_ec2_instance_launched_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.DateFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_aws_ec2_instance_subnet_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_aws_ec2_instance_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_aws_ec2_instance_vpc_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_aws_iam_access_key_created_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.DateFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_aws_iam_access_key_principal_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_aws_iam_access_key_status: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_aws_iam_access_key_user_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_aws_iam_user_user_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_aws_s3_bucket_owner_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_aws_s3_bucket_owner_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_container_image_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_container_image_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_container_launched_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.DateFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_container_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_details_other: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.MapFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_partition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_region: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.MapFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            sample: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.BooleanFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            severity_label: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            severity_normalized: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.NumberFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            severity_product: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.NumberFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            source_url: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            threat_intel_indicator_category: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            threat_intel_indicator_last_observed_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.DateFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            threat_intel_indicator_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            threat_intel_indicator_source_url: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            threat_intel_indicator_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            threat_intel_indicator_value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            title: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            updated_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.DateFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            user_defined_fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.MapFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            verification_state: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            vulnerabilities_exploit_available: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            vulnerabilities_fix_available: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            workflow_state: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            workflow_status: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''A collection of filters that are applied to all active findings aggregated by AWS Security Hub .

            You can filter by up to ten finding attributes. For each attribute, you can provide up to 20 filter values.

            :param aws_account_id: The AWS account ID in which a finding is generated.
            :param aws_account_name: The name of the AWS account in which a finding is generated.
            :param company_name: The name of the findings provider (company) that owns the solution (product) that generates findings.
            :param compliance_associated_standards_id: The unique identifier of a standard in which a control is enabled. This field consists of the resource portion of the Amazon Resource Name (ARN) returned for a standard in the `DescribeStandards <https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html>`_ API response.
            :param compliance_security_control_id: The unique identifier of a control across standards. Values for this field typically consist of an AWS service and a number, such as APIGateway.5.
            :param compliance_security_control_parameters_name: The name of a security control parameter.
            :param compliance_security_control_parameters_value: The current value of a security control parameter.
            :param compliance_status: Exclusive to findings that are generated as the result of a check run against a specific rule in a supported standard, such as CIS AWS Foundations. Contains security standard-related finding details.
            :param confidence: A finding's confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify. Confidence is scored on a 0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100 percent confidence.
            :param created_at: A timestamp that indicates when the security findings provider created the potential security issue that a finding reflects. This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples: - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` ) - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` ) - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )
            :param criticality: The level of importance assigned to the resources associated with the finding. A score of 0 means that the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.
            :param description: A finding's description.
            :param finding_provider_fields_confidence: The finding provider value for the finding confidence. Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify. Confidence is scored on a 0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100 percent confidence.
            :param finding_provider_fields_criticality: The finding provider value for the level of importance assigned to the resources associated with the findings. A score of 0 means that the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.
            :param finding_provider_fields_related_findings_id: The finding identifier of a related finding that is identified by the finding provider.
            :param finding_provider_fields_related_findings_product_arn: The ARN of the solution that generated a related finding that is identified by the finding provider.
            :param finding_provider_fields_severity_label: The finding provider value for the severity label.
            :param finding_provider_fields_severity_original: The finding provider's original value for the severity.
            :param finding_provider_fields_types: One or more finding types that the finding provider assigned to the finding. Uses the format of ``namespace/category/classifier`` that classify a finding. Valid namespace values are: Software and Configuration Checks | TTPs | Effects | Unusual Behaviors | Sensitive Data Identifications
            :param first_observed_at: A timestamp that indicates when the security findings provider first observed the potential security issue that a finding captured. This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples: - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` ) - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` ) - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )
            :param generator_id: The identifier for the solution-specific component (a discrete unit of logic) that generated a finding. In various security findings providers' solutions, this generator can be called a rule, a check, a detector, a plugin, etc.
            :param id: The security findings provider-specific identifier for a finding.
            :param keyword: This field is deprecated. A keyword for a finding.
            :param last_observed_at: A timestamp that indicates when the security findings provider most recently observed the potential security issue that a finding captured. This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples: - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` ) - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` ) - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )
            :param malware_name: The name of the malware that was observed.
            :param malware_path: The filesystem path of the malware that was observed.
            :param malware_state: The state of the malware that was observed.
            :param malware_type: The type of the malware that was observed.
            :param network_destination_domain: The destination domain of network-related information about a finding.
            :param network_destination_ip_v4: The destination IPv4 address of network-related information about a finding.
            :param network_destination_ip_v6: The destination IPv6 address of network-related information about a finding.
            :param network_destination_port: The destination port of network-related information about a finding.
            :param network_direction: Indicates the direction of network traffic associated with a finding.
            :param network_protocol: The protocol of network-related information about a finding.
            :param network_source_domain: The source domain of network-related information about a finding.
            :param network_source_ip_v4: The source IPv4 address of network-related information about a finding.
            :param network_source_ip_v6: The source IPv6 address of network-related information about a finding.
            :param network_source_mac: The source media access control (MAC) address of network-related information about a finding.
            :param network_source_port: The source port of network-related information about a finding.
            :param note_text: The text of a note.
            :param note_updated_at: The timestamp of when the note was updated.
            :param note_updated_by: The principal that created a note.
            :param process_launched_at: A timestamp that identifies when the process was launched. This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples: - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` ) - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` ) - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )
            :param process_name: The name of the process.
            :param process_parent_pid: The parent process ID. This field accepts positive integers between ``O`` and ``2147483647`` .
            :param process_path: The path to the process executable.
            :param process_pid: The process ID.
            :param process_terminated_at: A timestamp that identifies when the process was terminated. This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples: - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` ) - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` ) - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )
            :param product_arn: The ARN generated by Security Hub that uniquely identifies a third-party company (security findings provider) after this provider's product (solution that generates findings) is registered with Security Hub.
            :param product_fields: A data type where security findings providers can include additional solution-specific details that aren't part of the defined ``AwsSecurityFinding`` format.
            :param product_name: The name of the solution (product) that generates findings.
            :param recommendation_text: The recommendation of what to do about the issue described in a finding.
            :param record_state: The updated record state for the finding.
            :param region: The Region from which the finding was generated.
            :param related_findings_id: The solution-generated identifier for a related finding.
            :param related_findings_product_arn: The ARN of the solution that generated a related finding.
            :param resource_application_arn: The ARN of the application that is related to a finding.
            :param resource_application_name: The name of the application that is related to a finding.
            :param resource_aws_ec2_instance_iam_instance_profile_arn: The IAM profile ARN of the instance.
            :param resource_aws_ec2_instance_image_id: The Amazon Machine Image (AMI) ID of the instance.
            :param resource_aws_ec2_instance_ip_v4_addresses: The IPv4 addresses associated with the instance.
            :param resource_aws_ec2_instance_ip_v6_addresses: The IPv6 addresses associated with the instance.
            :param resource_aws_ec2_instance_key_name: The key name associated with the instance.
            :param resource_aws_ec2_instance_launched_at: The date and time the instance was launched.
            :param resource_aws_ec2_instance_subnet_id: The identifier of the subnet that the instance was launched in.
            :param resource_aws_ec2_instance_type: The instance type of the instance.
            :param resource_aws_ec2_instance_vpc_id: The identifier of the VPC that the instance was launched in.
            :param resource_aws_iam_access_key_created_at: The creation date/time of the IAM access key related to a finding.
            :param resource_aws_iam_access_key_principal_name: The name of the principal that is associated with an IAM access key.
            :param resource_aws_iam_access_key_status: The status of the IAM access key related to a finding.
            :param resource_aws_iam_access_key_user_name: This field is deprecated. The username associated with the IAM access key related to a finding.
            :param resource_aws_iam_user_user_name: The name of an IAM user.
            :param resource_aws_s3_bucket_owner_id: The canonical user ID of the owner of the S3 bucket.
            :param resource_aws_s3_bucket_owner_name: The display name of the owner of the S3 bucket.
            :param resource_container_image_id: The identifier of the image related to a finding.
            :param resource_container_image_name: The name of the image related to a finding.
            :param resource_container_launched_at: A timestamp that identifies when the container was started. This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples: - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` ) - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` ) - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )
            :param resource_container_name: The name of the container related to a finding.
            :param resource_details_other: The details of a resource that doesn't have a specific subfield for the resource type defined.
            :param resource_id: The canonical identifier for the given resource type.
            :param resource_partition: The canonical AWS partition name that the Region is assigned to.
            :param resource_region: The canonical AWS external Region name where this resource is located.
            :param resource_tags: A list of AWS tags associated with a resource at the time the finding was processed.
            :param resource_type: Specifies the type of the resource that details are provided for.
            :param sample: Indicates whether or not sample findings are included in the filter results.
            :param severity_label: The label of a finding's severity.
            :param severity_normalized: Deprecated. The normalized severity of a finding. Instead of providing ``Normalized`` , provide ``Label`` . The value of ``Normalized`` can be an integer between ``0`` and ``100`` . If you provide ``Label`` and do not provide ``Normalized`` , then ``Normalized`` is set automatically as follows. - ``INFORMATIONAL`` - 0 - ``LOW`` - 1 - ``MEDIUM`` - 40 - ``HIGH`` - 70 - ``CRITICAL`` - 90
            :param severity_product: Deprecated. This attribute isn't included in findings. Instead of providing ``Product`` , provide ``Original`` . The native severity as defined by the AWS service or integrated partner product that generated the finding.
            :param source_url: A URL that links to a page about the current finding in the security findings provider's solution.
            :param threat_intel_indicator_category: The category of a threat intelligence indicator.
            :param threat_intel_indicator_last_observed_at: A timestamp that identifies the last observation of a threat intelligence indicator.
            :param threat_intel_indicator_source: The source of the threat intelligence.
            :param threat_intel_indicator_source_url: The URL for more details from the source of the threat intelligence.
            :param threat_intel_indicator_type: The type of a threat intelligence indicator.
            :param threat_intel_indicator_value: The value of a threat intelligence indicator.
            :param title: A finding's title.
            :param type: A finding type in the format of ``namespace/category/classifier`` that classifies a finding.
            :param updated_at: A timestamp that indicates when the security findings provider last updated the finding record. This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples: - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` ) - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` ) - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )
            :param user_defined_fields: A list of name/value string pairs associated with the finding. These are custom, user-defined fields added to a finding.
            :param verification_state: The veracity of a finding.
            :param vulnerabilities_exploit_available: Indicates whether a software vulnerability in your environment has a known exploit. You can filter findings by this field only if you use Security Hub and Amazon Inspector.
            :param vulnerabilities_fix_available: Indicates whether a vulnerability is fixed in a newer version of the affected software packages. You can filter findings by this field only if you use Security Hub and Amazon Inspector.
            :param workflow_state: The workflow state of a finding. Note that this field is deprecated. To search for a finding based on its workflow status, use ``WorkflowStatus`` .
            :param workflow_status: The status of the investigation into a finding. Allowed values are the following. - ``NEW`` - The initial state of a finding, before it is reviewed. Security Hub also resets the workflow status from ``NOTIFIED`` or ``RESOLVED`` to ``NEW`` in the following cases: - ``RecordState`` changes from ``ARCHIVED`` to ``ACTIVE`` . - ``Compliance.Status`` changes from ``PASSED`` to either ``WARNING`` , ``FAILED`` , or ``NOT_AVAILABLE`` . - ``NOTIFIED`` - Indicates that the resource owner has been notified about the security issue. Used when the initial reviewer is not the resource owner, and needs intervention from the resource owner. If one of the following occurs, the workflow status is changed automatically from ``NOTIFIED`` to ``NEW`` : - ``RecordState`` changes from ``ARCHIVED`` to ``ACTIVE`` . - ``Compliance.Status`` changes from ``PASSED`` to ``FAILED`` , ``WARNING`` , or ``NOT_AVAILABLE`` . - ``SUPPRESSED`` - Indicates that you reviewed the finding and do not believe that any action is needed. The workflow status of a ``SUPPRESSED`` finding does not change if ``RecordState`` changes from ``ARCHIVED`` to ``ACTIVE`` . - ``RESOLVED`` - The finding was reviewed and remediated and is now considered resolved. The finding remains ``RESOLVED`` unless one of the following occurs: - ``RecordState`` changes from ``ARCHIVED`` to ``ACTIVE`` . - ``Compliance.Status`` changes from ``PASSED`` to ``FAILED`` , ``WARNING`` , or ``NOT_AVAILABLE`` . In those cases, the workflow status is automatically reset to ``NEW`` . For findings from controls, if ``Compliance.Status`` is ``PASSED`` , then Security Hub automatically sets the workflow status to ``RESOLVED`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityhub as securityhub
                
                aws_security_finding_filters_property = securityhub.CfnInsight.AwsSecurityFindingFiltersProperty(
                    aws_account_id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    aws_account_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    company_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    compliance_associated_standards_id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    compliance_security_control_id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    compliance_security_control_parameters_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    compliance_security_control_parameters_value=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    compliance_status=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    confidence=[securityhub.CfnInsight.NumberFilterProperty(
                        eq=123,
                        gte=123,
                        lte=123
                    )],
                    created_at=[securityhub.CfnInsight.DateFilterProperty(
                        date_range=securityhub.CfnInsight.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    criticality=[securityhub.CfnInsight.NumberFilterProperty(
                        eq=123,
                        gte=123,
                        lte=123
                    )],
                    description=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    finding_provider_fields_confidence=[securityhub.CfnInsight.NumberFilterProperty(
                        eq=123,
                        gte=123,
                        lte=123
                    )],
                    finding_provider_fields_criticality=[securityhub.CfnInsight.NumberFilterProperty(
                        eq=123,
                        gte=123,
                        lte=123
                    )],
                    finding_provider_fields_related_findings_id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    finding_provider_fields_related_findings_product_arn=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    finding_provider_fields_severity_label=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    finding_provider_fields_severity_original=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    finding_provider_fields_types=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    first_observed_at=[securityhub.CfnInsight.DateFilterProperty(
                        date_range=securityhub.CfnInsight.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    generator_id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    keyword=[securityhub.CfnInsight.KeywordFilterProperty(
                        value="value"
                    )],
                    last_observed_at=[securityhub.CfnInsight.DateFilterProperty(
                        date_range=securityhub.CfnInsight.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    malware_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    malware_path=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    malware_state=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    malware_type=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    network_destination_domain=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    network_destination_ip_v4=[securityhub.CfnInsight.IpFilterProperty(
                        cidr="cidr"
                    )],
                    network_destination_ip_v6=[securityhub.CfnInsight.IpFilterProperty(
                        cidr="cidr"
                    )],
                    network_destination_port=[securityhub.CfnInsight.NumberFilterProperty(
                        eq=123,
                        gte=123,
                        lte=123
                    )],
                    network_direction=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    network_protocol=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    network_source_domain=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    network_source_ip_v4=[securityhub.CfnInsight.IpFilterProperty(
                        cidr="cidr"
                    )],
                    network_source_ip_v6=[securityhub.CfnInsight.IpFilterProperty(
                        cidr="cidr"
                    )],
                    network_source_mac=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    network_source_port=[securityhub.CfnInsight.NumberFilterProperty(
                        eq=123,
                        gte=123,
                        lte=123
                    )],
                    note_text=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    note_updated_at=[securityhub.CfnInsight.DateFilterProperty(
                        date_range=securityhub.CfnInsight.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    note_updated_by=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    process_launched_at=[securityhub.CfnInsight.DateFilterProperty(
                        date_range=securityhub.CfnInsight.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    process_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    process_parent_pid=[securityhub.CfnInsight.NumberFilterProperty(
                        eq=123,
                        gte=123,
                        lte=123
                    )],
                    process_path=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    process_pid=[securityhub.CfnInsight.NumberFilterProperty(
                        eq=123,
                        gte=123,
                        lte=123
                    )],
                    process_terminated_at=[securityhub.CfnInsight.DateFilterProperty(
                        date_range=securityhub.CfnInsight.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    product_arn=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    product_fields=[securityhub.CfnInsight.MapFilterProperty(
                        comparison="comparison",
                        key="key",
                        value="value"
                    )],
                    product_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    recommendation_text=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    record_state=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    region=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    related_findings_id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    related_findings_product_arn=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_application_arn=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_application_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_aws_ec2_instance_iam_instance_profile_arn=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_aws_ec2_instance_image_id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_aws_ec2_instance_ip_v4_addresses=[securityhub.CfnInsight.IpFilterProperty(
                        cidr="cidr"
                    )],
                    resource_aws_ec2_instance_ip_v6_addresses=[securityhub.CfnInsight.IpFilterProperty(
                        cidr="cidr"
                    )],
                    resource_aws_ec2_instance_key_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_aws_ec2_instance_launched_at=[securityhub.CfnInsight.DateFilterProperty(
                        date_range=securityhub.CfnInsight.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    resource_aws_ec2_instance_subnet_id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_aws_ec2_instance_type=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_aws_ec2_instance_vpc_id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_aws_iam_access_key_created_at=[securityhub.CfnInsight.DateFilterProperty(
                        date_range=securityhub.CfnInsight.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    resource_aws_iam_access_key_principal_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_aws_iam_access_key_status=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_aws_iam_access_key_user_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_aws_iam_user_user_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_aws_s3_bucket_owner_id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_aws_s3_bucket_owner_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_container_image_id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_container_image_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_container_launched_at=[securityhub.CfnInsight.DateFilterProperty(
                        date_range=securityhub.CfnInsight.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    resource_container_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_details_other=[securityhub.CfnInsight.MapFilterProperty(
                        comparison="comparison",
                        key="key",
                        value="value"
                    )],
                    resource_id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_partition=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_region=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_tags=[securityhub.CfnInsight.MapFilterProperty(
                        comparison="comparison",
                        key="key",
                        value="value"
                    )],
                    resource_type=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    sample=[securityhub.CfnInsight.BooleanFilterProperty(
                        value=False
                    )],
                    severity_label=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    severity_normalized=[securityhub.CfnInsight.NumberFilterProperty(
                        eq=123,
                        gte=123,
                        lte=123
                    )],
                    severity_product=[securityhub.CfnInsight.NumberFilterProperty(
                        eq=123,
                        gte=123,
                        lte=123
                    )],
                    source_url=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    threat_intel_indicator_category=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    threat_intel_indicator_last_observed_at=[securityhub.CfnInsight.DateFilterProperty(
                        date_range=securityhub.CfnInsight.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    threat_intel_indicator_source=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    threat_intel_indicator_source_url=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    threat_intel_indicator_type=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    threat_intel_indicator_value=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    title=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    type=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    updated_at=[securityhub.CfnInsight.DateFilterProperty(
                        date_range=securityhub.CfnInsight.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    user_defined_fields=[securityhub.CfnInsight.MapFilterProperty(
                        comparison="comparison",
                        key="key",
                        value="value"
                    )],
                    verification_state=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    vulnerabilities_exploit_available=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    vulnerabilities_fix_available=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    workflow_state=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    workflow_status=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f929ea28f5698af2f86b0f581baee2cb87fe5520179930ea0794beb525d75f5d)
                check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
                check_type(argname="argument aws_account_name", value=aws_account_name, expected_type=type_hints["aws_account_name"])
                check_type(argname="argument company_name", value=company_name, expected_type=type_hints["company_name"])
                check_type(argname="argument compliance_associated_standards_id", value=compliance_associated_standards_id, expected_type=type_hints["compliance_associated_standards_id"])
                check_type(argname="argument compliance_security_control_id", value=compliance_security_control_id, expected_type=type_hints["compliance_security_control_id"])
                check_type(argname="argument compliance_security_control_parameters_name", value=compliance_security_control_parameters_name, expected_type=type_hints["compliance_security_control_parameters_name"])
                check_type(argname="argument compliance_security_control_parameters_value", value=compliance_security_control_parameters_value, expected_type=type_hints["compliance_security_control_parameters_value"])
                check_type(argname="argument compliance_status", value=compliance_status, expected_type=type_hints["compliance_status"])
                check_type(argname="argument confidence", value=confidence, expected_type=type_hints["confidence"])
                check_type(argname="argument created_at", value=created_at, expected_type=type_hints["created_at"])
                check_type(argname="argument criticality", value=criticality, expected_type=type_hints["criticality"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument finding_provider_fields_confidence", value=finding_provider_fields_confidence, expected_type=type_hints["finding_provider_fields_confidence"])
                check_type(argname="argument finding_provider_fields_criticality", value=finding_provider_fields_criticality, expected_type=type_hints["finding_provider_fields_criticality"])
                check_type(argname="argument finding_provider_fields_related_findings_id", value=finding_provider_fields_related_findings_id, expected_type=type_hints["finding_provider_fields_related_findings_id"])
                check_type(argname="argument finding_provider_fields_related_findings_product_arn", value=finding_provider_fields_related_findings_product_arn, expected_type=type_hints["finding_provider_fields_related_findings_product_arn"])
                check_type(argname="argument finding_provider_fields_severity_label", value=finding_provider_fields_severity_label, expected_type=type_hints["finding_provider_fields_severity_label"])
                check_type(argname="argument finding_provider_fields_severity_original", value=finding_provider_fields_severity_original, expected_type=type_hints["finding_provider_fields_severity_original"])
                check_type(argname="argument finding_provider_fields_types", value=finding_provider_fields_types, expected_type=type_hints["finding_provider_fields_types"])
                check_type(argname="argument first_observed_at", value=first_observed_at, expected_type=type_hints["first_observed_at"])
                check_type(argname="argument generator_id", value=generator_id, expected_type=type_hints["generator_id"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument keyword", value=keyword, expected_type=type_hints["keyword"])
                check_type(argname="argument last_observed_at", value=last_observed_at, expected_type=type_hints["last_observed_at"])
                check_type(argname="argument malware_name", value=malware_name, expected_type=type_hints["malware_name"])
                check_type(argname="argument malware_path", value=malware_path, expected_type=type_hints["malware_path"])
                check_type(argname="argument malware_state", value=malware_state, expected_type=type_hints["malware_state"])
                check_type(argname="argument malware_type", value=malware_type, expected_type=type_hints["malware_type"])
                check_type(argname="argument network_destination_domain", value=network_destination_domain, expected_type=type_hints["network_destination_domain"])
                check_type(argname="argument network_destination_ip_v4", value=network_destination_ip_v4, expected_type=type_hints["network_destination_ip_v4"])
                check_type(argname="argument network_destination_ip_v6", value=network_destination_ip_v6, expected_type=type_hints["network_destination_ip_v6"])
                check_type(argname="argument network_destination_port", value=network_destination_port, expected_type=type_hints["network_destination_port"])
                check_type(argname="argument network_direction", value=network_direction, expected_type=type_hints["network_direction"])
                check_type(argname="argument network_protocol", value=network_protocol, expected_type=type_hints["network_protocol"])
                check_type(argname="argument network_source_domain", value=network_source_domain, expected_type=type_hints["network_source_domain"])
                check_type(argname="argument network_source_ip_v4", value=network_source_ip_v4, expected_type=type_hints["network_source_ip_v4"])
                check_type(argname="argument network_source_ip_v6", value=network_source_ip_v6, expected_type=type_hints["network_source_ip_v6"])
                check_type(argname="argument network_source_mac", value=network_source_mac, expected_type=type_hints["network_source_mac"])
                check_type(argname="argument network_source_port", value=network_source_port, expected_type=type_hints["network_source_port"])
                check_type(argname="argument note_text", value=note_text, expected_type=type_hints["note_text"])
                check_type(argname="argument note_updated_at", value=note_updated_at, expected_type=type_hints["note_updated_at"])
                check_type(argname="argument note_updated_by", value=note_updated_by, expected_type=type_hints["note_updated_by"])
                check_type(argname="argument process_launched_at", value=process_launched_at, expected_type=type_hints["process_launched_at"])
                check_type(argname="argument process_name", value=process_name, expected_type=type_hints["process_name"])
                check_type(argname="argument process_parent_pid", value=process_parent_pid, expected_type=type_hints["process_parent_pid"])
                check_type(argname="argument process_path", value=process_path, expected_type=type_hints["process_path"])
                check_type(argname="argument process_pid", value=process_pid, expected_type=type_hints["process_pid"])
                check_type(argname="argument process_terminated_at", value=process_terminated_at, expected_type=type_hints["process_terminated_at"])
                check_type(argname="argument product_arn", value=product_arn, expected_type=type_hints["product_arn"])
                check_type(argname="argument product_fields", value=product_fields, expected_type=type_hints["product_fields"])
                check_type(argname="argument product_name", value=product_name, expected_type=type_hints["product_name"])
                check_type(argname="argument recommendation_text", value=recommendation_text, expected_type=type_hints["recommendation_text"])
                check_type(argname="argument record_state", value=record_state, expected_type=type_hints["record_state"])
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument related_findings_id", value=related_findings_id, expected_type=type_hints["related_findings_id"])
                check_type(argname="argument related_findings_product_arn", value=related_findings_product_arn, expected_type=type_hints["related_findings_product_arn"])
                check_type(argname="argument resource_application_arn", value=resource_application_arn, expected_type=type_hints["resource_application_arn"])
                check_type(argname="argument resource_application_name", value=resource_application_name, expected_type=type_hints["resource_application_name"])
                check_type(argname="argument resource_aws_ec2_instance_iam_instance_profile_arn", value=resource_aws_ec2_instance_iam_instance_profile_arn, expected_type=type_hints["resource_aws_ec2_instance_iam_instance_profile_arn"])
                check_type(argname="argument resource_aws_ec2_instance_image_id", value=resource_aws_ec2_instance_image_id, expected_type=type_hints["resource_aws_ec2_instance_image_id"])
                check_type(argname="argument resource_aws_ec2_instance_ip_v4_addresses", value=resource_aws_ec2_instance_ip_v4_addresses, expected_type=type_hints["resource_aws_ec2_instance_ip_v4_addresses"])
                check_type(argname="argument resource_aws_ec2_instance_ip_v6_addresses", value=resource_aws_ec2_instance_ip_v6_addresses, expected_type=type_hints["resource_aws_ec2_instance_ip_v6_addresses"])
                check_type(argname="argument resource_aws_ec2_instance_key_name", value=resource_aws_ec2_instance_key_name, expected_type=type_hints["resource_aws_ec2_instance_key_name"])
                check_type(argname="argument resource_aws_ec2_instance_launched_at", value=resource_aws_ec2_instance_launched_at, expected_type=type_hints["resource_aws_ec2_instance_launched_at"])
                check_type(argname="argument resource_aws_ec2_instance_subnet_id", value=resource_aws_ec2_instance_subnet_id, expected_type=type_hints["resource_aws_ec2_instance_subnet_id"])
                check_type(argname="argument resource_aws_ec2_instance_type", value=resource_aws_ec2_instance_type, expected_type=type_hints["resource_aws_ec2_instance_type"])
                check_type(argname="argument resource_aws_ec2_instance_vpc_id", value=resource_aws_ec2_instance_vpc_id, expected_type=type_hints["resource_aws_ec2_instance_vpc_id"])
                check_type(argname="argument resource_aws_iam_access_key_created_at", value=resource_aws_iam_access_key_created_at, expected_type=type_hints["resource_aws_iam_access_key_created_at"])
                check_type(argname="argument resource_aws_iam_access_key_principal_name", value=resource_aws_iam_access_key_principal_name, expected_type=type_hints["resource_aws_iam_access_key_principal_name"])
                check_type(argname="argument resource_aws_iam_access_key_status", value=resource_aws_iam_access_key_status, expected_type=type_hints["resource_aws_iam_access_key_status"])
                check_type(argname="argument resource_aws_iam_access_key_user_name", value=resource_aws_iam_access_key_user_name, expected_type=type_hints["resource_aws_iam_access_key_user_name"])
                check_type(argname="argument resource_aws_iam_user_user_name", value=resource_aws_iam_user_user_name, expected_type=type_hints["resource_aws_iam_user_user_name"])
                check_type(argname="argument resource_aws_s3_bucket_owner_id", value=resource_aws_s3_bucket_owner_id, expected_type=type_hints["resource_aws_s3_bucket_owner_id"])
                check_type(argname="argument resource_aws_s3_bucket_owner_name", value=resource_aws_s3_bucket_owner_name, expected_type=type_hints["resource_aws_s3_bucket_owner_name"])
                check_type(argname="argument resource_container_image_id", value=resource_container_image_id, expected_type=type_hints["resource_container_image_id"])
                check_type(argname="argument resource_container_image_name", value=resource_container_image_name, expected_type=type_hints["resource_container_image_name"])
                check_type(argname="argument resource_container_launched_at", value=resource_container_launched_at, expected_type=type_hints["resource_container_launched_at"])
                check_type(argname="argument resource_container_name", value=resource_container_name, expected_type=type_hints["resource_container_name"])
                check_type(argname="argument resource_details_other", value=resource_details_other, expected_type=type_hints["resource_details_other"])
                check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
                check_type(argname="argument resource_partition", value=resource_partition, expected_type=type_hints["resource_partition"])
                check_type(argname="argument resource_region", value=resource_region, expected_type=type_hints["resource_region"])
                check_type(argname="argument resource_tags", value=resource_tags, expected_type=type_hints["resource_tags"])
                check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
                check_type(argname="argument sample", value=sample, expected_type=type_hints["sample"])
                check_type(argname="argument severity_label", value=severity_label, expected_type=type_hints["severity_label"])
                check_type(argname="argument severity_normalized", value=severity_normalized, expected_type=type_hints["severity_normalized"])
                check_type(argname="argument severity_product", value=severity_product, expected_type=type_hints["severity_product"])
                check_type(argname="argument source_url", value=source_url, expected_type=type_hints["source_url"])
                check_type(argname="argument threat_intel_indicator_category", value=threat_intel_indicator_category, expected_type=type_hints["threat_intel_indicator_category"])
                check_type(argname="argument threat_intel_indicator_last_observed_at", value=threat_intel_indicator_last_observed_at, expected_type=type_hints["threat_intel_indicator_last_observed_at"])
                check_type(argname="argument threat_intel_indicator_source", value=threat_intel_indicator_source, expected_type=type_hints["threat_intel_indicator_source"])
                check_type(argname="argument threat_intel_indicator_source_url", value=threat_intel_indicator_source_url, expected_type=type_hints["threat_intel_indicator_source_url"])
                check_type(argname="argument threat_intel_indicator_type", value=threat_intel_indicator_type, expected_type=type_hints["threat_intel_indicator_type"])
                check_type(argname="argument threat_intel_indicator_value", value=threat_intel_indicator_value, expected_type=type_hints["threat_intel_indicator_value"])
                check_type(argname="argument title", value=title, expected_type=type_hints["title"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument updated_at", value=updated_at, expected_type=type_hints["updated_at"])
                check_type(argname="argument user_defined_fields", value=user_defined_fields, expected_type=type_hints["user_defined_fields"])
                check_type(argname="argument verification_state", value=verification_state, expected_type=type_hints["verification_state"])
                check_type(argname="argument vulnerabilities_exploit_available", value=vulnerabilities_exploit_available, expected_type=type_hints["vulnerabilities_exploit_available"])
                check_type(argname="argument vulnerabilities_fix_available", value=vulnerabilities_fix_available, expected_type=type_hints["vulnerabilities_fix_available"])
                check_type(argname="argument workflow_state", value=workflow_state, expected_type=type_hints["workflow_state"])
                check_type(argname="argument workflow_status", value=workflow_status, expected_type=type_hints["workflow_status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if aws_account_id is not None:
                self._values["aws_account_id"] = aws_account_id
            if aws_account_name is not None:
                self._values["aws_account_name"] = aws_account_name
            if company_name is not None:
                self._values["company_name"] = company_name
            if compliance_associated_standards_id is not None:
                self._values["compliance_associated_standards_id"] = compliance_associated_standards_id
            if compliance_security_control_id is not None:
                self._values["compliance_security_control_id"] = compliance_security_control_id
            if compliance_security_control_parameters_name is not None:
                self._values["compliance_security_control_parameters_name"] = compliance_security_control_parameters_name
            if compliance_security_control_parameters_value is not None:
                self._values["compliance_security_control_parameters_value"] = compliance_security_control_parameters_value
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
            if finding_provider_fields_confidence is not None:
                self._values["finding_provider_fields_confidence"] = finding_provider_fields_confidence
            if finding_provider_fields_criticality is not None:
                self._values["finding_provider_fields_criticality"] = finding_provider_fields_criticality
            if finding_provider_fields_related_findings_id is not None:
                self._values["finding_provider_fields_related_findings_id"] = finding_provider_fields_related_findings_id
            if finding_provider_fields_related_findings_product_arn is not None:
                self._values["finding_provider_fields_related_findings_product_arn"] = finding_provider_fields_related_findings_product_arn
            if finding_provider_fields_severity_label is not None:
                self._values["finding_provider_fields_severity_label"] = finding_provider_fields_severity_label
            if finding_provider_fields_severity_original is not None:
                self._values["finding_provider_fields_severity_original"] = finding_provider_fields_severity_original
            if finding_provider_fields_types is not None:
                self._values["finding_provider_fields_types"] = finding_provider_fields_types
            if first_observed_at is not None:
                self._values["first_observed_at"] = first_observed_at
            if generator_id is not None:
                self._values["generator_id"] = generator_id
            if id is not None:
                self._values["id"] = id
            if keyword is not None:
                self._values["keyword"] = keyword
            if last_observed_at is not None:
                self._values["last_observed_at"] = last_observed_at
            if malware_name is not None:
                self._values["malware_name"] = malware_name
            if malware_path is not None:
                self._values["malware_path"] = malware_path
            if malware_state is not None:
                self._values["malware_state"] = malware_state
            if malware_type is not None:
                self._values["malware_type"] = malware_type
            if network_destination_domain is not None:
                self._values["network_destination_domain"] = network_destination_domain
            if network_destination_ip_v4 is not None:
                self._values["network_destination_ip_v4"] = network_destination_ip_v4
            if network_destination_ip_v6 is not None:
                self._values["network_destination_ip_v6"] = network_destination_ip_v6
            if network_destination_port is not None:
                self._values["network_destination_port"] = network_destination_port
            if network_direction is not None:
                self._values["network_direction"] = network_direction
            if network_protocol is not None:
                self._values["network_protocol"] = network_protocol
            if network_source_domain is not None:
                self._values["network_source_domain"] = network_source_domain
            if network_source_ip_v4 is not None:
                self._values["network_source_ip_v4"] = network_source_ip_v4
            if network_source_ip_v6 is not None:
                self._values["network_source_ip_v6"] = network_source_ip_v6
            if network_source_mac is not None:
                self._values["network_source_mac"] = network_source_mac
            if network_source_port is not None:
                self._values["network_source_port"] = network_source_port
            if note_text is not None:
                self._values["note_text"] = note_text
            if note_updated_at is not None:
                self._values["note_updated_at"] = note_updated_at
            if note_updated_by is not None:
                self._values["note_updated_by"] = note_updated_by
            if process_launched_at is not None:
                self._values["process_launched_at"] = process_launched_at
            if process_name is not None:
                self._values["process_name"] = process_name
            if process_parent_pid is not None:
                self._values["process_parent_pid"] = process_parent_pid
            if process_path is not None:
                self._values["process_path"] = process_path
            if process_pid is not None:
                self._values["process_pid"] = process_pid
            if process_terminated_at is not None:
                self._values["process_terminated_at"] = process_terminated_at
            if product_arn is not None:
                self._values["product_arn"] = product_arn
            if product_fields is not None:
                self._values["product_fields"] = product_fields
            if product_name is not None:
                self._values["product_name"] = product_name
            if recommendation_text is not None:
                self._values["recommendation_text"] = recommendation_text
            if record_state is not None:
                self._values["record_state"] = record_state
            if region is not None:
                self._values["region"] = region
            if related_findings_id is not None:
                self._values["related_findings_id"] = related_findings_id
            if related_findings_product_arn is not None:
                self._values["related_findings_product_arn"] = related_findings_product_arn
            if resource_application_arn is not None:
                self._values["resource_application_arn"] = resource_application_arn
            if resource_application_name is not None:
                self._values["resource_application_name"] = resource_application_name
            if resource_aws_ec2_instance_iam_instance_profile_arn is not None:
                self._values["resource_aws_ec2_instance_iam_instance_profile_arn"] = resource_aws_ec2_instance_iam_instance_profile_arn
            if resource_aws_ec2_instance_image_id is not None:
                self._values["resource_aws_ec2_instance_image_id"] = resource_aws_ec2_instance_image_id
            if resource_aws_ec2_instance_ip_v4_addresses is not None:
                self._values["resource_aws_ec2_instance_ip_v4_addresses"] = resource_aws_ec2_instance_ip_v4_addresses
            if resource_aws_ec2_instance_ip_v6_addresses is not None:
                self._values["resource_aws_ec2_instance_ip_v6_addresses"] = resource_aws_ec2_instance_ip_v6_addresses
            if resource_aws_ec2_instance_key_name is not None:
                self._values["resource_aws_ec2_instance_key_name"] = resource_aws_ec2_instance_key_name
            if resource_aws_ec2_instance_launched_at is not None:
                self._values["resource_aws_ec2_instance_launched_at"] = resource_aws_ec2_instance_launched_at
            if resource_aws_ec2_instance_subnet_id is not None:
                self._values["resource_aws_ec2_instance_subnet_id"] = resource_aws_ec2_instance_subnet_id
            if resource_aws_ec2_instance_type is not None:
                self._values["resource_aws_ec2_instance_type"] = resource_aws_ec2_instance_type
            if resource_aws_ec2_instance_vpc_id is not None:
                self._values["resource_aws_ec2_instance_vpc_id"] = resource_aws_ec2_instance_vpc_id
            if resource_aws_iam_access_key_created_at is not None:
                self._values["resource_aws_iam_access_key_created_at"] = resource_aws_iam_access_key_created_at
            if resource_aws_iam_access_key_principal_name is not None:
                self._values["resource_aws_iam_access_key_principal_name"] = resource_aws_iam_access_key_principal_name
            if resource_aws_iam_access_key_status is not None:
                self._values["resource_aws_iam_access_key_status"] = resource_aws_iam_access_key_status
            if resource_aws_iam_access_key_user_name is not None:
                self._values["resource_aws_iam_access_key_user_name"] = resource_aws_iam_access_key_user_name
            if resource_aws_iam_user_user_name is not None:
                self._values["resource_aws_iam_user_user_name"] = resource_aws_iam_user_user_name
            if resource_aws_s3_bucket_owner_id is not None:
                self._values["resource_aws_s3_bucket_owner_id"] = resource_aws_s3_bucket_owner_id
            if resource_aws_s3_bucket_owner_name is not None:
                self._values["resource_aws_s3_bucket_owner_name"] = resource_aws_s3_bucket_owner_name
            if resource_container_image_id is not None:
                self._values["resource_container_image_id"] = resource_container_image_id
            if resource_container_image_name is not None:
                self._values["resource_container_image_name"] = resource_container_image_name
            if resource_container_launched_at is not None:
                self._values["resource_container_launched_at"] = resource_container_launched_at
            if resource_container_name is not None:
                self._values["resource_container_name"] = resource_container_name
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
            if sample is not None:
                self._values["sample"] = sample
            if severity_label is not None:
                self._values["severity_label"] = severity_label
            if severity_normalized is not None:
                self._values["severity_normalized"] = severity_normalized
            if severity_product is not None:
                self._values["severity_product"] = severity_product
            if source_url is not None:
                self._values["source_url"] = source_url
            if threat_intel_indicator_category is not None:
                self._values["threat_intel_indicator_category"] = threat_intel_indicator_category
            if threat_intel_indicator_last_observed_at is not None:
                self._values["threat_intel_indicator_last_observed_at"] = threat_intel_indicator_last_observed_at
            if threat_intel_indicator_source is not None:
                self._values["threat_intel_indicator_source"] = threat_intel_indicator_source
            if threat_intel_indicator_source_url is not None:
                self._values["threat_intel_indicator_source_url"] = threat_intel_indicator_source_url
            if threat_intel_indicator_type is not None:
                self._values["threat_intel_indicator_type"] = threat_intel_indicator_type
            if threat_intel_indicator_value is not None:
                self._values["threat_intel_indicator_value"] = threat_intel_indicator_value
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
            if vulnerabilities_exploit_available is not None:
                self._values["vulnerabilities_exploit_available"] = vulnerabilities_exploit_available
            if vulnerabilities_fix_available is not None:
                self._values["vulnerabilities_fix_available"] = vulnerabilities_fix_available
            if workflow_state is not None:
                self._values["workflow_state"] = workflow_state
            if workflow_status is not None:
                self._values["workflow_status"] = workflow_status

        @builtins.property
        def aws_account_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The AWS account ID in which a finding is generated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-awsaccountid
            '''
            result = self._values.get("aws_account_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def aws_account_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The name of the AWS account in which a finding is generated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-awsaccountname
            '''
            result = self._values.get("aws_account_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def company_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The name of the findings provider (company) that owns the solution (product) that generates findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-companyname
            '''
            result = self._values.get("company_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def compliance_associated_standards_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The unique identifier of a standard in which a control is enabled.

            This field consists of the resource portion of the Amazon Resource Name (ARN) returned for a standard in the `DescribeStandards <https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html>`_ API response.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-complianceassociatedstandardsid
            '''
            result = self._values.get("compliance_associated_standards_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def compliance_security_control_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The unique identifier of a control across standards.

            Values for this field typically consist of an AWS service and a number, such as APIGateway.5.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-compliancesecuritycontrolid
            '''
            result = self._values.get("compliance_security_control_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def compliance_security_control_parameters_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The name of a security control parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-compliancesecuritycontrolparametersname
            '''
            result = self._values.get("compliance_security_control_parameters_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def compliance_security_control_parameters_value(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The current value of a security control parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-compliancesecuritycontrolparametersvalue
            '''
            result = self._values.get("compliance_security_control_parameters_value")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def compliance_status(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''Exclusive to findings that are generated as the result of a check run against a specific rule in a supported standard, such as CIS AWS Foundations.

            Contains security standard-related finding details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-compliancestatus
            '''
            result = self._values.get("compliance_status")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def confidence(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.NumberFilterProperty"]]]]:
            '''A finding's confidence.

            Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify.

            Confidence is scored on a 0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100 percent confidence.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-confidence
            '''
            result = self._values.get("confidence")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.NumberFilterProperty"]]]], result)

        @builtins.property
        def created_at(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.DateFilterProperty"]]]]:
            '''A timestamp that indicates when the security findings provider created the potential security issue that a finding reflects.

            This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples:

            - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` )
            - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` )
            - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-createdat
            '''
            result = self._values.get("created_at")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.DateFilterProperty"]]]], result)

        @builtins.property
        def criticality(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.NumberFilterProperty"]]]]:
            '''The level of importance assigned to the resources associated with the finding.

            A score of 0 means that the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-criticality
            '''
            result = self._values.get("criticality")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.NumberFilterProperty"]]]], result)

        @builtins.property
        def description(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''A finding's description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def finding_provider_fields_confidence(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.NumberFilterProperty"]]]]:
            '''The finding provider value for the finding confidence.

            Confidence is defined as the likelihood that a finding accurately identifies the behavior or issue that it was intended to identify.

            Confidence is scored on a 0-100 basis using a ratio scale, where 0 means zero percent confidence and 100 means 100 percent confidence.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldsconfidence
            '''
            result = self._values.get("finding_provider_fields_confidence")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.NumberFilterProperty"]]]], result)

        @builtins.property
        def finding_provider_fields_criticality(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.NumberFilterProperty"]]]]:
            '''The finding provider value for the level of importance assigned to the resources associated with the findings.

            A score of 0 means that the underlying resources have no criticality, and a score of 100 is reserved for the most critical resources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldscriticality
            '''
            result = self._values.get("finding_provider_fields_criticality")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.NumberFilterProperty"]]]], result)

        @builtins.property
        def finding_provider_fields_related_findings_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The finding identifier of a related finding that is identified by the finding provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldsrelatedfindingsid
            '''
            result = self._values.get("finding_provider_fields_related_findings_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def finding_provider_fields_related_findings_product_arn(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The ARN of the solution that generated a related finding that is identified by the finding provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldsrelatedfindingsproductarn
            '''
            result = self._values.get("finding_provider_fields_related_findings_product_arn")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def finding_provider_fields_severity_label(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The finding provider value for the severity label.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldsseveritylabel
            '''
            result = self._values.get("finding_provider_fields_severity_label")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def finding_provider_fields_severity_original(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The finding provider's original value for the severity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldsseverityoriginal
            '''
            result = self._values.get("finding_provider_fields_severity_original")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def finding_provider_fields_types(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''One or more finding types that the finding provider assigned to the finding.

            Uses the format of ``namespace/category/classifier`` that classify a finding.

            Valid namespace values are: Software and Configuration Checks | TTPs | Effects | Unusual Behaviors | Sensitive Data Identifications

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-findingproviderfieldstypes
            '''
            result = self._values.get("finding_provider_fields_types")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def first_observed_at(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.DateFilterProperty"]]]]:
            '''A timestamp that indicates when the security findings provider first observed the potential security issue that a finding captured.

            This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples:

            - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` )
            - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` )
            - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-firstobservedat
            '''
            result = self._values.get("first_observed_at")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.DateFilterProperty"]]]], result)

        @builtins.property
        def generator_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The identifier for the solution-specific component (a discrete unit of logic) that generated a finding.

            In various security findings providers' solutions, this generator can be called a rule, a check, a detector, a plugin, etc.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-generatorid
            '''
            result = self._values.get("generator_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The security findings provider-specific identifier for a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-id
            '''
            result = self._values.get("id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def keyword(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.KeywordFilterProperty"]]]]:
            '''This field is deprecated.

            A keyword for a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-keyword
            '''
            result = self._values.get("keyword")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.KeywordFilterProperty"]]]], result)

        @builtins.property
        def last_observed_at(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.DateFilterProperty"]]]]:
            '''A timestamp that indicates when the security findings provider most recently observed the potential security issue that a finding captured.

            This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples:

            - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` )
            - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` )
            - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-lastobservedat
            '''
            result = self._values.get("last_observed_at")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.DateFilterProperty"]]]], result)

        @builtins.property
        def malware_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The name of the malware that was observed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-malwarename
            '''
            result = self._values.get("malware_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def malware_path(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The filesystem path of the malware that was observed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-malwarepath
            '''
            result = self._values.get("malware_path")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def malware_state(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The state of the malware that was observed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-malwarestate
            '''
            result = self._values.get("malware_state")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def malware_type(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The type of the malware that was observed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-malwaretype
            '''
            result = self._values.get("malware_type")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def network_destination_domain(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The destination domain of network-related information about a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-networkdestinationdomain
            '''
            result = self._values.get("network_destination_domain")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def network_destination_ip_v4(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.IpFilterProperty"]]]]:
            '''The destination IPv4 address of network-related information about a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-networkdestinationipv4
            '''
            result = self._values.get("network_destination_ip_v4")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.IpFilterProperty"]]]], result)

        @builtins.property
        def network_destination_ip_v6(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.IpFilterProperty"]]]]:
            '''The destination IPv6 address of network-related information about a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-networkdestinationipv6
            '''
            result = self._values.get("network_destination_ip_v6")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.IpFilterProperty"]]]], result)

        @builtins.property
        def network_destination_port(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.NumberFilterProperty"]]]]:
            '''The destination port of network-related information about a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-networkdestinationport
            '''
            result = self._values.get("network_destination_port")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.NumberFilterProperty"]]]], result)

        @builtins.property
        def network_direction(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''Indicates the direction of network traffic associated with a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-networkdirection
            '''
            result = self._values.get("network_direction")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def network_protocol(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The protocol of network-related information about a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-networkprotocol
            '''
            result = self._values.get("network_protocol")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def network_source_domain(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The source domain of network-related information about a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-networksourcedomain
            '''
            result = self._values.get("network_source_domain")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def network_source_ip_v4(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.IpFilterProperty"]]]]:
            '''The source IPv4 address of network-related information about a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-networksourceipv4
            '''
            result = self._values.get("network_source_ip_v4")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.IpFilterProperty"]]]], result)

        @builtins.property
        def network_source_ip_v6(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.IpFilterProperty"]]]]:
            '''The source IPv6 address of network-related information about a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-networksourceipv6
            '''
            result = self._values.get("network_source_ip_v6")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.IpFilterProperty"]]]], result)

        @builtins.property
        def network_source_mac(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The source media access control (MAC) address of network-related information about a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-networksourcemac
            '''
            result = self._values.get("network_source_mac")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def network_source_port(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.NumberFilterProperty"]]]]:
            '''The source port of network-related information about a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-networksourceport
            '''
            result = self._values.get("network_source_port")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.NumberFilterProperty"]]]], result)

        @builtins.property
        def note_text(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The text of a note.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-notetext
            '''
            result = self._values.get("note_text")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def note_updated_at(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.DateFilterProperty"]]]]:
            '''The timestamp of when the note was updated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-noteupdatedat
            '''
            result = self._values.get("note_updated_at")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.DateFilterProperty"]]]], result)

        @builtins.property
        def note_updated_by(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The principal that created a note.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-noteupdatedby
            '''
            result = self._values.get("note_updated_by")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def process_launched_at(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.DateFilterProperty"]]]]:
            '''A timestamp that identifies when the process was launched.

            This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples:

            - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` )
            - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` )
            - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-processlaunchedat
            '''
            result = self._values.get("process_launched_at")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.DateFilterProperty"]]]], result)

        @builtins.property
        def process_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The name of the process.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-processname
            '''
            result = self._values.get("process_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def process_parent_pid(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.NumberFilterProperty"]]]]:
            '''The parent process ID.

            This field accepts positive integers between ``O`` and ``2147483647`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-processparentpid
            '''
            result = self._values.get("process_parent_pid")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.NumberFilterProperty"]]]], result)

        @builtins.property
        def process_path(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The path to the process executable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-processpath
            '''
            result = self._values.get("process_path")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def process_pid(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.NumberFilterProperty"]]]]:
            '''The process ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-processpid
            '''
            result = self._values.get("process_pid")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.NumberFilterProperty"]]]], result)

        @builtins.property
        def process_terminated_at(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.DateFilterProperty"]]]]:
            '''A timestamp that identifies when the process was terminated.

            This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples:

            - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` )
            - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` )
            - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-processterminatedat
            '''
            result = self._values.get("process_terminated_at")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.DateFilterProperty"]]]], result)

        @builtins.property
        def product_arn(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The ARN generated by Security Hub that uniquely identifies a third-party company (security findings provider) after this provider's product (solution that generates findings) is registered with Security Hub.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-productarn
            '''
            result = self._values.get("product_arn")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def product_fields(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.MapFilterProperty"]]]]:
            '''A data type where security findings providers can include additional solution-specific details that aren't part of the defined ``AwsSecurityFinding`` format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-productfields
            '''
            result = self._values.get("product_fields")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.MapFilterProperty"]]]], result)

        @builtins.property
        def product_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The name of the solution (product) that generates findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-productname
            '''
            result = self._values.get("product_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def recommendation_text(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The recommendation of what to do about the issue described in a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-recommendationtext
            '''
            result = self._values.get("recommendation_text")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def record_state(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The updated record state for the finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-recordstate
            '''
            result = self._values.get("record_state")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def region(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The Region from which the finding was generated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-region
            '''
            result = self._values.get("region")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def related_findings_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The solution-generated identifier for a related finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-relatedfindingsid
            '''
            result = self._values.get("related_findings_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def related_findings_product_arn(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The ARN of the solution that generated a related finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-relatedfindingsproductarn
            '''
            result = self._values.get("related_findings_product_arn")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_application_arn(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The ARN of the application that is related to a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourceapplicationarn
            '''
            result = self._values.get("resource_application_arn")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_application_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The name of the application that is related to a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourceapplicationname
            '''
            result = self._values.get("resource_application_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_aws_ec2_instance_iam_instance_profile_arn(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The IAM profile ARN of the instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instanceiaminstanceprofilearn
            '''
            result = self._values.get("resource_aws_ec2_instance_iam_instance_profile_arn")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_aws_ec2_instance_image_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The Amazon Machine Image (AMI) ID of the instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instanceimageid
            '''
            result = self._values.get("resource_aws_ec2_instance_image_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_aws_ec2_instance_ip_v4_addresses(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.IpFilterProperty"]]]]:
            '''The IPv4 addresses associated with the instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instanceipv4addresses
            '''
            result = self._values.get("resource_aws_ec2_instance_ip_v4_addresses")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.IpFilterProperty"]]]], result)

        @builtins.property
        def resource_aws_ec2_instance_ip_v6_addresses(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.IpFilterProperty"]]]]:
            '''The IPv6 addresses associated with the instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instanceipv6addresses
            '''
            result = self._values.get("resource_aws_ec2_instance_ip_v6_addresses")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.IpFilterProperty"]]]], result)

        @builtins.property
        def resource_aws_ec2_instance_key_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The key name associated with the instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instancekeyname
            '''
            result = self._values.get("resource_aws_ec2_instance_key_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_aws_ec2_instance_launched_at(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.DateFilterProperty"]]]]:
            '''The date and time the instance was launched.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instancelaunchedat
            '''
            result = self._values.get("resource_aws_ec2_instance_launched_at")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.DateFilterProperty"]]]], result)

        @builtins.property
        def resource_aws_ec2_instance_subnet_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The identifier of the subnet that the instance was launched in.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instancesubnetid
            '''
            result = self._values.get("resource_aws_ec2_instance_subnet_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_aws_ec2_instance_type(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The instance type of the instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instancetype
            '''
            result = self._values.get("resource_aws_ec2_instance_type")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_aws_ec2_instance_vpc_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The identifier of the VPC that the instance was launched in.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsec2instancevpcid
            '''
            result = self._values.get("resource_aws_ec2_instance_vpc_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_aws_iam_access_key_created_at(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.DateFilterProperty"]]]]:
            '''The creation date/time of the IAM access key related to a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsiamaccesskeycreatedat
            '''
            result = self._values.get("resource_aws_iam_access_key_created_at")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.DateFilterProperty"]]]], result)

        @builtins.property
        def resource_aws_iam_access_key_principal_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The name of the principal that is associated with an IAM access key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsiamaccesskeyprincipalname
            '''
            result = self._values.get("resource_aws_iam_access_key_principal_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_aws_iam_access_key_status(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The status of the IAM access key related to a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsiamaccesskeystatus
            '''
            result = self._values.get("resource_aws_iam_access_key_status")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_aws_iam_access_key_user_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''This field is deprecated.

            The username associated with the IAM access key related to a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsiamaccesskeyusername
            '''
            result = self._values.get("resource_aws_iam_access_key_user_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_aws_iam_user_user_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The name of an IAM user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourceawsiamuserusername
            '''
            result = self._values.get("resource_aws_iam_user_user_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_aws_s3_bucket_owner_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The canonical user ID of the owner of the S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourceawss3bucketownerid
            '''
            result = self._values.get("resource_aws_s3_bucket_owner_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_aws_s3_bucket_owner_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The display name of the owner of the S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourceawss3bucketownername
            '''
            result = self._values.get("resource_aws_s3_bucket_owner_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_container_image_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The identifier of the image related to a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourcecontainerimageid
            '''
            result = self._values.get("resource_container_image_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_container_image_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The name of the image related to a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourcecontainerimagename
            '''
            result = self._values.get("resource_container_image_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_container_launched_at(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.DateFilterProperty"]]]]:
            '''A timestamp that identifies when the container was started.

            This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples:

            - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` )
            - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` )
            - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourcecontainerlaunchedat
            '''
            result = self._values.get("resource_container_launched_at")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.DateFilterProperty"]]]], result)

        @builtins.property
        def resource_container_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The name of the container related to a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourcecontainername
            '''
            result = self._values.get("resource_container_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_details_other(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.MapFilterProperty"]]]]:
            '''The details of a resource that doesn't have a specific subfield for the resource type defined.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourcedetailsother
            '''
            result = self._values.get("resource_details_other")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.MapFilterProperty"]]]], result)

        @builtins.property
        def resource_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The canonical identifier for the given resource type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourceid
            '''
            result = self._values.get("resource_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_partition(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The canonical AWS partition name that the Region is assigned to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourcepartition
            '''
            result = self._values.get("resource_partition")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_region(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The canonical AWS external Region name where this resource is located.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourceregion
            '''
            result = self._values.get("resource_region")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_tags(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.MapFilterProperty"]]]]:
            '''A list of AWS tags associated with a resource at the time the finding was processed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourcetags
            '''
            result = self._values.get("resource_tags")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.MapFilterProperty"]]]], result)

        @builtins.property
        def resource_type(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''Specifies the type of the resource that details are provided for.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-resourcetype
            '''
            result = self._values.get("resource_type")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def sample(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.BooleanFilterProperty"]]]]:
            '''Indicates whether or not sample findings are included in the filter results.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-sample
            '''
            result = self._values.get("sample")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.BooleanFilterProperty"]]]], result)

        @builtins.property
        def severity_label(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The label of a finding's severity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-severitylabel
            '''
            result = self._values.get("severity_label")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def severity_normalized(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.NumberFilterProperty"]]]]:
            '''Deprecated. The normalized severity of a finding. Instead of providing ``Normalized`` , provide ``Label`` .

            The value of ``Normalized`` can be an integer between ``0`` and ``100`` .

            If you provide ``Label`` and do not provide ``Normalized`` , then ``Normalized`` is set automatically as follows.

            - ``INFORMATIONAL`` - 0
            - ``LOW`` - 1
            - ``MEDIUM`` - 40
            - ``HIGH`` - 70
            - ``CRITICAL`` - 90

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-severitynormalized
            '''
            result = self._values.get("severity_normalized")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.NumberFilterProperty"]]]], result)

        @builtins.property
        def severity_product(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.NumberFilterProperty"]]]]:
            '''Deprecated. This attribute isn't included in findings. Instead of providing ``Product`` , provide ``Original`` .

            The native severity as defined by the AWS service or integrated partner product that generated the finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-severityproduct
            '''
            result = self._values.get("severity_product")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.NumberFilterProperty"]]]], result)

        @builtins.property
        def source_url(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''A URL that links to a page about the current finding in the security findings provider's solution.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-sourceurl
            '''
            result = self._values.get("source_url")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def threat_intel_indicator_category(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The category of a threat intelligence indicator.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-threatintelindicatorcategory
            '''
            result = self._values.get("threat_intel_indicator_category")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def threat_intel_indicator_last_observed_at(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.DateFilterProperty"]]]]:
            '''A timestamp that identifies the last observation of a threat intelligence indicator.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-threatintelindicatorlastobservedat
            '''
            result = self._values.get("threat_intel_indicator_last_observed_at")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.DateFilterProperty"]]]], result)

        @builtins.property
        def threat_intel_indicator_source(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The source of the threat intelligence.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-threatintelindicatorsource
            '''
            result = self._values.get("threat_intel_indicator_source")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def threat_intel_indicator_source_url(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The URL for more details from the source of the threat intelligence.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-threatintelindicatorsourceurl
            '''
            result = self._values.get("threat_intel_indicator_source_url")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def threat_intel_indicator_type(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The type of a threat intelligence indicator.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-threatintelindicatortype
            '''
            result = self._values.get("threat_intel_indicator_type")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def threat_intel_indicator_value(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The value of a threat intelligence indicator.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-threatintelindicatorvalue
            '''
            result = self._values.get("threat_intel_indicator_value")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def title(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''A finding's title.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-title
            '''
            result = self._values.get("title")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def type(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''A finding type in the format of ``namespace/category/classifier`` that classifies a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def updated_at(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.DateFilterProperty"]]]]:
            '''A timestamp that indicates when the security findings provider last updated the finding record.

            This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples:

            - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` )
            - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` )
            - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-updatedat
            '''
            result = self._values.get("updated_at")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.DateFilterProperty"]]]], result)

        @builtins.property
        def user_defined_fields(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.MapFilterProperty"]]]]:
            '''A list of name/value string pairs associated with the finding.

            These are custom, user-defined fields added to a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-userdefinedfields
            '''
            result = self._values.get("user_defined_fields")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.MapFilterProperty"]]]], result)

        @builtins.property
        def verification_state(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The veracity of a finding.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-verificationstate
            '''
            result = self._values.get("verification_state")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def vulnerabilities_exploit_available(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''Indicates whether a software vulnerability in your environment has a known exploit.

            You can filter findings by this field only if you use Security Hub and Amazon Inspector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-vulnerabilitiesexploitavailable
            '''
            result = self._values.get("vulnerabilities_exploit_available")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def vulnerabilities_fix_available(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''Indicates whether a vulnerability is fixed in a newer version of the affected software packages.

            You can filter findings by this field only if you use Security Hub and Amazon Inspector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-vulnerabilitiesfixavailable
            '''
            result = self._values.get("vulnerabilities_fix_available")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def workflow_state(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The workflow state of a finding.

            Note that this field is deprecated. To search for a finding based on its workflow status, use ``WorkflowStatus`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-workflowstate
            '''
            result = self._values.get("workflow_state")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        @builtins.property
        def workflow_status(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]]:
            '''The status of the investigation into a finding. Allowed values are the following.

            - ``NEW`` - The initial state of a finding, before it is reviewed.

            Security Hub also resets the workflow status from ``NOTIFIED`` or ``RESOLVED`` to ``NEW`` in the following cases:

            - ``RecordState`` changes from ``ARCHIVED`` to ``ACTIVE`` .
            - ``Compliance.Status`` changes from ``PASSED`` to either ``WARNING`` , ``FAILED`` , or ``NOT_AVAILABLE`` .
            - ``NOTIFIED`` - Indicates that the resource owner has been notified about the security issue. Used when the initial reviewer is not the resource owner, and needs intervention from the resource owner.

            If one of the following occurs, the workflow status is changed automatically from ``NOTIFIED`` to ``NEW`` :

            - ``RecordState`` changes from ``ARCHIVED`` to ``ACTIVE`` .
            - ``Compliance.Status`` changes from ``PASSED`` to ``FAILED`` , ``WARNING`` , or ``NOT_AVAILABLE`` .
            - ``SUPPRESSED`` - Indicates that you reviewed the finding and do not believe that any action is needed.

            The workflow status of a ``SUPPRESSED`` finding does not change if ``RecordState`` changes from ``ARCHIVED`` to ``ACTIVE`` .

            - ``RESOLVED`` - The finding was reviewed and remediated and is now considered resolved.

            The finding remains ``RESOLVED`` unless one of the following occurs:

            - ``RecordState`` changes from ``ARCHIVED`` to ``ACTIVE`` .
            - ``Compliance.Status`` changes from ``PASSED`` to ``FAILED`` , ``WARNING`` , or ``NOT_AVAILABLE`` .

            In those cases, the workflow status is automatically reset to ``NEW`` .

            For findings from controls, if ``Compliance.Status`` is ``PASSED`` , then Security Hub automatically sets the workflow status to ``RESOLVED`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-awssecurityfindingfilters.html#cfn-securityhub-insight-awssecurityfindingfilters-workflowstatus
            '''
            result = self._values.get("workflow_status")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInsight.StringFilterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AwsSecurityFindingFiltersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityhub.CfnInsight.BooleanFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"value": "value"},
    )
    class BooleanFilterProperty:
        def __init__(
            self,
            *,
            value: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''Boolean filter for querying findings.

            :param value: The value of the boolean.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-booleanfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityhub as securityhub
                
                boolean_filter_property = securityhub.CfnInsight.BooleanFilterProperty(
                    value=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a5a7b05d1f5476886d210727e9a8fbb00921baaea17579194f4516a64aabf91f)
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "value": value,
            }

        @builtins.property
        def value(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''The value of the boolean.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-booleanfilter.html#cfn-securityhub-insight-booleanfilter-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BooleanFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityhub.CfnInsight.DateFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"date_range": "dateRange", "end": "end", "start": "start"},
    )
    class DateFilterProperty:
        def __init__(
            self,
            *,
            date_range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInsight.DateRangeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            end: typing.Optional[builtins.str] = None,
            start: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A date filter for querying findings.

            :param date_range: A date range for the date filter.
            :param end: A timestamp that provides the end date for the date filter. This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples: - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` ) - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` ) - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )
            :param start: A timestamp that provides the start date for the date filter. This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples: - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` ) - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` ) - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` ) - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-datefilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityhub as securityhub
                
                date_filter_property = securityhub.CfnInsight.DateFilterProperty(
                    date_range=securityhub.CfnInsight.DateRangeProperty(
                        unit="unit",
                        value=123
                    ),
                    end="end",
                    start="start"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9cb480e997d22aaa214323658210a916b5a4f15c6d303951222410878eaba867)
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
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInsight.DateRangeProperty"]]:
            '''A date range for the date filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-datefilter.html#cfn-securityhub-insight-datefilter-daterange
            '''
            result = self._values.get("date_range")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInsight.DateRangeProperty"]], result)

        @builtins.property
        def end(self) -> typing.Optional[builtins.str]:
            '''A timestamp that provides the end date for the date filter.

            This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples:

            - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` )
            - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` )
            - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-datefilter.html#cfn-securityhub-insight-datefilter-end
            '''
            result = self._values.get("end")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def start(self) -> typing.Optional[builtins.str]:
            '''A timestamp that provides the start date for the date filter.

            This field accepts only the specified formats. Timestamps can end with ``Z`` or ``("+" / "-") time-hour [":" time-minute]`` . The time-secfrac after seconds is limited to a maximum of 9 digits. The offset is bounded by +/-18:00. Here are valid timestamp formats with examples:

            - ``YYYY-MM-DDTHH:MM:SSZ`` (for example, ``2019-01-31T23:00:00Z`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmmZ`` (for example, ``2019-01-31T23:00:00.123456789Z`` )
            - ``YYYY-MM-DDTHH:MM:SS+HH:MM`` (for example, ``2024-01-04T15:25:10+17:59`` )
            - ``YYYY-MM-DDTHH:MM:SS-HHMM`` (for example, ``2024-01-04T15:25:10-1759`` )
            - ``YYYY-MM-DDTHH:MM:SS.mmmmmmmmm+HH:MM`` (for example, ``2024-01-04T15:25:10.123456789+17:59`` )

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-datefilter.html#cfn-securityhub-insight-datefilter-start
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
        jsii_type="aws-cdk-lib.aws_securityhub.CfnInsight.DateRangeProperty",
        jsii_struct_bases=[],
        name_mapping={"unit": "unit", "value": "value"},
    )
    class DateRangeProperty:
        def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
            '''A date range for the date filter.

            :param unit: A date range unit for the date filter.
            :param value: A date range value for the date filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-daterange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityhub as securityhub
                
                date_range_property = securityhub.CfnInsight.DateRangeProperty(
                    unit="unit",
                    value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f123ee938660323ad366a17d236071df2194961f4f09f39d83658361ca33c941)
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "unit": unit,
                "value": value,
            }

        @builtins.property
        def unit(self) -> builtins.str:
            '''A date range unit for the date filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-daterange.html#cfn-securityhub-insight-daterange-unit
            '''
            result = self._values.get("unit")
            assert result is not None, "Required property 'unit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> jsii.Number:
            '''A date range value for the date filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-daterange.html#cfn-securityhub-insight-daterange-value
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
        jsii_type="aws-cdk-lib.aws_securityhub.CfnInsight.IpFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"cidr": "cidr"},
    )
    class IpFilterProperty:
        def __init__(self, *, cidr: builtins.str) -> None:
            '''The IP filter for querying findings.

            :param cidr: A finding's CIDR value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-ipfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityhub as securityhub
                
                ip_filter_property = securityhub.CfnInsight.IpFilterProperty(
                    cidr="cidr"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7a04baf7fe373b7822c226f4ba3f79fd13f1a39d5b79f07450e0a0494e6b0319)
                check_type(argname="argument cidr", value=cidr, expected_type=type_hints["cidr"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cidr": cidr,
            }

        @builtins.property
        def cidr(self) -> builtins.str:
            '''A finding's CIDR value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-ipfilter.html#cfn-securityhub-insight-ipfilter-cidr
            '''
            result = self._values.get("cidr")
            assert result is not None, "Required property 'cidr' is missing"
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
        jsii_type="aws-cdk-lib.aws_securityhub.CfnInsight.KeywordFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"value": "value"},
    )
    class KeywordFilterProperty:
        def __init__(self, *, value: builtins.str) -> None:
            '''A keyword filter for querying findings.

            :param value: A value for the keyword.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-keywordfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityhub as securityhub
                
                keyword_filter_property = securityhub.CfnInsight.KeywordFilterProperty(
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c908713b4949b1a8de0bfb063114bb136fa9a8dafe7b791ef5e54068c0430ee3)
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "value": value,
            }

        @builtins.property
        def value(self) -> builtins.str:
            '''A value for the keyword.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-keywordfilter.html#cfn-securityhub-insight-keywordfilter-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeywordFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityhub.CfnInsight.MapFilterProperty",
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

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-mapfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityhub as securityhub
                
                map_filter_property = securityhub.CfnInsight.MapFilterProperty(
                    comparison="comparison",
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c48d5892081a7948f12fe8af08fabcacdd4aefd7ff391339639ac358218e2aef)
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

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-mapfilter.html#cfn-securityhub-insight-mapfilter-comparison
            '''
            result = self._values.get("comparison")
            assert result is not None, "Required property 'comparison' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''The key of the map filter.

            For example, for ``ResourceTags`` , ``Key`` identifies the name of the tag. For ``UserDefinedFields`` , ``Key`` is the name of the field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-mapfilter.html#cfn-securityhub-insight-mapfilter-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value for the key in the map filter.

            Filter values are case sensitive. For example, one of the values for a tag called ``Department`` might be ``Security`` . If you provide ``security`` as the filter value, then there's no match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-mapfilter.html#cfn-securityhub-insight-mapfilter-value
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
        jsii_type="aws-cdk-lib.aws_securityhub.CfnInsight.NumberFilterProperty",
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

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-numberfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityhub as securityhub
                
                number_filter_property = securityhub.CfnInsight.NumberFilterProperty(
                    eq=123,
                    gte=123,
                    lte=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6f97ed6463c5d2ffdf4de2022130ff68a5e527ac150694985b9605e4e5df8b05)
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

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-numberfilter.html#cfn-securityhub-insight-numberfilter-eq
            '''
            result = self._values.get("eq")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def gte(self) -> typing.Optional[jsii.Number]:
            '''The greater-than-equal condition to be applied to a single field when querying for findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-numberfilter.html#cfn-securityhub-insight-numberfilter-gte
            '''
            result = self._values.get("gte")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def lte(self) -> typing.Optional[jsii.Number]:
            '''The less-than-equal condition to be applied to a single field when querying for findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-numberfilter.html#cfn-securityhub-insight-numberfilter-lte
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
        jsii_type="aws-cdk-lib.aws_securityhub.CfnInsight.StringFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"comparison": "comparison", "value": "value"},
    )
    class StringFilterProperty:
        def __init__(self, *, comparison: builtins.str, value: builtins.str) -> None:
            '''A string filter for filtering AWS Security Hub findings.

            :param comparison: The condition to apply to a string value when filtering Security Hub findings. To search for values that have the filter value, use one of the following comparison operators: - To search for values that include the filter value, use ``CONTAINS`` . For example, the filter ``Title CONTAINS CloudFront`` matches findings that have a ``Title`` that includes the string CloudFront. - To search for values that exactly match the filter value, use ``EQUALS`` . For example, the filter ``AwsAccountId EQUALS 123456789012`` only matches findings that have an account ID of ``123456789012`` . - To search for values that start with the filter value, use ``PREFIX`` . For example, the filter ``ResourceRegion PREFIX us`` matches findings that have a ``ResourceRegion`` that starts with ``us`` . A ``ResourceRegion`` that starts with a different value, such as ``af`` , ``ap`` , or ``ca`` , doesn't match. ``CONTAINS`` , ``EQUALS`` , and ``PREFIX`` filters on the same field are joined by ``OR`` . A finding matches if it matches any one of those filters. For example, the filters ``Title CONTAINS CloudFront OR Title CONTAINS CloudWatch`` match a finding that includes either ``CloudFront`` , ``CloudWatch`` , or both strings in the title. To search for values that don’t have the filter value, use one of the following comparison operators: - To search for values that exclude the filter value, use ``NOT_CONTAINS`` . For example, the filter ``Title NOT_CONTAINS CloudFront`` matches findings that have a ``Title`` that excludes the string CloudFront. - To search for values other than the filter value, use ``NOT_EQUALS`` . For example, the filter ``AwsAccountId NOT_EQUALS 123456789012`` only matches findings that have an account ID other than ``123456789012`` . - To search for values that don't start with the filter value, use ``PREFIX_NOT_EQUALS`` . For example, the filter ``ResourceRegion PREFIX_NOT_EQUALS us`` matches findings with a ``ResourceRegion`` that starts with a value other than ``us`` . ``NOT_CONTAINS`` , ``NOT_EQUALS`` , and ``PREFIX_NOT_EQUALS`` filters on the same field are joined by ``AND`` . A finding matches only if it matches all of those filters. For example, the filters ``Title NOT_CONTAINS CloudFront AND Title NOT_CONTAINS CloudWatch`` match a finding that excludes both ``CloudFront`` and ``CloudWatch`` in the title. You can’t have both a ``CONTAINS`` filter and a ``NOT_CONTAINS`` filter on the same field. Similarly, you can't provide both an ``EQUALS`` filter and a ``NOT_EQUALS`` or ``PREFIX_NOT_EQUALS`` filter on the same field. Combining filters in this way returns an error. ``CONTAINS`` filters can only be used with other ``CONTAINS`` filters. ``NOT_CONTAINS`` filters can only be used with other ``NOT_CONTAINS`` filters. You can combine ``PREFIX`` filters with ``NOT_EQUALS`` or ``PREFIX_NOT_EQUALS`` filters for the same field. Security Hub first processes the ``PREFIX`` filters, and then the ``NOT_EQUALS`` or ``PREFIX_NOT_EQUALS`` filters. For example, for the following filters, Security Hub first identifies findings that have resource types that start with either ``AwsIam`` or ``AwsEc2`` . It then excludes findings that have a resource type of ``AwsIamPolicy`` and findings that have a resource type of ``AwsEc2NetworkInterface`` . - ``ResourceType PREFIX AwsIam`` - ``ResourceType PREFIX AwsEc2`` - ``ResourceType NOT_EQUALS AwsIamPolicy`` - ``ResourceType NOT_EQUALS AwsEc2NetworkInterface`` ``CONTAINS`` and ``NOT_CONTAINS`` operators can be used only with automation rules. For more information, see `Automation rules <https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html>`_ in the *AWS Security Hub User Guide* .
            :param value: The string filter value. Filter values are case sensitive. For example, the product name for control-based findings is ``Security Hub`` . If you provide ``security hub`` as the filter value, there's no match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-stringfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityhub as securityhub
                
                string_filter_property = securityhub.CfnInsight.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__334c5662d5059b01b0797e56b688a03d7d992a0448888f48c768913865cb8255)
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

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-stringfilter.html#cfn-securityhub-insight-stringfilter-comparison
            '''
            result = self._values.get("comparison")
            assert result is not None, "Required property 'comparison' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The string filter value.

            Filter values are case sensitive. For example, the product name for control-based findings is ``Security Hub`` . If you provide ``security hub`` as the filter value, there's no match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-insight-stringfilter.html#cfn-securityhub-insight-stringfilter-value
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
    jsii_type="aws-cdk-lib.aws_securityhub.CfnInsightProps",
    jsii_struct_bases=[],
    name_mapping={
        "filters": "filters",
        "group_by_attribute": "groupByAttribute",
        "name": "name",
    },
)
class CfnInsightProps:
    def __init__(
        self,
        *,
        filters: typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.AwsSecurityFindingFiltersProperty, typing.Dict[builtins.str, typing.Any]]],
        group_by_attribute: builtins.str,
        name: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnInsight``.

        :param filters: One or more attributes used to filter the findings included in the insight. The insight only includes findings that match the criteria defined in the filters. You can filter by up to ten finding attributes. For each attribute, you can provide up to 20 filter values.
        :param group_by_attribute: The grouping attribute for the insight's findings. Indicates how to group the matching findings, and identifies the type of item that the insight applies to. For example, if an insight is grouped by resource identifier, then the insight produces a list of resource identifiers.
        :param name: The name of a Security Hub insight.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-insight.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_securityhub as securityhub
            
            cfn_insight_props = securityhub.CfnInsightProps(
                filters=securityhub.CfnInsight.AwsSecurityFindingFiltersProperty(
                    aws_account_id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    aws_account_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    company_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    compliance_associated_standards_id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    compliance_security_control_id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    compliance_security_control_parameters_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    compliance_security_control_parameters_value=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    compliance_status=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    confidence=[securityhub.CfnInsight.NumberFilterProperty(
                        eq=123,
                        gte=123,
                        lte=123
                    )],
                    created_at=[securityhub.CfnInsight.DateFilterProperty(
                        date_range=securityhub.CfnInsight.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    criticality=[securityhub.CfnInsight.NumberFilterProperty(
                        eq=123,
                        gte=123,
                        lte=123
                    )],
                    description=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    finding_provider_fields_confidence=[securityhub.CfnInsight.NumberFilterProperty(
                        eq=123,
                        gte=123,
                        lte=123
                    )],
                    finding_provider_fields_criticality=[securityhub.CfnInsight.NumberFilterProperty(
                        eq=123,
                        gte=123,
                        lte=123
                    )],
                    finding_provider_fields_related_findings_id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    finding_provider_fields_related_findings_product_arn=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    finding_provider_fields_severity_label=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    finding_provider_fields_severity_original=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    finding_provider_fields_types=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    first_observed_at=[securityhub.CfnInsight.DateFilterProperty(
                        date_range=securityhub.CfnInsight.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    generator_id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    keyword=[securityhub.CfnInsight.KeywordFilterProperty(
                        value="value"
                    )],
                    last_observed_at=[securityhub.CfnInsight.DateFilterProperty(
                        date_range=securityhub.CfnInsight.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    malware_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    malware_path=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    malware_state=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    malware_type=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    network_destination_domain=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    network_destination_ip_v4=[securityhub.CfnInsight.IpFilterProperty(
                        cidr="cidr"
                    )],
                    network_destination_ip_v6=[securityhub.CfnInsight.IpFilterProperty(
                        cidr="cidr"
                    )],
                    network_destination_port=[securityhub.CfnInsight.NumberFilterProperty(
                        eq=123,
                        gte=123,
                        lte=123
                    )],
                    network_direction=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    network_protocol=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    network_source_domain=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    network_source_ip_v4=[securityhub.CfnInsight.IpFilterProperty(
                        cidr="cidr"
                    )],
                    network_source_ip_v6=[securityhub.CfnInsight.IpFilterProperty(
                        cidr="cidr"
                    )],
                    network_source_mac=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    network_source_port=[securityhub.CfnInsight.NumberFilterProperty(
                        eq=123,
                        gte=123,
                        lte=123
                    )],
                    note_text=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    note_updated_at=[securityhub.CfnInsight.DateFilterProperty(
                        date_range=securityhub.CfnInsight.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    note_updated_by=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    process_launched_at=[securityhub.CfnInsight.DateFilterProperty(
                        date_range=securityhub.CfnInsight.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    process_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    process_parent_pid=[securityhub.CfnInsight.NumberFilterProperty(
                        eq=123,
                        gte=123,
                        lte=123
                    )],
                    process_path=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    process_pid=[securityhub.CfnInsight.NumberFilterProperty(
                        eq=123,
                        gte=123,
                        lte=123
                    )],
                    process_terminated_at=[securityhub.CfnInsight.DateFilterProperty(
                        date_range=securityhub.CfnInsight.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    product_arn=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    product_fields=[securityhub.CfnInsight.MapFilterProperty(
                        comparison="comparison",
                        key="key",
                        value="value"
                    )],
                    product_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    recommendation_text=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    record_state=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    region=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    related_findings_id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    related_findings_product_arn=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_application_arn=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_application_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_aws_ec2_instance_iam_instance_profile_arn=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_aws_ec2_instance_image_id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_aws_ec2_instance_ip_v4_addresses=[securityhub.CfnInsight.IpFilterProperty(
                        cidr="cidr"
                    )],
                    resource_aws_ec2_instance_ip_v6_addresses=[securityhub.CfnInsight.IpFilterProperty(
                        cidr="cidr"
                    )],
                    resource_aws_ec2_instance_key_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_aws_ec2_instance_launched_at=[securityhub.CfnInsight.DateFilterProperty(
                        date_range=securityhub.CfnInsight.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    resource_aws_ec2_instance_subnet_id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_aws_ec2_instance_type=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_aws_ec2_instance_vpc_id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_aws_iam_access_key_created_at=[securityhub.CfnInsight.DateFilterProperty(
                        date_range=securityhub.CfnInsight.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    resource_aws_iam_access_key_principal_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_aws_iam_access_key_status=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_aws_iam_access_key_user_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_aws_iam_user_user_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_aws_s3_bucket_owner_id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_aws_s3_bucket_owner_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_container_image_id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_container_image_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_container_launched_at=[securityhub.CfnInsight.DateFilterProperty(
                        date_range=securityhub.CfnInsight.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    resource_container_name=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_details_other=[securityhub.CfnInsight.MapFilterProperty(
                        comparison="comparison",
                        key="key",
                        value="value"
                    )],
                    resource_id=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_partition=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_region=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_tags=[securityhub.CfnInsight.MapFilterProperty(
                        comparison="comparison",
                        key="key",
                        value="value"
                    )],
                    resource_type=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    sample=[securityhub.CfnInsight.BooleanFilterProperty(
                        value=False
                    )],
                    severity_label=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    severity_normalized=[securityhub.CfnInsight.NumberFilterProperty(
                        eq=123,
                        gte=123,
                        lte=123
                    )],
                    severity_product=[securityhub.CfnInsight.NumberFilterProperty(
                        eq=123,
                        gte=123,
                        lte=123
                    )],
                    source_url=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    threat_intel_indicator_category=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    threat_intel_indicator_last_observed_at=[securityhub.CfnInsight.DateFilterProperty(
                        date_range=securityhub.CfnInsight.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    threat_intel_indicator_source=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    threat_intel_indicator_source_url=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    threat_intel_indicator_type=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    threat_intel_indicator_value=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    title=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    type=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    updated_at=[securityhub.CfnInsight.DateFilterProperty(
                        date_range=securityhub.CfnInsight.DateRangeProperty(
                            unit="unit",
                            value=123
                        ),
                        end="end",
                        start="start"
                    )],
                    user_defined_fields=[securityhub.CfnInsight.MapFilterProperty(
                        comparison="comparison",
                        key="key",
                        value="value"
                    )],
                    verification_state=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    vulnerabilities_exploit_available=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    vulnerabilities_fix_available=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    workflow_state=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    workflow_status=[securityhub.CfnInsight.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )]
                ),
                group_by_attribute="groupByAttribute",
                name="name"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__592cb12c63690d3f829ab7f245b3d227f77eaa3657e0fd4c8452bc7d2a8ed3f8)
            check_type(argname="argument filters", value=filters, expected_type=type_hints["filters"])
            check_type(argname="argument group_by_attribute", value=group_by_attribute, expected_type=type_hints["group_by_attribute"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "filters": filters,
            "group_by_attribute": group_by_attribute,
            "name": name,
        }

    @builtins.property
    def filters(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnInsight.AwsSecurityFindingFiltersProperty]:
        '''One or more attributes used to filter the findings included in the insight.

        The insight only includes findings that match the criteria defined in the filters. You can filter by up to ten finding attributes. For each attribute, you can provide up to 20 filter values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-insight.html#cfn-securityhub-insight-filters
        '''
        result = self._values.get("filters")
        assert result is not None, "Required property 'filters' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnInsight.AwsSecurityFindingFiltersProperty], result)

    @builtins.property
    def group_by_attribute(self) -> builtins.str:
        '''The grouping attribute for the insight's findings.

        Indicates how to group the matching findings, and identifies the type of item that the insight applies to. For example, if an insight is grouped by resource identifier, then the insight produces a list of resource identifiers.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-insight.html#cfn-securityhub-insight-groupbyattribute
        '''
        result = self._values.get("group_by_attribute")
        assert result is not None, "Required property 'group_by_attribute' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of a Security Hub insight.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-insight.html#cfn-securityhub-insight-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInsightProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnProductSubscription(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_securityhub.CfnProductSubscription",
):
    '''The ``AWS::SecurityHub::ProductSubscription`` resource creates a subscription to a third-party product that generates findings that you want to receive in AWS Security Hub .

    For a list of integrations to third-party products, see `Available third-party partner product integrations <https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-partner-providers.html>`_ in the *AWS Security Hub User Guide* .

    To change a product subscription, remove the current product subscription resource, and then create a new one.

    Tags aren't supported for this resource.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-productsubscription.html
    :cloudformationResource: AWS::SecurityHub::ProductSubscription
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_securityhub as securityhub
        
        cfn_product_subscription = securityhub.CfnProductSubscription(self, "MyCfnProductSubscription",
            product_arn="productArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        product_arn: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param product_arn: The ARN of the product to enable the integration for.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45ff00dc1d7d1ca799678f5a142f5b951b1d37a1f101efd45167c0d18d8a8593)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProductSubscriptionProps(product_arn=product_arn)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2609f0db7b096ee9ba1823dba2f6a7b3f67772749f5637c04ca2f35698c45651)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1b4fc7b3dc1098174b63be9cc3fb55214b9d990ac65e3b77855b5668f4b8fa9c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrProductSubscriptionArn")
    def attr_product_subscription_arn(self) -> builtins.str:
        '''The ARN of your subscription to the product to enable integrations for.

        :cloudformationAttribute: ProductSubscriptionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProductSubscriptionArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="productArn")
    def product_arn(self) -> builtins.str:
        '''The ARN of the product to enable the integration for.'''
        return typing.cast(builtins.str, jsii.get(self, "productArn"))

    @product_arn.setter
    def product_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e63b86460e92e5a56fd9d1eaf71d8f57c62718a7502fdde0b9cc7898029252a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "productArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_securityhub.CfnProductSubscriptionProps",
    jsii_struct_bases=[],
    name_mapping={"product_arn": "productArn"},
)
class CfnProductSubscriptionProps:
    def __init__(self, *, product_arn: builtins.str) -> None:
        '''Properties for defining a ``CfnProductSubscription``.

        :param product_arn: The ARN of the product to enable the integration for.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-productsubscription.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_securityhub as securityhub
            
            cfn_product_subscription_props = securityhub.CfnProductSubscriptionProps(
                product_arn="productArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1bfdbbfd3a598a5b02234a0dfd7a548ca422910244f63e8798ff35dfb927389)
            check_type(argname="argument product_arn", value=product_arn, expected_type=type_hints["product_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "product_arn": product_arn,
        }

    @builtins.property
    def product_arn(self) -> builtins.str:
        '''The ARN of the product to enable the integration for.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-productsubscription.html#cfn-securityhub-productsubscription-productarn
        '''
        result = self._values.get("product_arn")
        assert result is not None, "Required property 'product_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProductSubscriptionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSecurityControl(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_securityhub.CfnSecurityControl",
):
    '''A security control in Security Hub describes a security best practice related to a specific resource.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-securitycontrol.html
    :cloudformationResource: AWS::SecurityHub::SecurityControl
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_securityhub as securityhub
        
        cfn_security_control = securityhub.CfnSecurityControl(self, "MyCfnSecurityControl",
            parameters={
                "parameters_key": securityhub.CfnSecurityControl.ParameterConfigurationProperty(
                    value_type="valueType"
                )
            },
        
            # the properties below are optional
            last_update_reason="lastUpdateReason",
            security_control_arn="securityControlArn",
            security_control_id="securityControlId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        parameters: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnSecurityControl.ParameterConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]],
        last_update_reason: typing.Optional[builtins.str] = None,
        security_control_arn: typing.Optional[builtins.str] = None,
        security_control_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param parameters: 
        :param last_update_reason: The most recent reason for updating the customizable properties of a security control. This differs from the UpdateReason field of the BatchUpdateStandardsControlAssociations API, which tracks the reason for updating the enablement status of a control. This field accepts alphanumeric characters in addition to white spaces, dashes, and underscores.
        :param security_control_arn: 
        :param security_control_id: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__726fa705fd558de76e132e75c55b8475c62b8dc48c449b5a702f64b1f4bff214)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSecurityControlProps(
            parameters=parameters,
            last_update_reason=last_update_reason,
            security_control_arn=security_control_arn,
            security_control_id=security_control_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72e19ace58419cf7e5cc55ad38fcc4775e0c46952b1855a7a5ce7a6181b02400)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dedfe4cee5ed4d744f654a047ae9cf47ebabdaf6eef2879ed46833422d93c9b7)
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
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnSecurityControl.ParameterConfigurationProperty"]]]:
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnSecurityControl.ParameterConfigurationProperty"]]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnSecurityControl.ParameterConfigurationProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba42fae33edc1f1aa919c0aa456d75e2059314d6bb1a4b1deec59b91ddaeaf4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="lastUpdateReason")
    def last_update_reason(self) -> typing.Optional[builtins.str]:
        '''The most recent reason for updating the customizable properties of a security control.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lastUpdateReason"))

    @last_update_reason.setter
    def last_update_reason(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b44d1cfbd6f5b9cc0e4f01d2215ab6605103c5dd09dd732f99604233458a89a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lastUpdateReason", value)

    @builtins.property
    @jsii.member(jsii_name="securityControlArn")
    def security_control_arn(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityControlArn"))

    @security_control_arn.setter
    def security_control_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4478e81bddb9f9df8efd5c0032ddfb869fb7885b4a68ad3bdb3c327deb03328a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityControlArn", value)

    @builtins.property
    @jsii.member(jsii_name="securityControlId")
    def security_control_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityControlId"))

    @security_control_id.setter
    def security_control_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff55fd11201a4a7c92e4e58e9fa5bcdb6762a8ac0310ada761c3b90158e2f5e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityControlId", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securityhub.CfnSecurityControl.ParameterConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"value_type": "valueType"},
    )
    class ParameterConfigurationProperty:
        def __init__(self, *, value_type: builtins.str) -> None:
            '''
            :param value_type: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-securitycontrol-parameterconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securityhub as securityhub
                
                parameter_configuration_property = securityhub.CfnSecurityControl.ParameterConfigurationProperty(
                    value_type="valueType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b4f8a75fb36fae6899e2291977edacf36a70ed147a49bd553150965029bec549)
                check_type(argname="argument value_type", value=value_type, expected_type=type_hints["value_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "value_type": value_type,
            }

        @builtins.property
        def value_type(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securityhub-securitycontrol-parameterconfiguration.html#cfn-securityhub-securitycontrol-parameterconfiguration-valuetype
            '''
            result = self._values.get("value_type")
            assert result is not None, "Required property 'value_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParameterConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_securityhub.CfnSecurityControlProps",
    jsii_struct_bases=[],
    name_mapping={
        "parameters": "parameters",
        "last_update_reason": "lastUpdateReason",
        "security_control_arn": "securityControlArn",
        "security_control_id": "securityControlId",
    },
)
class CfnSecurityControlProps:
    def __init__(
        self,
        *,
        parameters: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityControl.ParameterConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
        last_update_reason: typing.Optional[builtins.str] = None,
        security_control_arn: typing.Optional[builtins.str] = None,
        security_control_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSecurityControl``.

        :param parameters: 
        :param last_update_reason: The most recent reason for updating the customizable properties of a security control. This differs from the UpdateReason field of the BatchUpdateStandardsControlAssociations API, which tracks the reason for updating the enablement status of a control. This field accepts alphanumeric characters in addition to white spaces, dashes, and underscores.
        :param security_control_arn: 
        :param security_control_id: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-securitycontrol.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_securityhub as securityhub
            
            cfn_security_control_props = securityhub.CfnSecurityControlProps(
                parameters={
                    "parameters_key": securityhub.CfnSecurityControl.ParameterConfigurationProperty(
                        value_type="valueType"
                    )
                },
            
                # the properties below are optional
                last_update_reason="lastUpdateReason",
                security_control_arn="securityControlArn",
                security_control_id="securityControlId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__592aeb56f2970a16d30327b0b500710f94ac9725954a4c60fb68c82fd900e348)
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument last_update_reason", value=last_update_reason, expected_type=type_hints["last_update_reason"])
            check_type(argname="argument security_control_arn", value=security_control_arn, expected_type=type_hints["security_control_arn"])
            check_type(argname="argument security_control_id", value=security_control_id, expected_type=type_hints["security_control_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "parameters": parameters,
        }
        if last_update_reason is not None:
            self._values["last_update_reason"] = last_update_reason
        if security_control_arn is not None:
            self._values["security_control_arn"] = security_control_arn
        if security_control_id is not None:
            self._values["security_control_id"] = security_control_id

    @builtins.property
    def parameters(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnSecurityControl.ParameterConfigurationProperty]]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-securitycontrol.html#cfn-securityhub-securitycontrol-parameters
        '''
        result = self._values.get("parameters")
        assert result is not None, "Required property 'parameters' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnSecurityControl.ParameterConfigurationProperty]]], result)

    @builtins.property
    def last_update_reason(self) -> typing.Optional[builtins.str]:
        '''The most recent reason for updating the customizable properties of a security control.

        This differs from the UpdateReason field of the BatchUpdateStandardsControlAssociations API, which tracks the reason for updating the enablement status of a control. This field accepts alphanumeric characters in addition to white spaces, dashes, and underscores.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-securitycontrol.html#cfn-securityhub-securitycontrol-lastupdatereason
        '''
        result = self._values.get("last_update_reason")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_control_arn(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-securitycontrol.html#cfn-securityhub-securitycontrol-securitycontrolarn
        '''
        result = self._values.get("security_control_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_control_id(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-securitycontrol.html#cfn-securityhub-securitycontrol-securitycontrolid
        '''
        result = self._values.get("security_control_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSecurityControlProps(%s)" % ", ".join(
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
    :cloudformationResource: AWS::SecurityHub::Standard
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
    "CfnDelegatedAdmin",
    "CfnDelegatedAdminProps",
    "CfnHub",
    "CfnHubProps",
    "CfnInsight",
    "CfnInsightProps",
    "CfnProductSubscription",
    "CfnProductSubscriptionProps",
    "CfnSecurityControl",
    "CfnSecurityControlProps",
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
    user_defined_fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
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

def _typecheckingstub__e27e329e801cb67f6ec71f03a054a574103f5946def22c1bfdcd99ba50827d58(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    admin_account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baaaa369299b88b2085a28b2af39aa2abf07ab6772dc8c3ce8044a9ef9ea4df7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c0e442efc9a3d07aaf74da8d8d9132c602da0b1c240bc4589e6ce7e3e2459a3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5fdd5db8baf5624dbb4185acb8020d5499aa459d03967b97375912c3e6844c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bccd0acf2d461662eef1addff325ba8fe883439d680f7762ea393681a481c0ca(
    *,
    admin_account_id: builtins.str,
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

def _typecheckingstub__d671d628902c96b28f2d378ea3f0a99fe19e13873725f86dd92bbe36b4c9a166(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    filters: typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.AwsSecurityFindingFiltersProperty, typing.Dict[builtins.str, typing.Any]]],
    group_by_attribute: builtins.str,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12375a912637f8bdf52366060d1f39a683bdba181f295acc48a50989fdd81232(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a18620bef3bfa4a37ce6dbea7bd1e144bc38b0403e564d72f00f996c67a180a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40bc93b289fd6fbe5ea66bbe5f8eca6d1371fec0a59789022949021156c016a4(
    value: typing.Union[_IResolvable_da3f097b, CfnInsight.AwsSecurityFindingFiltersProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__645260a48ef5fcfdb2acc56551dd1e6897e309e4feef6d7b81e9aa50ad0cc353(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__766e42c726b2c502b30c5c9ccf965e83324fe1b106e1918e14b49c7f3b6cb61c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f929ea28f5698af2f86b0f581baee2cb87fe5520179930ea0794beb525d75f5d(
    *,
    aws_account_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    aws_account_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    company_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    compliance_associated_standards_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    compliance_security_control_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    compliance_security_control_parameters_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    compliance_security_control_parameters_value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    compliance_status: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    confidence: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.NumberFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    created_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.DateFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    criticality: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.NumberFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    finding_provider_fields_confidence: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.NumberFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    finding_provider_fields_criticality: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.NumberFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    finding_provider_fields_related_findings_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    finding_provider_fields_related_findings_product_arn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    finding_provider_fields_severity_label: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    finding_provider_fields_severity_original: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    finding_provider_fields_types: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    first_observed_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.DateFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    generator_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    keyword: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.KeywordFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    last_observed_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.DateFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    malware_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    malware_path: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    malware_state: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    malware_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    network_destination_domain: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    network_destination_ip_v4: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.IpFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    network_destination_ip_v6: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.IpFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    network_destination_port: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.NumberFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    network_direction: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    network_protocol: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    network_source_domain: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    network_source_ip_v4: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.IpFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    network_source_ip_v6: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.IpFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    network_source_mac: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    network_source_port: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.NumberFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    note_text: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    note_updated_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.DateFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    note_updated_by: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    process_launched_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.DateFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    process_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    process_parent_pid: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.NumberFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    process_path: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    process_pid: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.NumberFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    process_terminated_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.DateFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    product_arn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    product_fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.MapFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    product_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    recommendation_text: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    record_state: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    region: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    related_findings_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    related_findings_product_arn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_application_arn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_application_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_aws_ec2_instance_iam_instance_profile_arn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_aws_ec2_instance_image_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_aws_ec2_instance_ip_v4_addresses: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.IpFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_aws_ec2_instance_ip_v6_addresses: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.IpFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_aws_ec2_instance_key_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_aws_ec2_instance_launched_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.DateFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_aws_ec2_instance_subnet_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_aws_ec2_instance_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_aws_ec2_instance_vpc_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_aws_iam_access_key_created_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.DateFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_aws_iam_access_key_principal_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_aws_iam_access_key_status: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_aws_iam_access_key_user_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_aws_iam_user_user_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_aws_s3_bucket_owner_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_aws_s3_bucket_owner_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_container_image_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_container_image_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_container_launched_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.DateFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_container_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_details_other: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.MapFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_partition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_region: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.MapFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    sample: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.BooleanFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    severity_label: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    severity_normalized: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.NumberFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    severity_product: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.NumberFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    source_url: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    threat_intel_indicator_category: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    threat_intel_indicator_last_observed_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.DateFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    threat_intel_indicator_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    threat_intel_indicator_source_url: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    threat_intel_indicator_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    threat_intel_indicator_value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    title: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    updated_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.DateFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    user_defined_fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.MapFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    verification_state: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    vulnerabilities_exploit_available: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    vulnerabilities_fix_available: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    workflow_state: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    workflow_status: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5a7b05d1f5476886d210727e9a8fbb00921baaea17579194f4516a64aabf91f(
    *,
    value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cb480e997d22aaa214323658210a916b5a4f15c6d303951222410878eaba867(
    *,
    date_range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.DateRangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    end: typing.Optional[builtins.str] = None,
    start: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f123ee938660323ad366a17d236071df2194961f4f09f39d83658361ca33c941(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a04baf7fe373b7822c226f4ba3f79fd13f1a39d5b79f07450e0a0494e6b0319(
    *,
    cidr: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c908713b4949b1a8de0bfb063114bb136fa9a8dafe7b791ef5e54068c0430ee3(
    *,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c48d5892081a7948f12fe8af08fabcacdd4aefd7ff391339639ac358218e2aef(
    *,
    comparison: builtins.str,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f97ed6463c5d2ffdf4de2022130ff68a5e527ac150694985b9605e4e5df8b05(
    *,
    eq: typing.Optional[jsii.Number] = None,
    gte: typing.Optional[jsii.Number] = None,
    lte: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__334c5662d5059b01b0797e56b688a03d7d992a0448888f48c768913865cb8255(
    *,
    comparison: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__592cb12c63690d3f829ab7f245b3d227f77eaa3657e0fd4c8452bc7d2a8ed3f8(
    *,
    filters: typing.Union[_IResolvable_da3f097b, typing.Union[CfnInsight.AwsSecurityFindingFiltersProperty, typing.Dict[builtins.str, typing.Any]]],
    group_by_attribute: builtins.str,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45ff00dc1d7d1ca799678f5a142f5b951b1d37a1f101efd45167c0d18d8a8593(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    product_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2609f0db7b096ee9ba1823dba2f6a7b3f67772749f5637c04ca2f35698c45651(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b4fc7b3dc1098174b63be9cc3fb55214b9d990ac65e3b77855b5668f4b8fa9c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e63b86460e92e5a56fd9d1eaf71d8f57c62718a7502fdde0b9cc7898029252a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1bfdbbfd3a598a5b02234a0dfd7a548ca422910244f63e8798ff35dfb927389(
    *,
    product_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__726fa705fd558de76e132e75c55b8475c62b8dc48c449b5a702f64b1f4bff214(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    parameters: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityControl.ParameterConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    last_update_reason: typing.Optional[builtins.str] = None,
    security_control_arn: typing.Optional[builtins.str] = None,
    security_control_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72e19ace58419cf7e5cc55ad38fcc4775e0c46952b1855a7a5ce7a6181b02400(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dedfe4cee5ed4d744f654a047ae9cf47ebabdaf6eef2879ed46833422d93c9b7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba42fae33edc1f1aa919c0aa456d75e2059314d6bb1a4b1deec59b91ddaeaf4e(
    value: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnSecurityControl.ParameterConfigurationProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b44d1cfbd6f5b9cc0e4f01d2215ab6605103c5dd09dd732f99604233458a89a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4478e81bddb9f9df8efd5c0032ddfb869fb7885b4a68ad3bdb3c327deb03328a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff55fd11201a4a7c92e4e58e9fa5bcdb6762a8ac0310ada761c3b90158e2f5e4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4f8a75fb36fae6899e2291977edacf36a70ed147a49bd553150965029bec549(
    *,
    value_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__592aeb56f2970a16d30327b0b500710f94ac9725954a4c60fb68c82fd900e348(
    *,
    parameters: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityControl.ParameterConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    last_update_reason: typing.Optional[builtins.str] = None,
    security_control_arn: typing.Optional[builtins.str] = None,
    security_control_id: typing.Optional[builtins.str] = None,
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
