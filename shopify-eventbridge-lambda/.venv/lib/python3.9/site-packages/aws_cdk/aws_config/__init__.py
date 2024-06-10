'''
# AWS Config Construct Library

[AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) provides a detailed view of the configuration of AWS resources in your AWS account.
This includes how the resources are related to one another and how they were configured in the
past so that you can see how the configurations and relationships change over time.

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

## Initial Setup

Before using the constructs provided in this module, you need to set up AWS Config
in the region in which it will be used. This setup includes the one-time creation of the
following resources per region:

* `ConfigurationRecorder`: Configure which resources will be recorded for config changes.
* `DeliveryChannel`: Configure where to store the recorded data.

The following guides provide the steps for getting started with AWS Config:

* [Using the AWS Console](https://docs.aws.amazon.com/config/latest/developerguide/gs-console.html)
* [Using the AWS CLI](https://docs.aws.amazon.com/config/latest/developerguide/gs-cli.html)

## Rules

AWS Config can evaluate the configuration settings of your AWS resources by creating AWS Config rules,
which represent your ideal configuration settings.

See [Evaluating Resources with AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) to learn more about AWS Config rules.

### AWS Managed Rules

AWS Config provides AWS managed rules, which are predefined, customizable rules that AWS Config
uses to evaluate whether your AWS resources comply with common best practices.

For example, you could create a managed rule that checks whether active access keys are rotated
within the number of days specified.

```python
# https://docs.aws.amazon.com/config/latest/developerguide/access-keys-rotated.html
config.ManagedRule(self, "AccessKeysRotated",
    identifier=config.ManagedRuleIdentifiers.ACCESS_KEYS_ROTATED,
    input_parameters={
        "max_access_key_age": 60
    },

    # default is 24 hours
    maximum_execution_frequency=config.MaximumExecutionFrequency.TWELVE_HOURS
)
```

Identifiers for AWS managed rules are available through static constants in the `ManagedRuleIdentifiers` class.
You can find supported input parameters in the [List of AWS Config Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html).

The following higher level constructs for AWS managed rules are available.

#### Access Key rotation

Checks whether your active access keys are rotated within the number of days specified.

```python
# compliant if access keys have been rotated within the last 90 days
config.AccessKeysRotated(self, "AccessKeyRotated")
```

#### CloudFormation Stack drift detection

Checks whether your CloudFormation stack's actual configuration differs, or has drifted,
from it's expected configuration.

```python
# compliant if stack's status is 'IN_SYNC'
# non-compliant if the stack's drift status is 'DRIFTED'
config.CloudFormationStackDriftDetectionCheck(self, "Drift",
    own_stack_only=True
)
```

#### CloudFormation Stack notifications

Checks whether your CloudFormation stacks are sending event notifications to a SNS topic.

```python
# topics to which CloudFormation stacks may send event notifications
topic1 = sns.Topic(self, "AllowedTopic1")
topic2 = sns.Topic(self, "AllowedTopic2")

# non-compliant if CloudFormation stack does not send notifications to 'topic1' or 'topic2'
config.CloudFormationStackNotificationCheck(self, "NotificationCheck",
    topics=[topic1, topic2]
)
```

### Custom rules

You can develop custom rules and add them to AWS Config. You associate each custom rule with an
AWS Lambda function and Guard.

#### Custom Lambda Rules

Lambda function which contains the logic that evaluates whether your AWS resources comply with the rule.

```python
# Lambda function containing logic that evaluates compliance with the rule.
eval_compliance_fn = lambda_.Function(self, "CustomFunction",
    code=lambda_.AssetCode.from_inline("exports.handler = (event) => console.log(event);"),
    handler="index.handler",
    runtime=lambda_.Runtime.NODEJS_18_X
)

# A custom rule that runs on configuration changes of EC2 instances
custom_rule = config.CustomRule(self, "Custom",
    configuration_changes=True,
    lambda_function=eval_compliance_fn,
    rule_scope=config.RuleScope.from_resource(config.ResourceType.EC2_INSTANCE)
)
```

#### Custom Policy Rules

Guard which contains the logic that evaluates whether your AWS resources comply with the rule.

```python
sample_policy_text = """
# This rule checks if point in time recovery (PITR) is enabled on active Amazon DynamoDB tables
let status = ['ACTIVE']

rule tableisactive when
    resourceType == "AWS::DynamoDB::Table" {
    configuration.tableStatus == %status
}

rule checkcompliance when
    resourceType == "AWS::DynamoDB::Table"
    tableisactive {
        let pitr = supplementaryConfiguration.ContinuousBackupsDescription.pointInTimeRecoveryDescription.pointInTimeRecoveryStatus
        %pitr == "ENABLED"
}
"""

config.CustomPolicy(self, "Custom",
    policy_text=sample_policy_text,
    enable_debug_log=True,
    rule_scope=config.RuleScope.from_resources([config.ResourceType.DYNAMODB_TABLE
    ])
)
```

### Triggers

AWS Lambda executes functions in response to events that are published by AWS Services.
The function for a custom Config rule receives an event that is published by AWS Config,
and is responsible for evaluating the compliance of the rule.

Evaluations can be triggered by configuration changes, periodically, or both.
To create a custom rule, define a `CustomRule` and specify the Lambda Function
to run and the trigger types.

```python
# eval_compliance_fn: lambda.Function


config.CustomRule(self, "CustomRule",
    lambda_function=eval_compliance_fn,
    configuration_changes=True,
    periodic=True,

    # default is 24 hours
    maximum_execution_frequency=config.MaximumExecutionFrequency.SIX_HOURS
)
```

When the trigger for a rule occurs, the Lambda function is invoked by publishing an event.
See [example events for AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_example-events.html)

The AWS documentation has examples of Lambda functions for evaluations that are
[triggered by configuration changes](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_nodejs-sample.html#event-based-example-rule) and [triggered periodically](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_nodejs-sample.html#periodic-example-rule)

### Scope

By default rules are triggered by changes to all [resources](https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources).

Use the `RuleScope` APIs (`fromResource()`, `fromResources()` or `fromTag()`) to restrict
the scope of both managed and custom rules:

```python
# eval_compliance_fn: lambda.Function
ssh_rule = config.ManagedRule(self, "SSH",
    identifier=config.ManagedRuleIdentifiers.EC2_SECURITY_GROUPS_INCOMING_SSH_DISABLED,
    rule_scope=config.RuleScope.from_resource(config.ResourceType.EC2_SECURITY_GROUP, "sg-1234567890abcdefgh")
)
custom_rule = config.CustomRule(self, "Lambda",
    lambda_function=eval_compliance_fn,
    configuration_changes=True,
    rule_scope=config.RuleScope.from_resources([config.ResourceType.CLOUDFORMATION_STACK, config.ResourceType.S3_BUCKET])
)

tag_rule = config.CustomRule(self, "CostCenterTagRule",
    lambda_function=eval_compliance_fn,
    configuration_changes=True,
    rule_scope=config.RuleScope.from_tag("Cost Center", "MyApp")
)
```

### Events

You can define Amazon EventBridge event rules which trigger when a compliance check fails
or when a rule is re-evaluated.

Use the `onComplianceChange()` APIs to trigger an EventBridge event when a compliance check
of your AWS Config Rule fails:

```python
# Topic to which compliance notification events will be published
compliance_topic = sns.Topic(self, "ComplianceTopic")

rule = config.CloudFormationStackDriftDetectionCheck(self, "Drift")
rule.on_compliance_change("TopicEvent",
    target=targets.SnsTopic(compliance_topic)
)
```

Use the `onReEvaluationStatus()` status to trigger an EventBridge event when an AWS Config
rule is re-evaluated.

```python
# Topic to which re-evaluation notification events will be published
re_evaluation_topic = sns.Topic(self, "ComplianceTopic")

rule = config.CloudFormationStackDriftDetectionCheck(self, "Drift")
rule.on_re_evaluation_status("ReEvaluationEvent",
    target=targets.SnsTopic(re_evaluation_topic)
)
```

### Example

The following example creates a custom rule that evaluates whether EC2 instances are compliant.
Compliance events are published to an SNS topic.

```python
# Lambda function containing logic that evaluates compliance with the rule.
eval_compliance_fn = lambda_.Function(self, "CustomFunction",
    code=lambda_.AssetCode.from_inline("exports.handler = (event) => console.log(event);"),
    handler="index.handler",
    runtime=lambda_.Runtime.NODEJS_18_X
)

# A custom rule that runs on configuration changes of EC2 instances
custom_rule = config.CustomRule(self, "Custom",
    configuration_changes=True,
    lambda_function=eval_compliance_fn,
    rule_scope=config.RuleScope.from_resource(config.ResourceType.EC2_INSTANCE)
)

# A rule to detect stack drifts
drift_rule = config.CloudFormationStackDriftDetectionCheck(self, "Drift")

# Topic to which compliance notification events will be published
compliance_topic = sns.Topic(self, "ComplianceTopic")

# Send notification on compliance change events
drift_rule.on_compliance_change("ComplianceChange",
    target=targets.SnsTopic(compliance_topic)
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
    Resource as _Resource_45bc6135,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_events import (
    EventPattern as _EventPattern_fe557901,
    IRuleTarget as _IRuleTarget_7a91f454,
    OnEventOptions as _OnEventOptions_8711b8b3,
    Rule as _Rule_334ed2b5,
)
from ..aws_iam import IRole as _IRole_235f5d8e
from ..aws_lambda import IFunction as _IFunction_6adb0ab8
from ..aws_sns import ITopic as _ITopic_9eca4852


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnAggregationAuthorization(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_config.CfnAggregationAuthorization",
):
    '''An object that represents the authorizations granted to aggregator accounts and regions.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html
    :cloudformationResource: AWS::Config::AggregationAuthorization
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_config as config
        
        cfn_aggregation_authorization = config.CfnAggregationAuthorization(self, "MyCfnAggregationAuthorization",
            authorized_account_id="authorizedAccountId",
            authorized_aws_region="authorizedAwsRegion",
        
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
        authorized_account_id: builtins.str,
        authorized_aws_region: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param authorized_account_id: The 12-digit account ID of the account authorized to aggregate data.
        :param authorized_aws_region: The region authorized to collect aggregated data.
        :param tags: An array of tag object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d45b6827b30a710c41539b6e64a482fe288457f84fc8da58a369837e081918d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAggregationAuthorizationProps(
            authorized_account_id=authorized_account_id,
            authorized_aws_region=authorized_aws_region,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d44e9df1899840ed48cc8968c2953fc999bd4ebae4355121a7d0d44eb5a78d5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f4fe46b64cd7b2c7a7801c9f82cf436cd14b88bc96df13f85f4ae4b6503bda96)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAggregationAuthorizationArn")
    def attr_aggregation_authorization_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the aggregation object.

        :cloudformationAttribute: AggregationAuthorizationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAggregationAuthorizationArn"))

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
    @jsii.member(jsii_name="authorizedAccountId")
    def authorized_account_id(self) -> builtins.str:
        '''The 12-digit account ID of the account authorized to aggregate data.'''
        return typing.cast(builtins.str, jsii.get(self, "authorizedAccountId"))

    @authorized_account_id.setter
    def authorized_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd3558b66422be906f2e97b3cadb6ab3aff487b0ae706aa3e5e5cb5e361a5db2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizedAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="authorizedAwsRegion")
    def authorized_aws_region(self) -> builtins.str:
        '''The region authorized to collect aggregated data.'''
        return typing.cast(builtins.str, jsii.get(self, "authorizedAwsRegion"))

    @authorized_aws_region.setter
    def authorized_aws_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ec985b949ac5925a51ebe338acec25ecef0e6592afa79374fef259e6fef4198)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizedAwsRegion", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of tag object.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2acb4bb46d29ee80a30777200253cd46f769127ae01597fbc2e951064ea932d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_config.CfnAggregationAuthorizationProps",
    jsii_struct_bases=[],
    name_mapping={
        "authorized_account_id": "authorizedAccountId",
        "authorized_aws_region": "authorizedAwsRegion",
        "tags": "tags",
    },
)
class CfnAggregationAuthorizationProps:
    def __init__(
        self,
        *,
        authorized_account_id: builtins.str,
        authorized_aws_region: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAggregationAuthorization``.

        :param authorized_account_id: The 12-digit account ID of the account authorized to aggregate data.
        :param authorized_aws_region: The region authorized to collect aggregated data.
        :param tags: An array of tag object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_config as config
            
            cfn_aggregation_authorization_props = config.CfnAggregationAuthorizationProps(
                authorized_account_id="authorizedAccountId",
                authorized_aws_region="authorizedAwsRegion",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e6bdcf05466c02c7af89caa08522d10ba8181fd13410bcd081dbf714fbb74c9)
            check_type(argname="argument authorized_account_id", value=authorized_account_id, expected_type=type_hints["authorized_account_id"])
            check_type(argname="argument authorized_aws_region", value=authorized_aws_region, expected_type=type_hints["authorized_aws_region"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authorized_account_id": authorized_account_id,
            "authorized_aws_region": authorized_aws_region,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def authorized_account_id(self) -> builtins.str:
        '''The 12-digit account ID of the account authorized to aggregate data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html#cfn-config-aggregationauthorization-authorizedaccountid
        '''
        result = self._values.get("authorized_account_id")
        assert result is not None, "Required property 'authorized_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorized_aws_region(self) -> builtins.str:
        '''The region authorized to collect aggregated data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html#cfn-config-aggregationauthorization-authorizedawsregion
        '''
        result = self._values.get("authorized_aws_region")
        assert result is not None, "Required property 'authorized_aws_region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of tag object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html#cfn-config-aggregationauthorization-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAggregationAuthorizationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnConfigRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_config.CfnConfigRule",
):
    '''.. epigraph::

   You must first create and start the AWS Config configuration recorder in order to create AWS Config managed rules with AWS CloudFormation .

    For more information, see `Managing the Configuration Recorder <https://docs.aws.amazon.com/config/latest/developerguide/stop-start-recorder.html>`_ .

    Adds or updates an AWS Config rule to evaluate if your AWS resources comply with your desired configurations. For information on how many AWS Config rules you can have per account, see `*Service Limits* <https://docs.aws.amazon.com/config/latest/developerguide/configlimits.html>`_ in the *AWS Config Developer Guide* .

    There are two types of rules: *AWS Config Managed Rules* and *AWS Config Custom Rules* . You can use the ``ConfigRule`` resource to create both AWS Config Managed Rules and AWS Config Custom Rules.

    AWS Config Managed Rules are predefined, customizable rules created by AWS Config . For a list of managed rules, see `List of AWS Config Managed Rules <https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html>`_ . If you are adding an AWS Config managed rule, you must specify the rule's identifier for the ``SourceIdentifier`` key.

    AWS Config Custom Rules are rules that you create from scratch. There are two ways to create AWS Config custom rules: with Lambda functions ( `AWS Lambda Developer Guide <https://docs.aws.amazon.com/config/latest/developerguide/gettingstarted-concepts.html#gettingstarted-concepts-function>`_ ) and with Guard ( `Guard GitHub Repository <https://docs.aws.amazon.com/https://github.com/aws-cloudformation/cloudformation-guard>`_ ), a policy-as-code language. AWS Config custom rules created with AWS Lambda are called *AWS Config Custom Lambda Rules* and AWS Config custom rules created with Guard are called *AWS Config Custom Policy Rules* .

    If you are adding a new AWS Config Custom Lambda rule, you first need to create an AWS Lambda function that the rule invokes to evaluate your resources. When you use the ``ConfigRule`` resource to add a Custom Lambda rule to AWS Config , you must specify the Amazon Resource Name (ARN) that AWS Lambda assigns to the function. You specify the ARN in the ``SourceIdentifier`` key. This key is part of the ``Source`` object, which is part of the ``ConfigRule`` object.

    For any new AWS Config rule that you add, specify the ``ConfigRuleName`` in the ``ConfigRule`` object. Do not specify the ``ConfigRuleArn`` or the ``ConfigRuleId`` . These values are generated by AWS Config for new rules.

    If you are updating a rule that you added previously, you can specify the rule by ``ConfigRuleName`` , ``ConfigRuleId`` , or ``ConfigRuleArn`` in the ``ConfigRule`` data type that you use in this request.

    For more information about developing and using AWS Config rules, see `Evaluating Resources with AWS Config Rules <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html>`_ in the *AWS Config Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html
    :cloudformationResource: AWS::Config::ConfigRule
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_config as config
        
        # input_parameters: Any
        
        cfn_config_rule = config.CfnConfigRule(self, "MyCfnConfigRule",
            source=config.CfnConfigRule.SourceProperty(
                owner="owner",
        
                # the properties below are optional
                custom_policy_details=config.CfnConfigRule.CustomPolicyDetailsProperty(
                    enable_debug_log_delivery=False,
                    policy_runtime="policyRuntime",
                    policy_text="policyText"
                ),
                source_details=[config.CfnConfigRule.SourceDetailProperty(
                    event_source="eventSource",
                    message_type="messageType",
        
                    # the properties below are optional
                    maximum_execution_frequency="maximumExecutionFrequency"
                )],
                source_identifier="sourceIdentifier"
            ),
        
            # the properties below are optional
            compliance=config.CfnConfigRule.ComplianceProperty(
                type="type"
            ),
            config_rule_name="configRuleName",
            description="description",
            evaluation_modes=[config.CfnConfigRule.EvaluationModeConfigurationProperty(
                mode="mode"
            )],
            input_parameters=input_parameters,
            maximum_execution_frequency="maximumExecutionFrequency",
            scope=config.CfnConfigRule.ScopeProperty(
                compliance_resource_id="complianceResourceId",
                compliance_resource_types=["complianceResourceTypes"],
                tag_key="tagKey",
                tag_value="tagValue"
            )
        )
    '''

    def __init__(
        self,
        scope_: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        source: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigRule.SourceProperty", typing.Dict[builtins.str, typing.Any]]],
        compliance: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigRule.ComplianceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        evaluation_modes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigRule.EvaluationModeConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        input_parameters: typing.Any = None,
        maximum_execution_frequency: typing.Optional[builtins.str] = None,
        scope: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigRule.ScopeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope_: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param source: Provides the rule owner ( ``AWS`` for managed rules, ``CUSTOM_POLICY`` for Custom Policy rules, and ``CUSTOM_LAMBDA`` for Custom Lambda rules), the rule identifier, and the notifications that cause the function to evaluate your AWS resources.
        :param compliance: Indicates whether an AWS resource or AWS Config rule is compliant and provides the number of contributors that affect the compliance.
        :param config_rule_name: A name for the AWS Config rule. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the rule name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ .
        :param description: The description that you provide for the AWS Config rule.
        :param evaluation_modes: The modes the AWS Config rule can be evaluated in. The valid values are distinct objects. By default, the value is Detective evaluation mode only.
        :param input_parameters: A string, in JSON format, that is passed to the AWS Config rule Lambda function.
        :param maximum_execution_frequency: The maximum frequency with which AWS Config runs evaluations for a rule. You can specify a value for ``MaximumExecutionFrequency`` when: - You are using an AWS managed rule that is triggered at a periodic frequency. - Your custom rule is triggered when AWS Config delivers the configuration snapshot. For more information, see `ConfigSnapshotDeliveryProperties <https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigSnapshotDeliveryProperties.html>`_ . .. epigraph:: By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.
        :param scope: Defines which resources can trigger an evaluation for the rule. The scope can include one or more resource types, a combination of one resource type and one resource ID, or a combination of a tag key and value. Specify a scope to constrain the resources that can trigger an evaluation for the rule. If you do not specify a scope, evaluations are triggered when any resource in the recording group changes. .. epigraph:: The scope can be empty.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__deecc74e0a0f7e54fde16a159ece5d8f96f56f6b8aca025003adcc1d931d5d00)
            check_type(argname="argument scope_", value=scope_, expected_type=type_hints["scope_"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigRuleProps(
            source=source,
            compliance=compliance,
            config_rule_name=config_rule_name,
            description=description,
            evaluation_modes=evaluation_modes,
            input_parameters=input_parameters,
            maximum_execution_frequency=maximum_execution_frequency,
            scope=scope,
        )

        jsii.create(self.__class__, self, [scope_, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75ac7fdaab59736823d3ea7aee906c770b124ed77c2a19e236c7baea8446f076)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e2026b4300b4bc12decf81d1ef0dc9858c81f4dff9157afd07ab04e953241b21)
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
        '''The Amazon Resource Name (ARN) of the AWS Config rule, such as ``arn:aws:config:us-east-1:123456789012:config-rule/config-rule-a1bzhi`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrComplianceType")
    def attr_compliance_type(self) -> builtins.str:
        '''Compliance type determined by the Config rule.

        :cloudformationAttribute: Compliance.Type
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrComplianceType"))

    @builtins.property
    @jsii.member(jsii_name="attrConfigRuleId")
    def attr_config_rule_id(self) -> builtins.str:
        '''The ID of the AWS Config rule, such as ``config-rule-a1bzhi`` .

        :cloudformationAttribute: ConfigRuleId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConfigRuleId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnConfigRule.SourceProperty"]:
        '''Provides the rule owner ( ``AWS`` for managed rules, ``CUSTOM_POLICY`` for Custom Policy rules, and ``CUSTOM_LAMBDA`` for Custom Lambda rules), the rule identifier, and the notifications that cause the function to evaluate your AWS resources.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConfigRule.SourceProperty"], jsii.get(self, "source"))

    @source.setter
    def source(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnConfigRule.SourceProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a30b5901e0068cf18be7f15f8558e224eb62559802cd26646f648c0dbf5f3680)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="compliance")
    def compliance(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigRule.ComplianceProperty"]]:
        '''Indicates whether an AWS resource or AWS Config rule is compliant and provides the number of contributors that affect the compliance.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigRule.ComplianceProperty"]], jsii.get(self, "compliance"))

    @compliance.setter
    def compliance(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigRule.ComplianceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__743f9ee6243708ed2e606e31e618af32604f35d387093cdc8d8634e961b27324)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compliance", value)

    @builtins.property
    @jsii.member(jsii_name="configRuleName")
    def config_rule_name(self) -> typing.Optional[builtins.str]:
        '''A name for the AWS Config rule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configRuleName"))

    @config_rule_name.setter
    def config_rule_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e021e024fd440e8ec5c9b4d24e2029d1629640189c221a5866e301e89aa53b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configRuleName", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description that you provide for the AWS Config rule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__446b3dad0fdf8c8a9449d165e2fed6fa45c11495397d8cfdaf24ac1368e14962)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="evaluationModes")
    def evaluation_modes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigRule.EvaluationModeConfigurationProperty"]]]]:
        '''The modes the AWS Config rule can be evaluated in.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigRule.EvaluationModeConfigurationProperty"]]]], jsii.get(self, "evaluationModes"))

    @evaluation_modes.setter
    def evaluation_modes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigRule.EvaluationModeConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3563e34d09c0fb5a803e72a8cee06c0ed65b4c596390bf75303600bfd5df9f44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationModes", value)

    @builtins.property
    @jsii.member(jsii_name="inputParameters")
    def input_parameters(self) -> typing.Any:
        '''A string, in JSON format, that is passed to the AWS Config rule Lambda function.'''
        return typing.cast(typing.Any, jsii.get(self, "inputParameters"))

    @input_parameters.setter
    def input_parameters(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d61437c3cdab85e8dc7a25b710d93b6aaaa2a833466cfb80eb3d13340c62da3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inputParameters", value)

    @builtins.property
    @jsii.member(jsii_name="maximumExecutionFrequency")
    def maximum_execution_frequency(self) -> typing.Optional[builtins.str]:
        '''The maximum frequency with which AWS Config runs evaluations for a rule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maximumExecutionFrequency"))

    @maximum_execution_frequency.setter
    def maximum_execution_frequency(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c19facad0744d2d150810a1e9fb83a8d41c5447083981222c737ba287c7d08f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumExecutionFrequency", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigRule.ScopeProperty"]]:
        '''Defines which resources can trigger an evaluation for the rule.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigRule.ScopeProperty"]], jsii.get(self, "scope"))

    @scope.setter
    def scope(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigRule.ScopeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c70fa274e56c5def397aac6cec3b30f31c7ee9cc7367d5b6bf0c78e63400ca24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_config.CfnConfigRule.ComplianceProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type"},
    )
    class ComplianceProperty:
        def __init__(self, *, type: typing.Optional[builtins.str] = None) -> None:
            '''Indicates whether an AWS resource or AWS Config rule is compliant and provides the number of contributors that affect the compliance.

            :param type: Indicates whether an AWS resource or AWS Config rule is compliant. A resource is compliant if it complies with all of the AWS Config rules that evaluate it. A resource is noncompliant if it does not comply with one or more of these rules. A rule is compliant if all of the resources that the rule evaluates comply with it. A rule is noncompliant if any of these resources do not comply. AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are available for the AWS resource or AWS Config rule. For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-compliance.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_config as config
                
                compliance_property = config.CfnConfigRule.ComplianceProperty(
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4d66dbd2cc5d052bcc47c92d8ce8dd64bcb0b5dd57cfcc434e393029984359db)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''Indicates whether an AWS resource or AWS Config rule is compliant.

            A resource is compliant if it complies with all of the AWS Config rules that evaluate it. A resource is noncompliant if it does not comply with one or more of these rules.

            A rule is compliant if all of the resources that the rule evaluates comply with it. A rule is noncompliant if any of these resources do not comply.

            AWS Config returns the ``INSUFFICIENT_DATA`` value when no evaluation results are available for the AWS resource or AWS Config rule.

            For the ``Compliance`` data type, AWS Config supports only ``COMPLIANT`` , ``NON_COMPLIANT`` , and ``INSUFFICIENT_DATA`` values. AWS Config does not support the ``NOT_APPLICABLE`` value for the ``Compliance`` data type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-compliance.html#cfn-config-configrule-compliance-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComplianceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_config.CfnConfigRule.CustomPolicyDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_debug_log_delivery": "enableDebugLogDelivery",
            "policy_runtime": "policyRuntime",
            "policy_text": "policyText",
        },
    )
    class CustomPolicyDetailsProperty:
        def __init__(
            self,
            *,
            enable_debug_log_delivery: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            policy_runtime: typing.Optional[builtins.str] = None,
            policy_text: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides the CustomPolicyDetails, the rule owner ( ``AWS`` for managed rules, ``CUSTOM_POLICY`` for Custom Policy rules, and ``CUSTOM_LAMBDA`` for Custom Lambda rules), the rule identifier, and the events that cause the evaluation of your AWS resources.

            :param enable_debug_log_delivery: The boolean expression for enabling debug logging for your AWS Config Custom Policy rule. The default value is ``false`` .
            :param policy_runtime: The runtime system for your AWS Config Custom Policy rule. Guard is a policy-as-code language that allows you to write policies that are enforced by AWS Config Custom Policy rules. For more information about Guard, see the `Guard GitHub Repository <https://docs.aws.amazon.com/https://github.com/aws-cloudformation/cloudformation-guard>`_ .
            :param policy_text: The policy definition containing the logic for your AWS Config Custom Policy rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-custompolicydetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_config as config
                
                custom_policy_details_property = config.CfnConfigRule.CustomPolicyDetailsProperty(
                    enable_debug_log_delivery=False,
                    policy_runtime="policyRuntime",
                    policy_text="policyText"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f7656d43bed3c419437bf5b25bc9711a8cf65f9f6b46c7d52710b15c35aa5af9)
                check_type(argname="argument enable_debug_log_delivery", value=enable_debug_log_delivery, expected_type=type_hints["enable_debug_log_delivery"])
                check_type(argname="argument policy_runtime", value=policy_runtime, expected_type=type_hints["policy_runtime"])
                check_type(argname="argument policy_text", value=policy_text, expected_type=type_hints["policy_text"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enable_debug_log_delivery is not None:
                self._values["enable_debug_log_delivery"] = enable_debug_log_delivery
            if policy_runtime is not None:
                self._values["policy_runtime"] = policy_runtime
            if policy_text is not None:
                self._values["policy_text"] = policy_text

        @builtins.property
        def enable_debug_log_delivery(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The boolean expression for enabling debug logging for your AWS Config Custom Policy rule.

            The default value is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-custompolicydetails.html#cfn-config-configrule-custompolicydetails-enabledebuglogdelivery
            '''
            result = self._values.get("enable_debug_log_delivery")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def policy_runtime(self) -> typing.Optional[builtins.str]:
            '''The runtime system for your AWS Config Custom Policy rule.

            Guard is a policy-as-code language that allows you to write policies that are enforced by AWS Config Custom Policy rules. For more information about Guard, see the `Guard GitHub Repository <https://docs.aws.amazon.com/https://github.com/aws-cloudformation/cloudformation-guard>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-custompolicydetails.html#cfn-config-configrule-custompolicydetails-policyruntime
            '''
            result = self._values.get("policy_runtime")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def policy_text(self) -> typing.Optional[builtins.str]:
            '''The policy definition containing the logic for your AWS Config Custom Policy rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-custompolicydetails.html#cfn-config-configrule-custompolicydetails-policytext
            '''
            result = self._values.get("policy_text")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomPolicyDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_config.CfnConfigRule.EvaluationModeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"mode": "mode"},
    )
    class EvaluationModeConfigurationProperty:
        def __init__(self, *, mode: typing.Optional[builtins.str] = None) -> None:
            '''The configuration object for AWS Config rule evaluation mode.

            The supported valid values are Detective or Proactive.

            :param mode: The mode of an evaluation. The valid values are Detective or Proactive.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-evaluationmodeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_config as config
                
                evaluation_mode_configuration_property = config.CfnConfigRule.EvaluationModeConfigurationProperty(
                    mode="mode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8b0afa0e56a40fa7b9efd435c94956c335f03393a48dc1d31c186bf76c9f256e)
                check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if mode is not None:
                self._values["mode"] = mode

        @builtins.property
        def mode(self) -> typing.Optional[builtins.str]:
            '''The mode of an evaluation.

            The valid values are Detective or Proactive.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-evaluationmodeconfiguration.html#cfn-config-configrule-evaluationmodeconfiguration-mode
            '''
            result = self._values.get("mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EvaluationModeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_config.CfnConfigRule.ScopeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "compliance_resource_id": "complianceResourceId",
            "compliance_resource_types": "complianceResourceTypes",
            "tag_key": "tagKey",
            "tag_value": "tagValue",
        },
    )
    class ScopeProperty:
        def __init__(
            self,
            *,
            compliance_resource_id: typing.Optional[builtins.str] = None,
            compliance_resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
            tag_key: typing.Optional[builtins.str] = None,
            tag_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines which resources trigger an evaluation for an AWS Config rule.

            The scope can include one or more resource types, a combination of a tag key and value, or a combination of one resource type and one resource ID. Specify a scope to constrain which resources trigger an evaluation for a rule. Otherwise, evaluations for the rule are triggered when any resource in your recording group changes in configuration.

            :param compliance_resource_id: The ID of the only AWS resource that you want to trigger an evaluation for the rule. If you specify a resource ID, you must specify one resource type for ``ComplianceResourceTypes`` .
            :param compliance_resource_types: The resource types of only those AWS resources that you want to trigger an evaluation for the rule. You can only specify one type if you also specify a resource ID for ``ComplianceResourceId`` .
            :param tag_key: The tag key that is applied to only those AWS resources that you want to trigger an evaluation for the rule.
            :param tag_value: The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule. If you specify a value for ``TagValue`` , you must also specify a value for ``TagKey`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_config as config
                
                scope_property = config.CfnConfigRule.ScopeProperty(
                    compliance_resource_id="complianceResourceId",
                    compliance_resource_types=["complianceResourceTypes"],
                    tag_key="tagKey",
                    tag_value="tagValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b1dad2d9487ce142bd6c079d94efb61400194537a7d97b4158bc27439f9ae457)
                check_type(argname="argument compliance_resource_id", value=compliance_resource_id, expected_type=type_hints["compliance_resource_id"])
                check_type(argname="argument compliance_resource_types", value=compliance_resource_types, expected_type=type_hints["compliance_resource_types"])
                check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
                check_type(argname="argument tag_value", value=tag_value, expected_type=type_hints["tag_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if compliance_resource_id is not None:
                self._values["compliance_resource_id"] = compliance_resource_id
            if compliance_resource_types is not None:
                self._values["compliance_resource_types"] = compliance_resource_types
            if tag_key is not None:
                self._values["tag_key"] = tag_key
            if tag_value is not None:
                self._values["tag_value"] = tag_value

        @builtins.property
        def compliance_resource_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the only AWS resource that you want to trigger an evaluation for the rule.

            If you specify a resource ID, you must specify one resource type for ``ComplianceResourceTypes`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html#cfn-config-configrule-scope-complianceresourceid
            '''
            result = self._values.get("compliance_resource_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def compliance_resource_types(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''The resource types of only those AWS resources that you want to trigger an evaluation for the rule.

            You can only specify one type if you also specify a resource ID for ``ComplianceResourceId`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html#cfn-config-configrule-scope-complianceresourcetypes
            '''
            result = self._values.get("compliance_resource_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def tag_key(self) -> typing.Optional[builtins.str]:
            '''The tag key that is applied to only those AWS resources that you want to trigger an evaluation for the rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html#cfn-config-configrule-scope-tagkey
            '''
            result = self._values.get("tag_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tag_value(self) -> typing.Optional[builtins.str]:
            '''The tag value applied to only those AWS resources that you want to trigger an evaluation for the rule.

            If you specify a value for ``TagValue`` , you must also specify a value for ``TagKey`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-scope.html#cfn-config-configrule-scope-tagvalue
            '''
            result = self._values.get("tag_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScopeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_config.CfnConfigRule.SourceDetailProperty",
        jsii_struct_bases=[],
        name_mapping={
            "event_source": "eventSource",
            "message_type": "messageType",
            "maximum_execution_frequency": "maximumExecutionFrequency",
        },
    )
    class SourceDetailProperty:
        def __init__(
            self,
            *,
            event_source: builtins.str,
            message_type: builtins.str,
            maximum_execution_frequency: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides the source and the message types that trigger AWS Config to evaluate your AWS resources against a rule.

            It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic. You can specify the parameter values for ``SourceDetail`` only for custom rules.

            :param event_source: The source of the event, such as an AWS service, that triggers AWS Config to evaluate your AWS resources.
            :param message_type: The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types: - ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers a configuration item as a result of a resource change. - ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS. - ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency specified for ``MaximumExecutionFrequency`` . - ``ConfigurationSnapshotDeliveryCompleted`` - Triggers a periodic evaluation when AWS Config delivers a configuration snapshot. If you want your custom rule to be triggered by configuration changes, specify two SourceDetail objects, one for ``ConfigurationItemChangeNotification`` and one for ``OversizedConfigurationItemChangeNotification`` .
            :param maximum_execution_frequency: The frequency at which you want AWS Config to run evaluations for a custom rule with a periodic trigger. If you specify a value for ``MaximumExecutionFrequency`` , then ``MessageType`` must use the ``ScheduledNotification`` value. .. epigraph:: By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter. Based on the valid value you choose, AWS Config runs evaluations once for each valid value. For example, if you choose ``Three_Hours`` , AWS Config runs evaluations once every three hours. In this case, ``Three_Hours`` is the frequency of this rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-sourcedetail.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_config as config
                
                source_detail_property = config.CfnConfigRule.SourceDetailProperty(
                    event_source="eventSource",
                    message_type="messageType",
                
                    # the properties below are optional
                    maximum_execution_frequency="maximumExecutionFrequency"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f7d66badade1eb1594b8d1b078e9a871db86cf85d41ad81a5858329bf4ba3775)
                check_type(argname="argument event_source", value=event_source, expected_type=type_hints["event_source"])
                check_type(argname="argument message_type", value=message_type, expected_type=type_hints["message_type"])
                check_type(argname="argument maximum_execution_frequency", value=maximum_execution_frequency, expected_type=type_hints["maximum_execution_frequency"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "event_source": event_source,
                "message_type": message_type,
            }
            if maximum_execution_frequency is not None:
                self._values["maximum_execution_frequency"] = maximum_execution_frequency

        @builtins.property
        def event_source(self) -> builtins.str:
            '''The source of the event, such as an AWS service, that triggers AWS Config to evaluate your AWS resources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-sourcedetail.html#cfn-config-configrule-sourcedetail-eventsource
            '''
            result = self._values.get("event_source")
            assert result is not None, "Required property 'event_source' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def message_type(self) -> builtins.str:
            '''The type of notification that triggers AWS Config to run an evaluation for a rule.

            You can specify the following notification types:

            - ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers a configuration item as a result of a resource change.
            - ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS.
            - ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency specified for ``MaximumExecutionFrequency`` .
            - ``ConfigurationSnapshotDeliveryCompleted`` - Triggers a periodic evaluation when AWS Config delivers a configuration snapshot.

            If you want your custom rule to be triggered by configuration changes, specify two SourceDetail objects, one for ``ConfigurationItemChangeNotification`` and one for ``OversizedConfigurationItemChangeNotification`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-sourcedetail.html#cfn-config-configrule-sourcedetail-messagetype
            '''
            result = self._values.get("message_type")
            assert result is not None, "Required property 'message_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def maximum_execution_frequency(self) -> typing.Optional[builtins.str]:
            '''The frequency at which you want AWS Config to run evaluations for a custom rule with a periodic trigger.

            If you specify a value for ``MaximumExecutionFrequency`` , then ``MessageType`` must use the ``ScheduledNotification`` value.
            .. epigraph::

               By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

               Based on the valid value you choose, AWS Config runs evaluations once for each valid value. For example, if you choose ``Three_Hours`` , AWS Config runs evaluations once every three hours. In this case, ``Three_Hours`` is the frequency of this rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-sourcedetail.html#cfn-config-configrule-sourcedetail-maximumexecutionfrequency
            '''
            result = self._values.get("maximum_execution_frequency")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceDetailProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_config.CfnConfigRule.SourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "owner": "owner",
            "custom_policy_details": "customPolicyDetails",
            "source_details": "sourceDetails",
            "source_identifier": "sourceIdentifier",
        },
    )
    class SourceProperty:
        def __init__(
            self,
            *,
            owner: builtins.str,
            custom_policy_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigRule.CustomPolicyDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            source_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigRule.SourceDetailProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            source_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides the CustomPolicyDetails, the rule owner ( ``AWS`` for managed rules, ``CUSTOM_POLICY`` for Custom Policy rules, and ``CUSTOM_LAMBDA`` for Custom Lambda rules), the rule identifier, and the events that cause the evaluation of your AWS resources.

            :param owner: Indicates whether AWS or the customer owns and manages the AWS Config rule. AWS Config Managed Rules are predefined rules owned by AWS . For more information, see `AWS Config Managed Rules <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`_ in the *AWS Config developer guide* . AWS Config Custom Rules are rules that you can develop either with Guard ( ``CUSTOM_POLICY`` ) or AWS Lambda ( ``CUSTOM_LAMBDA`` ). For more information, see `AWS Config Custom Rules <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html>`_ in the *AWS Config developer guide* .
            :param custom_policy_details: Provides the runtime system, policy definition, and whether debug logging is enabled. Required when owner is set to ``CUSTOM_POLICY`` .
            :param source_details: Provides the source and the message types that cause AWS Config to evaluate your AWS resources against a rule. It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic. If the owner is set to ``CUSTOM_POLICY`` , the only acceptable values for the AWS Config rule trigger message type are ``ConfigurationItemChangeNotification`` and ``OversizedConfigurationItemChangeNotification`` .
            :param source_identifier: For AWS Config Managed rules, a predefined identifier from a list. For example, ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see `List of AWS Config Managed Rules <https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html>`_ . For AWS Config Custom Lambda rules, the identifier is the Amazon Resource Name (ARN) of the rule's AWS Lambda function, such as ``arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name`` . For AWS Config Custom Policy rules, this field will be ignored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_config as config
                
                source_property = config.CfnConfigRule.SourceProperty(
                    owner="owner",
                
                    # the properties below are optional
                    custom_policy_details=config.CfnConfigRule.CustomPolicyDetailsProperty(
                        enable_debug_log_delivery=False,
                        policy_runtime="policyRuntime",
                        policy_text="policyText"
                    ),
                    source_details=[config.CfnConfigRule.SourceDetailProperty(
                        event_source="eventSource",
                        message_type="messageType",
                
                        # the properties below are optional
                        maximum_execution_frequency="maximumExecutionFrequency"
                    )],
                    source_identifier="sourceIdentifier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c8f7d3fbc3eba470d52b27b24c17f4eb9fae6ee74da9bf511cdb8b4ce4483652)
                check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
                check_type(argname="argument custom_policy_details", value=custom_policy_details, expected_type=type_hints["custom_policy_details"])
                check_type(argname="argument source_details", value=source_details, expected_type=type_hints["source_details"])
                check_type(argname="argument source_identifier", value=source_identifier, expected_type=type_hints["source_identifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "owner": owner,
            }
            if custom_policy_details is not None:
                self._values["custom_policy_details"] = custom_policy_details
            if source_details is not None:
                self._values["source_details"] = source_details
            if source_identifier is not None:
                self._values["source_identifier"] = source_identifier

        @builtins.property
        def owner(self) -> builtins.str:
            '''Indicates whether AWS or the customer owns and manages the AWS Config rule.

            AWS Config Managed Rules are predefined rules owned by AWS . For more information, see `AWS Config Managed Rules <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`_ in the *AWS Config developer guide* .

            AWS Config Custom Rules are rules that you can develop either with Guard ( ``CUSTOM_POLICY`` ) or AWS Lambda ( ``CUSTOM_LAMBDA`` ). For more information, see `AWS Config Custom Rules <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html>`_ in the *AWS Config developer guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html#cfn-config-configrule-source-owner
            '''
            result = self._values.get("owner")
            assert result is not None, "Required property 'owner' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def custom_policy_details(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigRule.CustomPolicyDetailsProperty"]]:
            '''Provides the runtime system, policy definition, and whether debug logging is enabled.

            Required when owner is set to ``CUSTOM_POLICY`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html#cfn-config-configrule-source-custompolicydetails
            '''
            result = self._values.get("custom_policy_details")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigRule.CustomPolicyDetailsProperty"]], result)

        @builtins.property
        def source_details(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigRule.SourceDetailProperty"]]]]:
            '''Provides the source and the message types that cause AWS Config to evaluate your AWS resources against a rule.

            It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic.

            If the owner is set to ``CUSTOM_POLICY`` , the only acceptable values for the AWS Config rule trigger message type are ``ConfigurationItemChangeNotification`` and ``OversizedConfigurationItemChangeNotification`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html#cfn-config-configrule-source-sourcedetails
            '''
            result = self._values.get("source_details")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigRule.SourceDetailProperty"]]]], result)

        @builtins.property
        def source_identifier(self) -> typing.Optional[builtins.str]:
            '''For AWS Config Managed rules, a predefined identifier from a list.

            For example, ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see `List of AWS Config Managed Rules <https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html>`_ .

            For AWS Config Custom Lambda rules, the identifier is the Amazon Resource Name (ARN) of the rule's AWS Lambda function, such as ``arn:aws:lambda:us-east-2:123456789012:function:custom_rule_name`` .

            For AWS Config Custom Policy rules, this field will be ignored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configrule-source.html#cfn-config-configrule-source-sourceidentifier
            '''
            result = self._values.get("source_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_config.CfnConfigRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "source": "source",
        "compliance": "compliance",
        "config_rule_name": "configRuleName",
        "description": "description",
        "evaluation_modes": "evaluationModes",
        "input_parameters": "inputParameters",
        "maximum_execution_frequency": "maximumExecutionFrequency",
        "scope": "scope",
    },
)
class CfnConfigRuleProps:
    def __init__(
        self,
        *,
        source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigRule.SourceProperty, typing.Dict[builtins.str, typing.Any]]],
        compliance: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigRule.ComplianceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        evaluation_modes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigRule.EvaluationModeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        input_parameters: typing.Any = None,
        maximum_execution_frequency: typing.Optional[builtins.str] = None,
        scope: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigRule.ScopeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfigRule``.

        :param source: Provides the rule owner ( ``AWS`` for managed rules, ``CUSTOM_POLICY`` for Custom Policy rules, and ``CUSTOM_LAMBDA`` for Custom Lambda rules), the rule identifier, and the notifications that cause the function to evaluate your AWS resources.
        :param compliance: Indicates whether an AWS resource or AWS Config rule is compliant and provides the number of contributors that affect the compliance.
        :param config_rule_name: A name for the AWS Config rule. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the rule name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ .
        :param description: The description that you provide for the AWS Config rule.
        :param evaluation_modes: The modes the AWS Config rule can be evaluated in. The valid values are distinct objects. By default, the value is Detective evaluation mode only.
        :param input_parameters: A string, in JSON format, that is passed to the AWS Config rule Lambda function.
        :param maximum_execution_frequency: The maximum frequency with which AWS Config runs evaluations for a rule. You can specify a value for ``MaximumExecutionFrequency`` when: - You are using an AWS managed rule that is triggered at a periodic frequency. - Your custom rule is triggered when AWS Config delivers the configuration snapshot. For more information, see `ConfigSnapshotDeliveryProperties <https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigSnapshotDeliveryProperties.html>`_ . .. epigraph:: By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.
        :param scope: Defines which resources can trigger an evaluation for the rule. The scope can include one or more resource types, a combination of one resource type and one resource ID, or a combination of a tag key and value. Specify a scope to constrain the resources that can trigger an evaluation for the rule. If you do not specify a scope, evaluations are triggered when any resource in the recording group changes. .. epigraph:: The scope can be empty.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_config as config
            
            # input_parameters: Any
            
            cfn_config_rule_props = config.CfnConfigRuleProps(
                source=config.CfnConfigRule.SourceProperty(
                    owner="owner",
            
                    # the properties below are optional
                    custom_policy_details=config.CfnConfigRule.CustomPolicyDetailsProperty(
                        enable_debug_log_delivery=False,
                        policy_runtime="policyRuntime",
                        policy_text="policyText"
                    ),
                    source_details=[config.CfnConfigRule.SourceDetailProperty(
                        event_source="eventSource",
                        message_type="messageType",
            
                        # the properties below are optional
                        maximum_execution_frequency="maximumExecutionFrequency"
                    )],
                    source_identifier="sourceIdentifier"
                ),
            
                # the properties below are optional
                compliance=config.CfnConfigRule.ComplianceProperty(
                    type="type"
                ),
                config_rule_name="configRuleName",
                description="description",
                evaluation_modes=[config.CfnConfigRule.EvaluationModeConfigurationProperty(
                    mode="mode"
                )],
                input_parameters=input_parameters,
                maximum_execution_frequency="maximumExecutionFrequency",
                scope=config.CfnConfigRule.ScopeProperty(
                    compliance_resource_id="complianceResourceId",
                    compliance_resource_types=["complianceResourceTypes"],
                    tag_key="tagKey",
                    tag_value="tagValue"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__116f429a66beeda0419005586893a32aeefeb73824ac9dc6668b4e69b23facc2)
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument compliance", value=compliance, expected_type=type_hints["compliance"])
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument evaluation_modes", value=evaluation_modes, expected_type=type_hints["evaluation_modes"])
            check_type(argname="argument input_parameters", value=input_parameters, expected_type=type_hints["input_parameters"])
            check_type(argname="argument maximum_execution_frequency", value=maximum_execution_frequency, expected_type=type_hints["maximum_execution_frequency"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "source": source,
        }
        if compliance is not None:
            self._values["compliance"] = compliance
        if config_rule_name is not None:
            self._values["config_rule_name"] = config_rule_name
        if description is not None:
            self._values["description"] = description
        if evaluation_modes is not None:
            self._values["evaluation_modes"] = evaluation_modes
        if input_parameters is not None:
            self._values["input_parameters"] = input_parameters
        if maximum_execution_frequency is not None:
            self._values["maximum_execution_frequency"] = maximum_execution_frequency
        if scope is not None:
            self._values["scope"] = scope

    @builtins.property
    def source(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnConfigRule.SourceProperty]:
        '''Provides the rule owner ( ``AWS`` for managed rules, ``CUSTOM_POLICY`` for Custom Policy rules, and ``CUSTOM_LAMBDA`` for Custom Lambda rules), the rule identifier, and the notifications that cause the function to evaluate your AWS resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-source
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnConfigRule.SourceProperty], result)

    @builtins.property
    def compliance(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigRule.ComplianceProperty]]:
        '''Indicates whether an AWS resource or AWS Config rule is compliant and provides the number of contributors that affect the compliance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-compliance
        '''
        result = self._values.get("compliance")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigRule.ComplianceProperty]], result)

    @builtins.property
    def config_rule_name(self) -> typing.Optional[builtins.str]:
        '''A name for the AWS Config rule.

        If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the rule name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-configrulename
        '''
        result = self._values.get("config_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description that you provide for the AWS Config rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def evaluation_modes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfigRule.EvaluationModeConfigurationProperty]]]]:
        '''The modes the AWS Config rule can be evaluated in.

        The valid values are distinct objects. By default, the value is Detective evaluation mode only.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-evaluationmodes
        '''
        result = self._values.get("evaluation_modes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfigRule.EvaluationModeConfigurationProperty]]]], result)

    @builtins.property
    def input_parameters(self) -> typing.Any:
        '''A string, in JSON format, that is passed to the AWS Config rule Lambda function.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-inputparameters
        '''
        result = self._values.get("input_parameters")
        return typing.cast(typing.Any, result)

    @builtins.property
    def maximum_execution_frequency(self) -> typing.Optional[builtins.str]:
        '''The maximum frequency with which AWS Config runs evaluations for a rule.

        You can specify a value for ``MaximumExecutionFrequency`` when:

        - You are using an AWS managed rule that is triggered at a periodic frequency.
        - Your custom rule is triggered when AWS Config delivers the configuration snapshot. For more information, see `ConfigSnapshotDeliveryProperties <https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigSnapshotDeliveryProperties.html>`_ .

        .. epigraph::

           By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-maximumexecutionfrequency
        '''
        result = self._values.get("maximum_execution_frequency")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scope(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigRule.ScopeProperty]]:
        '''Defines which resources can trigger an evaluation for the rule.

        The scope can include one or more resource types, a combination of one resource type and one resource ID, or a combination of a tag key and value. Specify a scope to constrain the resources that can trigger an evaluation for the rule. If you do not specify a scope, evaluations are triggered when any resource in the recording group changes.
        .. epigraph::

           The scope can be empty.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html#cfn-config-configrule-scope
        '''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigRule.ScopeProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnConfigurationAggregator(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_config.CfnConfigurationAggregator",
):
    '''The details about the configuration aggregator, including information about source accounts, regions, and metadata of the aggregator.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html
    :cloudformationResource: AWS::Config::ConfigurationAggregator
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_config as config
        
        cfn_configuration_aggregator = config.CfnConfigurationAggregator(self, "MyCfnConfigurationAggregator",
            account_aggregation_sources=[config.CfnConfigurationAggregator.AccountAggregationSourceProperty(
                account_ids=["accountIds"],
        
                # the properties below are optional
                all_aws_regions=False,
                aws_regions=["awsRegions"]
            )],
            configuration_aggregator_name="configurationAggregatorName",
            organization_aggregation_source=config.CfnConfigurationAggregator.OrganizationAggregationSourceProperty(
                role_arn="roleArn",
        
                # the properties below are optional
                all_aws_regions=False,
                aws_regions=["awsRegions"]
            ),
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
        account_aggregation_sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationAggregator.AccountAggregationSourceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        configuration_aggregator_name: typing.Optional[builtins.str] = None,
        organization_aggregation_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationAggregator.OrganizationAggregationSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param account_aggregation_sources: Provides a list of source accounts and regions to be aggregated.
        :param configuration_aggregator_name: The name of the aggregator.
        :param organization_aggregation_source: Provides an organization and list of regions to be aggregated.
        :param tags: An array of tag object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40705fa4ca5c4067a90bb01d176f11c05ad5552df80610a53368350023ed36f2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigurationAggregatorProps(
            account_aggregation_sources=account_aggregation_sources,
            configuration_aggregator_name=configuration_aggregator_name,
            organization_aggregation_source=organization_aggregation_source,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a67b0d51dcca76878a73006884af15e33330c306c3d8647f96d10c0ba3f57ef9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ce2cf39aa72c31cf38b4c26fc5f5192604fe0a27dca13c342e158bdd5e5787cd)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrConfigurationAggregatorArn")
    def attr_configuration_aggregator_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the aggregator.

        :cloudformationAttribute: ConfigurationAggregatorArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConfigurationAggregatorArn"))

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
    @jsii.member(jsii_name="accountAggregationSources")
    def account_aggregation_sources(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigurationAggregator.AccountAggregationSourceProperty"]]]]:
        '''Provides a list of source accounts and regions to be aggregated.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigurationAggregator.AccountAggregationSourceProperty"]]]], jsii.get(self, "accountAggregationSources"))

    @account_aggregation_sources.setter
    def account_aggregation_sources(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigurationAggregator.AccountAggregationSourceProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca6667d76e5d18c00525f2f2e305db803462801d9dd67cb2cc46951b67b7e1c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountAggregationSources", value)

    @builtins.property
    @jsii.member(jsii_name="configurationAggregatorName")
    def configuration_aggregator_name(self) -> typing.Optional[builtins.str]:
        '''The name of the aggregator.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configurationAggregatorName"))

    @configuration_aggregator_name.setter
    def configuration_aggregator_name(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5d468f6c23924787d592b321e6a582b8ee2144e5dc7e23a15626d783a2637da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationAggregatorName", value)

    @builtins.property
    @jsii.member(jsii_name="organizationAggregationSource")
    def organization_aggregation_source(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationAggregator.OrganizationAggregationSourceProperty"]]:
        '''Provides an organization and list of regions to be aggregated.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationAggregator.OrganizationAggregationSourceProperty"]], jsii.get(self, "organizationAggregationSource"))

    @organization_aggregation_source.setter
    def organization_aggregation_source(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationAggregator.OrganizationAggregationSourceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adc51ade0f3204fdf6726c1ef680ca92c25055c195dce6a07df154db27d4c155)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationAggregationSource", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of tag object.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3d290ef49845b3910d8dfd1137db37b79d04caa1266e44513db09527493d2da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_config.CfnConfigurationAggregator.AccountAggregationSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_ids": "accountIds",
            "all_aws_regions": "allAwsRegions",
            "aws_regions": "awsRegions",
        },
    )
    class AccountAggregationSourceProperty:
        def __init__(
            self,
            *,
            account_ids: typing.Sequence[builtins.str],
            all_aws_regions: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A collection of accounts and regions.

            :param account_ids: The 12-digit account ID of the account being aggregated.
            :param all_aws_regions: If true, aggregate existing AWS Config regions and future regions.
            :param aws_regions: The source regions being aggregated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-accountaggregationsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_config as config
                
                account_aggregation_source_property = config.CfnConfigurationAggregator.AccountAggregationSourceProperty(
                    account_ids=["accountIds"],
                
                    # the properties below are optional
                    all_aws_regions=False,
                    aws_regions=["awsRegions"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a6a7c257ab123c8bd6831aa9a0a52136ad391b912ac2682938757e16c6bdec2a)
                check_type(argname="argument account_ids", value=account_ids, expected_type=type_hints["account_ids"])
                check_type(argname="argument all_aws_regions", value=all_aws_regions, expected_type=type_hints["all_aws_regions"])
                check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "account_ids": account_ids,
            }
            if all_aws_regions is not None:
                self._values["all_aws_regions"] = all_aws_regions
            if aws_regions is not None:
                self._values["aws_regions"] = aws_regions

        @builtins.property
        def account_ids(self) -> typing.List[builtins.str]:
            '''The 12-digit account ID of the account being aggregated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-accountaggregationsource.html#cfn-config-configurationaggregator-accountaggregationsource-accountids
            '''
            result = self._values.get("account_ids")
            assert result is not None, "Required property 'account_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def all_aws_regions(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If true, aggregate existing AWS Config regions and future regions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-accountaggregationsource.html#cfn-config-configurationaggregator-accountaggregationsource-allawsregions
            '''
            result = self._values.get("all_aws_regions")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The source regions being aggregated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-accountaggregationsource.html#cfn-config-configurationaggregator-accountaggregationsource-awsregions
            '''
            result = self._values.get("aws_regions")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccountAggregationSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_config.CfnConfigurationAggregator.OrganizationAggregationSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "all_aws_regions": "allAwsRegions",
            "aws_regions": "awsRegions",
        },
    )
    class OrganizationAggregationSourceProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            all_aws_regions: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''This object contains regions to set up the aggregator and an IAM role to retrieve organization details.

            :param role_arn: ARN of the IAM role used to retrieve AWS Organizations details associated with the aggregator account.
            :param all_aws_regions: If true, aggregate existing AWS Config regions and future regions.
            :param aws_regions: The source regions being aggregated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-organizationaggregationsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_config as config
                
                organization_aggregation_source_property = config.CfnConfigurationAggregator.OrganizationAggregationSourceProperty(
                    role_arn="roleArn",
                
                    # the properties below are optional
                    all_aws_regions=False,
                    aws_regions=["awsRegions"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__96908b20c43c7212f0b7cad39b2803ff294c40bcf770282dd47c8969bcd8bf51)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument all_aws_regions", value=all_aws_regions, expected_type=type_hints["all_aws_regions"])
                check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
            }
            if all_aws_regions is not None:
                self._values["all_aws_regions"] = all_aws_regions
            if aws_regions is not None:
                self._values["aws_regions"] = aws_regions

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''ARN of the IAM role used to retrieve AWS Organizations details associated with the aggregator account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-organizationaggregationsource.html#cfn-config-configurationaggregator-organizationaggregationsource-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def all_aws_regions(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If true, aggregate existing AWS Config regions and future regions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-organizationaggregationsource.html#cfn-config-configurationaggregator-organizationaggregationsource-allawsregions
            '''
            result = self._values.get("all_aws_regions")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The source regions being aggregated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationaggregator-organizationaggregationsource.html#cfn-config-configurationaggregator-organizationaggregationsource-awsregions
            '''
            result = self._values.get("aws_regions")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OrganizationAggregationSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_config.CfnConfigurationAggregatorProps",
    jsii_struct_bases=[],
    name_mapping={
        "account_aggregation_sources": "accountAggregationSources",
        "configuration_aggregator_name": "configurationAggregatorName",
        "organization_aggregation_source": "organizationAggregationSource",
        "tags": "tags",
    },
)
class CfnConfigurationAggregatorProps:
    def __init__(
        self,
        *,
        account_aggregation_sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationAggregator.AccountAggregationSourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        configuration_aggregator_name: typing.Optional[builtins.str] = None,
        organization_aggregation_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationAggregator.OrganizationAggregationSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfigurationAggregator``.

        :param account_aggregation_sources: Provides a list of source accounts and regions to be aggregated.
        :param configuration_aggregator_name: The name of the aggregator.
        :param organization_aggregation_source: Provides an organization and list of regions to be aggregated.
        :param tags: An array of tag object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_config as config
            
            cfn_configuration_aggregator_props = config.CfnConfigurationAggregatorProps(
                account_aggregation_sources=[config.CfnConfigurationAggregator.AccountAggregationSourceProperty(
                    account_ids=["accountIds"],
            
                    # the properties below are optional
                    all_aws_regions=False,
                    aws_regions=["awsRegions"]
                )],
                configuration_aggregator_name="configurationAggregatorName",
                organization_aggregation_source=config.CfnConfigurationAggregator.OrganizationAggregationSourceProperty(
                    role_arn="roleArn",
            
                    # the properties below are optional
                    all_aws_regions=False,
                    aws_regions=["awsRegions"]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23996e22d45c091c120b53006e9571da0dfd1a6a925c8a526fad11fbe913c027)
            check_type(argname="argument account_aggregation_sources", value=account_aggregation_sources, expected_type=type_hints["account_aggregation_sources"])
            check_type(argname="argument configuration_aggregator_name", value=configuration_aggregator_name, expected_type=type_hints["configuration_aggregator_name"])
            check_type(argname="argument organization_aggregation_source", value=organization_aggregation_source, expected_type=type_hints["organization_aggregation_source"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if account_aggregation_sources is not None:
            self._values["account_aggregation_sources"] = account_aggregation_sources
        if configuration_aggregator_name is not None:
            self._values["configuration_aggregator_name"] = configuration_aggregator_name
        if organization_aggregation_source is not None:
            self._values["organization_aggregation_source"] = organization_aggregation_source
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def account_aggregation_sources(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfigurationAggregator.AccountAggregationSourceProperty]]]]:
        '''Provides a list of source accounts and regions to be aggregated.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html#cfn-config-configurationaggregator-accountaggregationsources
        '''
        result = self._values.get("account_aggregation_sources")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfigurationAggregator.AccountAggregationSourceProperty]]]], result)

    @builtins.property
    def configuration_aggregator_name(self) -> typing.Optional[builtins.str]:
        '''The name of the aggregator.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html#cfn-config-configurationaggregator-configurationaggregatorname
        '''
        result = self._values.get("configuration_aggregator_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organization_aggregation_source(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationAggregator.OrganizationAggregationSourceProperty]]:
        '''Provides an organization and list of regions to be aggregated.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html#cfn-config-configurationaggregator-organizationaggregationsource
        '''
        result = self._values.get("organization_aggregation_source")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationAggregator.OrganizationAggregationSourceProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of tag object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html#cfn-config-configurationaggregator-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationAggregatorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnConfigurationRecorder(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_config.CfnConfigurationRecorder",
):
    '''The ``AWS::Config::ConfigurationRecorder`` resource type describes the AWS resource types that AWS Config records for configuration changes.

    The configuration recorder stores the configuration changes of the specified resources in your account as configuration items.
    .. epigraph::

       To enable AWS Config , you must create a configuration recorder and a delivery channel.

       AWS Config uses the delivery channel to deliver the configuration changes to your Amazon S3 bucket or Amazon SNS topic. For more information, see `AWS::Config::DeliveryChannel <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html>`_ .

    AWS CloudFormation starts the recorder as soon as the delivery channel is available.

    To stop the recorder and delete it, delete the configuration recorder from your stack. To stop the recorder without deleting it, call the `StopConfigurationRecorder <https://docs.aws.amazon.com/config/latest/APIReference/API_StopConfigurationRecorder.html>`_ action of the AWS Config API directly.

    For more information, see `Configuration Recorder <https://docs.aws.amazon.com/config/latest/developerguide/config-concepts.html#config-recorder>`_ in the AWS Config Developer Guide.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html
    :cloudformationResource: AWS::Config::ConfigurationRecorder
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_config as config
        
        cfn_configuration_recorder = config.CfnConfigurationRecorder(self, "MyCfnConfigurationRecorder",
            role_arn="roleArn",
        
            # the properties below are optional
            name="name",
            recording_group=config.CfnConfigurationRecorder.RecordingGroupProperty(
                all_supported=False,
                exclusion_by_resource_types=config.CfnConfigurationRecorder.ExclusionByResourceTypesProperty(
                    resource_types=["resourceTypes"]
                ),
                include_global_resource_types=False,
                recording_strategy=config.CfnConfigurationRecorder.RecordingStrategyProperty(
                    use_only="useOnly"
                ),
                resource_types=["resourceTypes"]
            ),
            recording_mode=config.CfnConfigurationRecorder.RecordingModeProperty(
                recording_frequency="recordingFrequency",
        
                # the properties below are optional
                recording_mode_overrides=[config.CfnConfigurationRecorder.RecordingModeOverrideProperty(
                    recording_frequency="recordingFrequency",
                    resource_types=["resourceTypes"],
        
                    # the properties below are optional
                    description="description"
                )]
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        role_arn: builtins.str,
        name: typing.Optional[builtins.str] = None,
        recording_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationRecorder.RecordingGroupProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        recording_mode: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationRecorder.RecordingModeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param role_arn: Amazon Resource Name (ARN) of the IAM role assumed by AWS Config and used by the configuration recorder. For more information, see `Permissions for the IAM Role Assigned <https://docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html>`_ to AWS Config in the AWS Config Developer Guide. .. epigraph:: *Pre-existing AWS Config role* If you have used an AWS service that uses AWS Config , such as AWS Security Hub or AWS Control Tower , and an AWS Config role has already been created, make sure that the IAM role that you use when setting up AWS Config keeps the same minimum permissions as the already created AWS Config role. You must do this so that the other AWS service continues to run as expected. For example, if AWS Control Tower has an IAM role that allows AWS Config to read Amazon Simple Storage Service ( Amazon S3 ) objects, make sure that the same permissions are granted within the IAM role you use when setting up AWS Config . Otherwise, it may interfere with how AWS Control Tower operates. For more information about IAM roles for AWS Config , see `*Identity and Access Management for AWS Config* <https://docs.aws.amazon.com/config/latest/developerguide/security-iam.html>`_ in the *AWS Config Developer Guide* .
        :param name: The name of the configuration recorder. AWS Config automatically assigns the name of "default" when creating the configuration recorder. You cannot change the name of the configuration recorder after it has been created. To change the configuration recorder name, you must delete it and create a new configuration recorder with a new name.
        :param recording_group: Specifies which resource types AWS Config records for configuration changes. .. epigraph:: *High Number of AWS Config Evaluations* You may notice increased activity in your account during your initial month recording with AWS Config when compared to subsequent months. During the initial bootstrapping process, AWS Config runs evaluations on all the resources in your account that you have selected for AWS Config to record. If you are running ephemeral workloads, you may see increased activity from AWS Config as it records configuration changes associated with creating and deleting these temporary resources. An *ephemeral workload* is a temporary use of computing resources that are loaded and run when needed. Examples include Amazon Elastic Compute Cloud ( Amazon EC2 ) Spot Instances, Amazon EMR jobs, and AWS Auto Scaling . If you want to avoid the increased activity from running ephemeral workloads, you can run these types of workloads in a separate account with AWS Config turned off to avoid increased configuration recording and rule evaluations.
        :param recording_mode: Specifies the default recording frequency that AWS Config uses to record configuration changes. AWS Config supports *Continuous recording* and *Daily recording* . - Continuous recording allows you to record configuration changes continuously whenever a change occurs. - Daily recording allows you to receive a configuration item (CI) representing the most recent state of your resources over the last 24-hour period, only if it’s different from the previous CI recorded. .. epigraph:: AWS Firewall Manager depends on continuous recording to monitor your resources. If you are using Firewall Manager, it is recommended that you set the recording frequency to Continuous. You can also override the recording frequency for specific resource types.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cc1fca38c04598953e44108edff915ed0a33e7e99e047d1bffcbd31ac2e3b03)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigurationRecorderProps(
            role_arn=role_arn,
            name=name,
            recording_group=recording_group,
            recording_mode=recording_mode,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f0ad5fea2a79c807a345af7618aeaf866bf5a74d50a1a738fab4def57031159)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9732775bf56ded9f1fec94c1669136a91512c9ba51aaaebf836d5d8ef071812a)
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
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''Amazon Resource Name (ARN) of the IAM role assumed by AWS Config and used by the configuration recorder.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcbc5734beaea5ab983c66a385694785e3c9ee7351911d6b565ea4e897a7826e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the configuration recorder.

        AWS Config automatically assigns the name of "default" when creating the configuration recorder.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2a1c68bd9cad77de81d8251d2998854170a63f9e469e6bdea9a9e56f75e6622)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="recordingGroup")
    def recording_group(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationRecorder.RecordingGroupProperty"]]:
        '''Specifies which resource types AWS Config records for configuration changes.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationRecorder.RecordingGroupProperty"]], jsii.get(self, "recordingGroup"))

    @recording_group.setter
    def recording_group(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationRecorder.RecordingGroupProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e1878a10e77a1aa31c809535803af7748be10257943ccb0147e9c0839dda938)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordingGroup", value)

    @builtins.property
    @jsii.member(jsii_name="recordingMode")
    def recording_mode(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationRecorder.RecordingModeProperty"]]:
        '''Specifies the default recording frequency that AWS Config uses to record configuration changes.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationRecorder.RecordingModeProperty"]], jsii.get(self, "recordingMode"))

    @recording_mode.setter
    def recording_mode(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationRecorder.RecordingModeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79c601a52da19c88133151b63852ca6a6ba71894cd962c2e118e75d604e83fe5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordingMode", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_config.CfnConfigurationRecorder.ExclusionByResourceTypesProperty",
        jsii_struct_bases=[],
        name_mapping={"resource_types": "resourceTypes"},
    )
    class ExclusionByResourceTypesProperty:
        def __init__(self, *, resource_types: typing.Sequence[builtins.str]) -> None:
            '''Specifies whether the configuration recorder excludes certain resource types from being recorded.

            Use the ``ResourceTypes`` field to enter a comma-separated list of resource types you want to exclude from recording.

            By default, when AWS Config adds support for a new resource type in the Region where you set up the configuration recorder, including global resource types, AWS Config starts recording resources of that type automatically.
            .. epigraph::

               *How to use the exclusion recording strategy*

               To use this option, you must set the ``useOnly`` field of `RecordingStrategy <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingStrategy.html>`_ to ``EXCLUSION_BY_RESOURCE_TYPES`` .

               AWS Config will then record configuration changes for all supported resource types, except the resource types that you specify to exclude from being recorded.

               *Global resource types and the exclusion recording strategy*

               Unless specifically listed as exclusions, ``AWS::RDS::GlobalCluster`` will be recorded automatically in all supported AWS Config Regions were the configuration recorder is enabled.

               IAM users, groups, roles, and customer managed policies will be recorded in the Region where you set up the configuration recorder if that is a Region where AWS Config was available before February 2022. You cannot be record the global IAM resouce types in Regions supported by AWS Config after February 2022. This list where you cannot record the global IAM resource types includes the following Regions:

               - Asia Pacific (Hyderabad)
               - Asia Pacific (Melbourne)
               - Canada West (Calgary)
               - Europe (Spain)
               - Europe (Zurich)
               - Israel (Tel Aviv)
               - Middle East (UAE)

            :param resource_types: A comma-separated list of resource types to exclude from recording by the configuration recorder.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-exclusionbyresourcetypes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_config as config
                
                exclusion_by_resource_types_property = config.CfnConfigurationRecorder.ExclusionByResourceTypesProperty(
                    resource_types=["resourceTypes"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1bfeeb41a82e166dbe5ee3f6a4cb224863af8ea802ed4106641b03f2b048f32a)
                check_type(argname="argument resource_types", value=resource_types, expected_type=type_hints["resource_types"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_types": resource_types,
            }

        @builtins.property
        def resource_types(self) -> typing.List[builtins.str]:
            '''A comma-separated list of resource types to exclude from recording by the configuration recorder.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-exclusionbyresourcetypes.html#cfn-config-configurationrecorder-exclusionbyresourcetypes-resourcetypes
            '''
            result = self._values.get("resource_types")
            assert result is not None, "Required property 'resource_types' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExclusionByResourceTypesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_config.CfnConfigurationRecorder.RecordingGroupProperty",
        jsii_struct_bases=[],
        name_mapping={
            "all_supported": "allSupported",
            "exclusion_by_resource_types": "exclusionByResourceTypes",
            "include_global_resource_types": "includeGlobalResourceTypes",
            "recording_strategy": "recordingStrategy",
            "resource_types": "resourceTypes",
        },
    )
    class RecordingGroupProperty:
        def __init__(
            self,
            *,
            all_supported: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            exclusion_by_resource_types: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationRecorder.ExclusionByResourceTypesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            include_global_resource_types: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            recording_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationRecorder.RecordingStrategyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Specifies which resource types AWS Config records for configuration changes.

            By default, AWS Config records configuration changes for all current and future supported resource types in the AWS Region where you have enabled AWS Config , excluding the global IAM resource types: IAM users, groups, roles, and customer managed policies.

            In the recording group, you specify whether you want to record all supported current and future supported resource types or to include or exclude specific resources types. For a list of supported resource types, see `Supported Resource Types <https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources>`_ in the *AWS Config developer guide* .

            If you don't want AWS Config to record all current and future supported resource types (excluding the global IAM resource types), use one of the following recording strategies:

            - *Record all current and future resource types with exclusions* ( ``EXCLUSION_BY_RESOURCE_TYPES`` ), or
            - *Record specific resource types* ( ``INCLUSION_BY_RESOURCE_TYPES`` ).

            If you use the recording strategy to *Record all current and future resource types* ( ``ALL_SUPPORTED_RESOURCE_TYPES`` ), you can use the flag ``IncludeGlobalResourceTypes`` to include the global IAM resource types in your recording.
            .. epigraph::

               *Aurora global clusters are recorded in all enabled Regions*

               The ``AWS::RDS::GlobalCluster`` resource type will be recorded in all supported AWS Config Regions where the configuration recorder is enabled.

               If you do not want to record ``AWS::RDS::GlobalCluster`` in all enabled Regions, use the ``EXCLUSION_BY_RESOURCE_TYPES`` or ``INCLUSION_BY_RESOURCE_TYPES`` recording strategy.

            :param all_supported: Specifies whether AWS Config records configuration changes for all supported resource types, excluding the global IAM resource types. If you set this field to ``true`` , when AWS Config adds support for a new resource type, AWS Config starts recording resources of that type automatically. If you set this field to ``true`` , you cannot enumerate specific resource types to record in the ``resourceTypes`` field of `RecordingGroup <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html>`_ , or to exclude in the ``resourceTypes`` field of `ExclusionByResourceTypes <https://docs.aws.amazon.com/config/latest/APIReference/API_ExclusionByResourceTypes.html>`_ . .. epigraph:: *Region availability* Check `Resource Coverage by Region Availability <https://docs.aws.amazon.com/config/latest/developerguide/what-is-resource-config-coverage.html>`_ to see if a resource type is supported in the AWS Region where you set up AWS Config .
            :param exclusion_by_resource_types: An object that specifies how AWS Config excludes resource types from being recorded by the configuration recorder. To use this option, you must set the ``useOnly`` field of `AWS::Config::ConfigurationRecorder RecordingStrategy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordingstrategy.html>`_ to ``EXCLUSION_BY_RESOURCE_TYPES`` .
            :param include_global_resource_types: This option is a bundle which only applies to the global IAM resource types: IAM users, groups, roles, and customer managed policies. These global IAM resource types can only be recorded by AWS Config in Regions where AWS Config was available before February 2022. You cannot be record the global IAM resouce types in Regions supported by AWS Config after February 2022. This list where you cannot record the global IAM resource types includes the following Regions: - Asia Pacific (Hyderabad) - Asia Pacific (Melbourne) - Canada West (Calgary) - Europe (Spain) - Europe (Zurich) - Israel (Tel Aviv) - Middle East (UAE) .. epigraph:: *Aurora global clusters are recorded in all enabled Regions* The ``AWS::RDS::GlobalCluster`` resource type will be recorded in all supported AWS Config Regions where the configuration recorder is enabled, even if ``IncludeGlobalResourceTypes`` is set to ``false`` . The ``IncludeGlobalResourceTypes`` option is a bundle which only applies to IAM users, groups, roles, and customer managed policies. If you do not want to record ``AWS::RDS::GlobalCluster`` in all enabled Regions, use one of the following recording strategies: - *Record all current and future resource types with exclusions* ( ``EXCLUSION_BY_RESOURCE_TYPES`` ), or - *Record specific resource types* ( ``INCLUSION_BY_RESOURCE_TYPES`` ). For more information, see `Selecting Which Resources are Recorded <https://docs.aws.amazon.com/config/latest/developerguide/select-resources.html#select-resources-all>`_ in the *AWS Config developer guide* . > *IncludeGlobalResourceTypes and the exclusion recording strategy* The ``IncludeGlobalResourceTypes`` field has no impact on the ``EXCLUSION_BY_RESOURCE_TYPES`` recording strategy. This means that the global IAM resource types ( IAM users, groups, roles, and customer managed policies) will not be automatically added as exclusions for ``ExclusionByResourceTypes`` when ``IncludeGlobalResourceTypes`` is set to ``false`` . The ``IncludeGlobalResourceTypes`` field should only be used to modify the ``AllSupported`` field, as the default for the ``AllSupported`` field is to record configuration changes for all supported resource types excluding the global IAM resource types. To include the global IAM resource types when ``AllSupported`` is set to ``true`` , make sure to set ``IncludeGlobalResourceTypes`` to ``true`` . To exclude the global IAM resource types for the ``EXCLUSION_BY_RESOURCE_TYPES`` recording strategy, you need to manually add them to the ``ResourceTypes`` field of ``ExclusionByResourceTypes`` . > *Required and optional fields* Before you set this field to ``true`` , set the ``AllSupported`` field of `RecordingGroup <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html>`_ to ``true`` . Optionally, you can set the ``useOnly`` field of `RecordingStrategy <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingStrategy.html>`_ to ``ALL_SUPPORTED_RESOURCE_TYPES`` . > *Overriding fields* If you set this field to ``false`` but list global IAM resource types in the ``ResourceTypes`` field of `RecordingGroup <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html>`_ , AWS Config will still record configuration changes for those specified resource types *regardless* of if you set the ``IncludeGlobalResourceTypes`` field to false. If you do not want to record configuration changes to the global IAM resource types (IAM users, groups, roles, and customer managed policies), make sure to not list them in the ``ResourceTypes`` field in addition to setting the ``IncludeGlobalResourceTypes`` field to false.
            :param recording_strategy: An object that specifies the recording strategy for the configuration recorder. - If you set the ``useOnly`` field of `RecordingStrategy <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingStrategy.html>`_ to ``ALL_SUPPORTED_RESOURCE_TYPES`` , AWS Config records configuration changes for all supported resource types, excluding the global IAM resource types. You also must set the ``AllSupported`` field of `RecordingGroup <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html>`_ to ``true`` . When AWS Config adds support for a new resource type, AWS Config automatically starts recording resources of that type. - If you set the ``useOnly`` field of `RecordingStrategy <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingStrategy.html>`_ to ``INCLUSION_BY_RESOURCE_TYPES`` , AWS Config records configuration changes for only the resource types you specify in the ``ResourceTypes`` field of `RecordingGroup <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html>`_ . - If you set the ``useOnly`` field of `RecordingStrategy <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingStrategy.html>`_ to ``EXCLUSION_BY_RESOURCE_TYPES`` , AWS Config records configuration changes for all supported resource types except the resource types that you specify to exclude from being recorded in the ``ResourceTypes`` field of `ExclusionByResourceTypes <https://docs.aws.amazon.com/config/latest/APIReference/API_ExclusionByResourceTypes.html>`_ . .. epigraph:: *Required and optional fields* The ``recordingStrategy`` field is optional when you set the ``AllSupported`` field of `RecordingGroup <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html>`_ to ``true`` . The ``recordingStrategy`` field is optional when you list resource types in the ``ResourceTypes`` field of `RecordingGroup <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html>`_ . The ``recordingStrategy`` field is required if you list resource types to exclude from recording in the ``ResourceTypes`` field of `ExclusionByResourceTypes <https://docs.aws.amazon.com/config/latest/APIReference/API_ExclusionByResourceTypes.html>`_ . > *Overriding fields* If you choose ``EXCLUSION_BY_RESOURCE_TYPES`` for the recording strategy, the ``ExclusionByResourceTypes`` field will override other properties in the request. For example, even if you set ``IncludeGlobalResourceTypes`` to false, global IAM resource types will still be automatically recorded in this option unless those resource types are specifically listed as exclusions in the ``ResourceTypes`` field of ``ExclusionByResourceTypes`` . > *Global resources types and the resource exclusion recording strategy* By default, if you choose the ``EXCLUSION_BY_RESOURCE_TYPES`` recording strategy, when AWS Config adds support for a new resource type in the Region where you set up the configuration recorder, including global resource types, AWS Config starts recording resources of that type automatically. Unless specifically listed as exclusions, ``AWS::RDS::GlobalCluster`` will be recorded automatically in all supported AWS Config Regions were the configuration recorder is enabled. IAM users, groups, roles, and customer managed policies will be recorded in the Region where you set up the configuration recorder if that is a Region where AWS Config was available before February 2022. You cannot be record the global IAM resouce types in Regions supported by AWS Config after February 2022. This list where you cannot record the global IAM resource types includes the following Regions: - Asia Pacific (Hyderabad) - Asia Pacific (Melbourne) - Canada West (Calgary) - Europe (Spain) - Europe (Zurich) - Israel (Tel Aviv) - Middle East (UAE)
            :param resource_types: A comma-separated list that specifies which resource types AWS Config records. For a list of valid ``ResourceTypes`` values, see the *Resource Type Value* column in `Supported AWS resource Types <https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources>`_ in the *AWS Config developer guide* . .. epigraph:: *Required and optional fields* Optionally, you can set the ``useOnly`` field of `RecordingStrategy <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingStrategy.html>`_ to ``INCLUSION_BY_RESOURCE_TYPES`` . To record all configuration changes, set the ``AllSupported`` field of `RecordingGroup <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html>`_ to ``true`` , and either omit this field or don't specify any resource types in this field. If you set the ``AllSupported`` field to ``false`` and specify values for ``ResourceTypes`` , when AWS Config adds support for a new type of resource, it will not record resources of that type unless you manually add that type to your recording group. > *Region availability* Before specifying a resource type for AWS Config to track, check `Resource Coverage by Region Availability <https://docs.aws.amazon.com/config/latest/developerguide/what-is-resource-config-coverage.html>`_ to see if the resource type is supported in the AWS Region where you set up AWS Config . If a resource type is supported by AWS Config in at least one Region, you can enable the recording of that resource type in all Regions supported by AWS Config , even if the specified resource type is not supported in the AWS Region where you set up AWS Config .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_config as config
                
                recording_group_property = config.CfnConfigurationRecorder.RecordingGroupProperty(
                    all_supported=False,
                    exclusion_by_resource_types=config.CfnConfigurationRecorder.ExclusionByResourceTypesProperty(
                        resource_types=["resourceTypes"]
                    ),
                    include_global_resource_types=False,
                    recording_strategy=config.CfnConfigurationRecorder.RecordingStrategyProperty(
                        use_only="useOnly"
                    ),
                    resource_types=["resourceTypes"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__574b2463724d6487e33926405844644e49df72910787a048a5ca198552045f16)
                check_type(argname="argument all_supported", value=all_supported, expected_type=type_hints["all_supported"])
                check_type(argname="argument exclusion_by_resource_types", value=exclusion_by_resource_types, expected_type=type_hints["exclusion_by_resource_types"])
                check_type(argname="argument include_global_resource_types", value=include_global_resource_types, expected_type=type_hints["include_global_resource_types"])
                check_type(argname="argument recording_strategy", value=recording_strategy, expected_type=type_hints["recording_strategy"])
                check_type(argname="argument resource_types", value=resource_types, expected_type=type_hints["resource_types"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if all_supported is not None:
                self._values["all_supported"] = all_supported
            if exclusion_by_resource_types is not None:
                self._values["exclusion_by_resource_types"] = exclusion_by_resource_types
            if include_global_resource_types is not None:
                self._values["include_global_resource_types"] = include_global_resource_types
            if recording_strategy is not None:
                self._values["recording_strategy"] = recording_strategy
            if resource_types is not None:
                self._values["resource_types"] = resource_types

        @builtins.property
        def all_supported(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether AWS Config records configuration changes for all supported resource types, excluding the global IAM resource types.

            If you set this field to ``true`` , when AWS Config adds support for a new resource type, AWS Config starts recording resources of that type automatically.

            If you set this field to ``true`` , you cannot enumerate specific resource types to record in the ``resourceTypes`` field of `RecordingGroup <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html>`_ , or to exclude in the ``resourceTypes`` field of `ExclusionByResourceTypes <https://docs.aws.amazon.com/config/latest/APIReference/API_ExclusionByResourceTypes.html>`_ .
            .. epigraph::

               *Region availability*

               Check `Resource Coverage by Region Availability <https://docs.aws.amazon.com/config/latest/developerguide/what-is-resource-config-coverage.html>`_ to see if a resource type is supported in the AWS Region where you set up AWS Config .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html#cfn-config-configurationrecorder-recordinggroup-allsupported
            '''
            result = self._values.get("all_supported")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def exclusion_by_resource_types(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationRecorder.ExclusionByResourceTypesProperty"]]:
            '''An object that specifies how AWS Config excludes resource types from being recorded by the configuration recorder.

            To use this option, you must set the ``useOnly`` field of `AWS::Config::ConfigurationRecorder RecordingStrategy <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordingstrategy.html>`_ to ``EXCLUSION_BY_RESOURCE_TYPES`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html#cfn-config-configurationrecorder-recordinggroup-exclusionbyresourcetypes
            '''
            result = self._values.get("exclusion_by_resource_types")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationRecorder.ExclusionByResourceTypesProperty"]], result)

        @builtins.property
        def include_global_resource_types(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''This option is a bundle which only applies to the global IAM resource types: IAM users, groups, roles, and customer managed policies.

            These global IAM resource types can only be recorded by AWS Config in Regions where AWS Config was available before February 2022. You cannot be record the global IAM resouce types in Regions supported by AWS Config after February 2022. This list where you cannot record the global IAM resource types includes the following Regions:

            - Asia Pacific (Hyderabad)
            - Asia Pacific (Melbourne)
            - Canada West (Calgary)
            - Europe (Spain)
            - Europe (Zurich)
            - Israel (Tel Aviv)
            - Middle East (UAE)

            .. epigraph::

               *Aurora global clusters are recorded in all enabled Regions*

               The ``AWS::RDS::GlobalCluster`` resource type will be recorded in all supported AWS Config Regions where the configuration recorder is enabled, even if ``IncludeGlobalResourceTypes`` is set to ``false`` . The ``IncludeGlobalResourceTypes`` option is a bundle which only applies to IAM users, groups, roles, and customer managed policies.

               If you do not want to record ``AWS::RDS::GlobalCluster`` in all enabled Regions, use one of the following recording strategies:

               - *Record all current and future resource types with exclusions* ( ``EXCLUSION_BY_RESOURCE_TYPES`` ), or
               - *Record specific resource types* ( ``INCLUSION_BY_RESOURCE_TYPES`` ).

               For more information, see `Selecting Which Resources are Recorded <https://docs.aws.amazon.com/config/latest/developerguide/select-resources.html#select-resources-all>`_ in the *AWS Config developer guide* . > *IncludeGlobalResourceTypes and the exclusion recording strategy*

               The ``IncludeGlobalResourceTypes`` field has no impact on the ``EXCLUSION_BY_RESOURCE_TYPES`` recording strategy. This means that the global IAM resource types ( IAM users, groups, roles, and customer managed policies) will not be automatically added as exclusions for ``ExclusionByResourceTypes`` when ``IncludeGlobalResourceTypes`` is set to ``false`` .

               The ``IncludeGlobalResourceTypes`` field should only be used to modify the ``AllSupported`` field, as the default for the ``AllSupported`` field is to record configuration changes for all supported resource types excluding the global IAM resource types. To include the global IAM resource types when ``AllSupported`` is set to ``true`` , make sure to set ``IncludeGlobalResourceTypes`` to ``true`` .

               To exclude the global IAM resource types for the ``EXCLUSION_BY_RESOURCE_TYPES`` recording strategy, you need to manually add them to the ``ResourceTypes`` field of ``ExclusionByResourceTypes`` . > *Required and optional fields*

               Before you set this field to ``true`` , set the ``AllSupported`` field of `RecordingGroup <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html>`_ to ``true`` . Optionally, you can set the ``useOnly`` field of `RecordingStrategy <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingStrategy.html>`_ to ``ALL_SUPPORTED_RESOURCE_TYPES`` . > *Overriding fields*

               If you set this field to ``false`` but list global IAM resource types in the ``ResourceTypes`` field of `RecordingGroup <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html>`_ , AWS Config will still record configuration changes for those specified resource types *regardless* of if you set the ``IncludeGlobalResourceTypes`` field to false.

               If you do not want to record configuration changes to the global IAM resource types (IAM users, groups, roles, and customer managed policies), make sure to not list them in the ``ResourceTypes`` field in addition to setting the ``IncludeGlobalResourceTypes`` field to false.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html#cfn-config-configurationrecorder-recordinggroup-includeglobalresourcetypes
            '''
            result = self._values.get("include_global_resource_types")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def recording_strategy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationRecorder.RecordingStrategyProperty"]]:
            '''An object that specifies the recording strategy for the configuration recorder.

            - If you set the ``useOnly`` field of `RecordingStrategy <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingStrategy.html>`_ to ``ALL_SUPPORTED_RESOURCE_TYPES`` , AWS Config records configuration changes for all supported resource types, excluding the global IAM resource types. You also must set the ``AllSupported`` field of `RecordingGroup <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html>`_ to ``true`` . When AWS Config adds support for a new resource type, AWS Config automatically starts recording resources of that type.
            - If you set the ``useOnly`` field of `RecordingStrategy <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingStrategy.html>`_ to ``INCLUSION_BY_RESOURCE_TYPES`` , AWS Config records configuration changes for only the resource types you specify in the ``ResourceTypes`` field of `RecordingGroup <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html>`_ .
            - If you set the ``useOnly`` field of `RecordingStrategy <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingStrategy.html>`_ to ``EXCLUSION_BY_RESOURCE_TYPES`` , AWS Config records configuration changes for all supported resource types except the resource types that you specify to exclude from being recorded in the ``ResourceTypes`` field of `ExclusionByResourceTypes <https://docs.aws.amazon.com/config/latest/APIReference/API_ExclusionByResourceTypes.html>`_ .

            .. epigraph::

               *Required and optional fields*

               The ``recordingStrategy`` field is optional when you set the ``AllSupported`` field of `RecordingGroup <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html>`_ to ``true`` .

               The ``recordingStrategy`` field is optional when you list resource types in the ``ResourceTypes`` field of `RecordingGroup <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html>`_ .

               The ``recordingStrategy`` field is required if you list resource types to exclude from recording in the ``ResourceTypes`` field of `ExclusionByResourceTypes <https://docs.aws.amazon.com/config/latest/APIReference/API_ExclusionByResourceTypes.html>`_ . > *Overriding fields*

               If you choose ``EXCLUSION_BY_RESOURCE_TYPES`` for the recording strategy, the ``ExclusionByResourceTypes`` field will override other properties in the request.

               For example, even if you set ``IncludeGlobalResourceTypes`` to false, global IAM resource types will still be automatically recorded in this option unless those resource types are specifically listed as exclusions in the ``ResourceTypes`` field of ``ExclusionByResourceTypes`` . > *Global resources types and the resource exclusion recording strategy*

               By default, if you choose the ``EXCLUSION_BY_RESOURCE_TYPES`` recording strategy, when AWS Config adds support for a new resource type in the Region where you set up the configuration recorder, including global resource types, AWS Config starts recording resources of that type automatically.

               Unless specifically listed as exclusions, ``AWS::RDS::GlobalCluster`` will be recorded automatically in all supported AWS Config Regions were the configuration recorder is enabled.

               IAM users, groups, roles, and customer managed policies will be recorded in the Region where you set up the configuration recorder if that is a Region where AWS Config was available before February 2022. You cannot be record the global IAM resouce types in Regions supported by AWS Config after February 2022. This list where you cannot record the global IAM resource types includes the following Regions:

               - Asia Pacific (Hyderabad)
               - Asia Pacific (Melbourne)
               - Canada West (Calgary)
               - Europe (Spain)
               - Europe (Zurich)
               - Israel (Tel Aviv)
               - Middle East (UAE)

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html#cfn-config-configurationrecorder-recordinggroup-recordingstrategy
            '''
            result = self._values.get("recording_strategy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationRecorder.RecordingStrategyProperty"]], result)

        @builtins.property
        def resource_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A comma-separated list that specifies which resource types AWS Config records.

            For a list of valid ``ResourceTypes`` values, see the *Resource Type Value* column in `Supported AWS resource Types <https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources>`_ in the *AWS Config developer guide* .
            .. epigraph::

               *Required and optional fields*

               Optionally, you can set the ``useOnly`` field of `RecordingStrategy <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingStrategy.html>`_ to ``INCLUSION_BY_RESOURCE_TYPES`` .

               To record all configuration changes, set the ``AllSupported`` field of `RecordingGroup <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html>`_ to ``true`` , and either omit this field or don't specify any resource types in this field. If you set the ``AllSupported`` field to ``false`` and specify values for ``ResourceTypes`` , when AWS Config adds support for a new type of resource, it will not record resources of that type unless you manually add that type to your recording group. > *Region availability*

               Before specifying a resource type for AWS Config to track, check `Resource Coverage by Region Availability <https://docs.aws.amazon.com/config/latest/developerguide/what-is-resource-config-coverage.html>`_ to see if the resource type is supported in the AWS Region where you set up AWS Config . If a resource type is supported by AWS Config in at least one Region, you can enable the recording of that resource type in all Regions supported by AWS Config , even if the specified resource type is not supported in the AWS Region where you set up AWS Config .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordinggroup.html#cfn-config-configurationrecorder-recordinggroup-resourcetypes
            '''
            result = self._values.get("resource_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecordingGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_config.CfnConfigurationRecorder.RecordingModeOverrideProperty",
        jsii_struct_bases=[],
        name_mapping={
            "recording_frequency": "recordingFrequency",
            "resource_types": "resourceTypes",
            "description": "description",
        },
    )
    class RecordingModeOverrideProperty:
        def __init__(
            self,
            *,
            recording_frequency: builtins.str,
            resource_types: typing.Sequence[builtins.str],
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object for you to specify your overrides for the recording mode.

            :param recording_frequency: The recording frequency that will be applied to all the resource types specified in the override. - Continuous recording allows you to record configuration changes continuously whenever a change occurs. - Daily recording allows you to receive a configuration item (CI) representing the most recent state of your resources over the last 24-hour period, only if it’s different from the previous CI recorded. .. epigraph:: AWS Firewall Manager depends on continuous recording to monitor your resources. If you are using Firewall Manager, it is recommended that you set the recording frequency to Continuous.
            :param resource_types: A comma-separated list that specifies which resource types AWS Config includes in the override. .. epigraph:: Daily recording is not supported for the following resource types: - ``AWS::Config::ResourceCompliance`` - ``AWS::Config::ConformancePackCompliance`` - ``AWS::Config::ConfigurationRecorder``
            :param description: A description that you provide for the override.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordingmodeoverride.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_config as config
                
                recording_mode_override_property = config.CfnConfigurationRecorder.RecordingModeOverrideProperty(
                    recording_frequency="recordingFrequency",
                    resource_types=["resourceTypes"],
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__301d91ec25370b3d9c2f7b2aef5e6913cf2370b1c4e1ffda877aafd174d11165)
                check_type(argname="argument recording_frequency", value=recording_frequency, expected_type=type_hints["recording_frequency"])
                check_type(argname="argument resource_types", value=resource_types, expected_type=type_hints["resource_types"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "recording_frequency": recording_frequency,
                "resource_types": resource_types,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def recording_frequency(self) -> builtins.str:
            '''The recording frequency that will be applied to all the resource types specified in the override.

            - Continuous recording allows you to record configuration changes continuously whenever a change occurs.
            - Daily recording allows you to receive a configuration item (CI) representing the most recent state of your resources over the last 24-hour period, only if it’s different from the previous CI recorded.

            .. epigraph::

               AWS Firewall Manager depends on continuous recording to monitor your resources. If you are using Firewall Manager, it is recommended that you set the recording frequency to Continuous.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordingmodeoverride.html#cfn-config-configurationrecorder-recordingmodeoverride-recordingfrequency
            '''
            result = self._values.get("recording_frequency")
            assert result is not None, "Required property 'recording_frequency' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource_types(self) -> typing.List[builtins.str]:
            '''A comma-separated list that specifies which resource types AWS Config includes in the override.

            .. epigraph::

               Daily recording is not supported for the following resource types:

               - ``AWS::Config::ResourceCompliance``
               - ``AWS::Config::ConformancePackCompliance``
               - ``AWS::Config::ConfigurationRecorder``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordingmodeoverride.html#cfn-config-configurationrecorder-recordingmodeoverride-resourcetypes
            '''
            result = self._values.get("resource_types")
            assert result is not None, "Required property 'resource_types' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''A description that you provide for the override.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordingmodeoverride.html#cfn-config-configurationrecorder-recordingmodeoverride-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecordingModeOverrideProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_config.CfnConfigurationRecorder.RecordingModeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "recording_frequency": "recordingFrequency",
            "recording_mode_overrides": "recordingModeOverrides",
        },
    )
    class RecordingModeProperty:
        def __init__(
            self,
            *,
            recording_frequency: builtins.str,
            recording_mode_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationRecorder.RecordingModeOverrideProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Specifies the default recording frequency that AWS Config uses to record configuration changes.

            AWS Config supports *Continuous recording* and *Daily recording* .

            - Continuous recording allows you to record configuration changes continuously whenever a change occurs.
            - Daily recording allows you to receive a configuration item (CI) representing the most recent state of your resources over the last 24-hour period, only if it’s different from the previous CI recorded.

            .. epigraph::

               AWS Firewall Manager depends on continuous recording to monitor your resources. If you are using Firewall Manager, it is recommended that you set the recording frequency to Continuous.

            You can also override the recording frequency for specific resource types.

            :param recording_frequency: The default recording frequency that AWS Config uses to record configuration changes. .. epigraph:: Daily recording is not supported for the following resource types: - ``AWS::Config::ResourceCompliance`` - ``AWS::Config::ConformancePackCompliance`` - ``AWS::Config::ConfigurationRecorder`` For the *allSupported* ( ``ALL_SUPPORTED_RESOURCE_TYPES`` ) recording strategy, these resource types will be set to Continuous recording.
            :param recording_mode_overrides: An array of ``recordingModeOverride`` objects for you to specify your overrides for the recording mode. The ``recordingModeOverride`` object in the ``recordingModeOverrides`` array consists of three fields: a ``description`` , the new ``recordingFrequency`` , and an array of ``resourceTypes`` to override.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordingmode.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_config as config
                
                recording_mode_property = config.CfnConfigurationRecorder.RecordingModeProperty(
                    recording_frequency="recordingFrequency",
                
                    # the properties below are optional
                    recording_mode_overrides=[config.CfnConfigurationRecorder.RecordingModeOverrideProperty(
                        recording_frequency="recordingFrequency",
                        resource_types=["resourceTypes"],
                
                        # the properties below are optional
                        description="description"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2db8a0d318e287d3329642f2526ea9c788965e7dbe0f581278bef988ee908d63)
                check_type(argname="argument recording_frequency", value=recording_frequency, expected_type=type_hints["recording_frequency"])
                check_type(argname="argument recording_mode_overrides", value=recording_mode_overrides, expected_type=type_hints["recording_mode_overrides"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "recording_frequency": recording_frequency,
            }
            if recording_mode_overrides is not None:
                self._values["recording_mode_overrides"] = recording_mode_overrides

        @builtins.property
        def recording_frequency(self) -> builtins.str:
            '''The default recording frequency that AWS Config uses to record configuration changes.

            .. epigraph::

               Daily recording is not supported for the following resource types:

               - ``AWS::Config::ResourceCompliance``
               - ``AWS::Config::ConformancePackCompliance``
               - ``AWS::Config::ConfigurationRecorder``

               For the *allSupported* ( ``ALL_SUPPORTED_RESOURCE_TYPES`` ) recording strategy, these resource types will be set to Continuous recording.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordingmode.html#cfn-config-configurationrecorder-recordingmode-recordingfrequency
            '''
            result = self._values.get("recording_frequency")
            assert result is not None, "Required property 'recording_frequency' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def recording_mode_overrides(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigurationRecorder.RecordingModeOverrideProperty"]]]]:
            '''An array of ``recordingModeOverride`` objects for you to specify your overrides for the recording mode.

            The ``recordingModeOverride`` object in the ``recordingModeOverrides`` array consists of three fields: a ``description`` , the new ``recordingFrequency`` , and an array of ``resourceTypes`` to override.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordingmode.html#cfn-config-configurationrecorder-recordingmode-recordingmodeoverrides
            '''
            result = self._values.get("recording_mode_overrides")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigurationRecorder.RecordingModeOverrideProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecordingModeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_config.CfnConfigurationRecorder.RecordingStrategyProperty",
        jsii_struct_bases=[],
        name_mapping={"use_only": "useOnly"},
    )
    class RecordingStrategyProperty:
        def __init__(self, *, use_only: builtins.str) -> None:
            '''Specifies the recording strategy of the configuration recorder.

            Valid values include: ``ALL_SUPPORTED_RESOURCE_TYPES`` , ``INCLUSION_BY_RESOURCE_TYPES`` , and ``EXCLUSION_BY_RESOURCE_TYPES`` .

            :param use_only: The recording strategy for the configuration recorder. - If you set this option to ``ALL_SUPPORTED_RESOURCE_TYPES`` , AWS Config records configuration changes for all supported resource types, excluding the global IAM resource types. You also must set the ``AllSupported`` field of `RecordingGroup <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html>`_ to ``true`` . When AWS Config adds support for a new resource type, AWS Config automatically starts recording resources of that type. For a list of supported resource types, see `Supported Resource Types <https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources>`_ in the *AWS Config developer guide* . - If you set this option to ``INCLUSION_BY_RESOURCE_TYPES`` , AWS Config records configuration changes for only the resource types that you specify in the ``ResourceTypes`` field of `RecordingGroup <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html>`_ . - If you set this option to ``EXCLUSION_BY_RESOURCE_TYPES`` , AWS Config records configuration changes for all supported resource types, except the resource types that you specify to exclude from being recorded in the ``ResourceTypes`` field of `ExclusionByResourceTypes <https://docs.aws.amazon.com/config/latest/APIReference/API_ExclusionByResourceTypes.html>`_ . .. epigraph:: *Required and optional fields* The ``recordingStrategy`` field is optional when you set the ``AllSupported`` field of `RecordingGroup <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html>`_ to ``true`` . The ``recordingStrategy`` field is optional when you list resource types in the ``ResourceTypes`` field of `RecordingGroup <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html>`_ . The ``recordingStrategy`` field is required if you list resource types to exclude from recording in the ``ResourceTypes`` field of `ExclusionByResourceTypes <https://docs.aws.amazon.com/config/latest/APIReference/API_ExclusionByResourceTypes.html>`_ . > *Overriding fields* If you choose ``EXCLUSION_BY_RESOURCE_TYPES`` for the recording strategy, the ``ExclusionByResourceTypes`` field will override other properties in the request. For example, even if you set ``IncludeGlobalResourceTypes`` to false, global IAM resource types will still be automatically recorded in this option unless those resource types are specifically listed as exclusions in the ``ResourceTypes`` field of ``ExclusionByResourceTypes`` . > *Global resource types and the exclusion recording strategy* By default, if you choose the ``EXCLUSION_BY_RESOURCE_TYPES`` recording strategy, when AWS Config adds support for a new resource type in the Region where you set up the configuration recorder, including global resource types, AWS Config starts recording resources of that type automatically. Unless specifically listed as exclusions, ``AWS::RDS::GlobalCluster`` will be recorded automatically in all supported AWS Config Regions were the configuration recorder is enabled. IAM users, groups, roles, and customer managed policies will be recorded in the Region where you set up the configuration recorder if that is a Region where AWS Config was available before February 2022. You cannot be record the global IAM resouce types in Regions supported by AWS Config after February 2022. This list where you cannot record the global IAM resource types includes the following Regions: - Asia Pacific (Hyderabad) - Asia Pacific (Melbourne) - Canada West (Calgary) - Europe (Spain) - Europe (Zurich) - Israel (Tel Aviv) - Middle East (UAE)

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordingstrategy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_config as config
                
                recording_strategy_property = config.CfnConfigurationRecorder.RecordingStrategyProperty(
                    use_only="useOnly"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cdc0c3a0d4a9aa5083c337e0372ddbd0be93f7adadc83df65d33ce75c0b906bb)
                check_type(argname="argument use_only", value=use_only, expected_type=type_hints["use_only"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "use_only": use_only,
            }

        @builtins.property
        def use_only(self) -> builtins.str:
            '''The recording strategy for the configuration recorder.

            - If you set this option to ``ALL_SUPPORTED_RESOURCE_TYPES`` , AWS Config records configuration changes for all supported resource types, excluding the global IAM resource types. You also must set the ``AllSupported`` field of `RecordingGroup <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html>`_ to ``true`` . When AWS Config adds support for a new resource type, AWS Config automatically starts recording resources of that type. For a list of supported resource types, see `Supported Resource Types <https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html#supported-resources>`_ in the *AWS Config developer guide* .
            - If you set this option to ``INCLUSION_BY_RESOURCE_TYPES`` , AWS Config records configuration changes for only the resource types that you specify in the ``ResourceTypes`` field of `RecordingGroup <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html>`_ .
            - If you set this option to ``EXCLUSION_BY_RESOURCE_TYPES`` , AWS Config records configuration changes for all supported resource types, except the resource types that you specify to exclude from being recorded in the ``ResourceTypes`` field of `ExclusionByResourceTypes <https://docs.aws.amazon.com/config/latest/APIReference/API_ExclusionByResourceTypes.html>`_ .

            .. epigraph::

               *Required and optional fields*

               The ``recordingStrategy`` field is optional when you set the ``AllSupported`` field of `RecordingGroup <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html>`_ to ``true`` .

               The ``recordingStrategy`` field is optional when you list resource types in the ``ResourceTypes`` field of `RecordingGroup <https://docs.aws.amazon.com/config/latest/APIReference/API_RecordingGroup.html>`_ .

               The ``recordingStrategy`` field is required if you list resource types to exclude from recording in the ``ResourceTypes`` field of `ExclusionByResourceTypes <https://docs.aws.amazon.com/config/latest/APIReference/API_ExclusionByResourceTypes.html>`_ . > *Overriding fields*

               If you choose ``EXCLUSION_BY_RESOURCE_TYPES`` for the recording strategy, the ``ExclusionByResourceTypes`` field will override other properties in the request.

               For example, even if you set ``IncludeGlobalResourceTypes`` to false, global IAM resource types will still be automatically recorded in this option unless those resource types are specifically listed as exclusions in the ``ResourceTypes`` field of ``ExclusionByResourceTypes`` . > *Global resource types and the exclusion recording strategy*

               By default, if you choose the ``EXCLUSION_BY_RESOURCE_TYPES`` recording strategy, when AWS Config adds support for a new resource type in the Region where you set up the configuration recorder, including global resource types, AWS Config starts recording resources of that type automatically.

               Unless specifically listed as exclusions, ``AWS::RDS::GlobalCluster`` will be recorded automatically in all supported AWS Config Regions were the configuration recorder is enabled.

               IAM users, groups, roles, and customer managed policies will be recorded in the Region where you set up the configuration recorder if that is a Region where AWS Config was available before February 2022. You cannot be record the global IAM resouce types in Regions supported by AWS Config after February 2022. This list where you cannot record the global IAM resource types includes the following Regions:

               - Asia Pacific (Hyderabad)
               - Asia Pacific (Melbourne)
               - Canada West (Calgary)
               - Europe (Spain)
               - Europe (Zurich)
               - Israel (Tel Aviv)
               - Middle East (UAE)

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-configurationrecorder-recordingstrategy.html#cfn-config-configurationrecorder-recordingstrategy-useonly
            '''
            result = self._values.get("use_only")
            assert result is not None, "Required property 'use_only' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecordingStrategyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_config.CfnConfigurationRecorderProps",
    jsii_struct_bases=[],
    name_mapping={
        "role_arn": "roleArn",
        "name": "name",
        "recording_group": "recordingGroup",
        "recording_mode": "recordingMode",
    },
)
class CfnConfigurationRecorderProps:
    def __init__(
        self,
        *,
        role_arn: builtins.str,
        name: typing.Optional[builtins.str] = None,
        recording_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationRecorder.RecordingGroupProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        recording_mode: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationRecorder.RecordingModeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfigurationRecorder``.

        :param role_arn: Amazon Resource Name (ARN) of the IAM role assumed by AWS Config and used by the configuration recorder. For more information, see `Permissions for the IAM Role Assigned <https://docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html>`_ to AWS Config in the AWS Config Developer Guide. .. epigraph:: *Pre-existing AWS Config role* If you have used an AWS service that uses AWS Config , such as AWS Security Hub or AWS Control Tower , and an AWS Config role has already been created, make sure that the IAM role that you use when setting up AWS Config keeps the same minimum permissions as the already created AWS Config role. You must do this so that the other AWS service continues to run as expected. For example, if AWS Control Tower has an IAM role that allows AWS Config to read Amazon Simple Storage Service ( Amazon S3 ) objects, make sure that the same permissions are granted within the IAM role you use when setting up AWS Config . Otherwise, it may interfere with how AWS Control Tower operates. For more information about IAM roles for AWS Config , see `*Identity and Access Management for AWS Config* <https://docs.aws.amazon.com/config/latest/developerguide/security-iam.html>`_ in the *AWS Config Developer Guide* .
        :param name: The name of the configuration recorder. AWS Config automatically assigns the name of "default" when creating the configuration recorder. You cannot change the name of the configuration recorder after it has been created. To change the configuration recorder name, you must delete it and create a new configuration recorder with a new name.
        :param recording_group: Specifies which resource types AWS Config records for configuration changes. .. epigraph:: *High Number of AWS Config Evaluations* You may notice increased activity in your account during your initial month recording with AWS Config when compared to subsequent months. During the initial bootstrapping process, AWS Config runs evaluations on all the resources in your account that you have selected for AWS Config to record. If you are running ephemeral workloads, you may see increased activity from AWS Config as it records configuration changes associated with creating and deleting these temporary resources. An *ephemeral workload* is a temporary use of computing resources that are loaded and run when needed. Examples include Amazon Elastic Compute Cloud ( Amazon EC2 ) Spot Instances, Amazon EMR jobs, and AWS Auto Scaling . If you want to avoid the increased activity from running ephemeral workloads, you can run these types of workloads in a separate account with AWS Config turned off to avoid increased configuration recording and rule evaluations.
        :param recording_mode: Specifies the default recording frequency that AWS Config uses to record configuration changes. AWS Config supports *Continuous recording* and *Daily recording* . - Continuous recording allows you to record configuration changes continuously whenever a change occurs. - Daily recording allows you to receive a configuration item (CI) representing the most recent state of your resources over the last 24-hour period, only if it’s different from the previous CI recorded. .. epigraph:: AWS Firewall Manager depends on continuous recording to monitor your resources. If you are using Firewall Manager, it is recommended that you set the recording frequency to Continuous. You can also override the recording frequency for specific resource types.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_config as config
            
            cfn_configuration_recorder_props = config.CfnConfigurationRecorderProps(
                role_arn="roleArn",
            
                # the properties below are optional
                name="name",
                recording_group=config.CfnConfigurationRecorder.RecordingGroupProperty(
                    all_supported=False,
                    exclusion_by_resource_types=config.CfnConfigurationRecorder.ExclusionByResourceTypesProperty(
                        resource_types=["resourceTypes"]
                    ),
                    include_global_resource_types=False,
                    recording_strategy=config.CfnConfigurationRecorder.RecordingStrategyProperty(
                        use_only="useOnly"
                    ),
                    resource_types=["resourceTypes"]
                ),
                recording_mode=config.CfnConfigurationRecorder.RecordingModeProperty(
                    recording_frequency="recordingFrequency",
            
                    # the properties below are optional
                    recording_mode_overrides=[config.CfnConfigurationRecorder.RecordingModeOverrideProperty(
                        recording_frequency="recordingFrequency",
                        resource_types=["resourceTypes"],
            
                        # the properties below are optional
                        description="description"
                    )]
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68cc2049b8c095672250d1c12a5af6fc05b3421a6c23124f87e5e31e2668698e)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument recording_group", value=recording_group, expected_type=type_hints["recording_group"])
            check_type(argname="argument recording_mode", value=recording_mode, expected_type=type_hints["recording_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_arn": role_arn,
        }
        if name is not None:
            self._values["name"] = name
        if recording_group is not None:
            self._values["recording_group"] = recording_group
        if recording_mode is not None:
            self._values["recording_mode"] = recording_mode

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Amazon Resource Name (ARN) of the IAM role assumed by AWS Config and used by the configuration recorder.

        For more information, see `Permissions for the IAM Role Assigned <https://docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html>`_ to AWS Config in the AWS Config Developer Guide.
        .. epigraph::

           *Pre-existing AWS Config role*

           If you have used an AWS service that uses AWS Config , such as AWS Security Hub or AWS Control Tower , and an AWS Config role has already been created, make sure that the IAM role that you use when setting up AWS Config keeps the same minimum permissions as the already created AWS Config role. You must do this so that the other AWS service continues to run as expected.

           For example, if AWS Control Tower has an IAM role that allows AWS Config to read Amazon Simple Storage Service ( Amazon S3 ) objects, make sure that the same permissions are granted within the IAM role you use when setting up AWS Config . Otherwise, it may interfere with how AWS Control Tower operates. For more information about IAM roles for AWS Config , see `*Identity and Access Management for AWS Config* <https://docs.aws.amazon.com/config/latest/developerguide/security-iam.html>`_ in the *AWS Config Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the configuration recorder. AWS Config automatically assigns the name of "default" when creating the configuration recorder.

        You cannot change the name of the configuration recorder after it has been created. To change the configuration recorder name, you must delete it and create a new configuration recorder with a new name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recording_group(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationRecorder.RecordingGroupProperty]]:
        '''Specifies which resource types AWS Config records for configuration changes.

        .. epigraph::

           *High Number of AWS Config Evaluations*

           You may notice increased activity in your account during your initial month recording with AWS Config when compared to subsequent months. During the initial bootstrapping process, AWS Config runs evaluations on all the resources in your account that you have selected for AWS Config to record.

           If you are running ephemeral workloads, you may see increased activity from AWS Config as it records configuration changes associated with creating and deleting these temporary resources. An *ephemeral workload* is a temporary use of computing resources that are loaded and run when needed. Examples include Amazon Elastic Compute Cloud ( Amazon EC2 ) Spot Instances, Amazon EMR jobs, and AWS Auto Scaling . If you want to avoid the increased activity from running ephemeral workloads, you can run these types of workloads in a separate account with AWS Config turned off to avoid increased configuration recording and rule evaluations.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-recordinggroup
        '''
        result = self._values.get("recording_group")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationRecorder.RecordingGroupProperty]], result)

    @builtins.property
    def recording_mode(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationRecorder.RecordingModeProperty]]:
        '''Specifies the default recording frequency that AWS Config uses to record configuration changes.

        AWS Config supports *Continuous recording* and *Daily recording* .

        - Continuous recording allows you to record configuration changes continuously whenever a change occurs.
        - Daily recording allows you to receive a configuration item (CI) representing the most recent state of your resources over the last 24-hour period, only if it’s different from the previous CI recorded.

        .. epigraph::

           AWS Firewall Manager depends on continuous recording to monitor your resources. If you are using Firewall Manager, it is recommended that you set the recording frequency to Continuous.

        You can also override the recording frequency for specific resource types.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html#cfn-config-configurationrecorder-recordingmode
        '''
        result = self._values.get("recording_mode")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationRecorder.RecordingModeProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationRecorderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnConformancePack(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_config.CfnConformancePack",
):
    '''A conformance pack is a collection of AWS Config rules and remediation actions that can be easily deployed in an account and a region.

    ConformancePack creates a service linked role in your account. The service linked role is created only when the role does not exist in your account.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html
    :cloudformationResource: AWS::Config::ConformancePack
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_config as config
        
        # template_ssm_document_details: Any
        
        cfn_conformance_pack = config.CfnConformancePack(self, "MyCfnConformancePack",
            conformance_pack_name="conformancePackName",
        
            # the properties below are optional
            conformance_pack_input_parameters=[config.CfnConformancePack.ConformancePackInputParameterProperty(
                parameter_name="parameterName",
                parameter_value="parameterValue"
            )],
            delivery_s3_bucket="deliveryS3Bucket",
            delivery_s3_key_prefix="deliveryS3KeyPrefix",
            template_body="templateBody",
            template_s3_uri="templateS3Uri",
            template_ssm_document_details=template_ssm_document_details
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        conformance_pack_name: builtins.str,
        conformance_pack_input_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConformancePack.ConformancePackInputParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        delivery_s3_bucket: typing.Optional[builtins.str] = None,
        delivery_s3_key_prefix: typing.Optional[builtins.str] = None,
        template_body: typing.Optional[builtins.str] = None,
        template_s3_uri: typing.Optional[builtins.str] = None,
        template_ssm_document_details: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param conformance_pack_name: Name of the conformance pack you want to create.
        :param conformance_pack_input_parameters: A list of ConformancePackInputParameter objects.
        :param delivery_s3_bucket: The name of the Amazon S3 bucket where AWS Config stores conformance pack templates.
        :param delivery_s3_key_prefix: The prefix for the Amazon S3 bucket.
        :param template_body: A string containing full conformance pack template body. Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. .. epigraph:: You can only use a YAML template with two resource types: config rule ( ``AWS::Config::ConfigRule`` ) and a remediation action ( ``AWS::Config::RemediationConfiguration`` ).
        :param template_s3_uri: Location of file containing the template body (s3://bucketname/prefix). The uri must point to the conformance pack template (max size: 300 KB) that is located in an Amazon S3 bucket. .. epigraph:: You must have access to read Amazon S3 bucket.
        :param template_ssm_document_details: An object that contains the name or Amazon Resource Name (ARN) of the AWS Systems Manager document (SSM document) and the version of the SSM document that is used to create a conformance pack.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e2b5c522b5074ba2ef97dd80a498043778309ce04aa178507276f160fde847d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConformancePackProps(
            conformance_pack_name=conformance_pack_name,
            conformance_pack_input_parameters=conformance_pack_input_parameters,
            delivery_s3_bucket=delivery_s3_bucket,
            delivery_s3_key_prefix=delivery_s3_key_prefix,
            template_body=template_body,
            template_s3_uri=template_s3_uri,
            template_ssm_document_details=template_ssm_document_details,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7403d4346a8cf57174116d6f88a4f63ca05740a7985a84232a53a10b8c76626b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e6563d8daaed12475c806618fef63d370ca145285fb0811fb3eb18a8ae205322)
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
    @jsii.member(jsii_name="conformancePackName")
    def conformance_pack_name(self) -> builtins.str:
        '''Name of the conformance pack you want to create.'''
        return typing.cast(builtins.str, jsii.get(self, "conformancePackName"))

    @conformance_pack_name.setter
    def conformance_pack_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__017266c6d2336c47dd9ced678b7f1432f1d8c14f7d6c1fa5d4e1b853ea226215)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conformancePackName", value)

    @builtins.property
    @jsii.member(jsii_name="conformancePackInputParameters")
    def conformance_pack_input_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConformancePack.ConformancePackInputParameterProperty"]]]]:
        '''A list of ConformancePackInputParameter objects.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConformancePack.ConformancePackInputParameterProperty"]]]], jsii.get(self, "conformancePackInputParameters"))

    @conformance_pack_input_parameters.setter
    def conformance_pack_input_parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConformancePack.ConformancePackInputParameterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66a3c1376d21fbc61cfccda9673dabefb2864004881e13f61c2450d58f726d02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conformancePackInputParameters", value)

    @builtins.property
    @jsii.member(jsii_name="deliveryS3Bucket")
    def delivery_s3_bucket(self) -> typing.Optional[builtins.str]:
        '''The name of the Amazon S3 bucket where AWS Config stores conformance pack templates.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryS3Bucket"))

    @delivery_s3_bucket.setter
    def delivery_s3_bucket(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e9ac9dd0b9bfb5622779dff282ea562c91d27ddf6529b24e403f4405f47b8ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryS3Bucket", value)

    @builtins.property
    @jsii.member(jsii_name="deliveryS3KeyPrefix")
    def delivery_s3_key_prefix(self) -> typing.Optional[builtins.str]:
        '''The prefix for the Amazon S3 bucket.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryS3KeyPrefix"))

    @delivery_s3_key_prefix.setter
    def delivery_s3_key_prefix(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efa81031141bc30ac68f2881e9910f55d05494d80263ec0832f9c3b4cfa72355)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryS3KeyPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="templateBody")
    def template_body(self) -> typing.Optional[builtins.str]:
        '''A string containing full conformance pack template body.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateBody"))

    @template_body.setter
    def template_body(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e35eeba4feaded039ed05fa15d28eda7714d806f9cc117a1a4e2a9b4ee39433)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateBody", value)

    @builtins.property
    @jsii.member(jsii_name="templateS3Uri")
    def template_s3_uri(self) -> typing.Optional[builtins.str]:
        '''Location of file containing the template body (s3://bucketname/prefix).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateS3Uri"))

    @template_s3_uri.setter
    def template_s3_uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b029ab96d5271df83bfd4de01aeaa0b8d0647c023edcc97787666ca457aa18a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateS3Uri", value)

    @builtins.property
    @jsii.member(jsii_name="templateSsmDocumentDetails")
    def template_ssm_document_details(self) -> typing.Any:
        '''An object that contains the name or Amazon Resource Name (ARN) of the AWS Systems Manager document (SSM document) and the version of the SSM document that is used to create a conformance pack.'''
        return typing.cast(typing.Any, jsii.get(self, "templateSsmDocumentDetails"))

    @template_ssm_document_details.setter
    def template_ssm_document_details(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6f6517778467c160ab2997b6792fb457789ecbb58da9204e3c4a9e8d1b789ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateSsmDocumentDetails", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_config.CfnConformancePack.ConformancePackInputParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "parameter_name": "parameterName",
            "parameter_value": "parameterValue",
        },
    )
    class ConformancePackInputParameterProperty:
        def __init__(
            self,
            *,
            parameter_name: builtins.str,
            parameter_value: builtins.str,
        ) -> None:
            '''Input parameters in the form of key-value pairs for the conformance pack, both of which you define.

            Keys can have a maximum character length of 255 characters, and values can have a maximum length of 4096 characters.

            :param parameter_name: One part of a key-value pair.
            :param parameter_value: Another part of the key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-conformancepack-conformancepackinputparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_config as config
                
                conformance_pack_input_parameter_property = config.CfnConformancePack.ConformancePackInputParameterProperty(
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0051d9ed94eb42b0d8f41b517dbab424e6b016ccd95fda52fae7900e6c773833)
                check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
                check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "parameter_name": parameter_name,
                "parameter_value": parameter_value,
            }

        @builtins.property
        def parameter_name(self) -> builtins.str:
            '''One part of a key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-conformancepack-conformancepackinputparameter.html#cfn-config-conformancepack-conformancepackinputparameter-parametername
            '''
            result = self._values.get("parameter_name")
            assert result is not None, "Required property 'parameter_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameter_value(self) -> builtins.str:
            '''Another part of the key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-conformancepack-conformancepackinputparameter.html#cfn-config-conformancepack-conformancepackinputparameter-parametervalue
            '''
            result = self._values.get("parameter_value")
            assert result is not None, "Required property 'parameter_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConformancePackInputParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_config.CfnConformancePack.TemplateSSMDocumentDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "document_name": "documentName",
            "document_version": "documentVersion",
        },
    )
    class TemplateSSMDocumentDetailsProperty:
        def __init__(
            self,
            *,
            document_name: typing.Optional[builtins.str] = None,
            document_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''This API allows you to create a conformance pack template with an AWS Systems Manager document (SSM document).

            To deploy a conformance pack using an SSM document, first create an SSM document with conformance pack content, and then provide the ``DocumentName`` in the `PutConformancePack API <https://docs.aws.amazon.com/config/latest/APIReference/API_PutConformancePack.html>`_ . You can also provide the ``DocumentVersion`` .

            The ``TemplateSSMDocumentDetails`` object contains the name of the SSM document and the version of the SSM document.

            :param document_name: The name or Amazon Resource Name (ARN) of the SSM document to use to create a conformance pack. If you use the document name, AWS Config checks only your account and AWS Region for the SSM document.
            :param document_version: The version of the SSM document to use to create a conformance pack. By default, AWS Config uses the latest version. .. epigraph:: This field is optional.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-conformancepack-templatessmdocumentdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_config as config
                
                template_sSMDocument_details_property = config.CfnConformancePack.TemplateSSMDocumentDetailsProperty(
                    document_name="documentName",
                    document_version="documentVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__10d0cf9a7e5ad0f39e4c2325532b8a4ad5ccd7cd37c16ad8dbbdb7c948035106)
                check_type(argname="argument document_name", value=document_name, expected_type=type_hints["document_name"])
                check_type(argname="argument document_version", value=document_version, expected_type=type_hints["document_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if document_name is not None:
                self._values["document_name"] = document_name
            if document_version is not None:
                self._values["document_version"] = document_version

        @builtins.property
        def document_name(self) -> typing.Optional[builtins.str]:
            '''The name or Amazon Resource Name (ARN) of the SSM document to use to create a conformance pack.

            If you use the document name, AWS Config checks only your account and AWS Region for the SSM document.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-conformancepack-templatessmdocumentdetails.html#cfn-config-conformancepack-templatessmdocumentdetails-documentname
            '''
            result = self._values.get("document_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def document_version(self) -> typing.Optional[builtins.str]:
            '''The version of the SSM document to use to create a conformance pack.

            By default, AWS Config uses the latest version.
            .. epigraph::

               This field is optional.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-conformancepack-templatessmdocumentdetails.html#cfn-config-conformancepack-templatessmdocumentdetails-documentversion
            '''
            result = self._values.get("document_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TemplateSSMDocumentDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_config.CfnConformancePackProps",
    jsii_struct_bases=[],
    name_mapping={
        "conformance_pack_name": "conformancePackName",
        "conformance_pack_input_parameters": "conformancePackInputParameters",
        "delivery_s3_bucket": "deliveryS3Bucket",
        "delivery_s3_key_prefix": "deliveryS3KeyPrefix",
        "template_body": "templateBody",
        "template_s3_uri": "templateS3Uri",
        "template_ssm_document_details": "templateSsmDocumentDetails",
    },
)
class CfnConformancePackProps:
    def __init__(
        self,
        *,
        conformance_pack_name: builtins.str,
        conformance_pack_input_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConformancePack.ConformancePackInputParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        delivery_s3_bucket: typing.Optional[builtins.str] = None,
        delivery_s3_key_prefix: typing.Optional[builtins.str] = None,
        template_body: typing.Optional[builtins.str] = None,
        template_s3_uri: typing.Optional[builtins.str] = None,
        template_ssm_document_details: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnConformancePack``.

        :param conformance_pack_name: Name of the conformance pack you want to create.
        :param conformance_pack_input_parameters: A list of ConformancePackInputParameter objects.
        :param delivery_s3_bucket: The name of the Amazon S3 bucket where AWS Config stores conformance pack templates.
        :param delivery_s3_key_prefix: The prefix for the Amazon S3 bucket.
        :param template_body: A string containing full conformance pack template body. Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. .. epigraph:: You can only use a YAML template with two resource types: config rule ( ``AWS::Config::ConfigRule`` ) and a remediation action ( ``AWS::Config::RemediationConfiguration`` ).
        :param template_s3_uri: Location of file containing the template body (s3://bucketname/prefix). The uri must point to the conformance pack template (max size: 300 KB) that is located in an Amazon S3 bucket. .. epigraph:: You must have access to read Amazon S3 bucket.
        :param template_ssm_document_details: An object that contains the name or Amazon Resource Name (ARN) of the AWS Systems Manager document (SSM document) and the version of the SSM document that is used to create a conformance pack.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_config as config
            
            # template_ssm_document_details: Any
            
            cfn_conformance_pack_props = config.CfnConformancePackProps(
                conformance_pack_name="conformancePackName",
            
                # the properties below are optional
                conformance_pack_input_parameters=[config.CfnConformancePack.ConformancePackInputParameterProperty(
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )],
                delivery_s3_bucket="deliveryS3Bucket",
                delivery_s3_key_prefix="deliveryS3KeyPrefix",
                template_body="templateBody",
                template_s3_uri="templateS3Uri",
                template_ssm_document_details=template_ssm_document_details
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb7114b56400f450b835ab5d3aed18b5a4e6466e2dad2710b6844c6e70ef670e)
            check_type(argname="argument conformance_pack_name", value=conformance_pack_name, expected_type=type_hints["conformance_pack_name"])
            check_type(argname="argument conformance_pack_input_parameters", value=conformance_pack_input_parameters, expected_type=type_hints["conformance_pack_input_parameters"])
            check_type(argname="argument delivery_s3_bucket", value=delivery_s3_bucket, expected_type=type_hints["delivery_s3_bucket"])
            check_type(argname="argument delivery_s3_key_prefix", value=delivery_s3_key_prefix, expected_type=type_hints["delivery_s3_key_prefix"])
            check_type(argname="argument template_body", value=template_body, expected_type=type_hints["template_body"])
            check_type(argname="argument template_s3_uri", value=template_s3_uri, expected_type=type_hints["template_s3_uri"])
            check_type(argname="argument template_ssm_document_details", value=template_ssm_document_details, expected_type=type_hints["template_ssm_document_details"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "conformance_pack_name": conformance_pack_name,
        }
        if conformance_pack_input_parameters is not None:
            self._values["conformance_pack_input_parameters"] = conformance_pack_input_parameters
        if delivery_s3_bucket is not None:
            self._values["delivery_s3_bucket"] = delivery_s3_bucket
        if delivery_s3_key_prefix is not None:
            self._values["delivery_s3_key_prefix"] = delivery_s3_key_prefix
        if template_body is not None:
            self._values["template_body"] = template_body
        if template_s3_uri is not None:
            self._values["template_s3_uri"] = template_s3_uri
        if template_ssm_document_details is not None:
            self._values["template_ssm_document_details"] = template_ssm_document_details

    @builtins.property
    def conformance_pack_name(self) -> builtins.str:
        '''Name of the conformance pack you want to create.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-conformancepackname
        '''
        result = self._values.get("conformance_pack_name")
        assert result is not None, "Required property 'conformance_pack_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def conformance_pack_input_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConformancePack.ConformancePackInputParameterProperty]]]]:
        '''A list of ConformancePackInputParameter objects.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-conformancepackinputparameters
        '''
        result = self._values.get("conformance_pack_input_parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConformancePack.ConformancePackInputParameterProperty]]]], result)

    @builtins.property
    def delivery_s3_bucket(self) -> typing.Optional[builtins.str]:
        '''The name of the Amazon S3 bucket where AWS Config stores conformance pack templates.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-deliverys3bucket
        '''
        result = self._values.get("delivery_s3_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delivery_s3_key_prefix(self) -> typing.Optional[builtins.str]:
        '''The prefix for the Amazon S3 bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-deliverys3keyprefix
        '''
        result = self._values.get("delivery_s3_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_body(self) -> typing.Optional[builtins.str]:
        '''A string containing full conformance pack template body.

        Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.
        .. epigraph::

           You can only use a YAML template with two resource types: config rule ( ``AWS::Config::ConfigRule`` ) and a remediation action ( ``AWS::Config::RemediationConfiguration`` ).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-templatebody
        '''
        result = self._values.get("template_body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_s3_uri(self) -> typing.Optional[builtins.str]:
        '''Location of file containing the template body (s3://bucketname/prefix).

        The uri must point to the conformance pack template (max size: 300 KB) that is located in an Amazon S3 bucket.
        .. epigraph::

           You must have access to read Amazon S3 bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-templates3uri
        '''
        result = self._values.get("template_s3_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_ssm_document_details(self) -> typing.Any:
        '''An object that contains the name or Amazon Resource Name (ARN) of the AWS Systems Manager document (SSM document) and the version of the SSM document that is used to create a conformance pack.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html#cfn-config-conformancepack-templatessmdocumentdetails
        '''
        result = self._values.get("template_ssm_document_details")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConformancePackProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDeliveryChannel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_config.CfnDeliveryChannel",
):
    '''Specifies a delivery channel object to deliver configuration information to an Amazon S3 bucket and Amazon SNS topic.

    Before you can create a delivery channel, you must create a configuration recorder. You can use this action to change the Amazon S3 bucket or an Amazon SNS topic of the existing delivery channel. To change the Amazon S3 bucket or an Amazon SNS topic, call this action and specify the changed values for the S3 bucket and the SNS topic. If you specify a different value for either the S3 bucket or the SNS topic, this action will keep the existing value for the parameter that is not changed.
    .. epigraph::

       In the China (Beijing) Region, when you call this action, the Amazon S3 bucket must also be in the China (Beijing) Region. In all the other regions, AWS Config supports cross-region and cross-account delivery channels.

    You can have only one delivery channel per region per AWS account, and the delivery channel is required to use AWS Config .
    .. epigraph::

       AWS Config does not support the delivery channel to an Amazon S3 bucket bucket where object lock is enabled. For more information, see `How S3 Object Lock works <https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock-overview.html>`_ .

    When you create the delivery channel, you can specify; how often AWS Config delivers configuration snapshots to your Amazon S3 bucket (for example, 24 hours), the S3 bucket to which AWS Config sends configuration snapshots and configuration history files, and the Amazon SNS topic to which AWS Config sends notifications about configuration changes, such as updated resources, AWS Config rule evaluations, and when AWS Config delivers the configuration snapshot to your S3 bucket. For more information, see `Deliver Configuration Items <https://docs.aws.amazon.com/config/latest/developerguide/how-does-config-work.html#delivery-channel>`_ in the AWS Config Developer Guide.
    .. epigraph::

       To enable AWS Config , you must create a configuration recorder and a delivery channel. If you want to create the resources separately, you must create a configuration recorder before you can create a delivery channel. AWS Config uses the configuration recorder to capture configuration changes to your resources. For more information, see `AWS::Config::ConfigurationRecorder <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html>`_ .

    For more information, see `Managing the Delivery Channel <https://docs.aws.amazon.com/config/latest/developerguide/manage-delivery-channel.html>`_ in the AWS Config Developer Guide.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html
    :cloudformationResource: AWS::Config::DeliveryChannel
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_config as config
        
        cfn_delivery_channel = config.CfnDeliveryChannel(self, "MyCfnDeliveryChannel",
            s3_bucket_name="s3BucketName",
        
            # the properties below are optional
            config_snapshot_delivery_properties=config.CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty(
                delivery_frequency="deliveryFrequency"
            ),
            name="name",
            s3_key_prefix="s3KeyPrefix",
            s3_kms_key_arn="s3KmsKeyArn",
            sns_topic_arn="snsTopicArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        s3_bucket_name: builtins.str,
        config_snapshot_delivery_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        s3_key_prefix: typing.Optional[builtins.str] = None,
        s3_kms_key_arn: typing.Optional[builtins.str] = None,
        sns_topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param s3_bucket_name: The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and configuration history files. If you specify a bucket that belongs to another AWS account , that bucket must have policies that grant access permissions to AWS Config . For more information, see `Permissions for the Amazon S3 Bucket <https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-policy.html>`_ in the *AWS Config Developer Guide* .
        :param config_snapshot_delivery_properties: The options for how often AWS Config delivers configuration snapshots to the Amazon S3 bucket.
        :param name: A name for the delivery channel. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the delivery channel name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . Updates are not supported. To change the name, you must run two separate updates. In the first update, delete this resource, and then recreate it with a new name in the second update.
        :param s3_key_prefix: The prefix for the specified Amazon S3 bucket.
        :param s3_kms_key_arn: The Amazon Resource Name (ARN) of the AWS Key Management Service ( AWS KMS ) AWS KMS key (KMS key) used to encrypt objects delivered by AWS Config . Must belong to the same Region as the destination S3 bucket.
        :param sns_topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to which AWS Config sends notifications about configuration changes. If you choose a topic from another account, the topic must have policies that grant access permissions to AWS Config . For more information, see `Permissions for the Amazon SNS Topic <https://docs.aws.amazon.com/config/latest/developerguide/sns-topic-policy.html>`_ in the *AWS Config Developer Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73c6e198efe26973129b68257eec368d6f11d6482310ee44da30ea815b09ce44)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDeliveryChannelProps(
            s3_bucket_name=s3_bucket_name,
            config_snapshot_delivery_properties=config_snapshot_delivery_properties,
            name=name,
            s3_key_prefix=s3_key_prefix,
            s3_kms_key_arn=s3_kms_key_arn,
            sns_topic_arn=sns_topic_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93fe2fc089232415921cfb7f1987ad394874d5cec29ce9cd68d50744a0667515)
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
            type_hints = typing.get_type_hints(_typecheckingstub__86778f392aecf273d1b4f4f57d53afa9b547f8fc6e6e320ef041d3b56e79f1d3)
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
    @jsii.member(jsii_name="s3BucketName")
    def s3_bucket_name(self) -> builtins.str:
        '''The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and configuration history files.'''
        return typing.cast(builtins.str, jsii.get(self, "s3BucketName"))

    @s3_bucket_name.setter
    def s3_bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12454c1d1b821f4416cba3de981294f5dbd46e9d821e3996f737b570da3a9428)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3BucketName", value)

    @builtins.property
    @jsii.member(jsii_name="configSnapshotDeliveryProperties")
    def config_snapshot_delivery_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty"]]:
        '''The options for how often AWS Config delivers configuration snapshots to the Amazon S3 bucket.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty"]], jsii.get(self, "configSnapshotDeliveryProperties"))

    @config_snapshot_delivery_properties.setter
    def config_snapshot_delivery_properties(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29732799858d5a51a49b644a23b9487d8a731f17a76776d46c2a417f67da3159)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configSnapshotDeliveryProperties", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''A name for the delivery channel.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1c1e8db307d687d985abe819d5a1478a0354508356913373a8ad756e39975e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="s3KeyPrefix")
    def s3_key_prefix(self) -> typing.Optional[builtins.str]:
        '''The prefix for the specified Amazon S3 bucket.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3KeyPrefix"))

    @s3_key_prefix.setter
    def s3_key_prefix(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e52266b167ad8133727ace537e117b4211b9b1601117d67caf7806c3954ef7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3KeyPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="s3KmsKeyArn")
    def s3_kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS Key Management Service ( AWS KMS ) AWS KMS key (KMS key) used to encrypt objects delivered by AWS Config .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3KmsKeyArn"))

    @s3_kms_key_arn.setter
    def s3_kms_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__004463c97f710f28b3097f13305e10414949a4af5d0c981486867fd7166ee1f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3KmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="snsTopicArn")
    def sns_topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic to which AWS Config sends notifications about configuration changes.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snsTopicArn"))

    @sns_topic_arn.setter
    def sns_topic_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ec3498b9deb557429daadb315089fa9733a0d0a1516f9379188370be46f7f5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snsTopicArn", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_config.CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"delivery_frequency": "deliveryFrequency"},
    )
    class ConfigSnapshotDeliveryPropertiesProperty:
        def __init__(
            self,
            *,
            delivery_frequency: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides options for how often AWS Config delivers configuration snapshots to the Amazon S3 bucket in your delivery channel.

            .. epigraph::

               If you want to create a rule that triggers evaluations for your resources when AWS Config delivers the configuration snapshot, see the following:

            The frequency for a rule that triggers evaluations for your resources when AWS Config delivers the configuration snapshot is set by one of two values, depending on which is less frequent:

            - The value for the ``deliveryFrequency`` parameter within the delivery channel configuration, which sets how often AWS Config delivers configuration snapshots. This value also sets how often AWS Config invokes evaluations for AWS Config rules.
            - The value for the ``MaximumExecutionFrequency`` parameter, which sets the maximum frequency with which AWS Config invokes evaluations for the rule. For more information, see `ConfigRule <https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigRule.html>`_ .

            If the ``deliveryFrequency`` value is less frequent than the ``MaximumExecutionFrequency`` value for a rule, AWS Config invokes the rule only as often as the ``deliveryFrequency`` value.

            - For example, you want your rule to run evaluations when AWS Config delivers the configuration snapshot.
            - You specify the ``MaximumExecutionFrequency`` value for ``Six_Hours`` .
            - You then specify the delivery channel ``deliveryFrequency`` value for ``TwentyFour_Hours`` .
            - Because the value for ``deliveryFrequency`` is less frequent than ``MaximumExecutionFrequency`` , AWS Config invokes evaluations for the rule every 24 hours.

            You should set the ``MaximumExecutionFrequency`` value to be at least as frequent as the ``deliveryFrequency`` value. You can view the ``deliveryFrequency`` value by using the ``DescribeDeliveryChannnels`` action.

            To update the ``deliveryFrequency`` with which AWS Config delivers your configuration snapshots, use the ``PutDeliveryChannel`` action.

            :param delivery_frequency: The frequency with which AWS Config delivers configuration snapshots.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-deliverychannel-configsnapshotdeliveryproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_config as config
                
                config_snapshot_delivery_properties_property = config.CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty(
                    delivery_frequency="deliveryFrequency"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__824c2ae974da56cf59c6872d5c3038e4fbf831ced2eb0f0d54679ffd8d7f35d0)
                check_type(argname="argument delivery_frequency", value=delivery_frequency, expected_type=type_hints["delivery_frequency"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if delivery_frequency is not None:
                self._values["delivery_frequency"] = delivery_frequency

        @builtins.property
        def delivery_frequency(self) -> typing.Optional[builtins.str]:
            '''The frequency with which AWS Config delivers configuration snapshots.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-deliverychannel-configsnapshotdeliveryproperties.html#cfn-config-deliverychannel-configsnapshotdeliveryproperties-deliveryfrequency
            '''
            result = self._values.get("delivery_frequency")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigSnapshotDeliveryPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_config.CfnDeliveryChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "s3_bucket_name": "s3BucketName",
        "config_snapshot_delivery_properties": "configSnapshotDeliveryProperties",
        "name": "name",
        "s3_key_prefix": "s3KeyPrefix",
        "s3_kms_key_arn": "s3KmsKeyArn",
        "sns_topic_arn": "snsTopicArn",
    },
)
class CfnDeliveryChannelProps:
    def __init__(
        self,
        *,
        s3_bucket_name: builtins.str,
        config_snapshot_delivery_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        s3_key_prefix: typing.Optional[builtins.str] = None,
        s3_kms_key_arn: typing.Optional[builtins.str] = None,
        sns_topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnDeliveryChannel``.

        :param s3_bucket_name: The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and configuration history files. If you specify a bucket that belongs to another AWS account , that bucket must have policies that grant access permissions to AWS Config . For more information, see `Permissions for the Amazon S3 Bucket <https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-policy.html>`_ in the *AWS Config Developer Guide* .
        :param config_snapshot_delivery_properties: The options for how often AWS Config delivers configuration snapshots to the Amazon S3 bucket.
        :param name: A name for the delivery channel. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the delivery channel name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . Updates are not supported. To change the name, you must run two separate updates. In the first update, delete this resource, and then recreate it with a new name in the second update.
        :param s3_key_prefix: The prefix for the specified Amazon S3 bucket.
        :param s3_kms_key_arn: The Amazon Resource Name (ARN) of the AWS Key Management Service ( AWS KMS ) AWS KMS key (KMS key) used to encrypt objects delivered by AWS Config . Must belong to the same Region as the destination S3 bucket.
        :param sns_topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to which AWS Config sends notifications about configuration changes. If you choose a topic from another account, the topic must have policies that grant access permissions to AWS Config . For more information, see `Permissions for the Amazon SNS Topic <https://docs.aws.amazon.com/config/latest/developerguide/sns-topic-policy.html>`_ in the *AWS Config Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_config as config
            
            cfn_delivery_channel_props = config.CfnDeliveryChannelProps(
                s3_bucket_name="s3BucketName",
            
                # the properties below are optional
                config_snapshot_delivery_properties=config.CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty(
                    delivery_frequency="deliveryFrequency"
                ),
                name="name",
                s3_key_prefix="s3KeyPrefix",
                s3_kms_key_arn="s3KmsKeyArn",
                sns_topic_arn="snsTopicArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0cdaf5740787bc293a2cfbbc714aaffedb113a45f3a519fd5ee5defd54f724f)
            check_type(argname="argument s3_bucket_name", value=s3_bucket_name, expected_type=type_hints["s3_bucket_name"])
            check_type(argname="argument config_snapshot_delivery_properties", value=config_snapshot_delivery_properties, expected_type=type_hints["config_snapshot_delivery_properties"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument s3_key_prefix", value=s3_key_prefix, expected_type=type_hints["s3_key_prefix"])
            check_type(argname="argument s3_kms_key_arn", value=s3_kms_key_arn, expected_type=type_hints["s3_kms_key_arn"])
            check_type(argname="argument sns_topic_arn", value=sns_topic_arn, expected_type=type_hints["sns_topic_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "s3_bucket_name": s3_bucket_name,
        }
        if config_snapshot_delivery_properties is not None:
            self._values["config_snapshot_delivery_properties"] = config_snapshot_delivery_properties
        if name is not None:
            self._values["name"] = name
        if s3_key_prefix is not None:
            self._values["s3_key_prefix"] = s3_key_prefix
        if s3_kms_key_arn is not None:
            self._values["s3_kms_key_arn"] = s3_kms_key_arn
        if sns_topic_arn is not None:
            self._values["sns_topic_arn"] = sns_topic_arn

    @builtins.property
    def s3_bucket_name(self) -> builtins.str:
        '''The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and configuration history files.

        If you specify a bucket that belongs to another AWS account , that bucket must have policies that grant access permissions to AWS Config . For more information, see `Permissions for the Amazon S3 Bucket <https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-policy.html>`_ in the *AWS Config Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-s3bucketname
        '''
        result = self._values.get("s3_bucket_name")
        assert result is not None, "Required property 's3_bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def config_snapshot_delivery_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty]]:
        '''The options for how often AWS Config delivers configuration snapshots to the Amazon S3 bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-configsnapshotdeliveryproperties
        '''
        result = self._values.get("config_snapshot_delivery_properties")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A name for the delivery channel.

        If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the delivery channel name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ .

        Updates are not supported. To change the name, you must run two separate updates. In the first update, delete this resource, and then recreate it with a new name in the second update.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_key_prefix(self) -> typing.Optional[builtins.str]:
        '''The prefix for the specified Amazon S3 bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-s3keyprefix
        '''
        result = self._values.get("s3_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS Key Management Service ( AWS KMS ) AWS KMS key (KMS key) used to encrypt objects delivered by AWS Config .

        Must belong to the same Region as the destination S3 bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-s3kmskeyarn
        '''
        result = self._values.get("s3_kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sns_topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic to which AWS Config sends notifications about configuration changes.

        If you choose a topic from another account, the topic must have policies that grant access permissions to AWS Config . For more information, see `Permissions for the Amazon SNS Topic <https://docs.aws.amazon.com/config/latest/developerguide/sns-topic-policy.html>`_ in the *AWS Config Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html#cfn-config-deliverychannel-snstopicarn
        '''
        result = self._values.get("sns_topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeliveryChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnOrganizationConfigRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_config.CfnOrganizationConfigRule",
):
    '''Adds or updates an AWS Config rule for your entire organization to evaluate if your AWS resources comply with your desired configurations.

    For information on how many organization AWS Config rules you can have per account, see `*Service Limits* <https://docs.aws.amazon.com/config/latest/developerguide/configlimits.html>`_ in the *AWS Config Developer Guide* .

    Only a management account and a delegated administrator can create or update an organization AWS Config rule. When calling the ``OrganizationConfigRule`` resource with a delegated administrator, you must ensure AWS Organizations ``ListDelegatedAdministrator`` permissions are added. An organization can have up to 3 delegated administrators.

    The ``OrganizationConfigRule`` resource enables organization service access through the ``EnableAWSServiceAccess`` action and creates a service-linked role ``AWSServiceRoleForConfigMultiAccountSetup`` in the management or delegated administrator account of your organization. The service-linked role is created only when the role does not exist in the caller account. AWS Config verifies the existence of role with ``GetRole`` action.

    To use the ``OrganizationConfigRule`` resource with delegated administrator, register a delegated administrator by calling AWS Organization ``register-delegated-administrator`` for ``config-multiaccountsetup.amazonaws.com`` .

    There are two types of rules: *AWS Config Managed Rules* and *AWS Config Custom Rules* . You can use ``PutOrganizationConfigRule`` to create both AWS Config Managed Rules and AWS Config Custom Rules.

    AWS Config Managed Rules are predefined, customizable rules created by AWS Config . For a list of managed rules, see `List of AWS Config Managed Rules <https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html>`_ . If you are adding an AWS Config managed rule, you must specify the rule's identifier for the ``RuleIdentifier`` key.

    AWS Config Custom Rules are rules that you create from scratch. There are two ways to create AWS Config custom rules: with Lambda functions ( `AWS Lambda Developer Guide <https://docs.aws.amazon.com/config/latest/developerguide/gettingstarted-concepts.html#gettingstarted-concepts-function>`_ ) and with Guard ( `Guard GitHub Repository <https://docs.aws.amazon.com/https://github.com/aws-cloudformation/cloudformation-guard>`_ ), a policy-as-code language. AWS Config custom rules created with AWS Lambda are called *AWS Config Custom Lambda Rules* and AWS Config custom rules created with Guard are called *AWS Config Custom Policy Rules* .

    If you are adding a new AWS Config Custom Lambda rule, you first need to create an AWS Lambda function in the management account or a delegated administrator that the rule invokes to evaluate your resources. You also need to create an IAM role in the managed account that can be assumed by the Lambda function. When you use ``PutOrganizationConfigRule`` to add a Custom Lambda rule to AWS Config , you must specify the Amazon Resource Name (ARN) that AWS Lambda assigns to the function.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html
    :cloudformationResource: AWS::Config::OrganizationConfigRule
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_config as config
        
        cfn_organization_config_rule = config.CfnOrganizationConfigRule(self, "MyCfnOrganizationConfigRule",
            organization_config_rule_name="organizationConfigRuleName",
        
            # the properties below are optional
            excluded_accounts=["excludedAccounts"],
            organization_custom_policy_rule_metadata=config.CfnOrganizationConfigRule.OrganizationCustomPolicyRuleMetadataProperty(
                policy_text="policyText",
                runtime="runtime",
        
                # the properties below are optional
                debug_log_delivery_accounts=["debugLogDeliveryAccounts"],
                description="description",
                input_parameters="inputParameters",
                maximum_execution_frequency="maximumExecutionFrequency",
                organization_config_rule_trigger_types=["organizationConfigRuleTriggerTypes"],
                resource_id_scope="resourceIdScope",
                resource_types_scope=["resourceTypesScope"],
                tag_key_scope="tagKeyScope",
                tag_value_scope="tagValueScope"
            ),
            organization_custom_rule_metadata=config.CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty(
                lambda_function_arn="lambdaFunctionArn",
                organization_config_rule_trigger_types=["organizationConfigRuleTriggerTypes"],
        
                # the properties below are optional
                description="description",
                input_parameters="inputParameters",
                maximum_execution_frequency="maximumExecutionFrequency",
                resource_id_scope="resourceIdScope",
                resource_types_scope=["resourceTypesScope"],
                tag_key_scope="tagKeyScope",
                tag_value_scope="tagValueScope"
            ),
            organization_managed_rule_metadata=config.CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty(
                rule_identifier="ruleIdentifier",
        
                # the properties below are optional
                description="description",
                input_parameters="inputParameters",
                maximum_execution_frequency="maximumExecutionFrequency",
                resource_id_scope="resourceIdScope",
                resource_types_scope=["resourceTypesScope"],
                tag_key_scope="tagKeyScope",
                tag_value_scope="tagValueScope"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        organization_config_rule_name: builtins.str,
        excluded_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
        organization_custom_policy_rule_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOrganizationConfigRule.OrganizationCustomPolicyRuleMetadataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        organization_custom_rule_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        organization_managed_rule_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param organization_config_rule_name: The name that you assign to organization AWS Config rule.
        :param excluded_accounts: A comma-separated list of accounts excluded from organization AWS Config rule.
        :param organization_custom_policy_rule_metadata: An object that specifies metadata for your organization's AWS Config Custom Policy rule. The metadata includes the runtime system in use, which accounts have debug logging enabled, and other custom rule metadata, such as resource type, resource ID of AWS resource, and organization trigger types that initiate AWS Config to evaluate AWS resources against a rule.
        :param organization_custom_rule_metadata: An ``OrganizationCustomRuleMetadata`` object.
        :param organization_managed_rule_metadata: An ``OrganizationManagedRuleMetadata`` object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbb132a46c30059a4907d7496d2b696999321fd7c5b82f7812c5a4d9bf7ffdef)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnOrganizationConfigRuleProps(
            organization_config_rule_name=organization_config_rule_name,
            excluded_accounts=excluded_accounts,
            organization_custom_policy_rule_metadata=organization_custom_policy_rule_metadata,
            organization_custom_rule_metadata=organization_custom_rule_metadata,
            organization_managed_rule_metadata=organization_managed_rule_metadata,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e581ed53a72e9f3241819d7b60aee8c45b6d8882e96a3754518305e3004fbe5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6fa3a06ce143fa26917309b4aad611deb91282cec0652e424ae8e59eab1c0f4b)
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
    @jsii.member(jsii_name="organizationConfigRuleName")
    def organization_config_rule_name(self) -> builtins.str:
        '''The name that you assign to organization AWS Config rule.'''
        return typing.cast(builtins.str, jsii.get(self, "organizationConfigRuleName"))

    @organization_config_rule_name.setter
    def organization_config_rule_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22e78630a330158f7539628357991f18a40deeba1fd6717ad961c7b74d3e220a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationConfigRuleName", value)

    @builtins.property
    @jsii.member(jsii_name="excludedAccounts")
    def excluded_accounts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A comma-separated list of accounts excluded from organization AWS Config rule.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludedAccounts"))

    @excluded_accounts.setter
    def excluded_accounts(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e24ca951119404bbb132d0e9fc6bac7e6de317bfd3583fa6527330cb5d68d99a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludedAccounts", value)

    @builtins.property
    @jsii.member(jsii_name="organizationCustomPolicyRuleMetadata")
    def organization_custom_policy_rule_metadata(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOrganizationConfigRule.OrganizationCustomPolicyRuleMetadataProperty"]]:
        '''An object that specifies metadata for your organization's AWS Config Custom Policy rule.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOrganizationConfigRule.OrganizationCustomPolicyRuleMetadataProperty"]], jsii.get(self, "organizationCustomPolicyRuleMetadata"))

    @organization_custom_policy_rule_metadata.setter
    def organization_custom_policy_rule_metadata(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOrganizationConfigRule.OrganizationCustomPolicyRuleMetadataProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d092f1b41cbf019a6c2f797b420e8cb6cce29c52a1fb671c69086ff9b8083246)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationCustomPolicyRuleMetadata", value)

    @builtins.property
    @jsii.member(jsii_name="organizationCustomRuleMetadata")
    def organization_custom_rule_metadata(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty"]]:
        '''An ``OrganizationCustomRuleMetadata`` object.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty"]], jsii.get(self, "organizationCustomRuleMetadata"))

    @organization_custom_rule_metadata.setter
    def organization_custom_rule_metadata(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c45ab894736dadec9d2a359d9fb78b8cce28027988ec287fb21ff6deaac97ea7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationCustomRuleMetadata", value)

    @builtins.property
    @jsii.member(jsii_name="organizationManagedRuleMetadata")
    def organization_managed_rule_metadata(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty"]]:
        '''An ``OrganizationManagedRuleMetadata`` object.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty"]], jsii.get(self, "organizationManagedRuleMetadata"))

    @organization_managed_rule_metadata.setter
    def organization_managed_rule_metadata(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afcd0c2707f5eb2640b1df26b94e2a0dc017a9171de66ccba46831ec339d624b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationManagedRuleMetadata", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_config.CfnOrganizationConfigRule.OrganizationCustomPolicyRuleMetadataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "policy_text": "policyText",
            "runtime": "runtime",
            "debug_log_delivery_accounts": "debugLogDeliveryAccounts",
            "description": "description",
            "input_parameters": "inputParameters",
            "maximum_execution_frequency": "maximumExecutionFrequency",
            "organization_config_rule_trigger_types": "organizationConfigRuleTriggerTypes",
            "resource_id_scope": "resourceIdScope",
            "resource_types_scope": "resourceTypesScope",
            "tag_key_scope": "tagKeyScope",
            "tag_value_scope": "tagValueScope",
        },
    )
    class OrganizationCustomPolicyRuleMetadataProperty:
        def __init__(
            self,
            *,
            policy_text: builtins.str,
            runtime: builtins.str,
            debug_log_delivery_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
            description: typing.Optional[builtins.str] = None,
            input_parameters: typing.Optional[builtins.str] = None,
            maximum_execution_frequency: typing.Optional[builtins.str] = None,
            organization_config_rule_trigger_types: typing.Optional[typing.Sequence[builtins.str]] = None,
            resource_id_scope: typing.Optional[builtins.str] = None,
            resource_types_scope: typing.Optional[typing.Sequence[builtins.str]] = None,
            tag_key_scope: typing.Optional[builtins.str] = None,
            tag_value_scope: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that specifies metadata for your organization's AWS Config Custom Policy rule.

            The metadata includes the runtime system in use, which accounts have debug logging enabled, and other custom rule metadata, such as resource type, resource ID of AWS resource, and organization trigger types that initiate AWS Config to evaluate AWS resources against a rule.

            :param policy_text: The policy definition containing the logic for your organization AWS Config Custom Policy rule.
            :param runtime: The runtime system for your organization AWS Config Custom Policy rules. Guard is a policy-as-code language that allows you to write policies that are enforced by AWS Config Custom Policy rules. For more information about Guard, see the `Guard GitHub Repository <https://docs.aws.amazon.com/https://github.com/aws-cloudformation/cloudformation-guard>`_ .
            :param debug_log_delivery_accounts: A list of accounts that you can enable debug logging for your organization AWS Config Custom Policy rule. List is null when debug logging is enabled for all accounts.
            :param description: The description that you provide for your organization AWS Config Custom Policy rule.
            :param input_parameters: A string, in JSON format, that is passed to your organization AWS Config Custom Policy rule.
            :param maximum_execution_frequency: The maximum frequency with which AWS Config runs evaluations for a rule. Your AWS Config Custom Policy rule is triggered when AWS Config delivers the configuration snapshot. For more information, see ``ConfigSnapshotDeliveryProperties`` .
            :param organization_config_rule_trigger_types: The type of notification that initiates AWS Config to run an evaluation for a rule. For AWS Config Custom Policy rules, AWS Config supports change-initiated notification types: - ``ConfigurationItemChangeNotification`` - Initiates an evaluation when AWS Config delivers a configuration item as a result of a resource change. - ``OversizedConfigurationItemChangeNotification`` - Initiates an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS.
            :param resource_id_scope: The ID of the AWS resource that was evaluated.
            :param resource_types_scope: The type of the AWS resource that was evaluated.
            :param tag_key_scope: One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.
            :param tag_value_scope: The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_config as config
                
                organization_custom_policy_rule_metadata_property = config.CfnOrganizationConfigRule.OrganizationCustomPolicyRuleMetadataProperty(
                    policy_text="policyText",
                    runtime="runtime",
                
                    # the properties below are optional
                    debug_log_delivery_accounts=["debugLogDeliveryAccounts"],
                    description="description",
                    input_parameters="inputParameters",
                    maximum_execution_frequency="maximumExecutionFrequency",
                    organization_config_rule_trigger_types=["organizationConfigRuleTriggerTypes"],
                    resource_id_scope="resourceIdScope",
                    resource_types_scope=["resourceTypesScope"],
                    tag_key_scope="tagKeyScope",
                    tag_value_scope="tagValueScope"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__016ff97a5da2c8c200eb9588ecaeb29452dbdd2d720dfa609e6359881809c740)
                check_type(argname="argument policy_text", value=policy_text, expected_type=type_hints["policy_text"])
                check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
                check_type(argname="argument debug_log_delivery_accounts", value=debug_log_delivery_accounts, expected_type=type_hints["debug_log_delivery_accounts"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument input_parameters", value=input_parameters, expected_type=type_hints["input_parameters"])
                check_type(argname="argument maximum_execution_frequency", value=maximum_execution_frequency, expected_type=type_hints["maximum_execution_frequency"])
                check_type(argname="argument organization_config_rule_trigger_types", value=organization_config_rule_trigger_types, expected_type=type_hints["organization_config_rule_trigger_types"])
                check_type(argname="argument resource_id_scope", value=resource_id_scope, expected_type=type_hints["resource_id_scope"])
                check_type(argname="argument resource_types_scope", value=resource_types_scope, expected_type=type_hints["resource_types_scope"])
                check_type(argname="argument tag_key_scope", value=tag_key_scope, expected_type=type_hints["tag_key_scope"])
                check_type(argname="argument tag_value_scope", value=tag_value_scope, expected_type=type_hints["tag_value_scope"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "policy_text": policy_text,
                "runtime": runtime,
            }
            if debug_log_delivery_accounts is not None:
                self._values["debug_log_delivery_accounts"] = debug_log_delivery_accounts
            if description is not None:
                self._values["description"] = description
            if input_parameters is not None:
                self._values["input_parameters"] = input_parameters
            if maximum_execution_frequency is not None:
                self._values["maximum_execution_frequency"] = maximum_execution_frequency
            if organization_config_rule_trigger_types is not None:
                self._values["organization_config_rule_trigger_types"] = organization_config_rule_trigger_types
            if resource_id_scope is not None:
                self._values["resource_id_scope"] = resource_id_scope
            if resource_types_scope is not None:
                self._values["resource_types_scope"] = resource_types_scope
            if tag_key_scope is not None:
                self._values["tag_key_scope"] = tag_key_scope
            if tag_value_scope is not None:
                self._values["tag_value_scope"] = tag_value_scope

        @builtins.property
        def policy_text(self) -> builtins.str:
            '''The policy definition containing the logic for your organization AWS Config Custom Policy rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html#cfn-config-organizationconfigrule-organizationcustompolicyrulemetadata-policytext
            '''
            result = self._values.get("policy_text")
            assert result is not None, "Required property 'policy_text' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def runtime(self) -> builtins.str:
            '''The runtime system for your organization AWS Config Custom Policy rules.

            Guard is a policy-as-code language that allows you to write policies that are enforced by AWS Config Custom Policy rules. For more information about Guard, see the `Guard GitHub Repository <https://docs.aws.amazon.com/https://github.com/aws-cloudformation/cloudformation-guard>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html#cfn-config-organizationconfigrule-organizationcustompolicyrulemetadata-runtime
            '''
            result = self._values.get("runtime")
            assert result is not None, "Required property 'runtime' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def debug_log_delivery_accounts(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of accounts that you can enable debug logging for your organization AWS Config Custom Policy rule.

            List is null when debug logging is enabled for all accounts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html#cfn-config-organizationconfigrule-organizationcustompolicyrulemetadata-debuglogdeliveryaccounts
            '''
            result = self._values.get("debug_log_delivery_accounts")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description that you provide for your organization AWS Config Custom Policy rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html#cfn-config-organizationconfigrule-organizationcustompolicyrulemetadata-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def input_parameters(self) -> typing.Optional[builtins.str]:
            '''A string, in JSON format, that is passed to your organization AWS Config Custom Policy rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html#cfn-config-organizationconfigrule-organizationcustompolicyrulemetadata-inputparameters
            '''
            result = self._values.get("input_parameters")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def maximum_execution_frequency(self) -> typing.Optional[builtins.str]:
            '''The maximum frequency with which AWS Config runs evaluations for a rule.

            Your AWS Config Custom Policy rule is triggered when AWS Config delivers the configuration snapshot. For more information, see ``ConfigSnapshotDeliveryProperties`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html#cfn-config-organizationconfigrule-organizationcustompolicyrulemetadata-maximumexecutionfrequency
            '''
            result = self._values.get("maximum_execution_frequency")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def organization_config_rule_trigger_types(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''The type of notification that initiates AWS Config to run an evaluation for a rule.

            For AWS Config Custom Policy rules, AWS Config supports change-initiated notification types:

            - ``ConfigurationItemChangeNotification`` - Initiates an evaluation when AWS Config delivers a configuration item as a result of a resource change.
            - ``OversizedConfigurationItemChangeNotification`` - Initiates an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html#cfn-config-organizationconfigrule-organizationcustompolicyrulemetadata-organizationconfigruletriggertypes
            '''
            result = self._values.get("organization_config_rule_trigger_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def resource_id_scope(self) -> typing.Optional[builtins.str]:
            '''The ID of the AWS resource that was evaluated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html#cfn-config-organizationconfigrule-organizationcustompolicyrulemetadata-resourceidscope
            '''
            result = self._values.get("resource_id_scope")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_types_scope(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The type of the AWS resource that was evaluated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html#cfn-config-organizationconfigrule-organizationcustompolicyrulemetadata-resourcetypesscope
            '''
            result = self._values.get("resource_types_scope")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def tag_key_scope(self) -> typing.Optional[builtins.str]:
            '''One part of a key-value pair that make up a tag.

            A key is a general label that acts like a category for more specific tag values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html#cfn-config-organizationconfigrule-organizationcustompolicyrulemetadata-tagkeyscope
            '''
            result = self._values.get("tag_key_scope")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tag_value_scope(self) -> typing.Optional[builtins.str]:
            '''The optional part of a key-value pair that make up a tag.

            A value acts as a descriptor within a tag category (key).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustompolicyrulemetadata.html#cfn-config-organizationconfigrule-organizationcustompolicyrulemetadata-tagvaluescope
            '''
            result = self._values.get("tag_value_scope")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OrganizationCustomPolicyRuleMetadataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_config.CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "lambda_function_arn": "lambdaFunctionArn",
            "organization_config_rule_trigger_types": "organizationConfigRuleTriggerTypes",
            "description": "description",
            "input_parameters": "inputParameters",
            "maximum_execution_frequency": "maximumExecutionFrequency",
            "resource_id_scope": "resourceIdScope",
            "resource_types_scope": "resourceTypesScope",
            "tag_key_scope": "tagKeyScope",
            "tag_value_scope": "tagValueScope",
        },
    )
    class OrganizationCustomRuleMetadataProperty:
        def __init__(
            self,
            *,
            lambda_function_arn: builtins.str,
            organization_config_rule_trigger_types: typing.Sequence[builtins.str],
            description: typing.Optional[builtins.str] = None,
            input_parameters: typing.Optional[builtins.str] = None,
            maximum_execution_frequency: typing.Optional[builtins.str] = None,
            resource_id_scope: typing.Optional[builtins.str] = None,
            resource_types_scope: typing.Optional[typing.Sequence[builtins.str]] = None,
            tag_key_scope: typing.Optional[builtins.str] = None,
            tag_value_scope: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that specifies organization custom rule metadata such as resource type, resource ID of AWS resource, Lambda function ARN, and organization trigger types that trigger AWS Config to evaluate your AWS resources against a rule.

            It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic.

            :param lambda_function_arn: The lambda function ARN.
            :param organization_config_rule_trigger_types: The type of notification that triggers AWS Config to run an evaluation for a rule. You can specify the following notification types: - ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers a configuration item as a result of a resource change. - ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS. - ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency specified for ``MaximumExecutionFrequency`` .
            :param description: The description that you provide for your organization AWS Config rule.
            :param input_parameters: A string, in JSON format, that is passed to your organization AWS Config rule Lambda function.
            :param maximum_execution_frequency: The maximum frequency with which AWS Config runs evaluations for a rule. Your custom rule is triggered when AWS Config delivers the configuration snapshot. For more information, see ``ConfigSnapshotDeliveryProperties`` . .. epigraph:: By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.
            :param resource_id_scope: The ID of the AWS resource that was evaluated.
            :param resource_types_scope: The type of the AWS resource that was evaluated.
            :param tag_key_scope: One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.
            :param tag_value_scope: The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_config as config
                
                organization_custom_rule_metadata_property = config.CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty(
                    lambda_function_arn="lambdaFunctionArn",
                    organization_config_rule_trigger_types=["organizationConfigRuleTriggerTypes"],
                
                    # the properties below are optional
                    description="description",
                    input_parameters="inputParameters",
                    maximum_execution_frequency="maximumExecutionFrequency",
                    resource_id_scope="resourceIdScope",
                    resource_types_scope=["resourceTypesScope"],
                    tag_key_scope="tagKeyScope",
                    tag_value_scope="tagValueScope"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__577ff8fffcd60b024a0a0af5c8c7405c61a255f395abee4abfc89e9a61d61339)
                check_type(argname="argument lambda_function_arn", value=lambda_function_arn, expected_type=type_hints["lambda_function_arn"])
                check_type(argname="argument organization_config_rule_trigger_types", value=organization_config_rule_trigger_types, expected_type=type_hints["organization_config_rule_trigger_types"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument input_parameters", value=input_parameters, expected_type=type_hints["input_parameters"])
                check_type(argname="argument maximum_execution_frequency", value=maximum_execution_frequency, expected_type=type_hints["maximum_execution_frequency"])
                check_type(argname="argument resource_id_scope", value=resource_id_scope, expected_type=type_hints["resource_id_scope"])
                check_type(argname="argument resource_types_scope", value=resource_types_scope, expected_type=type_hints["resource_types_scope"])
                check_type(argname="argument tag_key_scope", value=tag_key_scope, expected_type=type_hints["tag_key_scope"])
                check_type(argname="argument tag_value_scope", value=tag_value_scope, expected_type=type_hints["tag_value_scope"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "lambda_function_arn": lambda_function_arn,
                "organization_config_rule_trigger_types": organization_config_rule_trigger_types,
            }
            if description is not None:
                self._values["description"] = description
            if input_parameters is not None:
                self._values["input_parameters"] = input_parameters
            if maximum_execution_frequency is not None:
                self._values["maximum_execution_frequency"] = maximum_execution_frequency
            if resource_id_scope is not None:
                self._values["resource_id_scope"] = resource_id_scope
            if resource_types_scope is not None:
                self._values["resource_types_scope"] = resource_types_scope
            if tag_key_scope is not None:
                self._values["tag_key_scope"] = tag_key_scope
            if tag_value_scope is not None:
                self._values["tag_value_scope"] = tag_value_scope

        @builtins.property
        def lambda_function_arn(self) -> builtins.str:
            '''The lambda function ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-lambdafunctionarn
            '''
            result = self._values.get("lambda_function_arn")
            assert result is not None, "Required property 'lambda_function_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def organization_config_rule_trigger_types(self) -> typing.List[builtins.str]:
            '''The type of notification that triggers AWS Config to run an evaluation for a rule.

            You can specify the following notification types:

            - ``ConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers a configuration item as a result of a resource change.
            - ``OversizedConfigurationItemChangeNotification`` - Triggers an evaluation when AWS Config delivers an oversized configuration item. AWS Config may generate this notification type when a resource changes and the notification exceeds the maximum size allowed by Amazon SNS.
            - ``ScheduledNotification`` - Triggers a periodic evaluation at the frequency specified for ``MaximumExecutionFrequency`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-organizationconfigruletriggertypes
            '''
            result = self._values.get("organization_config_rule_trigger_types")
            assert result is not None, "Required property 'organization_config_rule_trigger_types' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description that you provide for your organization AWS Config rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def input_parameters(self) -> typing.Optional[builtins.str]:
            '''A string, in JSON format, that is passed to your organization AWS Config rule Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-inputparameters
            '''
            result = self._values.get("input_parameters")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def maximum_execution_frequency(self) -> typing.Optional[builtins.str]:
            '''The maximum frequency with which AWS Config runs evaluations for a rule.

            Your custom rule is triggered when AWS Config delivers the configuration snapshot. For more information, see ``ConfigSnapshotDeliveryProperties`` .
            .. epigraph::

               By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-maximumexecutionfrequency
            '''
            result = self._values.get("maximum_execution_frequency")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_id_scope(self) -> typing.Optional[builtins.str]:
            '''The ID of the AWS resource that was evaluated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-resourceidscope
            '''
            result = self._values.get("resource_id_scope")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_types_scope(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The type of the AWS resource that was evaluated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-resourcetypesscope
            '''
            result = self._values.get("resource_types_scope")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def tag_key_scope(self) -> typing.Optional[builtins.str]:
            '''One part of a key-value pair that make up a tag.

            A key is a general label that acts like a category for more specific tag values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-tagkeyscope
            '''
            result = self._values.get("tag_key_scope")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tag_value_scope(self) -> typing.Optional[builtins.str]:
            '''The optional part of a key-value pair that make up a tag.

            A value acts as a descriptor within a tag category (key).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationcustomrulemetadata.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata-tagvaluescope
            '''
            result = self._values.get("tag_value_scope")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OrganizationCustomRuleMetadataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_config.CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "rule_identifier": "ruleIdentifier",
            "description": "description",
            "input_parameters": "inputParameters",
            "maximum_execution_frequency": "maximumExecutionFrequency",
            "resource_id_scope": "resourceIdScope",
            "resource_types_scope": "resourceTypesScope",
            "tag_key_scope": "tagKeyScope",
            "tag_value_scope": "tagValueScope",
        },
    )
    class OrganizationManagedRuleMetadataProperty:
        def __init__(
            self,
            *,
            rule_identifier: builtins.str,
            description: typing.Optional[builtins.str] = None,
            input_parameters: typing.Optional[builtins.str] = None,
            maximum_execution_frequency: typing.Optional[builtins.str] = None,
            resource_id_scope: typing.Optional[builtins.str] = None,
            resource_types_scope: typing.Optional[typing.Sequence[builtins.str]] = None,
            tag_key_scope: typing.Optional[builtins.str] = None,
            tag_value_scope: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that specifies organization managed rule metadata such as resource type and ID of AWS resource along with the rule identifier.

            It also provides the frequency with which you want AWS Config to run evaluations for the rule if the trigger type is periodic.

            :param rule_identifier: For organization config managed rules, a predefined identifier from a list. For example, ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see `Using AWS Config managed rules <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`_ .
            :param description: The description that you provide for your organization AWS Config rule.
            :param input_parameters: A string, in JSON format, that is passed to your organization AWS Config rule Lambda function.
            :param maximum_execution_frequency: The maximum frequency with which AWS Config runs evaluations for a rule. This is for an AWS Config managed rule that is triggered at a periodic frequency. .. epigraph:: By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.
            :param resource_id_scope: The ID of the AWS resource that was evaluated.
            :param resource_types_scope: The type of the AWS resource that was evaluated.
            :param tag_key_scope: One part of a key-value pair that make up a tag. A key is a general label that acts like a category for more specific tag values.
            :param tag_value_scope: The optional part of a key-value pair that make up a tag. A value acts as a descriptor within a tag category (key).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_config as config
                
                organization_managed_rule_metadata_property = config.CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty(
                    rule_identifier="ruleIdentifier",
                
                    # the properties below are optional
                    description="description",
                    input_parameters="inputParameters",
                    maximum_execution_frequency="maximumExecutionFrequency",
                    resource_id_scope="resourceIdScope",
                    resource_types_scope=["resourceTypesScope"],
                    tag_key_scope="tagKeyScope",
                    tag_value_scope="tagValueScope"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5dc57dfb13d36d34c8df89d07bf5b91f2f225b7f64fcaf1e0ec85cc4bf0008e6)
                check_type(argname="argument rule_identifier", value=rule_identifier, expected_type=type_hints["rule_identifier"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument input_parameters", value=input_parameters, expected_type=type_hints["input_parameters"])
                check_type(argname="argument maximum_execution_frequency", value=maximum_execution_frequency, expected_type=type_hints["maximum_execution_frequency"])
                check_type(argname="argument resource_id_scope", value=resource_id_scope, expected_type=type_hints["resource_id_scope"])
                check_type(argname="argument resource_types_scope", value=resource_types_scope, expected_type=type_hints["resource_types_scope"])
                check_type(argname="argument tag_key_scope", value=tag_key_scope, expected_type=type_hints["tag_key_scope"])
                check_type(argname="argument tag_value_scope", value=tag_value_scope, expected_type=type_hints["tag_value_scope"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "rule_identifier": rule_identifier,
            }
            if description is not None:
                self._values["description"] = description
            if input_parameters is not None:
                self._values["input_parameters"] = input_parameters
            if maximum_execution_frequency is not None:
                self._values["maximum_execution_frequency"] = maximum_execution_frequency
            if resource_id_scope is not None:
                self._values["resource_id_scope"] = resource_id_scope
            if resource_types_scope is not None:
                self._values["resource_types_scope"] = resource_types_scope
            if tag_key_scope is not None:
                self._values["tag_key_scope"] = tag_key_scope
            if tag_value_scope is not None:
                self._values["tag_value_scope"] = tag_value_scope

        @builtins.property
        def rule_identifier(self) -> builtins.str:
            '''For organization config managed rules, a predefined identifier from a list.

            For example, ``IAM_PASSWORD_POLICY`` is a managed rule. To reference a managed rule, see `Using AWS Config managed rules <https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-ruleidentifier
            '''
            result = self._values.get("rule_identifier")
            assert result is not None, "Required property 'rule_identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description that you provide for your organization AWS Config rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def input_parameters(self) -> typing.Optional[builtins.str]:
            '''A string, in JSON format, that is passed to your organization AWS Config rule Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-inputparameters
            '''
            result = self._values.get("input_parameters")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def maximum_execution_frequency(self) -> typing.Optional[builtins.str]:
            '''The maximum frequency with which AWS Config runs evaluations for a rule.

            This is for an AWS Config managed rule that is triggered at a periodic frequency.
            .. epigraph::

               By default, rules with a periodic trigger are evaluated every 24 hours. To change the frequency, specify a valid value for the ``MaximumExecutionFrequency`` parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-maximumexecutionfrequency
            '''
            result = self._values.get("maximum_execution_frequency")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_id_scope(self) -> typing.Optional[builtins.str]:
            '''The ID of the AWS resource that was evaluated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-resourceidscope
            '''
            result = self._values.get("resource_id_scope")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_types_scope(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The type of the AWS resource that was evaluated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-resourcetypesscope
            '''
            result = self._values.get("resource_types_scope")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def tag_key_scope(self) -> typing.Optional[builtins.str]:
            '''One part of a key-value pair that make up a tag.

            A key is a general label that acts like a category for more specific tag values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-tagkeyscope
            '''
            result = self._values.get("tag_key_scope")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tag_value_scope(self) -> typing.Optional[builtins.str]:
            '''The optional part of a key-value pair that make up a tag.

            A value acts as a descriptor within a tag category (key).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconfigrule-organizationmanagedrulemetadata.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata-tagvaluescope
            '''
            result = self._values.get("tag_value_scope")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OrganizationManagedRuleMetadataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_config.CfnOrganizationConfigRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "organization_config_rule_name": "organizationConfigRuleName",
        "excluded_accounts": "excludedAccounts",
        "organization_custom_policy_rule_metadata": "organizationCustomPolicyRuleMetadata",
        "organization_custom_rule_metadata": "organizationCustomRuleMetadata",
        "organization_managed_rule_metadata": "organizationManagedRuleMetadata",
    },
)
class CfnOrganizationConfigRuleProps:
    def __init__(
        self,
        *,
        organization_config_rule_name: builtins.str,
        excluded_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
        organization_custom_policy_rule_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationConfigRule.OrganizationCustomPolicyRuleMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        organization_custom_rule_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        organization_managed_rule_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnOrganizationConfigRule``.

        :param organization_config_rule_name: The name that you assign to organization AWS Config rule.
        :param excluded_accounts: A comma-separated list of accounts excluded from organization AWS Config rule.
        :param organization_custom_policy_rule_metadata: An object that specifies metadata for your organization's AWS Config Custom Policy rule. The metadata includes the runtime system in use, which accounts have debug logging enabled, and other custom rule metadata, such as resource type, resource ID of AWS resource, and organization trigger types that initiate AWS Config to evaluate AWS resources against a rule.
        :param organization_custom_rule_metadata: An ``OrganizationCustomRuleMetadata`` object.
        :param organization_managed_rule_metadata: An ``OrganizationManagedRuleMetadata`` object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_config as config
            
            cfn_organization_config_rule_props = config.CfnOrganizationConfigRuleProps(
                organization_config_rule_name="organizationConfigRuleName",
            
                # the properties below are optional
                excluded_accounts=["excludedAccounts"],
                organization_custom_policy_rule_metadata=config.CfnOrganizationConfigRule.OrganizationCustomPolicyRuleMetadataProperty(
                    policy_text="policyText",
                    runtime="runtime",
            
                    # the properties below are optional
                    debug_log_delivery_accounts=["debugLogDeliveryAccounts"],
                    description="description",
                    input_parameters="inputParameters",
                    maximum_execution_frequency="maximumExecutionFrequency",
                    organization_config_rule_trigger_types=["organizationConfigRuleTriggerTypes"],
                    resource_id_scope="resourceIdScope",
                    resource_types_scope=["resourceTypesScope"],
                    tag_key_scope="tagKeyScope",
                    tag_value_scope="tagValueScope"
                ),
                organization_custom_rule_metadata=config.CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty(
                    lambda_function_arn="lambdaFunctionArn",
                    organization_config_rule_trigger_types=["organizationConfigRuleTriggerTypes"],
            
                    # the properties below are optional
                    description="description",
                    input_parameters="inputParameters",
                    maximum_execution_frequency="maximumExecutionFrequency",
                    resource_id_scope="resourceIdScope",
                    resource_types_scope=["resourceTypesScope"],
                    tag_key_scope="tagKeyScope",
                    tag_value_scope="tagValueScope"
                ),
                organization_managed_rule_metadata=config.CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty(
                    rule_identifier="ruleIdentifier",
            
                    # the properties below are optional
                    description="description",
                    input_parameters="inputParameters",
                    maximum_execution_frequency="maximumExecutionFrequency",
                    resource_id_scope="resourceIdScope",
                    resource_types_scope=["resourceTypesScope"],
                    tag_key_scope="tagKeyScope",
                    tag_value_scope="tagValueScope"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a10a93cf13b9b686cb420cfd72e8482fe531eebf751b0545e33ff1fa1739935)
            check_type(argname="argument organization_config_rule_name", value=organization_config_rule_name, expected_type=type_hints["organization_config_rule_name"])
            check_type(argname="argument excluded_accounts", value=excluded_accounts, expected_type=type_hints["excluded_accounts"])
            check_type(argname="argument organization_custom_policy_rule_metadata", value=organization_custom_policy_rule_metadata, expected_type=type_hints["organization_custom_policy_rule_metadata"])
            check_type(argname="argument organization_custom_rule_metadata", value=organization_custom_rule_metadata, expected_type=type_hints["organization_custom_rule_metadata"])
            check_type(argname="argument organization_managed_rule_metadata", value=organization_managed_rule_metadata, expected_type=type_hints["organization_managed_rule_metadata"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "organization_config_rule_name": organization_config_rule_name,
        }
        if excluded_accounts is not None:
            self._values["excluded_accounts"] = excluded_accounts
        if organization_custom_policy_rule_metadata is not None:
            self._values["organization_custom_policy_rule_metadata"] = organization_custom_policy_rule_metadata
        if organization_custom_rule_metadata is not None:
            self._values["organization_custom_rule_metadata"] = organization_custom_rule_metadata
        if organization_managed_rule_metadata is not None:
            self._values["organization_managed_rule_metadata"] = organization_managed_rule_metadata

    @builtins.property
    def organization_config_rule_name(self) -> builtins.str:
        '''The name that you assign to organization AWS Config rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html#cfn-config-organizationconfigrule-organizationconfigrulename
        '''
        result = self._values.get("organization_config_rule_name")
        assert result is not None, "Required property 'organization_config_rule_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def excluded_accounts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A comma-separated list of accounts excluded from organization AWS Config rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html#cfn-config-organizationconfigrule-excludedaccounts
        '''
        result = self._values.get("excluded_accounts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def organization_custom_policy_rule_metadata(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOrganizationConfigRule.OrganizationCustomPolicyRuleMetadataProperty]]:
        '''An object that specifies metadata for your organization's AWS Config Custom Policy rule.

        The metadata includes the runtime system in use, which accounts have debug logging enabled, and other custom rule metadata, such as resource type, resource ID of AWS resource, and organization trigger types that initiate AWS Config to evaluate AWS resources against a rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html#cfn-config-organizationconfigrule-organizationcustompolicyrulemetadata
        '''
        result = self._values.get("organization_custom_policy_rule_metadata")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOrganizationConfigRule.OrganizationCustomPolicyRuleMetadataProperty]], result)

    @builtins.property
    def organization_custom_rule_metadata(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty]]:
        '''An ``OrganizationCustomRuleMetadata`` object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html#cfn-config-organizationconfigrule-organizationcustomrulemetadata
        '''
        result = self._values.get("organization_custom_rule_metadata")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty]], result)

    @builtins.property
    def organization_managed_rule_metadata(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty]]:
        '''An ``OrganizationManagedRuleMetadata`` object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html#cfn-config-organizationconfigrule-organizationmanagedrulemetadata
        '''
        result = self._values.get("organization_managed_rule_metadata")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOrganizationConfigRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnOrganizationConformancePack(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_config.CfnOrganizationConformancePack",
):
    '''OrganizationConformancePack deploys conformance packs across member accounts in an AWS Organizations .

    OrganizationConformancePack enables organization service access for ``config-multiaccountsetup.amazonaws.com`` through the ``EnableAWSServiceAccess`` action and creates a service linked role in the master account of your organization. The service linked role is created only when the role does not exist in the master account.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html
    :cloudformationResource: AWS::Config::OrganizationConformancePack
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_config as config
        
        cfn_organization_conformance_pack = config.CfnOrganizationConformancePack(self, "MyCfnOrganizationConformancePack",
            organization_conformance_pack_name="organizationConformancePackName",
        
            # the properties below are optional
            conformance_pack_input_parameters=[config.CfnOrganizationConformancePack.ConformancePackInputParameterProperty(
                parameter_name="parameterName",
                parameter_value="parameterValue"
            )],
            delivery_s3_bucket="deliveryS3Bucket",
            delivery_s3_key_prefix="deliveryS3KeyPrefix",
            excluded_accounts=["excludedAccounts"],
            template_body="templateBody",
            template_s3_uri="templateS3Uri"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        organization_conformance_pack_name: builtins.str,
        conformance_pack_input_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOrganizationConformancePack.ConformancePackInputParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        delivery_s3_bucket: typing.Optional[builtins.str] = None,
        delivery_s3_key_prefix: typing.Optional[builtins.str] = None,
        excluded_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
        template_body: typing.Optional[builtins.str] = None,
        template_s3_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param organization_conformance_pack_name: The name you assign to an organization conformance pack.
        :param conformance_pack_input_parameters: A list of ``ConformancePackInputParameter`` objects.
        :param delivery_s3_bucket: The name of the Amazon S3 bucket where AWS Config stores conformance pack templates. .. epigraph:: This field is optional.
        :param delivery_s3_key_prefix: Any folder structure you want to add to an Amazon S3 bucket. .. epigraph:: This field is optional.
        :param excluded_accounts: A comma-separated list of accounts excluded from organization conformance pack.
        :param template_body: A string containing full conformance pack template body. Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.
        :param template_s3_uri: Location of file containing the template body. The uri must point to the conformance pack template (max size: 300 KB).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e30e375d1e6ca8bc1f56bcae0c6e77507133aca25c3deeb11629cc28c42740b7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnOrganizationConformancePackProps(
            organization_conformance_pack_name=organization_conformance_pack_name,
            conformance_pack_input_parameters=conformance_pack_input_parameters,
            delivery_s3_bucket=delivery_s3_bucket,
            delivery_s3_key_prefix=delivery_s3_key_prefix,
            excluded_accounts=excluded_accounts,
            template_body=template_body,
            template_s3_uri=template_s3_uri,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f252aeb695f75bc6a666da23c7215e6f51f866eee755884677a99c1e93dc7a12)
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
            type_hints = typing.get_type_hints(_typecheckingstub__972e7004ff93e8f6b80e4e18e235827cfb0a38ebe7df44468feef3093249b3bf)
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
    @jsii.member(jsii_name="organizationConformancePackName")
    def organization_conformance_pack_name(self) -> builtins.str:
        '''The name you assign to an organization conformance pack.'''
        return typing.cast(builtins.str, jsii.get(self, "organizationConformancePackName"))

    @organization_conformance_pack_name.setter
    def organization_conformance_pack_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cea7f4b86b4812225b1fd37ba822b06ca4f8bd2b4a689d8f0e20d4123126e765)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationConformancePackName", value)

    @builtins.property
    @jsii.member(jsii_name="conformancePackInputParameters")
    def conformance_pack_input_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnOrganizationConformancePack.ConformancePackInputParameterProperty"]]]]:
        '''A list of ``ConformancePackInputParameter`` objects.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnOrganizationConformancePack.ConformancePackInputParameterProperty"]]]], jsii.get(self, "conformancePackInputParameters"))

    @conformance_pack_input_parameters.setter
    def conformance_pack_input_parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnOrganizationConformancePack.ConformancePackInputParameterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__159adc773b03fcb350f20741e9412fc5c36ec7df507a92c7262d5956c971d644)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conformancePackInputParameters", value)

    @builtins.property
    @jsii.member(jsii_name="deliveryS3Bucket")
    def delivery_s3_bucket(self) -> typing.Optional[builtins.str]:
        '''The name of the Amazon S3 bucket where AWS Config stores conformance pack templates.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryS3Bucket"))

    @delivery_s3_bucket.setter
    def delivery_s3_bucket(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a94f3e9391cd9ccab63b3545ca2965f2b81da196ec3ed606dc2485e2d2bbba60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryS3Bucket", value)

    @builtins.property
    @jsii.member(jsii_name="deliveryS3KeyPrefix")
    def delivery_s3_key_prefix(self) -> typing.Optional[builtins.str]:
        '''Any folder structure you want to add to an Amazon S3 bucket.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryS3KeyPrefix"))

    @delivery_s3_key_prefix.setter
    def delivery_s3_key_prefix(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ae88516decc5ecfaa94d5667954693ac8954509566cfdc6d9a34f01c9b4c99d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryS3KeyPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="excludedAccounts")
    def excluded_accounts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A comma-separated list of accounts excluded from organization conformance pack.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "excludedAccounts"))

    @excluded_accounts.setter
    def excluded_accounts(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__febab378993c1407f9ee864835af34497e5cfa444855d849d7a49b108cdac530)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludedAccounts", value)

    @builtins.property
    @jsii.member(jsii_name="templateBody")
    def template_body(self) -> typing.Optional[builtins.str]:
        '''A string containing full conformance pack template body.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateBody"))

    @template_body.setter
    def template_body(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d860cd3b0fe658d27c522bab37bf76c633dcd9da0ecbb8f7f0f2f92015a535a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateBody", value)

    @builtins.property
    @jsii.member(jsii_name="templateS3Uri")
    def template_s3_uri(self) -> typing.Optional[builtins.str]:
        '''Location of file containing the template body.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateS3Uri"))

    @template_s3_uri.setter
    def template_s3_uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e88d12b7509e23789f96b51f072d3f7653802810b5db55480548e0a7bb433046)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateS3Uri", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_config.CfnOrganizationConformancePack.ConformancePackInputParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "parameter_name": "parameterName",
            "parameter_value": "parameterValue",
        },
    )
    class ConformancePackInputParameterProperty:
        def __init__(
            self,
            *,
            parameter_name: builtins.str,
            parameter_value: builtins.str,
        ) -> None:
            '''Input parameters in the form of key-value pairs for the conformance pack, both of which you define.

            Keys can have a maximum character length of 255 characters, and values can have a maximum length of 4096 characters.

            :param parameter_name: One part of a key-value pair.
            :param parameter_value: One part of a key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconformancepack-conformancepackinputparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_config as config
                
                conformance_pack_input_parameter_property = config.CfnOrganizationConformancePack.ConformancePackInputParameterProperty(
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e87ad63785baef983f0ec5a1a9627bbeadc5dda671b5ee551b1239daf8a0f13d)
                check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
                check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "parameter_name": parameter_name,
                "parameter_value": parameter_value,
            }

        @builtins.property
        def parameter_name(self) -> builtins.str:
            '''One part of a key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconformancepack-conformancepackinputparameter.html#cfn-config-organizationconformancepack-conformancepackinputparameter-parametername
            '''
            result = self._values.get("parameter_name")
            assert result is not None, "Required property 'parameter_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameter_value(self) -> builtins.str:
            '''One part of a key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-organizationconformancepack-conformancepackinputparameter.html#cfn-config-organizationconformancepack-conformancepackinputparameter-parametervalue
            '''
            result = self._values.get("parameter_value")
            assert result is not None, "Required property 'parameter_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConformancePackInputParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_config.CfnOrganizationConformancePackProps",
    jsii_struct_bases=[],
    name_mapping={
        "organization_conformance_pack_name": "organizationConformancePackName",
        "conformance_pack_input_parameters": "conformancePackInputParameters",
        "delivery_s3_bucket": "deliveryS3Bucket",
        "delivery_s3_key_prefix": "deliveryS3KeyPrefix",
        "excluded_accounts": "excludedAccounts",
        "template_body": "templateBody",
        "template_s3_uri": "templateS3Uri",
    },
)
class CfnOrganizationConformancePackProps:
    def __init__(
        self,
        *,
        organization_conformance_pack_name: builtins.str,
        conformance_pack_input_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationConformancePack.ConformancePackInputParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        delivery_s3_bucket: typing.Optional[builtins.str] = None,
        delivery_s3_key_prefix: typing.Optional[builtins.str] = None,
        excluded_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
        template_body: typing.Optional[builtins.str] = None,
        template_s3_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnOrganizationConformancePack``.

        :param organization_conformance_pack_name: The name you assign to an organization conformance pack.
        :param conformance_pack_input_parameters: A list of ``ConformancePackInputParameter`` objects.
        :param delivery_s3_bucket: The name of the Amazon S3 bucket where AWS Config stores conformance pack templates. .. epigraph:: This field is optional.
        :param delivery_s3_key_prefix: Any folder structure you want to add to an Amazon S3 bucket. .. epigraph:: This field is optional.
        :param excluded_accounts: A comma-separated list of accounts excluded from organization conformance pack.
        :param template_body: A string containing full conformance pack template body. Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.
        :param template_s3_uri: Location of file containing the template body. The uri must point to the conformance pack template (max size: 300 KB).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_config as config
            
            cfn_organization_conformance_pack_props = config.CfnOrganizationConformancePackProps(
                organization_conformance_pack_name="organizationConformancePackName",
            
                # the properties below are optional
                conformance_pack_input_parameters=[config.CfnOrganizationConformancePack.ConformancePackInputParameterProperty(
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )],
                delivery_s3_bucket="deliveryS3Bucket",
                delivery_s3_key_prefix="deliveryS3KeyPrefix",
                excluded_accounts=["excludedAccounts"],
                template_body="templateBody",
                template_s3_uri="templateS3Uri"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d72ae72e83823c856a2d710ca24a4c227a6d6b865d8fef8ea164121282f98af)
            check_type(argname="argument organization_conformance_pack_name", value=organization_conformance_pack_name, expected_type=type_hints["organization_conformance_pack_name"])
            check_type(argname="argument conformance_pack_input_parameters", value=conformance_pack_input_parameters, expected_type=type_hints["conformance_pack_input_parameters"])
            check_type(argname="argument delivery_s3_bucket", value=delivery_s3_bucket, expected_type=type_hints["delivery_s3_bucket"])
            check_type(argname="argument delivery_s3_key_prefix", value=delivery_s3_key_prefix, expected_type=type_hints["delivery_s3_key_prefix"])
            check_type(argname="argument excluded_accounts", value=excluded_accounts, expected_type=type_hints["excluded_accounts"])
            check_type(argname="argument template_body", value=template_body, expected_type=type_hints["template_body"])
            check_type(argname="argument template_s3_uri", value=template_s3_uri, expected_type=type_hints["template_s3_uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "organization_conformance_pack_name": organization_conformance_pack_name,
        }
        if conformance_pack_input_parameters is not None:
            self._values["conformance_pack_input_parameters"] = conformance_pack_input_parameters
        if delivery_s3_bucket is not None:
            self._values["delivery_s3_bucket"] = delivery_s3_bucket
        if delivery_s3_key_prefix is not None:
            self._values["delivery_s3_key_prefix"] = delivery_s3_key_prefix
        if excluded_accounts is not None:
            self._values["excluded_accounts"] = excluded_accounts
        if template_body is not None:
            self._values["template_body"] = template_body
        if template_s3_uri is not None:
            self._values["template_s3_uri"] = template_s3_uri

    @builtins.property
    def organization_conformance_pack_name(self) -> builtins.str:
        '''The name you assign to an organization conformance pack.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-organizationconformancepackname
        '''
        result = self._values.get("organization_conformance_pack_name")
        assert result is not None, "Required property 'organization_conformance_pack_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def conformance_pack_input_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnOrganizationConformancePack.ConformancePackInputParameterProperty]]]]:
        '''A list of ``ConformancePackInputParameter`` objects.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-conformancepackinputparameters
        '''
        result = self._values.get("conformance_pack_input_parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnOrganizationConformancePack.ConformancePackInputParameterProperty]]]], result)

    @builtins.property
    def delivery_s3_bucket(self) -> typing.Optional[builtins.str]:
        '''The name of the Amazon S3 bucket where AWS Config stores conformance pack templates.

        .. epigraph::

           This field is optional.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-deliverys3bucket
        '''
        result = self._values.get("delivery_s3_bucket")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delivery_s3_key_prefix(self) -> typing.Optional[builtins.str]:
        '''Any folder structure you want to add to an Amazon S3 bucket.

        .. epigraph::

           This field is optional.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-deliverys3keyprefix
        '''
        result = self._values.get("delivery_s3_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def excluded_accounts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A comma-separated list of accounts excluded from organization conformance pack.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-excludedaccounts
        '''
        result = self._values.get("excluded_accounts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def template_body(self) -> typing.Optional[builtins.str]:
        '''A string containing full conformance pack template body.

        Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-templatebody
        '''
        result = self._values.get("template_body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_s3_uri(self) -> typing.Optional[builtins.str]:
        '''Location of file containing the template body.

        The uri must point to the conformance pack template (max size: 300 KB).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html#cfn-config-organizationconformancepack-templates3uri
        '''
        result = self._values.get("template_s3_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOrganizationConformancePackProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnRemediationConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_config.CfnRemediationConfiguration",
):
    '''An object that represents the details about the remediation configuration that includes the remediation action, parameters, and data to execute the action.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html
    :cloudformationResource: AWS::Config::RemediationConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_config as config
        
        # parameters: Any
        
        cfn_remediation_configuration = config.CfnRemediationConfiguration(self, "MyCfnRemediationConfiguration",
            config_rule_name="configRuleName",
            target_id="targetId",
            target_type="targetType",
        
            # the properties below are optional
            automatic=False,
            execution_controls=config.CfnRemediationConfiguration.ExecutionControlsProperty(
                ssm_controls=config.CfnRemediationConfiguration.SsmControlsProperty(
                    concurrent_execution_rate_percentage=123,
                    error_percentage=123
                )
            ),
            maximum_automatic_attempts=123,
            parameters=parameters,
            resource_type="resourceType",
            retry_attempt_seconds=123,
            target_version="targetVersion"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        config_rule_name: builtins.str,
        target_id: builtins.str,
        target_type: builtins.str,
        automatic: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        execution_controls: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRemediationConfiguration.ExecutionControlsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        maximum_automatic_attempts: typing.Optional[jsii.Number] = None,
        parameters: typing.Any = None,
        resource_type: typing.Optional[builtins.str] = None,
        retry_attempt_seconds: typing.Optional[jsii.Number] = None,
        target_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param config_rule_name: The name of the AWS Config rule.
        :param target_id: Target ID is the name of the SSM document.
        :param target_type: The type of the target. Target executes remediation. For example, SSM document.
        :param automatic: The remediation is triggered automatically.
        :param execution_controls: An ExecutionControls object.
        :param maximum_automatic_attempts: The maximum number of failed attempts for auto-remediation. If you do not select a number, the default is 5. For example, if you specify MaximumAutomaticAttempts as 5 with RetryAttemptSeconds as 50 seconds, AWS Config will put a RemediationException on your behalf for the failing resource after the 5th failed attempt within 50 seconds.
        :param parameters: An object of the RemediationParameterValue. For more information, see `RemediationParameterValue <https://docs.aws.amazon.com/config/latest/APIReference/API_RemediationParameterValue.html>`_ . .. epigraph:: The type is a map of strings to RemediationParameterValue.
        :param resource_type: The type of a resource.
        :param retry_attempt_seconds: Time window to determine whether or not to add a remediation exception to prevent infinite remediation attempts. If ``MaximumAutomaticAttempts`` remediation attempts have been made under ``RetryAttemptSeconds`` , a remediation exception will be added to the resource. If you do not select a number, the default is 60 seconds. For example, if you specify ``RetryAttemptSeconds`` as 50 seconds and ``MaximumAutomaticAttempts`` as 5, AWS Config will run auto-remediations 5 times within 50 seconds before adding a remediation exception to the resource.
        :param target_version: Version of the target. For example, version of the SSM document. .. epigraph:: If you make backward incompatible changes to the SSM document, you must call PutRemediationConfiguration API again to ensure the remediations can run.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d77d8d51b1a809acec3ca2be829980e6b8f99140bb4eb3ce00b9209c088915c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRemediationConfigurationProps(
            config_rule_name=config_rule_name,
            target_id=target_id,
            target_type=target_type,
            automatic=automatic,
            execution_controls=execution_controls,
            maximum_automatic_attempts=maximum_automatic_attempts,
            parameters=parameters,
            resource_type=resource_type,
            retry_attempt_seconds=retry_attempt_seconds,
            target_version=target_version,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74c36a39512198e1aaa76b683ab3d6faa2dedf6814529e3325ab9fdf03a47934)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0981270ccb35fe1ed87d60ce8737ba6f99a474a8edb4981354a5adf2e9e9369b)
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
    @jsii.member(jsii_name="configRuleName")
    def config_rule_name(self) -> builtins.str:
        '''The name of the AWS Config rule.'''
        return typing.cast(builtins.str, jsii.get(self, "configRuleName"))

    @config_rule_name.setter
    def config_rule_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aec925175a5fdb6367c84a01b084043a639caa8c4046c1a46694ae861ddbfeec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configRuleName", value)

    @builtins.property
    @jsii.member(jsii_name="targetId")
    def target_id(self) -> builtins.str:
        '''Target ID is the name of the SSM document.'''
        return typing.cast(builtins.str, jsii.get(self, "targetId"))

    @target_id.setter
    def target_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__728a3fb0792a163b0d41711a1026e997d23c3bab737c4d3fc401219d2e69a7c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetId", value)

    @builtins.property
    @jsii.member(jsii_name="targetType")
    def target_type(self) -> builtins.str:
        '''The type of the target.'''
        return typing.cast(builtins.str, jsii.get(self, "targetType"))

    @target_type.setter
    def target_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8693bd26f1e00cf82d388d4d0c6a4d195b1e165878b4d05bd62ebfe3dd4c25b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetType", value)

    @builtins.property
    @jsii.member(jsii_name="automatic")
    def automatic(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''The remediation is triggered automatically.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "automatic"))

    @automatic.setter
    def automatic(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a612c6be9716c299f22f0fc2b57c084a7cafde2f9ec8ebed4b31decea797bb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automatic", value)

    @builtins.property
    @jsii.member(jsii_name="executionControls")
    def execution_controls(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRemediationConfiguration.ExecutionControlsProperty"]]:
        '''An ExecutionControls object.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRemediationConfiguration.ExecutionControlsProperty"]], jsii.get(self, "executionControls"))

    @execution_controls.setter
    def execution_controls(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRemediationConfiguration.ExecutionControlsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__923c16d43d84ed6ed11e372e8cd76942cbebbe48641cade38fc40a0c5b8a7f12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionControls", value)

    @builtins.property
    @jsii.member(jsii_name="maximumAutomaticAttempts")
    def maximum_automatic_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of failed attempts for auto-remediation.

        If you do not select a number, the default is 5.
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumAutomaticAttempts"))

    @maximum_automatic_attempts.setter
    def maximum_automatic_attempts(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5714155a99562d59349d9e442fb9b95dde4b3edc8e0c0c6ed79babb5d6067731)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumAutomaticAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Any:
        '''An object of the RemediationParameterValue.

        For more information, see `RemediationParameterValue <https://docs.aws.amazon.com/config/latest/APIReference/API_RemediationParameterValue.html>`_ .
        '''
        return typing.cast(typing.Any, jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__791d50036178abe388db7c3245e225f2e7ae9d06d20e7b2503c60ea3460eb769)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> typing.Optional[builtins.str]:
        '''The type of a resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceType"))

    @resource_type.setter
    def resource_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07705cb1e720ab1182823f69be5c3be2ef6f68a41b55f739f5df8c1a9c30deff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceType", value)

    @builtins.property
    @jsii.member(jsii_name="retryAttemptSeconds")
    def retry_attempt_seconds(self) -> typing.Optional[jsii.Number]:
        '''Time window to determine whether or not to add a remediation exception to prevent infinite remediation attempts.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retryAttemptSeconds"))

    @retry_attempt_seconds.setter
    def retry_attempt_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a02058d16a54cc526726991d338a7198653ae37da9de8b8e8aa6f724c390148d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retryAttemptSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="targetVersion")
    def target_version(self) -> typing.Optional[builtins.str]:
        '''Version of the target.

        For example, version of the SSM document.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetVersion"))

    @target_version.setter
    def target_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__526beea102f85b306c0a794c0c56ee453c40e4cbf63ae9026fc54ca9079a1d84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetVersion", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_config.CfnRemediationConfiguration.ExecutionControlsProperty",
        jsii_struct_bases=[],
        name_mapping={"ssm_controls": "ssmControls"},
    )
    class ExecutionControlsProperty:
        def __init__(
            self,
            *,
            ssm_controls: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRemediationConfiguration.SsmControlsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''An ExecutionControls object.

            :param ssm_controls: A SsmControls object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-executioncontrols.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_config as config
                
                execution_controls_property = config.CfnRemediationConfiguration.ExecutionControlsProperty(
                    ssm_controls=config.CfnRemediationConfiguration.SsmControlsProperty(
                        concurrent_execution_rate_percentage=123,
                        error_percentage=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3b9ea89c127bf27cc238eb72a592537954543d3bd38eb16e403d7b344a0f4b06)
                check_type(argname="argument ssm_controls", value=ssm_controls, expected_type=type_hints["ssm_controls"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ssm_controls is not None:
                self._values["ssm_controls"] = ssm_controls

        @builtins.property
        def ssm_controls(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRemediationConfiguration.SsmControlsProperty"]]:
            '''A SsmControls object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-executioncontrols.html#cfn-config-remediationconfiguration-executioncontrols-ssmcontrols
            '''
            result = self._values.get("ssm_controls")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRemediationConfiguration.SsmControlsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExecutionControlsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_config.CfnRemediationConfiguration.RemediationParameterValueProperty",
        jsii_struct_bases=[],
        name_mapping={
            "resource_value": "resourceValue",
            "static_value": "staticValue",
        },
    )
    class RemediationParameterValueProperty:
        def __init__(
            self,
            *,
            resource_value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRemediationConfiguration.ResourceValueProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            static_value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRemediationConfiguration.StaticValueProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The value is either a dynamic (resource) value or a static value.

            You must select either a dynamic value or a static value.

            :param resource_value: The value is dynamic and changes at run-time.
            :param static_value: The value is static and does not change at run-time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-remediationparametervalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_config as config
                
                remediation_parameter_value_property = config.CfnRemediationConfiguration.RemediationParameterValueProperty(
                    resource_value=config.CfnRemediationConfiguration.ResourceValueProperty(
                        value="value"
                    ),
                    static_value=config.CfnRemediationConfiguration.StaticValueProperty(
                        value=["value"],
                        values=["values"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__83268c4a5aa9dd16fbcd9db136b72315f14ed7f5e88cd78d4a8316697c24962a)
                check_type(argname="argument resource_value", value=resource_value, expected_type=type_hints["resource_value"])
                check_type(argname="argument static_value", value=static_value, expected_type=type_hints["static_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if resource_value is not None:
                self._values["resource_value"] = resource_value
            if static_value is not None:
                self._values["static_value"] = static_value

        @builtins.property
        def resource_value(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRemediationConfiguration.ResourceValueProperty"]]:
            '''The value is dynamic and changes at run-time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-remediationparametervalue.html#cfn-config-remediationconfiguration-remediationparametervalue-resourcevalue
            '''
            result = self._values.get("resource_value")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRemediationConfiguration.ResourceValueProperty"]], result)

        @builtins.property
        def static_value(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRemediationConfiguration.StaticValueProperty"]]:
            '''The value is static and does not change at run-time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-remediationparametervalue.html#cfn-config-remediationconfiguration-remediationparametervalue-staticvalue
            '''
            result = self._values.get("static_value")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRemediationConfiguration.StaticValueProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RemediationParameterValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_config.CfnRemediationConfiguration.ResourceValueProperty",
        jsii_struct_bases=[],
        name_mapping={"value": "value"},
    )
    class ResourceValueProperty:
        def __init__(self, *, value: typing.Optional[builtins.str] = None) -> None:
            '''
            :param value: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-resourcevalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_config as config
                
                resource_value_property = config.CfnRemediationConfiguration.ResourceValueProperty(
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5c9b5643d1901ce9d9e3cb8822a2e3bf181afe82eb235c809f78ece9baf11247)
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-resourcevalue.html#cfn-config-remediationconfiguration-resourcevalue-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_config.CfnRemediationConfiguration.SsmControlsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "concurrent_execution_rate_percentage": "concurrentExecutionRatePercentage",
            "error_percentage": "errorPercentage",
        },
    )
    class SsmControlsProperty:
        def __init__(
            self,
            *,
            concurrent_execution_rate_percentage: typing.Optional[jsii.Number] = None,
            error_percentage: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''AWS Systems Manager (SSM) specific remediation controls.

            :param concurrent_execution_rate_percentage: The maximum percentage of remediation actions allowed to run in parallel on the non-compliant resources for that specific rule. You can specify a percentage, such as 10%. The default value is 10.
            :param error_percentage: The percentage of errors that are allowed before SSM stops running automations on non-compliant resources for that specific rule. You can specify a percentage of errors, for example 10%. If you do not specifiy a percentage, the default is 50%. For example, if you set the ErrorPercentage to 40% for 10 non-compliant resources, then SSM stops running the automations when the fifth error is received.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-ssmcontrols.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_config as config
                
                ssm_controls_property = config.CfnRemediationConfiguration.SsmControlsProperty(
                    concurrent_execution_rate_percentage=123,
                    error_percentage=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0c78a12657b478ea0405bceec564d4064e3d948aa0c923a6c353813501256977)
                check_type(argname="argument concurrent_execution_rate_percentage", value=concurrent_execution_rate_percentage, expected_type=type_hints["concurrent_execution_rate_percentage"])
                check_type(argname="argument error_percentage", value=error_percentage, expected_type=type_hints["error_percentage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if concurrent_execution_rate_percentage is not None:
                self._values["concurrent_execution_rate_percentage"] = concurrent_execution_rate_percentage
            if error_percentage is not None:
                self._values["error_percentage"] = error_percentage

        @builtins.property
        def concurrent_execution_rate_percentage(self) -> typing.Optional[jsii.Number]:
            '''The maximum percentage of remediation actions allowed to run in parallel on the non-compliant resources for that specific rule.

            You can specify a percentage, such as 10%. The default value is 10.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-ssmcontrols.html#cfn-config-remediationconfiguration-ssmcontrols-concurrentexecutionratepercentage
            '''
            result = self._values.get("concurrent_execution_rate_percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def error_percentage(self) -> typing.Optional[jsii.Number]:
            '''The percentage of errors that are allowed before SSM stops running automations on non-compliant resources for that specific rule.

            You can specify a percentage of errors, for example 10%. If you do not specifiy a percentage, the default is 50%. For example, if you set the ErrorPercentage to 40% for 10 non-compliant resources, then SSM stops running the automations when the fifth error is received.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-ssmcontrols.html#cfn-config-remediationconfiguration-ssmcontrols-errorpercentage
            '''
            result = self._values.get("error_percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SsmControlsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_config.CfnRemediationConfiguration.StaticValueProperty",
        jsii_struct_bases=[],
        name_mapping={"value": "value", "values": "values"},
    )
    class StaticValueProperty:
        def __init__(
            self,
            *,
            value: typing.Optional[typing.Sequence[builtins.str]] = None,
            values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param value: 
            :param values: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-staticvalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_config as config
                
                static_value_property = config.CfnRemediationConfiguration.StaticValueProperty(
                    value=["value"],
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__40ba6e78a4bc7257e8360741f44912082b2a4d686ec43d8c0869c777777223a0)
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if value is not None:
                self._values["value"] = value
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def value(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-staticvalue.html#cfn-config-remediationconfiguration-staticvalue-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-config-remediationconfiguration-staticvalue.html#cfn-config-remediationconfiguration-staticvalue-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StaticValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_config.CfnRemediationConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "config_rule_name": "configRuleName",
        "target_id": "targetId",
        "target_type": "targetType",
        "automatic": "automatic",
        "execution_controls": "executionControls",
        "maximum_automatic_attempts": "maximumAutomaticAttempts",
        "parameters": "parameters",
        "resource_type": "resourceType",
        "retry_attempt_seconds": "retryAttemptSeconds",
        "target_version": "targetVersion",
    },
)
class CfnRemediationConfigurationProps:
    def __init__(
        self,
        *,
        config_rule_name: builtins.str,
        target_id: builtins.str,
        target_type: builtins.str,
        automatic: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        execution_controls: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRemediationConfiguration.ExecutionControlsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        maximum_automatic_attempts: typing.Optional[jsii.Number] = None,
        parameters: typing.Any = None,
        resource_type: typing.Optional[builtins.str] = None,
        retry_attempt_seconds: typing.Optional[jsii.Number] = None,
        target_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnRemediationConfiguration``.

        :param config_rule_name: The name of the AWS Config rule.
        :param target_id: Target ID is the name of the SSM document.
        :param target_type: The type of the target. Target executes remediation. For example, SSM document.
        :param automatic: The remediation is triggered automatically.
        :param execution_controls: An ExecutionControls object.
        :param maximum_automatic_attempts: The maximum number of failed attempts for auto-remediation. If you do not select a number, the default is 5. For example, if you specify MaximumAutomaticAttempts as 5 with RetryAttemptSeconds as 50 seconds, AWS Config will put a RemediationException on your behalf for the failing resource after the 5th failed attempt within 50 seconds.
        :param parameters: An object of the RemediationParameterValue. For more information, see `RemediationParameterValue <https://docs.aws.amazon.com/config/latest/APIReference/API_RemediationParameterValue.html>`_ . .. epigraph:: The type is a map of strings to RemediationParameterValue.
        :param resource_type: The type of a resource.
        :param retry_attempt_seconds: Time window to determine whether or not to add a remediation exception to prevent infinite remediation attempts. If ``MaximumAutomaticAttempts`` remediation attempts have been made under ``RetryAttemptSeconds`` , a remediation exception will be added to the resource. If you do not select a number, the default is 60 seconds. For example, if you specify ``RetryAttemptSeconds`` as 50 seconds and ``MaximumAutomaticAttempts`` as 5, AWS Config will run auto-remediations 5 times within 50 seconds before adding a remediation exception to the resource.
        :param target_version: Version of the target. For example, version of the SSM document. .. epigraph:: If you make backward incompatible changes to the SSM document, you must call PutRemediationConfiguration API again to ensure the remediations can run.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_config as config
            
            # parameters: Any
            
            cfn_remediation_configuration_props = config.CfnRemediationConfigurationProps(
                config_rule_name="configRuleName",
                target_id="targetId",
                target_type="targetType",
            
                # the properties below are optional
                automatic=False,
                execution_controls=config.CfnRemediationConfiguration.ExecutionControlsProperty(
                    ssm_controls=config.CfnRemediationConfiguration.SsmControlsProperty(
                        concurrent_execution_rate_percentage=123,
                        error_percentage=123
                    )
                ),
                maximum_automatic_attempts=123,
                parameters=parameters,
                resource_type="resourceType",
                retry_attempt_seconds=123,
                target_version="targetVersion"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f0c40c5aeff9a13df456a7637c89ca82a249888a8e5563b98aa3e2856779fd6)
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
            check_type(argname="argument target_id", value=target_id, expected_type=type_hints["target_id"])
            check_type(argname="argument target_type", value=target_type, expected_type=type_hints["target_type"])
            check_type(argname="argument automatic", value=automatic, expected_type=type_hints["automatic"])
            check_type(argname="argument execution_controls", value=execution_controls, expected_type=type_hints["execution_controls"])
            check_type(argname="argument maximum_automatic_attempts", value=maximum_automatic_attempts, expected_type=type_hints["maximum_automatic_attempts"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            check_type(argname="argument retry_attempt_seconds", value=retry_attempt_seconds, expected_type=type_hints["retry_attempt_seconds"])
            check_type(argname="argument target_version", value=target_version, expected_type=type_hints["target_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "config_rule_name": config_rule_name,
            "target_id": target_id,
            "target_type": target_type,
        }
        if automatic is not None:
            self._values["automatic"] = automatic
        if execution_controls is not None:
            self._values["execution_controls"] = execution_controls
        if maximum_automatic_attempts is not None:
            self._values["maximum_automatic_attempts"] = maximum_automatic_attempts
        if parameters is not None:
            self._values["parameters"] = parameters
        if resource_type is not None:
            self._values["resource_type"] = resource_type
        if retry_attempt_seconds is not None:
            self._values["retry_attempt_seconds"] = retry_attempt_seconds
        if target_version is not None:
            self._values["target_version"] = target_version

    @builtins.property
    def config_rule_name(self) -> builtins.str:
        '''The name of the AWS Config rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-configrulename
        '''
        result = self._values.get("config_rule_name")
        assert result is not None, "Required property 'config_rule_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_id(self) -> builtins.str:
        '''Target ID is the name of the SSM document.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-targetid
        '''
        result = self._values.get("target_id")
        assert result is not None, "Required property 'target_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_type(self) -> builtins.str:
        '''The type of the target.

        Target executes remediation. For example, SSM document.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-targettype
        '''
        result = self._values.get("target_type")
        assert result is not None, "Required property 'target_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def automatic(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''The remediation is triggered automatically.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-automatic
        '''
        result = self._values.get("automatic")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def execution_controls(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRemediationConfiguration.ExecutionControlsProperty]]:
        '''An ExecutionControls object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-executioncontrols
        '''
        result = self._values.get("execution_controls")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRemediationConfiguration.ExecutionControlsProperty]], result)

    @builtins.property
    def maximum_automatic_attempts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of failed attempts for auto-remediation. If you do not select a number, the default is 5.

        For example, if you specify MaximumAutomaticAttempts as 5 with RetryAttemptSeconds as 50 seconds, AWS Config will put a RemediationException on your behalf for the failing resource after the 5th failed attempt within 50 seconds.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-maximumautomaticattempts
        '''
        result = self._values.get("maximum_automatic_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def parameters(self) -> typing.Any:
        '''An object of the RemediationParameterValue. For more information, see `RemediationParameterValue <https://docs.aws.amazon.com/config/latest/APIReference/API_RemediationParameterValue.html>`_ .

        .. epigraph::

           The type is a map of strings to RemediationParameterValue.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Any, result)

    @builtins.property
    def resource_type(self) -> typing.Optional[builtins.str]:
        '''The type of a resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-resourcetype
        '''
        result = self._values.get("resource_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retry_attempt_seconds(self) -> typing.Optional[jsii.Number]:
        '''Time window to determine whether or not to add a remediation exception to prevent infinite remediation attempts.

        If ``MaximumAutomaticAttempts`` remediation attempts have been made under ``RetryAttemptSeconds`` , a remediation exception will be added to the resource. If you do not select a number, the default is 60 seconds.

        For example, if you specify ``RetryAttemptSeconds`` as 50 seconds and ``MaximumAutomaticAttempts`` as 5, AWS Config will run auto-remediations 5 times within 50 seconds before adding a remediation exception to the resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-retryattemptseconds
        '''
        result = self._values.get("retry_attempt_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_version(self) -> typing.Optional[builtins.str]:
        '''Version of the target. For example, version of the SSM document.

        .. epigraph::

           If you make backward incompatible changes to the SSM document, you must call PutRemediationConfiguration API again to ensure the remediations can run.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html#cfn-config-remediationconfiguration-targetversion
        '''
        result = self._values.get("target_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRemediationConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnStoredQuery(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_config.CfnStoredQuery",
):
    '''Provides the details of a stored query.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-storedquery.html
    :cloudformationResource: AWS::Config::StoredQuery
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_config as config
        
        cfn_stored_query = config.CfnStoredQuery(self, "MyCfnStoredQuery",
            query_expression="queryExpression",
            query_name="queryName",
        
            # the properties below are optional
            query_description="queryDescription",
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
        query_expression: builtins.str,
        query_name: builtins.str,
        query_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param query_expression: The expression of the query. For example, ``SELECT resourceId, resourceType, supplementaryConfiguration.BucketVersioningConfiguration.status WHERE resourceType = 'AWS::S3::Bucket' AND supplementaryConfiguration.BucketVersioningConfiguration.status = 'Off'.``
        :param query_name: The name of the query.
        :param query_description: A unique description for the query.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f740fdda2b469339e90610372faa181ce8f5c105aada22101b165e104f0931d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStoredQueryProps(
            query_expression=query_expression,
            query_name=query_name,
            query_description=query_description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07accbd2024de757d267b6a56c9c69945d6e00475dcbebdcb2827b570958a6c3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__def101baeae59836b51a0510d3933e645988c353a9a0ddeae879b5d45da36530)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrQueryArn")
    def attr_query_arn(self) -> builtins.str:
        '''Amazon Resource Name (ARN) of the query.

        For example, arn:partition:service:region:account-id:resource-type/resource-name/resource-id.

        :cloudformationAttribute: QueryArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrQueryArn"))

    @builtins.property
    @jsii.member(jsii_name="attrQueryId")
    def attr_query_id(self) -> builtins.str:
        '''The ID of the query.

        :cloudformationAttribute: QueryId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrQueryId"))

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
    @jsii.member(jsii_name="queryExpression")
    def query_expression(self) -> builtins.str:
        '''The expression of the query.'''
        return typing.cast(builtins.str, jsii.get(self, "queryExpression"))

    @query_expression.setter
    def query_expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68f07b8140bc1756df33b7349243de220a74acc8b22b3147e10df17d805bc46e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryExpression", value)

    @builtins.property
    @jsii.member(jsii_name="queryName")
    def query_name(self) -> builtins.str:
        '''The name of the query.'''
        return typing.cast(builtins.str, jsii.get(self, "queryName"))

    @query_name.setter
    def query_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c2d99f1e6f7c25ab75d279f03683a97d527c922ec9fa2631ca2d69a67087d7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryName", value)

    @builtins.property
    @jsii.member(jsii_name="queryDescription")
    def query_description(self) -> typing.Optional[builtins.str]:
        '''A unique description for the query.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryDescription"))

    @query_description.setter
    def query_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ed15ad66590b2bdac4f3a3adc1b4a104cfd7ec4d8f6cbfbad2588531f9c38b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryDescription", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1eb31c625f25801e6c38cec9ee395832782b987abddb68d127cc6e79701d2fb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_config.CfnStoredQueryProps",
    jsii_struct_bases=[],
    name_mapping={
        "query_expression": "queryExpression",
        "query_name": "queryName",
        "query_description": "queryDescription",
        "tags": "tags",
    },
)
class CfnStoredQueryProps:
    def __init__(
        self,
        *,
        query_expression: builtins.str,
        query_name: builtins.str,
        query_description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnStoredQuery``.

        :param query_expression: The expression of the query. For example, ``SELECT resourceId, resourceType, supplementaryConfiguration.BucketVersioningConfiguration.status WHERE resourceType = 'AWS::S3::Bucket' AND supplementaryConfiguration.BucketVersioningConfiguration.status = 'Off'.``
        :param query_name: The name of the query.
        :param query_description: A unique description for the query.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-storedquery.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_config as config
            
            cfn_stored_query_props = config.CfnStoredQueryProps(
                query_expression="queryExpression",
                query_name="queryName",
            
                # the properties below are optional
                query_description="queryDescription",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69bfcb3d7c917dfc61f55867cacc3efcb5ef56fa63ad37f8f26635c038ca8c94)
            check_type(argname="argument query_expression", value=query_expression, expected_type=type_hints["query_expression"])
            check_type(argname="argument query_name", value=query_name, expected_type=type_hints["query_name"])
            check_type(argname="argument query_description", value=query_description, expected_type=type_hints["query_description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "query_expression": query_expression,
            "query_name": query_name,
        }
        if query_description is not None:
            self._values["query_description"] = query_description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def query_expression(self) -> builtins.str:
        '''The expression of the query.

        For example, ``SELECT resourceId, resourceType, supplementaryConfiguration.BucketVersioningConfiguration.status WHERE resourceType = 'AWS::S3::Bucket' AND supplementaryConfiguration.BucketVersioningConfiguration.status = 'Off'.``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-storedquery.html#cfn-config-storedquery-queryexpression
        '''
        result = self._values.get("query_expression")
        assert result is not None, "Required property 'query_expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query_name(self) -> builtins.str:
        '''The name of the query.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-storedquery.html#cfn-config-storedquery-queryname
        '''
        result = self._values.get("query_name")
        assert result is not None, "Required property 'query_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def query_description(self) -> typing.Optional[builtins.str]:
        '''A unique description for the query.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-storedquery.html#cfn-config-storedquery-querydescription
        '''
        result = self._values.get("query_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-storedquery.html#cfn-config-storedquery-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStoredQueryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_config.IRule")
class IRule(_IResource_c80c4260, typing_extensions.Protocol):
    '''Interface representing an AWS Config rule.'''

    @builtins.property
    @jsii.member(jsii_name="configRuleName")
    def config_rule_name(self) -> builtins.str:
        '''The name of the rule.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="onComplianceChange")
    def on_compliance_change(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a EventBridge event rule which triggers for rule compliance events.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        ...

    @jsii.member(jsii_name="onEvent")
    def on_event(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines an EventBridge event rule which triggers for rule events.

        Use
        ``rule.addEventPattern(pattern)`` to specify a filter.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        ...

    @jsii.member(jsii_name="onReEvaluationStatus")
    def on_re_evaluation_status(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a EventBridge event rule which triggers for rule re-evaluation status events.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        ...


class _IRuleProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''Interface representing an AWS Config rule.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_config.IRule"

    @builtins.property
    @jsii.member(jsii_name="configRuleName")
    def config_rule_name(self) -> builtins.str:
        '''The name of the rule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "configRuleName"))

    @jsii.member(jsii_name="onComplianceChange")
    def on_compliance_change(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a EventBridge event rule which triggers for rule compliance events.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50bd433608bc8223746dfd9182d27a03d33e9feb360d971e5fbe80b64c01bad7)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onComplianceChange", [id, options]))

    @jsii.member(jsii_name="onEvent")
    def on_event(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines an EventBridge event rule which triggers for rule events.

        Use
        ``rule.addEventPattern(pattern)`` to specify a filter.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6febfef82b3f86776d6cee7dc380662e7260e6c87725a51aa2887e287633d64c)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onEvent", [id, options]))

    @jsii.member(jsii_name="onReEvaluationStatus")
    def on_re_evaluation_status(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines a EventBridge event rule which triggers for rule re-evaluation status events.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a7e56664b002adfcae896eec3992132b8186b275c8bb2d9a117f442e9ddac36)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onReEvaluationStatus", [id, options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRule).__jsii_proxy_class__ = lambda : _IRuleProxy


@jsii.implements(IRule)
class ManagedRule(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_config.ManagedRule",
):
    '''A new managed rule.

    :resource: AWS::Config::ConfigRule
    :exampleMetadata: infused

    Example::

        # https://docs.aws.amazon.com/config/latest/developerguide/access-keys-rotated.html
        config.ManagedRule(self, "AccessKeysRotated",
            identifier=config.ManagedRuleIdentifiers.ACCESS_KEYS_ROTATED,
            input_parameters={
                "max_access_key_age": 60
            },
        
            # default is 24 hours
            maximum_execution_frequency=config.MaximumExecutionFrequency.TWELVE_HOURS
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        identifier: builtins.str,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        maximum_execution_frequency: typing.Optional["MaximumExecutionFrequency"] = None,
        rule_scope: typing.Optional["RuleScope"] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param identifier: The identifier of the AWS managed rule.
        :param config_rule_name: A name for the AWS Config rule. Default: - CloudFormation generated name
        :param description: A description about this AWS Config rule. Default: - No description
        :param input_parameters: Input parameter values that are passed to the AWS Config rule. Default: - No input parameters
        :param maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        :param rule_scope: Defines which resources trigger an evaluation for an AWS Config rule. Default: - evaluations for the rule are triggered when any resource in the recording group changes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b04eb11639f1874bbc847a298e884e6c6104bf56bf29a6c68f11ca608818337a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ManagedRuleProps(
            identifier=identifier,
            config_rule_name=config_rule_name,
            description=description,
            input_parameters=input_parameters,
            maximum_execution_frequency=maximum_execution_frequency,
            rule_scope=rule_scope,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromConfigRuleName")
    @builtins.classmethod
    def from_config_rule_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        config_rule_name: builtins.str,
    ) -> IRule:
        '''Imports an existing rule.

        :param scope: -
        :param id: -
        :param config_rule_name: the name of the rule.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd906bb9949fe90ea1d037daff0b00a51209fdc942e8985cd71522bfc1fdb93a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
        return typing.cast(IRule, jsii.sinvoke(cls, "fromConfigRuleName", [scope, id, config_rule_name]))

    @jsii.member(jsii_name="onComplianceChange")
    def on_compliance_change(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines an EventBridge event rule which triggers for rule compliance events.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a23a1b4dbfc55b4ed462cfe9bdf1561bd5e4f5a47d8e23742648befac9fbdb62)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onComplianceChange", [id, options]))

    @jsii.member(jsii_name="onEvent")
    def on_event(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines an EventBridge event rule which triggers for rule events.

        Use
        ``rule.addEventPattern(pattern)`` to specify a filter.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2022c059de0a75d3a5144e438901a8b401177fd288452cd66f51ef4be8cf04f9)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onEvent", [id, options]))

    @jsii.member(jsii_name="onReEvaluationStatus")
    def on_re_evaluation_status(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines an EventBridge event rule which triggers for rule re-evaluation status events.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73a59bb1baf3b28c1af78b03eef77dfa2dd896ce471e8f0e9bc3cc92f565135e)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onReEvaluationStatus", [id, options]))

    @builtins.property
    @jsii.member(jsii_name="configRuleArn")
    def config_rule_arn(self) -> builtins.str:
        '''The arn of the rule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "configRuleArn"))

    @builtins.property
    @jsii.member(jsii_name="configRuleComplianceType")
    def config_rule_compliance_type(self) -> builtins.str:
        '''The compliance status of the rule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "configRuleComplianceType"))

    @builtins.property
    @jsii.member(jsii_name="configRuleId")
    def config_rule_id(self) -> builtins.str:
        '''The id of the rule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "configRuleId"))

    @builtins.property
    @jsii.member(jsii_name="configRuleName")
    def config_rule_name(self) -> builtins.str:
        '''The name of the rule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "configRuleName"))

    @builtins.property
    @jsii.member(jsii_name="isCustomWithChanges")
    def _is_custom_with_changes(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "isCustomWithChanges"))

    @_is_custom_with_changes.setter
    def _is_custom_with_changes(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04827ab0bb47eedff43c2f84b879e3697cdf9730cbb27993d70bf043fd305d6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isCustomWithChanges", value)

    @builtins.property
    @jsii.member(jsii_name="isManaged")
    def _is_managed(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "isManaged"))

    @_is_managed.setter
    def _is_managed(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__826b91f1363d629c0ed925d90a79b869890a41b6c4114592f18f237ecec2d251)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isManaged", value)

    @builtins.property
    @jsii.member(jsii_name="ruleScope")
    def _rule_scope(self) -> typing.Optional["RuleScope"]:
        return typing.cast(typing.Optional["RuleScope"], jsii.get(self, "ruleScope"))

    @_rule_scope.setter
    def _rule_scope(self, value: typing.Optional["RuleScope"]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49514315a00f8eccd0c88567ab6fd7f8fd1f97e7d5382a88e6bb3dd5185d8c9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleScope", value)


class ManagedRuleIdentifiers(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_config.ManagedRuleIdentifiers",
):
    '''Managed rules that are supported by AWS Config.

    :see: https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html
    :exampleMetadata: infused

    Example::

        # https://docs.aws.amazon.com/config/latest/developerguide/access-keys-rotated.html
        config.ManagedRule(self, "AccessKeysRotated",
            identifier=config.ManagedRuleIdentifiers.ACCESS_KEYS_ROTATED,
            input_parameters={
                "max_access_key_age": 60
            },
        
            # default is 24 hours
            maximum_execution_frequency=config.MaximumExecutionFrequency.TWELVE_HOURS
        )
    '''

    @jsii.python.classproperty
    @jsii.member(jsii_name="ACCESS_KEYS_ROTATED")
    def ACCESS_KEYS_ROTATED(cls) -> builtins.str:
        '''Checks whether the active access keys are rotated within the number of days specified in maxAccessKeyAge.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/access-keys-rotated.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ACCESS_KEYS_ROTATED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ACCOUNT_PART_OF_ORGANIZATIONS")
    def ACCOUNT_PART_OF_ORGANIZATIONS(cls) -> builtins.str:
        '''Checks whether AWS account is part of AWS Organizations.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/account-part-of-organizations.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ACCOUNT_PART_OF_ORGANIZATIONS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ACM_CERTIFICATE_EXPIRATION_CHECK")
    def ACM_CERTIFICATE_EXPIRATION_CHECK(cls) -> builtins.str:
        '''Checks whether ACM Certificates in your account are marked for expiration within the specified number of days.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/acm-certificate-expiration-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ACM_CERTIFICATE_EXPIRATION_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALB_DESYNC_MODE_CHECK")
    def ALB_DESYNC_MODE_CHECK(cls) -> builtins.str:
        '''Checks if an Application Load Balancer (ALB) is configured with a user defined desync mitigation mode.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/alb-desync-mode-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ALB_DESYNC_MODE_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALB_HTTP_DROP_INVALID_HEADER_ENABLED")
    def ALB_HTTP_DROP_INVALID_HEADER_ENABLED(cls) -> builtins.str:
        '''Checks if rule evaluates Application Load Balancers (ALBs) to ensure they are configured to drop http headers.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/alb-http-drop-invalid-header-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ALB_HTTP_DROP_INVALID_HEADER_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALB_HTTP_TO_HTTPS_REDIRECTION_CHECK")
    def ALB_HTTP_TO_HTTPS_REDIRECTION_CHECK(cls) -> builtins.str:
        '''Checks whether HTTP to HTTPS redirection is configured on all HTTP listeners of Application Load Balancer.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/alb-http-to-https-redirection-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ALB_HTTP_TO_HTTPS_REDIRECTION_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALB_WAF_ENABLED")
    def ALB_WAF_ENABLED(cls) -> builtins.str:
        '''Checks if Web Application Firewall (WAF) is enabled on Application Load Balancers (ALBs).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/alb-waf-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ALB_WAF_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="API_GW_ASSOCIATED_WITH_WAF")
    def API_GW_ASSOCIATED_WITH_WAF(cls) -> builtins.str:
        '''Checks if an Amazon API Gateway API stage is using an AWS WAF Web ACL.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/api-gw-associated-with-waf.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "API_GW_ASSOCIATED_WITH_WAF"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="API_GW_CACHE_ENABLED_AND_ENCRYPTED")
    def API_GW_CACHE_ENABLED_AND_ENCRYPTED(cls) -> builtins.str:
        '''Checks that all methods in Amazon API Gateway stages have caching enabled and encrypted.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/api-gw-cache-enabled-and-encrypted.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "API_GW_CACHE_ENABLED_AND_ENCRYPTED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="API_GW_ENDPOINT_TYPE_CHECK")
    def API_GW_ENDPOINT_TYPE_CHECK(cls) -> builtins.str:
        '''Checks that Amazon API Gateway APIs are of the type specified in the rule parameter endpointConfigurationType.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/api-gw-endpoint-type-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "API_GW_ENDPOINT_TYPE_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="API_GW_EXECUTION_LOGGING_ENABLED")
    def API_GW_EXECUTION_LOGGING_ENABLED(cls) -> builtins.str:
        '''Checks that all methods in Amazon API Gateway stage has logging enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/api-gw-execution-logging-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "API_GW_EXECUTION_LOGGING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="API_GW_SSL_ENABLED")
    def API_GW_SSL_ENABLED(cls) -> builtins.str:
        '''Checks if a REST API stage uses an Secure Sockets Layer (SSL) certificate.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/api-gw-ssl-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "API_GW_SSL_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="API_GW_XRAY_ENABLED")
    def API_GW_XRAY_ENABLED(cls) -> builtins.str:
        '''Checks if AWS X-Ray tracing is enabled on Amazon API Gateway REST APIs.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/api-gw-xray-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "API_GW_XRAY_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="API_GWV2_ACCESS_LOGS_ENABLED")
    def API_GWV2_ACCESS_LOGS_ENABLED(cls) -> builtins.str:
        '''Checks if Amazon API Gateway V2 stages have access logging enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/api-gwv2-access-logs-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "API_GWV2_ACCESS_LOGS_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="API_GWV2_AUTHORIZATION_TYPE_CONFIGURED")
    def API_GWV2_AUTHORIZATION_TYPE_CONFIGURED(cls) -> builtins.str:
        '''Checks if Amazon API Gatewayv2 API routes have an authorization type set.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/api-gwv2-authorization-type-configured.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "API_GWV2_AUTHORIZATION_TYPE_CONFIGURED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="APPROVED_AMIS_BY_ID")
    def APPROVED_AMIS_BY_ID(cls) -> builtins.str:
        '''Checks whether running instances are using specified AMIs.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/approved-amis-by-id.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "APPROVED_AMIS_BY_ID"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="APPROVED_AMIS_BY_TAG")
    def APPROVED_AMIS_BY_TAG(cls) -> builtins.str:
        '''Checks whether running instances are using specified AMIs.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/approved-amis-by-tag.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "APPROVED_AMIS_BY_TAG"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AURORA_LAST_BACKUP_RECOVERY_POINT_CREATED")
    def AURORA_LAST_BACKUP_RECOVERY_POINT_CREATED(cls) -> builtins.str:
        '''Checks if a recovery point was created for Amazon Aurora DB clusters.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/aurora-last-backup-recovery-point-created.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "AURORA_LAST_BACKUP_RECOVERY_POINT_CREATED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AURORA_MYSQL_BACKTRACKING_ENABLED")
    def AURORA_MYSQL_BACKTRACKING_ENABLED(cls) -> builtins.str:
        '''Checks if an Amazon Aurora MySQL cluster has backtracking enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/aurora-mysql-backtracking-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "AURORA_MYSQL_BACKTRACKING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AURORA_RESOURCES_PROTECTED_BY_BACKUP_PLAN")
    def AURORA_RESOURCES_PROTECTED_BY_BACKUP_PLAN(cls) -> builtins.str:
        '''Checks if Amazon Aurora DB clusters are protected by a backup plan.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/aurora-resources-protected-by-backup-plan.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "AURORA_RESOURCES_PROTECTED_BY_BACKUP_PLAN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTOSCALING_CAPACITY_REBALANCING")
    def AUTOSCALING_CAPACITY_REBALANCING(cls) -> builtins.str:
        '''Checks if Capacity Rebalancing is enabled for Amazon EC2 Auto Scaling groups that use multiple instance types.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/autoscaling-capacity-rebalancing.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "AUTOSCALING_CAPACITY_REBALANCING"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTOSCALING_GROUP_ELB_HEALTHCHECK_REQUIRED")
    def AUTOSCALING_GROUP_ELB_HEALTHCHECK_REQUIRED(cls) -> builtins.str:
        '''Checks whether your Auto Scaling groups that are associated with a load balancer are using Elastic Load Balancing health checks.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/autoscaling-group-elb-healthcheck-required.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "AUTOSCALING_GROUP_ELB_HEALTHCHECK_REQUIRED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTOSCALING_LAUNCH_CONFIG_HOP_LIMIT")
    def AUTOSCALING_LAUNCH_CONFIG_HOP_LIMIT(cls) -> builtins.str:
        '''Checks the number of network hops that the metadata token can travel.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/autoscaling-launch-config-hop-limit.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "AUTOSCALING_LAUNCH_CONFIG_HOP_LIMIT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTOSCALING_LAUNCH_CONFIG_PUBLIC_IP_DISABLED")
    def AUTOSCALING_LAUNCH_CONFIG_PUBLIC_IP_DISABLED(cls) -> builtins.str:
        '''Checks if Amazon EC2 Auto Scaling groups have public IP addresses enabled through Launch Configurations.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/autoscaling-launch-config-public-ip-disabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "AUTOSCALING_LAUNCH_CONFIG_PUBLIC_IP_DISABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTOSCALING_LAUNCH_TEMPLATE")
    def AUTOSCALING_LAUNCH_TEMPLATE(cls) -> builtins.str:
        '''Checks if an Amazon Elastic Compute Cloud (EC2) Auto Scaling group is created from an EC2 launch template.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/autoscaling-launch-template.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "AUTOSCALING_LAUNCH_TEMPLATE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTOSCALING_LAUNCHCONFIG_REQUIRES_IMDSV2")
    def AUTOSCALING_LAUNCHCONFIG_REQUIRES_IMDSV2(cls) -> builtins.str:
        '''Checks whether only IMDSv2 is enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/autoscaling-launchconfig-requires-imdsv2.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "AUTOSCALING_LAUNCHCONFIG_REQUIRES_IMDSV2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTOSCALING_MULTIPLE_AZ")
    def AUTOSCALING_MULTIPLE_AZ(cls) -> builtins.str:
        '''Checks if the Auto Scaling group spans multiple Availability Zones.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/autoscaling-multiple-az.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "AUTOSCALING_MULTIPLE_AZ"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTOSCALING_MULTIPLE_INSTANCE_TYPES")
    def AUTOSCALING_MULTIPLE_INSTANCE_TYPES(cls) -> builtins.str:
        '''Checks if an Amazon Elastic Compute Cloud (Amazon EC2) Auto Scaling group uses multiple instance types.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/autoscaling-multiple-instance-types.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "AUTOSCALING_MULTIPLE_INSTANCE_TYPES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BACKUP_PLAN_MIN_FREQUENCY_AND_MIN_RETENTION_CHECK")
    def BACKUP_PLAN_MIN_FREQUENCY_AND_MIN_RETENTION_CHECK(cls) -> builtins.str:
        '''Checks if a backup plan has a backup rule that satisfies the required frequency and retention period.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/backup-plan-min-frequency-and-min-retention-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "BACKUP_PLAN_MIN_FREQUENCY_AND_MIN_RETENTION_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BACKUP_RECOVERY_POINT_ENCRYPTED")
    def BACKUP_RECOVERY_POINT_ENCRYPTED(cls) -> builtins.str:
        '''Checks if a recovery point is encrypted.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/backup-recovery-point-encrypted.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "BACKUP_RECOVERY_POINT_ENCRYPTED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BACKUP_RECOVERY_POINT_MANUAL_DELETION_DISABLED")
    def BACKUP_RECOVERY_POINT_MANUAL_DELETION_DISABLED(cls) -> builtins.str:
        '''Checks if a backup vault has an attached resource-based policy which prevents deletion of recovery points.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/backup-recovery-point-manual-deletion-disabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "BACKUP_RECOVERY_POINT_MANUAL_DELETION_DISABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BACKUP_RECOVERY_POINT_MINIMUM_RETENTION_CHECK")
    def BACKUP_RECOVERY_POINT_MINIMUM_RETENTION_CHECK(cls) -> builtins.str:
        '''Checks if a recovery point expires no earlier than after the specified period.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/backup-recovery-point-minimum-retention-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "BACKUP_RECOVERY_POINT_MINIMUM_RETENTION_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BEANSTALK_ENHANCED_HEALTH_REPORTING_ENABLED")
    def BEANSTALK_ENHANCED_HEALTH_REPORTING_ENABLED(cls) -> builtins.str:
        '''Checks if an AWS Elastic Beanstalk environment is configured for enhanced health reporting.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/beanstalk-enhanced-health-reporting-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "BEANSTALK_ENHANCED_HEALTH_REPORTING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLB_DESYNC_MODE_CHECK")
    def CLB_DESYNC_MODE_CHECK(cls) -> builtins.str:
        '''Checks if Classic Load Balancers (CLB) are configured with a user defined Desync mitigation mode.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/clb-desync-mode-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLB_DESYNC_MODE_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLB_MULTIPLE_AZ")
    def CLB_MULTIPLE_AZ(cls) -> builtins.str:
        '''Checks if a Classic Load Balancer spans multiple Availability Zones (AZs).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/clb-multiple-az.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLB_MULTIPLE_AZ"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_TRAIL_CLOUD_WATCH_LOGS_ENABLED")
    def CLOUD_TRAIL_CLOUD_WATCH_LOGS_ENABLED(cls) -> builtins.str:
        '''Checks whether AWS CloudTrail trails are configured to send logs to Amazon CloudWatch Logs.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloud-trail-cloud-watch-logs-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUD_TRAIL_CLOUD_WATCH_LOGS_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_TRAIL_ENABLED")
    def CLOUD_TRAIL_ENABLED(cls) -> builtins.str:
        '''Checks whether AWS CloudTrail is enabled in your AWS account.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudtrail-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUD_TRAIL_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_TRAIL_ENCRYPTION_ENABLED")
    def CLOUD_TRAIL_ENCRYPTION_ENABLED(cls) -> builtins.str:
        '''Checks whether AWS CloudTrail is configured to use the server side encryption (SSE) AWS Key Management Service (AWS KMS) customer master key (CMK) encryption.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloud-trail-encryption-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUD_TRAIL_ENCRYPTION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD_TRAIL_LOG_FILE_VALIDATION_ENABLED")
    def CLOUD_TRAIL_LOG_FILE_VALIDATION_ENABLED(cls) -> builtins.str:
        '''Checks whether AWS CloudTrail creates a signed digest file with logs.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloud-trail-log-file-validation-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUD_TRAIL_LOG_FILE_VALIDATION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFORMATION_STACK_DRIFT_DETECTION_CHECK")
    def CLOUDFORMATION_STACK_DRIFT_DETECTION_CHECK(cls) -> builtins.str:
        '''Checks whether an AWS CloudFormation stack's actual configuration differs, or has drifted, from it's expected configuration.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudformation-stack-drift-detection-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDFORMATION_STACK_DRIFT_DETECTION_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFORMATION_STACK_NOTIFICATION_CHECK")
    def CLOUDFORMATION_STACK_NOTIFICATION_CHECK(cls) -> builtins.str:
        '''Checks whether your CloudFormation stacks are sending event notifications to an SNS topic.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudformation-stack-notification-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDFORMATION_STACK_NOTIFICATION_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFRONT_ACCESSLOGS_ENABLED")
    def CLOUDFRONT_ACCESSLOGS_ENABLED(cls) -> builtins.str:
        '''Checks if Amazon CloudFront distributions are configured to capture information from Amazon Simple Storage Service (Amazon S3) server access logs.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudfront-accesslogs-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDFRONT_ACCESSLOGS_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFRONT_ASSOCIATED_WITH_WAF")
    def CLOUDFRONT_ASSOCIATED_WITH_WAF(cls) -> builtins.str:
        '''Checks if Amazon CloudFront distributions are associated with either WAF or WAFv2 web access control lists (ACLs).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudfront-associated-with-waf.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDFRONT_ASSOCIATED_WITH_WAF"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFRONT_CUSTOM_SSL_CERTIFICATE")
    def CLOUDFRONT_CUSTOM_SSL_CERTIFICATE(cls) -> builtins.str:
        '''Checks if the certificate associated with an Amazon CloudFront distribution is the default Secure Sockets Layer (SSL) certificate.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudfront-custom-ssl-certificate.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDFRONT_CUSTOM_SSL_CERTIFICATE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFRONT_DEFAULT_ROOT_OBJECT_CONFIGURED")
    def CLOUDFRONT_DEFAULT_ROOT_OBJECT_CONFIGURED(cls) -> builtins.str:
        '''Checks if an Amazon CloudFront distribution is configured to return a specific object that is the default root object.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudfront-default-root-object-configured.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDFRONT_DEFAULT_ROOT_OBJECT_CONFIGURED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFRONT_NO_DEPRECATED_SSL_PROTOCOLS")
    def CLOUDFRONT_NO_DEPRECATED_SSL_PROTOCOLS(cls) -> builtins.str:
        '''Checks if CloudFront distributions are using deprecated SSL protocols for HTTPS communication between CloudFront edge locations and custom origins.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudfront-no-deprecated-ssl-protocols.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDFRONT_NO_DEPRECATED_SSL_PROTOCOLS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFRONT_ORIGIN_ACCESS_IDENTITY_ENABLED")
    def CLOUDFRONT_ORIGIN_ACCESS_IDENTITY_ENABLED(cls) -> builtins.str:
        '''Checks that Amazon CloudFront distribution with Amazon S3 Origin type has Origin Access Identity (OAI) configured.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudfront-origin-access-identity-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDFRONT_ORIGIN_ACCESS_IDENTITY_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFRONT_ORIGIN_FAILOVER_ENABLED")
    def CLOUDFRONT_ORIGIN_FAILOVER_ENABLED(cls) -> builtins.str:
        '''Checks whether an origin group is configured for the distribution of at least 2 origins in the origin group for Amazon CloudFront.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudfront-origin-failover-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDFRONT_ORIGIN_FAILOVER_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFRONT_SECURITY_POLICY_CHECK")
    def CLOUDFRONT_SECURITY_POLICY_CHECK(cls) -> builtins.str:
        '''Checks if Amazon CloudFront distributions are using a minimum security policy and cipher suite of TLSv1.2 or greater for viewer connections.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudfront-security-policy-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDFRONT_SECURITY_POLICY_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFRONT_SNI_ENABLED")
    def CLOUDFRONT_SNI_ENABLED(cls) -> builtins.str:
        '''Checks if Amazon CloudFront distributions are using a custom SSL certificate and are configured to use SNI to serve HTTPS requests.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudfront-sni-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDFRONT_SNI_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFRONT_TRAFFIC_TO_ORIGIN_ENCRYPTED")
    def CLOUDFRONT_TRAFFIC_TO_ORIGIN_ENCRYPTED(cls) -> builtins.str:
        '''Checks if Amazon CloudFront distributions are encrypting traffic to custom origins.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudfront-traffic-to-origin-encrypted.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDFRONT_TRAFFIC_TO_ORIGIN_ENCRYPTED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFRONT_VIEWER_POLICY_HTTPS")
    def CLOUDFRONT_VIEWER_POLICY_HTTPS(cls) -> builtins.str:
        '''Checks whether your Amazon CloudFront distributions use HTTPS (directly or via a redirection).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudfront-viewer-policy-https.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDFRONT_VIEWER_POLICY_HTTPS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDTRAIL_MULTI_REGION_ENABLED")
    def CLOUDTRAIL_MULTI_REGION_ENABLED(cls) -> builtins.str:
        '''Checks that there is at least one multi-region AWS CloudTrail.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/multi-region-cloudtrail-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDTRAIL_MULTI_REGION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDTRAIL_S3_DATAEVENTS_ENABLED")
    def CLOUDTRAIL_S3_DATAEVENTS_ENABLED(cls) -> builtins.str:
        '''Checks whether at least one AWS CloudTrail trail is logging Amazon S3 data events for all S3 buckets.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudtrail-s3-dataevents-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDTRAIL_S3_DATAEVENTS_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDTRAIL_SECURITY_TRAIL_ENABLED")
    def CLOUDTRAIL_SECURITY_TRAIL_ENABLED(cls) -> builtins.str:
        '''Checks that there is at least one AWS CloudTrail trail defined with security best practices.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudtrail-security-trail-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDTRAIL_SECURITY_TRAIL_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDWATCH_ALARM_ACTION_CHECK")
    def CLOUDWATCH_ALARM_ACTION_CHECK(cls) -> builtins.str:
        '''Checks whether CloudWatch alarms have at least one alarm action, one INSUFFICIENT_DATA action, or one OK action enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudwatch-alarm-action-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDWATCH_ALARM_ACTION_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDWATCH_ALARM_ACTION_ENABLED_CHECK")
    def CLOUDWATCH_ALARM_ACTION_ENABLED_CHECK(cls) -> builtins.str:
        '''Checks if Amazon CloudWatch alarms actions are in enabled state.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudwatch-alarm-action-enabled-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDWATCH_ALARM_ACTION_ENABLED_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDWATCH_ALARM_RESOURCE_CHECK")
    def CLOUDWATCH_ALARM_RESOURCE_CHECK(cls) -> builtins.str:
        '''Checks whether the specified resource type has a CloudWatch alarm for the specified metric.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudwatch-alarm-resource-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDWATCH_ALARM_RESOURCE_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDWATCH_ALARM_SETTINGS_CHECK")
    def CLOUDWATCH_ALARM_SETTINGS_CHECK(cls) -> builtins.str:
        '''Checks whether CloudWatch alarms with the given metric name have the specified settings.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudwatch-alarm-settings-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDWATCH_ALARM_SETTINGS_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDWATCH_LOG_GROUP_ENCRYPTED")
    def CLOUDWATCH_LOG_GROUP_ENCRYPTED(cls) -> builtins.str:
        '''Checks whether a log group in Amazon CloudWatch Logs is encrypted with a AWS Key Management Service (KMS) managed Customer Master Keys (CMK).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudwatch-log-group-encrypted.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDWATCH_LOG_GROUP_ENCRYPTED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CMK_BACKING_KEY_ROTATION_ENABLED")
    def CMK_BACKING_KEY_ROTATION_ENABLED(cls) -> builtins.str:
        '''Checks that key rotation is enabled for each key and matches to the key ID of the customer created customer master key (CMK).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cmk-backing-key-rotation-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CMK_BACKING_KEY_ROTATION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODEBUILD_PROJECT_ARTIFACT_ENCRYPTION")
    def CODEBUILD_PROJECT_ARTIFACT_ENCRYPTION(cls) -> builtins.str:
        '''Checks if an AWS CodeBuild project has encryption enabled for all of its artifacts.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/codebuild-project-artifact-encryption.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CODEBUILD_PROJECT_ARTIFACT_ENCRYPTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODEBUILD_PROJECT_ENVIRONMENT_PRIVILEGED_CHECK")
    def CODEBUILD_PROJECT_ENVIRONMENT_PRIVILEGED_CHECK(cls) -> builtins.str:
        '''Checks if an AWS CodeBuild project environment has privileged mode enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/codebuild-project-environment-privileged-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CODEBUILD_PROJECT_ENVIRONMENT_PRIVILEGED_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODEBUILD_PROJECT_ENVVAR_AWSCRED_CHECK")
    def CODEBUILD_PROJECT_ENVVAR_AWSCRED_CHECK(cls) -> builtins.str:
        '''Checks whether the project contains environment variables AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/codebuild-project-envvar-awscred-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CODEBUILD_PROJECT_ENVVAR_AWSCRED_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODEBUILD_PROJECT_LOGGING_ENABLED")
    def CODEBUILD_PROJECT_LOGGING_ENABLED(cls) -> builtins.str:
        '''Checks if an AWS CodeBuild project environment has at least one log option enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/codebuild-project-logging-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CODEBUILD_PROJECT_LOGGING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODEBUILD_PROJECT_S3_LOGS_ENCRYPTED")
    def CODEBUILD_PROJECT_S3_LOGS_ENCRYPTED(cls) -> builtins.str:
        '''Checks if a AWS CodeBuild project configured with Amazon S3 Logs has encryption enabled for its logs.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/codebuild-project-s3-logs-encrypted.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CODEBUILD_PROJECT_S3_LOGS_ENCRYPTED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODEBUILD_PROJECT_SOURCE_REPO_URL_CHECK")
    def CODEBUILD_PROJECT_SOURCE_REPO_URL_CHECK(cls) -> builtins.str:
        '''Checks whether the GitHub or Bitbucket source repository URL contains either personal access tokens or user name and password.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/codebuild-project-source-repo-url-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CODEBUILD_PROJECT_SOURCE_REPO_URL_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODEDEPLOY_AUTO_ROLLBACK_MONITOR_ENABLED")
    def CODEDEPLOY_AUTO_ROLLBACK_MONITOR_ENABLED(cls) -> builtins.str:
        '''Checks if the deployment group is configured with automatic deployment rollback and deployment monitoring with alarms attached.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/codedeploy-auto-rollback-monitor-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CODEDEPLOY_AUTO_ROLLBACK_MONITOR_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODEDEPLOY_EC2_MINIMUM_HEALTHY_HOSTS_CONFIGURED")
    def CODEDEPLOY_EC2_MINIMUM_HEALTHY_HOSTS_CONFIGURED(cls) -> builtins.str:
        '''Checks if the deployment group for EC2/On-Premises Compute Platform is configured with a minimum healthy hosts fleet percentage or host count greater than or equal to the input threshold.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/codedeploy-ec2-minimum-healthy-hosts-configured.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CODEDEPLOY_EC2_MINIMUM_HEALTHY_HOSTS_CONFIGURED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODEDEPLOY_LAMBDA_ALLATONCE_TRAFFIC_SHIFT_DISABLED")
    def CODEDEPLOY_LAMBDA_ALLATONCE_TRAFFIC_SHIFT_DISABLED(cls) -> builtins.str:
        '''Checks if the deployment group for Lambda Compute Platform is not using the default deployment configuration.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/codedeploy-lambda-allatonce-traffic-shift-disabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CODEDEPLOY_LAMBDA_ALLATONCE_TRAFFIC_SHIFT_DISABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODEPIPELINE_DEPLOYMENT_COUNT_CHECK")
    def CODEPIPELINE_DEPLOYMENT_COUNT_CHECK(cls) -> builtins.str:
        '''Checks whether the first deployment stage of the AWS CodePipeline performs more than one deployment.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/codepipeline-deployment-count-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CODEPIPELINE_DEPLOYMENT_COUNT_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODEPIPELINE_REGION_FANOUT_CHECK")
    def CODEPIPELINE_REGION_FANOUT_CHECK(cls) -> builtins.str:
        '''Checks whether each stage in the AWS CodePipeline deploys to more than N times the number of the regions the AWS CodePipeline has deployed in all the previous combined stages, where N is the region fanout number.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/codepipeline-region-fanout-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CODEPIPELINE_REGION_FANOUT_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CW_LOGGROUP_RETENTION_PERIOD_CHECK")
    def CW_LOGGROUP_RETENTION_PERIOD_CHECK(cls) -> builtins.str:
        '''Checks whether Amazon CloudWatch LogGroup retention period is set to specific number of days.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/cw-loggroup-retention-period-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CW_LOGGROUP_RETENTION_PERIOD_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DAX_ENCRYPTION_ENABLED")
    def DAX_ENCRYPTION_ENABLED(cls) -> builtins.str:
        '''Checks that DynamoDB Accelerator (DAX) clusters are encrypted.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/dax-encryption-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "DAX_ENCRYPTION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DMS_REPLICATION_NOT_PUBLIC")
    def DMS_REPLICATION_NOT_PUBLIC(cls) -> builtins.str:
        '''Checks whether AWS Database Migration Service replication instances are public.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/dms-replication-not-public.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "DMS_REPLICATION_NOT_PUBLIC"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DYNAMODB_AUTOSCALING_ENABLED")
    def DYNAMODB_AUTOSCALING_ENABLED(cls) -> builtins.str:
        '''Checks whether Auto Scaling or On-Demand is enabled on your DynamoDB tables and/or global secondary indexes.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/dynamodb-autoscaling-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "DYNAMODB_AUTOSCALING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DYNAMODB_IN_BACKUP_PLAN")
    def DYNAMODB_IN_BACKUP_PLAN(cls) -> builtins.str:
        '''Checks whether Amazon DynamoDB table is present in AWS Backup plans.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/dynamodb-in-backup-plan.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "DYNAMODB_IN_BACKUP_PLAN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DYNAMODB_LAST_BACKUP_RECOVERY_POINT_CREATED")
    def DYNAMODB_LAST_BACKUP_RECOVERY_POINT_CREATED(cls) -> builtins.str:
        '''Checks if a recovery point was created for Amazon DynamoDB Tables within the specified period.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/dynamodb-last-backup-recovery-point-created.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "DYNAMODB_LAST_BACKUP_RECOVERY_POINT_CREATED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DYNAMODB_PITR_ENABLED")
    def DYNAMODB_PITR_ENABLED(cls) -> builtins.str:
        '''Checks that point in time recovery (PITR) is enabled for Amazon DynamoDB tables.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/dynamodb-pitr-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "DYNAMODB_PITR_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DYNAMODB_RESOURCES_PROTECTED_BY_BACKUP_PLAN")
    def DYNAMODB_RESOURCES_PROTECTED_BY_BACKUP_PLAN(cls) -> builtins.str:
        '''Checks if Amazon DynamoDB tables are protected by a backup plan.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/dynamodb-resources-protected-by-backup-plan.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "DYNAMODB_RESOURCES_PROTECTED_BY_BACKUP_PLAN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DYNAMODB_TABLE_ENCRYPTED_KMS")
    def DYNAMODB_TABLE_ENCRYPTED_KMS(cls) -> builtins.str:
        '''Checks whether Amazon DynamoDB table is encrypted with AWS Key Management Service (KMS).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/dynamodb-table-encrypted-kms.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "DYNAMODB_TABLE_ENCRYPTED_KMS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DYNAMODB_TABLE_ENCRYPTION_ENABLED")
    def DYNAMODB_TABLE_ENCRYPTION_ENABLED(cls) -> builtins.str:
        '''Checks whether the Amazon DynamoDB tables are encrypted and checks their status.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/dynamodb-table-encryption-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "DYNAMODB_TABLE_ENCRYPTION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DYNAMODB_THROUGHPUT_LIMIT_CHECK")
    def DYNAMODB_THROUGHPUT_LIMIT_CHECK(cls) -> builtins.str:
        '''Checks whether provisioned DynamoDB throughput is approaching the maximum limit for your account.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/dynamodb-throughput-limit-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "DYNAMODB_THROUGHPUT_LIMIT_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EBS_ENCRYPTED_VOLUMES")
    def EBS_ENCRYPTED_VOLUMES(cls) -> builtins.str:
        '''Checks whether the EBS volumes that are in an attached state are encrypted.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/encrypted-volumes.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EBS_ENCRYPTED_VOLUMES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EBS_IN_BACKUP_PLAN")
    def EBS_IN_BACKUP_PLAN(cls) -> builtins.str:
        '''Checks if Amazon Elastic Block Store (Amazon EBS) volumes are added in backup plans of AWS Backup.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ebs-in-backup-plan.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EBS_IN_BACKUP_PLAN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EBS_OPTIMIZED_INSTANCE")
    def EBS_OPTIMIZED_INSTANCE(cls) -> builtins.str:
        '''Checks whether EBS optimization is enabled for your EC2 instances that can be EBS-optimized.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ebs-optimized-instance.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EBS_OPTIMIZED_INSTANCE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EBS_RESOURCES_PROTECTED_BY_BACKUP_PLAN")
    def EBS_RESOURCES_PROTECTED_BY_BACKUP_PLAN(cls) -> builtins.str:
        '''Checks if Amazon Elastic Block Store (Amazon EBS) volumes are protected by a backup plan.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ebs-resources-protected-by-backup-plan.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EBS_RESOURCES_PROTECTED_BY_BACKUP_PLAN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EBS_SNAPSHOT_PUBLIC_RESTORABLE_CHECK")
    def EBS_SNAPSHOT_PUBLIC_RESTORABLE_CHECK(cls) -> builtins.str:
        '''Checks whether Amazon Elastic Block Store snapshots are not publicly restorable.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ebs-snapshot-public-restorable-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EBS_SNAPSHOT_PUBLIC_RESTORABLE_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_DESIRED_INSTANCE_TENANCY")
    def EC2_DESIRED_INSTANCE_TENANCY(cls) -> builtins.str:
        '''Checks instances for specified tenancy.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/desired-instance-tenancy.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_DESIRED_INSTANCE_TENANCY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_DESIRED_INSTANCE_TYPE")
    def EC2_DESIRED_INSTANCE_TYPE(cls) -> builtins.str:
        '''Checks whether your EC2 instances are of the specified instance types.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/desired-instance-type.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_DESIRED_INSTANCE_TYPE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_EBS_ENCRYPTION_BY_DEFAULT")
    def EC2_EBS_ENCRYPTION_BY_DEFAULT(cls) -> builtins.str:
        '''Check that Amazon Elastic Block Store (EBS) encryption is enabled by default.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-ebs-encryption-by-default.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_EBS_ENCRYPTION_BY_DEFAULT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_IMDSV2_CHECK")
    def EC2_IMDSV2_CHECK(cls) -> builtins.str:
        '''Checks whether your Amazon Elastic Compute Cloud (Amazon EC2) instance metadata version is configured with Instance Metadata Service Version 2 (IMDSv2).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-imdsv2-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_IMDSV2_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_INSTANCE_DETAILED_MONITORING_ENABLED")
    def EC2_INSTANCE_DETAILED_MONITORING_ENABLED(cls) -> builtins.str:
        '''Checks whether detailed monitoring is enabled for EC2 instances.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-instance-detailed-monitoring-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_INSTANCE_DETAILED_MONITORING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_INSTANCE_MANAGED_BY_SSM")
    def EC2_INSTANCE_MANAGED_BY_SSM(cls) -> builtins.str:
        '''Checks whether the Amazon EC2 instances in your account are managed by AWS Systems Manager.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-instance-managed-by-systems-manager.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_INSTANCE_MANAGED_BY_SSM"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_INSTANCE_MULTIPLE_ENI_CHECK")
    def EC2_INSTANCE_MULTIPLE_ENI_CHECK(cls) -> builtins.str:
        '''Checks if Amazon Elastic Compute Cloud (Amazon EC2) uses multiple ENIs (Elastic Network Interfaces) or Elastic Fabric Adapters (EFAs).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-instance-multiple-eni-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_INSTANCE_MULTIPLE_ENI_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_INSTANCE_NO_PUBLIC_IP")
    def EC2_INSTANCE_NO_PUBLIC_IP(cls) -> builtins.str:
        '''Checks whether Amazon Elastic Compute Cloud (Amazon EC2) instances have a public IP association.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-instance-no-public-ip.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_INSTANCE_NO_PUBLIC_IP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_INSTANCE_PROFILE_ATTACHED")
    def EC2_INSTANCE_PROFILE_ATTACHED(cls) -> builtins.str:
        '''Checks if an Amazon Elastic Compute Cloud (Amazon EC2) instance has an Identity and Access Management (IAM) profile attached to it.

        This rule is NON_COMPLIANT if no IAM profile is
        attached to the Amazon EC2 instance.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-instance-profile-attached.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_INSTANCE_PROFILE_ATTACHED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_INSTANCES_IN_VPC")
    def EC2_INSTANCES_IN_VPC(cls) -> builtins.str:
        '''Checks whether your EC2 instances belong to a virtual private cloud (VPC).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-instances-in-vpc.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_INSTANCES_IN_VPC"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_LAST_BACKUP_RECOVERY_POINT_CREATED")
    def EC2_LAST_BACKUP_RECOVERY_POINT_CREATED(cls) -> builtins.str:
        '''Checks if a recovery point was created for Amazon Elastic Compute Cloud (Amazon EC2) instances.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-last-backup-recovery-point-created.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_LAST_BACKUP_RECOVERY_POINT_CREATED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_MANAGED_INSTANCE_APPLICATIONS_BLOCKED")
    def EC2_MANAGED_INSTANCE_APPLICATIONS_BLOCKED(cls) -> builtins.str:
        '''Checks that none of the specified applications are installed on the instance.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-managedinstance-applications-blacklisted.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_MANAGED_INSTANCE_APPLICATIONS_BLOCKED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_MANAGED_INSTANCE_APPLICATIONS_REQUIRED")
    def EC2_MANAGED_INSTANCE_APPLICATIONS_REQUIRED(cls) -> builtins.str:
        '''Checks whether all of the specified applications are installed on the instance.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-managedinstance-applications-required.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_MANAGED_INSTANCE_APPLICATIONS_REQUIRED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_MANAGED_INSTANCE_ASSOCIATION_COMPLIANCE_STATUS_CHECK")
    def EC2_MANAGED_INSTANCE_ASSOCIATION_COMPLIANCE_STATUS_CHECK(cls) -> builtins.str:
        '''Checks whether the compliance status of AWS Systems Manager association compliance is COMPLIANT or NON_COMPLIANT after the association execution on the instance.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-managedinstance-association-compliance-status-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_MANAGED_INSTANCE_ASSOCIATION_COMPLIANCE_STATUS_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_MANAGED_INSTANCE_INVENTORY_BLOCKED")
    def EC2_MANAGED_INSTANCE_INVENTORY_BLOCKED(cls) -> builtins.str:
        '''Checks whether instances managed by AWS Systems Manager are configured to collect blocked inventory types.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-managedinstance-inventory-blacklisted.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_MANAGED_INSTANCE_INVENTORY_BLOCKED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_MANAGED_INSTANCE_PATCH_COMPLIANCE_STATUS_CHECK")
    def EC2_MANAGED_INSTANCE_PATCH_COMPLIANCE_STATUS_CHECK(cls) -> builtins.str:
        '''Checks whether the compliance status of the Amazon EC2 Systems Manager patch compliance is COMPLIANT or NON_COMPLIANT after the patch installation on the instance.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-managedinstance-patch-compliance-status-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_MANAGED_INSTANCE_PATCH_COMPLIANCE_STATUS_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_MANAGED_INSTANCE_PLATFORM_CHECK")
    def EC2_MANAGED_INSTANCE_PLATFORM_CHECK(cls) -> builtins.str:
        '''Checks whether EC2 managed instances have the desired configurations.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-managedinstance-platform-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_MANAGED_INSTANCE_PLATFORM_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_NO_AMAZON_KEY_PAIR")
    def EC2_NO_AMAZON_KEY_PAIR(cls) -> builtins.str:
        '''Checks if running Amazon Elastic Compute Cloud (EC2) instances are launched using amazon key pairs.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-no-amazon-key-pair.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_NO_AMAZON_KEY_PAIR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_PARAVIRTUAL_INSTANCE_CHECK")
    def EC2_PARAVIRTUAL_INSTANCE_CHECK(cls) -> builtins.str:
        '''Checks if the virtualization type of an EC2 instance is paravirtual.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-paravirtual-instance-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_PARAVIRTUAL_INSTANCE_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_RESOURCES_PROTECTED_BY_BACKUP_PLAN")
    def EC2_RESOURCES_PROTECTED_BY_BACKUP_PLAN(cls) -> builtins.str:
        '''Checks if Amazon Elastic Compute Cloud (Amazon EC2) instances are protected by a backup plan.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-resources-protected-by-backup-plan.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_RESOURCES_PROTECTED_BY_BACKUP_PLAN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_SECURITY_GROUP_ATTACHED_TO_ENI")
    def EC2_SECURITY_GROUP_ATTACHED_TO_ENI(cls) -> builtins.str:
        '''Checks that security groups are attached to Amazon Elastic Compute Cloud (Amazon EC2) instances or to an elastic network interface.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-security-group-attached-to-eni.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_SECURITY_GROUP_ATTACHED_TO_ENI"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_SECURITY_GROUP_ATTACHED_TO_ENI_PERIODIC")
    def EC2_SECURITY_GROUP_ATTACHED_TO_ENI_PERIODIC(cls) -> builtins.str:
        '''Checks if non-default security groups are attached to Elastic network interfaces (ENIs).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-security-group-attached-to-eni-periodic.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_SECURITY_GROUP_ATTACHED_TO_ENI_PERIODIC"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_SECURITY_GROUPS_INCOMING_SSH_DISABLED")
    def EC2_SECURITY_GROUPS_INCOMING_SSH_DISABLED(cls) -> builtins.str:
        '''Checks whether the incoming SSH traffic for the security groups is accessible.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/restricted-ssh.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_SECURITY_GROUPS_INCOMING_SSH_DISABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_SECURITY_GROUPS_RESTRICTED_INCOMING_TRAFFIC")
    def EC2_SECURITY_GROUPS_RESTRICTED_INCOMING_TRAFFIC(cls) -> builtins.str:
        '''Checks whether the security groups in use do not allow unrestricted incoming TCP traffic to the specified ports.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/restricted-common-ports.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_SECURITY_GROUPS_RESTRICTED_INCOMING_TRAFFIC"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_STOPPED_INSTANCE")
    def EC2_STOPPED_INSTANCE(cls) -> builtins.str:
        '''Checks whether there are instances stopped for more than the allowed number of days.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-stopped-instance.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_STOPPED_INSTANCE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_TOKEN_HOP_LIMIT_CHECK")
    def EC2_TOKEN_HOP_LIMIT_CHECK(cls) -> builtins.str:
        '''Checks if an Amazon Elastic Compute Cloud (EC2) instance metadata has a specified token hop limit that is below the desired limit.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-token-hop-limit-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_TOKEN_HOP_LIMIT_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_TRANSIT_GATEWAY_AUTO_VPC_ATTACH_DISABLED")
    def EC2_TRANSIT_GATEWAY_AUTO_VPC_ATTACH_DISABLED(cls) -> builtins.str:
        '''Checks if Amazon Elastic Compute Cloud (Amazon EC2) Transit Gateways have 'AutoAcceptSharedAttachments' enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-transit-gateway-auto-vpc-attach-disabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_TRANSIT_GATEWAY_AUTO_VPC_ATTACH_DISABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_VOLUME_IECS_TASK_DEFINITION_USER_FOR_HOST_MODE_CHECKNUSE_CHECK")
    def EC2_VOLUME_IECS_TASK_DEFINITION_USER_FOR_HOST_MODE_CHECKNUSE_CHECK(
        cls,
    ) -> builtins.str:
        '''Checks if an Amazon Elastic Container Service (Amazon ECS) task definition with host networking mode has 'privileged' or 'user' container definitions.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-volume-inuse-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_VOLUME_IECS_TASK_DEFINITION_USER_FOR_HOST_MODE_CHECKNUSE_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_VOLUME_INUSE_CHECK")
    def EC2_VOLUME_INUSE_CHECK(cls) -> builtins.str:
        '''Checks whether EBS volumes are attached to EC2 instances.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-volume-inuse-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EC2_VOLUME_INUSE_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ECR_PRIVATE_IMAGE_SCANNING_ENABLED")
    def ECR_PRIVATE_IMAGE_SCANNING_ENABLED(cls) -> builtins.str:
        '''Checks if a private Amazon Elastic Container Registry (ECR) repository has image scanning enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ecr-private-image-scanning-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ECR_PRIVATE_IMAGE_SCANNING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ECR_PRIVATE_LIFECYCLE_POLICY_CONFIGURED")
    def ECR_PRIVATE_LIFECYCLE_POLICY_CONFIGURED(cls) -> builtins.str:
        '''Checks if a private Amazon Elastic Container Registry (ECR) repository has at least one lifecycle policy configured.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ecr-private-lifecycle-policy-configured.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ECR_PRIVATE_LIFECYCLE_POLICY_CONFIGURED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ECR_PRIVATE_TAG_IMMUTABILITY_ENABLED")
    def ECR_PRIVATE_TAG_IMMUTABILITY_ENABLED(cls) -> builtins.str:
        '''Checks if a private Amazon Elastic Container Registry (ECR) repository has tag immutability enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ecr-private-tag-immutability-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ECR_PRIVATE_TAG_IMMUTABILITY_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ECS_AWSVPC_NETWORKING_ENABLED")
    def ECS_AWSVPC_NETWORKING_ENABLED(cls) -> builtins.str:
        '''Checks if the networking mode for active ECSTaskDefinitions is set to ‘awsvpc’.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ecs-awsvpc-networking-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ECS_AWSVPC_NETWORKING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ECS_CONTAINER_INSIGHTS_ENABLED")
    def ECS_CONTAINER_INSIGHTS_ENABLED(cls) -> builtins.str:
        '''Checks if Amazon Elastic Container Service clusters have container insights enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ecs-container-insights-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ECS_CONTAINER_INSIGHTS_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ECS_CONTAINERS_NONPRIVILEGED")
    def ECS_CONTAINERS_NONPRIVILEGED(cls) -> builtins.str:
        '''Checks if the privileged parameter in the container definition of ECSTaskDefinitions is set to ‘true’.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-instances-in-vpc.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ECS_CONTAINERS_NONPRIVILEGED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ECS_CONTAINERS_READONLY_ACCESS")
    def ECS_CONTAINERS_READONLY_ACCESS(cls) -> builtins.str:
        '''Checks if Amazon Elastic Container Service (Amazon ECS) Containers only have read-only access to its root filesystems.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ecs-containers-readonly-access.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ECS_CONTAINERS_READONLY_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ECS_FARGATE_LATEST_PLATFORM_VERSION")
    def ECS_FARGATE_LATEST_PLATFORM_VERSION(cls) -> builtins.str:
        '''Checks if Amazon Elastic Container Service (ECS) Fargate Services is running on the latest Fargate platform version.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ecs-fargate-latest-platform-version.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ECS_FARGATE_LATEST_PLATFORM_VERSION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ECS_NO_ENVIRONMENT_SECRETS")
    def ECS_NO_ENVIRONMENT_SECRETS(cls) -> builtins.str:
        '''Checks if secrets are passed as container environment variables.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ecs-no-environment-secrets.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ECS_NO_ENVIRONMENT_SECRETS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ECS_TASK_DEFINITION_LOG_CONFIGURATION")
    def ECS_TASK_DEFINITION_LOG_CONFIGURATION(cls) -> builtins.str:
        '''Checks if logConfiguration is set on active ECS Task Definitions.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ecs-task-definition-log-configuration.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ECS_TASK_DEFINITION_LOG_CONFIGURATION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ECS_TASK_DEFINITION_MEMORY_HARD_LIMIT")
    def ECS_TASK_DEFINITION_MEMORY_HARD_LIMIT(cls) -> builtins.str:
        '''Checks if Amazon Elastic Container Service (ECS) task definitions have a set memory limit for its container definitions.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ecs-task-definition-memory-hard-limit.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ECS_TASK_DEFINITION_MEMORY_HARD_LIMIT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ECS_TASK_DEFINITION_NONROOT_USER")
    def ECS_TASK_DEFINITION_NONROOT_USER(cls) -> builtins.str:
        '''Checks if ECSTaskDefinitions specify a user for Amazon Elastic Container Service (Amazon ECS) EC2 launch type containers to run on.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ecs-task-definition-nonroot-user.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ECS_TASK_DEFINITION_NONROOT_USER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ECS_TASK_DEFINITION_PID_MODE_CHECK")
    def ECS_TASK_DEFINITION_PID_MODE_CHECK(cls) -> builtins.str:
        '''Checks if ECSTaskDefinitions are configured to share a host’s process namespace with its Amazon Elastic Container Service (Amazon ECS) containers.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-stopped-instance.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ECS_TASK_DEFINITION_PID_MODE_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EFS_ACCESS_POINT_ENFORCE_ROOT_DIRECTORY")
    def EFS_ACCESS_POINT_ENFORCE_ROOT_DIRECTORY(cls) -> builtins.str:
        '''Checks if Amazon Elastic File System (Amazon EFS) access points are configured to enforce a root directory.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/efs-access-point-enforce-root-directory.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EFS_ACCESS_POINT_ENFORCE_ROOT_DIRECTORY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EFS_ACCESS_POINT_ENFORCE_USER_IDENTITY")
    def EFS_ACCESS_POINT_ENFORCE_USER_IDENTITY(cls) -> builtins.str:
        '''Checks if Amazon Elastic File System (Amazon EFS) access points are configured to enforce a user identity.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ec2-volume-inuse-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EFS_ACCESS_POINT_ENFORCE_USER_IDENTITY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EFS_ENCRYPTED_CHECK")
    def EFS_ENCRYPTED_CHECK(cls) -> builtins.str:
        '''hecks whether Amazon Elastic File System (Amazon EFS) is configured to encrypt the file data using AWS Key Management Service (AWS KMS).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/efs-encrypted-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EFS_ENCRYPTED_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EFS_IN_BACKUP_PLAN")
    def EFS_IN_BACKUP_PLAN(cls) -> builtins.str:
        '''Checks whether Amazon Elastic File System (Amazon EFS) file systems are added in the backup plans of AWS Backup.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/efs-in-backup-plan.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EFS_IN_BACKUP_PLAN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EFS_LAST_BACKUP_RECOVERY_POINT_CREATED")
    def EFS_LAST_BACKUP_RECOVERY_POINT_CREATED(cls) -> builtins.str:
        '''Checks if a recovery point was created for Amazon Elastic File System (Amazon EFS) File Systems.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/efs-last-backup-recovery-point-created.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EFS_LAST_BACKUP_RECOVERY_POINT_CREATED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EFS_RESOURCES_PROTECTED_BY_BACKUP_PLAN")
    def EFS_RESOURCES_PROTECTED_BY_BACKUP_PLAN(cls) -> builtins.str:
        '''Checks if Amazon Elastic File System (Amazon EFS) File Systems are protected by a backup plan.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/efs-resources-protected-by-backup-plan.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EFS_RESOURCES_PROTECTED_BY_BACKUP_PLAN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EIP_ATTACHED")
    def EIP_ATTACHED(cls) -> builtins.str:
        '''Checks whether all Elastic IP addresses that are allocated to a VPC are attached to EC2 instances or in-use elastic network interfaces (ENIs).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/eip-attached.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EIP_ATTACHED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EKS_CLUSTER_OLDEST_SUPPORTED_VERSION")
    def EKS_CLUSTER_OLDEST_SUPPORTED_VERSION(cls) -> builtins.str:
        '''Checks if an Amazon Elastic Kubernetes Service (EKS) cluster is running the oldest supported version.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/eks-cluster-oldest-supported-version.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EKS_CLUSTER_OLDEST_SUPPORTED_VERSION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EKS_CLUSTER_SUPPORTED_VERSION")
    def EKS_CLUSTER_SUPPORTED_VERSION(cls) -> builtins.str:
        '''Checks if an Amazon Elastic Kubernetes Service (EKS) cluster is running a supported Kubernetes version.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/eks-cluster-supported-version.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EKS_CLUSTER_SUPPORTED_VERSION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EKS_ENDPOINT_NO_PUBLIC_ACCESS")
    def EKS_ENDPOINT_NO_PUBLIC_ACCESS(cls) -> builtins.str:
        '''Checks whether Amazon Elastic Kubernetes Service (Amazon EKS) endpoint is not publicly accessible.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/eks-endpoint-no-public-access.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EKS_ENDPOINT_NO_PUBLIC_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EKS_SECRETS_ENCRYPTED")
    def EKS_SECRETS_ENCRYPTED(cls) -> builtins.str:
        '''Checks whether Amazon Elastic Kubernetes Service clusters are configured to have Kubernetes secrets encrypted using AWS Key Management Service (KMS) keys.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/eks-secrets-encrypted.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EKS_SECRETS_ENCRYPTED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTIC_BEANSTALK_MANAGED_UPDATES_ENABLED")
    def ELASTIC_BEANSTALK_MANAGED_UPDATES_ENABLED(cls) -> builtins.str:
        '''Checks if managed platform updates in an AWS Elastic Beanstalk environment is enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/elastic-beanstalk-managed-updates-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ELASTIC_BEANSTALK_MANAGED_UPDATES_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICACHE_REDIS_CLUSTER_AUTOMATIC_BACKUP_CHECK")
    def ELASTICACHE_REDIS_CLUSTER_AUTOMATIC_BACKUP_CHECK(cls) -> builtins.str:
        '''Check if the Amazon ElastiCache Redis clusters have automatic backup turned on.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/elasticache-redis-cluster-automatic-backup-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ELASTICACHE_REDIS_CLUSTER_AUTOMATIC_BACKUP_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_ENCRYPTED_AT_REST")
    def ELASTICSEARCH_ENCRYPTED_AT_REST(cls) -> builtins.str:
        '''Checks whether Amazon Elasticsearch Service (Amazon ES) domains have encryption at rest configuration enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/elasticsearch-encrypted-at-rest.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ELASTICSEARCH_ENCRYPTED_AT_REST"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_IN_VPC_ONLY")
    def ELASTICSEARCH_IN_VPC_ONLY(cls) -> builtins.str:
        '''Checks whether Amazon Elasticsearch Service (Amazon ES) domains are in Amazon Virtual Private Cloud (Amazon VPC).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/elasticsearch-in-vpc-only.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ELASTICSEARCH_IN_VPC_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_NODE_TO_NODE_ENCRYPTION_CHECK")
    def ELASTICSEARCH_NODE_TO_NODE_ENCRYPTION_CHECK(cls) -> builtins.str:
        '''Check that Amazon ElasticSearch Service nodes are encrypted end to end.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/elasticsearch-node-to-node-encryption-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ELASTICSEARCH_NODE_TO_NODE_ENCRYPTION_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELB_ACM_CERTIFICATE_REQUIRED")
    def ELB_ACM_CERTIFICATE_REQUIRED(cls) -> builtins.str:
        '''Checks whether the Classic Load Balancers use SSL certificates provided by AWS Certificate Manager.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/elb-acm-certificate-required.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ELB_ACM_CERTIFICATE_REQUIRED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELB_CROSS_ZONE_LOAD_BALANCING_ENABLED")
    def ELB_CROSS_ZONE_LOAD_BALANCING_ENABLED(cls) -> builtins.str:
        '''Checks if cross-zone load balancing is enabled for the Classic Load Balancers (CLBs).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/elb-cross-zone-load-balancing-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ELB_CROSS_ZONE_LOAD_BALANCING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELB_CUSTOM_SECURITY_POLICY_SSL_CHECK")
    def ELB_CUSTOM_SECURITY_POLICY_SSL_CHECK(cls) -> builtins.str:
        '''Checks whether your Classic Load Balancer SSL listeners are using a custom policy.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/elb-custom-security-policy-ssl-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ELB_CUSTOM_SECURITY_POLICY_SSL_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELB_DELETION_PROTECTION_ENABLED")
    def ELB_DELETION_PROTECTION_ENABLED(cls) -> builtins.str:
        '''Checks whether Elastic Load Balancing has deletion protection enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/elb-deletion-protection-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ELB_DELETION_PROTECTION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELB_LOGGING_ENABLED")
    def ELB_LOGGING_ENABLED(cls) -> builtins.str:
        '''Checks whether the Application Load Balancer and the Classic Load Balancer have logging enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/elb-logging-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ELB_LOGGING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELB_PREDEFINED_SECURITY_POLICY_SSL_CHECK")
    def ELB_PREDEFINED_SECURITY_POLICY_SSL_CHECK(cls) -> builtins.str:
        '''Checks whether your Classic Load Balancer SSL listeners are using a predefined policy.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/elb-predefined-security-policy-ssl-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ELB_PREDEFINED_SECURITY_POLICY_SSL_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELB_TLS_HTTPS_LISTENERS_ONLY")
    def ELB_TLS_HTTPS_LISTENERS_ONLY(cls) -> builtins.str:
        '''Checks whether your Classic Load Balancer is configured with SSL or HTTPS listeners.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/elb-tls-https-listeners-only.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ELB_TLS_HTTPS_LISTENERS_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELBV2_ACM_CERTIFICATE_REQUIRED")
    def ELBV2_ACM_CERTIFICATE_REQUIRED(cls) -> builtins.str:
        '''Checks if Application Load Balancers and Network Load Balancers have listeners that are configured to use certificates from AWS Certificate Manager (ACM).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/elbv2-acm-certificate-required.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ELBV2_ACM_CERTIFICATE_REQUIRED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELBV2_MULTIPLE_AZ")
    def ELBV2_MULTIPLE_AZ(cls) -> builtins.str:
        '''Checks if an Elastic Load Balancer V2 (Application, Network, or Gateway Load Balancer) has registered instances from multiple Availability Zones (AZ's).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/elbv2-multiple-az.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ELBV2_MULTIPLE_AZ"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EMR_KERBEROS_ENABLED")
    def EMR_KERBEROS_ENABLED(cls) -> builtins.str:
        '''Checks that Amazon EMR clusters have Kerberos enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/emr-kerberos-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EMR_KERBEROS_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EMR_MASTER_NO_PUBLIC_IP")
    def EMR_MASTER_NO_PUBLIC_IP(cls) -> builtins.str:
        '''Checks whether Amazon Elastic MapReduce (EMR) clusters' master nodes have public IPs.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/emr-master-no-public-ip.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "EMR_MASTER_NO_PUBLIC_IP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="FMS_SECURITY_GROUP_AUDIT_POLICY_CHECK")
    def FMS_SECURITY_GROUP_AUDIT_POLICY_CHECK(cls) -> builtins.str:
        '''(deprecated) Checks whether the security groups associated inScope resources are compliant with the master security groups at each rule level based on allowSecurityGroup and denySecurityGroup flag.

        :deprecated: Inactive managed rule

        :see: https://docs.aws.amazon.com/config/latest/developerguide/fms-security-group-audit-policy-check.html
        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "FMS_SECURITY_GROUP_AUDIT_POLICY_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="FMS_SECURITY_GROUP_CONTENT_CHECK")
    def FMS_SECURITY_GROUP_CONTENT_CHECK(cls) -> builtins.str:
        '''(deprecated) Checks whether AWS Firewall Manager created security groups content is the same as the master security groups.

        :deprecated: Inactive managed rule

        :see: https://docs.aws.amazon.com/config/latest/developerguide/fms-security-group-content-check.html
        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "FMS_SECURITY_GROUP_CONTENT_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="FMS_SECURITY_GROUP_RESOURCE_ASSOCIATION_CHECK")
    def FMS_SECURITY_GROUP_RESOURCE_ASSOCIATION_CHECK(cls) -> builtins.str:
        '''(deprecated) Checks whether Amazon EC2 or an elastic network interface is associated with AWS Firewall Manager security groups.

        :deprecated: Inactive managed rule

        :see: https://docs.aws.amazon.com/config/latest/developerguide/fms-security-group-resource-association-check.html
        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "FMS_SECURITY_GROUP_RESOURCE_ASSOCIATION_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="FMS_SHIELD_RESOURCE_POLICY_CHECK")
    def FMS_SHIELD_RESOURCE_POLICY_CHECK(cls) -> builtins.str:
        '''Checks whether an Application Load Balancer, Amazon CloudFront distributions, Elastic Load Balancer or Elastic IP has AWS Shield protection.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/fms-shield-resource-policy-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "FMS_SHIELD_RESOURCE_POLICY_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="FMS_WEBACL_RESOURCE_POLICY_CHECK")
    def FMS_WEBACL_RESOURCE_POLICY_CHECK(cls) -> builtins.str:
        '''Checks whether the web ACL is associated with an Application Load Balancer, API Gateway stage, or Amazon CloudFront distributions.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/fms-webacl-resource-policy-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "FMS_WEBACL_RESOURCE_POLICY_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="FMS_WEBACL_RULEGROUP_ASSOCIATION_CHECK")
    def FMS_WEBACL_RULEGROUP_ASSOCIATION_CHECK(cls) -> builtins.str:
        '''Checks that the rule groups associate with the web ACL at the correct priority.

        The correct priority is decided by the rank of the rule groups in the ruleGroups parameter.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/fms-webacl-rulegroup-association-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "FMS_WEBACL_RULEGROUP_ASSOCIATION_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="FSX_LAST_BACKUP_RECOVERY_POINT_CREATED")
    def FSX_LAST_BACKUP_RECOVERY_POINT_CREATED(cls) -> builtins.str:
        '''Checks if a recovery point was created for Amazon FSx File Systems.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/fsx-last-backup-recovery-point-created.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "FSX_LAST_BACKUP_RECOVERY_POINT_CREATED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="FSX_RESOURCES_PROTECTED_BY_BACKUP_PLAN")
    def FSX_RESOURCES_PROTECTED_BY_BACKUP_PLAN(cls) -> builtins.str:
        '''Checks if Amazon FSx File Systems are protected by a backup plan.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/fsx-resources-protected-by-backup-plan.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "FSX_RESOURCES_PROTECTED_BY_BACKUP_PLAN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GUARDDUTY_ENABLED_CENTRALIZED")
    def GUARDDUTY_ENABLED_CENTRALIZED(cls) -> builtins.str:
        '''Checks whether Amazon GuardDuty is enabled in your AWS account and region.

        If you provide an AWS account for centralization,
        the rule evaluates the Amazon GuardDuty results in the centralized account.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/guardduty-enabled-centralized.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "GUARDDUTY_ENABLED_CENTRALIZED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GUARDDUTY_NON_ARCHIVED_FINDINGS")
    def GUARDDUTY_NON_ARCHIVED_FINDINGS(cls) -> builtins.str:
        '''Checks whether the Amazon GuardDuty has findings that are non archived.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/guardduty-non-archived-findings.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "GUARDDUTY_NON_ARCHIVED_FINDINGS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_CUSTOMER_POLICY_BLOCKED_KMS_ACTIONS")
    def IAM_CUSTOMER_POLICY_BLOCKED_KMS_ACTIONS(cls) -> builtins.str:
        '''Checks that the managed AWS Identity and Access Management policies that you create do not allow blocked actions on all AWS AWS KMS keys.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-customer-policy-blocked-kms-actions.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_CUSTOMER_POLICY_BLOCKED_KMS_ACTIONS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_GROUP_HAS_USERS_CHECK")
    def IAM_GROUP_HAS_USERS_CHECK(cls) -> builtins.str:
        '''Checks whether IAM groups have at least one IAM user.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-group-has-users-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_GROUP_HAS_USERS_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_INLINE_POLICY_BLOCKED_KMS_ACTIONS")
    def IAM_INLINE_POLICY_BLOCKED_KMS_ACTIONS(cls) -> builtins.str:
        '''Checks that the inline policies attached to your AWS Identity and Access Management users, roles, and groups do not allow blocked actions on all AWS Key Management Service keys.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-inline-policy-blocked-kms-actions.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_INLINE_POLICY_BLOCKED_KMS_ACTIONS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_NO_INLINE_POLICY_CHECK")
    def IAM_NO_INLINE_POLICY_CHECK(cls) -> builtins.str:
        '''Checks that inline policy feature is not in use.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-no-inline-policy-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_NO_INLINE_POLICY_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_PASSWORD_POLICY")
    def IAM_PASSWORD_POLICY(cls) -> builtins.str:
        '''Checks whether the account password policy for IAM users meets the specified requirements indicated in the parameters.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-password-policy.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_PASSWORD_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_POLICY_BLOCKED_CHECK")
    def IAM_POLICY_BLOCKED_CHECK(cls) -> builtins.str:
        '''Checks whether for each IAM resource, a policy ARN in the input parameter is attached to the IAM resource.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-policy-blacklisted-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_POLICY_BLOCKED_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_POLICY_IN_USE")
    def IAM_POLICY_IN_USE(cls) -> builtins.str:
        '''Checks whether the IAM policy ARN is attached to an IAM user, or an IAM group with one or more IAM users, or an IAM role with one or more trusted entity.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-policy-in-use.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_POLICY_IN_USE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_POLICY_NO_STATEMENTS_WITH_ADMIN_ACCESS")
    def IAM_POLICY_NO_STATEMENTS_WITH_ADMIN_ACCESS(cls) -> builtins.str:
        '''Checks the IAM policies that you create for Allow statements that grant permissions to all actions on all resources.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-policy-no-statements-with-admin-access.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_POLICY_NO_STATEMENTS_WITH_ADMIN_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_POLICY_NO_STATEMENTS_WITH_FULL_ACCESS")
    def IAM_POLICY_NO_STATEMENTS_WITH_FULL_ACCESS(cls) -> builtins.str:
        '''Checks if AWS Identity and Access Management (IAM) policies that you create grant permissions to all actions on individual AWS resources.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-policy-no-statements-with-full-access.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_POLICY_NO_STATEMENTS_WITH_FULL_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_ROLE_MANAGED_POLICY_CHECK")
    def IAM_ROLE_MANAGED_POLICY_CHECK(cls) -> builtins.str:
        '''Checks that AWS Identity and Access Management (IAM) policies in a list of policies are attached to all AWS roles.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-role-managed-policy-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_ROLE_MANAGED_POLICY_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_ROOT_ACCESS_KEY_CHECK")
    def IAM_ROOT_ACCESS_KEY_CHECK(cls) -> builtins.str:
        '''Checks whether the root user access key is available.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-root-access-key-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_ROOT_ACCESS_KEY_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_USER_GROUP_MEMBERSHIP_CHECK")
    def IAM_USER_GROUP_MEMBERSHIP_CHECK(cls) -> builtins.str:
        '''Checks whether IAM users are members of at least one IAM group.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-user-group-membership-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_USER_GROUP_MEMBERSHIP_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_USER_MFA_ENABLED")
    def IAM_USER_MFA_ENABLED(cls) -> builtins.str:
        '''Checks whether the AWS Identity and Access Management users have multi-factor authentication (MFA) enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-user-mfa-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_USER_MFA_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_USER_NO_POLICIES_CHECK")
    def IAM_USER_NO_POLICIES_CHECK(cls) -> builtins.str:
        '''Checks that none of your IAM users have policies attached.

        IAM users must inherit permissions from IAM groups or roles.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-user-no-policies-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_USER_NO_POLICIES_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_USER_UNUSED_CREDENTIALS_CHECK")
    def IAM_USER_UNUSED_CREDENTIALS_CHECK(cls) -> builtins.str:
        '''Checks whether your AWS Identity and Access Management (IAM) users have passwords or active access keys that have not been used within the specified number of days you provided.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/iam-user-unused-credentials-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "IAM_USER_UNUSED_CREDENTIALS_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="INTERNET_GATEWAY_AUTHORIZED_VPC_ONLY")
    def INTERNET_GATEWAY_AUTHORIZED_VPC_ONLY(cls) -> builtins.str:
        '''Checks that Internet gateways (IGWs) are only attached to an authorized Amazon Virtual Private Cloud (VPCs).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/internet-gateway-authorized-vpc-only.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "INTERNET_GATEWAY_AUTHORIZED_VPC_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="KINESIS_STREAM_ENCRYPTED")
    def KINESIS_STREAM_ENCRYPTED(cls) -> builtins.str:
        '''Checks if Amazon Kinesis streams are encrypted at rest with server-side encryption.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/kinesis-stream-encrypted.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "KINESIS_STREAM_ENCRYPTED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="KMS_CMK_NOT_SCHEDULED_FOR_DELETION")
    def KMS_CMK_NOT_SCHEDULED_FOR_DELETION(cls) -> builtins.str:
        '''Checks whether customer master keys (CMKs) are not scheduled for deletion in AWS Key Management Service (KMS).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/kms-cmk-not-scheduled-for-deletion.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "KMS_CMK_NOT_SCHEDULED_FOR_DELETION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LAMBDA_CONCURRENCY_CHECK")
    def LAMBDA_CONCURRENCY_CHECK(cls) -> builtins.str:
        '''Checks whether the AWS Lambda function is configured with function-level concurrent execution limit.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/lambda-concurrency-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LAMBDA_CONCURRENCY_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LAMBDA_DLQ_CHECK")
    def LAMBDA_DLQ_CHECK(cls) -> builtins.str:
        '''Checks whether an AWS Lambda function is configured with a dead-letter queue.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/lambda-dlq-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LAMBDA_DLQ_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LAMBDA_FUNCTION_PUBLIC_ACCESS_PROHIBITED")
    def LAMBDA_FUNCTION_PUBLIC_ACCESS_PROHIBITED(cls) -> builtins.str:
        '''Checks whether the AWS Lambda function policy attached to the Lambda resource prohibits public access.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/lambda-function-public-access-prohibited.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LAMBDA_FUNCTION_PUBLIC_ACCESS_PROHIBITED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LAMBDA_FUNCTION_SETTINGS_CHECK")
    def LAMBDA_FUNCTION_SETTINGS_CHECK(cls) -> builtins.str:
        '''Checks that the lambda function settings for runtime, role, timeout, and memory size match the expected values.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/lambda-function-settings-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LAMBDA_FUNCTION_SETTINGS_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LAMBDA_INSIDE_VPC")
    def LAMBDA_INSIDE_VPC(cls) -> builtins.str:
        '''Checks whether an AWS Lambda function is in an Amazon Virtual Private Cloud.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/lambda-inside-vpc.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LAMBDA_INSIDE_VPC"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LAMBDA_VPC_MULTI_AZ_CHECK")
    def LAMBDA_VPC_MULTI_AZ_CHECK(cls) -> builtins.str:
        '''Checks if Lambda has more than 1 availability zone associated.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/lambda-vpc-multi-az-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "LAMBDA_VPC_MULTI_AZ_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="MFA_ENABLED_FOR_IAM_CONSOLE_ACCESS")
    def MFA_ENABLED_FOR_IAM_CONSOLE_ACCESS(cls) -> builtins.str:
        '''Checks whether AWS Multi-Factor Authentication (MFA) is enabled for all IAM users that use a console password.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/mfa-enabled-for-iam-console-access.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "MFA_ENABLED_FOR_IAM_CONSOLE_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NACL_NO_UNRESTRICTED_SSH_RDP")
    def NACL_NO_UNRESTRICTED_SSH_RDP(cls) -> builtins.str:
        '''Checks if default ports for SSH/RDP ingress traffic for network access control lists (NACLs) is unrestricted.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/nacl-no-unrestricted-ssh-rdp.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "NACL_NO_UNRESTRICTED_SSH_RDP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NETFW_POLICY_DEFAULT_ACTION_FRAGMENT_PACKETS")
    def NETFW_POLICY_DEFAULT_ACTION_FRAGMENT_PACKETS(cls) -> builtins.str:
        '''Checks if an AWS Network Firewall policy is configured with a user defined stateless default action for fragmented packets.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/netfw-policy-default-action-fragment-packets.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "NETFW_POLICY_DEFAULT_ACTION_FRAGMENT_PACKETS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NETFW_POLICY_DEFAULT_ACTION_FULL_PACKETS")
    def NETFW_POLICY_DEFAULT_ACTION_FULL_PACKETS(cls) -> builtins.str:
        '''Checks if an AWS Network Firewall policy is configured with a user defined default stateless action for full packets.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/netfw-policy-default-action-full-packets.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "NETFW_POLICY_DEFAULT_ACTION_FULL_PACKETS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NETFW_POLICY_RULE_GROUP_ASSOCIATED")
    def NETFW_POLICY_RULE_GROUP_ASSOCIATED(cls) -> builtins.str:
        '''Check AWS Network Firewall policy is associated with stateful OR stateless rule groups.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/netfw-policy-rule-group-associated.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "NETFW_POLICY_RULE_GROUP_ASSOCIATED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NETFW_STATELESS_RULE_GROUP_NOT_EMPTY")
    def NETFW_STATELESS_RULE_GROUP_NOT_EMPTY(cls) -> builtins.str:
        '''Checks if a Stateless Network Firewall Rule Group contains rules.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/netfw-stateless-rule-group-not-empty.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "NETFW_STATELESS_RULE_GROUP_NOT_EMPTY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NLB_CROSS_ZONE_LOAD_BALANCING_ENABLED")
    def NLB_CROSS_ZONE_LOAD_BALANCING_ENABLED(cls) -> builtins.str:
        '''Checks if cross-zone load balancing is enabled on Network Load Balancers (NLBs).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/nlb-cross-zone-load-balancing-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "NLB_CROSS_ZONE_LOAD_BALANCING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="OPENSEARCH_ACCESS_CONTROL_ENABLED")
    def OPENSEARCH_ACCESS_CONTROL_ENABLED(cls) -> builtins.str:
        '''Checks if Amazon OpenSearch Service domains have fine-grained access control enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/opensearch-access-control-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "OPENSEARCH_ACCESS_CONTROL_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="OPENSEARCH_AUDIT_LOGGING_ENABLED")
    def OPENSEARCH_AUDIT_LOGGING_ENABLED(cls) -> builtins.str:
        '''Checks if Amazon OpenSearch Service domains have audit logging enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/opensearch-audit-logging-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "OPENSEARCH_AUDIT_LOGGING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="OPENSEARCH_DATA_NODE_FAULT_TOLERANCE")
    def OPENSEARCH_DATA_NODE_FAULT_TOLERANCE(cls) -> builtins.str:
        '''Checks if Amazon OpenSearch Service domains are configured with at least three data nodes and zoneAwarenessEnabled is true.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/opensearch-data-node-fault-tolerance.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "OPENSEARCH_DATA_NODE_FAULT_TOLERANCE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="OPENSEARCH_ENCRYPTED_AT_REST")
    def OPENSEARCH_ENCRYPTED_AT_REST(cls) -> builtins.str:
        '''Checks if Amazon OpenSearch Service domains have encryption at rest configuration enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/opensearch-encrypted-at-rest.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "OPENSEARCH_ENCRYPTED_AT_REST"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="OPENSEARCH_HTTPS_REQUIRED")
    def OPENSEARCH_HTTPS_REQUIRED(cls) -> builtins.str:
        '''Checks whether connections to OpenSearch domains are using HTTPS.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/opensearch-https-required.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "OPENSEARCH_HTTPS_REQUIRED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="OPENSEARCH_IN_VPC_ONLY")
    def OPENSEARCH_IN_VPC_ONLY(cls) -> builtins.str:
        '''Checks if Amazon OpenSearch Service domains are in an Amazon Virtual Private Cloud (VPC).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/opensearch-in-vpc-only.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "OPENSEARCH_IN_VPC_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="OPENSEARCH_LOGS_TO_CLOUDWATCH")
    def OPENSEARCH_LOGS_TO_CLOUDWATCH(cls) -> builtins.str:
        '''Checks if Amazon OpenSearch Service domains are configured to send logs to Amazon CloudWatch Logs.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/opensearch-logs-to-cloudwatch.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "OPENSEARCH_LOGS_TO_CLOUDWATCH"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="OPENSEARCH_NODE_TO_NODE_ENCRYPTION_CHECK")
    def OPENSEARCH_NODE_TO_NODE_ENCRYPTION_CHECK(cls) -> builtins.str:
        '''Check if Amazon OpenSearch Service nodes are encrypted end to end.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/opensearch-node-to-node-encryption-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "OPENSEARCH_NODE_TO_NODE_ENCRYPTION_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_AUTOMATIC_MINOR_VERSION_UPGRADE_ENABLED")
    def RDS_AUTOMATIC_MINOR_VERSION_UPGRADE_ENABLED(cls) -> builtins.str:
        '''Checks if Amazon Relational Database Service (RDS) database instances are configured for automatic minor version upgrades.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-automatic-minor-version-upgrade-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_AUTOMATIC_MINOR_VERSION_UPGRADE_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_CLUSTER_DEFAULT_ADMIN_CHECK")
    def RDS_CLUSTER_DEFAULT_ADMIN_CHECK(cls) -> builtins.str:
        '''Checks if an Amazon Relational Database Service (Amazon RDS) database cluster has changed the admin username from its default value.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-cluster-default-admin-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_CLUSTER_DEFAULT_ADMIN_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_CLUSTER_DELETION_PROTECTION_ENABLED")
    def RDS_CLUSTER_DELETION_PROTECTION_ENABLED(cls) -> builtins.str:
        '''Checks if an Amazon Relational Database Service (Amazon RDS) cluster has deletion protection enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-cluster-deletion-protection-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_CLUSTER_DELETION_PROTECTION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_CLUSTER_IAM_AUTHENTICATION_ENABLED")
    def RDS_CLUSTER_IAM_AUTHENTICATION_ENABLED(cls) -> builtins.str:
        '''Checks if an Amazon RDS Cluster has AWS Identity and Access Management (IAM) authentication enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-cluster-iam-authentication-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_CLUSTER_IAM_AUTHENTICATION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_CLUSTER_MULTI_AZ_ENABLED")
    def RDS_CLUSTER_MULTI_AZ_ENABLED(cls) -> builtins.str:
        '''Checks if Multi-AZ replication is enabled on Amazon Aurora and Hermes clusters managed by Amazon Relational Database Service (Amazon RDS).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-cluster-multi-az-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_CLUSTER_MULTI_AZ_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_DB_INSTANCE_BACKUP_ENABLED")
    def RDS_DB_INSTANCE_BACKUP_ENABLED(cls) -> builtins.str:
        '''Checks whether RDS DB instances have backups enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/db-instance-backup-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_DB_INSTANCE_BACKUP_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_DB_SECURITY_GROUP_NOT_ALLOWED")
    def RDS_DB_SECURITY_GROUP_NOT_ALLOWED(cls) -> builtins.str:
        '''Checks if there are any Amazon Relational Database Service (RDS) DB security groups that are not the default DB security group.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-db-security-group-not-allowed.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_DB_SECURITY_GROUP_NOT_ALLOWED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_ENHANCED_MONITORING_ENABLED")
    def RDS_ENHANCED_MONITORING_ENABLED(cls) -> builtins.str:
        '''Checks whether enhanced monitoring is enabled for Amazon Relational Database Service (Amazon RDS) instances.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-enhanced-monitoring-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_ENHANCED_MONITORING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_IN_BACKUP_PLAN")
    def RDS_IN_BACKUP_PLAN(cls) -> builtins.str:
        '''Checks whether Amazon RDS database is present in back plans of AWS Backup.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-in-backup-plan.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_IN_BACKUP_PLAN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_INSTANCE_DEFAULT_ADMIN_CHECK")
    def RDS_INSTANCE_DEFAULT_ADMIN_CHECK(cls) -> builtins.str:
        '''Checks if an Amazon Relational Database Service (Amazon RDS) database has changed the admin username from its default value.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-instance-default-admin-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_INSTANCE_DEFAULT_ADMIN_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_INSTANCE_DELETION_PROTECTION_ENABLED")
    def RDS_INSTANCE_DELETION_PROTECTION_ENABLED(cls) -> builtins.str:
        '''Checks if an Amazon Relational Database Service (Amazon RDS) instance has deletion protection enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-instance-deletion-protection-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_INSTANCE_DELETION_PROTECTION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_INSTANCE_IAM_AUTHENTICATION_ENABLED")
    def RDS_INSTANCE_IAM_AUTHENTICATION_ENABLED(cls) -> builtins.str:
        '''Checks if an Amazon RDS instance has AWS Identity and Access Management (IAM) authentication enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-instance-iam-authentication-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_INSTANCE_IAM_AUTHENTICATION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_INSTANCE_PUBLIC_ACCESS_CHECK")
    def RDS_INSTANCE_PUBLIC_ACCESS_CHECK(cls) -> builtins.str:
        '''Check whether the Amazon Relational Database Service instances are not publicly accessible.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-instance-public-access-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_INSTANCE_PUBLIC_ACCESS_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_LAST_BACKUP_RECOVERY_POINT_CREATED")
    def RDS_LAST_BACKUP_RECOVERY_POINT_CREATED(cls) -> builtins.str:
        '''Checks if a recovery point was created for Amazon Relational Database Service (Amazon RDS).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-last-backup-recovery-point-created.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_LAST_BACKUP_RECOVERY_POINT_CREATED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_LOGGING_ENABLED")
    def RDS_LOGGING_ENABLED(cls) -> builtins.str:
        '''Checks that respective logs of Amazon Relational Database Service (Amazon RDS) are enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-logging-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_LOGGING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_MULTI_AZ_SUPPORT")
    def RDS_MULTI_AZ_SUPPORT(cls) -> builtins.str:
        '''Checks whether high availability is enabled for your RDS DB instances.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-multi-az-support.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_MULTI_AZ_SUPPORT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_RESOURCES_PROTECTED_BY_BACKUP_PLAN")
    def RDS_RESOURCES_PROTECTED_BY_BACKUP_PLAN(cls) -> builtins.str:
        '''Checks if Amazon Relational Database Service (Amazon RDS) instances are protected by a backup plan.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-resources-protected-by-backup-plan.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_RESOURCES_PROTECTED_BY_BACKUP_PLAN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_SNAPSHOT_ENCRYPTED")
    def RDS_SNAPSHOT_ENCRYPTED(cls) -> builtins.str:
        '''Checks whether Amazon Relational Database Service (Amazon RDS) DB snapshots are encrypted.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-snapshot-encrypted.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_SNAPSHOT_ENCRYPTED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_SNAPSHOTS_PUBLIC_PROHIBITED")
    def RDS_SNAPSHOTS_PUBLIC_PROHIBITED(cls) -> builtins.str:
        '''Checks if Amazon Relational Database Service (Amazon RDS) snapshots are public.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-snapshots-public-prohibited.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_SNAPSHOTS_PUBLIC_PROHIBITED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_STORAGE_ENCRYPTED")
    def RDS_STORAGE_ENCRYPTED(cls) -> builtins.str:
        '''Checks whether storage encryption is enabled for your RDS DB instances.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/rds-storage-encrypted.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "RDS_STORAGE_ENCRYPTED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_AUDIT_LOGGING_ENABLED")
    def REDSHIFT_AUDIT_LOGGING_ENABLED(cls) -> builtins.str:
        '''Checks if Amazon Redshift clusters are logging audits to a specific bucket.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/redshift-audit-logging-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "REDSHIFT_AUDIT_LOGGING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_BACKUP_ENABLED")
    def REDSHIFT_BACKUP_ENABLED(cls) -> builtins.str:
        '''Checks that Amazon Redshift automated snapshots are enabled for clusters.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/redshift-backup-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "REDSHIFT_BACKUP_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_CLUSTER_CONFIGURATION_CHECK")
    def REDSHIFT_CLUSTER_CONFIGURATION_CHECK(cls) -> builtins.str:
        '''Checks whether Amazon Redshift clusters have the specified settings.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/redshift-cluster-configuration-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "REDSHIFT_CLUSTER_CONFIGURATION_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_CLUSTER_KMS_ENABLED")
    def REDSHIFT_CLUSTER_KMS_ENABLED(cls) -> builtins.str:
        '''Checks if Amazon Redshift clusters are using a specified AWS Key Management Service (AWS KMS) key for encryption.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/redshift-cluster-kms-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "REDSHIFT_CLUSTER_KMS_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_CLUSTER_MAINTENANCE_SETTINGS_CHECK")
    def REDSHIFT_CLUSTER_MAINTENANCE_SETTINGS_CHECK(cls) -> builtins.str:
        '''Checks whether Amazon Redshift clusters have the specified maintenance settings.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/redshift-cluster-maintenancesettings-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "REDSHIFT_CLUSTER_MAINTENANCE_SETTINGS_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_CLUSTER_PUBLIC_ACCESS_CHECK")
    def REDSHIFT_CLUSTER_PUBLIC_ACCESS_CHECK(cls) -> builtins.str:
        '''Checks whether Amazon Redshift clusters are not publicly accessible.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/redshift-cluster-public-access-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "REDSHIFT_CLUSTER_PUBLIC_ACCESS_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_DEFAULT_ADMIN_CHECK")
    def REDSHIFT_DEFAULT_ADMIN_CHECK(cls) -> builtins.str:
        '''Checks if an Amazon Redshift cluster has changed the admin username from its default value.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/redshift-default-admin-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "REDSHIFT_DEFAULT_ADMIN_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_DEFAULT_DB_NAME_CHECK")
    def REDSHIFT_DEFAULT_DB_NAME_CHECK(cls) -> builtins.str:
        '''Checks if a Redshift cluster has changed its database name from the default value.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/redshift-default-db-name-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "REDSHIFT_DEFAULT_DB_NAME_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_ENHANCED_VPC_ROUTING_ENABLED")
    def REDSHIFT_ENHANCED_VPC_ROUTING_ENABLED(cls) -> builtins.str:
        '''Checks if Amazon Redshift cluster has 'enhancedVpcRouting' enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/redshift-enhanced-vpc-routing-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "REDSHIFT_ENHANCED_VPC_ROUTING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_REQUIRE_TLS_SSL")
    def REDSHIFT_REQUIRE_TLS_SSL(cls) -> builtins.str:
        '''Checks whether Amazon Redshift clusters require TLS/SSL encryption to connect to SQL clients.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/redshift-require-tls-ssl.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "REDSHIFT_REQUIRE_TLS_SSL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REQUIRED_TAGS")
    def REQUIRED_TAGS(cls) -> builtins.str:
        '''Checks whether your resources have the tags that you specify.

        For example, you can check whether your Amazon EC2 instances have the CostCenter tag.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/required-tags.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "REQUIRED_TAGS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ROOT_ACCOUNT_HARDWARE_MFA_ENABLED")
    def ROOT_ACCOUNT_HARDWARE_MFA_ENABLED(cls) -> builtins.str:
        '''Checks whether your AWS account is enabled to use multi-factor authentication (MFA) hardware device to sign in with root credentials.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/root-account-hardware-mfa-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ROOT_ACCOUNT_HARDWARE_MFA_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ROOT_ACCOUNT_MFA_ENABLED")
    def ROOT_ACCOUNT_MFA_ENABLED(cls) -> builtins.str:
        '''Checks whether users of your AWS account require a multi-factor authentication (MFA) device to sign in with root credentials.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/root-account-mfa-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ROOT_ACCOUNT_MFA_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_ACCOUNT_LEVEL_PUBLIC_ACCESS_BLOCKS")
    def S3_ACCOUNT_LEVEL_PUBLIC_ACCESS_BLOCKS(cls) -> builtins.str:
        '''Checks whether the required public access block settings are configured from account level.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-account-level-public-access-blocks.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_ACCOUNT_LEVEL_PUBLIC_ACCESS_BLOCKS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_ACCOUNT_LEVEL_PUBLIC_ACCESS_BLOCKS_PERIODIC")
    def S3_ACCOUNT_LEVEL_PUBLIC_ACCESS_BLOCKS_PERIODIC(cls) -> builtins.str:
        '''Checks if the required public access block settings are configured from account level.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-account-level-public-access-blocks-periodic.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_ACCOUNT_LEVEL_PUBLIC_ACCESS_BLOCKS_PERIODIC"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET_ACL_PROHIBITED")
    def S3_BUCKET_ACL_PROHIBITED(cls) -> builtins.str:
        '''Checks if Amazon Simple Storage Service (Amazon S3) Buckets allow user permissions through access control lists (ACLs).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-acl-prohibited.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_BUCKET_ACL_PROHIBITED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET_BLOCKED_ACTIONS_PROHIBITED")
    def S3_BUCKET_BLOCKED_ACTIONS_PROHIBITED(cls) -> builtins.str:
        '''Checks if the Amazon Simple Storage Service bucket policy does not allow blacklisted bucket-level and object-level actions on resources in the bucket for principals from other AWS accounts.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-blacklisted-actions-prohibited.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_BUCKET_BLOCKED_ACTIONS_PROHIBITED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET_DEFAULT_LOCK_ENABLED")
    def S3_BUCKET_DEFAULT_LOCK_ENABLED(cls) -> builtins.str:
        '''Checks whether Amazon Simple Storage Service (Amazon S3) bucket has lock enabled, by default.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-default-lock-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_BUCKET_DEFAULT_LOCK_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET_LEVEL_PUBLIC_ACCESS_PROHIBITED")
    def S3_BUCKET_LEVEL_PUBLIC_ACCESS_PROHIBITED(cls) -> builtins.str:
        '''Checks if Amazon Simple Storage Service (Amazon S3) buckets are publicly accessible.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-level-public-access-prohibited.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_BUCKET_LEVEL_PUBLIC_ACCESS_PROHIBITED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET_LOGGING_ENABLED")
    def S3_BUCKET_LOGGING_ENABLED(cls) -> builtins.str:
        '''Checks whether logging is enabled for your S3 buckets.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-logging-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_BUCKET_LOGGING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET_POLICY_GRANTEE_CHECK")
    def S3_BUCKET_POLICY_GRANTEE_CHECK(cls) -> builtins.str:
        '''Checks that the access granted by the Amazon S3 bucket is restricted by any of the AWS principals, federated users, service principals, IP addresses, or VPCs that you provide.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-policy-grantee-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_BUCKET_POLICY_GRANTEE_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET_POLICY_NOT_MORE_PERMISSIVE")
    def S3_BUCKET_POLICY_NOT_MORE_PERMISSIVE(cls) -> builtins.str:
        '''Checks if your Amazon Simple Storage Service bucket policies do not allow other inter-account permissions than the control Amazon S3 bucket policy that you provide.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-policy-not-more-permissive.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_BUCKET_POLICY_NOT_MORE_PERMISSIVE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET_PUBLIC_READ_PROHIBITED")
    def S3_BUCKET_PUBLIC_READ_PROHIBITED(cls) -> builtins.str:
        '''Checks if your Amazon S3 buckets do not allow public read access.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-public-read-prohibited.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_BUCKET_PUBLIC_READ_PROHIBITED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET_PUBLIC_WRITE_PROHIBITED")
    def S3_BUCKET_PUBLIC_WRITE_PROHIBITED(cls) -> builtins.str:
        '''Checks that your Amazon S3 buckets do not allow public write access.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-public-write-prohibited.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_BUCKET_PUBLIC_WRITE_PROHIBITED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET_REPLICATION_ENABLED")
    def S3_BUCKET_REPLICATION_ENABLED(cls) -> builtins.str:
        '''Checks whether S3 buckets have cross-region replication enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-replication-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_BUCKET_REPLICATION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED")
    def S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED(cls) -> builtins.str:
        '''Checks that your Amazon S3 bucket either has Amazon S3 default encryption enabled or that the S3 bucket policy explicitly denies put-object requests without server side encryption that uses AES-256 or AWS Key Management Service.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-server-side-encryption-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET_SSL_REQUESTS_ONLY")
    def S3_BUCKET_SSL_REQUESTS_ONLY(cls) -> builtins.str:
        '''Checks whether S3 buckets have policies that require requests to use Secure Socket Layer (SSL).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-ssl-requests-only.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_BUCKET_SSL_REQUESTS_ONLY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET_VERSIONING_ENABLED")
    def S3_BUCKET_VERSIONING_ENABLED(cls) -> builtins.str:
        '''Checks whether versioning is enabled for your S3 buckets.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-versioning-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_BUCKET_VERSIONING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_DEFAULT_ENCRYPTION_KMS")
    def S3_DEFAULT_ENCRYPTION_KMS(cls) -> builtins.str:
        '''Checks whether the Amazon Simple Storage Service (Amazon S3) buckets are encrypted with AWS Key Management Service (AWS KMS).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-default-encryption-kms.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_DEFAULT_ENCRYPTION_KMS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_EVENT_NOTIFICATIONS_ENABLED")
    def S3_EVENT_NOTIFICATIONS_ENABLED(cls) -> builtins.str:
        '''Checks if Amazon S3 Events Notifications are enabled on an S3 bucket.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-event-notifications-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_EVENT_NOTIFICATIONS_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_LAST_BACKUP_RECOVERY_POINT_CREATED")
    def S3_LAST_BACKUP_RECOVERY_POINT_CREATED(cls) -> builtins.str:
        '''Checks if a recovery point was created for Amazon Simple Storage Service (Amazon S3).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-last-backup-recovery-point-created.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_LAST_BACKUP_RECOVERY_POINT_CREATED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_LIFECYCLE_POLICY_CHECK")
    def S3_LIFECYCLE_POLICY_CHECK(cls) -> builtins.str:
        '''Checks if a lifecycle rule is configured for an Amazon Simple Storage Service (Amazon S3) bucket.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-lifecycle-policy-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_LIFECYCLE_POLICY_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_RESOURCES_PROTECTED_BY_BACKUP_PLAN")
    def S3_RESOURCES_PROTECTED_BY_BACKUP_PLAN(cls) -> builtins.str:
        '''Checks if Amazon Simple Storage Service (Amazon S3) buckets are protected by a backup plan.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-resources-protected-by-backup-plan.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_RESOURCES_PROTECTED_BY_BACKUP_PLAN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_VERSION_LIFECYCLE_POLICY_CHECK")
    def S3_VERSION_LIFECYCLE_POLICY_CHECK(cls) -> builtins.str:
        '''Checks if Amazon Simple Storage Service (Amazon S3) version enabled buckets have lifecycle policy configured.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/s3-version-lifecycle-policy-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "S3_VERSION_LIFECYCLE_POLICY_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SAGEMAKER_ENDPOINT_CONFIGURATION_KMS_KEY_CONFIGURED")
    def SAGEMAKER_ENDPOINT_CONFIGURATION_KMS_KEY_CONFIGURED(cls) -> builtins.str:
        '''Checks whether AWS Key Management Service (KMS) key is configured for an Amazon SageMaker endpoint configuration.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-endpoint-configuration-kms-key-configured.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SAGEMAKER_ENDPOINT_CONFIGURATION_KMS_KEY_CONFIGURED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SAGEMAKER_NOTEBOOK_INSTANCE_KMS_KEY_CONFIGURED")
    def SAGEMAKER_NOTEBOOK_INSTANCE_KMS_KEY_CONFIGURED(cls) -> builtins.str:
        '''Check whether an AWS Key Management Service (KMS) key is configured for SageMaker notebook instance.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-notebook-instance-kms-key-configured.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SAGEMAKER_NOTEBOOK_INSTANCE_KMS_KEY_CONFIGURED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SAGEMAKER_NOTEBOOK_NO_DIRECT_INTERNET_ACCESS")
    def SAGEMAKER_NOTEBOOK_NO_DIRECT_INTERNET_ACCESS(cls) -> builtins.str:
        '''Checks whether direct internet access is disabled for an Amazon SageMaker notebook instance.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/sagemaker-notebook-no-direct-internet-access.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SAGEMAKER_NOTEBOOK_NO_DIRECT_INTERNET_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SECRETSMANAGER_ROTATION_ENABLED_CHECK")
    def SECRETSMANAGER_ROTATION_ENABLED_CHECK(cls) -> builtins.str:
        '''Checks whether AWS Secrets Manager secret has rotation enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/secretsmanager-rotation-enabled-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SECRETSMANAGER_ROTATION_ENABLED_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SECRETSMANAGER_SCHEDULED_ROTATION_SUCCESS_CHECK")
    def SECRETSMANAGER_SCHEDULED_ROTATION_SUCCESS_CHECK(cls) -> builtins.str:
        '''Checks whether AWS Secrets Manager secret rotation has rotated successfully as per the rotation schedule.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/secretsmanager-scheduled-rotation-success-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SECRETSMANAGER_SCHEDULED_ROTATION_SUCCESS_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SECRETSMANAGER_SECRET_PERIODIC_ROTATION")
    def SECRETSMANAGER_SECRET_PERIODIC_ROTATION(cls) -> builtins.str:
        '''Checks if AWS Secrets Manager secrets have been rotated in the past specified number of days.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/secretsmanager-secret-periodic-rotation.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SECRETSMANAGER_SECRET_PERIODIC_ROTATION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SECRETSMANAGER_SECRET_UNUSED")
    def SECRETSMANAGER_SECRET_UNUSED(cls) -> builtins.str:
        '''Checks if AWS Secrets Manager secrets have been accessed within a specified number of days.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/secretsmanager-secret-unused.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SECRETSMANAGER_SECRET_UNUSED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SECRETSMANAGER_USING_CMK")
    def SECRETSMANAGER_USING_CMK(cls) -> builtins.str:
        '''Checks if all secrets in AWS Secrets Manager are encrypted using the AWS managed key (aws/secretsmanager) or a customer managed key that was created in AWS Key Management Service (AWS KMS).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/secretsmanager-using-cmk.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SECRETSMANAGER_USING_CMK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SECURITYHUB_ENABLED")
    def SECURITYHUB_ENABLED(cls) -> builtins.str:
        '''Checks that AWS Security Hub is enabled for an AWS account.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/securityhub-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SECURITYHUB_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SERVICE_VPC_ENDPOINT_ENABLED")
    def SERVICE_VPC_ENDPOINT_ENABLED(cls) -> builtins.str:
        '''Checks whether Service Endpoint for the service provided in rule parameter is created for each Amazon VPC.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/service-vpc-endpoint-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SERVICE_VPC_ENDPOINT_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SHIELD_ADVANCED_ENABLED_AUTO_RENEW")
    def SHIELD_ADVANCED_ENABLED_AUTO_RENEW(cls) -> builtins.str:
        '''Checks whether EBS volumes are attached to EC2 instances.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/shield-advanced-enabled-autorenew.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SHIELD_ADVANCED_ENABLED_AUTO_RENEW"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SHIELD_DRT_ACCESS")
    def SHIELD_DRT_ACCESS(cls) -> builtins.str:
        '''Verify that DDoS response team (DRT) can access AWS account.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/shield-drt-access.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SHIELD_DRT_ACCESS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SNS_ENCRYPTED_KMS")
    def SNS_ENCRYPTED_KMS(cls) -> builtins.str:
        '''Checks whether Amazon SNS topic is encrypted with AWS Key Management Service (AWS KMS).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/sns-encrypted-kms.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SNS_ENCRYPTED_KMS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SNS_TOPIC_MESSAGE_DELIVERY_NOTIFICATION_ENABLED")
    def SNS_TOPIC_MESSAGE_DELIVERY_NOTIFICATION_ENABLED(cls) -> builtins.str:
        '''Checks if Amazon Simple Notification Service (SNS) logging is enabled for the delivery status of notification messages sent to a topic for the endpoints.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/sns-topic-message-delivery-notification-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SNS_TOPIC_MESSAGE_DELIVERY_NOTIFICATION_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SSM_DOCUMENT_NOT_PUBLIC")
    def SSM_DOCUMENT_NOT_PUBLIC(cls) -> builtins.str:
        '''Checks if AWS Systems Manager documents owned by the account are public.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/ssm-document-not-public.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SSM_DOCUMENT_NOT_PUBLIC"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="STORAGEGATEWAY_LAST_BACKUP_RECOVERY_POINT_CREATED")
    def STORAGEGATEWAY_LAST_BACKUP_RECOVERY_POINT_CREATED(cls) -> builtins.str:
        '''Checks if a recovery point was created for AWS Storage Gateway volumes.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/storagegateway-last-backup-recovery-point-created.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "STORAGEGATEWAY_LAST_BACKUP_RECOVERY_POINT_CREATED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SUBNET_AUTO_ASSIGN_PUBLIC_IP_DISABLED")
    def SUBNET_AUTO_ASSIGN_PUBLIC_IP_DISABLED(cls) -> builtins.str:
        '''hecks if Amazon Virtual Private Cloud (Amazon VPC) subnets are assigned a public IP address.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/subnet-auto-assign-public-ip-disabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "SUBNET_AUTO_ASSIGN_PUBLIC_IP_DISABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="VIRTUALMACHINE_LAST_BACKUP_RECOVERY_POINT_CREATED")
    def VIRTUALMACHINE_LAST_BACKUP_RECOVERY_POINT_CREATED(cls) -> builtins.str:
        '''Checks if a recovery point was created for AWS Backup-Gateway VirtualMachines.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/virtualmachine-last-backup-recovery-point-created.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "VIRTUALMACHINE_LAST_BACKUP_RECOVERY_POINT_CREATED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="VIRTUALMACHINE_RESOURCES_PROTECTED_BY_BACKUP_PLAN")
    def VIRTUALMACHINE_RESOURCES_PROTECTED_BY_BACKUP_PLAN(cls) -> builtins.str:
        '''Checks if AWS Backup-Gateway VirtualMachines are protected by a backup plan.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/virtualmachine-resources-protected-by-backup-plan.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "VIRTUALMACHINE_RESOURCES_PROTECTED_BY_BACKUP_PLAN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="VPC_DEFAULT_SECURITY_GROUP_CLOSED")
    def VPC_DEFAULT_SECURITY_GROUP_CLOSED(cls) -> builtins.str:
        '''Checks that the default security group of any Amazon Virtual Private Cloud (VPC) does not allow inbound or outbound traffic.

        The rule returns NOT_APPLICABLE if the security group
        is not default.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/vpc-default-security-group-closed.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "VPC_DEFAULT_SECURITY_GROUP_CLOSED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="VPC_FLOW_LOGS_ENABLED")
    def VPC_FLOW_LOGS_ENABLED(cls) -> builtins.str:
        '''Checks whether Amazon Virtual Private Cloud flow logs are found and enabled for Amazon VPC.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/vpc-flow-logs-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "VPC_FLOW_LOGS_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="VPC_NETWORK_ACL_UNUSED_CHECK")
    def VPC_NETWORK_ACL_UNUSED_CHECK(cls) -> builtins.str:
        '''Checks if there are unused network access control lists (network ACLs).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/vpc-network-acl-unused-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "VPC_NETWORK_ACL_UNUSED_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="VPC_PEERING_DNS_RESOLUTION_CHECK")
    def VPC_PEERING_DNS_RESOLUTION_CHECK(cls) -> builtins.str:
        '''Checks if DNS resolution from accepter/requester VPC to private IP is enabled.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/vpc-peering-dns-resolution-check.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "VPC_PEERING_DNS_RESOLUTION_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="VPC_SG_OPEN_ONLY_TO_AUTHORIZED_PORTS")
    def VPC_SG_OPEN_ONLY_TO_AUTHORIZED_PORTS(cls) -> builtins.str:
        '''Checks whether the security group with 0.0.0.0/0 of any Amazon Virtual Private Cloud (Amazon VPC) allows only specific inbound TCP or UDP traffic.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/vpc-sg-open-only-to-authorized-ports.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "VPC_SG_OPEN_ONLY_TO_AUTHORIZED_PORTS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="VPC_VPN_2_TUNNELS_UP")
    def VPC_VPN_2_TUNNELS_UP(cls) -> builtins.str:
        '''Checks that both AWS Virtual Private Network tunnels provided by AWS Site-to-Site VPN are in UP status.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/vpc-vpn-2-tunnels-up.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "VPC_VPN_2_TUNNELS_UP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_CLASSIC_LOGGING_ENABLED")
    def WAF_CLASSIC_LOGGING_ENABLED(cls) -> builtins.str:
        '''Checks if logging is enabled on AWS Web Application Firewall (WAF) classic global web ACLs.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/waf-classic-logging-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "WAF_CLASSIC_LOGGING_ENABLED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_GLOBAL_RULE_NOT_EMPTY")
    def WAF_GLOBAL_RULE_NOT_EMPTY(cls) -> builtins.str:
        '''Checks if an AWS WAF global rule contains any conditions.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/waf-global-rule-not-empty.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "WAF_GLOBAL_RULE_NOT_EMPTY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_GLOBAL_RULEGROUP_NOT_EMPTY")
    def WAF_GLOBAL_RULEGROUP_NOT_EMPTY(cls) -> builtins.str:
        '''Checks if an AWS WAF Classic rule group contains any rules.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/waf-global-rulegroup-not-empty.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "WAF_GLOBAL_RULEGROUP_NOT_EMPTY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_GLOBAL_WEBACL_NOT_EMPTY")
    def WAF_GLOBAL_WEBACL_NOT_EMPTY(cls) -> builtins.str:
        '''Checks whether a WAF Global Web ACL contains any WAF rules or rule groups.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/waf-global-webacl-not-empty.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "WAF_GLOBAL_WEBACL_NOT_EMPTY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_REGIONAL_RULE_NOT_EMPTY")
    def WAF_REGIONAL_RULE_NOT_EMPTY(cls) -> builtins.str:
        '''Checks whether WAF regional rule contains conditions.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/waf-regional-rule-not-empty.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "WAF_REGIONAL_RULE_NOT_EMPTY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_REGIONAL_RULEGROUP_NOT_EMPTY")
    def WAF_REGIONAL_RULEGROUP_NOT_EMPTY(cls) -> builtins.str:
        '''Checks if WAF Regional rule groups contain any rules.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/waf-regional-rulegroup-not-empty.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "WAF_REGIONAL_RULEGROUP_NOT_EMPTY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_REGIONAL_WEBACL_NOT_EMPTY")
    def WAF_REGIONAL_WEBACL_NOT_EMPTY(cls) -> builtins.str:
        '''Checks if a WAF regional Web ACL contains any WAF rules or rule groups.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/waf-regional-webacl-not-empty.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "WAF_REGIONAL_WEBACL_NOT_EMPTY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAFV2_LOGGING_ENABLED")
    def WAFV2_LOGGING_ENABLED(cls) -> builtins.str:
        '''Checks whether logging is enabled on AWS Web Application Firewall (WAFV2) regional and global web access control list (ACLs).

        :see: https://docs.aws.amazon.com/config/latest/developerguide/wafv2-logging-enabled.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "WAFV2_LOGGING_ENABLED"))


@jsii.enum(jsii_type="aws-cdk-lib.aws_config.MaximumExecutionFrequency")
class MaximumExecutionFrequency(enum.Enum):
    '''The maximum frequency at which the AWS Config rule runs evaluations.

    :exampleMetadata: infused

    Example::

        # https://docs.aws.amazon.com/config/latest/developerguide/access-keys-rotated.html
        config.ManagedRule(self, "AccessKeysRotated",
            identifier=config.ManagedRuleIdentifiers.ACCESS_KEYS_ROTATED,
            input_parameters={
                "max_access_key_age": 60
            },
        
            # default is 24 hours
            maximum_execution_frequency=config.MaximumExecutionFrequency.TWELVE_HOURS
        )
    '''

    ONE_HOUR = "ONE_HOUR"
    '''1 hour.'''
    THREE_HOURS = "THREE_HOURS"
    '''3 hours.'''
    SIX_HOURS = "SIX_HOURS"
    '''6 hours.'''
    TWELVE_HOURS = "TWELVE_HOURS"
    '''12 hours.'''
    TWENTY_FOUR_HOURS = "TWENTY_FOUR_HOURS"
    '''24 hours.'''


class ResourceType(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_config.ResourceType",
):
    '''Resources types that are supported by AWS Config.

    :see: https://docs.aws.amazon.com/config/latest/developerguide/resource-config-reference.html
    :exampleMetadata: infused

    Example::

        # Lambda function containing logic that evaluates compliance with the rule.
        eval_compliance_fn = lambda_.Function(self, "CustomFunction",
            code=lambda_.AssetCode.from_inline("exports.handler = (event) => console.log(event);"),
            handler="index.handler",
            runtime=lambda_.Runtime.NODEJS_18_X
        )
        
        # A custom rule that runs on configuration changes of EC2 instances
        custom_rule = config.CustomRule(self, "Custom",
            configuration_changes=True,
            lambda_function=eval_compliance_fn,
            rule_scope=config.RuleScope.from_resource(config.ResourceType.EC2_INSTANCE)
        )
    '''

    @jsii.member(jsii_name="of")
    @builtins.classmethod
    def of(cls, type: builtins.str) -> "ResourceType":
        '''A custom resource type to support future cases.

        :param type: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d47c160bf4bb1dd7741c5139c7a3ea417f94283943a510318608d3a02ef3af69)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        return typing.cast("ResourceType", jsii.sinvoke(cls, "of", [type]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ACM_CERTIFICATE")
    def ACM_CERTIFICATE(cls) -> "ResourceType":
        '''AWS Certificate manager certificate.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ACM_CERTIFICATE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_MQ_BROKER")
    def AMAZON_MQ_BROKER(cls) -> "ResourceType":
        '''Amazon MQ broker.'''
        return typing.cast("ResourceType", jsii.sget(cls, "AMAZON_MQ_BROKER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="APIGATEWAY_REST_API")
    def APIGATEWAY_REST_API(cls) -> "ResourceType":
        '''API Gateway REST API.'''
        return typing.cast("ResourceType", jsii.sget(cls, "APIGATEWAY_REST_API"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="APIGATEWAY_STAGE")
    def APIGATEWAY_STAGE(cls) -> "ResourceType":
        '''API Gateway Stage.'''
        return typing.cast("ResourceType", jsii.sget(cls, "APIGATEWAY_STAGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="APIGATEWAYV2_API")
    def APIGATEWAYV2_API(cls) -> "ResourceType":
        '''API Gatewayv2 API.'''
        return typing.cast("ResourceType", jsii.sget(cls, "APIGATEWAYV2_API"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="APIGATEWAYV2_STAGE")
    def APIGATEWAYV2_STAGE(cls) -> "ResourceType":
        '''API Gatewayv2 Stage.'''
        return typing.cast("ResourceType", jsii.sget(cls, "APIGATEWAYV2_STAGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="APPCONFIG_APPLICATION")
    def APPCONFIG_APPLICATION(cls) -> "ResourceType":
        '''AWS AppConfig application.'''
        return typing.cast("ResourceType", jsii.sget(cls, "APPCONFIG_APPLICATION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="APPCONFIG_CONFIGURATION_PROFILE")
    def APPCONFIG_CONFIGURATION_PROFILE(cls) -> "ResourceType":
        '''AWS AppConfig configuration profile.'''
        return typing.cast("ResourceType", jsii.sget(cls, "APPCONFIG_CONFIGURATION_PROFILE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="APPCONFIG_ENVIRONMENT")
    def APPCONFIG_ENVIRONMENT(cls) -> "ResourceType":
        '''AWS AppConfig environment.'''
        return typing.cast("ResourceType", jsii.sget(cls, "APPCONFIG_ENVIRONMENT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="APPSYNC_GRAPHQL_API")
    def APPSYNC_GRAPHQL_API(cls) -> "ResourceType":
        '''AWS AppSync GraphQL Api.'''
        return typing.cast("ResourceType", jsii.sget(cls, "APPSYNC_GRAPHQL_API"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTO_SCALING_GROUP")
    def AUTO_SCALING_GROUP(cls) -> "ResourceType":
        '''AWS Auto Scaling group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "AUTO_SCALING_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTO_SCALING_LAUNCH_CONFIGURATION")
    def AUTO_SCALING_LAUNCH_CONFIGURATION(cls) -> "ResourceType":
        '''AWS Auto Scaling launch configuration.'''
        return typing.cast("ResourceType", jsii.sget(cls, "AUTO_SCALING_LAUNCH_CONFIGURATION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTO_SCALING_POLICY")
    def AUTO_SCALING_POLICY(cls) -> "ResourceType":
        '''AWS Auto Scaling policy.'''
        return typing.cast("ResourceType", jsii.sget(cls, "AUTO_SCALING_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AUTO_SCALING_SCHEDULED_ACTION")
    def AUTO_SCALING_SCHEDULED_ACTION(cls) -> "ResourceType":
        '''AWS Auto Scaling scheduled action.'''
        return typing.cast("ResourceType", jsii.sget(cls, "AUTO_SCALING_SCHEDULED_ACTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BACKUP_BACKUP_PLAN")
    def BACKUP_BACKUP_PLAN(cls) -> "ResourceType":
        '''AWS Backup backup plan.'''
        return typing.cast("ResourceType", jsii.sget(cls, "BACKUP_BACKUP_PLAN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BACKUP_BACKUP_SELECTION")
    def BACKUP_BACKUP_SELECTION(cls) -> "ResourceType":
        '''AWS Backup backup selection.'''
        return typing.cast("ResourceType", jsii.sget(cls, "BACKUP_BACKUP_SELECTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BACKUP_BACKUP_VAULT")
    def BACKUP_BACKUP_VAULT(cls) -> "ResourceType":
        '''AWS Backup backup vault.'''
        return typing.cast("ResourceType", jsii.sget(cls, "BACKUP_BACKUP_VAULT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BACKUP_RECOVERY_POINT")
    def BACKUP_RECOVERY_POINT(cls) -> "ResourceType":
        '''AWS Backup recovery point.'''
        return typing.cast("ResourceType", jsii.sget(cls, "BACKUP_RECOVERY_POINT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BACKUP_REPORT_PLAN")
    def BACKUP_REPORT_PLAN(cls) -> "ResourceType":
        '''AWS Backup report plan.'''
        return typing.cast("ResourceType", jsii.sget(cls, "BACKUP_REPORT_PLAN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BATCH_COMPUTE_ENVIRONMENT")
    def BATCH_COMPUTE_ENVIRONMENT(cls) -> "ResourceType":
        '''AWS Batch compute environment.'''
        return typing.cast("ResourceType", jsii.sget(cls, "BATCH_COMPUTE_ENVIRONMENT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="BATCH_JOB_QUEUE")
    def BATCH_JOB_QUEUE(cls) -> "ResourceType":
        '''AWS Batch job queue.'''
        return typing.cast("ResourceType", jsii.sget(cls, "BATCH_JOB_QUEUE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUD9_ENVIRONMENT_EC2")
    def CLOUD9_ENVIRONMENT_EC2(cls) -> "ResourceType":
        '''AWS Cloud9 environment EC2.'''
        return typing.cast("ResourceType", jsii.sget(cls, "CLOUD9_ENVIRONMENT_EC2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFORMATION_STACK")
    def CLOUDFORMATION_STACK(cls) -> "ResourceType":
        '''AWS CloudFormation stack.'''
        return typing.cast("ResourceType", jsii.sget(cls, "CLOUDFORMATION_STACK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFRONT_DISTRIBUTION")
    def CLOUDFRONT_DISTRIBUTION(cls) -> "ResourceType":
        '''Amazon CloudFront Distribution.'''
        return typing.cast("ResourceType", jsii.sget(cls, "CLOUDFRONT_DISTRIBUTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFRONT_STREAMING_DISTRIBUTION")
    def CLOUDFRONT_STREAMING_DISTRIBUTION(cls) -> "ResourceType":
        '''Amazon CloudFront streaming distribution.'''
        return typing.cast("ResourceType", jsii.sget(cls, "CLOUDFRONT_STREAMING_DISTRIBUTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDTRAIL_TRAIL")
    def CLOUDTRAIL_TRAIL(cls) -> "ResourceType":
        '''AWS CloudTrail trail.'''
        return typing.cast("ResourceType", jsii.sget(cls, "CLOUDTRAIL_TRAIL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDWATCH_ALARM")
    def CLOUDWATCH_ALARM(cls) -> "ResourceType":
        '''Amazon CloudWatch Alarm.'''
        return typing.cast("ResourceType", jsii.sget(cls, "CLOUDWATCH_ALARM"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDWATCH_RUM_APP_MONITOR")
    def CLOUDWATCH_RUM_APP_MONITOR(cls) -> "ResourceType":
        '''Amazon CloudWatch RUM.'''
        return typing.cast("ResourceType", jsii.sget(cls, "CLOUDWATCH_RUM_APP_MONITOR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODEBUILD_PROJECT")
    def CODEBUILD_PROJECT(cls) -> "ResourceType":
        '''AWS CodeBuild project.'''
        return typing.cast("ResourceType", jsii.sget(cls, "CODEBUILD_PROJECT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODEDEPLOY_APPLICATION")
    def CODEDEPLOY_APPLICATION(cls) -> "ResourceType":
        '''AWS CodeDeploy application.'''
        return typing.cast("ResourceType", jsii.sget(cls, "CODEDEPLOY_APPLICATION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODEDEPLOY_DEPLOYMENT_CONFIG")
    def CODEDEPLOY_DEPLOYMENT_CONFIG(cls) -> "ResourceType":
        '''AWS CodeDeploy deployment config.'''
        return typing.cast("ResourceType", jsii.sget(cls, "CODEDEPLOY_DEPLOYMENT_CONFIG"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODEDEPLOY_DEPLOYMENT_GROUP")
    def CODEDEPLOY_DEPLOYMENT_GROUP(cls) -> "ResourceType":
        '''AWS CodeDeploy deployment group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "CODEDEPLOY_DEPLOYMENT_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CODEPIPELINE_PIPELINE")
    def CODEPIPELINE_PIPELINE(cls) -> "ResourceType":
        '''AWS CodePipeline pipeline.'''
        return typing.cast("ResourceType", jsii.sget(cls, "CODEPIPELINE_PIPELINE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CONFIG_CONFORMANCE_PACK_COMPLIANCE")
    def CONFIG_CONFORMANCE_PACK_COMPLIANCE(cls) -> "ResourceType":
        '''AWS Config conformance pack compliance.'''
        return typing.cast("ResourceType", jsii.sget(cls, "CONFIG_CONFORMANCE_PACK_COMPLIANCE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CONFIG_RESOURCE_COMPLIANCE")
    def CONFIG_RESOURCE_COMPLIANCE(cls) -> "ResourceType":
        '''AWS Config resource compliance.'''
        return typing.cast("ResourceType", jsii.sget(cls, "CONFIG_RESOURCE_COMPLIANCE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DATASYNC_LOCATION_EFS")
    def DATASYNC_LOCATION_EFS(cls) -> "ResourceType":
        '''AWS DataSync location EFS.'''
        return typing.cast("ResourceType", jsii.sget(cls, "DATASYNC_LOCATION_EFS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DATASYNC_LOCATION_FSX_LUSTRE")
    def DATASYNC_LOCATION_FSX_LUSTRE(cls) -> "ResourceType":
        '''AWS DataSync location FSx Lustre.'''
        return typing.cast("ResourceType", jsii.sget(cls, "DATASYNC_LOCATION_FSX_LUSTRE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DATASYNC_LOCATION_FSX_WINDOWS")
    def DATASYNC_LOCATION_FSX_WINDOWS(cls) -> "ResourceType":
        '''AWS DataSync location FSx Windows.'''
        return typing.cast("ResourceType", jsii.sget(cls, "DATASYNC_LOCATION_FSX_WINDOWS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DATASYNC_LOCATION_HDFS")
    def DATASYNC_LOCATION_HDFS(cls) -> "ResourceType":
        '''AWS DataSync location HDFS.'''
        return typing.cast("ResourceType", jsii.sget(cls, "DATASYNC_LOCATION_HDFS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DATASYNC_LOCATION_NFS")
    def DATASYNC_LOCATION_NFS(cls) -> "ResourceType":
        '''AWS DataSync location NFS.'''
        return typing.cast("ResourceType", jsii.sget(cls, "DATASYNC_LOCATION_NFS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DATASYNC_LOCATION_OBJECT_STORAGE")
    def DATASYNC_LOCATION_OBJECT_STORAGE(cls) -> "ResourceType":
        '''AWS DataSync location object storage.'''
        return typing.cast("ResourceType", jsii.sget(cls, "DATASYNC_LOCATION_OBJECT_STORAGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DATASYNC_LOCATION_S3")
    def DATASYNC_LOCATION_S3(cls) -> "ResourceType":
        '''AWS DataSync location S3.'''
        return typing.cast("ResourceType", jsii.sget(cls, "DATASYNC_LOCATION_S3"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DATASYNC_LOCATION_SMB")
    def DATASYNC_LOCATION_SMB(cls) -> "ResourceType":
        '''AWS DataSync location SMB.'''
        return typing.cast("ResourceType", jsii.sget(cls, "DATASYNC_LOCATION_SMB"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DATASYNC_TASK")
    def DATASYNC_TASK(cls) -> "ResourceType":
        '''AWS DataSync task.'''
        return typing.cast("ResourceType", jsii.sget(cls, "DATASYNC_TASK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DMS_EVENT_SUBSCRIPTION")
    def DMS_EVENT_SUBSCRIPTION(cls) -> "ResourceType":
        '''AWS DMS event subscription.'''
        return typing.cast("ResourceType", jsii.sget(cls, "DMS_EVENT_SUBSCRIPTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DMS_REPLICATION_SUBNET_GROUP")
    def DMS_REPLICATION_SUBNET_GROUP(cls) -> "ResourceType":
        '''AWS DMS replication subnet group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "DMS_REPLICATION_SUBNET_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="DYNAMODB_TABLE")
    def DYNAMODB_TABLE(cls) -> "ResourceType":
        '''Amazon DynamoDB Table.'''
        return typing.cast("ResourceType", jsii.sget(cls, "DYNAMODB_TABLE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EBS_VOLUME")
    def EBS_VOLUME(cls) -> "ResourceType":
        '''Elastic Block Store (EBS) volume.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EBS_VOLUME"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_CUSTOMER_GATEWAY")
    def EC2_CUSTOMER_GATEWAY(cls) -> "ResourceType":
        '''Amazon EC2 customer gateway.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_CUSTOMER_GATEWAY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_EGRESS_ONLY_INTERNET_GATEWAY")
    def EC2_EGRESS_ONLY_INTERNET_GATEWAY(cls) -> "ResourceType":
        '''EC2 Egress only internet gateway.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_EGRESS_ONLY_INTERNET_GATEWAY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_EIP")
    def EC2_EIP(cls) -> "ResourceType":
        '''EC2 Elastic IP.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_EIP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_FLOW_LOG")
    def EC2_FLOW_LOG(cls) -> "ResourceType":
        '''EC2 flow log.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_FLOW_LOG"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_HOST")
    def EC2_HOST(cls) -> "ResourceType":
        '''EC2 host.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_HOST"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_INSTANCE")
    def EC2_INSTANCE(cls) -> "ResourceType":
        '''EC2 instance.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_INSTANCE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_INTERNET_GATEWAY")
    def EC2_INTERNET_GATEWAY(cls) -> "ResourceType":
        '''Amazon EC2 internet gateway.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_INTERNET_GATEWAY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_LAUNCH_TEMPLATE")
    def EC2_LAUNCH_TEMPLATE(cls) -> "ResourceType":
        '''EC2 launch template.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_LAUNCH_TEMPLATE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_NAT_GATEWAY")
    def EC2_NAT_GATEWAY(cls) -> "ResourceType":
        '''EC2 NAT gateway.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_NAT_GATEWAY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_NETWORK_ACL")
    def EC2_NETWORK_ACL(cls) -> "ResourceType":
        '''Amazon EC2 network ACL.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_NETWORK_ACL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_NETWORK_INSIGHTS_ACCESS_SCOPE_ANALYSIS")
    def EC2_NETWORK_INSIGHTS_ACCESS_SCOPE_ANALYSIS(cls) -> "ResourceType":
        '''EC2 Network Insights Access Scope Analysis.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_NETWORK_INSIGHTS_ACCESS_SCOPE_ANALYSIS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_NETWORK_INTERFACE")
    def EC2_NETWORK_INTERFACE(cls) -> "ResourceType":
        '''EC2 Network Interface.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_NETWORK_INTERFACE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_REGISTERED_HA_INSTANCE")
    def EC2_REGISTERED_HA_INSTANCE(cls) -> "ResourceType":
        '''EC2 registered HA instance.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_REGISTERED_HA_INSTANCE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_ROUTE_TABLE")
    def EC2_ROUTE_TABLE(cls) -> "ResourceType":
        '''Amazon EC2 route table.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_ROUTE_TABLE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_SECURITY_GROUP")
    def EC2_SECURITY_GROUP(cls) -> "ResourceType":
        '''EC2 security group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_SECURITY_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_SUBNET")
    def EC2_SUBNET(cls) -> "ResourceType":
        '''Amazon EC2 subnet table.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_SUBNET"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_TRANSIT_GATEWAY")
    def EC2_TRANSIT_GATEWAY(cls) -> "ResourceType":
        '''EC2 transit gateway.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_TRANSIT_GATEWAY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_TRANSIT_GATEWAY_ATTACHMENT")
    def EC2_TRANSIT_GATEWAY_ATTACHMENT(cls) -> "ResourceType":
        '''EC2 transit gateway attachment.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_TRANSIT_GATEWAY_ATTACHMENT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_TRANSIT_GATEWAY_ROUTE_TABLE")
    def EC2_TRANSIT_GATEWAY_ROUTE_TABLE(cls) -> "ResourceType":
        '''EC2 transit gateway route table.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_TRANSIT_GATEWAY_ROUTE_TABLE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_VPC")
    def EC2_VPC(cls) -> "ResourceType":
        '''Amazon EC2 VPC.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_VPC"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_VPC_ENDPOINT")
    def EC2_VPC_ENDPOINT(cls) -> "ResourceType":
        '''EC2 VPC endpoint.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_VPC_ENDPOINT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_VPC_ENDPOINT_SERVICE")
    def EC2_VPC_ENDPOINT_SERVICE(cls) -> "ResourceType":
        '''EC2 VPC endpoint service.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_VPC_ENDPOINT_SERVICE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_VPC_PEERING_CONNECTION")
    def EC2_VPC_PEERING_CONNECTION(cls) -> "ResourceType":
        '''EC2 VPC peering connection.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_VPC_PEERING_CONNECTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_VPN_CONNECTION")
    def EC2_VPN_CONNECTION(cls) -> "ResourceType":
        '''Amazon EC2 VPN connection.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_VPN_CONNECTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC2_VPN_GATEWAY")
    def EC2_VPN_GATEWAY(cls) -> "ResourceType":
        '''Amazon EC2 VPN gateway.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EC2_VPN_GATEWAY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ECR_PUBLIC_REPOSITORY")
    def ECR_PUBLIC_REPOSITORY(cls) -> "ResourceType":
        '''Amazon ECR public repository.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ECR_PUBLIC_REPOSITORY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ECR_REGISTRY_POLICY")
    def ECR_REGISTRY_POLICY(cls) -> "ResourceType":
        '''Amazon ECR registry policy.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ECR_REGISTRY_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ECR_REPOSITORY")
    def ECR_REPOSITORY(cls) -> "ResourceType":
        '''Amazon ECR repository.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ECR_REPOSITORY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ECS_CLUSTER")
    def ECS_CLUSTER(cls) -> "ResourceType":
        '''Amazon ECS cluster.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ECS_CLUSTER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ECS_SERVICE")
    def ECS_SERVICE(cls) -> "ResourceType":
        '''Amazon ECS service.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ECS_SERVICE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ECS_TASK_DEFINITION")
    def ECS_TASK_DEFINITION(cls) -> "ResourceType":
        '''Amazon ECS task definition.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ECS_TASK_DEFINITION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EFS_ACCESS_POINT")
    def EFS_ACCESS_POINT(cls) -> "ResourceType":
        '''Amazon EFS access point.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EFS_ACCESS_POINT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EFS_FILE_SYSTEM")
    def EFS_FILE_SYSTEM(cls) -> "ResourceType":
        '''Amazon EFS file system.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EFS_FILE_SYSTEM"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EKS_ADDON")
    def EKS_ADDON(cls) -> "ResourceType":
        '''Amazon Elastic Kubernetes Service addon.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EKS_ADDON"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EKS_CLUSTER")
    def EKS_CLUSTER(cls) -> "ResourceType":
        '''Amazon Elastic Kubernetes Service cluster.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EKS_CLUSTER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EKS_IDENTITY_PROVIDER_CONFIG")
    def EKS_IDENTITY_PROVIDER_CONFIG(cls) -> "ResourceType":
        '''Amazon Elastic Kubernetes Service identity provider config.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EKS_IDENTITY_PROVIDER_CONFIG"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTIC_BEANSTALK_APPLICATION")
    def ELASTIC_BEANSTALK_APPLICATION(cls) -> "ResourceType":
        '''AWS Elastic Beanstalk (EB) application.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ELASTIC_BEANSTALK_APPLICATION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTIC_BEANSTALK_APPLICATION_VERSION")
    def ELASTIC_BEANSTALK_APPLICATION_VERSION(cls) -> "ResourceType":
        '''AWS Elastic Beanstalk (EB) application version.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ELASTIC_BEANSTALK_APPLICATION_VERSION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTIC_BEANSTALK_ENVIRONMENT")
    def ELASTIC_BEANSTALK_ENVIRONMENT(cls) -> "ResourceType":
        '''AWS Elastic Beanstalk (EB) environment.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ELASTIC_BEANSTALK_ENVIRONMENT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELASTICSEARCH_DOMAIN")
    def ELASTICSEARCH_DOMAIN(cls) -> "ResourceType":
        '''Amazon ElasticSearch domain.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ELASTICSEARCH_DOMAIN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELB_LOAD_BALANCER")
    def ELB_LOAD_BALANCER(cls) -> "ResourceType":
        '''AWS ELB classic load balancer.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ELB_LOAD_BALANCER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELBV2_LISTENER")
    def ELBV2_LISTENER(cls) -> "ResourceType":
        '''AWS ELBv2 application load balancer listener.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ELBV2_LISTENER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ELBV2_LOAD_BALANCER")
    def ELBV2_LOAD_BALANCER(cls) -> "ResourceType":
        '''AWS ELBv2 network load balancer or AWS ELBv2 application load balancer.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ELBV2_LOAD_BALANCER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EMR_SECURITY_CONFIGURATION")
    def EMR_SECURITY_CONFIGURATION(cls) -> "ResourceType":
        '''Amazon EMR security configuration.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EMR_SECURITY_CONFIGURATION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EVENTBRIDGE_API_DESTINATION")
    def EVENTBRIDGE_API_DESTINATION(cls) -> "ResourceType":
        '''Amazon EventBridge Api Destination.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EVENTBRIDGE_API_DESTINATION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EVENTBRIDGE_ARCHIVE")
    def EVENTBRIDGE_ARCHIVE(cls) -> "ResourceType":
        '''Amazon EventBridge Archive.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EVENTBRIDGE_ARCHIVE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EVENTBRIDGE_ENDPOINT")
    def EVENTBRIDGE_ENDPOINT(cls) -> "ResourceType":
        '''Amazon EventBridge Endpoint.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EVENTBRIDGE_ENDPOINT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EVENTBRIDGE_EVENTBUS")
    def EVENTBRIDGE_EVENTBUS(cls) -> "ResourceType":
        '''Amazon EventBridge EventBus.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EVENTBRIDGE_EVENTBUS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EVENTSCHEMAS_DISCOVERER")
    def EVENTSCHEMAS_DISCOVERER(cls) -> "ResourceType":
        '''Amazon EventBridge EventSchemas discoverer.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EVENTSCHEMAS_DISCOVERER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EVENTSCHEMAS_REGISTRY")
    def EVENTSCHEMAS_REGISTRY(cls) -> "ResourceType":
        '''Amazon EventBridge EventSchemas registry.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EVENTSCHEMAS_REGISTRY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EVENTSCHEMAS_REGISTRY_POLICY")
    def EVENTSCHEMAS_REGISTRY_POLICY(cls) -> "ResourceType":
        '''Amazon EventBridge EventSchemas registry policy.'''
        return typing.cast("ResourceType", jsii.sget(cls, "EVENTSCHEMAS_REGISTRY_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="FIS_EXPERIMENT_TEMPLATE")
    def FIS_EXPERIMENT_TEMPLATE(cls) -> "ResourceType":
        '''AWS Fault Injection Simulator Experiment_Template.'''
        return typing.cast("ResourceType", jsii.sget(cls, "FIS_EXPERIMENT_TEMPLATE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="FRAUDDETECTOR_ENTITY_TYPE")
    def FRAUDDETECTOR_ENTITY_TYPE(cls) -> "ResourceType":
        '''AWS FraudDetector entity type.'''
        return typing.cast("ResourceType", jsii.sget(cls, "FRAUDDETECTOR_ENTITY_TYPE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="FRAUDDETECTOR_LABEL")
    def FRAUDDETECTOR_LABEL(cls) -> "ResourceType":
        '''AWS FraudDetector label.'''
        return typing.cast("ResourceType", jsii.sget(cls, "FRAUDDETECTOR_LABEL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="FRAUDDETECTOR_OUTCOME")
    def FRAUDDETECTOR_OUTCOME(cls) -> "ResourceType":
        '''AWS FraudDetector outcome.'''
        return typing.cast("ResourceType", jsii.sget(cls, "FRAUDDETECTOR_OUTCOME"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="FRAUDDETECTOR_VARIABLE")
    def FRAUDDETECTOR_VARIABLE(cls) -> "ResourceType":
        '''AWS FraudDetector variable.'''
        return typing.cast("ResourceType", jsii.sget(cls, "FRAUDDETECTOR_VARIABLE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GLOBALACCELERATOR_ACCELERATOR")
    def GLOBALACCELERATOR_ACCELERATOR(cls) -> "ResourceType":
        '''AWS GlobalAccelerator accelerator.'''
        return typing.cast("ResourceType", jsii.sget(cls, "GLOBALACCELERATOR_ACCELERATOR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GLOBALACCELERATOR_ENDPOINT_GROUP")
    def GLOBALACCELERATOR_ENDPOINT_GROUP(cls) -> "ResourceType":
        '''AWS GlobalAccelerator endpoint group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "GLOBALACCELERATOR_ENDPOINT_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GLOBALACCELERATOR_LISTENER")
    def GLOBALACCELERATOR_LISTENER(cls) -> "ResourceType":
        '''AWS GlobalAccelerator listener.'''
        return typing.cast("ResourceType", jsii.sget(cls, "GLOBALACCELERATOR_LISTENER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GLUE_CLASSIFIER")
    def GLUE_CLASSIFIER(cls) -> "ResourceType":
        '''AWS Glue Classifier.'''
        return typing.cast("ResourceType", jsii.sget(cls, "GLUE_CLASSIFIER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GLUE_JOB")
    def GLUE_JOB(cls) -> "ResourceType":
        '''AWS Glue Job.'''
        return typing.cast("ResourceType", jsii.sget(cls, "GLUE_JOB"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GLUE_ML_TRANSFORM")
    def GLUE_ML_TRANSFORM(cls) -> "ResourceType":
        '''AWS Glue machine learning transform.'''
        return typing.cast("ResourceType", jsii.sget(cls, "GLUE_ML_TRANSFORM"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GUARDDUTY_DETECTOR")
    def GUARDDUTY_DETECTOR(cls) -> "ResourceType":
        '''Amazon GuardDuty detector.'''
        return typing.cast("ResourceType", jsii.sget(cls, "GUARDDUTY_DETECTOR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GUARDDUTY_FILTER")
    def GUARDDUTY_FILTER(cls) -> "ResourceType":
        '''Amazon GuardDuty Filter.'''
        return typing.cast("ResourceType", jsii.sget(cls, "GUARDDUTY_FILTER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GUARDDUTY_IP_SET")
    def GUARDDUTY_IP_SET(cls) -> "ResourceType":
        '''Amazon GuardDuty IP Set.'''
        return typing.cast("ResourceType", jsii.sget(cls, "GUARDDUTY_IP_SET"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GUARDDUTY_THREAT_INTEL_SET")
    def GUARDDUTY_THREAT_INTEL_SET(cls) -> "ResourceType":
        '''Amazon GuardDuty Threat Intel Set.'''
        return typing.cast("ResourceType", jsii.sget(cls, "GUARDDUTY_THREAT_INTEL_SET"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_ACCESSANALYZER_ANALYZER")
    def IAM_ACCESSANALYZER_ANALYZER(cls) -> "ResourceType":
        '''AWS IAM AccessAnalyzer analyzer.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IAM_ACCESSANALYZER_ANALYZER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_GROUP")
    def IAM_GROUP(cls) -> "ResourceType":
        '''AWS IAM group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IAM_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_POLICY")
    def IAM_POLICY(cls) -> "ResourceType":
        '''AWS IAM policy.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IAM_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_ROLE")
    def IAM_ROLE(cls) -> "ResourceType":
        '''AWS IAM role.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IAM_ROLE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IAM_USER")
    def IAM_USER(cls) -> "ResourceType":
        '''AWS IAM user.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IAM_USER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IMAGEBUILDER_CONTAINER_RECIPE")
    def IMAGEBUILDER_CONTAINER_RECIPE(cls) -> "ResourceType":
        '''EC2 Image Builder ContainerRecipe.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IMAGEBUILDER_CONTAINER_RECIPE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IMAGEBUILDER_DISTRIBUTION_CONFIGURATION")
    def IMAGEBUILDER_DISTRIBUTION_CONFIGURATION(cls) -> "ResourceType":
        '''EC2 Image Builder DistributionConfiguration.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IMAGEBUILDER_DISTRIBUTION_CONFIGURATION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IMAGEBUILDER_INFRASTRUCTURE_CONFIGURATION")
    def IMAGEBUILDER_INFRASTRUCTURE_CONFIGURATION(cls) -> "ResourceType":
        '''EC2 Image Builder InfrastructureConfiguration.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IMAGEBUILDER_INFRASTRUCTURE_CONFIGURATION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IOT_ANALYTICS_CHANNEL")
    def IOT_ANALYTICS_CHANNEL(cls) -> "ResourceType":
        '''AWS IoT Analytics channel.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IOT_ANALYTICS_CHANNEL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IOT_ANALYTICS_DATASET")
    def IOT_ANALYTICS_DATASET(cls) -> "ResourceType":
        '''AWS IoT Analytics dataset.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IOT_ANALYTICS_DATASET"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IOT_ANALYTICS_DATASTORE")
    def IOT_ANALYTICS_DATASTORE(cls) -> "ResourceType":
        '''AWS IoT Analytics datastore.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IOT_ANALYTICS_DATASTORE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IOT_ANALYTICS_PIPELINE")
    def IOT_ANALYTICS_PIPELINE(cls) -> "ResourceType":
        '''AWS IoT Analytics pipeline.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IOT_ANALYTICS_PIPELINE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IOT_AUTHORIZER")
    def IOT_AUTHORIZER(cls) -> "ResourceType":
        '''AWS IoT authorizer.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IOT_AUTHORIZER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IOT_DIMENSION")
    def IOT_DIMENSION(cls) -> "ResourceType":
        '''AWS IoT dimension.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IOT_DIMENSION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IOT_EVENTS_ALARM_MODEL")
    def IOT_EVENTS_ALARM_MODEL(cls) -> "ResourceType":
        '''AWS IoT Events Alarm Model.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IOT_EVENTS_ALARM_MODEL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IOT_EVENTS_DETECTOR_MODEL")
    def IOT_EVENTS_DETECTOR_MODEL(cls) -> "ResourceType":
        '''AWS IoT Events Detector Model.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IOT_EVENTS_DETECTOR_MODEL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IOT_EVENTS_INPUT")
    def IOT_EVENTS_INPUT(cls) -> "ResourceType":
        '''AWS IoT Events Input.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IOT_EVENTS_INPUT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IOT_MITIGATION_ACTION")
    def IOT_MITIGATION_ACTION(cls) -> "ResourceType":
        '''AWS IoT mitigation action.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IOT_MITIGATION_ACTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IOT_POLICY")
    def IOT_POLICY(cls) -> "ResourceType":
        '''AWS IoT policy.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IOT_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IOT_ROLE_ALIAS")
    def IOT_ROLE_ALIAS(cls) -> "ResourceType":
        '''AWS IoT role alias.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IOT_ROLE_ALIAS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IOT_SECURITY_PROFILE")
    def IOT_SECURITY_PROFILE(cls) -> "ResourceType":
        '''AWS IoT security profile.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IOT_SECURITY_PROFILE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IOT_SITEWISE_ASSETMODEL")
    def IOT_SITEWISE_ASSETMODEL(cls) -> "ResourceType":
        '''AWS IoT SiteWise asset model.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IOT_SITEWISE_ASSETMODEL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IOT_SITEWISE_DASHBOARD")
    def IOT_SITEWISE_DASHBOARD(cls) -> "ResourceType":
        '''AWS IoT SiteWise dashboard.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IOT_SITEWISE_DASHBOARD"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IOT_SITEWISE_PORTAL")
    def IOT_SITEWISE_PORTAL(cls) -> "ResourceType":
        '''AWS IoT SiteWise portal.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IOT_SITEWISE_PORTAL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IOT_SITEWISE_PROJECT")
    def IOT_SITEWISE_PROJECT(cls) -> "ResourceType":
        '''AWS IoT SiteWise project.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IOT_SITEWISE_PROJECT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IOT_TWINMAKER_ENTITY")
    def IOT_TWINMAKER_ENTITY(cls) -> "ResourceType":
        '''AWS IoT TwinMaker entity.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IOT_TWINMAKER_ENTITY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IOT_TWINMAKER_WORKSPACE")
    def IOT_TWINMAKER_WORKSPACE(cls) -> "ResourceType":
        '''AWS IoT TwinMaker workspace.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IOT_TWINMAKER_WORKSPACE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IVS_CHANNEL")
    def IVS_CHANNEL(cls) -> "ResourceType":
        '''Amazon Interactive Video Service (IVS) channel.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IVS_CHANNEL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IVS_PLAYBACK_KEYPAIR")
    def IVS_PLAYBACK_KEYPAIR(cls) -> "ResourceType":
        '''Amazon Interactive Video Service (IVS) playback key pair.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IVS_PLAYBACK_KEYPAIR"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="IVS_RECORDING_CONFIGURATION")
    def IVS_RECORDING_CONFIGURATION(cls) -> "ResourceType":
        '''Amazon Interactive Video Service (IVS) recording configuration.'''
        return typing.cast("ResourceType", jsii.sget(cls, "IVS_RECORDING_CONFIGURATION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="KINESIS_ANALYTICS_V2_APPLICATION")
    def KINESIS_ANALYTICS_V2_APPLICATION(cls) -> "ResourceType":
        '''Amazon Kinesis Analytics V2 application.'''
        return typing.cast("ResourceType", jsii.sget(cls, "KINESIS_ANALYTICS_V2_APPLICATION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="KINESIS_STREAM")
    def KINESIS_STREAM(cls) -> "ResourceType":
        '''Amazon Kinesis stream.'''
        return typing.cast("ResourceType", jsii.sget(cls, "KINESIS_STREAM"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="KINESIS_STREAM_CONSUMER")
    def KINESIS_STREAM_CONSUMER(cls) -> "ResourceType":
        '''Amazon Kinesis stream consumer.'''
        return typing.cast("ResourceType", jsii.sget(cls, "KINESIS_STREAM_CONSUMER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="KMS_KEY")
    def KMS_KEY(cls) -> "ResourceType":
        '''AWS KMS Key.'''
        return typing.cast("ResourceType", jsii.sget(cls, "KMS_KEY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LAMBDA_FUNCTION")
    def LAMBDA_FUNCTION(cls) -> "ResourceType":
        '''AWS Lambda function.'''
        return typing.cast("ResourceType", jsii.sget(cls, "LAMBDA_FUNCTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LIGHTSAIL_BUCKET")
    def LIGHTSAIL_BUCKET(cls) -> "ResourceType":
        '''AWS Lightsail bucket.'''
        return typing.cast("ResourceType", jsii.sget(cls, "LIGHTSAIL_BUCKET"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LIGHTSAIL_CERTIFICATE")
    def LIGHTSAIL_CERTIFICATE(cls) -> "ResourceType":
        '''Amazon Lightsail Certificate.'''
        return typing.cast("ResourceType", jsii.sget(cls, "LIGHTSAIL_CERTIFICATE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LIGHTSAIL_DISK")
    def LIGHTSAIL_DISK(cls) -> "ResourceType":
        '''Amazon Lightsail Disk.'''
        return typing.cast("ResourceType", jsii.sget(cls, "LIGHTSAIL_DISK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LIGHTSAIL_STATIC_IP")
    def LIGHTSAIL_STATIC_IP(cls) -> "ResourceType":
        '''AWS Lightsail static IP.'''
        return typing.cast("ResourceType", jsii.sget(cls, "LIGHTSAIL_STATIC_IP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="MEDIAPACKAGE_PACKAGING_GROUP")
    def MEDIAPACKAGE_PACKAGING_GROUP(cls) -> "ResourceType":
        '''AWS Elemental MediaPackage packaging group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "MEDIAPACKAGE_PACKAGING_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="MSK_CLUSTER")
    def MSK_CLUSTER(cls) -> "ResourceType":
        '''Amazon MSK cluster.'''
        return typing.cast("ResourceType", jsii.sget(cls, "MSK_CLUSTER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NETWORK_FIREWALL_FIREWALL")
    def NETWORK_FIREWALL_FIREWALL(cls) -> "ResourceType":
        '''AWS Network Firewall Firewall.'''
        return typing.cast("ResourceType", jsii.sget(cls, "NETWORK_FIREWALL_FIREWALL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NETWORK_FIREWALL_FIREWALL_POLICY")
    def NETWORK_FIREWALL_FIREWALL_POLICY(cls) -> "ResourceType":
        '''AWS Network Firewall Firewall Policy.'''
        return typing.cast("ResourceType", jsii.sget(cls, "NETWORK_FIREWALL_FIREWALL_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="NETWORK_FIREWALL_RULE_GROUP")
    def NETWORK_FIREWALL_RULE_GROUP(cls) -> "ResourceType":
        '''AWS Network Firewall Rule Group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "NETWORK_FIREWALL_RULE_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="OPENSEARCH_DOMAIN")
    def OPENSEARCH_DOMAIN(cls) -> "ResourceType":
        '''Amazon OpenSearch domain.'''
        return typing.cast("ResourceType", jsii.sget(cls, "OPENSEARCH_DOMAIN"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="QLDB_LEDGER")
    def QLDB_LEDGER(cls) -> "ResourceType":
        '''Amazon QLDB ledger.'''
        return typing.cast("ResourceType", jsii.sget(cls, "QLDB_LEDGER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_DB_CLUSTER")
    def RDS_DB_CLUSTER(cls) -> "ResourceType":
        '''Amazon RDS database cluster.'''
        return typing.cast("ResourceType", jsii.sget(cls, "RDS_DB_CLUSTER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_DB_CLUSTER_SNAPSHOT")
    def RDS_DB_CLUSTER_SNAPSHOT(cls) -> "ResourceType":
        '''Amazon RDS database cluster snapshot.'''
        return typing.cast("ResourceType", jsii.sget(cls, "RDS_DB_CLUSTER_SNAPSHOT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_DB_INSTANCE")
    def RDS_DB_INSTANCE(cls) -> "ResourceType":
        '''Amazon RDS database instance.'''
        return typing.cast("ResourceType", jsii.sget(cls, "RDS_DB_INSTANCE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_DB_SECURITY_GROUP")
    def RDS_DB_SECURITY_GROUP(cls) -> "ResourceType":
        '''Amazon RDS database security group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "RDS_DB_SECURITY_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_DB_SNAPSHOT")
    def RDS_DB_SNAPSHOT(cls) -> "ResourceType":
        '''Amazon RDS database snapshot.'''
        return typing.cast("ResourceType", jsii.sget(cls, "RDS_DB_SNAPSHOT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_DB_SUBNET_GROUP")
    def RDS_DB_SUBNET_GROUP(cls) -> "ResourceType":
        '''Amazon RDS database subnet group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "RDS_DB_SUBNET_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_EVENT_SUBSCRIPTION")
    def RDS_EVENT_SUBSCRIPTION(cls) -> "ResourceType":
        '''Amazon RDS event subscription.'''
        return typing.cast("ResourceType", jsii.sget(cls, "RDS_EVENT_SUBSCRIPTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RDS_GLOBAL_CLUSTER")
    def RDS_GLOBAL_CLUSTER(cls) -> "ResourceType":
        '''Amazon RDS global cluster.'''
        return typing.cast("ResourceType", jsii.sget(cls, "RDS_GLOBAL_CLUSTER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_CLUSTER")
    def REDSHIFT_CLUSTER(cls) -> "ResourceType":
        '''Amazon Redshift cluster.'''
        return typing.cast("ResourceType", jsii.sget(cls, "REDSHIFT_CLUSTER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_CLUSTER_PARAMETER_GROUP")
    def REDSHIFT_CLUSTER_PARAMETER_GROUP(cls) -> "ResourceType":
        '''Amazon Redshift cluster parameter group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "REDSHIFT_CLUSTER_PARAMETER_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_CLUSTER_SECURITY_GROUP")
    def REDSHIFT_CLUSTER_SECURITY_GROUP(cls) -> "ResourceType":
        '''Amazon Redshift cluster security group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "REDSHIFT_CLUSTER_SECURITY_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_CLUSTER_SNAPSHOT")
    def REDSHIFT_CLUSTER_SNAPSHOT(cls) -> "ResourceType":
        '''Amazon Redshift cluster snapshot.'''
        return typing.cast("ResourceType", jsii.sget(cls, "REDSHIFT_CLUSTER_SNAPSHOT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_CLUSTER_SUBNET_GROUP")
    def REDSHIFT_CLUSTER_SUBNET_GROUP(cls) -> "ResourceType":
        '''Amazon Redshift cluster subnet group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "REDSHIFT_CLUSTER_SUBNET_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REDSHIFT_EVENT_SUBSCRIPTION")
    def REDSHIFT_EVENT_SUBSCRIPTION(cls) -> "ResourceType":
        '''Amazon Redshift event subscription.'''
        return typing.cast("ResourceType", jsii.sget(cls, "REDSHIFT_EVENT_SUBSCRIPTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RESILIENCEHUB_RESILIENCY_POLICY")
    def RESILIENCEHUB_RESILIENCY_POLICY(cls) -> "ResourceType":
        '''AWS ResilienceHub resiliency policy.'''
        return typing.cast("ResourceType", jsii.sget(cls, "RESILIENCEHUB_RESILIENCY_POLICY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ROUTE53_HEALTH_CHECK")
    def ROUTE53_HEALTH_CHECK(cls) -> "ResourceType":
        '''Amazon Route53 Health Check.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ROUTE53_HEALTH_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ROUTE53_HOSTED_ZONE")
    def ROUTE53_HOSTED_ZONE(cls) -> "ResourceType":
        '''Amazon Route53 Hosted Zone.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ROUTE53_HOSTED_ZONE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ROUTE53_RECOVERY_READINESS_CELL")
    def ROUTE53_RECOVERY_READINESS_CELL(cls) -> "ResourceType":
        '''Amazon Route 53 Application Recovery Controller Cell.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ROUTE53_RECOVERY_READINESS_CELL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ROUTE53_RECOVERY_READINESS_READINESS_CHECK")
    def ROUTE53_RECOVERY_READINESS_READINESS_CHECK(cls) -> "ResourceType":
        '''Amazon Route 53 Application Recovery Controller Readiness Check.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ROUTE53_RECOVERY_READINESS_READINESS_CHECK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ROUTE53_RECOVERY_READINESS_RECOVERY_GROUP")
    def ROUTE53_RECOVERY_READINESS_RECOVERY_GROUP(cls) -> "ResourceType":
        '''Amazon Route53 recovery readiness recovery group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ROUTE53_RECOVERY_READINESS_RECOVERY_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ROUTE53_RESOLVER_RESOLVER_ENDPOINT")
    def ROUTE53_RESOLVER_RESOLVER_ENDPOINT(cls) -> "ResourceType":
        '''Amazon Route53 resolver resolver endpoint.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ROUTE53_RESOLVER_RESOLVER_ENDPOINT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ROUTE53_RESOLVER_RESOLVER_RULE")
    def ROUTE53_RESOLVER_RESOLVER_RULE(cls) -> "ResourceType":
        '''Amazon Route53 resolver resolver rule.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ROUTE53_RESOLVER_RESOLVER_RULE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ROUTE53_RESOLVER_RESOLVER_RULE_ASSOCIATION")
    def ROUTE53_RESOLVER_RESOLVER_RULE_ASSOCIATION(cls) -> "ResourceType":
        '''Amazon Route53 resolver resolver rule association.'''
        return typing.cast("ResourceType", jsii.sget(cls, "ROUTE53_RESOLVER_RESOLVER_RULE_ASSOCIATION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_ACCOUNT_PUBLIC_ACCESS_BLOCK")
    def S3_ACCOUNT_PUBLIC_ACCESS_BLOCK(cls) -> "ResourceType":
        '''Amazon S3 account public access block.'''
        return typing.cast("ResourceType", jsii.sget(cls, "S3_ACCOUNT_PUBLIC_ACCESS_BLOCK"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_BUCKET")
    def S3_BUCKET(cls) -> "ResourceType":
        '''Amazon S3 bucket.'''
        return typing.cast("ResourceType", jsii.sget(cls, "S3_BUCKET"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="S3_MULTIREGION_ACCESS_POINT")
    def S3_MULTIREGION_ACCESS_POINT(cls) -> "ResourceType":
        '''Amazon S3 Multi-Region Access Point.'''
        return typing.cast("ResourceType", jsii.sget(cls, "S3_MULTIREGION_ACCESS_POINT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SAGEMAKER_CODE_REPOSITORY")
    def SAGEMAKER_CODE_REPOSITORY(cls) -> "ResourceType":
        '''Amazon SageMaker code repository.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SAGEMAKER_CODE_REPOSITORY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SAGEMAKER_MODEL")
    def SAGEMAKER_MODEL(cls) -> "ResourceType":
        '''Amazon SageMaker model.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SAGEMAKER_MODEL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SAGEMAKER_NOTEBOOK_INSTANCE")
    def SAGEMAKER_NOTEBOOK_INSTANCE(cls) -> "ResourceType":
        '''Amazon SageMaker notebook instance.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SAGEMAKER_NOTEBOOK_INSTANCE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SAGEMAKER_WORKTEAM")
    def SAGEMAKER_WORKTEAM(cls) -> "ResourceType":
        '''Amazon SageMaker workteam.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SAGEMAKER_WORKTEAM"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SECRETS_MANAGER_SECRET")
    def SECRETS_MANAGER_SECRET(cls) -> "ResourceType":
        '''AWS Secrets Manager secret.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SECRETS_MANAGER_SECRET"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SERVICE_CATALOG_CLOUDFORMATION_PRODUCT")
    def SERVICE_CATALOG_CLOUDFORMATION_PRODUCT(cls) -> "ResourceType":
        '''AWS Service Catalog CloudFormation product.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SERVICE_CATALOG_CLOUDFORMATION_PRODUCT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SERVICE_CATALOG_CLOUDFORMATION_PROVISIONED_PRODUCT")
    def SERVICE_CATALOG_CLOUDFORMATION_PROVISIONED_PRODUCT(cls) -> "ResourceType":
        '''AWS Service Catalog CloudFormation provisioned product.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SERVICE_CATALOG_CLOUDFORMATION_PROVISIONED_PRODUCT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SERVICE_CATALOG_PORTFOLIO")
    def SERVICE_CATALOG_PORTFOLIO(cls) -> "ResourceType":
        '''AWS Service Catalog portfolio.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SERVICE_CATALOG_PORTFOLIO"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SERVICEDISCOVERY_HTTP_NAMESPACE")
    def SERVICEDISCOVERY_HTTP_NAMESPACE(cls) -> "ResourceType":
        '''AWS Cloud Map(ServiceDiscovery) Http Namespace.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SERVICEDISCOVERY_HTTP_NAMESPACE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SERVICEDISCOVERY_PUBLIC_DNS_NAMESPACE")
    def SERVICEDISCOVERY_PUBLIC_DNS_NAMESPACE(cls) -> "ResourceType":
        '''AWS Cloud Map(ServiceDiscovery) Public Dns Namespace.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SERVICEDISCOVERY_PUBLIC_DNS_NAMESPACE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SERVICEDISCOVERY_SERVICE")
    def SERVICEDISCOVERY_SERVICE(cls) -> "ResourceType":
        '''AWS Cloud Map(ServiceDiscovery) service.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SERVICEDISCOVERY_SERVICE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SES_CONFIGURATION_SET")
    def SES_CONFIGURATION_SET(cls) -> "ResourceType":
        '''Amazon SES Configuration Set.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SES_CONFIGURATION_SET"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SES_CONTACT_LIST")
    def SES_CONTACT_LIST(cls) -> "ResourceType":
        '''Amazon SES Contact List.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SES_CONTACT_LIST"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SES_RECEIPT_FILTER")
    def SES_RECEIPT_FILTER(cls) -> "ResourceType":
        '''Amazon SES ReceiptFilter.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SES_RECEIPT_FILTER"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SES_RECEIPT_RECEIPT_RULE_SET")
    def SES_RECEIPT_RECEIPT_RULE_SET(cls) -> "ResourceType":
        '''Amazon SES ReceiptRuleSet.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SES_RECEIPT_RECEIPT_RULE_SET"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SES_TEMPLATE")
    def SES_TEMPLATE(cls) -> "ResourceType":
        '''Amazon SES Template.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SES_TEMPLATE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SHIELD_PROTECTION")
    def SHIELD_PROTECTION(cls) -> "ResourceType":
        '''AWS Shield protection.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SHIELD_PROTECTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SHIELD_REGIONAL_PROTECTION")
    def SHIELD_REGIONAL_PROTECTION(cls) -> "ResourceType":
        '''AWS Shield regional protection.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SHIELD_REGIONAL_PROTECTION"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SNS_TOPIC")
    def SNS_TOPIC(cls) -> "ResourceType":
        '''Amazon SNS topic.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SNS_TOPIC"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SQS_QUEUE")
    def SQS_QUEUE(cls) -> "ResourceType":
        '''Amazon SQS queue.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SQS_QUEUE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="STEPFUNCTIONS_ACTIVITY")
    def STEPFUNCTIONS_ACTIVITY(cls) -> "ResourceType":
        '''AWS StepFunctions activity.'''
        return typing.cast("ResourceType", jsii.sget(cls, "STEPFUNCTIONS_ACTIVITY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="STEPFUNCTIONS_STATE_MACHINE")
    def STEPFUNCTIONS_STATE_MACHINE(cls) -> "ResourceType":
        '''AWS StepFunctions state machine.'''
        return typing.cast("ResourceType", jsii.sget(cls, "STEPFUNCTIONS_STATE_MACHINE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYSTEMS_MANAGER_ASSOCIATION_COMPLIANCE")
    def SYSTEMS_MANAGER_ASSOCIATION_COMPLIANCE(cls) -> "ResourceType":
        '''AWS Systems Manager association compliance.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SYSTEMS_MANAGER_ASSOCIATION_COMPLIANCE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYSTEMS_MANAGER_FILE_DATA")
    def SYSTEMS_MANAGER_FILE_DATA(cls) -> "ResourceType":
        '''AWS Systems Manager file data.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SYSTEMS_MANAGER_FILE_DATA"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYSTEMS_MANAGER_MANAGED_INSTANCE_INVENTORY")
    def SYSTEMS_MANAGER_MANAGED_INSTANCE_INVENTORY(cls) -> "ResourceType":
        '''AWS Systems Manager managed instance inventory.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SYSTEMS_MANAGER_MANAGED_INSTANCE_INVENTORY"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYSTEMS_MANAGER_PATCH_COMPLIANCE")
    def SYSTEMS_MANAGER_PATCH_COMPLIANCE(cls) -> "ResourceType":
        '''AWS Systems Manager patch compliance.'''
        return typing.cast("ResourceType", jsii.sget(cls, "SYSTEMS_MANAGER_PATCH_COMPLIANCE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="TRANSFER_WORKFLOW")
    def TRANSFER_WORKFLOW(cls) -> "ResourceType":
        '''AWS Transfer workflow.'''
        return typing.cast("ResourceType", jsii.sget(cls, "TRANSFER_WORKFLOW"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_RATE_BASED_RULE")
    def WAF_RATE_BASED_RULE(cls) -> "ResourceType":
        '''AWS WAF rate based rule.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WAF_RATE_BASED_RULE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_REGIONAL_RATE_BASED_RULE")
    def WAF_REGIONAL_RATE_BASED_RULE(cls) -> "ResourceType":
        '''AWS WAF regional rate based rule.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WAF_REGIONAL_RATE_BASED_RULE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_REGIONAL_RULE")
    def WAF_REGIONAL_RULE(cls) -> "ResourceType":
        '''AWS WAF regional rule.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WAF_REGIONAL_RULE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_REGIONAL_RULE_GROUP")
    def WAF_REGIONAL_RULE_GROUP(cls) -> "ResourceType":
        '''AWS WAF regional rule group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WAF_REGIONAL_RULE_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_REGIONAL_WEB_ACL")
    def WAF_REGIONAL_WEB_ACL(cls) -> "ResourceType":
        '''AWS WAF web ACL.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WAF_REGIONAL_WEB_ACL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_RULE")
    def WAF_RULE(cls) -> "ResourceType":
        '''AWS WAF rule.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WAF_RULE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_RULE_GROUP")
    def WAF_RULE_GROUP(cls) -> "ResourceType":
        '''AWS WAF rule group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WAF_RULE_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAF_WEB_ACL")
    def WAF_WEB_ACL(cls) -> "ResourceType":
        '''AWS WAF web ACL.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WAF_WEB_ACL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAFV2_IP_SET")
    def WAFV2_IP_SET(cls) -> "ResourceType":
        '''AWS WAFv2 ip set.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WAFV2_IP_SET"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAFV2_MANAGED_RULE_SET")
    def WAFV2_MANAGED_RULE_SET(cls) -> "ResourceType":
        '''AWS WAFv2 managed rule set.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WAFV2_MANAGED_RULE_SET"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAFV2_REGEX_PATTERN_SET")
    def WAFV2_REGEX_PATTERN_SET(cls) -> "ResourceType":
        '''AWS WAFv2 regex pattern set.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WAFV2_REGEX_PATTERN_SET"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAFV2_RULE_GROUP")
    def WAFV2_RULE_GROUP(cls) -> "ResourceType":
        '''AWS WAFv2 rule group.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WAFV2_RULE_GROUP"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WAFV2_WEB_ACL")
    def WAFV2_WEB_ACL(cls) -> "ResourceType":
        '''AWS WAFv2 web ACL.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WAFV2_WEB_ACL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WORKSPACES_CONNECTION_ALIAS")
    def WORKSPACES_CONNECTION_ALIAS(cls) -> "ResourceType":
        '''Amazon WorkSpaces connection alias.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WORKSPACES_CONNECTION_ALIAS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="WORKSPACES_WORKSPACE")
    def WORKSPACES_WORKSPACE(cls) -> "ResourceType":
        '''Amazon WorkSpaces workSpace.'''
        return typing.cast("ResourceType", jsii.sget(cls, "WORKSPACES_WORKSPACE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="XRAY_ENCRYPTION_CONFIGURATION")
    def XRAY_ENCRYPTION_CONFIGURATION(cls) -> "ResourceType":
        '''AWS X-Ray encryption configuration.'''
        return typing.cast("ResourceType", jsii.sget(cls, "XRAY_ENCRYPTION_CONFIGURATION"))

    @builtins.property
    @jsii.member(jsii_name="complianceResourceType")
    def compliance_resource_type(self) -> builtins.str:
        '''Valid value of resource type.'''
        return typing.cast(builtins.str, jsii.get(self, "complianceResourceType"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_config.RuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "config_rule_name": "configRuleName",
        "description": "description",
        "input_parameters": "inputParameters",
        "maximum_execution_frequency": "maximumExecutionFrequency",
        "rule_scope": "ruleScope",
    },
)
class RuleProps:
    def __init__(
        self,
        *,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
        rule_scope: typing.Optional["RuleScope"] = None,
    ) -> None:
        '''Construction properties for a new rule.

        :param config_rule_name: A name for the AWS Config rule. Default: - CloudFormation generated name
        :param description: A description about this AWS Config rule. Default: - No description
        :param input_parameters: Input parameter values that are passed to the AWS Config rule. Default: - No input parameters
        :param maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        :param rule_scope: Defines which resources trigger an evaluation for an AWS Config rule. Default: - evaluations for the rule are triggered when any resource in the recording group changes.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_config as config
            
            # input_parameters: Any
            # rule_scope: config.RuleScope
            
            rule_props = config.RuleProps(
                config_rule_name="configRuleName",
                description="description",
                input_parameters={
                    "input_parameters_key": input_parameters
                },
                maximum_execution_frequency=config.MaximumExecutionFrequency.ONE_HOUR,
                rule_scope=rule_scope
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__789e7d0bc168eb66eb1a98c5813daac930a5d1a0a7544dd838595180eccba39e)
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument input_parameters", value=input_parameters, expected_type=type_hints["input_parameters"])
            check_type(argname="argument maximum_execution_frequency", value=maximum_execution_frequency, expected_type=type_hints["maximum_execution_frequency"])
            check_type(argname="argument rule_scope", value=rule_scope, expected_type=type_hints["rule_scope"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if config_rule_name is not None:
            self._values["config_rule_name"] = config_rule_name
        if description is not None:
            self._values["description"] = description
        if input_parameters is not None:
            self._values["input_parameters"] = input_parameters
        if maximum_execution_frequency is not None:
            self._values["maximum_execution_frequency"] = maximum_execution_frequency
        if rule_scope is not None:
            self._values["rule_scope"] = rule_scope

    @builtins.property
    def config_rule_name(self) -> typing.Optional[builtins.str]:
        '''A name for the AWS Config rule.

        :default: - CloudFormation generated name
        '''
        result = self._values.get("config_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description about this AWS Config rule.

        :default: - No description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Input parameter values that are passed to the AWS Config rule.

        :default: - No input parameters
        '''
        result = self._values.get("input_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def maximum_execution_frequency(self) -> typing.Optional[MaximumExecutionFrequency]:
        '''The maximum frequency at which the AWS Config rule runs evaluations.

        :default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        '''
        result = self._values.get("maximum_execution_frequency")
        return typing.cast(typing.Optional[MaximumExecutionFrequency], result)

    @builtins.property
    def rule_scope(self) -> typing.Optional["RuleScope"]:
        '''Defines which resources trigger an evaluation for an AWS Config rule.

        :default: - evaluations for the rule are triggered when any resource in the recording group changes.
        '''
        result = self._values.get("rule_scope")
        return typing.cast(typing.Optional["RuleScope"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RuleScope(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.aws_config.RuleScope"):
    '''Determines which resources trigger an evaluation of an AWS Config rule.

    :exampleMetadata: infused

    Example::

        # Lambda function containing logic that evaluates compliance with the rule.
        eval_compliance_fn = lambda_.Function(self, "CustomFunction",
            code=lambda_.AssetCode.from_inline("exports.handler = (event) => console.log(event);"),
            handler="index.handler",
            runtime=lambda_.Runtime.NODEJS_18_X
        )
        
        # A custom rule that runs on configuration changes of EC2 instances
        custom_rule = config.CustomRule(self, "Custom",
            configuration_changes=True,
            lambda_function=eval_compliance_fn,
            rule_scope=config.RuleScope.from_resource(config.ResourceType.EC2_INSTANCE)
        )
    '''

    @jsii.member(jsii_name="fromResource")
    @builtins.classmethod
    def from_resource(
        cls,
        resource_type: ResourceType,
        resource_id: typing.Optional[builtins.str] = None,
    ) -> "RuleScope":
        '''restricts scope of changes to a specific resource type or resource identifier.

        :param resource_type: -
        :param resource_id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c3113bd3d59601fad88eff4129cb100fd6ea61855418c78d070b9b942b6a3fd)
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
        return typing.cast("RuleScope", jsii.sinvoke(cls, "fromResource", [resource_type, resource_id]))

    @jsii.member(jsii_name="fromResources")
    @builtins.classmethod
    def from_resources(
        cls,
        resource_types: typing.Sequence[ResourceType],
    ) -> "RuleScope":
        '''restricts scope of changes to specific resource types.

        :param resource_types: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02f717c6b93d162c57dd0e440602591d6826daf133eb9d2cd6476d3ff4632896)
            check_type(argname="argument resource_types", value=resource_types, expected_type=type_hints["resource_types"])
        return typing.cast("RuleScope", jsii.sinvoke(cls, "fromResources", [resource_types]))

    @jsii.member(jsii_name="fromTag")
    @builtins.classmethod
    def from_tag(
        cls,
        key: builtins.str,
        value: typing.Optional[builtins.str] = None,
    ) -> "RuleScope":
        '''restricts scope of changes to a specific tag.

        :param key: -
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__824a576061a9e684cc0cf31a6506e1aa0490f392890aaceb8f7c4288d4145499)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("RuleScope", jsii.sinvoke(cls, "fromTag", [key, value]))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> typing.Optional[builtins.str]:
        '''tag key applied to resources that will trigger evaluation of a rule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "key"))

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> typing.Optional[builtins.str]:
        '''ID of the only AWS resource that will trigger evaluation of a rule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceId"))

    @builtins.property
    @jsii.member(jsii_name="resourceTypes")
    def resource_types(self) -> typing.Optional[typing.List[ResourceType]]:
        '''Resource types that will trigger evaluation of a rule.'''
        return typing.cast(typing.Optional[typing.List[ResourceType]], jsii.get(self, "resourceTypes"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> typing.Optional[builtins.str]:
        '''tag value applied to resources that will trigger evaluation of a rule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "value"))


class AccessKeysRotated(
    ManagedRule,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_config.AccessKeysRotated",
):
    '''Checks whether the active access keys are rotated within the number of days specified in ``maxAge``.

    :see: https://docs.aws.amazon.com/config/latest/developerguide/access-keys-rotated.html
    :resource: AWS::Config::ConfigRule
    :exampleMetadata: infused

    Example::

        # compliant if access keys have been rotated within the last 90 days
        config.AccessKeysRotated(self, "AccessKeyRotated")
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        max_age: typing.Optional[_Duration_4839e8c3] = None,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
        rule_scope: typing.Optional[RuleScope] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param max_age: The maximum number of days within which the access keys must be rotated. Default: Duration.days(90)
        :param config_rule_name: A name for the AWS Config rule. Default: - CloudFormation generated name
        :param description: A description about this AWS Config rule. Default: - No description
        :param input_parameters: Input parameter values that are passed to the AWS Config rule. Default: - No input parameters
        :param maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        :param rule_scope: Defines which resources trigger an evaluation for an AWS Config rule. Default: - evaluations for the rule are triggered when any resource in the recording group changes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__169ed3b4e4a53c1239b7388f8b4f342054686b6693630d0139a3f739cdfadf74)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AccessKeysRotatedProps(
            max_age=max_age,
            config_rule_name=config_rule_name,
            description=description,
            input_parameters=input_parameters,
            maximum_execution_frequency=maximum_execution_frequency,
            rule_scope=rule_scope,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_config.AccessKeysRotatedProps",
    jsii_struct_bases=[RuleProps],
    name_mapping={
        "config_rule_name": "configRuleName",
        "description": "description",
        "input_parameters": "inputParameters",
        "maximum_execution_frequency": "maximumExecutionFrequency",
        "rule_scope": "ruleScope",
        "max_age": "maxAge",
    },
)
class AccessKeysRotatedProps(RuleProps):
    def __init__(
        self,
        *,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
        rule_scope: typing.Optional[RuleScope] = None,
        max_age: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Construction properties for a AccessKeysRotated.

        :param config_rule_name: A name for the AWS Config rule. Default: - CloudFormation generated name
        :param description: A description about this AWS Config rule. Default: - No description
        :param input_parameters: Input parameter values that are passed to the AWS Config rule. Default: - No input parameters
        :param maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        :param rule_scope: Defines which resources trigger an evaluation for an AWS Config rule. Default: - evaluations for the rule are triggered when any resource in the recording group changes.
        :param max_age: The maximum number of days within which the access keys must be rotated. Default: Duration.days(90)

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_config as config
            
            # input_parameters: Any
            # rule_scope: config.RuleScope
            
            access_keys_rotated_props = config.AccessKeysRotatedProps(
                config_rule_name="configRuleName",
                description="description",
                input_parameters={
                    "input_parameters_key": input_parameters
                },
                max_age=cdk.Duration.minutes(30),
                maximum_execution_frequency=config.MaximumExecutionFrequency.ONE_HOUR,
                rule_scope=rule_scope
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__777e9fc45f9c8a322b98f9c1a5e59fa61b582e46ce2e628d20a703d225da6262)
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument input_parameters", value=input_parameters, expected_type=type_hints["input_parameters"])
            check_type(argname="argument maximum_execution_frequency", value=maximum_execution_frequency, expected_type=type_hints["maximum_execution_frequency"])
            check_type(argname="argument rule_scope", value=rule_scope, expected_type=type_hints["rule_scope"])
            check_type(argname="argument max_age", value=max_age, expected_type=type_hints["max_age"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if config_rule_name is not None:
            self._values["config_rule_name"] = config_rule_name
        if description is not None:
            self._values["description"] = description
        if input_parameters is not None:
            self._values["input_parameters"] = input_parameters
        if maximum_execution_frequency is not None:
            self._values["maximum_execution_frequency"] = maximum_execution_frequency
        if rule_scope is not None:
            self._values["rule_scope"] = rule_scope
        if max_age is not None:
            self._values["max_age"] = max_age

    @builtins.property
    def config_rule_name(self) -> typing.Optional[builtins.str]:
        '''A name for the AWS Config rule.

        :default: - CloudFormation generated name
        '''
        result = self._values.get("config_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description about this AWS Config rule.

        :default: - No description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Input parameter values that are passed to the AWS Config rule.

        :default: - No input parameters
        '''
        result = self._values.get("input_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def maximum_execution_frequency(self) -> typing.Optional[MaximumExecutionFrequency]:
        '''The maximum frequency at which the AWS Config rule runs evaluations.

        :default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        '''
        result = self._values.get("maximum_execution_frequency")
        return typing.cast(typing.Optional[MaximumExecutionFrequency], result)

    @builtins.property
    def rule_scope(self) -> typing.Optional[RuleScope]:
        '''Defines which resources trigger an evaluation for an AWS Config rule.

        :default: - evaluations for the rule are triggered when any resource in the recording group changes.
        '''
        result = self._values.get("rule_scope")
        return typing.cast(typing.Optional[RuleScope], result)

    @builtins.property
    def max_age(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum number of days within which the access keys must be rotated.

        :default: Duration.days(90)
        '''
        result = self._values.get("max_age")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessKeysRotatedProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudFormationStackDriftDetectionCheck(
    ManagedRule,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_config.CloudFormationStackDriftDetectionCheck",
):
    '''Checks whether your CloudFormation stacks' actual configuration differs, or has drifted, from its expected configuration.

    :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudformation-stack-drift-detection-check.html
    :resource: AWS::Config::ConfigRule
    :exampleMetadata: infused

    Example::

        # Topic to which compliance notification events will be published
        compliance_topic = sns.Topic(self, "ComplianceTopic")
        
        rule = config.CloudFormationStackDriftDetectionCheck(self, "Drift")
        rule.on_compliance_change("TopicEvent",
            target=targets.SnsTopic(compliance_topic)
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        own_stack_only: typing.Optional[builtins.bool] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
        rule_scope: typing.Optional[RuleScope] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param own_stack_only: Whether to check only the stack where this rule is deployed. Default: false
        :param role: The IAM role to use for this rule. It must have permissions to detect drift for AWS CloudFormation stacks. Ensure to attach ``config.amazonaws.com`` trusted permissions and ``ReadOnlyAccess`` policy permissions. For specific policy permissions, refer to https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html. Default: - A role will be created
        :param config_rule_name: A name for the AWS Config rule. Default: - CloudFormation generated name
        :param description: A description about this AWS Config rule. Default: - No description
        :param input_parameters: Input parameter values that are passed to the AWS Config rule. Default: - No input parameters
        :param maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        :param rule_scope: Defines which resources trigger an evaluation for an AWS Config rule. Default: - evaluations for the rule are triggered when any resource in the recording group changes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a22b3986125c76fb9e9557349b6727e4d1c0b600ef5e07d36a6ef3232ce01a7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CloudFormationStackDriftDetectionCheckProps(
            own_stack_only=own_stack_only,
            role=role,
            config_rule_name=config_rule_name,
            description=description,
            input_parameters=input_parameters,
            maximum_execution_frequency=maximum_execution_frequency,
            rule_scope=rule_scope,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_config.CloudFormationStackDriftDetectionCheckProps",
    jsii_struct_bases=[RuleProps],
    name_mapping={
        "config_rule_name": "configRuleName",
        "description": "description",
        "input_parameters": "inputParameters",
        "maximum_execution_frequency": "maximumExecutionFrequency",
        "rule_scope": "ruleScope",
        "own_stack_only": "ownStackOnly",
        "role": "role",
    },
)
class CloudFormationStackDriftDetectionCheckProps(RuleProps):
    def __init__(
        self,
        *,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
        rule_scope: typing.Optional[RuleScope] = None,
        own_stack_only: typing.Optional[builtins.bool] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''Construction properties for a CloudFormationStackDriftDetectionCheck.

        :param config_rule_name: A name for the AWS Config rule. Default: - CloudFormation generated name
        :param description: A description about this AWS Config rule. Default: - No description
        :param input_parameters: Input parameter values that are passed to the AWS Config rule. Default: - No input parameters
        :param maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        :param rule_scope: Defines which resources trigger an evaluation for an AWS Config rule. Default: - evaluations for the rule are triggered when any resource in the recording group changes.
        :param own_stack_only: Whether to check only the stack where this rule is deployed. Default: false
        :param role: The IAM role to use for this rule. It must have permissions to detect drift for AWS CloudFormation stacks. Ensure to attach ``config.amazonaws.com`` trusted permissions and ``ReadOnlyAccess`` policy permissions. For specific policy permissions, refer to https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html. Default: - A role will be created

        :exampleMetadata: infused

        Example::

            # compliant if stack's status is 'IN_SYNC'
            # non-compliant if the stack's drift status is 'DRIFTED'
            config.CloudFormationStackDriftDetectionCheck(self, "Drift",
                own_stack_only=True
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6e3aa47b4b02ba66dc0d2476d22bede4156332edf92696248dc715d6621a4a2)
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument input_parameters", value=input_parameters, expected_type=type_hints["input_parameters"])
            check_type(argname="argument maximum_execution_frequency", value=maximum_execution_frequency, expected_type=type_hints["maximum_execution_frequency"])
            check_type(argname="argument rule_scope", value=rule_scope, expected_type=type_hints["rule_scope"])
            check_type(argname="argument own_stack_only", value=own_stack_only, expected_type=type_hints["own_stack_only"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if config_rule_name is not None:
            self._values["config_rule_name"] = config_rule_name
        if description is not None:
            self._values["description"] = description
        if input_parameters is not None:
            self._values["input_parameters"] = input_parameters
        if maximum_execution_frequency is not None:
            self._values["maximum_execution_frequency"] = maximum_execution_frequency
        if rule_scope is not None:
            self._values["rule_scope"] = rule_scope
        if own_stack_only is not None:
            self._values["own_stack_only"] = own_stack_only
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def config_rule_name(self) -> typing.Optional[builtins.str]:
        '''A name for the AWS Config rule.

        :default: - CloudFormation generated name
        '''
        result = self._values.get("config_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description about this AWS Config rule.

        :default: - No description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Input parameter values that are passed to the AWS Config rule.

        :default: - No input parameters
        '''
        result = self._values.get("input_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def maximum_execution_frequency(self) -> typing.Optional[MaximumExecutionFrequency]:
        '''The maximum frequency at which the AWS Config rule runs evaluations.

        :default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        '''
        result = self._values.get("maximum_execution_frequency")
        return typing.cast(typing.Optional[MaximumExecutionFrequency], result)

    @builtins.property
    def rule_scope(self) -> typing.Optional[RuleScope]:
        '''Defines which resources trigger an evaluation for an AWS Config rule.

        :default: - evaluations for the rule are triggered when any resource in the recording group changes.
        '''
        result = self._values.get("rule_scope")
        return typing.cast(typing.Optional[RuleScope], result)

    @builtins.property
    def own_stack_only(self) -> typing.Optional[builtins.bool]:
        '''Whether to check only the stack where this rule is deployed.

        :default: false
        '''
        result = self._values.get("own_stack_only")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM role to use for this rule.

        It must have permissions to detect drift
        for AWS CloudFormation stacks. Ensure to attach ``config.amazonaws.com`` trusted
        permissions and ``ReadOnlyAccess`` policy permissions. For specific policy permissions,
        refer to https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html.

        :default: - A role will be created
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudFormationStackDriftDetectionCheckProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudFormationStackNotificationCheck(
    ManagedRule,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_config.CloudFormationStackNotificationCheck",
):
    '''Checks whether your CloudFormation stacks are sending event notifications to a SNS topic.

    Optionally checks whether specified SNS topics are used.

    :see: https://docs.aws.amazon.com/config/latest/developerguide/cloudformation-stack-notification-check.html
    :resource: AWS::Config::ConfigRule
    :exampleMetadata: infused

    Example::

        # topics to which CloudFormation stacks may send event notifications
        topic1 = sns.Topic(self, "AllowedTopic1")
        topic2 = sns.Topic(self, "AllowedTopic2")
        
        # non-compliant if CloudFormation stack does not send notifications to 'topic1' or 'topic2'
        config.CloudFormationStackNotificationCheck(self, "NotificationCheck",
            topics=[topic1, topic2]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        topics: typing.Optional[typing.Sequence[_ITopic_9eca4852]] = None,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
        rule_scope: typing.Optional[RuleScope] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param topics: A list of allowed topics. At most 5 topics. Default: - No topics.
        :param config_rule_name: A name for the AWS Config rule. Default: - CloudFormation generated name
        :param description: A description about this AWS Config rule. Default: - No description
        :param input_parameters: Input parameter values that are passed to the AWS Config rule. Default: - No input parameters
        :param maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        :param rule_scope: Defines which resources trigger an evaluation for an AWS Config rule. Default: - evaluations for the rule are triggered when any resource in the recording group changes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3f2230d810e1b4e21cbed5c1f6dbaae3f6b443915ac3b8148dd5cc54a19e75a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CloudFormationStackNotificationCheckProps(
            topics=topics,
            config_rule_name=config_rule_name,
            description=description,
            input_parameters=input_parameters,
            maximum_execution_frequency=maximum_execution_frequency,
            rule_scope=rule_scope,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_config.CloudFormationStackNotificationCheckProps",
    jsii_struct_bases=[RuleProps],
    name_mapping={
        "config_rule_name": "configRuleName",
        "description": "description",
        "input_parameters": "inputParameters",
        "maximum_execution_frequency": "maximumExecutionFrequency",
        "rule_scope": "ruleScope",
        "topics": "topics",
    },
)
class CloudFormationStackNotificationCheckProps(RuleProps):
    def __init__(
        self,
        *,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
        rule_scope: typing.Optional[RuleScope] = None,
        topics: typing.Optional[typing.Sequence[_ITopic_9eca4852]] = None,
    ) -> None:
        '''Construction properties for a CloudFormationStackNotificationCheck.

        :param config_rule_name: A name for the AWS Config rule. Default: - CloudFormation generated name
        :param description: A description about this AWS Config rule. Default: - No description
        :param input_parameters: Input parameter values that are passed to the AWS Config rule. Default: - No input parameters
        :param maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        :param rule_scope: Defines which resources trigger an evaluation for an AWS Config rule. Default: - evaluations for the rule are triggered when any resource in the recording group changes.
        :param topics: A list of allowed topics. At most 5 topics. Default: - No topics.

        :exampleMetadata: infused

        Example::

            # topics to which CloudFormation stacks may send event notifications
            topic1 = sns.Topic(self, "AllowedTopic1")
            topic2 = sns.Topic(self, "AllowedTopic2")
            
            # non-compliant if CloudFormation stack does not send notifications to 'topic1' or 'topic2'
            config.CloudFormationStackNotificationCheck(self, "NotificationCheck",
                topics=[topic1, topic2]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4a2e1a2e2112721950f4e16046156e3b9bff53c55c515662c906f895bef67d1)
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument input_parameters", value=input_parameters, expected_type=type_hints["input_parameters"])
            check_type(argname="argument maximum_execution_frequency", value=maximum_execution_frequency, expected_type=type_hints["maximum_execution_frequency"])
            check_type(argname="argument rule_scope", value=rule_scope, expected_type=type_hints["rule_scope"])
            check_type(argname="argument topics", value=topics, expected_type=type_hints["topics"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if config_rule_name is not None:
            self._values["config_rule_name"] = config_rule_name
        if description is not None:
            self._values["description"] = description
        if input_parameters is not None:
            self._values["input_parameters"] = input_parameters
        if maximum_execution_frequency is not None:
            self._values["maximum_execution_frequency"] = maximum_execution_frequency
        if rule_scope is not None:
            self._values["rule_scope"] = rule_scope
        if topics is not None:
            self._values["topics"] = topics

    @builtins.property
    def config_rule_name(self) -> typing.Optional[builtins.str]:
        '''A name for the AWS Config rule.

        :default: - CloudFormation generated name
        '''
        result = self._values.get("config_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description about this AWS Config rule.

        :default: - No description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Input parameter values that are passed to the AWS Config rule.

        :default: - No input parameters
        '''
        result = self._values.get("input_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def maximum_execution_frequency(self) -> typing.Optional[MaximumExecutionFrequency]:
        '''The maximum frequency at which the AWS Config rule runs evaluations.

        :default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        '''
        result = self._values.get("maximum_execution_frequency")
        return typing.cast(typing.Optional[MaximumExecutionFrequency], result)

    @builtins.property
    def rule_scope(self) -> typing.Optional[RuleScope]:
        '''Defines which resources trigger an evaluation for an AWS Config rule.

        :default: - evaluations for the rule are triggered when any resource in the recording group changes.
        '''
        result = self._values.get("rule_scope")
        return typing.cast(typing.Optional[RuleScope], result)

    @builtins.property
    def topics(self) -> typing.Optional[typing.List[_ITopic_9eca4852]]:
        '''A list of allowed topics.

        At most 5 topics.

        :default: - No topics.
        '''
        result = self._values.get("topics")
        return typing.cast(typing.Optional[typing.List[_ITopic_9eca4852]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudFormationStackNotificationCheckProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IRule)
class CustomPolicy(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_config.CustomPolicy",
):
    '''A new custom policy.

    :resource: AWS::Config::ConfigRule
    :exampleMetadata: infused

    Example::

        sample_policy_text = """
        # This rule checks if point in time recovery (PITR) is enabled on active Amazon DynamoDB tables
        let status = ['ACTIVE']
        
        rule tableisactive when
            resourceType == "AWS::DynamoDB::Table" {
            configuration.tableStatus == %status
        }
        
        rule checkcompliance when
            resourceType == "AWS::DynamoDB::Table"
            tableisactive {
                let pitr = supplementaryConfiguration.ContinuousBackupsDescription.pointInTimeRecoveryDescription.pointInTimeRecoveryStatus
                %pitr == "ENABLED"
        }
        """
        
        config.CustomPolicy(self, "Custom",
            policy_text=sample_policy_text,
            enable_debug_log=True,
            rule_scope=config.RuleScope.from_resources([config.ResourceType.DYNAMODB_TABLE
            ])
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        policy_text: builtins.str,
        enable_debug_log: typing.Optional[builtins.bool] = None,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
        rule_scope: typing.Optional[RuleScope] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param policy_text: The policy definition containing the logic for your AWS Config Custom Policy rule.
        :param enable_debug_log: The boolean expression for enabling debug logging for your AWS Config Custom Policy rule. Default: false
        :param config_rule_name: A name for the AWS Config rule. Default: - CloudFormation generated name
        :param description: A description about this AWS Config rule. Default: - No description
        :param input_parameters: Input parameter values that are passed to the AWS Config rule. Default: - No input parameters
        :param maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        :param rule_scope: Defines which resources trigger an evaluation for an AWS Config rule. Default: - evaluations for the rule are triggered when any resource in the recording group changes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49010e8081bbdd3bfbafae78ccebf0b5a42d400543b3dff90687e28d2c491579)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CustomPolicyProps(
            policy_text=policy_text,
            enable_debug_log=enable_debug_log,
            config_rule_name=config_rule_name,
            description=description,
            input_parameters=input_parameters,
            maximum_execution_frequency=maximum_execution_frequency,
            rule_scope=rule_scope,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromConfigRuleName")
    @builtins.classmethod
    def from_config_rule_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        config_rule_name: builtins.str,
    ) -> IRule:
        '''Imports an existing rule.

        :param scope: -
        :param id: -
        :param config_rule_name: the name of the rule.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e40e3bd2d39a3dc7854fedb9fe3187292fff5413ee20f739e96f26a0ddf0efd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
        return typing.cast(IRule, jsii.sinvoke(cls, "fromConfigRuleName", [scope, id, config_rule_name]))

    @jsii.member(jsii_name="onComplianceChange")
    def on_compliance_change(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines an EventBridge event rule which triggers for rule compliance events.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a0a36a2cb813a5fe745e4bea0f64d4c5a9026b5c50474a53297e9e20b6fd81e)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onComplianceChange", [id, options]))

    @jsii.member(jsii_name="onEvent")
    def on_event(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines an EventBridge event rule which triggers for rule events.

        Use
        ``rule.addEventPattern(pattern)`` to specify a filter.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39e7a300478811593a99ff8f1fed3908300731aab8791186b6cf1dad84b8a856)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onEvent", [id, options]))

    @jsii.member(jsii_name="onReEvaluationStatus")
    def on_re_evaluation_status(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines an EventBridge event rule which triggers for rule re-evaluation status events.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a30be9c312961f8a2abd3a82da4460a1bd1fc45702591da31bfc9c17b11ddcd)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onReEvaluationStatus", [id, options]))

    @builtins.property
    @jsii.member(jsii_name="configRuleArn")
    def config_rule_arn(self) -> builtins.str:
        '''The arn of the rule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "configRuleArn"))

    @builtins.property
    @jsii.member(jsii_name="configRuleComplianceType")
    def config_rule_compliance_type(self) -> builtins.str:
        '''The compliance status of the rule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "configRuleComplianceType"))

    @builtins.property
    @jsii.member(jsii_name="configRuleId")
    def config_rule_id(self) -> builtins.str:
        '''The id of the rule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "configRuleId"))

    @builtins.property
    @jsii.member(jsii_name="configRuleName")
    def config_rule_name(self) -> builtins.str:
        '''The name of the rule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "configRuleName"))

    @builtins.property
    @jsii.member(jsii_name="isCustomWithChanges")
    def _is_custom_with_changes(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "isCustomWithChanges"))

    @_is_custom_with_changes.setter
    def _is_custom_with_changes(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b9854d10077a651dbdf4a0cba3107e925b9c9a611c8097fed5bcc7444e15b83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isCustomWithChanges", value)

    @builtins.property
    @jsii.member(jsii_name="isManaged")
    def _is_managed(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "isManaged"))

    @_is_managed.setter
    def _is_managed(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9abd1840e8081b6260fc81d74f36283b1fe5d04439637f73b38817fbca86b313)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isManaged", value)

    @builtins.property
    @jsii.member(jsii_name="ruleScope")
    def _rule_scope(self) -> typing.Optional[RuleScope]:
        return typing.cast(typing.Optional[RuleScope], jsii.get(self, "ruleScope"))

    @_rule_scope.setter
    def _rule_scope(self, value: typing.Optional[RuleScope]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef65597b7cc84c802aee5d97e6dbc9dbf9e0f04df2ae41e5102e9265b7960d0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleScope", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_config.CustomPolicyProps",
    jsii_struct_bases=[RuleProps],
    name_mapping={
        "config_rule_name": "configRuleName",
        "description": "description",
        "input_parameters": "inputParameters",
        "maximum_execution_frequency": "maximumExecutionFrequency",
        "rule_scope": "ruleScope",
        "policy_text": "policyText",
        "enable_debug_log": "enableDebugLog",
    },
)
class CustomPolicyProps(RuleProps):
    def __init__(
        self,
        *,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
        rule_scope: typing.Optional[RuleScope] = None,
        policy_text: builtins.str,
        enable_debug_log: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Construction properties for a CustomPolicy.

        :param config_rule_name: A name for the AWS Config rule. Default: - CloudFormation generated name
        :param description: A description about this AWS Config rule. Default: - No description
        :param input_parameters: Input parameter values that are passed to the AWS Config rule. Default: - No input parameters
        :param maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        :param rule_scope: Defines which resources trigger an evaluation for an AWS Config rule. Default: - evaluations for the rule are triggered when any resource in the recording group changes.
        :param policy_text: The policy definition containing the logic for your AWS Config Custom Policy rule.
        :param enable_debug_log: The boolean expression for enabling debug logging for your AWS Config Custom Policy rule. Default: false

        :exampleMetadata: infused

        Example::

            sample_policy_text = """
            # This rule checks if point in time recovery (PITR) is enabled on active Amazon DynamoDB tables
            let status = ['ACTIVE']
            
            rule tableisactive when
                resourceType == "AWS::DynamoDB::Table" {
                configuration.tableStatus == %status
            }
            
            rule checkcompliance when
                resourceType == "AWS::DynamoDB::Table"
                tableisactive {
                    let pitr = supplementaryConfiguration.ContinuousBackupsDescription.pointInTimeRecoveryDescription.pointInTimeRecoveryStatus
                    %pitr == "ENABLED"
            }
            """
            
            config.CustomPolicy(self, "Custom",
                policy_text=sample_policy_text,
                enable_debug_log=True,
                rule_scope=config.RuleScope.from_resources([config.ResourceType.DYNAMODB_TABLE
                ])
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a248d79f961151a1c3a0a4ffba1d7f034b78164fd67cc63e24d802e6fca8c2e)
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument input_parameters", value=input_parameters, expected_type=type_hints["input_parameters"])
            check_type(argname="argument maximum_execution_frequency", value=maximum_execution_frequency, expected_type=type_hints["maximum_execution_frequency"])
            check_type(argname="argument rule_scope", value=rule_scope, expected_type=type_hints["rule_scope"])
            check_type(argname="argument policy_text", value=policy_text, expected_type=type_hints["policy_text"])
            check_type(argname="argument enable_debug_log", value=enable_debug_log, expected_type=type_hints["enable_debug_log"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_text": policy_text,
        }
        if config_rule_name is not None:
            self._values["config_rule_name"] = config_rule_name
        if description is not None:
            self._values["description"] = description
        if input_parameters is not None:
            self._values["input_parameters"] = input_parameters
        if maximum_execution_frequency is not None:
            self._values["maximum_execution_frequency"] = maximum_execution_frequency
        if rule_scope is not None:
            self._values["rule_scope"] = rule_scope
        if enable_debug_log is not None:
            self._values["enable_debug_log"] = enable_debug_log

    @builtins.property
    def config_rule_name(self) -> typing.Optional[builtins.str]:
        '''A name for the AWS Config rule.

        :default: - CloudFormation generated name
        '''
        result = self._values.get("config_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description about this AWS Config rule.

        :default: - No description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Input parameter values that are passed to the AWS Config rule.

        :default: - No input parameters
        '''
        result = self._values.get("input_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def maximum_execution_frequency(self) -> typing.Optional[MaximumExecutionFrequency]:
        '''The maximum frequency at which the AWS Config rule runs evaluations.

        :default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        '''
        result = self._values.get("maximum_execution_frequency")
        return typing.cast(typing.Optional[MaximumExecutionFrequency], result)

    @builtins.property
    def rule_scope(self) -> typing.Optional[RuleScope]:
        '''Defines which resources trigger an evaluation for an AWS Config rule.

        :default: - evaluations for the rule are triggered when any resource in the recording group changes.
        '''
        result = self._values.get("rule_scope")
        return typing.cast(typing.Optional[RuleScope], result)

    @builtins.property
    def policy_text(self) -> builtins.str:
        '''The policy definition containing the logic for your AWS Config Custom Policy rule.'''
        result = self._values.get("policy_text")
        assert result is not None, "Required property 'policy_text' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enable_debug_log(self) -> typing.Optional[builtins.bool]:
        '''The boolean expression for enabling debug logging for your AWS Config Custom Policy rule.

        :default: false
        '''
        result = self._values.get("enable_debug_log")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IRule)
class CustomRule(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_config.CustomRule",
):
    '''A new custom rule.

    :resource: AWS::Config::ConfigRule
    :exampleMetadata: infused

    Example::

        # Lambda function containing logic that evaluates compliance with the rule.
        eval_compliance_fn = lambda_.Function(self, "CustomFunction",
            code=lambda_.AssetCode.from_inline("exports.handler = (event) => console.log(event);"),
            handler="index.handler",
            runtime=lambda_.Runtime.NODEJS_18_X
        )
        
        # A custom rule that runs on configuration changes of EC2 instances
        custom_rule = config.CustomRule(self, "Custom",
            configuration_changes=True,
            lambda_function=eval_compliance_fn,
            rule_scope=config.RuleScope.from_resource(config.ResourceType.EC2_INSTANCE)
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        lambda_function: _IFunction_6adb0ab8,
        configuration_changes: typing.Optional[builtins.bool] = None,
        periodic: typing.Optional[builtins.bool] = None,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
        rule_scope: typing.Optional[RuleScope] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param lambda_function: The Lambda function to run.
        :param configuration_changes: Whether to run the rule on configuration changes. Default: false
        :param periodic: Whether to run the rule on a fixed frequency. Default: false
        :param config_rule_name: A name for the AWS Config rule. Default: - CloudFormation generated name
        :param description: A description about this AWS Config rule. Default: - No description
        :param input_parameters: Input parameter values that are passed to the AWS Config rule. Default: - No input parameters
        :param maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        :param rule_scope: Defines which resources trigger an evaluation for an AWS Config rule. Default: - evaluations for the rule are triggered when any resource in the recording group changes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c04b50bb256529db27e261da69377598f975841e3cdb477cd74feb70373983b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CustomRuleProps(
            lambda_function=lambda_function,
            configuration_changes=configuration_changes,
            periodic=periodic,
            config_rule_name=config_rule_name,
            description=description,
            input_parameters=input_parameters,
            maximum_execution_frequency=maximum_execution_frequency,
            rule_scope=rule_scope,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromConfigRuleName")
    @builtins.classmethod
    def from_config_rule_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        config_rule_name: builtins.str,
    ) -> IRule:
        '''Imports an existing rule.

        :param scope: -
        :param id: -
        :param config_rule_name: the name of the rule.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eea17ae081715a75c721bf7b8a98441fbcd9d3fdfaf56f61d888cd4d5a4e8ab3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
        return typing.cast(IRule, jsii.sinvoke(cls, "fromConfigRuleName", [scope, id, config_rule_name]))

    @jsii.member(jsii_name="onComplianceChange")
    def on_compliance_change(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines an EventBridge event rule which triggers for rule compliance events.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1326aee63fdb27f4bc6888e53a1aaad7c4d6c4bd2bf0661852059dfb412654c1)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onComplianceChange", [id, options]))

    @jsii.member(jsii_name="onEvent")
    def on_event(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines an EventBridge event rule which triggers for rule events.

        Use
        ``rule.addEventPattern(pattern)`` to specify a filter.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8fb04d46bf1c7afea8e0849d3e449732008011a1668b9836310c1101b73043c)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onEvent", [id, options]))

    @jsii.member(jsii_name="onReEvaluationStatus")
    def on_re_evaluation_status(
        self,
        id: builtins.str,
        *,
        target: typing.Optional[_IRuleTarget_7a91f454] = None,
        cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
        description: typing.Optional[builtins.str] = None,
        event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
        rule_name: typing.Optional[builtins.str] = None,
    ) -> _Rule_334ed2b5:
        '''Defines an EventBridge event rule which triggers for rule re-evaluation status events.

        :param id: -
        :param target: The target to register for the event. Default: - No target is added to the rule. Use ``addTarget()`` to add a target.
        :param cross_stack_scope: The scope to use if the source of the rule and its target are in different Stacks (but in the same account & region). This helps dealing with cycles that often arise in these situations. Default: - none (the main scope will be used, even for cross-stack Events)
        :param description: A description of the rule's purpose. Default: - No description
        :param event_pattern: Additional restrictions for the event to route to the specified target. The method that generates the rule probably imposes some type of event filtering. The filtering implied by what you pass here is added on top of that filtering. Default: - No additional filtering based on an event pattern.
        :param rule_name: A name for the rule. Default: AWS CloudFormation generates a unique physical ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ab48da45e6070573de565a2b77e458a32622a57d5f1b3e1b3219c2bd2236bda)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = _OnEventOptions_8711b8b3(
            target=target,
            cross_stack_scope=cross_stack_scope,
            description=description,
            event_pattern=event_pattern,
            rule_name=rule_name,
        )

        return typing.cast(_Rule_334ed2b5, jsii.invoke(self, "onReEvaluationStatus", [id, options]))

    @builtins.property
    @jsii.member(jsii_name="configRuleArn")
    def config_rule_arn(self) -> builtins.str:
        '''The arn of the rule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "configRuleArn"))

    @builtins.property
    @jsii.member(jsii_name="configRuleComplianceType")
    def config_rule_compliance_type(self) -> builtins.str:
        '''The compliance status of the rule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "configRuleComplianceType"))

    @builtins.property
    @jsii.member(jsii_name="configRuleId")
    def config_rule_id(self) -> builtins.str:
        '''The id of the rule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "configRuleId"))

    @builtins.property
    @jsii.member(jsii_name="configRuleName")
    def config_rule_name(self) -> builtins.str:
        '''The name of the rule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "configRuleName"))

    @builtins.property
    @jsii.member(jsii_name="isCustomWithChanges")
    def _is_custom_with_changes(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "isCustomWithChanges"))

    @_is_custom_with_changes.setter
    def _is_custom_with_changes(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c0958f3032e21e6d261e16c22aa71b2651c7a065516dfb3c5643d0d9c874710)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isCustomWithChanges", value)

    @builtins.property
    @jsii.member(jsii_name="isManaged")
    def _is_managed(self) -> typing.Optional[builtins.bool]:
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "isManaged"))

    @_is_managed.setter
    def _is_managed(self, value: typing.Optional[builtins.bool]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d658d05e8291c14eee0e010031415e38f12fcc5a172cffd783e9708dd81b597f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isManaged", value)

    @builtins.property
    @jsii.member(jsii_name="ruleScope")
    def _rule_scope(self) -> typing.Optional[RuleScope]:
        return typing.cast(typing.Optional[RuleScope], jsii.get(self, "ruleScope"))

    @_rule_scope.setter
    def _rule_scope(self, value: typing.Optional[RuleScope]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4a42de8a257fafa046633793b8c78f666811737b6939072d51be06693e271c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleScope", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_config.CustomRuleProps",
    jsii_struct_bases=[RuleProps],
    name_mapping={
        "config_rule_name": "configRuleName",
        "description": "description",
        "input_parameters": "inputParameters",
        "maximum_execution_frequency": "maximumExecutionFrequency",
        "rule_scope": "ruleScope",
        "lambda_function": "lambdaFunction",
        "configuration_changes": "configurationChanges",
        "periodic": "periodic",
    },
)
class CustomRuleProps(RuleProps):
    def __init__(
        self,
        *,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
        rule_scope: typing.Optional[RuleScope] = None,
        lambda_function: _IFunction_6adb0ab8,
        configuration_changes: typing.Optional[builtins.bool] = None,
        periodic: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Construction properties for a CustomRule.

        :param config_rule_name: A name for the AWS Config rule. Default: - CloudFormation generated name
        :param description: A description about this AWS Config rule. Default: - No description
        :param input_parameters: Input parameter values that are passed to the AWS Config rule. Default: - No input parameters
        :param maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        :param rule_scope: Defines which resources trigger an evaluation for an AWS Config rule. Default: - evaluations for the rule are triggered when any resource in the recording group changes.
        :param lambda_function: The Lambda function to run.
        :param configuration_changes: Whether to run the rule on configuration changes. Default: false
        :param periodic: Whether to run the rule on a fixed frequency. Default: false

        :exampleMetadata: infused

        Example::

            # Lambda function containing logic that evaluates compliance with the rule.
            eval_compliance_fn = lambda_.Function(self, "CustomFunction",
                code=lambda_.AssetCode.from_inline("exports.handler = (event) => console.log(event);"),
                handler="index.handler",
                runtime=lambda_.Runtime.NODEJS_18_X
            )
            
            # A custom rule that runs on configuration changes of EC2 instances
            custom_rule = config.CustomRule(self, "Custom",
                configuration_changes=True,
                lambda_function=eval_compliance_fn,
                rule_scope=config.RuleScope.from_resource(config.ResourceType.EC2_INSTANCE)
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__218427563a034726fd41356c6d38c7959e2a44897cb1d6d9133bc9254a35c9f0)
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument input_parameters", value=input_parameters, expected_type=type_hints["input_parameters"])
            check_type(argname="argument maximum_execution_frequency", value=maximum_execution_frequency, expected_type=type_hints["maximum_execution_frequency"])
            check_type(argname="argument rule_scope", value=rule_scope, expected_type=type_hints["rule_scope"])
            check_type(argname="argument lambda_function", value=lambda_function, expected_type=type_hints["lambda_function"])
            check_type(argname="argument configuration_changes", value=configuration_changes, expected_type=type_hints["configuration_changes"])
            check_type(argname="argument periodic", value=periodic, expected_type=type_hints["periodic"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "lambda_function": lambda_function,
        }
        if config_rule_name is not None:
            self._values["config_rule_name"] = config_rule_name
        if description is not None:
            self._values["description"] = description
        if input_parameters is not None:
            self._values["input_parameters"] = input_parameters
        if maximum_execution_frequency is not None:
            self._values["maximum_execution_frequency"] = maximum_execution_frequency
        if rule_scope is not None:
            self._values["rule_scope"] = rule_scope
        if configuration_changes is not None:
            self._values["configuration_changes"] = configuration_changes
        if periodic is not None:
            self._values["periodic"] = periodic

    @builtins.property
    def config_rule_name(self) -> typing.Optional[builtins.str]:
        '''A name for the AWS Config rule.

        :default: - CloudFormation generated name
        '''
        result = self._values.get("config_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description about this AWS Config rule.

        :default: - No description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Input parameter values that are passed to the AWS Config rule.

        :default: - No input parameters
        '''
        result = self._values.get("input_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def maximum_execution_frequency(self) -> typing.Optional[MaximumExecutionFrequency]:
        '''The maximum frequency at which the AWS Config rule runs evaluations.

        :default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        '''
        result = self._values.get("maximum_execution_frequency")
        return typing.cast(typing.Optional[MaximumExecutionFrequency], result)

    @builtins.property
    def rule_scope(self) -> typing.Optional[RuleScope]:
        '''Defines which resources trigger an evaluation for an AWS Config rule.

        :default: - evaluations for the rule are triggered when any resource in the recording group changes.
        '''
        result = self._values.get("rule_scope")
        return typing.cast(typing.Optional[RuleScope], result)

    @builtins.property
    def lambda_function(self) -> _IFunction_6adb0ab8:
        '''The Lambda function to run.'''
        result = self._values.get("lambda_function")
        assert result is not None, "Required property 'lambda_function' is missing"
        return typing.cast(_IFunction_6adb0ab8, result)

    @builtins.property
    def configuration_changes(self) -> typing.Optional[builtins.bool]:
        '''Whether to run the rule on configuration changes.

        :default: false
        '''
        result = self._values.get("configuration_changes")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def periodic(self) -> typing.Optional[builtins.bool]:
        '''Whether to run the rule on a fixed frequency.

        :default: false
        '''
        result = self._values.get("periodic")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_config.ManagedRuleProps",
    jsii_struct_bases=[RuleProps],
    name_mapping={
        "config_rule_name": "configRuleName",
        "description": "description",
        "input_parameters": "inputParameters",
        "maximum_execution_frequency": "maximumExecutionFrequency",
        "rule_scope": "ruleScope",
        "identifier": "identifier",
    },
)
class ManagedRuleProps(RuleProps):
    def __init__(
        self,
        *,
        config_rule_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
        maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
        rule_scope: typing.Optional[RuleScope] = None,
        identifier: builtins.str,
    ) -> None:
        '''Construction properties for a ManagedRule.

        :param config_rule_name: A name for the AWS Config rule. Default: - CloudFormation generated name
        :param description: A description about this AWS Config rule. Default: - No description
        :param input_parameters: Input parameter values that are passed to the AWS Config rule. Default: - No input parameters
        :param maximum_execution_frequency: The maximum frequency at which the AWS Config rule runs evaluations. Default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        :param rule_scope: Defines which resources trigger an evaluation for an AWS Config rule. Default: - evaluations for the rule are triggered when any resource in the recording group changes.
        :param identifier: The identifier of the AWS managed rule.

        :exampleMetadata: infused

        Example::

            # https://docs.aws.amazon.com/config/latest/developerguide/access-keys-rotated.html
            config.ManagedRule(self, "AccessKeysRotated",
                identifier=config.ManagedRuleIdentifiers.ACCESS_KEYS_ROTATED,
                input_parameters={
                    "max_access_key_age": 60
                },
            
                # default is 24 hours
                maximum_execution_frequency=config.MaximumExecutionFrequency.TWELVE_HOURS
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__feaff635e0230e65515841ea744975d751e424acf376b8ed530119931a2ea4ed)
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument input_parameters", value=input_parameters, expected_type=type_hints["input_parameters"])
            check_type(argname="argument maximum_execution_frequency", value=maximum_execution_frequency, expected_type=type_hints["maximum_execution_frequency"])
            check_type(argname="argument rule_scope", value=rule_scope, expected_type=type_hints["rule_scope"])
            check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identifier": identifier,
        }
        if config_rule_name is not None:
            self._values["config_rule_name"] = config_rule_name
        if description is not None:
            self._values["description"] = description
        if input_parameters is not None:
            self._values["input_parameters"] = input_parameters
        if maximum_execution_frequency is not None:
            self._values["maximum_execution_frequency"] = maximum_execution_frequency
        if rule_scope is not None:
            self._values["rule_scope"] = rule_scope

    @builtins.property
    def config_rule_name(self) -> typing.Optional[builtins.str]:
        '''A name for the AWS Config rule.

        :default: - CloudFormation generated name
        '''
        result = self._values.get("config_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description about this AWS Config rule.

        :default: - No description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Any]]:
        '''Input parameter values that are passed to the AWS Config rule.

        :default: - No input parameters
        '''
        result = self._values.get("input_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Any]], result)

    @builtins.property
    def maximum_execution_frequency(self) -> typing.Optional[MaximumExecutionFrequency]:
        '''The maximum frequency at which the AWS Config rule runs evaluations.

        :default: MaximumExecutionFrequency.TWENTY_FOUR_HOURS
        '''
        result = self._values.get("maximum_execution_frequency")
        return typing.cast(typing.Optional[MaximumExecutionFrequency], result)

    @builtins.property
    def rule_scope(self) -> typing.Optional[RuleScope]:
        '''Defines which resources trigger an evaluation for an AWS Config rule.

        :default: - evaluations for the rule are triggered when any resource in the recording group changes.
        '''
        result = self._values.get("rule_scope")
        return typing.cast(typing.Optional[RuleScope], result)

    @builtins.property
    def identifier(self) -> builtins.str:
        '''The identifier of the AWS managed rule.

        :see: https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html
        '''
        result = self._values.get("identifier")
        assert result is not None, "Required property 'identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AccessKeysRotated",
    "AccessKeysRotatedProps",
    "CfnAggregationAuthorization",
    "CfnAggregationAuthorizationProps",
    "CfnConfigRule",
    "CfnConfigRuleProps",
    "CfnConfigurationAggregator",
    "CfnConfigurationAggregatorProps",
    "CfnConfigurationRecorder",
    "CfnConfigurationRecorderProps",
    "CfnConformancePack",
    "CfnConformancePackProps",
    "CfnDeliveryChannel",
    "CfnDeliveryChannelProps",
    "CfnOrganizationConfigRule",
    "CfnOrganizationConfigRuleProps",
    "CfnOrganizationConformancePack",
    "CfnOrganizationConformancePackProps",
    "CfnRemediationConfiguration",
    "CfnRemediationConfigurationProps",
    "CfnStoredQuery",
    "CfnStoredQueryProps",
    "CloudFormationStackDriftDetectionCheck",
    "CloudFormationStackDriftDetectionCheckProps",
    "CloudFormationStackNotificationCheck",
    "CloudFormationStackNotificationCheckProps",
    "CustomPolicy",
    "CustomPolicyProps",
    "CustomRule",
    "CustomRuleProps",
    "IRule",
    "ManagedRule",
    "ManagedRuleIdentifiers",
    "ManagedRuleProps",
    "MaximumExecutionFrequency",
    "ResourceType",
    "RuleProps",
    "RuleScope",
]

publication.publish()

def _typecheckingstub__6d45b6827b30a710c41539b6e64a482fe288457f84fc8da58a369837e081918d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    authorized_account_id: builtins.str,
    authorized_aws_region: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d44e9df1899840ed48cc8968c2953fc999bd4ebae4355121a7d0d44eb5a78d5(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4fe46b64cd7b2c7a7801c9f82cf436cd14b88bc96df13f85f4ae4b6503bda96(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd3558b66422be906f2e97b3cadb6ab3aff487b0ae706aa3e5e5cb5e361a5db2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ec985b949ac5925a51ebe338acec25ecef0e6592afa79374fef259e6fef4198(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2acb4bb46d29ee80a30777200253cd46f769127ae01597fbc2e951064ea932d4(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e6bdcf05466c02c7af89caa08522d10ba8181fd13410bcd081dbf714fbb74c9(
    *,
    authorized_account_id: builtins.str,
    authorized_aws_region: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__deecc74e0a0f7e54fde16a159ece5d8f96f56f6b8aca025003adcc1d931d5d00(
    scope_: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigRule.SourceProperty, typing.Dict[builtins.str, typing.Any]]],
    compliance: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigRule.ComplianceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    evaluation_modes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigRule.EvaluationModeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    input_parameters: typing.Any = None,
    maximum_execution_frequency: typing.Optional[builtins.str] = None,
    scope: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigRule.ScopeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75ac7fdaab59736823d3ea7aee906c770b124ed77c2a19e236c7baea8446f076(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2026b4300b4bc12decf81d1ef0dc9858c81f4dff9157afd07ab04e953241b21(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a30b5901e0068cf18be7f15f8558e224eb62559802cd26646f648c0dbf5f3680(
    value: typing.Union[_IResolvable_da3f097b, CfnConfigRule.SourceProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__743f9ee6243708ed2e606e31e618af32604f35d387093cdc8d8634e961b27324(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigRule.ComplianceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e021e024fd440e8ec5c9b4d24e2029d1629640189c221a5866e301e89aa53b6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__446b3dad0fdf8c8a9449d165e2fed6fa45c11495397d8cfdaf24ac1368e14962(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3563e34d09c0fb5a803e72a8cee06c0ed65b4c596390bf75303600bfd5df9f44(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfigRule.EvaluationModeConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d61437c3cdab85e8dc7a25b710d93b6aaaa2a833466cfb80eb3d13340c62da3(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c19facad0744d2d150810a1e9fb83a8d41c5447083981222c737ba287c7d08f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c70fa274e56c5def397aac6cec3b30f31c7ee9cc7367d5b6bf0c78e63400ca24(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigRule.ScopeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d66dbd2cc5d052bcc47c92d8ce8dd64bcb0b5dd57cfcc434e393029984359db(
    *,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7656d43bed3c419437bf5b25bc9711a8cf65f9f6b46c7d52710b15c35aa5af9(
    *,
    enable_debug_log_delivery: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    policy_runtime: typing.Optional[builtins.str] = None,
    policy_text: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b0afa0e56a40fa7b9efd435c94956c335f03393a48dc1d31c186bf76c9f256e(
    *,
    mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1dad2d9487ce142bd6c079d94efb61400194537a7d97b4158bc27439f9ae457(
    *,
    compliance_resource_id: typing.Optional[builtins.str] = None,
    compliance_resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    tag_key: typing.Optional[builtins.str] = None,
    tag_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7d66badade1eb1594b8d1b078e9a871db86cf85d41ad81a5858329bf4ba3775(
    *,
    event_source: builtins.str,
    message_type: builtins.str,
    maximum_execution_frequency: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8f7d3fbc3eba470d52b27b24c17f4eb9fae6ee74da9bf511cdb8b4ce4483652(
    *,
    owner: builtins.str,
    custom_policy_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigRule.CustomPolicyDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigRule.SourceDetailProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    source_identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__116f429a66beeda0419005586893a32aeefeb73824ac9dc6668b4e69b23facc2(
    *,
    source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigRule.SourceProperty, typing.Dict[builtins.str, typing.Any]]],
    compliance: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigRule.ComplianceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    evaluation_modes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigRule.EvaluationModeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    input_parameters: typing.Any = None,
    maximum_execution_frequency: typing.Optional[builtins.str] = None,
    scope: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigRule.ScopeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40705fa4ca5c4067a90bb01d176f11c05ad5552df80610a53368350023ed36f2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    account_aggregation_sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationAggregator.AccountAggregationSourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    configuration_aggregator_name: typing.Optional[builtins.str] = None,
    organization_aggregation_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationAggregator.OrganizationAggregationSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a67b0d51dcca76878a73006884af15e33330c306c3d8647f96d10c0ba3f57ef9(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce2cf39aa72c31cf38b4c26fc5f5192604fe0a27dca13c342e158bdd5e5787cd(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca6667d76e5d18c00525f2f2e305db803462801d9dd67cb2cc46951b67b7e1c9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfigurationAggregator.AccountAggregationSourceProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5d468f6c23924787d592b321e6a582b8ee2144e5dc7e23a15626d783a2637da(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adc51ade0f3204fdf6726c1ef680ca92c25055c195dce6a07df154db27d4c155(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationAggregator.OrganizationAggregationSourceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3d290ef49845b3910d8dfd1137db37b79d04caa1266e44513db09527493d2da(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6a7c257ab123c8bd6831aa9a0a52136ad391b912ac2682938757e16c6bdec2a(
    *,
    account_ids: typing.Sequence[builtins.str],
    all_aws_regions: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96908b20c43c7212f0b7cad39b2803ff294c40bcf770282dd47c8969bcd8bf51(
    *,
    role_arn: builtins.str,
    all_aws_regions: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23996e22d45c091c120b53006e9571da0dfd1a6a925c8a526fad11fbe913c027(
    *,
    account_aggregation_sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationAggregator.AccountAggregationSourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    configuration_aggregator_name: typing.Optional[builtins.str] = None,
    organization_aggregation_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationAggregator.OrganizationAggregationSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cc1fca38c04598953e44108edff915ed0a33e7e99e047d1bffcbd31ac2e3b03(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    role_arn: builtins.str,
    name: typing.Optional[builtins.str] = None,
    recording_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationRecorder.RecordingGroupProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    recording_mode: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationRecorder.RecordingModeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f0ad5fea2a79c807a345af7618aeaf866bf5a74d50a1a738fab4def57031159(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9732775bf56ded9f1fec94c1669136a91512c9ba51aaaebf836d5d8ef071812a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcbc5734beaea5ab983c66a385694785e3c9ee7351911d6b565ea4e897a7826e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2a1c68bd9cad77de81d8251d2998854170a63f9e469e6bdea9a9e56f75e6622(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e1878a10e77a1aa31c809535803af7748be10257943ccb0147e9c0839dda938(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationRecorder.RecordingGroupProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79c601a52da19c88133151b63852ca6a6ba71894cd962c2e118e75d604e83fe5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationRecorder.RecordingModeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bfeeb41a82e166dbe5ee3f6a4cb224863af8ea802ed4106641b03f2b048f32a(
    *,
    resource_types: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__574b2463724d6487e33926405844644e49df72910787a048a5ca198552045f16(
    *,
    all_supported: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    exclusion_by_resource_types: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationRecorder.ExclusionByResourceTypesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    include_global_resource_types: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    recording_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationRecorder.RecordingStrategyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__301d91ec25370b3d9c2f7b2aef5e6913cf2370b1c4e1ffda877aafd174d11165(
    *,
    recording_frequency: builtins.str,
    resource_types: typing.Sequence[builtins.str],
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2db8a0d318e287d3329642f2526ea9c788965e7dbe0f581278bef988ee908d63(
    *,
    recording_frequency: builtins.str,
    recording_mode_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationRecorder.RecordingModeOverrideProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdc0c3a0d4a9aa5083c337e0372ddbd0be93f7adadc83df65d33ce75c0b906bb(
    *,
    use_only: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68cc2049b8c095672250d1c12a5af6fc05b3421a6c23124f87e5e31e2668698e(
    *,
    role_arn: builtins.str,
    name: typing.Optional[builtins.str] = None,
    recording_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationRecorder.RecordingGroupProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    recording_mode: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationRecorder.RecordingModeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e2b5c522b5074ba2ef97dd80a498043778309ce04aa178507276f160fde847d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    conformance_pack_name: builtins.str,
    conformance_pack_input_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConformancePack.ConformancePackInputParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    delivery_s3_bucket: typing.Optional[builtins.str] = None,
    delivery_s3_key_prefix: typing.Optional[builtins.str] = None,
    template_body: typing.Optional[builtins.str] = None,
    template_s3_uri: typing.Optional[builtins.str] = None,
    template_ssm_document_details: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7403d4346a8cf57174116d6f88a4f63ca05740a7985a84232a53a10b8c76626b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6563d8daaed12475c806618fef63d370ca145285fb0811fb3eb18a8ae205322(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__017266c6d2336c47dd9ced678b7f1432f1d8c14f7d6c1fa5d4e1b853ea226215(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66a3c1376d21fbc61cfccda9673dabefb2864004881e13f61c2450d58f726d02(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConformancePack.ConformancePackInputParameterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e9ac9dd0b9bfb5622779dff282ea562c91d27ddf6529b24e403f4405f47b8ea(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efa81031141bc30ac68f2881e9910f55d05494d80263ec0832f9c3b4cfa72355(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e35eeba4feaded039ed05fa15d28eda7714d806f9cc117a1a4e2a9b4ee39433(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b029ab96d5271df83bfd4de01aeaa0b8d0647c023edcc97787666ca457aa18a9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6f6517778467c160ab2997b6792fb457789ecbb58da9204e3c4a9e8d1b789ed(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0051d9ed94eb42b0d8f41b517dbab424e6b016ccd95fda52fae7900e6c773833(
    *,
    parameter_name: builtins.str,
    parameter_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10d0cf9a7e5ad0f39e4c2325532b8a4ad5ccd7cd37c16ad8dbbdb7c948035106(
    *,
    document_name: typing.Optional[builtins.str] = None,
    document_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb7114b56400f450b835ab5d3aed18b5a4e6466e2dad2710b6844c6e70ef670e(
    *,
    conformance_pack_name: builtins.str,
    conformance_pack_input_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConformancePack.ConformancePackInputParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    delivery_s3_bucket: typing.Optional[builtins.str] = None,
    delivery_s3_key_prefix: typing.Optional[builtins.str] = None,
    template_body: typing.Optional[builtins.str] = None,
    template_s3_uri: typing.Optional[builtins.str] = None,
    template_ssm_document_details: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73c6e198efe26973129b68257eec368d6f11d6482310ee44da30ea815b09ce44(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    s3_bucket_name: builtins.str,
    config_snapshot_delivery_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    s3_key_prefix: typing.Optional[builtins.str] = None,
    s3_kms_key_arn: typing.Optional[builtins.str] = None,
    sns_topic_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93fe2fc089232415921cfb7f1987ad394874d5cec29ce9cd68d50744a0667515(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86778f392aecf273d1b4f4f57d53afa9b547f8fc6e6e320ef041d3b56e79f1d3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12454c1d1b821f4416cba3de981294f5dbd46e9d821e3996f737b570da3a9428(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29732799858d5a51a49b644a23b9487d8a731f17a76776d46c2a417f67da3159(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1c1e8db307d687d985abe819d5a1478a0354508356913373a8ad756e39975e9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e52266b167ad8133727ace537e117b4211b9b1601117d67caf7806c3954ef7f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__004463c97f710f28b3097f13305e10414949a4af5d0c981486867fd7166ee1f5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ec3498b9deb557429daadb315089fa9733a0d0a1516f9379188370be46f7f5d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__824c2ae974da56cf59c6872d5c3038e4fbf831ced2eb0f0d54679ffd8d7f35d0(
    *,
    delivery_frequency: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0cdaf5740787bc293a2cfbbc714aaffedb113a45f3a519fd5ee5defd54f724f(
    *,
    s3_bucket_name: builtins.str,
    config_snapshot_delivery_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryChannel.ConfigSnapshotDeliveryPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    s3_key_prefix: typing.Optional[builtins.str] = None,
    s3_kms_key_arn: typing.Optional[builtins.str] = None,
    sns_topic_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbb132a46c30059a4907d7496d2b696999321fd7c5b82f7812c5a4d9bf7ffdef(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    organization_config_rule_name: builtins.str,
    excluded_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    organization_custom_policy_rule_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationConfigRule.OrganizationCustomPolicyRuleMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    organization_custom_rule_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    organization_managed_rule_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e581ed53a72e9f3241819d7b60aee8c45b6d8882e96a3754518305e3004fbe5(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fa3a06ce143fa26917309b4aad611deb91282cec0652e424ae8e59eab1c0f4b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22e78630a330158f7539628357991f18a40deeba1fd6717ad961c7b74d3e220a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e24ca951119404bbb132d0e9fc6bac7e6de317bfd3583fa6527330cb5d68d99a(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d092f1b41cbf019a6c2f797b420e8cb6cce29c52a1fb671c69086ff9b8083246(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOrganizationConfigRule.OrganizationCustomPolicyRuleMetadataProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c45ab894736dadec9d2a359d9fb78b8cce28027988ec287fb21ff6deaac97ea7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afcd0c2707f5eb2640b1df26b94e2a0dc017a9171de66ccba46831ec339d624b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__016ff97a5da2c8c200eb9588ecaeb29452dbdd2d720dfa609e6359881809c740(
    *,
    policy_text: builtins.str,
    runtime: builtins.str,
    debug_log_delivery_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[builtins.str] = None,
    maximum_execution_frequency: typing.Optional[builtins.str] = None,
    organization_config_rule_trigger_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    resource_id_scope: typing.Optional[builtins.str] = None,
    resource_types_scope: typing.Optional[typing.Sequence[builtins.str]] = None,
    tag_key_scope: typing.Optional[builtins.str] = None,
    tag_value_scope: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__577ff8fffcd60b024a0a0af5c8c7405c61a255f395abee4abfc89e9a61d61339(
    *,
    lambda_function_arn: builtins.str,
    organization_config_rule_trigger_types: typing.Sequence[builtins.str],
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[builtins.str] = None,
    maximum_execution_frequency: typing.Optional[builtins.str] = None,
    resource_id_scope: typing.Optional[builtins.str] = None,
    resource_types_scope: typing.Optional[typing.Sequence[builtins.str]] = None,
    tag_key_scope: typing.Optional[builtins.str] = None,
    tag_value_scope: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dc57dfb13d36d34c8df89d07bf5b91f2f225b7f64fcaf1e0ec85cc4bf0008e6(
    *,
    rule_identifier: builtins.str,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[builtins.str] = None,
    maximum_execution_frequency: typing.Optional[builtins.str] = None,
    resource_id_scope: typing.Optional[builtins.str] = None,
    resource_types_scope: typing.Optional[typing.Sequence[builtins.str]] = None,
    tag_key_scope: typing.Optional[builtins.str] = None,
    tag_value_scope: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a10a93cf13b9b686cb420cfd72e8482fe531eebf751b0545e33ff1fa1739935(
    *,
    organization_config_rule_name: builtins.str,
    excluded_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    organization_custom_policy_rule_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationConfigRule.OrganizationCustomPolicyRuleMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    organization_custom_rule_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationConfigRule.OrganizationCustomRuleMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    organization_managed_rule_metadata: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationConfigRule.OrganizationManagedRuleMetadataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e30e375d1e6ca8bc1f56bcae0c6e77507133aca25c3deeb11629cc28c42740b7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    organization_conformance_pack_name: builtins.str,
    conformance_pack_input_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationConformancePack.ConformancePackInputParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    delivery_s3_bucket: typing.Optional[builtins.str] = None,
    delivery_s3_key_prefix: typing.Optional[builtins.str] = None,
    excluded_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    template_body: typing.Optional[builtins.str] = None,
    template_s3_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f252aeb695f75bc6a666da23c7215e6f51f866eee755884677a99c1e93dc7a12(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__972e7004ff93e8f6b80e4e18e235827cfb0a38ebe7df44468feef3093249b3bf(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cea7f4b86b4812225b1fd37ba822b06ca4f8bd2b4a689d8f0e20d4123126e765(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__159adc773b03fcb350f20741e9412fc5c36ec7df507a92c7262d5956c971d644(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnOrganizationConformancePack.ConformancePackInputParameterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a94f3e9391cd9ccab63b3545ca2965f2b81da196ec3ed606dc2485e2d2bbba60(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ae88516decc5ecfaa94d5667954693ac8954509566cfdc6d9a34f01c9b4c99d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__febab378993c1407f9ee864835af34497e5cfa444855d849d7a49b108cdac530(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d860cd3b0fe658d27c522bab37bf76c633dcd9da0ecbb8f7f0f2f92015a535a6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e88d12b7509e23789f96b51f072d3f7653802810b5db55480548e0a7bb433046(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e87ad63785baef983f0ec5a1a9627bbeadc5dda671b5ee551b1239daf8a0f13d(
    *,
    parameter_name: builtins.str,
    parameter_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d72ae72e83823c856a2d710ca24a4c227a6d6b865d8fef8ea164121282f98af(
    *,
    organization_conformance_pack_name: builtins.str,
    conformance_pack_input_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationConformancePack.ConformancePackInputParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    delivery_s3_bucket: typing.Optional[builtins.str] = None,
    delivery_s3_key_prefix: typing.Optional[builtins.str] = None,
    excluded_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    template_body: typing.Optional[builtins.str] = None,
    template_s3_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d77d8d51b1a809acec3ca2be829980e6b8f99140bb4eb3ce00b9209c088915c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    config_rule_name: builtins.str,
    target_id: builtins.str,
    target_type: builtins.str,
    automatic: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    execution_controls: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRemediationConfiguration.ExecutionControlsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    maximum_automatic_attempts: typing.Optional[jsii.Number] = None,
    parameters: typing.Any = None,
    resource_type: typing.Optional[builtins.str] = None,
    retry_attempt_seconds: typing.Optional[jsii.Number] = None,
    target_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74c36a39512198e1aaa76b683ab3d6faa2dedf6814529e3325ab9fdf03a47934(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0981270ccb35fe1ed87d60ce8737ba6f99a474a8edb4981354a5adf2e9e9369b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aec925175a5fdb6367c84a01b084043a639caa8c4046c1a46694ae861ddbfeec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__728a3fb0792a163b0d41711a1026e997d23c3bab737c4d3fc401219d2e69a7c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8693bd26f1e00cf82d388d4d0c6a4d195b1e165878b4d05bd62ebfe3dd4c25b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a612c6be9716c299f22f0fc2b57c084a7cafde2f9ec8ebed4b31decea797bb9(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__923c16d43d84ed6ed11e372e8cd76942cbebbe48641cade38fc40a0c5b8a7f12(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRemediationConfiguration.ExecutionControlsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5714155a99562d59349d9e442fb9b95dde4b3edc8e0c0c6ed79babb5d6067731(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__791d50036178abe388db7c3245e225f2e7ae9d06d20e7b2503c60ea3460eb769(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07705cb1e720ab1182823f69be5c3be2ef6f68a41b55f739f5df8c1a9c30deff(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a02058d16a54cc526726991d338a7198653ae37da9de8b8e8aa6f724c390148d(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__526beea102f85b306c0a794c0c56ee453c40e4cbf63ae9026fc54ca9079a1d84(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b9ea89c127bf27cc238eb72a592537954543d3bd38eb16e403d7b344a0f4b06(
    *,
    ssm_controls: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRemediationConfiguration.SsmControlsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83268c4a5aa9dd16fbcd9db136b72315f14ed7f5e88cd78d4a8316697c24962a(
    *,
    resource_value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRemediationConfiguration.ResourceValueProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    static_value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRemediationConfiguration.StaticValueProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c9b5643d1901ce9d9e3cb8822a2e3bf181afe82eb235c809f78ece9baf11247(
    *,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c78a12657b478ea0405bceec564d4064e3d948aa0c923a6c353813501256977(
    *,
    concurrent_execution_rate_percentage: typing.Optional[jsii.Number] = None,
    error_percentage: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40ba6e78a4bc7257e8360741f44912082b2a4d686ec43d8c0869c777777223a0(
    *,
    value: typing.Optional[typing.Sequence[builtins.str]] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f0c40c5aeff9a13df456a7637c89ca82a249888a8e5563b98aa3e2856779fd6(
    *,
    config_rule_name: builtins.str,
    target_id: builtins.str,
    target_type: builtins.str,
    automatic: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    execution_controls: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRemediationConfiguration.ExecutionControlsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    maximum_automatic_attempts: typing.Optional[jsii.Number] = None,
    parameters: typing.Any = None,
    resource_type: typing.Optional[builtins.str] = None,
    retry_attempt_seconds: typing.Optional[jsii.Number] = None,
    target_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f740fdda2b469339e90610372faa181ce8f5c105aada22101b165e104f0931d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    query_expression: builtins.str,
    query_name: builtins.str,
    query_description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07accbd2024de757d267b6a56c9c69945d6e00475dcbebdcb2827b570958a6c3(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__def101baeae59836b51a0510d3933e645988c353a9a0ddeae879b5d45da36530(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68f07b8140bc1756df33b7349243de220a74acc8b22b3147e10df17d805bc46e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c2d99f1e6f7c25ab75d279f03683a97d527c922ec9fa2631ca2d69a67087d7e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ed15ad66590b2bdac4f3a3adc1b4a104cfd7ec4d8f6cbfbad2588531f9c38b7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1eb31c625f25801e6c38cec9ee395832782b987abddb68d127cc6e79701d2fb8(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69bfcb3d7c917dfc61f55867cacc3efcb5ef56fa63ad37f8f26635c038ca8c94(
    *,
    query_expression: builtins.str,
    query_name: builtins.str,
    query_description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50bd433608bc8223746dfd9182d27a03d33e9feb360d971e5fbe80b64c01bad7(
    id: builtins.str,
    *,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6febfef82b3f86776d6cee7dc380662e7260e6c87725a51aa2887e287633d64c(
    id: builtins.str,
    *,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a7e56664b002adfcae896eec3992132b8186b275c8bb2d9a117f442e9ddac36(
    id: builtins.str,
    *,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b04eb11639f1874bbc847a298e884e6c6104bf56bf29a6c68f11ca608818337a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    identifier: builtins.str,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
    rule_scope: typing.Optional[RuleScope] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd906bb9949fe90ea1d037daff0b00a51209fdc942e8985cd71522bfc1fdb93a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    config_rule_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a23a1b4dbfc55b4ed462cfe9bdf1561bd5e4f5a47d8e23742648befac9fbdb62(
    id: builtins.str,
    *,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2022c059de0a75d3a5144e438901a8b401177fd288452cd66f51ef4be8cf04f9(
    id: builtins.str,
    *,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73a59bb1baf3b28c1af78b03eef77dfa2dd896ce471e8f0e9bc3cc92f565135e(
    id: builtins.str,
    *,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04827ab0bb47eedff43c2f84b879e3697cdf9730cbb27993d70bf043fd305d6e(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__826b91f1363d629c0ed925d90a79b869890a41b6c4114592f18f237ecec2d251(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49514315a00f8eccd0c88567ab6fd7f8fd1f97e7d5382a88e6bb3dd5185d8c9b(
    value: typing.Optional[RuleScope],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d47c160bf4bb1dd7741c5139c7a3ea417f94283943a510318608d3a02ef3af69(
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__789e7d0bc168eb66eb1a98c5813daac930a5d1a0a7544dd838595180eccba39e(
    *,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
    rule_scope: typing.Optional[RuleScope] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c3113bd3d59601fad88eff4129cb100fd6ea61855418c78d070b9b942b6a3fd(
    resource_type: ResourceType,
    resource_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02f717c6b93d162c57dd0e440602591d6826daf133eb9d2cd6476d3ff4632896(
    resource_types: typing.Sequence[ResourceType],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__824a576061a9e684cc0cf31a6506e1aa0490f392890aaceb8f7c4288d4145499(
    key: builtins.str,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__169ed3b4e4a53c1239b7388f8b4f342054686b6693630d0139a3f739cdfadf74(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    max_age: typing.Optional[_Duration_4839e8c3] = None,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
    rule_scope: typing.Optional[RuleScope] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__777e9fc45f9c8a322b98f9c1a5e59fa61b582e46ce2e628d20a703d225da6262(
    *,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
    rule_scope: typing.Optional[RuleScope] = None,
    max_age: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a22b3986125c76fb9e9557349b6727e4d1c0b600ef5e07d36a6ef3232ce01a7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    own_stack_only: typing.Optional[builtins.bool] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
    rule_scope: typing.Optional[RuleScope] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6e3aa47b4b02ba66dc0d2476d22bede4156332edf92696248dc715d6621a4a2(
    *,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
    rule_scope: typing.Optional[RuleScope] = None,
    own_stack_only: typing.Optional[builtins.bool] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3f2230d810e1b4e21cbed5c1f6dbaae3f6b443915ac3b8148dd5cc54a19e75a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    topics: typing.Optional[typing.Sequence[_ITopic_9eca4852]] = None,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
    rule_scope: typing.Optional[RuleScope] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4a2e1a2e2112721950f4e16046156e3b9bff53c55c515662c906f895bef67d1(
    *,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
    rule_scope: typing.Optional[RuleScope] = None,
    topics: typing.Optional[typing.Sequence[_ITopic_9eca4852]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49010e8081bbdd3bfbafae78ccebf0b5a42d400543b3dff90687e28d2c491579(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy_text: builtins.str,
    enable_debug_log: typing.Optional[builtins.bool] = None,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
    rule_scope: typing.Optional[RuleScope] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e40e3bd2d39a3dc7854fedb9fe3187292fff5413ee20f739e96f26a0ddf0efd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    config_rule_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a0a36a2cb813a5fe745e4bea0f64d4c5a9026b5c50474a53297e9e20b6fd81e(
    id: builtins.str,
    *,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39e7a300478811593a99ff8f1fed3908300731aab8791186b6cf1dad84b8a856(
    id: builtins.str,
    *,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a30be9c312961f8a2abd3a82da4460a1bd1fc45702591da31bfc9c17b11ddcd(
    id: builtins.str,
    *,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b9854d10077a651dbdf4a0cba3107e925b9c9a611c8097fed5bcc7444e15b83(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9abd1840e8081b6260fc81d74f36283b1fe5d04439637f73b38817fbca86b313(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef65597b7cc84c802aee5d97e6dbc9dbf9e0f04df2ae41e5102e9265b7960d0f(
    value: typing.Optional[RuleScope],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a248d79f961151a1c3a0a4ffba1d7f034b78164fd67cc63e24d802e6fca8c2e(
    *,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
    rule_scope: typing.Optional[RuleScope] = None,
    policy_text: builtins.str,
    enable_debug_log: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c04b50bb256529db27e261da69377598f975841e3cdb477cd74feb70373983b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    lambda_function: _IFunction_6adb0ab8,
    configuration_changes: typing.Optional[builtins.bool] = None,
    periodic: typing.Optional[builtins.bool] = None,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
    rule_scope: typing.Optional[RuleScope] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eea17ae081715a75c721bf7b8a98441fbcd9d3fdfaf56f61d888cd4d5a4e8ab3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    config_rule_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1326aee63fdb27f4bc6888e53a1aaad7c4d6c4bd2bf0661852059dfb412654c1(
    id: builtins.str,
    *,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8fb04d46bf1c7afea8e0849d3e449732008011a1668b9836310c1101b73043c(
    id: builtins.str,
    *,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ab48da45e6070573de565a2b77e458a32622a57d5f1b3e1b3219c2bd2236bda(
    id: builtins.str,
    *,
    target: typing.Optional[_IRuleTarget_7a91f454] = None,
    cross_stack_scope: typing.Optional[_constructs_77d1e7e8.Construct] = None,
    description: typing.Optional[builtins.str] = None,
    event_pattern: typing.Optional[typing.Union[_EventPattern_fe557901, typing.Dict[builtins.str, typing.Any]]] = None,
    rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c0958f3032e21e6d261e16c22aa71b2651c7a065516dfb3c5643d0d9c874710(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d658d05e8291c14eee0e010031415e38f12fcc5a172cffd783e9708dd81b597f(
    value: typing.Optional[builtins.bool],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4a42de8a257fafa046633793b8c78f666811737b6939072d51be06693e271c8(
    value: typing.Optional[RuleScope],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__218427563a034726fd41356c6d38c7959e2a44897cb1d6d9133bc9254a35c9f0(
    *,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
    rule_scope: typing.Optional[RuleScope] = None,
    lambda_function: _IFunction_6adb0ab8,
    configuration_changes: typing.Optional[builtins.bool] = None,
    periodic: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__feaff635e0230e65515841ea744975d751e424acf376b8ed530119931a2ea4ed(
    *,
    config_rule_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    input_parameters: typing.Optional[typing.Mapping[builtins.str, typing.Any]] = None,
    maximum_execution_frequency: typing.Optional[MaximumExecutionFrequency] = None,
    rule_scope: typing.Optional[RuleScope] = None,
    identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
