'''
# AWS::FraudDetector Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_frauddetector as frauddetector
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for FraudDetector construct libraries](https://constructs.dev/search?q=frauddetector)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::FraudDetector resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_FraudDetector.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::FraudDetector](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_FraudDetector.html).

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
    ITaggable as _ITaggable_36806126,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDetector(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_frauddetector.CfnDetector",
):
    '''Manages a detector and associated detector versions.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_frauddetector as frauddetector
        
        cfn_detector = frauddetector.CfnDetector(self, "MyCfnDetector",
            detector_id="detectorId",
            event_type=frauddetector.CfnDetector.EventTypeProperty(
                arn="arn",
                created_time="createdTime",
                description="description",
                entity_types=[frauddetector.CfnDetector.EntityTypeProperty(
                    arn="arn",
                    created_time="createdTime",
                    description="description",
                    inline=False,
                    last_updated_time="lastUpdatedTime",
                    name="name",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )],
                event_variables=[frauddetector.CfnDetector.EventVariableProperty(
                    arn="arn",
                    created_time="createdTime",
                    data_source="dataSource",
                    data_type="dataType",
                    default_value="defaultValue",
                    description="description",
                    inline=False,
                    last_updated_time="lastUpdatedTime",
                    name="name",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )],
                    variable_type="variableType"
                )],
                inline=False,
                labels=[frauddetector.CfnDetector.LabelProperty(
                    arn="arn",
                    created_time="createdTime",
                    description="description",
                    inline=False,
                    last_updated_time="lastUpdatedTime",
                    name="name",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )],
                last_updated_time="lastUpdatedTime",
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            ),
            rules=[frauddetector.CfnDetector.RuleProperty(
                arn="arn",
                created_time="createdTime",
                description="description",
                detector_id="detectorId",
                expression="expression",
                language="language",
                last_updated_time="lastUpdatedTime",
                outcomes=[frauddetector.CfnDetector.OutcomeProperty(
                    arn="arn",
                    created_time="createdTime",
                    description="description",
                    inline=False,
                    last_updated_time="lastUpdatedTime",
                    name="name",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )],
                rule_id="ruleId",
                rule_version="ruleVersion",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )],
        
            # the properties below are optional
            associated_models=[frauddetector.CfnDetector.ModelProperty(
                arn="arn"
            )],
            description="description",
            detector_version_status="detectorVersionStatus",
            rule_execution_mode="ruleExecutionMode",
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
        detector_id: builtins.str,
        event_type: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetector.EventTypeProperty", typing.Dict[builtins.str, typing.Any]]],
        rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetector.RuleProperty", typing.Dict[builtins.str, typing.Any]]]]],
        associated_models: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetector.ModelProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        detector_version_status: typing.Optional[builtins.str] = None,
        rule_execution_mode: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param detector_id: The name of the detector.
        :param event_type: The event type associated with this detector.
        :param rules: The rules to include in the detector version.
        :param associated_models: The models to associate with this detector. You must provide the ARNs of all the models you want to associate.
        :param description: The detector description.
        :param detector_version_status: The status of the detector version. If a value is not provided for this property, AWS CloudFormation assumes ``DRAFT`` status. Valid values: ``ACTIVE | DRAFT``
        :param rule_execution_mode: The rule execution mode for the rules included in the detector version. Valid values: ``FIRST_MATCHED | ALL_MATCHED`` Default value: ``FIRST_MATCHED`` You can define and edit the rule mode at the detector version level, when it is in draft status. If you specify ``FIRST_MATCHED`` , Amazon Fraud Detector evaluates rules sequentially, first to last, stopping at the first matched rule. Amazon Fraud dectector then provides the outcomes for that single rule. If you specifiy ``ALL_MATCHED`` , Amazon Fraud Detector evaluates all rules and returns the outcomes for all matched rules.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34f177b06bae06cc28a84eadedbeeac967db23fde60544e18b48e387ec5e98f8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDetectorProps(
            detector_id=detector_id,
            event_type=event_type,
            rules=rules,
            associated_models=associated_models,
            description=description,
            detector_version_status=detector_version_status,
            rule_execution_mode=rule_execution_mode,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__126b5270f9e7ee19c314a22a060f32922f846c4adae62a4d0b4479d45bd125ac)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ccb1420d0dc99c9166f8186cf6aac8171c218937f45e47f0971713c0231a004e)
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
        '''The detector ARN.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''Timestamp of when detector was created.

        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrDetectorVersionId")
    def attr_detector_version_id(self) -> builtins.str:
        '''The name of the detector.

        :cloudformationAttribute: DetectorVersionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDetectorVersionId"))

    @builtins.property
    @jsii.member(jsii_name="attrEventTypeArn")
    def attr_event_type_arn(self) -> builtins.str:
        '''The ARN of the event type.

        :cloudformationAttribute: EventType.Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEventTypeArn"))

    @builtins.property
    @jsii.member(jsii_name="attrEventTypeCreatedTime")
    def attr_event_type_created_time(self) -> builtins.str:
        '''The time when the event type was created.

        :cloudformationAttribute: EventType.CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEventTypeCreatedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrEventTypeLastUpdatedTime")
    def attr_event_type_last_updated_time(self) -> builtins.str:
        '''The time when the event type was last updated.

        :cloudformationAttribute: EventType.LastUpdatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEventTypeLastUpdatedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedTime")
    def attr_last_updated_time(self) -> builtins.str:
        '''Timestamp of when detector was last updated.

        :cloudformationAttribute: LastUpdatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedTime"))

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
    @jsii.member(jsii_name="detectorId")
    def detector_id(self) -> builtins.str:
        '''The name of the detector.'''
        return typing.cast(builtins.str, jsii.get(self, "detectorId"))

    @detector_id.setter
    def detector_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea1c83f296328b1afdeee432d51335bf25e25782aaa9cd76b6f2757dbe1419f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detectorId", value)

    @builtins.property
    @jsii.member(jsii_name="eventType")
    def event_type(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnDetector.EventTypeProperty"]:
        '''The event type associated with this detector.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDetector.EventTypeProperty"], jsii.get(self, "eventType"))

    @event_type.setter
    def event_type(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnDetector.EventTypeProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93bd5757764ac87038d7f200cd3d8de7e8b2fe7c1672e6177be640824ba52ccf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventType", value)

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetector.RuleProperty"]]]:
        '''The rules to include in the detector version.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetector.RuleProperty"]]], jsii.get(self, "rules"))

    @rules.setter
    def rules(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetector.RuleProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fb8a2023ee1e11b475185f1ce6d40e0f9724e1f39f830efce457fec14d6e803)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rules", value)

    @builtins.property
    @jsii.member(jsii_name="associatedModels")
    def associated_models(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetector.ModelProperty"]]]]:
        '''The models to associate with this detector.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetector.ModelProperty"]]]], jsii.get(self, "associatedModels"))

    @associated_models.setter
    def associated_models(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetector.ModelProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fa17c6e2d7f7f459019fd5d15924131bdf90bb9a9137f9b0d489a3063bb0c57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associatedModels", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The detector description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9657adb56d25aaeb148b4c0b1d9a4db1824078c550951eb37676edd06e02e228)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="detectorVersionStatus")
    def detector_version_status(self) -> typing.Optional[builtins.str]:
        '''The status of the detector version.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "detectorVersionStatus"))

    @detector_version_status.setter
    def detector_version_status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80ccaa368bd0676492bec90566a80d80de97fa630f6cc5a916bcd87a8fb61e08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detectorVersionStatus", value)

    @builtins.property
    @jsii.member(jsii_name="ruleExecutionMode")
    def rule_execution_mode(self) -> typing.Optional[builtins.str]:
        '''The rule execution mode for the rules included in the detector version.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleExecutionMode"))

    @rule_execution_mode.setter
    def rule_execution_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f37c0d89da5c5181365d1b3e0d414babeedcb502094947b1e138d41918da0bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleExecutionMode", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79bbcae57d55d3a1292ee375130b1ce78e88694b733f5018de1532c9840f2d00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_frauddetector.CfnDetector.EntityTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "created_time": "createdTime",
            "description": "description",
            "inline": "inline",
            "last_updated_time": "lastUpdatedTime",
            "name": "name",
            "tags": "tags",
        },
    )
    class EntityTypeProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            created_time: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            inline: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            last_updated_time: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The entity type details.

            :param arn: The entity type ARN.
            :param created_time: Timestamp of when the entity type was created.
            :param description: The entity type description.
            :param inline: Indicates whether the resource is defined within this CloudFormation template and impacts the create, update, and delete behavior of the stack. If the value is ``true`` , CloudFormation will create/update/delete the resource when creating/updating/deleting the stack. If the value is ``false`` , CloudFormation will validate that the object exists and then use it within the resource without making changes to the object. For example, when creating ``AWS::FraudDetector::Detector`` you must define at least two variables. You can set ``Inline=true`` for these Variables and CloudFormation will create/update/delete the variables as part of stack operations. However, if you set ``Inline=false`` , CloudFormation will associate the variables to your detector but not execute any changes to the variables.
            :param last_updated_time: Timestamp of when the entity type was last updated.
            :param name: The entity type name.
            :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_frauddetector as frauddetector
                
                entity_type_property = frauddetector.CfnDetector.EntityTypeProperty(
                    arn="arn",
                    created_time="createdTime",
                    description="description",
                    inline=False,
                    last_updated_time="lastUpdatedTime",
                    name="name",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__748d29fdb915a872929d832801bbc352f01eda4881f57ab49c9f76dc67866b13)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument created_time", value=created_time, expected_type=type_hints["created_time"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument inline", value=inline, expected_type=type_hints["inline"])
                check_type(argname="argument last_updated_time", value=last_updated_time, expected_type=type_hints["last_updated_time"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if created_time is not None:
                self._values["created_time"] = created_time
            if description is not None:
                self._values["description"] = description
            if inline is not None:
                self._values["inline"] = inline
            if last_updated_time is not None:
                self._values["last_updated_time"] = last_updated_time
            if name is not None:
                self._values["name"] = name
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The entity type ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def created_time(self) -> typing.Optional[builtins.str]:
            '''Timestamp of when the entity type was created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-createdtime
            '''
            result = self._values.get("created_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The entity type description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inline(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the resource is defined within this CloudFormation template and impacts the create, update, and delete behavior of the stack.

            If the value is ``true`` , CloudFormation will create/update/delete the resource when creating/updating/deleting the stack. If the value is ``false`` , CloudFormation will validate that the object exists and then use it within the resource without making changes to the object.

            For example, when creating ``AWS::FraudDetector::Detector`` you must define at least two variables. You can set ``Inline=true`` for these Variables and CloudFormation will create/update/delete the variables as part of stack operations. However, if you set ``Inline=false`` , CloudFormation will associate the variables to your detector but not execute any changes to the variables.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-inline
            '''
            result = self._values.get("inline")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def last_updated_time(self) -> typing.Optional[builtins.str]:
            '''Timestamp of when the entity type was last updated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-lastupdatedtime
            '''
            result = self._values.get("last_updated_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The entity type name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
            '''An array of key-value pairs to apply to this resource.

            For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-entitytype.html#cfn-frauddetector-detector-entitytype-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EntityTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_frauddetector.CfnDetector.EventTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "created_time": "createdTime",
            "description": "description",
            "entity_types": "entityTypes",
            "event_variables": "eventVariables",
            "inline": "inline",
            "labels": "labels",
            "last_updated_time": "lastUpdatedTime",
            "name": "name",
            "tags": "tags",
        },
    )
    class EventTypeProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            created_time: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            entity_types: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetector.EntityTypeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            event_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetector.EventVariableProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            inline: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            labels: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetector.LabelProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            last_updated_time: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The event type details.

            :param arn: The entity type ARN.
            :param created_time: Timestamp of when the event type was created.
            :param description: The event type description.
            :param entity_types: The event type entity types.
            :param event_variables: The event type event variables.
            :param inline: Indicates whether the resource is defined within this CloudFormation template and impacts the create, update, and delete behavior of the stack. If the value is ``true`` , CloudFormation will create/update/delete the resource when creating/updating/deleting the stack. If the value is ``false`` , CloudFormation will validate that the object exists and then use it within the resource without making changes to the object. For example, when creating ``AWS::FraudDetector::Detector`` you must define at least two variables. You can set ``Inline=true`` for these variables and CloudFormation will create/update/delete the Variables as part of stack operations. However, if you set ``Inline=false`` , CloudFormation will associate the variables to your detector but not execute any changes to the variables.
            :param labels: The event type labels.
            :param last_updated_time: Timestamp of when the event type was last updated.
            :param name: The event type name.
            :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_frauddetector as frauddetector
                
                event_type_property = frauddetector.CfnDetector.EventTypeProperty(
                    arn="arn",
                    created_time="createdTime",
                    description="description",
                    entity_types=[frauddetector.CfnDetector.EntityTypeProperty(
                        arn="arn",
                        created_time="createdTime",
                        description="description",
                        inline=False,
                        last_updated_time="lastUpdatedTime",
                        name="name",
                        tags=[CfnTag(
                            key="key",
                            value="value"
                        )]
                    )],
                    event_variables=[frauddetector.CfnDetector.EventVariableProperty(
                        arn="arn",
                        created_time="createdTime",
                        data_source="dataSource",
                        data_type="dataType",
                        default_value="defaultValue",
                        description="description",
                        inline=False,
                        last_updated_time="lastUpdatedTime",
                        name="name",
                        tags=[CfnTag(
                            key="key",
                            value="value"
                        )],
                        variable_type="variableType"
                    )],
                    inline=False,
                    labels=[frauddetector.CfnDetector.LabelProperty(
                        arn="arn",
                        created_time="createdTime",
                        description="description",
                        inline=False,
                        last_updated_time="lastUpdatedTime",
                        name="name",
                        tags=[CfnTag(
                            key="key",
                            value="value"
                        )]
                    )],
                    last_updated_time="lastUpdatedTime",
                    name="name",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__118c1a0ac0699f5c01003dd52bd52397d476baf9a00d5bad28ed3d95cdc2ffad)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument created_time", value=created_time, expected_type=type_hints["created_time"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument entity_types", value=entity_types, expected_type=type_hints["entity_types"])
                check_type(argname="argument event_variables", value=event_variables, expected_type=type_hints["event_variables"])
                check_type(argname="argument inline", value=inline, expected_type=type_hints["inline"])
                check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
                check_type(argname="argument last_updated_time", value=last_updated_time, expected_type=type_hints["last_updated_time"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if created_time is not None:
                self._values["created_time"] = created_time
            if description is not None:
                self._values["description"] = description
            if entity_types is not None:
                self._values["entity_types"] = entity_types
            if event_variables is not None:
                self._values["event_variables"] = event_variables
            if inline is not None:
                self._values["inline"] = inline
            if labels is not None:
                self._values["labels"] = labels
            if last_updated_time is not None:
                self._values["last_updated_time"] = last_updated_time
            if name is not None:
                self._values["name"] = name
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The entity type ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def created_time(self) -> typing.Optional[builtins.str]:
            '''Timestamp of when the event type was created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-createdtime
            '''
            result = self._values.get("created_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The event type description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def entity_types(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetector.EntityTypeProperty"]]]]:
            '''The event type entity types.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-entitytypes
            '''
            result = self._values.get("entity_types")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetector.EntityTypeProperty"]]]], result)

        @builtins.property
        def event_variables(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetector.EventVariableProperty"]]]]:
            '''The event type event variables.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-eventvariables
            '''
            result = self._values.get("event_variables")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetector.EventVariableProperty"]]]], result)

        @builtins.property
        def inline(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the resource is defined within this CloudFormation template and impacts the create, update, and delete behavior of the stack.

            If the value is ``true`` , CloudFormation will create/update/delete the resource when creating/updating/deleting the stack. If the value is ``false`` , CloudFormation will validate that the object exists and then use it within the resource without making changes to the object.

            For example, when creating ``AWS::FraudDetector::Detector`` you must define at least two variables. You can set ``Inline=true`` for these variables and CloudFormation will create/update/delete the Variables as part of stack operations. However, if you set ``Inline=false`` , CloudFormation will associate the variables to your detector but not execute any changes to the variables.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-inline
            '''
            result = self._values.get("inline")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def labels(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetector.LabelProperty"]]]]:
            '''The event type labels.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-labels
            '''
            result = self._values.get("labels")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetector.LabelProperty"]]]], result)

        @builtins.property
        def last_updated_time(self) -> typing.Optional[builtins.str]:
            '''Timestamp of when the event type was last updated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-lastupdatedtime
            '''
            result = self._values.get("last_updated_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The event type name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
            '''An array of key-value pairs to apply to this resource.

            For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventtype.html#cfn-frauddetector-detector-eventtype-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_frauddetector.CfnDetector.EventVariableProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "created_time": "createdTime",
            "data_source": "dataSource",
            "data_type": "dataType",
            "default_value": "defaultValue",
            "description": "description",
            "inline": "inline",
            "last_updated_time": "lastUpdatedTime",
            "name": "name",
            "tags": "tags",
            "variable_type": "variableType",
        },
    )
    class EventVariableProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            created_time: typing.Optional[builtins.str] = None,
            data_source: typing.Optional[builtins.str] = None,
            data_type: typing.Optional[builtins.str] = None,
            default_value: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            inline: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            last_updated_time: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
            variable_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The event type variable for the detector.

            :param arn: The event variable ARN.
            :param created_time: Timestamp for when the event variable was created.
            :param data_source: The data source of the event variable. Valid values: ``EVENT | EXTERNAL_MODEL_SCORE`` When defining a variable within a detector, you can only use the ``EVENT`` value for DataSource when the *Inline* property is set to true. If the *Inline* property is set false, you can use either ``EVENT`` or ``MODEL_SCORE`` for DataSource.
            :param data_type: The data type of the event variable. Valid values: ``STRING | INTEGER | BOOLEAN | FLOAT``
            :param default_value: The default value of the event variable. This is required if you are providing the details of your variables instead of the ARN.
            :param description: The description of the event variable.
            :param inline: Indicates whether the resource is defined within this CloudFormation template and impacts the create, update, and delete behavior of the stack. If the value is ``true`` , CloudFormation will create/update/delete the resource when creating/updating/deleting the stack. If the value is ``false`` , CloudFormation will validate that the object exists and then use it within the resource without making changes to the object. For example, when creating ``AWS::FraudDetector::Detector`` you must define at least two variables. You can set ``Inline=true`` for these variables and CloudFormation will create/update/delete the variables as part of stack operations. However, if you set ``Inline=false`` , CloudFormation will associate the variables to your detector but not execute any changes to the variables.
            :param last_updated_time: Timestamp for when the event variable was last updated.
            :param name: The name of the event variable.
            :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
            :param variable_type: The type of event variable. For more information, see `Variable types <https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_frauddetector as frauddetector
                
                event_variable_property = frauddetector.CfnDetector.EventVariableProperty(
                    arn="arn",
                    created_time="createdTime",
                    data_source="dataSource",
                    data_type="dataType",
                    default_value="defaultValue",
                    description="description",
                    inline=False,
                    last_updated_time="lastUpdatedTime",
                    name="name",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )],
                    variable_type="variableType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cb4525b017a8d1866b255be6b865fcd15a8810d62d25e0bd80f2d4868748d7a2)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument created_time", value=created_time, expected_type=type_hints["created_time"])
                check_type(argname="argument data_source", value=data_source, expected_type=type_hints["data_source"])
                check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
                check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument inline", value=inline, expected_type=type_hints["inline"])
                check_type(argname="argument last_updated_time", value=last_updated_time, expected_type=type_hints["last_updated_time"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
                check_type(argname="argument variable_type", value=variable_type, expected_type=type_hints["variable_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if created_time is not None:
                self._values["created_time"] = created_time
            if data_source is not None:
                self._values["data_source"] = data_source
            if data_type is not None:
                self._values["data_type"] = data_type
            if default_value is not None:
                self._values["default_value"] = default_value
            if description is not None:
                self._values["description"] = description
            if inline is not None:
                self._values["inline"] = inline
            if last_updated_time is not None:
                self._values["last_updated_time"] = last_updated_time
            if name is not None:
                self._values["name"] = name
            if tags is not None:
                self._values["tags"] = tags
            if variable_type is not None:
                self._values["variable_type"] = variable_type

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The event variable ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def created_time(self) -> typing.Optional[builtins.str]:
            '''Timestamp for when the event variable was created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-createdtime
            '''
            result = self._values.get("created_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_source(self) -> typing.Optional[builtins.str]:
            '''The data source of the event variable.

            Valid values: ``EVENT | EXTERNAL_MODEL_SCORE``

            When defining a variable within a detector, you can only use the ``EVENT`` value for DataSource when the *Inline* property is set to true. If the *Inline* property is set false, you can use either ``EVENT`` or ``MODEL_SCORE`` for DataSource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-datasource
            '''
            result = self._values.get("data_source")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_type(self) -> typing.Optional[builtins.str]:
            '''The data type of the event variable.

            Valid values: ``STRING | INTEGER | BOOLEAN | FLOAT``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-datatype
            '''
            result = self._values.get("data_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def default_value(self) -> typing.Optional[builtins.str]:
            '''The default value of the event variable.

            This is required if you are providing the details of your variables instead of the ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-defaultvalue
            '''
            result = self._values.get("default_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description of the event variable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inline(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the resource is defined within this CloudFormation template and impacts the create, update, and delete behavior of the stack.

            If the value is ``true`` , CloudFormation will create/update/delete the resource when creating/updating/deleting the stack. If the value is ``false`` , CloudFormation will validate that the object exists and then use it within the resource without making changes to the object.

            For example, when creating ``AWS::FraudDetector::Detector`` you must define at least two variables. You can set ``Inline=true`` for these variables and CloudFormation will create/update/delete the variables as part of stack operations. However, if you set ``Inline=false`` , CloudFormation will associate the variables to your detector but not execute any changes to the variables.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-inline
            '''
            result = self._values.get("inline")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def last_updated_time(self) -> typing.Optional[builtins.str]:
            '''Timestamp for when the event variable was last updated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-lastupdatedtime
            '''
            result = self._values.get("last_updated_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the event variable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
            '''An array of key-value pairs to apply to this resource.

            For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

        @builtins.property
        def variable_type(self) -> typing.Optional[builtins.str]:
            '''The type of event variable.

            For more information, see `Variable types <https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-eventvariable.html#cfn-frauddetector-detector-eventvariable-variabletype
            '''
            result = self._values.get("variable_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventVariableProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_frauddetector.CfnDetector.LabelProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "created_time": "createdTime",
            "description": "description",
            "inline": "inline",
            "last_updated_time": "lastUpdatedTime",
            "name": "name",
            "tags": "tags",
        },
    )
    class LabelProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            created_time: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            inline: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            last_updated_time: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The label details.

            :param arn: The label ARN.
            :param created_time: Timestamp of when the event type was created.
            :param description: The label description.
            :param inline: Indicates whether the resource is defined within this CloudFormation template and impacts the create, update, and delete behavior of the stack. If the value is ``true`` , CloudFormation will create/update/delete the resource when creating/updating/deleting the stack. If the value is ``false`` , CloudFormation will validate that the object exists and then use it within the resource without making changes to the object. For example, when creating ``AWS::FraudDetector::Detector`` you must define at least two variables. You can set ``Inline=true`` for these variables and CloudFormation will create/update/delete the variables as part of stack operations. However, if you set ``Inline=false`` , CloudFormation will associate the variables to your detector but not execute any changes to the variables.
            :param last_updated_time: Timestamp of when the label was last updated.
            :param name: The label name.
            :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_frauddetector as frauddetector
                
                label_property = frauddetector.CfnDetector.LabelProperty(
                    arn="arn",
                    created_time="createdTime",
                    description="description",
                    inline=False,
                    last_updated_time="lastUpdatedTime",
                    name="name",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6ae88d73256647a482ae1ad952813d8ef10946f1a7a7069dd4bb50626b592fa2)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument created_time", value=created_time, expected_type=type_hints["created_time"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument inline", value=inline, expected_type=type_hints["inline"])
                check_type(argname="argument last_updated_time", value=last_updated_time, expected_type=type_hints["last_updated_time"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if created_time is not None:
                self._values["created_time"] = created_time
            if description is not None:
                self._values["description"] = description
            if inline is not None:
                self._values["inline"] = inline
            if last_updated_time is not None:
                self._values["last_updated_time"] = last_updated_time
            if name is not None:
                self._values["name"] = name
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The label ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def created_time(self) -> typing.Optional[builtins.str]:
            '''Timestamp of when the event type was created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-createdtime
            '''
            result = self._values.get("created_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The label description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inline(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the resource is defined within this CloudFormation template and impacts the create, update, and delete behavior of the stack.

            If the value is ``true`` , CloudFormation will create/update/delete the resource when creating/updating/deleting the stack. If the value is ``false`` , CloudFormation will validate that the object exists and then use it within the resource without making changes to the object.

            For example, when creating ``AWS::FraudDetector::Detector`` you must define at least two variables. You can set ``Inline=true`` for these variables and CloudFormation will create/update/delete the variables as part of stack operations. However, if you set ``Inline=false`` , CloudFormation will associate the variables to your detector but not execute any changes to the variables.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-inline
            '''
            result = self._values.get("inline")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def last_updated_time(self) -> typing.Optional[builtins.str]:
            '''Timestamp of when the label was last updated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-lastupdatedtime
            '''
            result = self._values.get("last_updated_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The label name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
            '''An array of key-value pairs to apply to this resource.

            For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-label.html#cfn-frauddetector-detector-label-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LabelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_frauddetector.CfnDetector.ModelProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn"},
    )
    class ModelProperty:
        def __init__(self, *, arn: typing.Optional[builtins.str] = None) -> None:
            '''A model to associate with a detector.

            :param arn: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-model.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_frauddetector as frauddetector
                
                model_property = frauddetector.CfnDetector.ModelProperty(
                    arn="arn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a706373cb67d66c8702dcfd1e6f3496d5692fff02c37d6f866578375b8df4064)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-model.html#cfn-frauddetector-detector-model-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_frauddetector.CfnDetector.OutcomeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "created_time": "createdTime",
            "description": "description",
            "inline": "inline",
            "last_updated_time": "lastUpdatedTime",
            "name": "name",
            "tags": "tags",
        },
    )
    class OutcomeProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            created_time: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            inline: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            last_updated_time: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The outcome.

            :param arn: The outcome ARN.
            :param created_time: The timestamp when the outcome was created.
            :param description: The outcome description.
            :param inline: Indicates whether the resource is defined within this CloudFormation template and impacts the create, update, and delete behavior of the stack. If the value is ``true`` , CloudFormation will create/update/delete the resource when creating/updating/deleting the stack. If the value is ``false`` , CloudFormation will validate that the object exists and then use it within the resource without making changes to the object. For example, when creating ``AWS::FraudDetector::Detector`` you must define at least two variables. You can set ``Inline=true`` for these variables and CloudFormation will create/update/delete the variables as part of stack operations. However, if you set ``Inline=false`` , CloudFormation will associate the variables to your detector but not execute any changes to the variables.
            :param last_updated_time: The timestamp when the outcome was last updated.
            :param name: The outcome name.
            :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_frauddetector as frauddetector
                
                outcome_property = frauddetector.CfnDetector.OutcomeProperty(
                    arn="arn",
                    created_time="createdTime",
                    description="description",
                    inline=False,
                    last_updated_time="lastUpdatedTime",
                    name="name",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__42ab66224fc57d8de7d56e9f0b2377eac7bf49979a47fbe73eaa48e47147fc2d)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument created_time", value=created_time, expected_type=type_hints["created_time"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument inline", value=inline, expected_type=type_hints["inline"])
                check_type(argname="argument last_updated_time", value=last_updated_time, expected_type=type_hints["last_updated_time"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if created_time is not None:
                self._values["created_time"] = created_time
            if description is not None:
                self._values["description"] = description
            if inline is not None:
                self._values["inline"] = inline
            if last_updated_time is not None:
                self._values["last_updated_time"] = last_updated_time
            if name is not None:
                self._values["name"] = name
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The outcome ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def created_time(self) -> typing.Optional[builtins.str]:
            '''The timestamp when the outcome was created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-createdtime
            '''
            result = self._values.get("created_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The outcome description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inline(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the resource is defined within this CloudFormation template and impacts the create, update, and delete behavior of the stack.

            If the value is ``true`` , CloudFormation will create/update/delete the resource when creating/updating/deleting the stack. If the value is ``false`` , CloudFormation will validate that the object exists and then use it within the resource without making changes to the object.

            For example, when creating ``AWS::FraudDetector::Detector`` you must define at least two variables. You can set ``Inline=true`` for these variables and CloudFormation will create/update/delete the variables as part of stack operations. However, if you set ``Inline=false`` , CloudFormation will associate the variables to your detector but not execute any changes to the variables.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-inline
            '''
            result = self._values.get("inline")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def last_updated_time(self) -> typing.Optional[builtins.str]:
            '''The timestamp when the outcome was last updated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-lastupdatedtime
            '''
            result = self._values.get("last_updated_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The outcome name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
            '''An array of key-value pairs to apply to this resource.

            For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-outcome.html#cfn-frauddetector-detector-outcome-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutcomeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_frauddetector.CfnDetector.RuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "created_time": "createdTime",
            "description": "description",
            "detector_id": "detectorId",
            "expression": "expression",
            "language": "language",
            "last_updated_time": "lastUpdatedTime",
            "outcomes": "outcomes",
            "rule_id": "ruleId",
            "rule_version": "ruleVersion",
            "tags": "tags",
        },
    )
    class RuleProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            created_time: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            detector_id: typing.Optional[builtins.str] = None,
            expression: typing.Optional[builtins.str] = None,
            language: typing.Optional[builtins.str] = None,
            last_updated_time: typing.Optional[builtins.str] = None,
            outcomes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDetector.OutcomeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            rule_id: typing.Optional[builtins.str] = None,
            rule_version: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A rule.

            Rule is a condition that tells Amazon Fraud Detector how to interpret variables values during a fraud prediction.

            :param arn: The rule ARN.
            :param created_time: Timestamp for when the rule was created.
            :param description: The rule description.
            :param detector_id: The detector for which the rule is associated.
            :param expression: The rule expression. A rule expression captures the business logic. For more information, see `Rule language reference <https://docs.aws.amazon.com/frauddetector/latest/ug/rule-language-reference.html>`_ .
            :param language: The rule language.
            :param last_updated_time: Timestamp for when the rule was last updated.
            :param outcomes: The rule outcome.
            :param rule_id: The rule ID.
            :param rule_version: The rule version.
            :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_frauddetector as frauddetector
                
                rule_property = frauddetector.CfnDetector.RuleProperty(
                    arn="arn",
                    created_time="createdTime",
                    description="description",
                    detector_id="detectorId",
                    expression="expression",
                    language="language",
                    last_updated_time="lastUpdatedTime",
                    outcomes=[frauddetector.CfnDetector.OutcomeProperty(
                        arn="arn",
                        created_time="createdTime",
                        description="description",
                        inline=False,
                        last_updated_time="lastUpdatedTime",
                        name="name",
                        tags=[CfnTag(
                            key="key",
                            value="value"
                        )]
                    )],
                    rule_id="ruleId",
                    rule_version="ruleVersion",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__96e64cb156d83b6e85aee19c2adb7af17ac591c47655e3b1f709434834ff8e16)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument created_time", value=created_time, expected_type=type_hints["created_time"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument detector_id", value=detector_id, expected_type=type_hints["detector_id"])
                check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
                check_type(argname="argument language", value=language, expected_type=type_hints["language"])
                check_type(argname="argument last_updated_time", value=last_updated_time, expected_type=type_hints["last_updated_time"])
                check_type(argname="argument outcomes", value=outcomes, expected_type=type_hints["outcomes"])
                check_type(argname="argument rule_id", value=rule_id, expected_type=type_hints["rule_id"])
                check_type(argname="argument rule_version", value=rule_version, expected_type=type_hints["rule_version"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if created_time is not None:
                self._values["created_time"] = created_time
            if description is not None:
                self._values["description"] = description
            if detector_id is not None:
                self._values["detector_id"] = detector_id
            if expression is not None:
                self._values["expression"] = expression
            if language is not None:
                self._values["language"] = language
            if last_updated_time is not None:
                self._values["last_updated_time"] = last_updated_time
            if outcomes is not None:
                self._values["outcomes"] = outcomes
            if rule_id is not None:
                self._values["rule_id"] = rule_id
            if rule_version is not None:
                self._values["rule_version"] = rule_version
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The rule ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def created_time(self) -> typing.Optional[builtins.str]:
            '''Timestamp for when the rule was created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-createdtime
            '''
            result = self._values.get("created_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The rule description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def detector_id(self) -> typing.Optional[builtins.str]:
            '''The detector for which the rule is associated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-detectorid
            '''
            result = self._values.get("detector_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def expression(self) -> typing.Optional[builtins.str]:
            '''The rule expression.

            A rule expression captures the business logic. For more information, see `Rule language reference <https://docs.aws.amazon.com/frauddetector/latest/ug/rule-language-reference.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-expression
            '''
            result = self._values.get("expression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def language(self) -> typing.Optional[builtins.str]:
            '''The rule language.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-language
            '''
            result = self._values.get("language")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def last_updated_time(self) -> typing.Optional[builtins.str]:
            '''Timestamp for when the rule was last updated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-lastupdatedtime
            '''
            result = self._values.get("last_updated_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def outcomes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetector.OutcomeProperty"]]]]:
            '''The rule outcome.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-outcomes
            '''
            result = self._values.get("outcomes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDetector.OutcomeProperty"]]]], result)

        @builtins.property
        def rule_id(self) -> typing.Optional[builtins.str]:
            '''The rule ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-ruleid
            '''
            result = self._values.get("rule_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def rule_version(self) -> typing.Optional[builtins.str]:
            '''The rule version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-ruleversion
            '''
            result = self._values.get("rule_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
            '''An array of key-value pairs to apply to this resource.

            For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-detector-rule.html#cfn-frauddetector-detector-rule-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_frauddetector.CfnDetectorProps",
    jsii_struct_bases=[],
    name_mapping={
        "detector_id": "detectorId",
        "event_type": "eventType",
        "rules": "rules",
        "associated_models": "associatedModels",
        "description": "description",
        "detector_version_status": "detectorVersionStatus",
        "rule_execution_mode": "ruleExecutionMode",
        "tags": "tags",
    },
)
class CfnDetectorProps:
    def __init__(
        self,
        *,
        detector_id: builtins.str,
        event_type: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetector.EventTypeProperty, typing.Dict[builtins.str, typing.Any]]],
        rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetector.RuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
        associated_models: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetector.ModelProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        detector_version_status: typing.Optional[builtins.str] = None,
        rule_execution_mode: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDetector``.

        :param detector_id: The name of the detector.
        :param event_type: The event type associated with this detector.
        :param rules: The rules to include in the detector version.
        :param associated_models: The models to associate with this detector. You must provide the ARNs of all the models you want to associate.
        :param description: The detector description.
        :param detector_version_status: The status of the detector version. If a value is not provided for this property, AWS CloudFormation assumes ``DRAFT`` status. Valid values: ``ACTIVE | DRAFT``
        :param rule_execution_mode: The rule execution mode for the rules included in the detector version. Valid values: ``FIRST_MATCHED | ALL_MATCHED`` Default value: ``FIRST_MATCHED`` You can define and edit the rule mode at the detector version level, when it is in draft status. If you specify ``FIRST_MATCHED`` , Amazon Fraud Detector evaluates rules sequentially, first to last, stopping at the first matched rule. Amazon Fraud dectector then provides the outcomes for that single rule. If you specifiy ``ALL_MATCHED`` , Amazon Fraud Detector evaluates all rules and returns the outcomes for all matched rules.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_frauddetector as frauddetector
            
            cfn_detector_props = frauddetector.CfnDetectorProps(
                detector_id="detectorId",
                event_type=frauddetector.CfnDetector.EventTypeProperty(
                    arn="arn",
                    created_time="createdTime",
                    description="description",
                    entity_types=[frauddetector.CfnDetector.EntityTypeProperty(
                        arn="arn",
                        created_time="createdTime",
                        description="description",
                        inline=False,
                        last_updated_time="lastUpdatedTime",
                        name="name",
                        tags=[CfnTag(
                            key="key",
                            value="value"
                        )]
                    )],
                    event_variables=[frauddetector.CfnDetector.EventVariableProperty(
                        arn="arn",
                        created_time="createdTime",
                        data_source="dataSource",
                        data_type="dataType",
                        default_value="defaultValue",
                        description="description",
                        inline=False,
                        last_updated_time="lastUpdatedTime",
                        name="name",
                        tags=[CfnTag(
                            key="key",
                            value="value"
                        )],
                        variable_type="variableType"
                    )],
                    inline=False,
                    labels=[frauddetector.CfnDetector.LabelProperty(
                        arn="arn",
                        created_time="createdTime",
                        description="description",
                        inline=False,
                        last_updated_time="lastUpdatedTime",
                        name="name",
                        tags=[CfnTag(
                            key="key",
                            value="value"
                        )]
                    )],
                    last_updated_time="lastUpdatedTime",
                    name="name",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                ),
                rules=[frauddetector.CfnDetector.RuleProperty(
                    arn="arn",
                    created_time="createdTime",
                    description="description",
                    detector_id="detectorId",
                    expression="expression",
                    language="language",
                    last_updated_time="lastUpdatedTime",
                    outcomes=[frauddetector.CfnDetector.OutcomeProperty(
                        arn="arn",
                        created_time="createdTime",
                        description="description",
                        inline=False,
                        last_updated_time="lastUpdatedTime",
                        name="name",
                        tags=[CfnTag(
                            key="key",
                            value="value"
                        )]
                    )],
                    rule_id="ruleId",
                    rule_version="ruleVersion",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )],
            
                # the properties below are optional
                associated_models=[frauddetector.CfnDetector.ModelProperty(
                    arn="arn"
                )],
                description="description",
                detector_version_status="detectorVersionStatus",
                rule_execution_mode="ruleExecutionMode",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b26e6685891f22272eaba159af0e6c7023d53e7080f932711c9d37ff7d04a215)
            check_type(argname="argument detector_id", value=detector_id, expected_type=type_hints["detector_id"])
            check_type(argname="argument event_type", value=event_type, expected_type=type_hints["event_type"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            check_type(argname="argument associated_models", value=associated_models, expected_type=type_hints["associated_models"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument detector_version_status", value=detector_version_status, expected_type=type_hints["detector_version_status"])
            check_type(argname="argument rule_execution_mode", value=rule_execution_mode, expected_type=type_hints["rule_execution_mode"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "detector_id": detector_id,
            "event_type": event_type,
            "rules": rules,
        }
        if associated_models is not None:
            self._values["associated_models"] = associated_models
        if description is not None:
            self._values["description"] = description
        if detector_version_status is not None:
            self._values["detector_version_status"] = detector_version_status
        if rule_execution_mode is not None:
            self._values["rule_execution_mode"] = rule_execution_mode
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''The name of the detector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-detectorid
        '''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_type(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnDetector.EventTypeProperty]:
        '''The event type associated with this detector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-eventtype
        '''
        result = self._values.get("event_type")
        assert result is not None, "Required property 'event_type' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnDetector.EventTypeProperty], result)

    @builtins.property
    def rules(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDetector.RuleProperty]]]:
        '''The rules to include in the detector version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-rules
        '''
        result = self._values.get("rules")
        assert result is not None, "Required property 'rules' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDetector.RuleProperty]]], result)

    @builtins.property
    def associated_models(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDetector.ModelProperty]]]]:
        '''The models to associate with this detector.

        You must provide the ARNs of all the models you want to associate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-associatedmodels
        '''
        result = self._values.get("associated_models")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDetector.ModelProperty]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The detector description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def detector_version_status(self) -> typing.Optional[builtins.str]:
        '''The status of the detector version.

        If a value is not provided for this property, AWS CloudFormation assumes ``DRAFT`` status.

        Valid values: ``ACTIVE | DRAFT``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-detectorversionstatus
        '''
        result = self._values.get("detector_version_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule_execution_mode(self) -> typing.Optional[builtins.str]:
        '''The rule execution mode for the rules included in the detector version.

        Valid values: ``FIRST_MATCHED | ALL_MATCHED`` Default value: ``FIRST_MATCHED``

        You can define and edit the rule mode at the detector version level, when it is in draft status.

        If you specify ``FIRST_MATCHED`` , Amazon Fraud Detector evaluates rules sequentially, first to last, stopping at the first matched rule. Amazon Fraud dectector then provides the outcomes for that single rule.

        If you specifiy ``ALL_MATCHED`` , Amazon Fraud Detector evaluates all rules and returns the outcomes for all matched rules.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-ruleexecutionmode
        '''
        result = self._values.get("rule_execution_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-detector.html#cfn-frauddetector-detector-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDetectorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnEntityType(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_frauddetector.CfnEntityType",
):
    '''Manages an entity type.

    An entity represents who is performing the event. As part of a fraud prediction, you pass the entity ID to indicate the specific entity who performed the event. An entity type classifies the entity. Example classifications include customer, merchant, or account.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-entitytype.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_frauddetector as frauddetector
        
        cfn_entity_type = frauddetector.CfnEntityType(self, "MyCfnEntityType",
            name="name",
        
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
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The entity type name. Pattern: ``^[0-9a-z_-]+$``
        :param description: The entity type description.
        :param tags: A key and value pair.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8bdfff4b2494486b1323350204c3429d0cd5e0c80cabaf21c7bf35893425d91)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEntityTypeProps(name=name, description=description, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1571c030c1f4eceb1eb429ce5e6aaa422cdd95b3620386f3e677d18030367fb2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e90300025950c0b81e217590ea856c2de60466ae1e258aa64dc945d2f6983de8)
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
        '''The entity type ARN.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''Timestamp of when entity type was created.

        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedTime")
    def attr_last_updated_time(self) -> builtins.str:
        '''Timestamp of when entity type was last updated.

        :cloudformationAttribute: LastUpdatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedTime"))

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
        '''The entity type name.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4992eda023f70fa90ab8a63e1125df15b3f02044513bf8a3d42d050330d13384)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The entity type description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4d2cecbe3561f37b9476c54f24e4f9ac5facd631897c1b90a00416d99a82254)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A key and value pair.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c909dc2ea7c1434dc4017053808f37d5041edd5e473826f0152aff8c19dd4d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_frauddetector.CfnEntityTypeProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "description": "description", "tags": "tags"},
)
class CfnEntityTypeProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEntityType``.

        :param name: The entity type name. Pattern: ``^[0-9a-z_-]+$``
        :param description: The entity type description.
        :param tags: A key and value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-entitytype.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_frauddetector as frauddetector
            
            cfn_entity_type_props = frauddetector.CfnEntityTypeProps(
                name="name",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0af61baf6c2e5424876fd48cdd930b1c05c66d9e45088e51b8c3775c6a209dfc)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The entity type name.

        Pattern: ``^[0-9a-z_-]+$``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-entitytype.html#cfn-frauddetector-entitytype-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The entity type description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-entitytype.html#cfn-frauddetector-entitytype-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A key and value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-entitytype.html#cfn-frauddetector-entitytype-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEntityTypeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnEventType(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_frauddetector.CfnEventType",
):
    '''Manages an event type.

    An event is a business activity that is evaluated for fraud risk. With Amazon Fraud Detector, you generate fraud predictions for events. An event type defines the structure for an event sent to Amazon Fraud Detector. This includes the variables sent as part of the event, the entity performing the event (such as a customer), and the labels that classify the event. Example event types include online payment transactions, account registrations, and authentications.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_frauddetector as frauddetector
        
        cfn_event_type = frauddetector.CfnEventType(self, "MyCfnEventType",
            entity_types=[frauddetector.CfnEventType.EntityTypeProperty(
                arn="arn",
                created_time="createdTime",
                description="description",
                inline=False,
                last_updated_time="lastUpdatedTime",
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )],
            event_variables=[frauddetector.CfnEventType.EventVariableProperty(
                arn="arn",
                created_time="createdTime",
                data_source="dataSource",
                data_type="dataType",
                default_value="defaultValue",
                description="description",
                inline=False,
                last_updated_time="lastUpdatedTime",
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                variable_type="variableType"
            )],
            labels=[frauddetector.CfnEventType.LabelProperty(
                arn="arn",
                created_time="createdTime",
                description="description",
                inline=False,
                last_updated_time="lastUpdatedTime",
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )],
            name="name",
        
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
        entity_types: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEventType.EntityTypeProperty", typing.Dict[builtins.str, typing.Any]]]]],
        event_variables: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEventType.EventVariableProperty", typing.Dict[builtins.str, typing.Any]]]]],
        labels: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEventType.LabelProperty", typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param entity_types: The event type entity types.
        :param event_variables: The event type event variables.
        :param labels: The event type labels.
        :param name: The event type name. Pattern : ``^[0-9a-z_-]+$``
        :param description: The event type description.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__451d211f5cf761d7405bdc87e43ae39817ac3300cbc123e9dee6bf9c666c41d6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEventTypeProps(
            entity_types=entity_types,
            event_variables=event_variables,
            labels=labels,
            name=name,
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
            type_hints = typing.get_type_hints(_typecheckingstub__57073e537e1028dc4fd6dd2f1ad4592226f5ca14432d451af056c7fba3486a89)
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
            type_hints = typing.get_type_hints(_typecheckingstub__896e3b720206ace186a02ffaedea2e54f15b7ffb2309deee514062d40406c174)
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
        '''The event type ARN.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''Timestamp of when event type was created.

        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedTime")
    def attr_last_updated_time(self) -> builtins.str:
        '''Timestamp of when event type was last updated.

        :cloudformationAttribute: LastUpdatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedTime"))

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
    @jsii.member(jsii_name="entityTypes")
    def entity_types(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventType.EntityTypeProperty"]]]:
        '''The event type entity types.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventType.EntityTypeProperty"]]], jsii.get(self, "entityTypes"))

    @entity_types.setter
    def entity_types(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventType.EntityTypeProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53bb265a6c55aad83b33927c1087b3e8bc522ccd1d14bcfd6782272dff526d11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entityTypes", value)

    @builtins.property
    @jsii.member(jsii_name="eventVariables")
    def event_variables(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventType.EventVariableProperty"]]]:
        '''The event type event variables.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventType.EventVariableProperty"]]], jsii.get(self, "eventVariables"))

    @event_variables.setter
    def event_variables(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventType.EventVariableProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__069acb584ea2685e6dec07d73d0d6962da831960b0309eee686ac2523e72d972)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventVariables", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventType.LabelProperty"]]]:
        '''The event type labels.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventType.LabelProperty"]]], jsii.get(self, "labels"))

    @labels.setter
    def labels(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEventType.LabelProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__365faaa83e644ceabaa6459d7b1a94dc88c201e84990388c642c666254e5beb4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The event type name.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82fef4b211d5ec66774645b2ecfcc0adb17643d3060cb14cdf95896b0fd3a8f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The event type description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1631a2144130626280154fffd9661dcd8519a2076fc0261481b4ea14ba4dc7e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5422e1150c24f0251536c92e0de44a7dd468b252c7e492f7885af852df4a03d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_frauddetector.CfnEventType.EntityTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "created_time": "createdTime",
            "description": "description",
            "inline": "inline",
            "last_updated_time": "lastUpdatedTime",
            "name": "name",
            "tags": "tags",
        },
    )
    class EntityTypeProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            created_time: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            inline: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            last_updated_time: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The entity type details.

            :param arn: The entity type ARN.
            :param created_time: Timestamp of when the entity type was created.
            :param description: The entity type description.
            :param inline: Indicates whether the resource is defined within this CloudFormation template and impacts the create, update, and delete behavior of the stack. If the value is ``true`` , CloudFormation will create/update/delete the resource when creating/updating/deleting the stack. If the value is ``false`` , CloudFormation will validate that the object exists and then use it within the resource without making changes to the object. For example, when creating ``AWS::FraudDetector::EventType`` you must define at least two variables. You can set ``Inline=true`` for these variables and CloudFormation will create/update/delete the variables as part of stack operations. However, if you set ``Inline=false`` , CloudFormation will associate the variables to your event type but not execute any changes to the variables.
            :param last_updated_time: Timestamp of when the entity type was last updated.
            :param name: The entity type name. ``^[0-9a-z_-]+$``
            :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_frauddetector as frauddetector
                
                entity_type_property = frauddetector.CfnEventType.EntityTypeProperty(
                    arn="arn",
                    created_time="createdTime",
                    description="description",
                    inline=False,
                    last_updated_time="lastUpdatedTime",
                    name="name",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__260ae8e52abed94a34c34efe87ffa1a80dd84c9261659e66aaf7d4643c3901dc)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument created_time", value=created_time, expected_type=type_hints["created_time"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument inline", value=inline, expected_type=type_hints["inline"])
                check_type(argname="argument last_updated_time", value=last_updated_time, expected_type=type_hints["last_updated_time"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if created_time is not None:
                self._values["created_time"] = created_time
            if description is not None:
                self._values["description"] = description
            if inline is not None:
                self._values["inline"] = inline
            if last_updated_time is not None:
                self._values["last_updated_time"] = last_updated_time
            if name is not None:
                self._values["name"] = name
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The entity type ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def created_time(self) -> typing.Optional[builtins.str]:
            '''Timestamp of when the entity type was created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-createdtime
            '''
            result = self._values.get("created_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The entity type description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inline(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the resource is defined within this CloudFormation template and impacts the create, update, and delete behavior of the stack.

            If the value is ``true`` , CloudFormation will create/update/delete the resource when creating/updating/deleting the stack. If the value is ``false`` , CloudFormation will validate that the object exists and then use it within the resource without making changes to the object.

            For example, when creating ``AWS::FraudDetector::EventType`` you must define at least two variables. You can set ``Inline=true`` for these variables and CloudFormation will create/update/delete the variables as part of stack operations. However, if you set ``Inline=false`` , CloudFormation will associate the variables to your event type but not execute any changes to the variables.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-inline
            '''
            result = self._values.get("inline")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def last_updated_time(self) -> typing.Optional[builtins.str]:
            '''Timestamp of when the entity type was last updated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-lastupdatedtime
            '''
            result = self._values.get("last_updated_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The entity type name.

            ``^[0-9a-z_-]+$``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
            '''An array of key-value pairs to apply to this resource.

            For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-entitytype.html#cfn-frauddetector-eventtype-entitytype-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EntityTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_frauddetector.CfnEventType.EventVariableProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "created_time": "createdTime",
            "data_source": "dataSource",
            "data_type": "dataType",
            "default_value": "defaultValue",
            "description": "description",
            "inline": "inline",
            "last_updated_time": "lastUpdatedTime",
            "name": "name",
            "tags": "tags",
            "variable_type": "variableType",
        },
    )
    class EventVariableProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            created_time: typing.Optional[builtins.str] = None,
            data_source: typing.Optional[builtins.str] = None,
            data_type: typing.Optional[builtins.str] = None,
            default_value: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            inline: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            last_updated_time: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
            variable_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The variables associated with this event type.

            :param arn: The event variable ARN.
            :param created_time: Timestamp for when event variable was created.
            :param data_source: The source of the event variable. Valid values: ``EVENT | EXTERNAL_MODEL_SCORE`` When defining a variable within a event type, you can only use the ``EVENT`` value for DataSource when the *Inline* property is set to true. If the *Inline* property is set false, you can use either ``EVENT`` or ``MODEL_SCORE`` for DataSource.
            :param data_type: The data type of the event variable. For more information, see `Data types <https://docs.aws.amazon.com/frauddetector/latest/ug/variables.html#data-types>`_ .
            :param default_value: The default value of the event variable.
            :param description: The event variable description.
            :param inline: Indicates whether the resource is defined within this CloudFormation template and impacts the create, update, and delete behavior of the stack. If the value is ``true`` , CloudFormation will create/update/delete the resource when creating/updating/deleting the stack. If the value is ``false`` , CloudFormation will validate that the object exists and then use it within the resource without making changes to the object. For example, when creating ``AWS::FraudDetector::EventType`` you must define at least two variables. You can set ``Inline=true`` for these variables and CloudFormation will create/update/delete the Variables as part of stack operations. However, if you set ``Inline=false`` , CloudFormation will associate the variables to your event type but not execute any changes to the variables.
            :param last_updated_time: Timestamp for when the event variable was last updated.
            :param name: The name of the event variable.
            :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
            :param variable_type: The type of event variable. For more information, see `Variable types <https://docs.aws.amazon.com/frauddetector/latest/ug/variables.html#variable-types>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_frauddetector as frauddetector
                
                event_variable_property = frauddetector.CfnEventType.EventVariableProperty(
                    arn="arn",
                    created_time="createdTime",
                    data_source="dataSource",
                    data_type="dataType",
                    default_value="defaultValue",
                    description="description",
                    inline=False,
                    last_updated_time="lastUpdatedTime",
                    name="name",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )],
                    variable_type="variableType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1cd57942d76cc854fe9f0ec8b954232ad9c483611dacb6c78b25da731de022eb)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument created_time", value=created_time, expected_type=type_hints["created_time"])
                check_type(argname="argument data_source", value=data_source, expected_type=type_hints["data_source"])
                check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
                check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument inline", value=inline, expected_type=type_hints["inline"])
                check_type(argname="argument last_updated_time", value=last_updated_time, expected_type=type_hints["last_updated_time"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
                check_type(argname="argument variable_type", value=variable_type, expected_type=type_hints["variable_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if created_time is not None:
                self._values["created_time"] = created_time
            if data_source is not None:
                self._values["data_source"] = data_source
            if data_type is not None:
                self._values["data_type"] = data_type
            if default_value is not None:
                self._values["default_value"] = default_value
            if description is not None:
                self._values["description"] = description
            if inline is not None:
                self._values["inline"] = inline
            if last_updated_time is not None:
                self._values["last_updated_time"] = last_updated_time
            if name is not None:
                self._values["name"] = name
            if tags is not None:
                self._values["tags"] = tags
            if variable_type is not None:
                self._values["variable_type"] = variable_type

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The event variable ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def created_time(self) -> typing.Optional[builtins.str]:
            '''Timestamp for when event variable was created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-createdtime
            '''
            result = self._values.get("created_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_source(self) -> typing.Optional[builtins.str]:
            '''The source of the event variable.

            Valid values: ``EVENT | EXTERNAL_MODEL_SCORE``

            When defining a variable within a event type, you can only use the ``EVENT`` value for DataSource when the *Inline* property is set to true. If the *Inline* property is set false, you can use either ``EVENT`` or ``MODEL_SCORE`` for DataSource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-datasource
            '''
            result = self._values.get("data_source")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_type(self) -> typing.Optional[builtins.str]:
            '''The data type of the event variable.

            For more information, see `Data types <https://docs.aws.amazon.com/frauddetector/latest/ug/variables.html#data-types>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-datatype
            '''
            result = self._values.get("data_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def default_value(self) -> typing.Optional[builtins.str]:
            '''The default value of the event variable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-defaultvalue
            '''
            result = self._values.get("default_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The event variable description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inline(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the resource is defined within this CloudFormation template and impacts the create, update, and delete behavior of the stack.

            If the value is ``true`` , CloudFormation will create/update/delete the resource when creating/updating/deleting the stack. If the value is ``false`` , CloudFormation will validate that the object exists and then use it within the resource without making changes to the object.

            For example, when creating ``AWS::FraudDetector::EventType`` you must define at least two variables. You can set ``Inline=true`` for these variables and CloudFormation will create/update/delete the Variables as part of stack operations. However, if you set ``Inline=false`` , CloudFormation will associate the variables to your event type but not execute any changes to the variables.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-inline
            '''
            result = self._values.get("inline")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def last_updated_time(self) -> typing.Optional[builtins.str]:
            '''Timestamp for when the event variable was last updated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-lastupdatedtime
            '''
            result = self._values.get("last_updated_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the event variable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
            '''An array of key-value pairs to apply to this resource.

            For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

        @builtins.property
        def variable_type(self) -> typing.Optional[builtins.str]:
            '''The type of event variable.

            For more information, see `Variable types <https://docs.aws.amazon.com/frauddetector/latest/ug/variables.html#variable-types>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-eventvariable.html#cfn-frauddetector-eventtype-eventvariable-variabletype
            '''
            result = self._values.get("variable_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventVariableProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_frauddetector.CfnEventType.LabelProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "created_time": "createdTime",
            "description": "description",
            "inline": "inline",
            "last_updated_time": "lastUpdatedTime",
            "name": "name",
            "tags": "tags",
        },
    )
    class LabelProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            created_time: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            inline: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            last_updated_time: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The label associated with the event type.

            :param arn: The label ARN.
            :param created_time: Timestamp of when the event type was created.
            :param description: The label description.
            :param inline: Indicates whether the resource is defined within this CloudFormation template and impacts the create, update, and delete behavior of the stack. If the value is ``true`` , CloudFormation will create/update/delete the resource when creating/updating/deleting the stack. If the value is ``false`` , CloudFormation will validate that the object exists and then use it within the resource without making changes to the object. For example, when creating ``AWS::FraudDetector::EventType`` you must define at least two variables. You can set ``Inline=true`` for these variables and CloudFormation will create/update/delete the variables as part of stack operations. However, if you set ``Inline=false`` , CloudFormation will associate the variables to your EventType but not execute any changes to the variables.
            :param last_updated_time: Timestamp of when the label was last updated.
            :param name: The label name.
            :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_frauddetector as frauddetector
                
                label_property = frauddetector.CfnEventType.LabelProperty(
                    arn="arn",
                    created_time="createdTime",
                    description="description",
                    inline=False,
                    last_updated_time="lastUpdatedTime",
                    name="name",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8e8447a99b85327953986a476104b222d330a3ac72c6452bc91cb9a365efc593)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument created_time", value=created_time, expected_type=type_hints["created_time"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument inline", value=inline, expected_type=type_hints["inline"])
                check_type(argname="argument last_updated_time", value=last_updated_time, expected_type=type_hints["last_updated_time"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if created_time is not None:
                self._values["created_time"] = created_time
            if description is not None:
                self._values["description"] = description
            if inline is not None:
                self._values["inline"] = inline
            if last_updated_time is not None:
                self._values["last_updated_time"] = last_updated_time
            if name is not None:
                self._values["name"] = name
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The label ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def created_time(self) -> typing.Optional[builtins.str]:
            '''Timestamp of when the event type was created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-createdtime
            '''
            result = self._values.get("created_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The label description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inline(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the resource is defined within this CloudFormation template and impacts the create, update, and delete behavior of the stack.

            If the value is ``true`` , CloudFormation will create/update/delete the resource when creating/updating/deleting the stack. If the value is ``false`` , CloudFormation will validate that the object exists and then use it within the resource without making changes to the object.

            For example, when creating ``AWS::FraudDetector::EventType`` you must define at least two variables. You can set ``Inline=true`` for these variables and CloudFormation will create/update/delete the variables as part of stack operations. However, if you set ``Inline=false`` , CloudFormation will associate the variables to your EventType but not execute any changes to the variables.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-inline
            '''
            result = self._values.get("inline")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def last_updated_time(self) -> typing.Optional[builtins.str]:
            '''Timestamp of when the label was last updated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-lastupdatedtime
            '''
            result = self._values.get("last_updated_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The label name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
            '''An array of key-value pairs to apply to this resource.

            For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-frauddetector-eventtype-label.html#cfn-frauddetector-eventtype-label-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LabelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_frauddetector.CfnEventTypeProps",
    jsii_struct_bases=[],
    name_mapping={
        "entity_types": "entityTypes",
        "event_variables": "eventVariables",
        "labels": "labels",
        "name": "name",
        "description": "description",
        "tags": "tags",
    },
)
class CfnEventTypeProps:
    def __init__(
        self,
        *,
        entity_types: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventType.EntityTypeProperty, typing.Dict[builtins.str, typing.Any]]]]],
        event_variables: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventType.EventVariableProperty, typing.Dict[builtins.str, typing.Any]]]]],
        labels: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventType.LabelProperty, typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEventType``.

        :param entity_types: The event type entity types.
        :param event_variables: The event type event variables.
        :param labels: The event type labels.
        :param name: The event type name. Pattern : ``^[0-9a-z_-]+$``
        :param description: The event type description.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_frauddetector as frauddetector
            
            cfn_event_type_props = frauddetector.CfnEventTypeProps(
                entity_types=[frauddetector.CfnEventType.EntityTypeProperty(
                    arn="arn",
                    created_time="createdTime",
                    description="description",
                    inline=False,
                    last_updated_time="lastUpdatedTime",
                    name="name",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )],
                event_variables=[frauddetector.CfnEventType.EventVariableProperty(
                    arn="arn",
                    created_time="createdTime",
                    data_source="dataSource",
                    data_type="dataType",
                    default_value="defaultValue",
                    description="description",
                    inline=False,
                    last_updated_time="lastUpdatedTime",
                    name="name",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )],
                    variable_type="variableType"
                )],
                labels=[frauddetector.CfnEventType.LabelProperty(
                    arn="arn",
                    created_time="createdTime",
                    description="description",
                    inline=False,
                    last_updated_time="lastUpdatedTime",
                    name="name",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )],
                name="name",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e56a177c70c9bd1f38e708e145e3e6914e7a4d5bd3fed7466de6c3948aadabb7)
            check_type(argname="argument entity_types", value=entity_types, expected_type=type_hints["entity_types"])
            check_type(argname="argument event_variables", value=event_variables, expected_type=type_hints["event_variables"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "entity_types": entity_types,
            "event_variables": event_variables,
            "labels": labels,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def entity_types(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEventType.EntityTypeProperty]]]:
        '''The event type entity types.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-entitytypes
        '''
        result = self._values.get("entity_types")
        assert result is not None, "Required property 'entity_types' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEventType.EntityTypeProperty]]], result)

    @builtins.property
    def event_variables(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEventType.EventVariableProperty]]]:
        '''The event type event variables.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-eventvariables
        '''
        result = self._values.get("event_variables")
        assert result is not None, "Required property 'event_variables' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEventType.EventVariableProperty]]], result)

    @builtins.property
    def labels(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEventType.LabelProperty]]]:
        '''The event type labels.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-labels
        '''
        result = self._values.get("labels")
        assert result is not None, "Required property 'labels' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEventType.LabelProperty]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The event type name.

        Pattern : ``^[0-9a-z_-]+$``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The event type description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-eventtype.html#cfn-frauddetector-eventtype-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEventTypeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnLabel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_frauddetector.CfnLabel",
):
    '''Creates or updates label.

    A label classifies an event as fraudulent or legitimate. Labels are associated with event types and used to train supervised machine learning models in Amazon Fraud Detector.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_frauddetector as frauddetector
        
        cfn_label = frauddetector.CfnLabel(self, "MyCfnLabel",
            name="name",
        
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
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The label name. Pattern: ``^[0-9a-z_-]+$``
        :param description: The label description.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0a39e2a13e05950403b56b1af577d5a68139a2ca929eeb8d317f4d63405fde3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLabelProps(name=name, description=description, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__846d8694c0a1fb75a9d878596433171417933948ad87217108fadef702e46ad8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d1a7441e5b98737591872f05b12f252f5415e6a715918c761449c806ae1099e7)
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
        '''The ARN of the label.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''Timestamp of when label was created.

        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedTime")
    def attr_last_updated_time(self) -> builtins.str:
        '''Timestamp of when label was last updated.

        :cloudformationAttribute: LastUpdatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedTime"))

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
        '''The label name.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ea021d0099cd26ef1cb4651c8822d8793e2aab1e73ebec481a5dae4ce829dd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The label description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c12115fd0f9077627c47abee3df17f7273449232e8f344399b245e1d4b7d390)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cefa25d3e293c90a44bfae875532dea0458ac7bfc5ab23042df6edd882e48f79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_frauddetector.CfnLabelProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "description": "description", "tags": "tags"},
)
class CfnLabelProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLabel``.

        :param name: The label name. Pattern: ``^[0-9a-z_-]+$``
        :param description: The label description.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_frauddetector as frauddetector
            
            cfn_label_props = frauddetector.CfnLabelProps(
                name="name",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e644e14f734aefd7f5a6a211ec9822cd9accb53cdd0c619b609b777f094ef91)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The label name.

        Pattern: ``^[0-9a-z_-]+$``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#cfn-frauddetector-label-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The label description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#cfn-frauddetector-label-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-label.html#cfn-frauddetector-label-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLabelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnList(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_frauddetector.CfnList",
):
    '''Creates a list.

    List is a set of input data for a variable in your event dataset. You use the input data in a rule that's associated with your detector. For more information, see `Lists <https://docs.aws.amazon.com//frauddetector/latest/ug/lists.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-list.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_frauddetector as frauddetector
        
        cfn_list = frauddetector.CfnList(self, "MyCfnList",
            name="name",
        
            # the properties below are optional
            description="description",
            elements=["elements"],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            variable_type="variableType"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        elements: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        variable_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the list.
        :param description: The description of the list.
        :param elements: The elements in the list.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param variable_type: The variable type of the list. For more information, see `Variable types <https://docs.aws.amazon.com/frauddetector/latest/ug/variables.html#variable-types>`_
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7557a1eddb9d179a34bcf99a7e13b5784e8e399dc50d632a1a35e6f33559ea7d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnListProps(
            name=name,
            description=description,
            elements=elements,
            tags=tags,
            variable_type=variable_type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f20630db82ff99ed16fe5ef965c2bf119b32d566ed397567e0518858f3b5f77a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bdf9b84448c9e22dcf579028df053d7f0e5d5dbed871fe7de3e9d5260be30ec9)
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
        '''The event type ARN.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''Timestamp of when the list was created.

        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedTime")
    def attr_last_updated_time(self) -> builtins.str:
        '''Timestamp of when list was last updated.

        :cloudformationAttribute: LastUpdatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedTime"))

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
        '''The name of the list.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c6ee22c1cf4c2004cdf89f5026d17232a07a5ebd4c0aa403bd83359e16aaafc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the list.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9fdbb1b05780a5faadf8389814bef11ff7e42925b05617d4c87c0ff3f6e7d77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="elements")
    def elements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The elements in the list.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "elements"))

    @elements.setter
    def elements(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7030c8c92588018f78dd92396b547b788d9226b270fef8398bfb9791e29b30e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elements", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e6897c9c9c9ece04bb98a11be57f07b78009b82810f51bd21199eb3e2df3a82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="variableType")
    def variable_type(self) -> typing.Optional[builtins.str]:
        '''The variable type of the list.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "variableType"))

    @variable_type.setter
    def variable_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91e5fa5718fdf5ec2d6742206ed24709286db5ad5b416c1ef4d6f2f518595a4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "variableType", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_frauddetector.CfnListProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "elements": "elements",
        "tags": "tags",
        "variable_type": "variableType",
    },
)
class CfnListProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        elements: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        variable_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnList``.

        :param name: The name of the list.
        :param description: The description of the list.
        :param elements: The elements in the list.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param variable_type: The variable type of the list. For more information, see `Variable types <https://docs.aws.amazon.com/frauddetector/latest/ug/variables.html#variable-types>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-list.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_frauddetector as frauddetector
            
            cfn_list_props = frauddetector.CfnListProps(
                name="name",
            
                # the properties below are optional
                description="description",
                elements=["elements"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                variable_type="variableType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43236150e9a7db410fb7d326444e41492d6a4cb6de67f0733a004a6b84845a0b)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument elements", value=elements, expected_type=type_hints["elements"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument variable_type", value=variable_type, expected_type=type_hints["variable_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if elements is not None:
            self._values["elements"] = elements
        if tags is not None:
            self._values["tags"] = tags
        if variable_type is not None:
            self._values["variable_type"] = variable_type

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the list.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-list.html#cfn-frauddetector-list-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the list.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-list.html#cfn-frauddetector-list-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elements(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The elements in the list.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-list.html#cfn-frauddetector-list-elements
        '''
        result = self._values.get("elements")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-list.html#cfn-frauddetector-list-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def variable_type(self) -> typing.Optional[builtins.str]:
        '''The variable type of the list.

        For more information, see `Variable types <https://docs.aws.amazon.com/frauddetector/latest/ug/variables.html#variable-types>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-list.html#cfn-frauddetector-list-variabletype
        '''
        result = self._values.get("variable_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnListProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnOutcome(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_frauddetector.CfnOutcome",
):
    '''Creates or updates an outcome.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-outcome.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_frauddetector as frauddetector
        
        cfn_outcome = frauddetector.CfnOutcome(self, "MyCfnOutcome",
            name="name",
        
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
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The outcome name.
        :param description: The outcome description.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7609b23ac956162d8ea875a7c98b19bff4324c5b4f1ec8d395317e4dc7378837)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnOutcomeProps(name=name, description=description, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9a38349654b6392882cf28b67a77f9892c0f4144e3269bd5b8d9c3d8b44ef95)
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
            type_hints = typing.get_type_hints(_typecheckingstub__434ed5ead845bb805682170c79e4d6630ee0662b362d3238bb6c49b5661f9993)
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
        '''The ARN of the outcome.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''Timestamp of when outcome was created.

        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedTime")
    def attr_last_updated_time(self) -> builtins.str:
        '''Timestamp of when outcome was last updated.

        :cloudformationAttribute: LastUpdatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedTime"))

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
        '''The outcome name.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__402a3f582d4070b145a934d8b3ee15430c257bede3da8f02879600d401ccbaca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The outcome description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20fb944d46994af61daf79479ed1b7f09f72ba6b18ba4ea3e4c283f368fa1734)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2200712d63dfe736298ba3b837b2fedad3adac205c754484072f872ecb6a50c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_frauddetector.CfnOutcomeProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "description": "description", "tags": "tags"},
)
class CfnOutcomeProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnOutcome``.

        :param name: The outcome name.
        :param description: The outcome description.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-outcome.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_frauddetector as frauddetector
            
            cfn_outcome_props = frauddetector.CfnOutcomeProps(
                name="name",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53a02d43cb404eb2c8d53e3055c34f9c1368865e6086ba4b2f2506978110870f)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The outcome name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-outcome.html#cfn-frauddetector-outcome-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The outcome description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-outcome.html#cfn-frauddetector-outcome-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-outcome.html#cfn-frauddetector-outcome-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOutcomeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnVariable(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_frauddetector.CfnVariable",
):
    '''Manages a variable.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_frauddetector as frauddetector
        
        cfn_variable = frauddetector.CfnVariable(self, "MyCfnVariable",
            data_source="dataSource",
            data_type="dataType",
            default_value="defaultValue",
            name="name",
        
            # the properties below are optional
            description="description",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            variable_type="variableType"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        data_source: builtins.str,
        data_type: builtins.str,
        default_value: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        variable_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param data_source: The data source of the variable. Valid values: ``EVENT | EXTERNAL_MODEL_SCORE`` When defining a variable within a detector, you can only use the ``EVENT`` value for DataSource when the *Inline* property is set to true. If the *Inline* property is set false, you can use either ``EVENT`` or ``MODEL_SCORE`` for DataSource.
        :param data_type: The data type of the variable. Valid data types: ``STRING | INTEGER | BOOLEAN | FLOAT``
        :param default_value: The default value of the variable.
        :param name: The name of the variable. Pattern: ``^[0-9a-z_-]+$``
        :param description: The description of the variable.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param variable_type: The type of the variable. For more information see `Variable types <https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types>`_ . Valid Values: ``AUTH_CODE | AVS | BILLING_ADDRESS_L1 | BILLING_ADDRESS_L2 | BILLING_CITY | BILLING_COUNTRY | BILLING_NAME | BILLING_PHONE | BILLING_STATE | BILLING_ZIP | CARD_BIN | CATEGORICAL | CURRENCY_CODE | EMAIL_ADDRESS | FINGERPRINT | FRAUD_LABEL | FREE_FORM_TEXT | IP_ADDRESS | NUMERIC | ORDER_ID | PAYMENT_TYPE | PHONE_NUMBER | PRICE | PRODUCT_CATEGORY | SHIPPING_ADDRESS_L1 | SHIPPING_ADDRESS_L2 | SHIPPING_CITY | SHIPPING_COUNTRY | SHIPPING_NAME | SHIPPING_PHONE | SHIPPING_STATE | SHIPPING_ZIP | USERAGENT``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4f9344b7d9d1d1df0e685bc95efe9fdea7f0f858689eee7822ef4ae9247d912)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVariableProps(
            data_source=data_source,
            data_type=data_type,
            default_value=default_value,
            name=name,
            description=description,
            tags=tags,
            variable_type=variable_type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb7462fbff0f449ca87f85719a4f29e57a9692d8cc6f16130662dcd8fc8a9acf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ed755977a0365a073cbd7335e592f9bf1dee88121ed8651952c8007356c2ff05)
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
        '''The ARN of the variable.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''Timestamp of when variable was created.

        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedTime")
    def attr_last_updated_time(self) -> builtins.str:
        '''Timestamp of when variable was last updated.

        :cloudformationAttribute: LastUpdatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedTime"))

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
    @jsii.member(jsii_name="dataSource")
    def data_source(self) -> builtins.str:
        '''The data source of the variable.'''
        return typing.cast(builtins.str, jsii.get(self, "dataSource"))

    @data_source.setter
    def data_source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95107ddb7f8ff1717579be81cba5e1e0643f76f209c38357d2d52d3b3b0adffa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSource", value)

    @builtins.property
    @jsii.member(jsii_name="dataType")
    def data_type(self) -> builtins.str:
        '''The data type of the variable.'''
        return typing.cast(builtins.str, jsii.get(self, "dataType"))

    @data_type.setter
    def data_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9498d27cb5fcf8c5e220b6a071c2fd4387ea764c332e146436320d35cd0aee8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataType", value)

    @builtins.property
    @jsii.member(jsii_name="defaultValue")
    def default_value(self) -> builtins.str:
        '''The default value of the variable.'''
        return typing.cast(builtins.str, jsii.get(self, "defaultValue"))

    @default_value.setter
    def default_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23db352b848b7e937bca9ba9dd051209c4bf4acb876596f7c0a3428ad0f2d217)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultValue", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the variable.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efbfa25b36d51615fcef4c425cae1664d53ce595122d283d3c67eb58015562b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the variable.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05eff86202432d2849aa1e5c6cf3171f1bb66115804e73aa4862cb8cf2d5fe5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79501842c44e1a5fd839a7c5b83f896477c1ba415b083913c0ab0b8ab0fd5d4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="variableType")
    def variable_type(self) -> typing.Optional[builtins.str]:
        '''The type of the variable.

        For more information see `Variable types <https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types>`_ .
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "variableType"))

    @variable_type.setter
    def variable_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da235edb54f22d36e180719c9e70ea051788681cc9d40e391de1778f7858c879)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "variableType", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_frauddetector.CfnVariableProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_source": "dataSource",
        "data_type": "dataType",
        "default_value": "defaultValue",
        "name": "name",
        "description": "description",
        "tags": "tags",
        "variable_type": "variableType",
    },
)
class CfnVariableProps:
    def __init__(
        self,
        *,
        data_source: builtins.str,
        data_type: builtins.str,
        default_value: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        variable_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnVariable``.

        :param data_source: The data source of the variable. Valid values: ``EVENT | EXTERNAL_MODEL_SCORE`` When defining a variable within a detector, you can only use the ``EVENT`` value for DataSource when the *Inline* property is set to true. If the *Inline* property is set false, you can use either ``EVENT`` or ``MODEL_SCORE`` for DataSource.
        :param data_type: The data type of the variable. Valid data types: ``STRING | INTEGER | BOOLEAN | FLOAT``
        :param default_value: The default value of the variable.
        :param name: The name of the variable. Pattern: ``^[0-9a-z_-]+$``
        :param description: The description of the variable.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param variable_type: The type of the variable. For more information see `Variable types <https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types>`_ . Valid Values: ``AUTH_CODE | AVS | BILLING_ADDRESS_L1 | BILLING_ADDRESS_L2 | BILLING_CITY | BILLING_COUNTRY | BILLING_NAME | BILLING_PHONE | BILLING_STATE | BILLING_ZIP | CARD_BIN | CATEGORICAL | CURRENCY_CODE | EMAIL_ADDRESS | FINGERPRINT | FRAUD_LABEL | FREE_FORM_TEXT | IP_ADDRESS | NUMERIC | ORDER_ID | PAYMENT_TYPE | PHONE_NUMBER | PRICE | PRODUCT_CATEGORY | SHIPPING_ADDRESS_L1 | SHIPPING_ADDRESS_L2 | SHIPPING_CITY | SHIPPING_COUNTRY | SHIPPING_NAME | SHIPPING_PHONE | SHIPPING_STATE | SHIPPING_ZIP | USERAGENT``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_frauddetector as frauddetector
            
            cfn_variable_props = frauddetector.CfnVariableProps(
                data_source="dataSource",
                data_type="dataType",
                default_value="defaultValue",
                name="name",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                variable_type="variableType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e971889a72633f798e1c1ab65a7e842476bacc0ab6a37b199a03406565283072)
            check_type(argname="argument data_source", value=data_source, expected_type=type_hints["data_source"])
            check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
            check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument variable_type", value=variable_type, expected_type=type_hints["variable_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_source": data_source,
            "data_type": data_type,
            "default_value": default_value,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags
        if variable_type is not None:
            self._values["variable_type"] = variable_type

    @builtins.property
    def data_source(self) -> builtins.str:
        '''The data source of the variable.

        Valid values: ``EVENT | EXTERNAL_MODEL_SCORE``

        When defining a variable within a detector, you can only use the ``EVENT`` value for DataSource when the *Inline* property is set to true. If the *Inline* property is set false, you can use either ``EVENT`` or ``MODEL_SCORE`` for DataSource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-datasource
        '''
        result = self._values.get("data_source")
        assert result is not None, "Required property 'data_source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_type(self) -> builtins.str:
        '''The data type of the variable.

        Valid data types: ``STRING | INTEGER | BOOLEAN | FLOAT``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-datatype
        '''
        result = self._values.get("data_type")
        assert result is not None, "Required property 'data_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_value(self) -> builtins.str:
        '''The default value of the variable.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-defaultvalue
        '''
        result = self._values.get("default_value")
        assert result is not None, "Required property 'default_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the variable.

        Pattern: ``^[0-9a-z_-]+$``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the variable.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def variable_type(self) -> typing.Optional[builtins.str]:
        '''The type of the variable. For more information see `Variable types <https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types>`_ .

        Valid Values: ``AUTH_CODE | AVS | BILLING_ADDRESS_L1 | BILLING_ADDRESS_L2 | BILLING_CITY | BILLING_COUNTRY | BILLING_NAME | BILLING_PHONE | BILLING_STATE | BILLING_ZIP | CARD_BIN | CATEGORICAL | CURRENCY_CODE | EMAIL_ADDRESS | FINGERPRINT | FRAUD_LABEL | FREE_FORM_TEXT | IP_ADDRESS | NUMERIC | ORDER_ID | PAYMENT_TYPE | PHONE_NUMBER | PRICE | PRODUCT_CATEGORY | SHIPPING_ADDRESS_L1 | SHIPPING_ADDRESS_L2 | SHIPPING_CITY | SHIPPING_COUNTRY | SHIPPING_NAME | SHIPPING_PHONE | SHIPPING_STATE | SHIPPING_ZIP | USERAGENT``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-frauddetector-variable.html#cfn-frauddetector-variable-variabletype
        '''
        result = self._values.get("variable_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVariableProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDetector",
    "CfnDetectorProps",
    "CfnEntityType",
    "CfnEntityTypeProps",
    "CfnEventType",
    "CfnEventTypeProps",
    "CfnLabel",
    "CfnLabelProps",
    "CfnList",
    "CfnListProps",
    "CfnOutcome",
    "CfnOutcomeProps",
    "CfnVariable",
    "CfnVariableProps",
]

publication.publish()

def _typecheckingstub__34f177b06bae06cc28a84eadedbeeac967db23fde60544e18b48e387ec5e98f8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    detector_id: builtins.str,
    event_type: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetector.EventTypeProperty, typing.Dict[builtins.str, typing.Any]]],
    rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetector.RuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
    associated_models: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetector.ModelProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    detector_version_status: typing.Optional[builtins.str] = None,
    rule_execution_mode: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__126b5270f9e7ee19c314a22a060f32922f846c4adae62a4d0b4479d45bd125ac(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccb1420d0dc99c9166f8186cf6aac8171c218937f45e47f0971713c0231a004e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea1c83f296328b1afdeee432d51335bf25e25782aaa9cd76b6f2757dbe1419f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93bd5757764ac87038d7f200cd3d8de7e8b2fe7c1672e6177be640824ba52ccf(
    value: typing.Union[_IResolvable_da3f097b, CfnDetector.EventTypeProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fb8a2023ee1e11b475185f1ce6d40e0f9724e1f39f830efce457fec14d6e803(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDetector.RuleProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fa17c6e2d7f7f459019fd5d15924131bdf90bb9a9137f9b0d489a3063bb0c57(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDetector.ModelProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9657adb56d25aaeb148b4c0b1d9a4db1824078c550951eb37676edd06e02e228(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80ccaa368bd0676492bec90566a80d80de97fa630f6cc5a916bcd87a8fb61e08(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f37c0d89da5c5181365d1b3e0d414babeedcb502094947b1e138d41918da0bc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79bbcae57d55d3a1292ee375130b1ce78e88694b733f5018de1532c9840f2d00(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__748d29fdb915a872929d832801bbc352f01eda4881f57ab49c9f76dc67866b13(
    *,
    arn: typing.Optional[builtins.str] = None,
    created_time: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    inline: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    last_updated_time: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__118c1a0ac0699f5c01003dd52bd52397d476baf9a00d5bad28ed3d95cdc2ffad(
    *,
    arn: typing.Optional[builtins.str] = None,
    created_time: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    entity_types: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetector.EntityTypeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    event_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetector.EventVariableProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    inline: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    labels: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetector.LabelProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    last_updated_time: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb4525b017a8d1866b255be6b865fcd15a8810d62d25e0bd80f2d4868748d7a2(
    *,
    arn: typing.Optional[builtins.str] = None,
    created_time: typing.Optional[builtins.str] = None,
    data_source: typing.Optional[builtins.str] = None,
    data_type: typing.Optional[builtins.str] = None,
    default_value: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    inline: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    last_updated_time: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    variable_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ae88d73256647a482ae1ad952813d8ef10946f1a7a7069dd4bb50626b592fa2(
    *,
    arn: typing.Optional[builtins.str] = None,
    created_time: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    inline: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    last_updated_time: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a706373cb67d66c8702dcfd1e6f3496d5692fff02c37d6f866578375b8df4064(
    *,
    arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42ab66224fc57d8de7d56e9f0b2377eac7bf49979a47fbe73eaa48e47147fc2d(
    *,
    arn: typing.Optional[builtins.str] = None,
    created_time: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    inline: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    last_updated_time: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96e64cb156d83b6e85aee19c2adb7af17ac591c47655e3b1f709434834ff8e16(
    *,
    arn: typing.Optional[builtins.str] = None,
    created_time: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    detector_id: typing.Optional[builtins.str] = None,
    expression: typing.Optional[builtins.str] = None,
    language: typing.Optional[builtins.str] = None,
    last_updated_time: typing.Optional[builtins.str] = None,
    outcomes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetector.OutcomeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    rule_id: typing.Optional[builtins.str] = None,
    rule_version: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b26e6685891f22272eaba159af0e6c7023d53e7080f932711c9d37ff7d04a215(
    *,
    detector_id: builtins.str,
    event_type: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetector.EventTypeProperty, typing.Dict[builtins.str, typing.Any]]],
    rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetector.RuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
    associated_models: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDetector.ModelProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    detector_version_status: typing.Optional[builtins.str] = None,
    rule_execution_mode: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8bdfff4b2494486b1323350204c3429d0cd5e0c80cabaf21c7bf35893425d91(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1571c030c1f4eceb1eb429ce5e6aaa422cdd95b3620386f3e677d18030367fb2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e90300025950c0b81e217590ea856c2de60466ae1e258aa64dc945d2f6983de8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4992eda023f70fa90ab8a63e1125df15b3f02044513bf8a3d42d050330d13384(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4d2cecbe3561f37b9476c54f24e4f9ac5facd631897c1b90a00416d99a82254(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c909dc2ea7c1434dc4017053808f37d5041edd5e473826f0152aff8c19dd4d5(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0af61baf6c2e5424876fd48cdd930b1c05c66d9e45088e51b8c3775c6a209dfc(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__451d211f5cf761d7405bdc87e43ae39817ac3300cbc123e9dee6bf9c666c41d6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    entity_types: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventType.EntityTypeProperty, typing.Dict[builtins.str, typing.Any]]]]],
    event_variables: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventType.EventVariableProperty, typing.Dict[builtins.str, typing.Any]]]]],
    labels: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventType.LabelProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57073e537e1028dc4fd6dd2f1ad4592226f5ca14432d451af056c7fba3486a89(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__896e3b720206ace186a02ffaedea2e54f15b7ffb2309deee514062d40406c174(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53bb265a6c55aad83b33927c1087b3e8bc522ccd1d14bcfd6782272dff526d11(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEventType.EntityTypeProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__069acb584ea2685e6dec07d73d0d6962da831960b0309eee686ac2523e72d972(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEventType.EventVariableProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__365faaa83e644ceabaa6459d7b1a94dc88c201e84990388c642c666254e5beb4(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEventType.LabelProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82fef4b211d5ec66774645b2ecfcc0adb17643d3060cb14cdf95896b0fd3a8f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1631a2144130626280154fffd9661dcd8519a2076fc0261481b4ea14ba4dc7e7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5422e1150c24f0251536c92e0de44a7dd468b252c7e492f7885af852df4a03d(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__260ae8e52abed94a34c34efe87ffa1a80dd84c9261659e66aaf7d4643c3901dc(
    *,
    arn: typing.Optional[builtins.str] = None,
    created_time: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    inline: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    last_updated_time: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cd57942d76cc854fe9f0ec8b954232ad9c483611dacb6c78b25da731de022eb(
    *,
    arn: typing.Optional[builtins.str] = None,
    created_time: typing.Optional[builtins.str] = None,
    data_source: typing.Optional[builtins.str] = None,
    data_type: typing.Optional[builtins.str] = None,
    default_value: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    inline: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    last_updated_time: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    variable_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e8447a99b85327953986a476104b222d330a3ac72c6452bc91cb9a365efc593(
    *,
    arn: typing.Optional[builtins.str] = None,
    created_time: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    inline: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    last_updated_time: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e56a177c70c9bd1f38e708e145e3e6914e7a4d5bd3fed7466de6c3948aadabb7(
    *,
    entity_types: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventType.EntityTypeProperty, typing.Dict[builtins.str, typing.Any]]]]],
    event_variables: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventType.EventVariableProperty, typing.Dict[builtins.str, typing.Any]]]]],
    labels: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventType.LabelProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0a39e2a13e05950403b56b1af577d5a68139a2ca929eeb8d317f4d63405fde3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__846d8694c0a1fb75a9d878596433171417933948ad87217108fadef702e46ad8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1a7441e5b98737591872f05b12f252f5415e6a715918c761449c806ae1099e7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ea021d0099cd26ef1cb4651c8822d8793e2aab1e73ebec481a5dae4ce829dd1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c12115fd0f9077627c47abee3df17f7273449232e8f344399b245e1d4b7d390(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cefa25d3e293c90a44bfae875532dea0458ac7bfc5ab23042df6edd882e48f79(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e644e14f734aefd7f5a6a211ec9822cd9accb53cdd0c619b609b777f094ef91(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7557a1eddb9d179a34bcf99a7e13b5784e8e399dc50d632a1a35e6f33559ea7d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    elements: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    variable_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f20630db82ff99ed16fe5ef965c2bf119b32d566ed397567e0518858f3b5f77a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdf9b84448c9e22dcf579028df053d7f0e5d5dbed871fe7de3e9d5260be30ec9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c6ee22c1cf4c2004cdf89f5026d17232a07a5ebd4c0aa403bd83359e16aaafc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9fdbb1b05780a5faadf8389814bef11ff7e42925b05617d4c87c0ff3f6e7d77(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7030c8c92588018f78dd92396b547b788d9226b270fef8398bfb9791e29b30e4(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e6897c9c9c9ece04bb98a11be57f07b78009b82810f51bd21199eb3e2df3a82(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91e5fa5718fdf5ec2d6742206ed24709286db5ad5b416c1ef4d6f2f518595a4b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43236150e9a7db410fb7d326444e41492d6a4cb6de67f0733a004a6b84845a0b(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    elements: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    variable_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7609b23ac956162d8ea875a7c98b19bff4324c5b4f1ec8d395317e4dc7378837(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9a38349654b6392882cf28b67a77f9892c0f4144e3269bd5b8d9c3d8b44ef95(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__434ed5ead845bb805682170c79e4d6630ee0662b362d3238bb6c49b5661f9993(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__402a3f582d4070b145a934d8b3ee15430c257bede3da8f02879600d401ccbaca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20fb944d46994af61daf79479ed1b7f09f72ba6b18ba4ea3e4c283f368fa1734(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2200712d63dfe736298ba3b837b2fedad3adac205c754484072f872ecb6a50c3(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53a02d43cb404eb2c8d53e3055c34f9c1368865e6086ba4b2f2506978110870f(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4f9344b7d9d1d1df0e685bc95efe9fdea7f0f858689eee7822ef4ae9247d912(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    data_source: builtins.str,
    data_type: builtins.str,
    default_value: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    variable_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb7462fbff0f449ca87f85719a4f29e57a9692d8cc6f16130662dcd8fc8a9acf(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed755977a0365a073cbd7335e592f9bf1dee88121ed8651952c8007356c2ff05(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95107ddb7f8ff1717579be81cba5e1e0643f76f209c38357d2d52d3b3b0adffa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9498d27cb5fcf8c5e220b6a071c2fd4387ea764c332e146436320d35cd0aee8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23db352b848b7e937bca9ba9dd051209c4bf4acb876596f7c0a3428ad0f2d217(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efbfa25b36d51615fcef4c425cae1664d53ce595122d283d3c67eb58015562b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05eff86202432d2849aa1e5c6cf3171f1bb66115804e73aa4862cb8cf2d5fe5d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79501842c44e1a5fd839a7c5b83f896477c1ba415b083913c0ab0b8ab0fd5d4a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da235edb54f22d36e180719c9e70ea051788681cc9d40e391de1778f7858c879(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e971889a72633f798e1c1ab65a7e842476bacc0ab6a37b199a03406565283072(
    *,
    data_source: builtins.str,
    data_type: builtins.str,
    default_value: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    variable_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
