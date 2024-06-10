'''
# Amazon Data Lifecycle Manager Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_dlm as dlm
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for DLM construct libraries](https://constructs.dev/search?q=dlm)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::DLM resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DLM.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::DLM](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DLM.html).

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
class CfnLifecyclePolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_dlm.CfnLifecyclePolicy",
):
    '''Specifies a lifecycle policy, which is used to automate operations on Amazon EBS resources.

    The properties are required when you add a lifecycle policy and optional when you update a lifecycle policy.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html
    :cloudformationResource: AWS::DLM::LifecyclePolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_dlm as dlm
        
        # cross_region_copy_targets: Any
        # exclude_tags: Any
        # exclude_volume_types: Any
        
        cfn_lifecycle_policy = dlm.CfnLifecyclePolicy(self, "MyCfnLifecyclePolicy",
            copy_tags=False,
            create_interval=123,
            cross_region_copy_targets=cross_region_copy_targets,
            default_policy="defaultPolicy",
            description="description",
            exclusions=dlm.CfnLifecyclePolicy.ExclusionsProperty(
                exclude_boot_volumes=False,
                exclude_tags=exclude_tags,
                exclude_volume_types=exclude_volume_types
            ),
            execution_role_arn="executionRoleArn",
            extend_deletion=False,
            policy_details=dlm.CfnLifecyclePolicy.PolicyDetailsProperty(
                actions=[dlm.CfnLifecyclePolicy.ActionProperty(
                    cross_region_copy=[dlm.CfnLifecyclePolicy.CrossRegionCopyActionProperty(
                        encryption_configuration=dlm.CfnLifecyclePolicy.EncryptionConfigurationProperty(
                            encrypted=False,
        
                            # the properties below are optional
                            cmk_arn="cmkArn"
                        ),
                        target="target",
        
                        # the properties below are optional
                        retain_rule=dlm.CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty(
                            interval=123,
                            interval_unit="intervalUnit"
                        )
                    )],
                    name="name"
                )],
                copy_tags=False,
                create_interval=123,
                cross_region_copy_targets=cross_region_copy_targets,
                event_source=dlm.CfnLifecyclePolicy.EventSourceProperty(
                    type="type",
        
                    # the properties below are optional
                    parameters=dlm.CfnLifecyclePolicy.EventParametersProperty(
                        event_type="eventType",
                        snapshot_owner=["snapshotOwner"],
        
                        # the properties below are optional
                        description_regex="descriptionRegex"
                    )
                ),
                exclusions=dlm.CfnLifecyclePolicy.ExclusionsProperty(
                    exclude_boot_volumes=False,
                    exclude_tags=exclude_tags,
                    exclude_volume_types=exclude_volume_types
                ),
                extend_deletion=False,
                parameters=dlm.CfnLifecyclePolicy.ParametersProperty(
                    exclude_boot_volume=False,
                    exclude_data_volume_tags=[CfnTag(
                        key="key",
                        value="value"
                    )],
                    no_reboot=False
                ),
                policy_language="policyLanguage",
                policy_type="policyType",
                resource_locations=["resourceLocations"],
                resource_type="resourceType",
                resource_types=["resourceTypes"],
                retain_interval=123,
                schedules=[dlm.CfnLifecyclePolicy.ScheduleProperty(
                    archive_rule=dlm.CfnLifecyclePolicy.ArchiveRuleProperty(
                        retain_rule=dlm.CfnLifecyclePolicy.ArchiveRetainRuleProperty(
                            retention_archive_tier=dlm.CfnLifecyclePolicy.RetentionArchiveTierProperty(
                                count=123,
                                interval=123,
                                interval_unit="intervalUnit"
                            )
                        )
                    ),
                    copy_tags=False,
                    create_rule=dlm.CfnLifecyclePolicy.CreateRuleProperty(
                        cron_expression="cronExpression",
                        interval=123,
                        interval_unit="intervalUnit",
                        location="location",
                        scripts=[dlm.CfnLifecyclePolicy.ScriptProperty(
                            execute_operation_on_script_failure=False,
                            execution_handler="executionHandler",
                            execution_handler_service="executionHandlerService",
                            execution_timeout=123,
                            maximum_retry_count=123,
                            stages=["stages"]
                        )],
                        times=["times"]
                    ),
                    cross_region_copy_rules=[dlm.CfnLifecyclePolicy.CrossRegionCopyRuleProperty(
                        encrypted=False,
        
                        # the properties below are optional
                        cmk_arn="cmkArn",
                        copy_tags=False,
                        deprecate_rule=dlm.CfnLifecyclePolicy.CrossRegionCopyDeprecateRuleProperty(
                            interval=123,
                            interval_unit="intervalUnit"
                        ),
                        retain_rule=dlm.CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty(
                            interval=123,
                            interval_unit="intervalUnit"
                        ),
                        target="target",
                        target_region="targetRegion"
                    )],
                    deprecate_rule=dlm.CfnLifecyclePolicy.DeprecateRuleProperty(
                        count=123,
                        interval=123,
                        interval_unit="intervalUnit"
                    ),
                    fast_restore_rule=dlm.CfnLifecyclePolicy.FastRestoreRuleProperty(
                        availability_zones=["availabilityZones"],
                        count=123,
                        interval=123,
                        interval_unit="intervalUnit"
                    ),
                    name="name",
                    retain_rule=dlm.CfnLifecyclePolicy.RetainRuleProperty(
                        count=123,
                        interval=123,
                        interval_unit="intervalUnit"
                    ),
                    share_rules=[dlm.CfnLifecyclePolicy.ShareRuleProperty(
                        target_accounts=["targetAccounts"],
                        unshare_interval=123,
                        unshare_interval_unit="unshareIntervalUnit"
                    )],
                    tags_to_add=[CfnTag(
                        key="key",
                        value="value"
                    )],
                    variable_tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )],
                target_tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            ),
            retain_interval=123,
            state="state",
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
        copy_tags: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        create_interval: typing.Optional[jsii.Number] = None,
        cross_region_copy_targets: typing.Any = None,
        default_policy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        exclusions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.ExclusionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        extend_deletion: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        policy_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.PolicyDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        retain_interval: typing.Optional[jsii.Number] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param copy_tags: *[Default policies only]* Indicates whether the policy should copy tags from the source resource to the snapshot or AMI. If you do not specify a value, the default is ``false`` . Default: false
        :param create_interval: *[Default policies only]* Specifies how often the policy should run and create snapshots or AMIs. The creation frequency can range from 1 to 7 days. If you do not specify a value, the default is 1. Default: 1
        :param cross_region_copy_targets: *[Default policies only]* Specifies destination Regions for snapshot or AMI copies. You can specify up to 3 destination Regions. If you do not want to create cross-Region copies, omit this parameter.
        :param default_policy: *[Default policies only]* Specify the type of default policy to create. - To create a default policy for EBS snapshots, that creates snapshots of all volumes in the Region that do not have recent backups, specify ``VOLUME`` . - To create a default policy for EBS-backed AMIs, that creates EBS-backed AMIs from all instances in the Region that do not have recent backups, specify ``INSTANCE`` .
        :param description: A description of the lifecycle policy. The characters ^[0-9A-Za-z _-]+$ are supported.
        :param exclusions: *[Default policies only]* Specifies exclusion parameters for volumes or instances for which you do not want to create snapshots or AMIs. The policy will not create snapshots or AMIs for target resources that match any of the specified exclusion parameters.
        :param execution_role_arn: The Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the lifecycle policy.
        :param extend_deletion: *[Default policies only]* Defines the snapshot or AMI retention behavior for the policy if the source volume or instance is deleted, or if the policy enters the error, disabled, or deleted state. By default ( *ExtendDeletion=false* ): - If a source resource is deleted, Amazon Data Lifecycle Manager will continue to delete previously created snapshots or AMIs, up to but not including the last one, based on the specified retention period. If you want Amazon Data Lifecycle Manager to delete all snapshots or AMIs, including the last one, specify ``true`` . - If a policy enters the error, disabled, or deleted state, Amazon Data Lifecycle Manager stops deleting snapshots and AMIs. If you want Amazon Data Lifecycle Manager to continue deleting snapshots or AMIs, including the last one, if the policy enters one of these states, specify ``true`` . If you enable extended deletion ( *ExtendDeletion=true* ), you override both default behaviors simultaneously. If you do not specify a value, the default is ``false`` . Default: false
        :param policy_details: The configuration details of the lifecycle policy. .. epigraph:: If you create a default policy, you can specify the request parameters either in the request body, or in the PolicyDetails request structure, but not both.
        :param retain_interval: *[Default policies only]* Specifies how long the policy should retain snapshots or AMIs before deleting them. The retention period can range from 2 to 14 days, but it must be greater than the creation frequency to ensure that the policy retains at least 1 snapshot or AMI at any given time. If you do not specify a value, the default is 7. Default: 7
        :param state: The activation state of the lifecycle policy.
        :param tags: The tags to apply to the lifecycle policy during creation.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2602533fbe79433bf8a3cb4984e0ec983ab5d121243f4d319dfc6038c8b96bb3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLifecyclePolicyProps(
            copy_tags=copy_tags,
            create_interval=create_interval,
            cross_region_copy_targets=cross_region_copy_targets,
            default_policy=default_policy,
            description=description,
            exclusions=exclusions,
            execution_role_arn=execution_role_arn,
            extend_deletion=extend_deletion,
            policy_details=policy_details,
            retain_interval=retain_interval,
            state=state,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81434f0dc784e8376f1ea6bb29bea9761940fdfd0b638198d90f60d4d0f20218)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c006aacfdbc5fd2892b4f2c7ce867935b955bf498cc4be3e84b77318aa692f8)
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
        '''The Amazon Resource Name (ARN) of the lifecycle policy.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    @jsii.member(jsii_name="copyTags")
    def copy_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''*[Default policies only]* Indicates whether the policy should copy tags from the source resource to the snapshot or AMI.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "copyTags"))

    @copy_tags.setter
    def copy_tags(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f66e06f3dd5f4f31da0050465d9d93ec64ce872a39b9831bba0678e14fa5fbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "copyTags", value)

    @builtins.property
    @jsii.member(jsii_name="createInterval")
    def create_interval(self) -> typing.Optional[jsii.Number]:
        '''*[Default policies only]* Specifies how often the policy should run and create snapshots or AMIs.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "createInterval"))

    @create_interval.setter
    def create_interval(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e355d2d56ace5cc54090484cdfafed2a85a9b48fa91a8df756bb89f4e2e1a38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createInterval", value)

    @builtins.property
    @jsii.member(jsii_name="crossRegionCopyTargets")
    def cross_region_copy_targets(self) -> typing.Any:
        '''*[Default policies only]* Specifies destination Regions for snapshot or AMI copies.'''
        return typing.cast(typing.Any, jsii.get(self, "crossRegionCopyTargets"))

    @cross_region_copy_targets.setter
    def cross_region_copy_targets(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c77534ad651e2a8d67574cbcffaf68110be041f8971255d26c52491b23fdc32f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crossRegionCopyTargets", value)

    @builtins.property
    @jsii.member(jsii_name="defaultPolicy")
    def default_policy(self) -> typing.Optional[builtins.str]:
        '''*[Default policies only]* Specify the type of default policy to create.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultPolicy"))

    @default_policy.setter
    def default_policy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fad1b7a52123f254bb9f0374f3546651f50ece8ef16650fdab011f0bd968afda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the lifecycle policy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b2c4be1aa9ae388ae0c3732cd9d2523c470c0014606872fca1696f56269686d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="exclusions")
    def exclusions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ExclusionsProperty"]]:
        '''*[Default policies only]* Specifies exclusion parameters for volumes or instances for which you do not want to create snapshots or AMIs.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ExclusionsProperty"]], jsii.get(self, "exclusions"))

    @exclusions.setter
    def exclusions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ExclusionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__697e92d466d31df6c2b785374b032b06ea49a5f0a5f4866b11f7a97c11bc27e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclusions", value)

    @builtins.property
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the lifecycle policy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__269443eefb0de5680ef719eb02ee0fda9c83a2e5291fa03da5a458a188d7a7c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="extendDeletion")
    def extend_deletion(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''*[Default policies only]* Defines the snapshot or AMI retention behavior for the policy if the source volume or instance is deleted, or if the policy enters the error, disabled, or deleted state.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "extendDeletion"))

    @extend_deletion.setter
    def extend_deletion(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5a72190a4691449f1542993dcce214b4e84f38189762057ccaccba7f456d683)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extendDeletion", value)

    @builtins.property
    @jsii.member(jsii_name="policyDetails")
    def policy_details(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.PolicyDetailsProperty"]]:
        '''The configuration details of the lifecycle policy.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.PolicyDetailsProperty"]], jsii.get(self, "policyDetails"))

    @policy_details.setter
    def policy_details(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.PolicyDetailsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28d8dbca09903b09bcfda56929bc379ae4e79616a6e38d78042df2d24f6464a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDetails", value)

    @builtins.property
    @jsii.member(jsii_name="retainInterval")
    def retain_interval(self) -> typing.Optional[jsii.Number]:
        '''*[Default policies only]* Specifies how long the policy should retain snapshots or AMIs before deleting them.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retainInterval"))

    @retain_interval.setter
    def retain_interval(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82aed9e32e25d4555a6a4435c5a18828e06b80cc9bf8e04617ce499f7259e7a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retainInterval", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> typing.Optional[builtins.str]:
        '''The activation state of the lifecycle policy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "state"))

    @state.setter
    def state(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dec6c26d53f2189b6a1eceb4738437bca568a6c7616d987a2d4300b6648248c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to apply to the lifecycle policy during creation.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b27e3373e59304017b144dff4d6d34a89b633c266e7a9c06230a117c457228b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dlm.CfnLifecyclePolicy.ActionProperty",
        jsii_struct_bases=[],
        name_mapping={"cross_region_copy": "crossRegionCopy", "name": "name"},
    )
    class ActionProperty:
        def __init__(
            self,
            *,
            cross_region_copy: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.CrossRegionCopyActionProperty", typing.Dict[builtins.str, typing.Any]]]]],
            name: builtins.str,
        ) -> None:
            '''*[Event-based policies only]* Specifies an action for an event-based policy.

            :param cross_region_copy: The rule for copying shared snapshots across Regions.
            :param name: A descriptive name for the action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dlm as dlm
                
                action_property = dlm.CfnLifecyclePolicy.ActionProperty(
                    cross_region_copy=[dlm.CfnLifecyclePolicy.CrossRegionCopyActionProperty(
                        encryption_configuration=dlm.CfnLifecyclePolicy.EncryptionConfigurationProperty(
                            encrypted=False,
                
                            # the properties below are optional
                            cmk_arn="cmkArn"
                        ),
                        target="target",
                
                        # the properties below are optional
                        retain_rule=dlm.CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty(
                            interval=123,
                            interval_unit="intervalUnit"
                        )
                    )],
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9307e01a397f6690aa0752ac88ca2306a9ece8a8a78eb132935a5549dfbabada)
                check_type(argname="argument cross_region_copy", value=cross_region_copy, expected_type=type_hints["cross_region_copy"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cross_region_copy": cross_region_copy,
                "name": name,
            }

        @builtins.property
        def cross_region_copy(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.CrossRegionCopyActionProperty"]]]:
            '''The rule for copying shared snapshots across Regions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-action.html#cfn-dlm-lifecyclepolicy-action-crossregioncopy
            '''
            result = self._values.get("cross_region_copy")
            assert result is not None, "Required property 'cross_region_copy' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.CrossRegionCopyActionProperty"]]], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''A descriptive name for the action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-action.html#cfn-dlm-lifecyclepolicy-action-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dlm.CfnLifecyclePolicy.ArchiveRetainRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"retention_archive_tier": "retentionArchiveTier"},
    )
    class ArchiveRetainRuleProperty:
        def __init__(
            self,
            *,
            retention_archive_tier: typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.RetentionArchiveTierProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''*[Custom snapshot policies only]* Specifies information about the archive storage tier retention period.

            :param retention_archive_tier: Information about retention period in the Amazon EBS Snapshots Archive. For more information, see `Archive Amazon EBS snapshots <https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/snapshot-archive.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-archiveretainrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dlm as dlm
                
                archive_retain_rule_property = dlm.CfnLifecyclePolicy.ArchiveRetainRuleProperty(
                    retention_archive_tier=dlm.CfnLifecyclePolicy.RetentionArchiveTierProperty(
                        count=123,
                        interval=123,
                        interval_unit="intervalUnit"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__69b614c12df5d26aa7cc0ea985df41404caf1067f445bd324dc6fa55b9b8c625)
                check_type(argname="argument retention_archive_tier", value=retention_archive_tier, expected_type=type_hints["retention_archive_tier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "retention_archive_tier": retention_archive_tier,
            }

        @builtins.property
        def retention_archive_tier(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.RetentionArchiveTierProperty"]:
            '''Information about retention period in the Amazon EBS Snapshots Archive.

            For more information, see `Archive Amazon EBS snapshots <https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/snapshot-archive.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-archiveretainrule.html#cfn-dlm-lifecyclepolicy-archiveretainrule-retentionarchivetier
            '''
            result = self._values.get("retention_archive_tier")
            assert result is not None, "Required property 'retention_archive_tier' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.RetentionArchiveTierProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ArchiveRetainRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dlm.CfnLifecyclePolicy.ArchiveRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"retain_rule": "retainRule"},
    )
    class ArchiveRuleProperty:
        def __init__(
            self,
            *,
            retain_rule: typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.ArchiveRetainRuleProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''*[Custom snapshot policies only]* Specifies a snapshot archiving rule for a schedule.

            :param retain_rule: Information about the retention period for the snapshot archiving rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-archiverule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dlm as dlm
                
                archive_rule_property = dlm.CfnLifecyclePolicy.ArchiveRuleProperty(
                    retain_rule=dlm.CfnLifecyclePolicy.ArchiveRetainRuleProperty(
                        retention_archive_tier=dlm.CfnLifecyclePolicy.RetentionArchiveTierProperty(
                            count=123,
                            interval=123,
                            interval_unit="intervalUnit"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e8e1039f6cae4097770e1e2f744b67af71fec5dee8b6c811d16906aabf00fccb)
                check_type(argname="argument retain_rule", value=retain_rule, expected_type=type_hints["retain_rule"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "retain_rule": retain_rule,
            }

        @builtins.property
        def retain_rule(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ArchiveRetainRuleProperty"]:
            '''Information about the retention period for the snapshot archiving rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-archiverule.html#cfn-dlm-lifecyclepolicy-archiverule-retainrule
            '''
            result = self._values.get("retain_rule")
            assert result is not None, "Required property 'retain_rule' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ArchiveRetainRuleProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ArchiveRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dlm.CfnLifecyclePolicy.CreateRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cron_expression": "cronExpression",
            "interval": "interval",
            "interval_unit": "intervalUnit",
            "location": "location",
            "scripts": "scripts",
            "times": "times",
        },
    )
    class CreateRuleProperty:
        def __init__(
            self,
            *,
            cron_expression: typing.Optional[builtins.str] = None,
            interval: typing.Optional[jsii.Number] = None,
            interval_unit: typing.Optional[builtins.str] = None,
            location: typing.Optional[builtins.str] = None,
            scripts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.ScriptProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            times: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''*[Custom snapshot and AMI policies only]* Specifies when the policy should create snapshots or AMIs.

            .. epigraph::

               - You must specify either *CronExpression* , or *Interval* , *IntervalUnit* , and *Times* .
               - If you need to specify an `ArchiveRule <https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRule.html>`_ for the schedule, then you must specify a creation frequency of at least 28 days.

            :param cron_expression: The schedule, as a Cron expression. The schedule interval must be between 1 hour and 1 year. For more information, see the `Cron expressions reference <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cron-expressions.html>`_ in the *Amazon EventBridge User Guide* .
            :param interval: The interval between snapshots. The supported values are 1, 2, 3, 4, 6, 8, 12, and 24.
            :param interval_unit: The interval unit.
            :param location: *[Custom snapshot policies only]* Specifies the destination for snapshots created by the policy. To create snapshots in the same Region as the source resource, specify ``CLOUD`` . To create snapshots on the same Outpost as the source resource, specify ``OUTPOST_LOCAL`` . If you omit this parameter, ``CLOUD`` is used by default. If the policy targets resources in an AWS Region , then you must create snapshots in the same Region as the source resource. If the policy targets resources on an Outpost, then you can create snapshots on the same Outpost as the source resource, or in the Region of that Outpost.
            :param scripts: *[Custom snapshot policies that target instances only]* Specifies pre and/or post scripts for a snapshot lifecycle policy that targets instances. This is useful for creating application-consistent snapshots, or for performing specific administrative tasks before or after Amazon Data Lifecycle Manager initiates snapshot creation. For more information, see `Automating application-consistent snapshots with pre and post scripts <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/automate-app-consistent-backups.html>`_ .
            :param times: The time, in UTC, to start the operation. The supported format is hh:mm. The operation occurs within a one-hour window following the specified time. If you do not specify a time, Amazon Data Lifecycle Manager selects a time within the next 24 hours.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dlm as dlm
                
                create_rule_property = dlm.CfnLifecyclePolicy.CreateRuleProperty(
                    cron_expression="cronExpression",
                    interval=123,
                    interval_unit="intervalUnit",
                    location="location",
                    scripts=[dlm.CfnLifecyclePolicy.ScriptProperty(
                        execute_operation_on_script_failure=False,
                        execution_handler="executionHandler",
                        execution_handler_service="executionHandlerService",
                        execution_timeout=123,
                        maximum_retry_count=123,
                        stages=["stages"]
                    )],
                    times=["times"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a9b28ae8c7d63af3dc6b9cff4da91a651b9df9c94011501d2f12308ab311cacc)
                check_type(argname="argument cron_expression", value=cron_expression, expected_type=type_hints["cron_expression"])
                check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
                check_type(argname="argument interval_unit", value=interval_unit, expected_type=type_hints["interval_unit"])
                check_type(argname="argument location", value=location, expected_type=type_hints["location"])
                check_type(argname="argument scripts", value=scripts, expected_type=type_hints["scripts"])
                check_type(argname="argument times", value=times, expected_type=type_hints["times"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cron_expression is not None:
                self._values["cron_expression"] = cron_expression
            if interval is not None:
                self._values["interval"] = interval
            if interval_unit is not None:
                self._values["interval_unit"] = interval_unit
            if location is not None:
                self._values["location"] = location
            if scripts is not None:
                self._values["scripts"] = scripts
            if times is not None:
                self._values["times"] = times

        @builtins.property
        def cron_expression(self) -> typing.Optional[builtins.str]:
            '''The schedule, as a Cron expression.

            The schedule interval must be between 1 hour and 1 year. For more information, see the `Cron expressions reference <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-cron-expressions.html>`_ in the *Amazon EventBridge User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-cronexpression
            '''
            result = self._values.get("cron_expression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def interval(self) -> typing.Optional[jsii.Number]:
            '''The interval between snapshots.

            The supported values are 1, 2, 3, 4, 6, 8, 12, and 24.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-interval
            '''
            result = self._values.get("interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def interval_unit(self) -> typing.Optional[builtins.str]:
            '''The interval unit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-intervalunit
            '''
            result = self._values.get("interval_unit")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def location(self) -> typing.Optional[builtins.str]:
            '''*[Custom snapshot policies only]* Specifies the destination for snapshots created by the policy.

            To create snapshots in the same Region as the source resource, specify ``CLOUD`` . To create snapshots on the same Outpost as the source resource, specify ``OUTPOST_LOCAL`` . If you omit this parameter, ``CLOUD`` is used by default.

            If the policy targets resources in an AWS Region , then you must create snapshots in the same Region as the source resource. If the policy targets resources on an Outpost, then you can create snapshots on the same Outpost as the source resource, or in the Region of that Outpost.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-location
            '''
            result = self._values.get("location")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def scripts(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ScriptProperty"]]]]:
            '''*[Custom snapshot policies that target instances only]* Specifies pre and/or post scripts for a snapshot lifecycle policy that targets instances.

            This is useful for creating application-consistent snapshots, or for performing specific administrative tasks before or after Amazon Data Lifecycle Manager initiates snapshot creation.

            For more information, see `Automating application-consistent snapshots with pre and post scripts <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/automate-app-consistent-backups.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-scripts
            '''
            result = self._values.get("scripts")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ScriptProperty"]]]], result)

        @builtins.property
        def times(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The time, in UTC, to start the operation. The supported format is hh:mm.

            The operation occurs within a one-hour window following the specified time. If you do not specify a time, Amazon Data Lifecycle Manager selects a time within the next 24 hours.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-createrule.html#cfn-dlm-lifecyclepolicy-createrule-times
            '''
            result = self._values.get("times")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CreateRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dlm.CfnLifecyclePolicy.CrossRegionCopyActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption_configuration": "encryptionConfiguration",
            "target": "target",
            "retain_rule": "retainRule",
        },
    )
    class CrossRegionCopyActionProperty:
        def __init__(
            self,
            *,
            encryption_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            target: builtins.str,
            retain_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''*[Event-based policies only]* Specifies a cross-Region copy action for event-based policies.

            .. epigraph::

               To specify a cross-Region copy rule for snapshot and AMI policies, use `CrossRegionCopyRule <https://docs.aws.amazon.com/dlm/latest/APIReference/API_CrossRegionCopyRule.html>`_ .

            :param encryption_configuration: The encryption settings for the copied snapshot.
            :param target: The target Region.
            :param retain_rule: Specifies a retention rule for cross-Region snapshot copies created by snapshot or event-based policies, or cross-Region AMI copies created by AMI policies. After the retention period expires, the cross-Region copy is deleted.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dlm as dlm
                
                cross_region_copy_action_property = dlm.CfnLifecyclePolicy.CrossRegionCopyActionProperty(
                    encryption_configuration=dlm.CfnLifecyclePolicy.EncryptionConfigurationProperty(
                        encrypted=False,
                
                        # the properties below are optional
                        cmk_arn="cmkArn"
                    ),
                    target="target",
                
                    # the properties below are optional
                    retain_rule=dlm.CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty(
                        interval=123,
                        interval_unit="intervalUnit"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2c5fae284dc8f050edba69cd60584bdd81e13c9e3407c49aa284415b34c6b0e0)
                check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
                check_type(argname="argument target", value=target, expected_type=type_hints["target"])
                check_type(argname="argument retain_rule", value=retain_rule, expected_type=type_hints["retain_rule"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encryption_configuration": encryption_configuration,
                "target": target,
            }
            if retain_rule is not None:
                self._values["retain_rule"] = retain_rule

        @builtins.property
        def encryption_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.EncryptionConfigurationProperty"]:
            '''The encryption settings for the copied snapshot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyaction.html#cfn-dlm-lifecyclepolicy-crossregioncopyaction-encryptionconfiguration
            '''
            result = self._values.get("encryption_configuration")
            assert result is not None, "Required property 'encryption_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.EncryptionConfigurationProperty"], result)

        @builtins.property
        def target(self) -> builtins.str:
            '''The target Region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyaction.html#cfn-dlm-lifecyclepolicy-crossregioncopyaction-target
            '''
            result = self._values.get("target")
            assert result is not None, "Required property 'target' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def retain_rule(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty"]]:
            '''Specifies a retention rule for cross-Region snapshot copies created by snapshot or event-based policies, or cross-Region AMI copies created by AMI policies.

            After the retention period expires, the cross-Region copy is deleted.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyaction.html#cfn-dlm-lifecyclepolicy-crossregioncopyaction-retainrule
            '''
            result = self._values.get("retain_rule")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CrossRegionCopyActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dlm.CfnLifecyclePolicy.CrossRegionCopyDeprecateRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"interval": "interval", "interval_unit": "intervalUnit"},
    )
    class CrossRegionCopyDeprecateRuleProperty:
        def __init__(
            self,
            *,
            interval: jsii.Number,
            interval_unit: builtins.str,
        ) -> None:
            '''*[Custom AMI policies only]* Specifies an AMI deprecation rule for cross-Region AMI copies created by an AMI policy.

            :param interval: The period after which to deprecate the cross-Region AMI copies. The period must be less than or equal to the cross-Region AMI copy retention period, and it can't be greater than 10 years. This is equivalent to 120 months, 520 weeks, or 3650 days.
            :param interval_unit: The unit of time in which to measure the *Interval* . For example, to deprecate a cross-Region AMI copy after 3 months, specify ``Interval=3`` and ``IntervalUnit=MONTHS`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopydeprecaterule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dlm as dlm
                
                cross_region_copy_deprecate_rule_property = dlm.CfnLifecyclePolicy.CrossRegionCopyDeprecateRuleProperty(
                    interval=123,
                    interval_unit="intervalUnit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2a0d27b116ca50c00fc7180da16cbf918eaa7d7119243d09585b27a71cabd3d5)
                check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
                check_type(argname="argument interval_unit", value=interval_unit, expected_type=type_hints["interval_unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "interval": interval,
                "interval_unit": interval_unit,
            }

        @builtins.property
        def interval(self) -> jsii.Number:
            '''The period after which to deprecate the cross-Region AMI copies.

            The period must be less than or equal to the cross-Region AMI copy retention period, and it can't be greater than 10 years. This is equivalent to 120 months, 520 weeks, or 3650 days.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopydeprecaterule.html#cfn-dlm-lifecyclepolicy-crossregioncopydeprecaterule-interval
            '''
            result = self._values.get("interval")
            assert result is not None, "Required property 'interval' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def interval_unit(self) -> builtins.str:
            '''The unit of time in which to measure the *Interval* .

            For example, to deprecate a cross-Region AMI copy after 3 months, specify ``Interval=3`` and ``IntervalUnit=MONTHS`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopydeprecaterule.html#cfn-dlm-lifecyclepolicy-crossregioncopydeprecaterule-intervalunit
            '''
            result = self._values.get("interval_unit")
            assert result is not None, "Required property 'interval_unit' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CrossRegionCopyDeprecateRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dlm.CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"interval": "interval", "interval_unit": "intervalUnit"},
    )
    class CrossRegionCopyRetainRuleProperty:
        def __init__(
            self,
            *,
            interval: jsii.Number,
            interval_unit: builtins.str,
        ) -> None:
            '''Specifies a retention rule for cross-Region snapshot copies created by snapshot or event-based policies, or cross-Region AMI copies created by AMI policies.

            After the retention period expires, the cross-Region copy is deleted.

            :param interval: The amount of time to retain a cross-Region snapshot or AMI copy. The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.
            :param interval_unit: The unit of time for time-based retention. For example, to retain a cross-Region copy for 3 months, specify ``Interval=3`` and ``IntervalUnit=MONTHS`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyretainrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dlm as dlm
                
                cross_region_copy_retain_rule_property = dlm.CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty(
                    interval=123,
                    interval_unit="intervalUnit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1718151bfbb17d9a4452203d36f9b6216ee80d4bd34f379b785da8696d31352e)
                check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
                check_type(argname="argument interval_unit", value=interval_unit, expected_type=type_hints["interval_unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "interval": interval,
                "interval_unit": interval_unit,
            }

        @builtins.property
        def interval(self) -> jsii.Number:
            '''The amount of time to retain a cross-Region snapshot or AMI copy.

            The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyretainrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyretainrule-interval
            '''
            result = self._values.get("interval")
            assert result is not None, "Required property 'interval' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def interval_unit(self) -> builtins.str:
            '''The unit of time for time-based retention.

            For example, to retain a cross-Region copy for 3 months, specify ``Interval=3`` and ``IntervalUnit=MONTHS`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyretainrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyretainrule-intervalunit
            '''
            result = self._values.get("interval_unit")
            assert result is not None, "Required property 'interval_unit' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CrossRegionCopyRetainRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dlm.CfnLifecyclePolicy.CrossRegionCopyRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encrypted": "encrypted",
            "cmk_arn": "cmkArn",
            "copy_tags": "copyTags",
            "deprecate_rule": "deprecateRule",
            "retain_rule": "retainRule",
            "target": "target",
            "target_region": "targetRegion",
        },
    )
    class CrossRegionCopyRuleProperty:
        def __init__(
            self,
            *,
            encrypted: typing.Union[builtins.bool, _IResolvable_da3f097b],
            cmk_arn: typing.Optional[builtins.str] = None,
            copy_tags: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            deprecate_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.CrossRegionCopyDeprecateRuleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            retain_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            target: typing.Optional[builtins.str] = None,
            target_region: typing.Optional[builtins.str] = None,
        ) -> None:
            '''*[Custom snapshot and AMI policies only]* Specifies a cross-Region copy rule for a snapshot and AMI policies.

            .. epigraph::

               To specify a cross-Region copy action for event-based polices, use `CrossRegionCopyAction <https://docs.aws.amazon.com/dlm/latest/APIReference/API_CrossRegionCopyAction.html>`_ .

            :param encrypted: To encrypt a copy of an unencrypted snapshot if encryption by default is not enabled, enable encryption using this parameter. Copies of encrypted snapshots are encrypted, even if this parameter is false or if encryption by default is not enabled.
            :param cmk_arn: The Amazon Resource Name (ARN) of the AWS KMS key to use for EBS encryption. If this parameter is not specified, the default KMS key for the account is used.
            :param copy_tags: Indicates whether to copy all user-defined tags from the source snapshot or AMI to the cross-Region copy.
            :param deprecate_rule: *[Custom AMI policies only]* The AMI deprecation rule for cross-Region AMI copies created by the rule.
            :param retain_rule: The retention rule that indicates how long the cross-Region snapshot or AMI copies are to be retained in the destination Region.
            :param target: .. epigraph:: Use this parameter for snapshot policies only. For AMI policies, use *TargetRegion* instead. *[Custom snapshot policies only]* The target Region or the Amazon Resource Name (ARN) of the target Outpost for the snapshot copies.
            :param target_region: .. epigraph:: Use this parameter for AMI policies only. For snapshot policies, use *Target* instead. For snapshot policies created before the *Target* parameter was introduced, this parameter indicates the target Region for snapshot copies. *[Custom AMI policies only]* The target Region or the Amazon Resource Name (ARN) of the target Outpost for the snapshot copies.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dlm as dlm
                
                cross_region_copy_rule_property = dlm.CfnLifecyclePolicy.CrossRegionCopyRuleProperty(
                    encrypted=False,
                
                    # the properties below are optional
                    cmk_arn="cmkArn",
                    copy_tags=False,
                    deprecate_rule=dlm.CfnLifecyclePolicy.CrossRegionCopyDeprecateRuleProperty(
                        interval=123,
                        interval_unit="intervalUnit"
                    ),
                    retain_rule=dlm.CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty(
                        interval=123,
                        interval_unit="intervalUnit"
                    ),
                    target="target",
                    target_region="targetRegion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__43d1308154968094810a1e971a8121cb2c821bd4deca38281f7b51fde975f885)
                check_type(argname="argument encrypted", value=encrypted, expected_type=type_hints["encrypted"])
                check_type(argname="argument cmk_arn", value=cmk_arn, expected_type=type_hints["cmk_arn"])
                check_type(argname="argument copy_tags", value=copy_tags, expected_type=type_hints["copy_tags"])
                check_type(argname="argument deprecate_rule", value=deprecate_rule, expected_type=type_hints["deprecate_rule"])
                check_type(argname="argument retain_rule", value=retain_rule, expected_type=type_hints["retain_rule"])
                check_type(argname="argument target", value=target, expected_type=type_hints["target"])
                check_type(argname="argument target_region", value=target_region, expected_type=type_hints["target_region"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encrypted": encrypted,
            }
            if cmk_arn is not None:
                self._values["cmk_arn"] = cmk_arn
            if copy_tags is not None:
                self._values["copy_tags"] = copy_tags
            if deprecate_rule is not None:
                self._values["deprecate_rule"] = deprecate_rule
            if retain_rule is not None:
                self._values["retain_rule"] = retain_rule
            if target is not None:
                self._values["target"] = target
            if target_region is not None:
                self._values["target_region"] = target_region

        @builtins.property
        def encrypted(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''To encrypt a copy of an unencrypted snapshot if encryption by default is not enabled, enable encryption using this parameter.

            Copies of encrypted snapshots are encrypted, even if this parameter is false or if encryption by default is not enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-encrypted
            '''
            result = self._values.get("encrypted")
            assert result is not None, "Required property 'encrypted' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def cmk_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the AWS KMS key to use for EBS encryption.

            If this parameter is not specified, the default KMS key for the account is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-cmkarn
            '''
            result = self._values.get("cmk_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def copy_tags(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether to copy all user-defined tags from the source snapshot or AMI to the cross-Region copy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-copytags
            '''
            result = self._values.get("copy_tags")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def deprecate_rule(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.CrossRegionCopyDeprecateRuleProperty"]]:
            '''*[Custom AMI policies only]* The AMI deprecation rule for cross-Region AMI copies created by the rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-deprecaterule
            '''
            result = self._values.get("deprecate_rule")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.CrossRegionCopyDeprecateRuleProperty"]], result)

        @builtins.property
        def retain_rule(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty"]]:
            '''The retention rule that indicates how long the cross-Region snapshot or AMI copies are to be retained in the destination Region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-retainrule
            '''
            result = self._values.get("retain_rule")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty"]], result)

        @builtins.property
        def target(self) -> typing.Optional[builtins.str]:
            '''.. epigraph::

   Use this parameter for snapshot policies only. For AMI policies, use *TargetRegion* instead.

            *[Custom snapshot policies only]* The target Region or the Amazon Resource Name (ARN) of the target Outpost for the snapshot copies.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-target
            '''
            result = self._values.get("target")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_region(self) -> typing.Optional[builtins.str]:
            '''.. epigraph::

   Use this parameter for AMI policies only.

            For snapshot policies, use *Target* instead. For snapshot policies created before the *Target* parameter was introduced, this parameter indicates the target Region for snapshot copies.

            *[Custom AMI policies only]* The target Region or the Amazon Resource Name (ARN) of the target Outpost for the snapshot copies.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-crossregioncopyrule.html#cfn-dlm-lifecyclepolicy-crossregioncopyrule-targetregion
            '''
            result = self._values.get("target_region")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CrossRegionCopyRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dlm.CfnLifecyclePolicy.DeprecateRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "count": "count",
            "interval": "interval",
            "interval_unit": "intervalUnit",
        },
    )
    class DeprecateRuleProperty:
        def __init__(
            self,
            *,
            count: typing.Optional[jsii.Number] = None,
            interval: typing.Optional[jsii.Number] = None,
            interval_unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''*[Custom AMI policies only]* Specifies an AMI deprecation rule for AMIs created by an AMI lifecycle policy.

            For age-based schedules, you must specify *Interval* and *IntervalUnit* . For count-based schedules, you must specify *Count* .

            :param count: If the schedule has a count-based retention rule, this parameter specifies the number of oldest AMIs to deprecate. The count must be less than or equal to the schedule's retention count, and it can't be greater than 1000.
            :param interval: If the schedule has an age-based retention rule, this parameter specifies the period after which to deprecate AMIs created by the schedule. The period must be less than or equal to the schedule's retention period, and it can't be greater than 10 years. This is equivalent to 120 months, 520 weeks, or 3650 days.
            :param interval_unit: The unit of time in which to measure the *Interval* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-deprecaterule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dlm as dlm
                
                deprecate_rule_property = dlm.CfnLifecyclePolicy.DeprecateRuleProperty(
                    count=123,
                    interval=123,
                    interval_unit="intervalUnit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__df13b895e1f0fe3ab1717df947409da20e475efc7de490ec9a5646ed329ef27a)
                check_type(argname="argument count", value=count, expected_type=type_hints["count"])
                check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
                check_type(argname="argument interval_unit", value=interval_unit, expected_type=type_hints["interval_unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if count is not None:
                self._values["count"] = count
            if interval is not None:
                self._values["interval"] = interval
            if interval_unit is not None:
                self._values["interval_unit"] = interval_unit

        @builtins.property
        def count(self) -> typing.Optional[jsii.Number]:
            '''If the schedule has a count-based retention rule, this parameter specifies the number of oldest AMIs to deprecate.

            The count must be less than or equal to the schedule's retention count, and it can't be greater than 1000.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-deprecaterule.html#cfn-dlm-lifecyclepolicy-deprecaterule-count
            '''
            result = self._values.get("count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def interval(self) -> typing.Optional[jsii.Number]:
            '''If the schedule has an age-based retention rule, this parameter specifies the period after which to deprecate AMIs created by the schedule.

            The period must be less than or equal to the schedule's retention period, and it can't be greater than 10 years. This is equivalent to 120 months, 520 weeks, or 3650 days.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-deprecaterule.html#cfn-dlm-lifecyclepolicy-deprecaterule-interval
            '''
            result = self._values.get("interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def interval_unit(self) -> typing.Optional[builtins.str]:
            '''The unit of time in which to measure the *Interval* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-deprecaterule.html#cfn-dlm-lifecyclepolicy-deprecaterule-intervalunit
            '''
            result = self._values.get("interval_unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeprecateRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dlm.CfnLifecyclePolicy.EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"encrypted": "encrypted", "cmk_arn": "cmkArn"},
    )
    class EncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            encrypted: typing.Union[builtins.bool, _IResolvable_da3f097b],
            cmk_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''*[Event-based policies only]* Specifies the encryption settings for cross-Region snapshot copies created by event-based policies.

            :param encrypted: To encrypt a copy of an unencrypted snapshot when encryption by default is not enabled, enable encryption using this parameter. Copies of encrypted snapshots are encrypted, even if this parameter is false or when encryption by default is not enabled.
            :param cmk_arn: The Amazon Resource Name (ARN) of the AWS KMS key to use for EBS encryption. If this parameter is not specified, the default KMS key for the account is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-encryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dlm as dlm
                
                encryption_configuration_property = dlm.CfnLifecyclePolicy.EncryptionConfigurationProperty(
                    encrypted=False,
                
                    # the properties below are optional
                    cmk_arn="cmkArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1b9db946321cd9d24710d3479024da80bd3abb6be9bba91ad39d61a817fca6a2)
                check_type(argname="argument encrypted", value=encrypted, expected_type=type_hints["encrypted"])
                check_type(argname="argument cmk_arn", value=cmk_arn, expected_type=type_hints["cmk_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encrypted": encrypted,
            }
            if cmk_arn is not None:
                self._values["cmk_arn"] = cmk_arn

        @builtins.property
        def encrypted(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''To encrypt a copy of an unencrypted snapshot when encryption by default is not enabled, enable encryption using this parameter.

            Copies of encrypted snapshots are encrypted, even if this parameter is false or when encryption by default is not enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-encryptionconfiguration.html#cfn-dlm-lifecyclepolicy-encryptionconfiguration-encrypted
            '''
            result = self._values.get("encrypted")
            assert result is not None, "Required property 'encrypted' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def cmk_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the AWS KMS key to use for EBS encryption.

            If this parameter is not specified, the default KMS key for the account is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-encryptionconfiguration.html#cfn-dlm-lifecyclepolicy-encryptionconfiguration-cmkarn
            '''
            result = self._values.get("cmk_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dlm.CfnLifecyclePolicy.EventParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "event_type": "eventType",
            "snapshot_owner": "snapshotOwner",
            "description_regex": "descriptionRegex",
        },
    )
    class EventParametersProperty:
        def __init__(
            self,
            *,
            event_type: builtins.str,
            snapshot_owner: typing.Sequence[builtins.str],
            description_regex: typing.Optional[builtins.str] = None,
        ) -> None:
            '''*[Event-based policies only]* Specifies an event that activates an event-based policy.

            :param event_type: The type of event. Currently, only snapshot sharing events are supported.
            :param snapshot_owner: The IDs of the AWS accounts that can trigger policy by sharing snapshots with your account. The policy only runs if one of the specified AWS accounts shares a snapshot with your account.
            :param description_regex: The snapshot description that can trigger the policy. The description pattern is specified using a regular expression. The policy runs only if a snapshot with a description that matches the specified pattern is shared with your account. For example, specifying ``^.*Created for policy: policy-1234567890abcdef0.*$`` configures the policy to run only if snapshots created by policy ``policy-1234567890abcdef0`` are shared with your account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dlm as dlm
                
                event_parameters_property = dlm.CfnLifecyclePolicy.EventParametersProperty(
                    event_type="eventType",
                    snapshot_owner=["snapshotOwner"],
                
                    # the properties below are optional
                    description_regex="descriptionRegex"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f94e5460355048729001240653f8d96a3168ef0cbb26f5bc1ed5c17d02222336)
                check_type(argname="argument event_type", value=event_type, expected_type=type_hints["event_type"])
                check_type(argname="argument snapshot_owner", value=snapshot_owner, expected_type=type_hints["snapshot_owner"])
                check_type(argname="argument description_regex", value=description_regex, expected_type=type_hints["description_regex"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "event_type": event_type,
                "snapshot_owner": snapshot_owner,
            }
            if description_regex is not None:
                self._values["description_regex"] = description_regex

        @builtins.property
        def event_type(self) -> builtins.str:
            '''The type of event.

            Currently, only snapshot sharing events are supported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventparameters.html#cfn-dlm-lifecyclepolicy-eventparameters-eventtype
            '''
            result = self._values.get("event_type")
            assert result is not None, "Required property 'event_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def snapshot_owner(self) -> typing.List[builtins.str]:
            '''The IDs of the AWS accounts that can trigger policy by sharing snapshots with your account.

            The policy only runs if one of the specified AWS accounts shares a snapshot with your account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventparameters.html#cfn-dlm-lifecyclepolicy-eventparameters-snapshotowner
            '''
            result = self._values.get("snapshot_owner")
            assert result is not None, "Required property 'snapshot_owner' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def description_regex(self) -> typing.Optional[builtins.str]:
            '''The snapshot description that can trigger the policy.

            The description pattern is specified using a regular expression. The policy runs only if a snapshot with a description that matches the specified pattern is shared with your account.

            For example, specifying ``^.*Created for policy: policy-1234567890abcdef0.*$`` configures the policy to run only if snapshots created by policy ``policy-1234567890abcdef0`` are shared with your account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventparameters.html#cfn-dlm-lifecyclepolicy-eventparameters-descriptionregex
            '''
            result = self._values.get("description_regex")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dlm.CfnLifecyclePolicy.EventSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "parameters": "parameters"},
    )
    class EventSourceProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.EventParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''*[Event-based policies only]* Specifies an event that activates an event-based policy.

            :param type: The source of the event. Currently only managed CloudWatch Events rules are supported.
            :param parameters: Information about the event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dlm as dlm
                
                event_source_property = dlm.CfnLifecyclePolicy.EventSourceProperty(
                    type="type",
                
                    # the properties below are optional
                    parameters=dlm.CfnLifecyclePolicy.EventParametersProperty(
                        event_type="eventType",
                        snapshot_owner=["snapshotOwner"],
                
                        # the properties below are optional
                        description_regex="descriptionRegex"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3f5f81a0abf746f322239a01132f42ce76e2468d95f09b5832596d946ade19d8)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if parameters is not None:
                self._values["parameters"] = parameters

        @builtins.property
        def type(self) -> builtins.str:
            '''The source of the event.

            Currently only managed CloudWatch Events rules are supported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventsource.html#cfn-dlm-lifecyclepolicy-eventsource-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.EventParametersProperty"]]:
            '''Information about the event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-eventsource.html#cfn-dlm-lifecyclepolicy-eventsource-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.EventParametersProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dlm.CfnLifecyclePolicy.ExclusionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "exclude_boot_volumes": "excludeBootVolumes",
            "exclude_tags": "excludeTags",
            "exclude_volume_types": "excludeVolumeTypes",
        },
    )
    class ExclusionsProperty:
        def __init__(
            self,
            *,
            exclude_boot_volumes: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            exclude_tags: typing.Any = None,
            exclude_volume_types: typing.Any = None,
        ) -> None:
            '''*[Default policies only]* Specifies exclusion parameters for volumes or instances for which you do not want to create snapshots or AMIs.

            The policy will not create snapshots or AMIs for target resources that match any of the specified exclusion parameters.

            :param exclude_boot_volumes: *[Default policies for EBS snapshots only]* Indicates whether to exclude volumes that are attached to instances as the boot volume. If you exclude boot volumes, only volumes attached as data (non-boot) volumes will be backed up by the policy. To exclude boot volumes, specify ``true`` .
            :param exclude_tags: *[Default policies for EBS-backed AMIs only]* Specifies whether to exclude volumes that have specific tags.
            :param exclude_volume_types: *[Default policies for EBS snapshots only]* Specifies the volume types to exclude. Volumes of the specified types will not be targeted by the policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-exclusions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dlm as dlm
                
                # exclude_tags: Any
                # exclude_volume_types: Any
                
                exclusions_property = dlm.CfnLifecyclePolicy.ExclusionsProperty(
                    exclude_boot_volumes=False,
                    exclude_tags=exclude_tags,
                    exclude_volume_types=exclude_volume_types
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5692b64ab6dee50c1d5309ad0a3d609805882baacd6ea4c1c2d0733bc12c7502)
                check_type(argname="argument exclude_boot_volumes", value=exclude_boot_volumes, expected_type=type_hints["exclude_boot_volumes"])
                check_type(argname="argument exclude_tags", value=exclude_tags, expected_type=type_hints["exclude_tags"])
                check_type(argname="argument exclude_volume_types", value=exclude_volume_types, expected_type=type_hints["exclude_volume_types"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if exclude_boot_volumes is not None:
                self._values["exclude_boot_volumes"] = exclude_boot_volumes
            if exclude_tags is not None:
                self._values["exclude_tags"] = exclude_tags
            if exclude_volume_types is not None:
                self._values["exclude_volume_types"] = exclude_volume_types

        @builtins.property
        def exclude_boot_volumes(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''*[Default policies for EBS snapshots only]* Indicates whether to exclude volumes that are attached to instances as the boot volume.

            If you exclude boot volumes, only volumes attached as data (non-boot) volumes will be backed up by the policy. To exclude boot volumes, specify ``true`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-exclusions.html#cfn-dlm-lifecyclepolicy-exclusions-excludebootvolumes
            '''
            result = self._values.get("exclude_boot_volumes")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def exclude_tags(self) -> typing.Any:
            '''*[Default policies for EBS-backed AMIs only]* Specifies whether to exclude volumes that have specific tags.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-exclusions.html#cfn-dlm-lifecyclepolicy-exclusions-excludetags
            '''
            result = self._values.get("exclude_tags")
            return typing.cast(typing.Any, result)

        @builtins.property
        def exclude_volume_types(self) -> typing.Any:
            '''*[Default policies for EBS snapshots only]* Specifies the volume types to exclude.

            Volumes of the specified types will not be targeted by the policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-exclusions.html#cfn-dlm-lifecyclepolicy-exclusions-excludevolumetypes
            '''
            result = self._values.get("exclude_volume_types")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExclusionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dlm.CfnLifecyclePolicy.FastRestoreRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "availability_zones": "availabilityZones",
            "count": "count",
            "interval": "interval",
            "interval_unit": "intervalUnit",
        },
    )
    class FastRestoreRuleProperty:
        def __init__(
            self,
            *,
            availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
            count: typing.Optional[jsii.Number] = None,
            interval: typing.Optional[jsii.Number] = None,
            interval_unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''*[Custom snapshot policies only]* Specifies a rule for enabling fast snapshot restore for snapshots created by snapshot policies.

            You can enable fast snapshot restore based on either a count or a time interval.

            :param availability_zones: The Availability Zones in which to enable fast snapshot restore.
            :param count: The number of snapshots to be enabled with fast snapshot restore.
            :param interval: The amount of time to enable fast snapshot restore. The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.
            :param interval_unit: The unit of time for enabling fast snapshot restore.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dlm as dlm
                
                fast_restore_rule_property = dlm.CfnLifecyclePolicy.FastRestoreRuleProperty(
                    availability_zones=["availabilityZones"],
                    count=123,
                    interval=123,
                    interval_unit="intervalUnit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3c6091dc8881dc1eefedb91f093e87a24b9de27bbfd0785b7629a26e2bca19c9)
                check_type(argname="argument availability_zones", value=availability_zones, expected_type=type_hints["availability_zones"])
                check_type(argname="argument count", value=count, expected_type=type_hints["count"])
                check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
                check_type(argname="argument interval_unit", value=interval_unit, expected_type=type_hints["interval_unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if availability_zones is not None:
                self._values["availability_zones"] = availability_zones
            if count is not None:
                self._values["count"] = count
            if interval is not None:
                self._values["interval"] = interval
            if interval_unit is not None:
                self._values["interval_unit"] = interval_unit

        @builtins.property
        def availability_zones(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The Availability Zones in which to enable fast snapshot restore.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html#cfn-dlm-lifecyclepolicy-fastrestorerule-availabilityzones
            '''
            result = self._values.get("availability_zones")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def count(self) -> typing.Optional[jsii.Number]:
            '''The number of snapshots to be enabled with fast snapshot restore.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html#cfn-dlm-lifecyclepolicy-fastrestorerule-count
            '''
            result = self._values.get("count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def interval(self) -> typing.Optional[jsii.Number]:
            '''The amount of time to enable fast snapshot restore.

            The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html#cfn-dlm-lifecyclepolicy-fastrestorerule-interval
            '''
            result = self._values.get("interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def interval_unit(self) -> typing.Optional[builtins.str]:
            '''The unit of time for enabling fast snapshot restore.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-fastrestorerule.html#cfn-dlm-lifecyclepolicy-fastrestorerule-intervalunit
            '''
            result = self._values.get("interval_unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FastRestoreRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dlm.CfnLifecyclePolicy.ParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "exclude_boot_volume": "excludeBootVolume",
            "exclude_data_volume_tags": "excludeDataVolumeTags",
            "no_reboot": "noReboot",
        },
    )
    class ParametersProperty:
        def __init__(
            self,
            *,
            exclude_boot_volume: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            exclude_data_volume_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
            no_reboot: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''*[Custom snapshot and AMI policies only]* Specifies optional parameters for snapshot and AMI policies.

            The set of valid parameters depends on the combination of policy type and target resource type.

            If you choose to exclude boot volumes and you specify tags that consequently exclude all of the additional data volumes attached to an instance, then Amazon Data Lifecycle Manager will not create any snapshots for the affected instance, and it will emit a ``SnapshotsCreateFailed`` Amazon CloudWatch metric. For more information, see `Monitor your policies using Amazon CloudWatch <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitor-dlm-cw-metrics.html>`_ .

            :param exclude_boot_volume: *[Custom snapshot policies that target instances only]* Indicates whether to exclude the root volume from multi-volume snapshot sets. The default is ``false`` . If you specify ``true`` , then the root volumes attached to targeted instances will be excluded from the multi-volume snapshot sets created by the policy.
            :param exclude_data_volume_tags: *[Custom snapshot policies that target instances only]* The tags used to identify data (non-root) volumes to exclude from multi-volume snapshot sets. If you create a snapshot lifecycle policy that targets instances and you specify tags for this parameter, then data volumes with the specified tags that are attached to targeted instances will be excluded from the multi-volume snapshot sets created by the policy.
            :param no_reboot: *[Custom AMI policies only]* Indicates whether targeted instances are rebooted when the lifecycle policy runs. ``true`` indicates that targeted instances are not rebooted when the policy runs. ``false`` indicates that target instances are rebooted when the policy runs. The default is ``true`` (instances are not rebooted).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-parameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dlm as dlm
                
                parameters_property = dlm.CfnLifecyclePolicy.ParametersProperty(
                    exclude_boot_volume=False,
                    exclude_data_volume_tags=[CfnTag(
                        key="key",
                        value="value"
                    )],
                    no_reboot=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ce5c17fb8a6043f2aa8baec3f4fa0908ae761e69ffca448db0c9b5b5d6e208ef)
                check_type(argname="argument exclude_boot_volume", value=exclude_boot_volume, expected_type=type_hints["exclude_boot_volume"])
                check_type(argname="argument exclude_data_volume_tags", value=exclude_data_volume_tags, expected_type=type_hints["exclude_data_volume_tags"])
                check_type(argname="argument no_reboot", value=no_reboot, expected_type=type_hints["no_reboot"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if exclude_boot_volume is not None:
                self._values["exclude_boot_volume"] = exclude_boot_volume
            if exclude_data_volume_tags is not None:
                self._values["exclude_data_volume_tags"] = exclude_data_volume_tags
            if no_reboot is not None:
                self._values["no_reboot"] = no_reboot

        @builtins.property
        def exclude_boot_volume(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''*[Custom snapshot policies that target instances only]* Indicates whether to exclude the root volume from multi-volume snapshot sets.

            The default is ``false`` . If you specify ``true`` , then the root volumes attached to targeted instances will be excluded from the multi-volume snapshot sets created by the policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-parameters.html#cfn-dlm-lifecyclepolicy-parameters-excludebootvolume
            '''
            result = self._values.get("exclude_boot_volume")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def exclude_data_volume_tags(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]]:
            '''*[Custom snapshot policies that target instances only]* The tags used to identify data (non-root) volumes to exclude from multi-volume snapshot sets.

            If you create a snapshot lifecycle policy that targets instances and you specify tags for this parameter, then data volumes with the specified tags that are attached to targeted instances will be excluded from the multi-volume snapshot sets created by the policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-parameters.html#cfn-dlm-lifecyclepolicy-parameters-excludedatavolumetags
            '''
            result = self._values.get("exclude_data_volume_tags")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]], result)

        @builtins.property
        def no_reboot(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''*[Custom AMI policies only]* Indicates whether targeted instances are rebooted when the lifecycle policy runs.

            ``true`` indicates that targeted instances are not rebooted when the policy runs. ``false`` indicates that target instances are rebooted when the policy runs. The default is ``true`` (instances are not rebooted).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-parameters.html#cfn-dlm-lifecyclepolicy-parameters-noreboot
            '''
            result = self._values.get("no_reboot")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dlm.CfnLifecyclePolicy.PolicyDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "actions": "actions",
            "copy_tags": "copyTags",
            "create_interval": "createInterval",
            "cross_region_copy_targets": "crossRegionCopyTargets",
            "event_source": "eventSource",
            "exclusions": "exclusions",
            "extend_deletion": "extendDeletion",
            "parameters": "parameters",
            "policy_language": "policyLanguage",
            "policy_type": "policyType",
            "resource_locations": "resourceLocations",
            "resource_type": "resourceType",
            "resource_types": "resourceTypes",
            "retain_interval": "retainInterval",
            "schedules": "schedules",
            "target_tags": "targetTags",
        },
    )
    class PolicyDetailsProperty:
        def __init__(
            self,
            *,
            actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.ActionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            copy_tags: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            create_interval: typing.Optional[jsii.Number] = None,
            cross_region_copy_targets: typing.Any = None,
            event_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.EventSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            exclusions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.ExclusionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            extend_deletion: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.ParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            policy_language: typing.Optional[builtins.str] = None,
            policy_type: typing.Optional[builtins.str] = None,
            resource_locations: typing.Optional[typing.Sequence[builtins.str]] = None,
            resource_type: typing.Optional[builtins.str] = None,
            resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
            retain_interval: typing.Optional[jsii.Number] = None,
            schedules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.ScheduleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            target_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Specifies the configuration of a lifecycle policy.

            :param actions: *[Event-based policies only]* The actions to be performed when the event-based policy is activated. You can specify only one action per policy.
            :param copy_tags: *[Default policies only]* Indicates whether the policy should copy tags from the source resource to the snapshot or AMI. If you do not specify a value, the default is ``false`` . Default: false
            :param create_interval: *[Default policies only]* Specifies how often the policy should run and create snapshots or AMIs. The creation frequency can range from 1 to 7 days. If you do not specify a value, the default is 1. Default: 1
            :param cross_region_copy_targets: *[Default policies only]* Specifies destination Regions for snapshot or AMI copies. You can specify up to 3 destination Regions. If you do not want to create cross-Region copies, omit this parameter.
            :param event_source: *[Event-based policies only]* The event that activates the event-based policy.
            :param exclusions: *[Default policies only]* Specifies exclusion parameters for volumes or instances for which you do not want to create snapshots or AMIs. The policy will not create snapshots or AMIs for target resources that match any of the specified exclusion parameters.
            :param extend_deletion: *[Default policies only]* Defines the snapshot or AMI retention behavior for the policy if the source volume or instance is deleted, or if the policy enters the error, disabled, or deleted state. By default ( *ExtendDeletion=false* ): - If a source resource is deleted, Amazon Data Lifecycle Manager will continue to delete previously created snapshots or AMIs, up to but not including the last one, based on the specified retention period. If you want Amazon Data Lifecycle Manager to delete all snapshots or AMIs, including the last one, specify ``true`` . - If a policy enters the error, disabled, or deleted state, Amazon Data Lifecycle Manager stops deleting snapshots and AMIs. If you want Amazon Data Lifecycle Manager to continue deleting snapshots or AMIs, including the last one, if the policy enters one of these states, specify ``true`` . If you enable extended deletion ( *ExtendDeletion=true* ), you override both default behaviors simultaneously. If you do not specify a value, the default is ``false`` . Default: false
            :param parameters: *[Custom snapshot and AMI policies only]* A set of optional parameters for snapshot and AMI lifecycle policies. .. epigraph:: If you are modifying a policy that was created or previously modified using the Amazon Data Lifecycle Manager console, then you must include this parameter and specify either the default values or the new values that you require. You can't omit this parameter or set its values to null.
            :param policy_language: The type of policy to create. Specify one of the following:. - ``SIMPLIFIED`` To create a default policy. - ``STANDARD`` To create a custom policy.
            :param policy_type: The type of policy. Specify ``EBS_SNAPSHOT_MANAGEMENT`` to create a lifecycle policy that manages the lifecycle of Amazon EBS snapshots. Specify ``IMAGE_MANAGEMENT`` to create a lifecycle policy that manages the lifecycle of EBS-backed AMIs. Specify ``EVENT_BASED_POLICY`` to create an event-based policy that performs specific actions when a defined event occurs in your AWS account . The default is ``EBS_SNAPSHOT_MANAGEMENT`` .
            :param resource_locations: *[Custom snapshot and AMI policies only]* The location of the resources to backup. If the source resources are located in an AWS Region , specify ``CLOUD`` . If the source resources are located on an Outpost in your account, specify ``OUTPOST`` . If you specify ``OUTPOST`` , Amazon Data Lifecycle Manager backs up all resources of the specified type with matching target tags across all of the Outposts in your account.
            :param resource_type: *[Default policies only]* Specify the type of default policy to create. - To create a default policy for EBS snapshots, that creates snapshots of all volumes in the Region that do not have recent backups, specify ``VOLUME`` . - To create a default policy for EBS-backed AMIs, that creates EBS-backed AMIs from all instances in the Region that do not have recent backups, specify ``INSTANCE`` .
            :param resource_types: *[Custom snapshot policies only]* The target resource type for snapshot and AMI lifecycle policies. Use ``VOLUME`` to create snapshots of individual volumes or use ``INSTANCE`` to create multi-volume snapshots from the volumes for an instance.
            :param retain_interval: *[Default policies only]* Specifies how long the policy should retain snapshots or AMIs before deleting them. The retention period can range from 2 to 14 days, but it must be greater than the creation frequency to ensure that the policy retains at least 1 snapshot or AMI at any given time. If you do not specify a value, the default is 7. Default: 7
            :param schedules: *[Custom snapshot and AMI policies only]* The schedules of policy-defined actions for snapshot and AMI lifecycle policies. A policy can have up to four schedules—one mandatory schedule and up to three optional schedules.
            :param target_tags: *[Custom snapshot and AMI policies only]* The single tag that identifies targeted resources for this policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dlm as dlm
                
                # cross_region_copy_targets: Any
                # exclude_tags: Any
                # exclude_volume_types: Any
                
                policy_details_property = dlm.CfnLifecyclePolicy.PolicyDetailsProperty(
                    actions=[dlm.CfnLifecyclePolicy.ActionProperty(
                        cross_region_copy=[dlm.CfnLifecyclePolicy.CrossRegionCopyActionProperty(
                            encryption_configuration=dlm.CfnLifecyclePolicy.EncryptionConfigurationProperty(
                                encrypted=False,
                
                                # the properties below are optional
                                cmk_arn="cmkArn"
                            ),
                            target="target",
                
                            # the properties below are optional
                            retain_rule=dlm.CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty(
                                interval=123,
                                interval_unit="intervalUnit"
                            )
                        )],
                        name="name"
                    )],
                    copy_tags=False,
                    create_interval=123,
                    cross_region_copy_targets=cross_region_copy_targets,
                    event_source=dlm.CfnLifecyclePolicy.EventSourceProperty(
                        type="type",
                
                        # the properties below are optional
                        parameters=dlm.CfnLifecyclePolicy.EventParametersProperty(
                            event_type="eventType",
                            snapshot_owner=["snapshotOwner"],
                
                            # the properties below are optional
                            description_regex="descriptionRegex"
                        )
                    ),
                    exclusions=dlm.CfnLifecyclePolicy.ExclusionsProperty(
                        exclude_boot_volumes=False,
                        exclude_tags=exclude_tags,
                        exclude_volume_types=exclude_volume_types
                    ),
                    extend_deletion=False,
                    parameters=dlm.CfnLifecyclePolicy.ParametersProperty(
                        exclude_boot_volume=False,
                        exclude_data_volume_tags=[CfnTag(
                            key="key",
                            value="value"
                        )],
                        no_reboot=False
                    ),
                    policy_language="policyLanguage",
                    policy_type="policyType",
                    resource_locations=["resourceLocations"],
                    resource_type="resourceType",
                    resource_types=["resourceTypes"],
                    retain_interval=123,
                    schedules=[dlm.CfnLifecyclePolicy.ScheduleProperty(
                        archive_rule=dlm.CfnLifecyclePolicy.ArchiveRuleProperty(
                            retain_rule=dlm.CfnLifecyclePolicy.ArchiveRetainRuleProperty(
                                retention_archive_tier=dlm.CfnLifecyclePolicy.RetentionArchiveTierProperty(
                                    count=123,
                                    interval=123,
                                    interval_unit="intervalUnit"
                                )
                            )
                        ),
                        copy_tags=False,
                        create_rule=dlm.CfnLifecyclePolicy.CreateRuleProperty(
                            cron_expression="cronExpression",
                            interval=123,
                            interval_unit="intervalUnit",
                            location="location",
                            scripts=[dlm.CfnLifecyclePolicy.ScriptProperty(
                                execute_operation_on_script_failure=False,
                                execution_handler="executionHandler",
                                execution_handler_service="executionHandlerService",
                                execution_timeout=123,
                                maximum_retry_count=123,
                                stages=["stages"]
                            )],
                            times=["times"]
                        ),
                        cross_region_copy_rules=[dlm.CfnLifecyclePolicy.CrossRegionCopyRuleProperty(
                            encrypted=False,
                
                            # the properties below are optional
                            cmk_arn="cmkArn",
                            copy_tags=False,
                            deprecate_rule=dlm.CfnLifecyclePolicy.CrossRegionCopyDeprecateRuleProperty(
                                interval=123,
                                interval_unit="intervalUnit"
                            ),
                            retain_rule=dlm.CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty(
                                interval=123,
                                interval_unit="intervalUnit"
                            ),
                            target="target",
                            target_region="targetRegion"
                        )],
                        deprecate_rule=dlm.CfnLifecyclePolicy.DeprecateRuleProperty(
                            count=123,
                            interval=123,
                            interval_unit="intervalUnit"
                        ),
                        fast_restore_rule=dlm.CfnLifecyclePolicy.FastRestoreRuleProperty(
                            availability_zones=["availabilityZones"],
                            count=123,
                            interval=123,
                            interval_unit="intervalUnit"
                        ),
                        name="name",
                        retain_rule=dlm.CfnLifecyclePolicy.RetainRuleProperty(
                            count=123,
                            interval=123,
                            interval_unit="intervalUnit"
                        ),
                        share_rules=[dlm.CfnLifecyclePolicy.ShareRuleProperty(
                            target_accounts=["targetAccounts"],
                            unshare_interval=123,
                            unshare_interval_unit="unshareIntervalUnit"
                        )],
                        tags_to_add=[CfnTag(
                            key="key",
                            value="value"
                        )],
                        variable_tags=[CfnTag(
                            key="key",
                            value="value"
                        )]
                    )],
                    target_tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__64a970d220e1b895bd71825b15385fe27ec0bc3bb778dbb76043312a45c45696)
                check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
                check_type(argname="argument copy_tags", value=copy_tags, expected_type=type_hints["copy_tags"])
                check_type(argname="argument create_interval", value=create_interval, expected_type=type_hints["create_interval"])
                check_type(argname="argument cross_region_copy_targets", value=cross_region_copy_targets, expected_type=type_hints["cross_region_copy_targets"])
                check_type(argname="argument event_source", value=event_source, expected_type=type_hints["event_source"])
                check_type(argname="argument exclusions", value=exclusions, expected_type=type_hints["exclusions"])
                check_type(argname="argument extend_deletion", value=extend_deletion, expected_type=type_hints["extend_deletion"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
                check_type(argname="argument policy_language", value=policy_language, expected_type=type_hints["policy_language"])
                check_type(argname="argument policy_type", value=policy_type, expected_type=type_hints["policy_type"])
                check_type(argname="argument resource_locations", value=resource_locations, expected_type=type_hints["resource_locations"])
                check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
                check_type(argname="argument resource_types", value=resource_types, expected_type=type_hints["resource_types"])
                check_type(argname="argument retain_interval", value=retain_interval, expected_type=type_hints["retain_interval"])
                check_type(argname="argument schedules", value=schedules, expected_type=type_hints["schedules"])
                check_type(argname="argument target_tags", value=target_tags, expected_type=type_hints["target_tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if actions is not None:
                self._values["actions"] = actions
            if copy_tags is not None:
                self._values["copy_tags"] = copy_tags
            if create_interval is not None:
                self._values["create_interval"] = create_interval
            if cross_region_copy_targets is not None:
                self._values["cross_region_copy_targets"] = cross_region_copy_targets
            if event_source is not None:
                self._values["event_source"] = event_source
            if exclusions is not None:
                self._values["exclusions"] = exclusions
            if extend_deletion is not None:
                self._values["extend_deletion"] = extend_deletion
            if parameters is not None:
                self._values["parameters"] = parameters
            if policy_language is not None:
                self._values["policy_language"] = policy_language
            if policy_type is not None:
                self._values["policy_type"] = policy_type
            if resource_locations is not None:
                self._values["resource_locations"] = resource_locations
            if resource_type is not None:
                self._values["resource_type"] = resource_type
            if resource_types is not None:
                self._values["resource_types"] = resource_types
            if retain_interval is not None:
                self._values["retain_interval"] = retain_interval
            if schedules is not None:
                self._values["schedules"] = schedules
            if target_tags is not None:
                self._values["target_tags"] = target_tags

        @builtins.property
        def actions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ActionProperty"]]]]:
            '''*[Event-based policies only]* The actions to be performed when the event-based policy is activated.

            You can specify only one action per policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-actions
            '''
            result = self._values.get("actions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ActionProperty"]]]], result)

        @builtins.property
        def copy_tags(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''*[Default policies only]* Indicates whether the policy should copy tags from the source resource to the snapshot or AMI.

            If you do not specify a value, the default is ``false`` .

            Default: false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-copytags
            '''
            result = self._values.get("copy_tags")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def create_interval(self) -> typing.Optional[jsii.Number]:
            '''*[Default policies only]* Specifies how often the policy should run and create snapshots or AMIs.

            The creation frequency can range from 1 to 7 days. If you do not specify a value, the default is 1.

            Default: 1

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-createinterval
            '''
            result = self._values.get("create_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def cross_region_copy_targets(self) -> typing.Any:
            '''*[Default policies only]* Specifies destination Regions for snapshot or AMI copies.

            You can specify up to 3 destination Regions. If you do not want to create cross-Region copies, omit this parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-crossregioncopytargets
            '''
            result = self._values.get("cross_region_copy_targets")
            return typing.cast(typing.Any, result)

        @builtins.property
        def event_source(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.EventSourceProperty"]]:
            '''*[Event-based policies only]* The event that activates the event-based policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-eventsource
            '''
            result = self._values.get("event_source")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.EventSourceProperty"]], result)

        @builtins.property
        def exclusions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ExclusionsProperty"]]:
            '''*[Default policies only]* Specifies exclusion parameters for volumes or instances for which you do not want to create snapshots or AMIs.

            The policy will not create snapshots or AMIs for target resources that match any of the specified exclusion parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-exclusions
            '''
            result = self._values.get("exclusions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ExclusionsProperty"]], result)

        @builtins.property
        def extend_deletion(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''*[Default policies only]* Defines the snapshot or AMI retention behavior for the policy if the source volume or instance is deleted, or if the policy enters the error, disabled, or deleted state.

            By default ( *ExtendDeletion=false* ):

            - If a source resource is deleted, Amazon Data Lifecycle Manager will continue to delete previously created snapshots or AMIs, up to but not including the last one, based on the specified retention period. If you want Amazon Data Lifecycle Manager to delete all snapshots or AMIs, including the last one, specify ``true`` .
            - If a policy enters the error, disabled, or deleted state, Amazon Data Lifecycle Manager stops deleting snapshots and AMIs. If you want Amazon Data Lifecycle Manager to continue deleting snapshots or AMIs, including the last one, if the policy enters one of these states, specify ``true`` .

            If you enable extended deletion ( *ExtendDeletion=true* ), you override both default behaviors simultaneously.

            If you do not specify a value, the default is ``false`` .

            Default: false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-extenddeletion
            '''
            result = self._values.get("extend_deletion")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ParametersProperty"]]:
            '''*[Custom snapshot and AMI policies only]* A set of optional parameters for snapshot and AMI lifecycle policies.

            .. epigraph::

               If you are modifying a policy that was created or previously modified using the Amazon Data Lifecycle Manager console, then you must include this parameter and specify either the default values or the new values that you require. You can't omit this parameter or set its values to null.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ParametersProperty"]], result)

        @builtins.property
        def policy_language(self) -> typing.Optional[builtins.str]:
            '''The type of policy to create. Specify one of the following:.

            - ``SIMPLIFIED`` To create a default policy.
            - ``STANDARD`` To create a custom policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-policylanguage
            '''
            result = self._values.get("policy_language")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def policy_type(self) -> typing.Optional[builtins.str]:
            '''The type of policy.

            Specify ``EBS_SNAPSHOT_MANAGEMENT`` to create a lifecycle policy that manages the lifecycle of Amazon EBS snapshots. Specify ``IMAGE_MANAGEMENT`` to create a lifecycle policy that manages the lifecycle of EBS-backed AMIs. Specify ``EVENT_BASED_POLICY`` to create an event-based policy that performs specific actions when a defined event occurs in your AWS account .

            The default is ``EBS_SNAPSHOT_MANAGEMENT`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-policytype
            '''
            result = self._values.get("policy_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_locations(self) -> typing.Optional[typing.List[builtins.str]]:
            '''*[Custom snapshot and AMI policies only]* The location of the resources to backup.

            If the source resources are located in an AWS Region , specify ``CLOUD`` . If the source resources are located on an Outpost in your account, specify ``OUTPOST`` .

            If you specify ``OUTPOST`` , Amazon Data Lifecycle Manager backs up all resources of the specified type with matching target tags across all of the Outposts in your account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-resourcelocations
            '''
            result = self._values.get("resource_locations")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def resource_type(self) -> typing.Optional[builtins.str]:
            '''*[Default policies only]* Specify the type of default policy to create.

            - To create a default policy for EBS snapshots, that creates snapshots of all volumes in the Region that do not have recent backups, specify ``VOLUME`` .
            - To create a default policy for EBS-backed AMIs, that creates EBS-backed AMIs from all instances in the Region that do not have recent backups, specify ``INSTANCE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-resourcetype
            '''
            result = self._values.get("resource_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''*[Custom snapshot policies only]* The target resource type for snapshot and AMI lifecycle policies.

            Use ``VOLUME`` to create snapshots of individual volumes or use ``INSTANCE`` to create multi-volume snapshots from the volumes for an instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-resourcetypes
            '''
            result = self._values.get("resource_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def retain_interval(self) -> typing.Optional[jsii.Number]:
            '''*[Default policies only]* Specifies how long the policy should retain snapshots or AMIs before deleting them.

            The retention period can range from 2 to 14 days, but it must be greater than the creation frequency to ensure that the policy retains at least 1 snapshot or AMI at any given time. If you do not specify a value, the default is 7.

            Default: 7

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-retaininterval
            '''
            result = self._values.get("retain_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def schedules(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ScheduleProperty"]]]]:
            '''*[Custom snapshot and AMI policies only]* The schedules of policy-defined actions for snapshot and AMI lifecycle policies.

            A policy can have up to four schedules—one mandatory schedule and up to three optional schedules.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-schedules
            '''
            result = self._values.get("schedules")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ScheduleProperty"]]]], result)

        @builtins.property
        def target_tags(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]]:
            '''*[Custom snapshot and AMI policies only]* The single tag that identifies targeted resources for this policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-policydetails.html#cfn-dlm-lifecyclepolicy-policydetails-targettags
            '''
            result = self._values.get("target_tags")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PolicyDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dlm.CfnLifecyclePolicy.RetainRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "count": "count",
            "interval": "interval",
            "interval_unit": "intervalUnit",
        },
    )
    class RetainRuleProperty:
        def __init__(
            self,
            *,
            count: typing.Optional[jsii.Number] = None,
            interval: typing.Optional[jsii.Number] = None,
            interval_unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''*[Custom snapshot and AMI policies only]* Specifies a retention rule for snapshots created by snapshot policies, or for AMIs created by AMI policies.

            .. epigraph::

               For snapshot policies that have an `ArchiveRule <https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRule.html>`_ , this retention rule applies to standard tier retention. When the retention threshold is met, snapshots are moved from the standard to the archive tier.

               For snapshot policies that do not have an *ArchiveRule* , snapshots are permanently deleted when this retention threshold is met.

            You can retain snapshots based on either a count or a time interval.

            - *Count-based retention*

            You must specify *Count* . If you specify an `ArchiveRule <https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRule.html>`_ for the schedule, then you can specify a retention count of ``0`` to archive snapshots immediately after creation. If you specify a `FastRestoreRule <https://docs.aws.amazon.com/dlm/latest/APIReference/API_FastRestoreRule.html>`_ , `ShareRule <https://docs.aws.amazon.com/dlm/latest/APIReference/API_ShareRule.html>`_ , or a `CrossRegionCopyRule <https://docs.aws.amazon.com/dlm/latest/APIReference/API_CrossRegionCopyRule.html>`_ , then you must specify a retention count of ``1`` or more.

            - *Age-based retention*

            You must specify *Interval* and *IntervalUnit* . If you specify an `ArchiveRule <https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRule.html>`_ for the schedule, then you can specify a retention interval of ``0`` days to archive snapshots immediately after creation. If you specify a `FastRestoreRule <https://docs.aws.amazon.com/dlm/latest/APIReference/API_FastRestoreRule.html>`_ , `ShareRule <https://docs.aws.amazon.com/dlm/latest/APIReference/API_ShareRule.html>`_ , or a `CrossRegionCopyRule <https://docs.aws.amazon.com/dlm/latest/APIReference/API_CrossRegionCopyRule.html>`_ , then you must specify a retention interval of ``1`` day or more.

            :param count: The number of snapshots to retain for each volume, up to a maximum of 1000. For example if you want to retain a maximum of three snapshots, specify ``3`` . When the fourth snapshot is created, the oldest retained snapshot is deleted, or it is moved to the archive tier if you have specified an `ArchiveRule <https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRule.html>`_ .
            :param interval: The amount of time to retain each snapshot. The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.
            :param interval_unit: The unit of time for time-based retention. For example, to retain snapshots for 3 months, specify ``Interval=3`` and ``IntervalUnit=MONTHS`` . Once the snapshot has been retained for 3 months, it is deleted, or it is moved to the archive tier if you have specified an `ArchiveRule <https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRule.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retainrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dlm as dlm
                
                retain_rule_property = dlm.CfnLifecyclePolicy.RetainRuleProperty(
                    count=123,
                    interval=123,
                    interval_unit="intervalUnit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d63890f98bdab663b74392c501d0b6d353daba75e373aec4c47e220cb0c317ea)
                check_type(argname="argument count", value=count, expected_type=type_hints["count"])
                check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
                check_type(argname="argument interval_unit", value=interval_unit, expected_type=type_hints["interval_unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if count is not None:
                self._values["count"] = count
            if interval is not None:
                self._values["interval"] = interval
            if interval_unit is not None:
                self._values["interval_unit"] = interval_unit

        @builtins.property
        def count(self) -> typing.Optional[jsii.Number]:
            '''The number of snapshots to retain for each volume, up to a maximum of 1000.

            For example if you want to retain a maximum of three snapshots, specify ``3`` . When the fourth snapshot is created, the oldest retained snapshot is deleted, or it is moved to the archive tier if you have specified an `ArchiveRule <https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRule.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retainrule.html#cfn-dlm-lifecyclepolicy-retainrule-count
            '''
            result = self._values.get("count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def interval(self) -> typing.Optional[jsii.Number]:
            '''The amount of time to retain each snapshot.

            The maximum is 100 years. This is equivalent to 1200 months, 5200 weeks, or 36500 days.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retainrule.html#cfn-dlm-lifecyclepolicy-retainrule-interval
            '''
            result = self._values.get("interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def interval_unit(self) -> typing.Optional[builtins.str]:
            '''The unit of time for time-based retention.

            For example, to retain snapshots for 3 months, specify ``Interval=3`` and ``IntervalUnit=MONTHS`` . Once the snapshot has been retained for 3 months, it is deleted, or it is moved to the archive tier if you have specified an `ArchiveRule <https://docs.aws.amazon.com/dlm/latest/APIReference/API_ArchiveRule.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retainrule.html#cfn-dlm-lifecyclepolicy-retainrule-intervalunit
            '''
            result = self._values.get("interval_unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RetainRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dlm.CfnLifecyclePolicy.RetentionArchiveTierProperty",
        jsii_struct_bases=[],
        name_mapping={
            "count": "count",
            "interval": "interval",
            "interval_unit": "intervalUnit",
        },
    )
    class RetentionArchiveTierProperty:
        def __init__(
            self,
            *,
            count: typing.Optional[jsii.Number] = None,
            interval: typing.Optional[jsii.Number] = None,
            interval_unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''*[Custom snapshot policies only]* Describes the retention rule for archived snapshots.

            Once the archive retention threshold is met, the snapshots are permanently deleted from the archive tier.
            .. epigraph::

               The archive retention rule must retain snapshots in the archive tier for a minimum of 90 days.

            For *count-based schedules* , you must specify *Count* . For *age-based schedules* , you must specify *Interval* and *IntervalUnit* .

            For more information about using snapshot archiving, see `Considerations for snapshot lifecycle policies <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-ami-policy.html#dlm-archive>`_ .

            :param count: The maximum number of snapshots to retain in the archive storage tier for each volume. The count must ensure that each snapshot remains in the archive tier for at least 90 days. For example, if the schedule creates snapshots every 30 days, you must specify a count of 3 or more to ensure that each snapshot is archived for at least 90 days.
            :param interval: Specifies the period of time to retain snapshots in the archive tier. After this period expires, the snapshot is permanently deleted.
            :param interval_unit: The unit of time in which to measure the *Interval* . For example, to retain a snapshots in the archive tier for 6 months, specify ``Interval=6`` and ``IntervalUnit=MONTHS`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retentionarchivetier.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dlm as dlm
                
                retention_archive_tier_property = dlm.CfnLifecyclePolicy.RetentionArchiveTierProperty(
                    count=123,
                    interval=123,
                    interval_unit="intervalUnit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__07f178891476deda83ce4ebdda6f02f0dff8b84d1330e2f6bf88d74f1e513ffa)
                check_type(argname="argument count", value=count, expected_type=type_hints["count"])
                check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
                check_type(argname="argument interval_unit", value=interval_unit, expected_type=type_hints["interval_unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if count is not None:
                self._values["count"] = count
            if interval is not None:
                self._values["interval"] = interval
            if interval_unit is not None:
                self._values["interval_unit"] = interval_unit

        @builtins.property
        def count(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of snapshots to retain in the archive storage tier for each volume.

            The count must ensure that each snapshot remains in the archive tier for at least 90 days. For example, if the schedule creates snapshots every 30 days, you must specify a count of 3 or more to ensure that each snapshot is archived for at least 90 days.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retentionarchivetier.html#cfn-dlm-lifecyclepolicy-retentionarchivetier-count
            '''
            result = self._values.get("count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def interval(self) -> typing.Optional[jsii.Number]:
            '''Specifies the period of time to retain snapshots in the archive tier.

            After this period expires, the snapshot is permanently deleted.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retentionarchivetier.html#cfn-dlm-lifecyclepolicy-retentionarchivetier-interval
            '''
            result = self._values.get("interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def interval_unit(self) -> typing.Optional[builtins.str]:
            '''The unit of time in which to measure the *Interval* .

            For example, to retain a snapshots in the archive tier for 6 months, specify ``Interval=6`` and ``IntervalUnit=MONTHS`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-retentionarchivetier.html#cfn-dlm-lifecyclepolicy-retentionarchivetier-intervalunit
            '''
            result = self._values.get("interval_unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RetentionArchiveTierProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dlm.CfnLifecyclePolicy.ScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "archive_rule": "archiveRule",
            "copy_tags": "copyTags",
            "create_rule": "createRule",
            "cross_region_copy_rules": "crossRegionCopyRules",
            "deprecate_rule": "deprecateRule",
            "fast_restore_rule": "fastRestoreRule",
            "name": "name",
            "retain_rule": "retainRule",
            "share_rules": "shareRules",
            "tags_to_add": "tagsToAdd",
            "variable_tags": "variableTags",
        },
    )
    class ScheduleProperty:
        def __init__(
            self,
            *,
            archive_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.ArchiveRuleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            copy_tags: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            create_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.CreateRuleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cross_region_copy_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.CrossRegionCopyRuleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            deprecate_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.DeprecateRuleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            fast_restore_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.FastRestoreRuleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            name: typing.Optional[builtins.str] = None,
            retain_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.RetainRuleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            share_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.ShareRuleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            tags_to_add: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
            variable_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''*[Custom snapshot and AMI policies only]* Specifies a schedule for a snapshot or AMI lifecycle policy.

            :param archive_rule: *[Custom snapshot policies that target volumes only]* The snapshot archiving rule for the schedule. When you specify an archiving rule, snapshots are automatically moved from the standard tier to the archive tier once the schedule's retention threshold is met. Snapshots are then retained in the archive tier for the archive retention period that you specify. For more information about using snapshot archiving, see `Considerations for snapshot lifecycle policies <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-ami-policy.html#dlm-archive>`_ .
            :param copy_tags: Copy all user-defined tags on a source volume to snapshots of the volume created by this policy.
            :param create_rule: The creation rule.
            :param cross_region_copy_rules: Specifies a rule for copying snapshots or AMIs across regions. .. epigraph:: You can't specify cross-Region copy rules for policies that create snapshots on an Outpost. If the policy creates snapshots in a Region, then snapshots can be copied to up to three Regions or Outposts.
            :param deprecate_rule: *[Custom AMI policies only]* The AMI deprecation rule for the schedule.
            :param fast_restore_rule: *[Custom snapshot policies only]* The rule for enabling fast snapshot restore.
            :param name: The name of the schedule.
            :param retain_rule: The retention rule for snapshots or AMIs created by the policy.
            :param share_rules: *[Custom snapshot policies only]* The rule for sharing snapshots with other AWS accounts .
            :param tags_to_add: The tags to apply to policy-created resources. These user-defined tags are in addition to the AWS -added lifecycle tags.
            :param variable_tags: *[AMI policies and snapshot policies that target instances only]* A collection of key/value pairs with values determined dynamically when the policy is executed. Keys may be any valid Amazon EC2 tag key. Values must be in one of the two following formats: ``$(instance-id)`` or ``$(timestamp)`` . Variable tags are only valid for EBS Snapshot Management – Instance policies.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dlm as dlm
                
                schedule_property = dlm.CfnLifecyclePolicy.ScheduleProperty(
                    archive_rule=dlm.CfnLifecyclePolicy.ArchiveRuleProperty(
                        retain_rule=dlm.CfnLifecyclePolicy.ArchiveRetainRuleProperty(
                            retention_archive_tier=dlm.CfnLifecyclePolicy.RetentionArchiveTierProperty(
                                count=123,
                                interval=123,
                                interval_unit="intervalUnit"
                            )
                        )
                    ),
                    copy_tags=False,
                    create_rule=dlm.CfnLifecyclePolicy.CreateRuleProperty(
                        cron_expression="cronExpression",
                        interval=123,
                        interval_unit="intervalUnit",
                        location="location",
                        scripts=[dlm.CfnLifecyclePolicy.ScriptProperty(
                            execute_operation_on_script_failure=False,
                            execution_handler="executionHandler",
                            execution_handler_service="executionHandlerService",
                            execution_timeout=123,
                            maximum_retry_count=123,
                            stages=["stages"]
                        )],
                        times=["times"]
                    ),
                    cross_region_copy_rules=[dlm.CfnLifecyclePolicy.CrossRegionCopyRuleProperty(
                        encrypted=False,
                
                        # the properties below are optional
                        cmk_arn="cmkArn",
                        copy_tags=False,
                        deprecate_rule=dlm.CfnLifecyclePolicy.CrossRegionCopyDeprecateRuleProperty(
                            interval=123,
                            interval_unit="intervalUnit"
                        ),
                        retain_rule=dlm.CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty(
                            interval=123,
                            interval_unit="intervalUnit"
                        ),
                        target="target",
                        target_region="targetRegion"
                    )],
                    deprecate_rule=dlm.CfnLifecyclePolicy.DeprecateRuleProperty(
                        count=123,
                        interval=123,
                        interval_unit="intervalUnit"
                    ),
                    fast_restore_rule=dlm.CfnLifecyclePolicy.FastRestoreRuleProperty(
                        availability_zones=["availabilityZones"],
                        count=123,
                        interval=123,
                        interval_unit="intervalUnit"
                    ),
                    name="name",
                    retain_rule=dlm.CfnLifecyclePolicy.RetainRuleProperty(
                        count=123,
                        interval=123,
                        interval_unit="intervalUnit"
                    ),
                    share_rules=[dlm.CfnLifecyclePolicy.ShareRuleProperty(
                        target_accounts=["targetAccounts"],
                        unshare_interval=123,
                        unshare_interval_unit="unshareIntervalUnit"
                    )],
                    tags_to_add=[CfnTag(
                        key="key",
                        value="value"
                    )],
                    variable_tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d9b4afd18ef7a7c10ab5cb55653ba53eff1da7bab75afaf21bdb01bb2d9841c5)
                check_type(argname="argument archive_rule", value=archive_rule, expected_type=type_hints["archive_rule"])
                check_type(argname="argument copy_tags", value=copy_tags, expected_type=type_hints["copy_tags"])
                check_type(argname="argument create_rule", value=create_rule, expected_type=type_hints["create_rule"])
                check_type(argname="argument cross_region_copy_rules", value=cross_region_copy_rules, expected_type=type_hints["cross_region_copy_rules"])
                check_type(argname="argument deprecate_rule", value=deprecate_rule, expected_type=type_hints["deprecate_rule"])
                check_type(argname="argument fast_restore_rule", value=fast_restore_rule, expected_type=type_hints["fast_restore_rule"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument retain_rule", value=retain_rule, expected_type=type_hints["retain_rule"])
                check_type(argname="argument share_rules", value=share_rules, expected_type=type_hints["share_rules"])
                check_type(argname="argument tags_to_add", value=tags_to_add, expected_type=type_hints["tags_to_add"])
                check_type(argname="argument variable_tags", value=variable_tags, expected_type=type_hints["variable_tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if archive_rule is not None:
                self._values["archive_rule"] = archive_rule
            if copy_tags is not None:
                self._values["copy_tags"] = copy_tags
            if create_rule is not None:
                self._values["create_rule"] = create_rule
            if cross_region_copy_rules is not None:
                self._values["cross_region_copy_rules"] = cross_region_copy_rules
            if deprecate_rule is not None:
                self._values["deprecate_rule"] = deprecate_rule
            if fast_restore_rule is not None:
                self._values["fast_restore_rule"] = fast_restore_rule
            if name is not None:
                self._values["name"] = name
            if retain_rule is not None:
                self._values["retain_rule"] = retain_rule
            if share_rules is not None:
                self._values["share_rules"] = share_rules
            if tags_to_add is not None:
                self._values["tags_to_add"] = tags_to_add
            if variable_tags is not None:
                self._values["variable_tags"] = variable_tags

        @builtins.property
        def archive_rule(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ArchiveRuleProperty"]]:
            '''*[Custom snapshot policies that target volumes only]* The snapshot archiving rule for the schedule.

            When you specify an archiving rule, snapshots are automatically moved from the standard tier to the archive tier once the schedule's retention threshold is met. Snapshots are then retained in the archive tier for the archive retention period that you specify.

            For more information about using snapshot archiving, see `Considerations for snapshot lifecycle policies <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-ami-policy.html#dlm-archive>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-archiverule
            '''
            result = self._values.get("archive_rule")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ArchiveRuleProperty"]], result)

        @builtins.property
        def copy_tags(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Copy all user-defined tags on a source volume to snapshots of the volume created by this policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-copytags
            '''
            result = self._values.get("copy_tags")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def create_rule(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.CreateRuleProperty"]]:
            '''The creation rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-createrule
            '''
            result = self._values.get("create_rule")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.CreateRuleProperty"]], result)

        @builtins.property
        def cross_region_copy_rules(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.CrossRegionCopyRuleProperty"]]]]:
            '''Specifies a rule for copying snapshots or AMIs across regions.

            .. epigraph::

               You can't specify cross-Region copy rules for policies that create snapshots on an Outpost. If the policy creates snapshots in a Region, then snapshots can be copied to up to three Regions or Outposts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-crossregioncopyrules
            '''
            result = self._values.get("cross_region_copy_rules")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.CrossRegionCopyRuleProperty"]]]], result)

        @builtins.property
        def deprecate_rule(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.DeprecateRuleProperty"]]:
            '''*[Custom AMI policies only]* The AMI deprecation rule for the schedule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-deprecaterule
            '''
            result = self._values.get("deprecate_rule")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.DeprecateRuleProperty"]], result)

        @builtins.property
        def fast_restore_rule(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.FastRestoreRuleProperty"]]:
            '''*[Custom snapshot policies only]* The rule for enabling fast snapshot restore.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-fastrestorerule
            '''
            result = self._values.get("fast_restore_rule")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.FastRestoreRuleProperty"]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the schedule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def retain_rule(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.RetainRuleProperty"]]:
            '''The retention rule for snapshots or AMIs created by the policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-retainrule
            '''
            result = self._values.get("retain_rule")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.RetainRuleProperty"]], result)

        @builtins.property
        def share_rules(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ShareRuleProperty"]]]]:
            '''*[Custom snapshot policies only]* The rule for sharing snapshots with other AWS accounts .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-sharerules
            '''
            result = self._values.get("share_rules")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ShareRuleProperty"]]]], result)

        @builtins.property
        def tags_to_add(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]]:
            '''The tags to apply to policy-created resources.

            These user-defined tags are in addition to the AWS -added lifecycle tags.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-tagstoadd
            '''
            result = self._values.get("tags_to_add")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]], result)

        @builtins.property
        def variable_tags(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]]:
            '''*[AMI policies and snapshot policies that target instances only]* A collection of key/value pairs with values determined dynamically when the policy is executed.

            Keys may be any valid Amazon EC2 tag key. Values must be in one of the two following formats: ``$(instance-id)`` or ``$(timestamp)`` . Variable tags are only valid for EBS Snapshot Management – Instance policies.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-schedule.html#cfn-dlm-lifecyclepolicy-schedule-variabletags
            '''
            result = self._values.get("variable_tags")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dlm.CfnLifecyclePolicy.ScriptProperty",
        jsii_struct_bases=[],
        name_mapping={
            "execute_operation_on_script_failure": "executeOperationOnScriptFailure",
            "execution_handler": "executionHandler",
            "execution_handler_service": "executionHandlerService",
            "execution_timeout": "executionTimeout",
            "maximum_retry_count": "maximumRetryCount",
            "stages": "stages",
        },
    )
    class ScriptProperty:
        def __init__(
            self,
            *,
            execute_operation_on_script_failure: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            execution_handler: typing.Optional[builtins.str] = None,
            execution_handler_service: typing.Optional[builtins.str] = None,
            execution_timeout: typing.Optional[jsii.Number] = None,
            maximum_retry_count: typing.Optional[jsii.Number] = None,
            stages: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''*[Custom snapshot policies that target instances only]* Information about pre and/or post scripts for a snapshot lifecycle policy that targets instances.

            For more information, see `Automating application-consistent snapshots with pre and post scripts <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/automate-app-consistent-backups.html>`_ .

            :param execute_operation_on_script_failure: Indicates whether Amazon Data Lifecycle Manager should default to crash-consistent snapshots if the pre script fails. - To default to crash consistent snapshot if the pre script fails, specify ``true`` . - To skip the instance for snapshot creation if the pre script fails, specify ``false`` . This parameter is supported only if you run a pre script. If you run a post script only, omit this parameter. Default: true
            :param execution_handler: The SSM document that includes the pre and/or post scripts to run. - If you are automating VSS backups, specify ``AWS_VSS_BACKUP`` . In this case, Amazon Data Lifecycle Manager automatically uses the ``AWSEC2-CreateVssSnapshot`` SSM document. - If you are automating application-consistent snapshots for SAP HANA workloads, specify ``AWSSystemsManagerSAP-CreateDLMSnapshotForSAPHANA`` . - If you are using a custom SSM document that you own, specify either the name or ARN of the SSM document. If you are using a custom SSM document that is shared with you, specify the ARN of the SSM document.
            :param execution_handler_service: Indicates the service used to execute the pre and/or post scripts. - If you are using custom SSM documents or automating application-consistent snapshots of SAP HANA workloads, specify ``AWS_SYSTEMS_MANAGER`` . - If you are automating VSS Backups, omit this parameter. Default: AWS_SYSTEMS_MANAGER
            :param execution_timeout: Specifies a timeout period, in seconds, after which Amazon Data Lifecycle Manager fails the script run attempt if it has not completed. If a script does not complete within its timeout period, Amazon Data Lifecycle Manager fails the attempt. The timeout period applies to the pre and post scripts individually. If you are automating VSS Backups, omit this parameter. Default: 10
            :param maximum_retry_count: Specifies the number of times Amazon Data Lifecycle Manager should retry scripts that fail. - If the pre script fails, Amazon Data Lifecycle Manager retries the entire snapshot creation process, including running the pre and post scripts. - If the post script fails, Amazon Data Lifecycle Manager retries the post script only; in this case, the pre script will have completed and the snapshot might have been created. If you do not want Amazon Data Lifecycle Manager to retry failed scripts, specify ``0`` . Default: 0
            :param stages: Indicate which scripts Amazon Data Lifecycle Manager should run on target instances. Pre scripts run before Amazon Data Lifecycle Manager initiates snapshot creation. Post scripts run after Amazon Data Lifecycle Manager initiates snapshot creation. - To run a pre script only, specify ``PRE`` . In this case, Amazon Data Lifecycle Manager calls the SSM document with the ``pre-script`` parameter before initiating snapshot creation. - To run a post script only, specify ``POST`` . In this case, Amazon Data Lifecycle Manager calls the SSM document with the ``post-script`` parameter after initiating snapshot creation. - To run both pre and post scripts, specify both ``PRE`` and ``POST`` . In this case, Amazon Data Lifecycle Manager calls the SSM document with the ``pre-script`` parameter before initiating snapshot creation, and then it calls the SSM document again with the ``post-script`` parameter after initiating snapshot creation. If you are automating VSS Backups, omit this parameter. Default: PRE and POST

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-script.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dlm as dlm
                
                script_property = dlm.CfnLifecyclePolicy.ScriptProperty(
                    execute_operation_on_script_failure=False,
                    execution_handler="executionHandler",
                    execution_handler_service="executionHandlerService",
                    execution_timeout=123,
                    maximum_retry_count=123,
                    stages=["stages"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ae035efa2ba94c476212d1e54c4004eec95481ef5b9123ad74f1ec61e8c3921c)
                check_type(argname="argument execute_operation_on_script_failure", value=execute_operation_on_script_failure, expected_type=type_hints["execute_operation_on_script_failure"])
                check_type(argname="argument execution_handler", value=execution_handler, expected_type=type_hints["execution_handler"])
                check_type(argname="argument execution_handler_service", value=execution_handler_service, expected_type=type_hints["execution_handler_service"])
                check_type(argname="argument execution_timeout", value=execution_timeout, expected_type=type_hints["execution_timeout"])
                check_type(argname="argument maximum_retry_count", value=maximum_retry_count, expected_type=type_hints["maximum_retry_count"])
                check_type(argname="argument stages", value=stages, expected_type=type_hints["stages"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if execute_operation_on_script_failure is not None:
                self._values["execute_operation_on_script_failure"] = execute_operation_on_script_failure
            if execution_handler is not None:
                self._values["execution_handler"] = execution_handler
            if execution_handler_service is not None:
                self._values["execution_handler_service"] = execution_handler_service
            if execution_timeout is not None:
                self._values["execution_timeout"] = execution_timeout
            if maximum_retry_count is not None:
                self._values["maximum_retry_count"] = maximum_retry_count
            if stages is not None:
                self._values["stages"] = stages

        @builtins.property
        def execute_operation_on_script_failure(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether Amazon Data Lifecycle Manager should default to crash-consistent snapshots if the pre script fails.

            - To default to crash consistent snapshot if the pre script fails, specify ``true`` .
            - To skip the instance for snapshot creation if the pre script fails, specify ``false`` .

            This parameter is supported only if you run a pre script. If you run a post script only, omit this parameter.

            Default: true

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-script.html#cfn-dlm-lifecyclepolicy-script-executeoperationonscriptfailure
            '''
            result = self._values.get("execute_operation_on_script_failure")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def execution_handler(self) -> typing.Optional[builtins.str]:
            '''The SSM document that includes the pre and/or post scripts to run.

            - If you are automating VSS backups, specify ``AWS_VSS_BACKUP`` . In this case, Amazon Data Lifecycle Manager automatically uses the ``AWSEC2-CreateVssSnapshot`` SSM document.
            - If you are automating application-consistent snapshots for SAP HANA workloads, specify ``AWSSystemsManagerSAP-CreateDLMSnapshotForSAPHANA`` .
            - If you are using a custom SSM document that you own, specify either the name or ARN of the SSM document. If you are using a custom SSM document that is shared with you, specify the ARN of the SSM document.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-script.html#cfn-dlm-lifecyclepolicy-script-executionhandler
            '''
            result = self._values.get("execution_handler")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def execution_handler_service(self) -> typing.Optional[builtins.str]:
            '''Indicates the service used to execute the pre and/or post scripts.

            - If you are using custom SSM documents or automating application-consistent snapshots of SAP HANA workloads, specify ``AWS_SYSTEMS_MANAGER`` .
            - If you are automating VSS Backups, omit this parameter.

            Default: AWS_SYSTEMS_MANAGER

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-script.html#cfn-dlm-lifecyclepolicy-script-executionhandlerservice
            '''
            result = self._values.get("execution_handler_service")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def execution_timeout(self) -> typing.Optional[jsii.Number]:
            '''Specifies a timeout period, in seconds, after which Amazon Data Lifecycle Manager fails the script run attempt if it has not completed.

            If a script does not complete within its timeout period, Amazon Data Lifecycle Manager fails the attempt. The timeout period applies to the pre and post scripts individually.

            If you are automating VSS Backups, omit this parameter.

            Default: 10

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-script.html#cfn-dlm-lifecyclepolicy-script-executiontimeout
            '''
            result = self._values.get("execution_timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def maximum_retry_count(self) -> typing.Optional[jsii.Number]:
            '''Specifies the number of times Amazon Data Lifecycle Manager should retry scripts that fail.

            - If the pre script fails, Amazon Data Lifecycle Manager retries the entire snapshot creation process, including running the pre and post scripts.
            - If the post script fails, Amazon Data Lifecycle Manager retries the post script only; in this case, the pre script will have completed and the snapshot might have been created.

            If you do not want Amazon Data Lifecycle Manager to retry failed scripts, specify ``0`` .

            Default: 0

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-script.html#cfn-dlm-lifecyclepolicy-script-maximumretrycount
            '''
            result = self._values.get("maximum_retry_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def stages(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Indicate which scripts Amazon Data Lifecycle Manager should run on target instances.

            Pre scripts run before Amazon Data Lifecycle Manager initiates snapshot creation. Post scripts run after Amazon Data Lifecycle Manager initiates snapshot creation.

            - To run a pre script only, specify ``PRE`` . In this case, Amazon Data Lifecycle Manager calls the SSM document with the ``pre-script`` parameter before initiating snapshot creation.
            - To run a post script only, specify ``POST`` . In this case, Amazon Data Lifecycle Manager calls the SSM document with the ``post-script`` parameter after initiating snapshot creation.
            - To run both pre and post scripts, specify both ``PRE`` and ``POST`` . In this case, Amazon Data Lifecycle Manager calls the SSM document with the ``pre-script`` parameter before initiating snapshot creation, and then it calls the SSM document again with the ``post-script`` parameter after initiating snapshot creation.

            If you are automating VSS Backups, omit this parameter.

            Default: PRE and POST

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-script.html#cfn-dlm-lifecyclepolicy-script-stages
            '''
            result = self._values.get("stages")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScriptProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dlm.CfnLifecyclePolicy.ShareRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "target_accounts": "targetAccounts",
            "unshare_interval": "unshareInterval",
            "unshare_interval_unit": "unshareIntervalUnit",
        },
    )
    class ShareRuleProperty:
        def __init__(
            self,
            *,
            target_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
            unshare_interval: typing.Optional[jsii.Number] = None,
            unshare_interval_unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''*[Custom snapshot policies only]* Specifies a rule for sharing snapshots across AWS accounts .

            :param target_accounts: The IDs of the AWS accounts with which to share the snapshots.
            :param unshare_interval: The period after which snapshots that are shared with other AWS accounts are automatically unshared.
            :param unshare_interval_unit: The unit of time for the automatic unsharing interval.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-sharerule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dlm as dlm
                
                share_rule_property = dlm.CfnLifecyclePolicy.ShareRuleProperty(
                    target_accounts=["targetAccounts"],
                    unshare_interval=123,
                    unshare_interval_unit="unshareIntervalUnit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__17018411aa866dc818102e8981736b177dd1a23646009ebb8d8cbe6a34da52bf)
                check_type(argname="argument target_accounts", value=target_accounts, expected_type=type_hints["target_accounts"])
                check_type(argname="argument unshare_interval", value=unshare_interval, expected_type=type_hints["unshare_interval"])
                check_type(argname="argument unshare_interval_unit", value=unshare_interval_unit, expected_type=type_hints["unshare_interval_unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if target_accounts is not None:
                self._values["target_accounts"] = target_accounts
            if unshare_interval is not None:
                self._values["unshare_interval"] = unshare_interval
            if unshare_interval_unit is not None:
                self._values["unshare_interval_unit"] = unshare_interval_unit

        @builtins.property
        def target_accounts(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The IDs of the AWS accounts with which to share the snapshots.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-sharerule.html#cfn-dlm-lifecyclepolicy-sharerule-targetaccounts
            '''
            result = self._values.get("target_accounts")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def unshare_interval(self) -> typing.Optional[jsii.Number]:
            '''The period after which snapshots that are shared with other AWS accounts are automatically unshared.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-sharerule.html#cfn-dlm-lifecyclepolicy-sharerule-unshareinterval
            '''
            result = self._values.get("unshare_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def unshare_interval_unit(self) -> typing.Optional[builtins.str]:
            '''The unit of time for the automatic unsharing interval.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dlm-lifecyclepolicy-sharerule.html#cfn-dlm-lifecyclepolicy-sharerule-unshareintervalunit
            '''
            result = self._values.get("unshare_interval_unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ShareRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_dlm.CfnLifecyclePolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "copy_tags": "copyTags",
        "create_interval": "createInterval",
        "cross_region_copy_targets": "crossRegionCopyTargets",
        "default_policy": "defaultPolicy",
        "description": "description",
        "exclusions": "exclusions",
        "execution_role_arn": "executionRoleArn",
        "extend_deletion": "extendDeletion",
        "policy_details": "policyDetails",
        "retain_interval": "retainInterval",
        "state": "state",
        "tags": "tags",
    },
)
class CfnLifecyclePolicyProps:
    def __init__(
        self,
        *,
        copy_tags: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        create_interval: typing.Optional[jsii.Number] = None,
        cross_region_copy_targets: typing.Any = None,
        default_policy: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        exclusions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.ExclusionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        extend_deletion: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        policy_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.PolicyDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        retain_interval: typing.Optional[jsii.Number] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLifecyclePolicy``.

        :param copy_tags: *[Default policies only]* Indicates whether the policy should copy tags from the source resource to the snapshot or AMI. If you do not specify a value, the default is ``false`` . Default: false
        :param create_interval: *[Default policies only]* Specifies how often the policy should run and create snapshots or AMIs. The creation frequency can range from 1 to 7 days. If you do not specify a value, the default is 1. Default: 1
        :param cross_region_copy_targets: *[Default policies only]* Specifies destination Regions for snapshot or AMI copies. You can specify up to 3 destination Regions. If you do not want to create cross-Region copies, omit this parameter.
        :param default_policy: *[Default policies only]* Specify the type of default policy to create. - To create a default policy for EBS snapshots, that creates snapshots of all volumes in the Region that do not have recent backups, specify ``VOLUME`` . - To create a default policy for EBS-backed AMIs, that creates EBS-backed AMIs from all instances in the Region that do not have recent backups, specify ``INSTANCE`` .
        :param description: A description of the lifecycle policy. The characters ^[0-9A-Za-z _-]+$ are supported.
        :param exclusions: *[Default policies only]* Specifies exclusion parameters for volumes or instances for which you do not want to create snapshots or AMIs. The policy will not create snapshots or AMIs for target resources that match any of the specified exclusion parameters.
        :param execution_role_arn: The Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the lifecycle policy.
        :param extend_deletion: *[Default policies only]* Defines the snapshot or AMI retention behavior for the policy if the source volume or instance is deleted, or if the policy enters the error, disabled, or deleted state. By default ( *ExtendDeletion=false* ): - If a source resource is deleted, Amazon Data Lifecycle Manager will continue to delete previously created snapshots or AMIs, up to but not including the last one, based on the specified retention period. If you want Amazon Data Lifecycle Manager to delete all snapshots or AMIs, including the last one, specify ``true`` . - If a policy enters the error, disabled, or deleted state, Amazon Data Lifecycle Manager stops deleting snapshots and AMIs. If you want Amazon Data Lifecycle Manager to continue deleting snapshots or AMIs, including the last one, if the policy enters one of these states, specify ``true`` . If you enable extended deletion ( *ExtendDeletion=true* ), you override both default behaviors simultaneously. If you do not specify a value, the default is ``false`` . Default: false
        :param policy_details: The configuration details of the lifecycle policy. .. epigraph:: If you create a default policy, you can specify the request parameters either in the request body, or in the PolicyDetails request structure, but not both.
        :param retain_interval: *[Default policies only]* Specifies how long the policy should retain snapshots or AMIs before deleting them. The retention period can range from 2 to 14 days, but it must be greater than the creation frequency to ensure that the policy retains at least 1 snapshot or AMI at any given time. If you do not specify a value, the default is 7. Default: 7
        :param state: The activation state of the lifecycle policy.
        :param tags: The tags to apply to the lifecycle policy during creation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_dlm as dlm
            
            # cross_region_copy_targets: Any
            # exclude_tags: Any
            # exclude_volume_types: Any
            
            cfn_lifecycle_policy_props = dlm.CfnLifecyclePolicyProps(
                copy_tags=False,
                create_interval=123,
                cross_region_copy_targets=cross_region_copy_targets,
                default_policy="defaultPolicy",
                description="description",
                exclusions=dlm.CfnLifecyclePolicy.ExclusionsProperty(
                    exclude_boot_volumes=False,
                    exclude_tags=exclude_tags,
                    exclude_volume_types=exclude_volume_types
                ),
                execution_role_arn="executionRoleArn",
                extend_deletion=False,
                policy_details=dlm.CfnLifecyclePolicy.PolicyDetailsProperty(
                    actions=[dlm.CfnLifecyclePolicy.ActionProperty(
                        cross_region_copy=[dlm.CfnLifecyclePolicy.CrossRegionCopyActionProperty(
                            encryption_configuration=dlm.CfnLifecyclePolicy.EncryptionConfigurationProperty(
                                encrypted=False,
            
                                # the properties below are optional
                                cmk_arn="cmkArn"
                            ),
                            target="target",
            
                            # the properties below are optional
                            retain_rule=dlm.CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty(
                                interval=123,
                                interval_unit="intervalUnit"
                            )
                        )],
                        name="name"
                    )],
                    copy_tags=False,
                    create_interval=123,
                    cross_region_copy_targets=cross_region_copy_targets,
                    event_source=dlm.CfnLifecyclePolicy.EventSourceProperty(
                        type="type",
            
                        # the properties below are optional
                        parameters=dlm.CfnLifecyclePolicy.EventParametersProperty(
                            event_type="eventType",
                            snapshot_owner=["snapshotOwner"],
            
                            # the properties below are optional
                            description_regex="descriptionRegex"
                        )
                    ),
                    exclusions=dlm.CfnLifecyclePolicy.ExclusionsProperty(
                        exclude_boot_volumes=False,
                        exclude_tags=exclude_tags,
                        exclude_volume_types=exclude_volume_types
                    ),
                    extend_deletion=False,
                    parameters=dlm.CfnLifecyclePolicy.ParametersProperty(
                        exclude_boot_volume=False,
                        exclude_data_volume_tags=[CfnTag(
                            key="key",
                            value="value"
                        )],
                        no_reboot=False
                    ),
                    policy_language="policyLanguage",
                    policy_type="policyType",
                    resource_locations=["resourceLocations"],
                    resource_type="resourceType",
                    resource_types=["resourceTypes"],
                    retain_interval=123,
                    schedules=[dlm.CfnLifecyclePolicy.ScheduleProperty(
                        archive_rule=dlm.CfnLifecyclePolicy.ArchiveRuleProperty(
                            retain_rule=dlm.CfnLifecyclePolicy.ArchiveRetainRuleProperty(
                                retention_archive_tier=dlm.CfnLifecyclePolicy.RetentionArchiveTierProperty(
                                    count=123,
                                    interval=123,
                                    interval_unit="intervalUnit"
                                )
                            )
                        ),
                        copy_tags=False,
                        create_rule=dlm.CfnLifecyclePolicy.CreateRuleProperty(
                            cron_expression="cronExpression",
                            interval=123,
                            interval_unit="intervalUnit",
                            location="location",
                            scripts=[dlm.CfnLifecyclePolicy.ScriptProperty(
                                execute_operation_on_script_failure=False,
                                execution_handler="executionHandler",
                                execution_handler_service="executionHandlerService",
                                execution_timeout=123,
                                maximum_retry_count=123,
                                stages=["stages"]
                            )],
                            times=["times"]
                        ),
                        cross_region_copy_rules=[dlm.CfnLifecyclePolicy.CrossRegionCopyRuleProperty(
                            encrypted=False,
            
                            # the properties below are optional
                            cmk_arn="cmkArn",
                            copy_tags=False,
                            deprecate_rule=dlm.CfnLifecyclePolicy.CrossRegionCopyDeprecateRuleProperty(
                                interval=123,
                                interval_unit="intervalUnit"
                            ),
                            retain_rule=dlm.CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty(
                                interval=123,
                                interval_unit="intervalUnit"
                            ),
                            target="target",
                            target_region="targetRegion"
                        )],
                        deprecate_rule=dlm.CfnLifecyclePolicy.DeprecateRuleProperty(
                            count=123,
                            interval=123,
                            interval_unit="intervalUnit"
                        ),
                        fast_restore_rule=dlm.CfnLifecyclePolicy.FastRestoreRuleProperty(
                            availability_zones=["availabilityZones"],
                            count=123,
                            interval=123,
                            interval_unit="intervalUnit"
                        ),
                        name="name",
                        retain_rule=dlm.CfnLifecyclePolicy.RetainRuleProperty(
                            count=123,
                            interval=123,
                            interval_unit="intervalUnit"
                        ),
                        share_rules=[dlm.CfnLifecyclePolicy.ShareRuleProperty(
                            target_accounts=["targetAccounts"],
                            unshare_interval=123,
                            unshare_interval_unit="unshareIntervalUnit"
                        )],
                        tags_to_add=[CfnTag(
                            key="key",
                            value="value"
                        )],
                        variable_tags=[CfnTag(
                            key="key",
                            value="value"
                        )]
                    )],
                    target_tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                ),
                retain_interval=123,
                state="state",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1414bd7f3e80e837a7b73bfb6d11bcc9e29191c357de74fe96a8efcfd1e89072)
            check_type(argname="argument copy_tags", value=copy_tags, expected_type=type_hints["copy_tags"])
            check_type(argname="argument create_interval", value=create_interval, expected_type=type_hints["create_interval"])
            check_type(argname="argument cross_region_copy_targets", value=cross_region_copy_targets, expected_type=type_hints["cross_region_copy_targets"])
            check_type(argname="argument default_policy", value=default_policy, expected_type=type_hints["default_policy"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument exclusions", value=exclusions, expected_type=type_hints["exclusions"])
            check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
            check_type(argname="argument extend_deletion", value=extend_deletion, expected_type=type_hints["extend_deletion"])
            check_type(argname="argument policy_details", value=policy_details, expected_type=type_hints["policy_details"])
            check_type(argname="argument retain_interval", value=retain_interval, expected_type=type_hints["retain_interval"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if copy_tags is not None:
            self._values["copy_tags"] = copy_tags
        if create_interval is not None:
            self._values["create_interval"] = create_interval
        if cross_region_copy_targets is not None:
            self._values["cross_region_copy_targets"] = cross_region_copy_targets
        if default_policy is not None:
            self._values["default_policy"] = default_policy
        if description is not None:
            self._values["description"] = description
        if exclusions is not None:
            self._values["exclusions"] = exclusions
        if execution_role_arn is not None:
            self._values["execution_role_arn"] = execution_role_arn
        if extend_deletion is not None:
            self._values["extend_deletion"] = extend_deletion
        if policy_details is not None:
            self._values["policy_details"] = policy_details
        if retain_interval is not None:
            self._values["retain_interval"] = retain_interval
        if state is not None:
            self._values["state"] = state
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def copy_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''*[Default policies only]* Indicates whether the policy should copy tags from the source resource to the snapshot or AMI.

        If you do not specify a value, the default is ``false`` .

        Default: false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-copytags
        '''
        result = self._values.get("copy_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def create_interval(self) -> typing.Optional[jsii.Number]:
        '''*[Default policies only]* Specifies how often the policy should run and create snapshots or AMIs.

        The creation frequency can range from 1 to 7 days. If you do not specify a value, the default is 1.

        Default: 1

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-createinterval
        '''
        result = self._values.get("create_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cross_region_copy_targets(self) -> typing.Any:
        '''*[Default policies only]* Specifies destination Regions for snapshot or AMI copies.

        You can specify up to 3 destination Regions. If you do not want to create cross-Region copies, omit this parameter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-crossregioncopytargets
        '''
        result = self._values.get("cross_region_copy_targets")
        return typing.cast(typing.Any, result)

    @builtins.property
    def default_policy(self) -> typing.Optional[builtins.str]:
        '''*[Default policies only]* Specify the type of default policy to create.

        - To create a default policy for EBS snapshots, that creates snapshots of all volumes in the Region that do not have recent backups, specify ``VOLUME`` .
        - To create a default policy for EBS-backed AMIs, that creates EBS-backed AMIs from all instances in the Region that do not have recent backups, specify ``INSTANCE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-defaultpolicy
        '''
        result = self._values.get("default_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the lifecycle policy.

        The characters ^[0-9A-Za-z _-]+$ are supported.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def exclusions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLifecyclePolicy.ExclusionsProperty]]:
        '''*[Default policies only]* Specifies exclusion parameters for volumes or instances for which you do not want to create snapshots or AMIs.

        The policy will not create snapshots or AMIs for target resources that match any of the specified exclusion parameters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-exclusions
        '''
        result = self._values.get("exclusions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLifecyclePolicy.ExclusionsProperty]], result)

    @builtins.property
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the IAM role used to run the operations specified by the lifecycle policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extend_deletion(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''*[Default policies only]* Defines the snapshot or AMI retention behavior for the policy if the source volume or instance is deleted, or if the policy enters the error, disabled, or deleted state.

        By default ( *ExtendDeletion=false* ):

        - If a source resource is deleted, Amazon Data Lifecycle Manager will continue to delete previously created snapshots or AMIs, up to but not including the last one, based on the specified retention period. If you want Amazon Data Lifecycle Manager to delete all snapshots or AMIs, including the last one, specify ``true`` .
        - If a policy enters the error, disabled, or deleted state, Amazon Data Lifecycle Manager stops deleting snapshots and AMIs. If you want Amazon Data Lifecycle Manager to continue deleting snapshots or AMIs, including the last one, if the policy enters one of these states, specify ``true`` .

        If you enable extended deletion ( *ExtendDeletion=true* ), you override both default behaviors simultaneously.

        If you do not specify a value, the default is ``false`` .

        Default: false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-extenddeletion
        '''
        result = self._values.get("extend_deletion")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def policy_details(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLifecyclePolicy.PolicyDetailsProperty]]:
        '''The configuration details of the lifecycle policy.

        .. epigraph::

           If you create a default policy, you can specify the request parameters either in the request body, or in the PolicyDetails request structure, but not both.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-policydetails
        '''
        result = self._values.get("policy_details")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLifecyclePolicy.PolicyDetailsProperty]], result)

    @builtins.property
    def retain_interval(self) -> typing.Optional[jsii.Number]:
        '''*[Default policies only]* Specifies how long the policy should retain snapshots or AMIs before deleting them.

        The retention period can range from 2 to 14 days, but it must be greater than the creation frequency to ensure that the policy retains at least 1 snapshot or AMI at any given time. If you do not specify a value, the default is 7.

        Default: 7

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-retaininterval
        '''
        result = self._values.get("retain_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''The activation state of the lifecycle policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-state
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to apply to the lifecycle policy during creation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html#cfn-dlm-lifecyclepolicy-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLifecyclePolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnLifecyclePolicy",
    "CfnLifecyclePolicyProps",
]

publication.publish()

def _typecheckingstub__2602533fbe79433bf8a3cb4984e0ec983ab5d121243f4d319dfc6038c8b96bb3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    copy_tags: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    create_interval: typing.Optional[jsii.Number] = None,
    cross_region_copy_targets: typing.Any = None,
    default_policy: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    exclusions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.ExclusionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    execution_role_arn: typing.Optional[builtins.str] = None,
    extend_deletion: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    policy_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.PolicyDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retain_interval: typing.Optional[jsii.Number] = None,
    state: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81434f0dc784e8376f1ea6bb29bea9761940fdfd0b638198d90f60d4d0f20218(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c006aacfdbc5fd2892b4f2c7ce867935b955bf498cc4be3e84b77318aa692f8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f66e06f3dd5f4f31da0050465d9d93ec64ce872a39b9831bba0678e14fa5fbc(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e355d2d56ace5cc54090484cdfafed2a85a9b48fa91a8df756bb89f4e2e1a38(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c77534ad651e2a8d67574cbcffaf68110be041f8971255d26c52491b23fdc32f(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fad1b7a52123f254bb9f0374f3546651f50ece8ef16650fdab011f0bd968afda(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b2c4be1aa9ae388ae0c3732cd9d2523c470c0014606872fca1696f56269686d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__697e92d466d31df6c2b785374b032b06ea49a5f0a5f4866b11f7a97c11bc27e5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLifecyclePolicy.ExclusionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__269443eefb0de5680ef719eb02ee0fda9c83a2e5291fa03da5a458a188d7a7c8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5a72190a4691449f1542993dcce214b4e84f38189762057ccaccba7f456d683(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28d8dbca09903b09bcfda56929bc379ae4e79616a6e38d78042df2d24f6464a3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLifecyclePolicy.PolicyDetailsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82aed9e32e25d4555a6a4435c5a18828e06b80cc9bf8e04617ce499f7259e7a0(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dec6c26d53f2189b6a1eceb4738437bca568a6c7616d987a2d4300b6648248c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b27e3373e59304017b144dff4d6d34a89b633c266e7a9c06230a117c457228b6(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9307e01a397f6690aa0752ac88ca2306a9ece8a8a78eb132935a5549dfbabada(
    *,
    cross_region_copy: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.CrossRegionCopyActionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69b614c12df5d26aa7cc0ea985df41404caf1067f445bd324dc6fa55b9b8c625(
    *,
    retention_archive_tier: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.RetentionArchiveTierProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8e1039f6cae4097770e1e2f744b67af71fec5dee8b6c811d16906aabf00fccb(
    *,
    retain_rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.ArchiveRetainRuleProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9b28ae8c7d63af3dc6b9cff4da91a651b9df9c94011501d2f12308ab311cacc(
    *,
    cron_expression: typing.Optional[builtins.str] = None,
    interval: typing.Optional[jsii.Number] = None,
    interval_unit: typing.Optional[builtins.str] = None,
    location: typing.Optional[builtins.str] = None,
    scripts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.ScriptProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    times: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c5fae284dc8f050edba69cd60584bdd81e13c9e3407c49aa284415b34c6b0e0(
    *,
    encryption_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    target: builtins.str,
    retain_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a0d27b116ca50c00fc7180da16cbf918eaa7d7119243d09585b27a71cabd3d5(
    *,
    interval: jsii.Number,
    interval_unit: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1718151bfbb17d9a4452203d36f9b6216ee80d4bd34f379b785da8696d31352e(
    *,
    interval: jsii.Number,
    interval_unit: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43d1308154968094810a1e971a8121cb2c821bd4deca38281f7b51fde975f885(
    *,
    encrypted: typing.Union[builtins.bool, _IResolvable_da3f097b],
    cmk_arn: typing.Optional[builtins.str] = None,
    copy_tags: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    deprecate_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.CrossRegionCopyDeprecateRuleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retain_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.CrossRegionCopyRetainRuleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    target: typing.Optional[builtins.str] = None,
    target_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df13b895e1f0fe3ab1717df947409da20e475efc7de490ec9a5646ed329ef27a(
    *,
    count: typing.Optional[jsii.Number] = None,
    interval: typing.Optional[jsii.Number] = None,
    interval_unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b9db946321cd9d24710d3479024da80bd3abb6be9bba91ad39d61a817fca6a2(
    *,
    encrypted: typing.Union[builtins.bool, _IResolvable_da3f097b],
    cmk_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f94e5460355048729001240653f8d96a3168ef0cbb26f5bc1ed5c17d02222336(
    *,
    event_type: builtins.str,
    snapshot_owner: typing.Sequence[builtins.str],
    description_regex: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f5f81a0abf746f322239a01132f42ce76e2468d95f09b5832596d946ade19d8(
    *,
    type: builtins.str,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.EventParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5692b64ab6dee50c1d5309ad0a3d609805882baacd6ea4c1c2d0733bc12c7502(
    *,
    exclude_boot_volumes: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    exclude_tags: typing.Any = None,
    exclude_volume_types: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c6091dc8881dc1eefedb91f093e87a24b9de27bbfd0785b7629a26e2bca19c9(
    *,
    availability_zones: typing.Optional[typing.Sequence[builtins.str]] = None,
    count: typing.Optional[jsii.Number] = None,
    interval: typing.Optional[jsii.Number] = None,
    interval_unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce5c17fb8a6043f2aa8baec3f4fa0908ae761e69ffca448db0c9b5b5d6e208ef(
    *,
    exclude_boot_volume: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    exclude_data_volume_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    no_reboot: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64a970d220e1b895bd71825b15385fe27ec0bc3bb778dbb76043312a45c45696(
    *,
    actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.ActionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    copy_tags: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    create_interval: typing.Optional[jsii.Number] = None,
    cross_region_copy_targets: typing.Any = None,
    event_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.EventSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    exclusions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.ExclusionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    extend_deletion: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.ParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    policy_language: typing.Optional[builtins.str] = None,
    policy_type: typing.Optional[builtins.str] = None,
    resource_locations: typing.Optional[typing.Sequence[builtins.str]] = None,
    resource_type: typing.Optional[builtins.str] = None,
    resource_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    retain_interval: typing.Optional[jsii.Number] = None,
    schedules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    target_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d63890f98bdab663b74392c501d0b6d353daba75e373aec4c47e220cb0c317ea(
    *,
    count: typing.Optional[jsii.Number] = None,
    interval: typing.Optional[jsii.Number] = None,
    interval_unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07f178891476deda83ce4ebdda6f02f0dff8b84d1330e2f6bf88d74f1e513ffa(
    *,
    count: typing.Optional[jsii.Number] = None,
    interval: typing.Optional[jsii.Number] = None,
    interval_unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9b4afd18ef7a7c10ab5cb55653ba53eff1da7bab75afaf21bdb01bb2d9841c5(
    *,
    archive_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.ArchiveRuleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    copy_tags: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    create_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.CreateRuleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cross_region_copy_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.CrossRegionCopyRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    deprecate_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.DeprecateRuleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    fast_restore_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.FastRestoreRuleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    retain_rule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.RetainRuleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    share_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.ShareRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags_to_add: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    variable_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae035efa2ba94c476212d1e54c4004eec95481ef5b9123ad74f1ec61e8c3921c(
    *,
    execute_operation_on_script_failure: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    execution_handler: typing.Optional[builtins.str] = None,
    execution_handler_service: typing.Optional[builtins.str] = None,
    execution_timeout: typing.Optional[jsii.Number] = None,
    maximum_retry_count: typing.Optional[jsii.Number] = None,
    stages: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17018411aa866dc818102e8981736b177dd1a23646009ebb8d8cbe6a34da52bf(
    *,
    target_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    unshare_interval: typing.Optional[jsii.Number] = None,
    unshare_interval_unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1414bd7f3e80e837a7b73bfb6d11bcc9e29191c357de74fe96a8efcfd1e89072(
    *,
    copy_tags: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    create_interval: typing.Optional[jsii.Number] = None,
    cross_region_copy_targets: typing.Any = None,
    default_policy: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    exclusions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.ExclusionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    execution_role_arn: typing.Optional[builtins.str] = None,
    extend_deletion: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    policy_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.PolicyDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retain_interval: typing.Optional[jsii.Number] = None,
    state: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
