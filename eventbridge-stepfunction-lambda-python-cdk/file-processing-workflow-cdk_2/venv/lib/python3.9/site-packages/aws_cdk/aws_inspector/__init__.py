'''
# Amazon Inspector Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_inspector as inspector
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Inspector construct libraries](https://constructs.dev/search?q=inspector)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Inspector resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Inspector.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Inspector](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Inspector.html).

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
class CfnAssessmentTarget(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_inspector.CfnAssessmentTarget",
):
    '''The ``AWS::Inspector::AssessmentTarget`` resource is used to create Amazon Inspector assessment targets, which specify the Amazon EC2 instances that will be analyzed during an assessment run.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttarget.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_inspector as inspector
        
        cfn_assessment_target = inspector.CfnAssessmentTarget(self, "MyCfnAssessmentTarget",
            assessment_target_name="assessmentTargetName",
            resource_group_arn="resourceGroupArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        assessment_target_name: typing.Optional[builtins.str] = None,
        resource_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param assessment_target_name: The name of the Amazon Inspector assessment target. The name must be unique within the AWS account .
        :param resource_group_arn: The ARN that specifies the resource group that is used to create the assessment target. If ``resourceGroupArn`` is not specified, all EC2 instances in the current AWS account and Region are included in the assessment target.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b68f769512afe2cc2200d1eaed82952c7d1dda03213723b68dd167dd4a283c7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAssessmentTargetProps(
            assessment_target_name=assessment_target_name,
            resource_group_arn=resource_group_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5f14eb1d1c6e1797ed67e8422f003c5cc4a0adbf320cde804dea9aa72def8c0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c96eda780d323d22a98c3b71d6497315b0c7cd642cee0584d8d2879261010ea4)
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
        '''The Amazon Resource Name (ARN) that specifies the assessment target that is created.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="assessmentTargetName")
    def assessment_target_name(self) -> typing.Optional[builtins.str]:
        '''The name of the Amazon Inspector assessment target.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assessmentTargetName"))

    @assessment_target_name.setter
    def assessment_target_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__696e7c8b7a035721b6449758cd7fb68528a5260db3e1a678f64a9e0b4c96126f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assessmentTargetName", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupArn")
    def resource_group_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN that specifies the resource group that is used to create the assessment target.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupArn"))

    @resource_group_arn.setter
    def resource_group_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c3b7128ce033766af9f209c5a813d7952af426568a0900860ae410016d94434)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_inspector.CfnAssessmentTargetProps",
    jsii_struct_bases=[],
    name_mapping={
        "assessment_target_name": "assessmentTargetName",
        "resource_group_arn": "resourceGroupArn",
    },
)
class CfnAssessmentTargetProps:
    def __init__(
        self,
        *,
        assessment_target_name: typing.Optional[builtins.str] = None,
        resource_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnAssessmentTarget``.

        :param assessment_target_name: The name of the Amazon Inspector assessment target. The name must be unique within the AWS account .
        :param resource_group_arn: The ARN that specifies the resource group that is used to create the assessment target. If ``resourceGroupArn`` is not specified, all EC2 instances in the current AWS account and Region are included in the assessment target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttarget.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_inspector as inspector
            
            cfn_assessment_target_props = inspector.CfnAssessmentTargetProps(
                assessment_target_name="assessmentTargetName",
                resource_group_arn="resourceGroupArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3da3c682a3ad54cf425ef49b70282900ce9139c52f5ffe48fcec156dad047881)
            check_type(argname="argument assessment_target_name", value=assessment_target_name, expected_type=type_hints["assessment_target_name"])
            check_type(argname="argument resource_group_arn", value=resource_group_arn, expected_type=type_hints["resource_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if assessment_target_name is not None:
            self._values["assessment_target_name"] = assessment_target_name
        if resource_group_arn is not None:
            self._values["resource_group_arn"] = resource_group_arn

    @builtins.property
    def assessment_target_name(self) -> typing.Optional[builtins.str]:
        '''The name of the Amazon Inspector assessment target.

        The name must be unique within the AWS account .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttarget.html#cfn-inspector-assessmenttarget-assessmenttargetname
        '''
        result = self._values.get("assessment_target_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_group_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN that specifies the resource group that is used to create the assessment target.

        If ``resourceGroupArn`` is not specified, all EC2 instances in the current AWS account and Region are included in the assessment target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttarget.html#cfn-inspector-assessmenttarget-resourcegrouparn
        '''
        result = self._values.get("resource_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssessmentTargetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnAssessmentTemplate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_inspector.CfnAssessmentTemplate",
):
    '''The ``AWS::Inspector::AssessmentTemplate`` resource creates an Amazon Inspector assessment template, which specifies the Inspector assessment targets that will be evaluated by an assessment run and its related configurations.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_inspector as inspector
        
        cfn_assessment_template = inspector.CfnAssessmentTemplate(self, "MyCfnAssessmentTemplate",
            assessment_target_arn="assessmentTargetArn",
            duration_in_seconds=123,
            rules_package_arns=["rulesPackageArns"],
        
            # the properties below are optional
            assessment_template_name="assessmentTemplateName",
            user_attributes_for_findings=[CfnTag(
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
        assessment_target_arn: builtins.str,
        duration_in_seconds: jsii.Number,
        rules_package_arns: typing.Sequence[builtins.str],
        assessment_template_name: typing.Optional[builtins.str] = None,
        user_attributes_for_findings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param assessment_target_arn: The ARN of the assessment target to be included in the assessment template.
        :param duration_in_seconds: The duration of the assessment run in seconds.
        :param rules_package_arns: The ARNs of the rules packages that you want to use in the assessment template.
        :param assessment_template_name: The user-defined name that identifies the assessment template that you want to create. You can create several assessment templates for the same assessment target. The names of the assessment templates that correspond to a particular assessment target must be unique.
        :param user_attributes_for_findings: The user-defined attributes that are assigned to every finding that is generated by the assessment run that uses this assessment template. Within an assessment template, each key must be unique.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0aec98d77afaa289ba5ff5ab3e1e82607bb8cb13a428a224da95d05728925c1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAssessmentTemplateProps(
            assessment_target_arn=assessment_target_arn,
            duration_in_seconds=duration_in_seconds,
            rules_package_arns=rules_package_arns,
            assessment_template_name=assessment_template_name,
            user_attributes_for_findings=user_attributes_for_findings,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26cf9a0eb97cd4919defd3b01b42374af27395ff83bd788954c1abe2240d2794)
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
            type_hints = typing.get_type_hints(_typecheckingstub__287bbc3b94e18fd36b8a19e492653dd18b9010bdc96d64acc7b606eab9de0b96)
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
        '''The Amazon Resource Name (ARN) that specifies the assessment template that is created.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="assessmentTargetArn")
    def assessment_target_arn(self) -> builtins.str:
        '''The ARN of the assessment target to be included in the assessment template.'''
        return typing.cast(builtins.str, jsii.get(self, "assessmentTargetArn"))

    @assessment_target_arn.setter
    def assessment_target_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63c7557bb27bbdcaee7ab7dcc8c266ff6e0ce7f0976bfd7657b5a0552ca5b141)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assessmentTargetArn", value)

    @builtins.property
    @jsii.member(jsii_name="durationInSeconds")
    def duration_in_seconds(self) -> jsii.Number:
        '''The duration of the assessment run in seconds.'''
        return typing.cast(jsii.Number, jsii.get(self, "durationInSeconds"))

    @duration_in_seconds.setter
    def duration_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1679cd823397fccdeff2d687564d3851dcf6771888a4a72e7272de9b8b18140)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "durationInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="rulesPackageArns")
    def rules_package_arns(self) -> typing.List[builtins.str]:
        '''The ARNs of the rules packages that you want to use in the assessment template.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "rulesPackageArns"))

    @rules_package_arns.setter
    def rules_package_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3a25aa19b6cb4b802c3c9b40923d82c4459ee78ac102140ee3072dc63781d6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rulesPackageArns", value)

    @builtins.property
    @jsii.member(jsii_name="assessmentTemplateName")
    def assessment_template_name(self) -> typing.Optional[builtins.str]:
        '''The user-defined name that identifies the assessment template that you want to create.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "assessmentTemplateName"))

    @assessment_template_name.setter
    def assessment_template_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7f0d1dbac048149a227c61a3da750d8a21856f65b1be53f20d2d13f8d061e0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assessmentTemplateName", value)

    @builtins.property
    @jsii.member(jsii_name="userAttributesForFindings")
    def user_attributes_for_findings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]]:
        '''The user-defined attributes that are assigned to every finding that is generated by the assessment run that uses this assessment template.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]], jsii.get(self, "userAttributesForFindings"))

    @user_attributes_for_findings.setter
    def user_attributes_for_findings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f1d80ec27deb1af871c5b61bfa5b4676d207855a37d91499ac58255befac278)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userAttributesForFindings", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_inspector.CfnAssessmentTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "assessment_target_arn": "assessmentTargetArn",
        "duration_in_seconds": "durationInSeconds",
        "rules_package_arns": "rulesPackageArns",
        "assessment_template_name": "assessmentTemplateName",
        "user_attributes_for_findings": "userAttributesForFindings",
    },
)
class CfnAssessmentTemplateProps:
    def __init__(
        self,
        *,
        assessment_target_arn: builtins.str,
        duration_in_seconds: jsii.Number,
        rules_package_arns: typing.Sequence[builtins.str],
        assessment_template_name: typing.Optional[builtins.str] = None,
        user_attributes_for_findings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAssessmentTemplate``.

        :param assessment_target_arn: The ARN of the assessment target to be included in the assessment template.
        :param duration_in_seconds: The duration of the assessment run in seconds.
        :param rules_package_arns: The ARNs of the rules packages that you want to use in the assessment template.
        :param assessment_template_name: The user-defined name that identifies the assessment template that you want to create. You can create several assessment templates for the same assessment target. The names of the assessment templates that correspond to a particular assessment target must be unique.
        :param user_attributes_for_findings: The user-defined attributes that are assigned to every finding that is generated by the assessment run that uses this assessment template. Within an assessment template, each key must be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_inspector as inspector
            
            cfn_assessment_template_props = inspector.CfnAssessmentTemplateProps(
                assessment_target_arn="assessmentTargetArn",
                duration_in_seconds=123,
                rules_package_arns=["rulesPackageArns"],
            
                # the properties below are optional
                assessment_template_name="assessmentTemplateName",
                user_attributes_for_findings=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd83de00af49e4bec0f309270e8475a120bd6b2cc3c1a1b5df0acbbd1f0e3424)
            check_type(argname="argument assessment_target_arn", value=assessment_target_arn, expected_type=type_hints["assessment_target_arn"])
            check_type(argname="argument duration_in_seconds", value=duration_in_seconds, expected_type=type_hints["duration_in_seconds"])
            check_type(argname="argument rules_package_arns", value=rules_package_arns, expected_type=type_hints["rules_package_arns"])
            check_type(argname="argument assessment_template_name", value=assessment_template_name, expected_type=type_hints["assessment_template_name"])
            check_type(argname="argument user_attributes_for_findings", value=user_attributes_for_findings, expected_type=type_hints["user_attributes_for_findings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "assessment_target_arn": assessment_target_arn,
            "duration_in_seconds": duration_in_seconds,
            "rules_package_arns": rules_package_arns,
        }
        if assessment_template_name is not None:
            self._values["assessment_template_name"] = assessment_template_name
        if user_attributes_for_findings is not None:
            self._values["user_attributes_for_findings"] = user_attributes_for_findings

    @builtins.property
    def assessment_target_arn(self) -> builtins.str:
        '''The ARN of the assessment target to be included in the assessment template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html#cfn-inspector-assessmenttemplate-assessmenttargetarn
        '''
        result = self._values.get("assessment_target_arn")
        assert result is not None, "Required property 'assessment_target_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def duration_in_seconds(self) -> jsii.Number:
        '''The duration of the assessment run in seconds.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html#cfn-inspector-assessmenttemplate-durationinseconds
        '''
        result = self._values.get("duration_in_seconds")
        assert result is not None, "Required property 'duration_in_seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def rules_package_arns(self) -> typing.List[builtins.str]:
        '''The ARNs of the rules packages that you want to use in the assessment template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html#cfn-inspector-assessmenttemplate-rulespackagearns
        '''
        result = self._values.get("rules_package_arns")
        assert result is not None, "Required property 'rules_package_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def assessment_template_name(self) -> typing.Optional[builtins.str]:
        '''The user-defined name that identifies the assessment template that you want to create.

        You can create several assessment templates for the same assessment target. The names of the assessment templates that correspond to a particular assessment target must be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html#cfn-inspector-assessmenttemplate-assessmenttemplatename
        '''
        result = self._values.get("assessment_template_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_attributes_for_findings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]]:
        '''The user-defined attributes that are assigned to every finding that is generated by the assessment run that uses this assessment template.

        Within an assessment template, each key must be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-assessmenttemplate.html#cfn-inspector-assessmenttemplate-userattributesforfindings
        '''
        result = self._values.get("user_attributes_for_findings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssessmentTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResourceGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_inspector.CfnResourceGroup",
):
    '''The ``AWS::Inspector::ResourceGroup`` resource is used to create Amazon Inspector resource groups.

    A resource group defines a set of tags that, when queried, identify the AWS resources that make up the assessment target.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-resourcegroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_inspector as inspector
        
        cfn_resource_group = inspector.CfnResourceGroup(self, "MyCfnResourceGroup",
            resource_group_tags=[CfnTag(
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
        resource_group_tags: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param resource_group_tags: The tags (key and value pairs) that will be associated with the resource group. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__765c554a4b71cd63f2e78a1e2076a685c6f29c2c80897b6ac5b42ba62c8eda6f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourceGroupProps(resource_group_tags=resource_group_tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2991bf2cce18051d1438267ba8bc5a3aab18f9935b0b46c4038d0430212be68a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d0708f9f6448e0e45875236612dde580742308098d7455aaab77a96199d883a)
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
        '''The Amazon Resource Name (ARN) that specifies the resource group that is created.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupTags")
    def resource_group_tags(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]:
        '''The tags (key and value pairs) that will be associated with the resource group.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]], jsii.get(self, "resourceGroupTags"))

    @resource_group_tags.setter
    def resource_group_tags(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__655fc060449fbf4c2bf808e3890ed0325d7694a9273187b0d9c458a3c573861e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupTags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_inspector.CfnResourceGroupProps",
    jsii_struct_bases=[],
    name_mapping={"resource_group_tags": "resourceGroupTags"},
)
class CfnResourceGroupProps:
    def __init__(
        self,
        *,
        resource_group_tags: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]],
    ) -> None:
        '''Properties for defining a ``CfnResourceGroup``.

        :param resource_group_tags: The tags (key and value pairs) that will be associated with the resource group. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-resourcegroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_inspector as inspector
            
            cfn_resource_group_props = inspector.CfnResourceGroupProps(
                resource_group_tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c5c1b9c891faa3d69b08685ad61d96a298505b5f24600854c5dd3fd3c4b5be2)
            check_type(argname="argument resource_group_tags", value=resource_group_tags, expected_type=type_hints["resource_group_tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_group_tags": resource_group_tags,
        }

    @builtins.property
    def resource_group_tags(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]:
        '''The tags (key and value pairs) that will be associated with the resource group.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspector-resourcegroup.html#cfn-inspector-resourcegroup-resourcegrouptags
        '''
        result = self._values.get("resource_group_tags")
        assert result is not None, "Required property 'resource_group_tags' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAssessmentTarget",
    "CfnAssessmentTargetProps",
    "CfnAssessmentTemplate",
    "CfnAssessmentTemplateProps",
    "CfnResourceGroup",
    "CfnResourceGroupProps",
]

publication.publish()

def _typecheckingstub__8b68f769512afe2cc2200d1eaed82952c7d1dda03213723b68dd167dd4a283c7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    assessment_target_name: typing.Optional[builtins.str] = None,
    resource_group_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5f14eb1d1c6e1797ed67e8422f003c5cc4a0adbf320cde804dea9aa72def8c0(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c96eda780d323d22a98c3b71d6497315b0c7cd642cee0584d8d2879261010ea4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__696e7c8b7a035721b6449758cd7fb68528a5260db3e1a678f64a9e0b4c96126f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c3b7128ce033766af9f209c5a813d7952af426568a0900860ae410016d94434(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3da3c682a3ad54cf425ef49b70282900ce9139c52f5ffe48fcec156dad047881(
    *,
    assessment_target_name: typing.Optional[builtins.str] = None,
    resource_group_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0aec98d77afaa289ba5ff5ab3e1e82607bb8cb13a428a224da95d05728925c1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    assessment_target_arn: builtins.str,
    duration_in_seconds: jsii.Number,
    rules_package_arns: typing.Sequence[builtins.str],
    assessment_template_name: typing.Optional[builtins.str] = None,
    user_attributes_for_findings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26cf9a0eb97cd4919defd3b01b42374af27395ff83bd788954c1abe2240d2794(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__287bbc3b94e18fd36b8a19e492653dd18b9010bdc96d64acc7b606eab9de0b96(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63c7557bb27bbdcaee7ab7dcc8c266ff6e0ce7f0976bfd7657b5a0552ca5b141(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1679cd823397fccdeff2d687564d3851dcf6771888a4a72e7272de9b8b18140(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3a25aa19b6cb4b802c3c9b40923d82c4459ee78ac102140ee3072dc63781d6a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7f0d1dbac048149a227c61a3da750d8a21856f65b1be53f20d2d13f8d061e0c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f1d80ec27deb1af871c5b61bfa5b4676d207855a37d91499ac58255befac278(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd83de00af49e4bec0f309270e8475a120bd6b2cc3c1a1b5df0acbbd1f0e3424(
    *,
    assessment_target_arn: builtins.str,
    duration_in_seconds: jsii.Number,
    rules_package_arns: typing.Sequence[builtins.str],
    assessment_template_name: typing.Optional[builtins.str] = None,
    user_attributes_for_findings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__765c554a4b71cd63f2e78a1e2076a685c6f29c2c80897b6ac5b42ba62c8eda6f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    resource_group_tags: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2991bf2cce18051d1438267ba8bc5a3aab18f9935b0b46c4038d0430212be68a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d0708f9f6448e0e45875236612dde580742308098d7455aaab77a96199d883a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__655fc060449fbf4c2bf808e3890ed0325d7694a9273187b0d9c458a3c573861e(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c5c1b9c891faa3d69b08685ad61d96a298505b5f24600854c5dd3fd3c4b5be2(
    *,
    resource_group_tags: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass
