'''
# AWS::Evidently Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_evidently as evidently
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Evidently construct libraries](https://constructs.dev/search?q=evidently)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Evidently resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Evidently.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Evidently](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Evidently.html).

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
class CfnExperiment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_evidently.CfnExperiment",
):
    '''Creates or updates an Evidently *experiment* .

    Before you create an experiment, you must create the feature to use for the experiment.

    An experiment helps you make feature design decisions based on evidence and data. An experiment can test as many as five variations at once. Evidently collects experiment data and analyzes it by statistical methods, and provides clear recommendations about which variations perform better.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html
    :cloudformationResource: AWS::Evidently::Experiment
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_evidently as evidently
        
        cfn_experiment = evidently.CfnExperiment(self, "MyCfnExperiment",
            metric_goals=[evidently.CfnExperiment.MetricGoalObjectProperty(
                desired_change="desiredChange",
                entity_id_key="entityIdKey",
                metric_name="metricName",
                value_key="valueKey",
        
                # the properties below are optional
                event_pattern="eventPattern",
                unit_label="unitLabel"
            )],
            name="name",
            online_ab_config=evidently.CfnExperiment.OnlineAbConfigObjectProperty(
                control_treatment_name="controlTreatmentName",
                treatment_weights=[evidently.CfnExperiment.TreatmentToWeightProperty(
                    split_weight=123,
                    treatment="treatment"
                )]
            ),
            project="project",
            treatments=[evidently.CfnExperiment.TreatmentObjectProperty(
                feature="feature",
                treatment_name="treatmentName",
                variation="variation",
        
                # the properties below are optional
                description="description"
            )],
        
            # the properties below are optional
            description="description",
            randomization_salt="randomizationSalt",
            remove_segment=False,
            running_status=evidently.CfnExperiment.RunningStatusObjectProperty(
                status="status",
        
                # the properties below are optional
                analysis_complete_time="analysisCompleteTime",
                desired_state="desiredState",
                reason="reason"
            ),
            sampling_rate=123,
            segment="segment",
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
        metric_goals: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnExperiment.MetricGoalObjectProperty", typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        online_ab_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnExperiment.OnlineAbConfigObjectProperty", typing.Dict[builtins.str, typing.Any]]],
        project: builtins.str,
        treatments: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnExperiment.TreatmentObjectProperty", typing.Dict[builtins.str, typing.Any]]]]],
        description: typing.Optional[builtins.str] = None,
        randomization_salt: typing.Optional[builtins.str] = None,
        remove_segment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        running_status: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnExperiment.RunningStatusObjectProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        sampling_rate: typing.Optional[jsii.Number] = None,
        segment: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param metric_goals: An array of structures that defines the metrics used for the experiment, and whether a higher or lower value for each metric is the goal. You can use up to three metrics in an experiment.
        :param name: A name for the new experiment.
        :param online_ab_config: A structure that contains the configuration of which variation to use as the "control" version. The "control" version is used for comparison with other variations. This structure also specifies how much experiment traffic is allocated to each variation.
        :param project: The name or the ARN of the project where this experiment is to be created.
        :param treatments: An array of structures that describe the configuration of each feature variation used in the experiment.
        :param description: An optional description of the experiment.
        :param randomization_salt: When Evidently assigns a particular user session to an experiment, it must use a randomization ID to determine which variation the user session is served. This randomization ID is a combination of the entity ID and ``randomizationSalt`` . If you omit ``randomizationSalt`` , Evidently uses the experiment name as the ``randomizationSalt`` .
        :param remove_segment: Set this to ``true`` to remove the segment that is associated with this experiment. You can't use this parameter if the experiment is currently running.
        :param running_status: A structure that you can use to start and stop the experiment.
        :param sampling_rate: The portion of the available audience that you want to allocate to this experiment, in thousandths of a percent. The available audience is the total audience minus the audience that you have allocated to overrides or current launches of this feature. This is represented in thousandths of a percent. For example, specify 10,000 to allocate 10% of the available audience.
        :param segment: Specifies an audience *segment* to use in the experiment. When a segment is used in an experiment, only user sessions that match the segment pattern are used in the experiment. For more information, see `Segment rule pattern syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-segments.html#CloudWatch-Evidently-segments-syntax>`_ .
        :param tags: Assigns one or more tags (key-value pairs) to the experiment. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters. You can associate as many as 50 tags with an experiment. For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__734b87b8f3689149de24177947f45b4fba5a135b998ba47c50d89ce2cb06add4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnExperimentProps(
            metric_goals=metric_goals,
            name=name,
            online_ab_config=online_ab_config,
            project=project,
            treatments=treatments,
            description=description,
            randomization_salt=randomization_salt,
            remove_segment=remove_segment,
            running_status=running_status,
            sampling_rate=sampling_rate,
            segment=segment,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41b97e94769ee2d783fedafec30d14cbaf6057e49b29e299b13e98dba56880e4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__70b9593b4954b7c3230131122acbaf53f869364117e4692d8414ae2ff6e748d9)
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
        '''The ARN of the experiment.

        For example, ``arn:aws:evidently:us-west-2:0123455678912:project/myProject/experiment/myExperiment``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    @jsii.member(jsii_name="metricGoals")
    def metric_goals(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnExperiment.MetricGoalObjectProperty"]]]:
        '''An array of structures that defines the metrics used for the experiment, and whether a higher or lower value for each metric is the goal.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnExperiment.MetricGoalObjectProperty"]]], jsii.get(self, "metricGoals"))

    @metric_goals.setter
    def metric_goals(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnExperiment.MetricGoalObjectProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__608184263fdaf5c6ddc6386129d9fcd580b9dd416b72defa8d9f5ff27dc0ad80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricGoals", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for the new experiment.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62a1f010ee09d989ee27529a57132add8442518e9b6f2ceb37e2d97f82fcafc6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="onlineAbConfig")
    def online_ab_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnExperiment.OnlineAbConfigObjectProperty"]:
        '''A structure that contains the configuration of which variation to use as the "control" version.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnExperiment.OnlineAbConfigObjectProperty"], jsii.get(self, "onlineAbConfig"))

    @online_ab_config.setter
    def online_ab_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnExperiment.OnlineAbConfigObjectProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9651d87c6a5223e7d5416809c8358bf08d64bb82e3e66321fbc5472926f1e38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onlineAbConfig", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        '''The name or the ARN of the project where this experiment is to be created.'''
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07be64da4d74661911440a7a55dc7642deba8efb90897ee9599a318f284a9adb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="treatments")
    def treatments(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnExperiment.TreatmentObjectProperty"]]]:
        '''An array of structures that describe the configuration of each feature variation used in the experiment.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnExperiment.TreatmentObjectProperty"]]], jsii.get(self, "treatments"))

    @treatments.setter
    def treatments(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnExperiment.TreatmentObjectProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8a944ff8713baacf061323da7bcd1ccc67e8156291e472b1a6e7bfd7c1cf92b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "treatments", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the experiment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__865f432735c9ae2589b5dc0da6b59a080030920590d98d2ded0165c2edeff3c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="randomizationSalt")
    def randomization_salt(self) -> typing.Optional[builtins.str]:
        '''When Evidently assigns a particular user session to an experiment, it must use a randomization ID to determine which variation the user session is served.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "randomizationSalt"))

    @randomization_salt.setter
    def randomization_salt(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b086c5eed82ba0413f95a08c8a909e92a0bbce547efac04b83e6724b6d12d0b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "randomizationSalt", value)

    @builtins.property
    @jsii.member(jsii_name="removeSegment")
    def remove_segment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Set this to ``true`` to remove the segment that is associated with this experiment.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "removeSegment"))

    @remove_segment.setter
    def remove_segment(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1c2ff5ffa047cc8e5fe6a3846276a1d082e084a7ec198cae726e776bdd2d4e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "removeSegment", value)

    @builtins.property
    @jsii.member(jsii_name="runningStatus")
    def running_status(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnExperiment.RunningStatusObjectProperty"]]:
        '''A structure that you can use to start and stop the experiment.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnExperiment.RunningStatusObjectProperty"]], jsii.get(self, "runningStatus"))

    @running_status.setter
    def running_status(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnExperiment.RunningStatusObjectProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6064ddcd75be5c188ab7d11fc7107d2eac8214fd898eaf1de24a1cf499a71e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runningStatus", value)

    @builtins.property
    @jsii.member(jsii_name="samplingRate")
    def sampling_rate(self) -> typing.Optional[jsii.Number]:
        '''The portion of the available audience that you want to allocate to this experiment, in thousandths of a percent.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "samplingRate"))

    @sampling_rate.setter
    def sampling_rate(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__725630988a0f01ce2a47e4320264c699d35632d1c973571abca74103c37d1b5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "samplingRate", value)

    @builtins.property
    @jsii.member(jsii_name="segment")
    def segment(self) -> typing.Optional[builtins.str]:
        '''Specifies an audience *segment* to use in the experiment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "segment"))

    @segment.setter
    def segment(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__396ba0543ba827f0fb88ab5adb79e786937fd037c560627366b5a5ce722b6c91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "segment", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Assigns one or more tags (key-value pairs) to the experiment.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5fbe1b3ff9f5bf995bd927d269240a4d47815a9b472e6e6ae669666dd96a2dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnExperiment.MetricGoalObjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "desired_change": "desiredChange",
            "entity_id_key": "entityIdKey",
            "metric_name": "metricName",
            "value_key": "valueKey",
            "event_pattern": "eventPattern",
            "unit_label": "unitLabel",
        },
    )
    class MetricGoalObjectProperty:
        def __init__(
            self,
            *,
            desired_change: builtins.str,
            entity_id_key: builtins.str,
            metric_name: builtins.str,
            value_key: builtins.str,
            event_pattern: typing.Optional[builtins.str] = None,
            unit_label: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Use this structure to tell Evidently whether higher or lower values are desired for a metric that is used in an experiment.

            :param desired_change: ``INCREASE`` means that a variation with a higher number for this metric is performing better. ``DECREASE`` means that a variation with a lower number for this metric is performing better.
            :param entity_id_key: The entity, such as a user or session, that does an action that causes a metric value to be recorded. An example is ``userDetails.userID`` .
            :param metric_name: A name for the metric. It can include up to 255 characters.
            :param value_key: The JSON path to reference the numerical metric value in the event.
            :param event_pattern: The EventBridge event pattern that defines how the metric is recorded. For more information about EventBridge event patterns, see `Amazon EventBridge event patterns <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html>`_ .
            :param unit_label: A label for the units that the metric is measuring.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-metricgoalobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                metric_goal_object_property = evidently.CfnExperiment.MetricGoalObjectProperty(
                    desired_change="desiredChange",
                    entity_id_key="entityIdKey",
                    metric_name="metricName",
                    value_key="valueKey",
                
                    # the properties below are optional
                    event_pattern="eventPattern",
                    unit_label="unitLabel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1d37577ea667d695d977083ce595268b133cc268157e79b97ce5a51eb91f1562)
                check_type(argname="argument desired_change", value=desired_change, expected_type=type_hints["desired_change"])
                check_type(argname="argument entity_id_key", value=entity_id_key, expected_type=type_hints["entity_id_key"])
                check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
                check_type(argname="argument value_key", value=value_key, expected_type=type_hints["value_key"])
                check_type(argname="argument event_pattern", value=event_pattern, expected_type=type_hints["event_pattern"])
                check_type(argname="argument unit_label", value=unit_label, expected_type=type_hints["unit_label"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "desired_change": desired_change,
                "entity_id_key": entity_id_key,
                "metric_name": metric_name,
                "value_key": value_key,
            }
            if event_pattern is not None:
                self._values["event_pattern"] = event_pattern
            if unit_label is not None:
                self._values["unit_label"] = unit_label

        @builtins.property
        def desired_change(self) -> builtins.str:
            '''``INCREASE`` means that a variation with a higher number for this metric is performing better.

            ``DECREASE`` means that a variation with a lower number for this metric is performing better.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-metricgoalobject.html#cfn-evidently-experiment-metricgoalobject-desiredchange
            '''
            result = self._values.get("desired_change")
            assert result is not None, "Required property 'desired_change' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def entity_id_key(self) -> builtins.str:
            '''The entity, such as a user or session, that does an action that causes a metric value to be recorded.

            An example is ``userDetails.userID`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-metricgoalobject.html#cfn-evidently-experiment-metricgoalobject-entityidkey
            '''
            result = self._values.get("entity_id_key")
            assert result is not None, "Required property 'entity_id_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''A name for the metric.

            It can include up to 255 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-metricgoalobject.html#cfn-evidently-experiment-metricgoalobject-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value_key(self) -> builtins.str:
            '''The JSON path to reference the numerical metric value in the event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-metricgoalobject.html#cfn-evidently-experiment-metricgoalobject-valuekey
            '''
            result = self._values.get("value_key")
            assert result is not None, "Required property 'value_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def event_pattern(self) -> typing.Optional[builtins.str]:
            '''The EventBridge event pattern that defines how the metric is recorded.

            For more information about EventBridge event patterns, see `Amazon EventBridge event patterns <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-metricgoalobject.html#cfn-evidently-experiment-metricgoalobject-eventpattern
            '''
            result = self._values.get("event_pattern")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def unit_label(self) -> typing.Optional[builtins.str]:
            '''A label for the units that the metric is measuring.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-metricgoalobject.html#cfn-evidently-experiment-metricgoalobject-unitlabel
            '''
            result = self._values.get("unit_label")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricGoalObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnExperiment.OnlineAbConfigObjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "control_treatment_name": "controlTreatmentName",
            "treatment_weights": "treatmentWeights",
        },
    )
    class OnlineAbConfigObjectProperty:
        def __init__(
            self,
            *,
            control_treatment_name: typing.Optional[builtins.str] = None,
            treatment_weights: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnExperiment.TreatmentToWeightProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''A structure that contains the configuration of which variation to use as the "control" version.

            The "control" version is used for comparison with other variations. This structure also specifies how much experiment traffic is allocated to each variation.

            :param control_treatment_name: The name of the variation that is to be the default variation that the other variations are compared to.
            :param treatment_weights: A set of key-value pairs. The keys are treatment names, and the values are the portion of experiment traffic to be assigned to that treatment. Specify the traffic portion in thousandths of a percent, so 20,000 for a variation would allocate 20% of the experiment traffic to that variation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-onlineabconfigobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                online_ab_config_object_property = evidently.CfnExperiment.OnlineAbConfigObjectProperty(
                    control_treatment_name="controlTreatmentName",
                    treatment_weights=[evidently.CfnExperiment.TreatmentToWeightProperty(
                        split_weight=123,
                        treatment="treatment"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__89b9e3dc636161b952f66372f7de126954391a890d3b4b6c5c9d8ecf9497c969)
                check_type(argname="argument control_treatment_name", value=control_treatment_name, expected_type=type_hints["control_treatment_name"])
                check_type(argname="argument treatment_weights", value=treatment_weights, expected_type=type_hints["treatment_weights"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if control_treatment_name is not None:
                self._values["control_treatment_name"] = control_treatment_name
            if treatment_weights is not None:
                self._values["treatment_weights"] = treatment_weights

        @builtins.property
        def control_treatment_name(self) -> typing.Optional[builtins.str]:
            '''The name of the variation that is to be the default variation that the other variations are compared to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-onlineabconfigobject.html#cfn-evidently-experiment-onlineabconfigobject-controltreatmentname
            '''
            result = self._values.get("control_treatment_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def treatment_weights(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnExperiment.TreatmentToWeightProperty"]]]]:
            '''A set of key-value pairs.

            The keys are treatment names, and the values are the portion of experiment traffic to be assigned to that treatment. Specify the traffic portion in thousandths of a percent, so 20,000 for a variation would allocate 20% of the experiment traffic to that variation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-onlineabconfigobject.html#cfn-evidently-experiment-onlineabconfigobject-treatmentweights
            '''
            result = self._values.get("treatment_weights")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnExperiment.TreatmentToWeightProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OnlineAbConfigObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnExperiment.RunningStatusObjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "status": "status",
            "analysis_complete_time": "analysisCompleteTime",
            "desired_state": "desiredState",
            "reason": "reason",
        },
    )
    class RunningStatusObjectProperty:
        def __init__(
            self,
            *,
            status: builtins.str,
            analysis_complete_time: typing.Optional[builtins.str] = None,
            desired_state: typing.Optional[builtins.str] = None,
            reason: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Use this structure to start and stop the experiment.

            :param status: To start the experiment now, specify ``START`` for this parameter. If this experiment is currently running and you want to stop it now, specify ``STOP`` .
            :param analysis_complete_time: If you are using AWS CloudFormation to start the experiment, use this field to specify when the experiment is to end. The format is as a UNIX timestamp. For more information about this format, see `The Current Epoch Unix Timestamp <https://docs.aws.amazon.com/https://www.unixtimestamp.com/index.php>`_ .
            :param desired_state: If you are using AWS CloudFormation to stop this experiment, specify either ``COMPLETED`` or ``CANCELLED`` here to indicate how to classify this experiment.
            :param reason: If you are using AWS CloudFormation to stop this experiment, this is an optional field that you can use to record why the experiment is being stopped or cancelled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-runningstatusobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                running_status_object_property = evidently.CfnExperiment.RunningStatusObjectProperty(
                    status="status",
                
                    # the properties below are optional
                    analysis_complete_time="analysisCompleteTime",
                    desired_state="desiredState",
                    reason="reason"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0bb80b983de21b5a767fb926c4b0335e3f64a61afb300308777b1584b59778db)
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument analysis_complete_time", value=analysis_complete_time, expected_type=type_hints["analysis_complete_time"])
                check_type(argname="argument desired_state", value=desired_state, expected_type=type_hints["desired_state"])
                check_type(argname="argument reason", value=reason, expected_type=type_hints["reason"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "status": status,
            }
            if analysis_complete_time is not None:
                self._values["analysis_complete_time"] = analysis_complete_time
            if desired_state is not None:
                self._values["desired_state"] = desired_state
            if reason is not None:
                self._values["reason"] = reason

        @builtins.property
        def status(self) -> builtins.str:
            '''To start the experiment now, specify ``START`` for this parameter.

            If this experiment is currently running and you want to stop it now, specify ``STOP`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-runningstatusobject.html#cfn-evidently-experiment-runningstatusobject-status
            '''
            result = self._values.get("status")
            assert result is not None, "Required property 'status' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def analysis_complete_time(self) -> typing.Optional[builtins.str]:
            '''If you are using AWS CloudFormation to start the experiment, use this field to specify when the experiment is to end.

            The format is as a UNIX timestamp. For more information about this format, see `The Current Epoch Unix Timestamp <https://docs.aws.amazon.com/https://www.unixtimestamp.com/index.php>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-runningstatusobject.html#cfn-evidently-experiment-runningstatusobject-analysiscompletetime
            '''
            result = self._values.get("analysis_complete_time")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def desired_state(self) -> typing.Optional[builtins.str]:
            '''If you are using AWS CloudFormation to stop this experiment, specify either ``COMPLETED`` or ``CANCELLED`` here to indicate how to classify this experiment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-runningstatusobject.html#cfn-evidently-experiment-runningstatusobject-desiredstate
            '''
            result = self._values.get("desired_state")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def reason(self) -> typing.Optional[builtins.str]:
            '''If you are using AWS CloudFormation to stop this experiment, this is an optional field that you can use to record why the experiment is being stopped or cancelled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-runningstatusobject.html#cfn-evidently-experiment-runningstatusobject-reason
            '''
            result = self._values.get("reason")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RunningStatusObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnExperiment.TreatmentObjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "feature": "feature",
            "treatment_name": "treatmentName",
            "variation": "variation",
            "description": "description",
        },
    )
    class TreatmentObjectProperty:
        def __init__(
            self,
            *,
            feature: builtins.str,
            treatment_name: builtins.str,
            variation: builtins.str,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure that defines one treatment in an experiment.

            A treatment is a variation of the feature that you are including in the experiment.

            :param feature: The name of the feature for this experiment.
            :param treatment_name: A name for this treatment. It can include up to 127 characters.
            :param variation: The name of the variation to use for this treatment.
            :param description: The description of the treatment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmentobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                treatment_object_property = evidently.CfnExperiment.TreatmentObjectProperty(
                    feature="feature",
                    treatment_name="treatmentName",
                    variation="variation",
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e275da028c15ab90e130e2dcd1b4cdcb0205addea248b0d3cd8434badd9f7b34)
                check_type(argname="argument feature", value=feature, expected_type=type_hints["feature"])
                check_type(argname="argument treatment_name", value=treatment_name, expected_type=type_hints["treatment_name"])
                check_type(argname="argument variation", value=variation, expected_type=type_hints["variation"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "feature": feature,
                "treatment_name": treatment_name,
                "variation": variation,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def feature(self) -> builtins.str:
            '''The name of the feature for this experiment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmentobject.html#cfn-evidently-experiment-treatmentobject-feature
            '''
            result = self._values.get("feature")
            assert result is not None, "Required property 'feature' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def treatment_name(self) -> builtins.str:
            '''A name for this treatment.

            It can include up to 127 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmentobject.html#cfn-evidently-experiment-treatmentobject-treatmentname
            '''
            result = self._values.get("treatment_name")
            assert result is not None, "Required property 'treatment_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def variation(self) -> builtins.str:
            '''The name of the variation to use for this treatment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmentobject.html#cfn-evidently-experiment-treatmentobject-variation
            '''
            result = self._values.get("variation")
            assert result is not None, "Required property 'variation' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description of the treatment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmentobject.html#cfn-evidently-experiment-treatmentobject-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TreatmentObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnExperiment.TreatmentToWeightProperty",
        jsii_struct_bases=[],
        name_mapping={"split_weight": "splitWeight", "treatment": "treatment"},
    )
    class TreatmentToWeightProperty:
        def __init__(
            self,
            *,
            split_weight: jsii.Number,
            treatment: builtins.str,
        ) -> None:
            '''This structure defines how much experiment traffic to allocate to one treatment used in the experiment.

            :param split_weight: The portion of experiment traffic to allocate to this treatment. Specify the traffic portion in thousandths of a percent, so 20,000 allocated to a treatment would allocate 20% of the experiment traffic to that treatment.
            :param treatment: The name of the treatment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmenttoweight.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                treatment_to_weight_property = evidently.CfnExperiment.TreatmentToWeightProperty(
                    split_weight=123,
                    treatment="treatment"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3c24913e7b4ce7d0ccc2499c81ecea7d897c69c7fbc1291a0521dbb0d3ce04ad)
                check_type(argname="argument split_weight", value=split_weight, expected_type=type_hints["split_weight"])
                check_type(argname="argument treatment", value=treatment, expected_type=type_hints["treatment"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "split_weight": split_weight,
                "treatment": treatment,
            }

        @builtins.property
        def split_weight(self) -> jsii.Number:
            '''The portion of experiment traffic to allocate to this treatment.

            Specify the traffic portion in thousandths of a percent, so 20,000 allocated to a treatment would allocate 20% of the experiment traffic to that treatment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmenttoweight.html#cfn-evidently-experiment-treatmenttoweight-splitweight
            '''
            result = self._values.get("split_weight")
            assert result is not None, "Required property 'split_weight' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def treatment(self) -> builtins.str:
            '''The name of the treatment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-experiment-treatmenttoweight.html#cfn-evidently-experiment-treatmenttoweight-treatment
            '''
            result = self._values.get("treatment")
            assert result is not None, "Required property 'treatment' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TreatmentToWeightProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_evidently.CfnExperimentProps",
    jsii_struct_bases=[],
    name_mapping={
        "metric_goals": "metricGoals",
        "name": "name",
        "online_ab_config": "onlineAbConfig",
        "project": "project",
        "treatments": "treatments",
        "description": "description",
        "randomization_salt": "randomizationSalt",
        "remove_segment": "removeSegment",
        "running_status": "runningStatus",
        "sampling_rate": "samplingRate",
        "segment": "segment",
        "tags": "tags",
    },
)
class CfnExperimentProps:
    def __init__(
        self,
        *,
        metric_goals: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnExperiment.MetricGoalObjectProperty, typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        online_ab_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnExperiment.OnlineAbConfigObjectProperty, typing.Dict[builtins.str, typing.Any]]],
        project: builtins.str,
        treatments: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnExperiment.TreatmentObjectProperty, typing.Dict[builtins.str, typing.Any]]]]],
        description: typing.Optional[builtins.str] = None,
        randomization_salt: typing.Optional[builtins.str] = None,
        remove_segment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        running_status: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnExperiment.RunningStatusObjectProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        sampling_rate: typing.Optional[jsii.Number] = None,
        segment: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnExperiment``.

        :param metric_goals: An array of structures that defines the metrics used for the experiment, and whether a higher or lower value for each metric is the goal. You can use up to three metrics in an experiment.
        :param name: A name for the new experiment.
        :param online_ab_config: A structure that contains the configuration of which variation to use as the "control" version. The "control" version is used for comparison with other variations. This structure also specifies how much experiment traffic is allocated to each variation.
        :param project: The name or the ARN of the project where this experiment is to be created.
        :param treatments: An array of structures that describe the configuration of each feature variation used in the experiment.
        :param description: An optional description of the experiment.
        :param randomization_salt: When Evidently assigns a particular user session to an experiment, it must use a randomization ID to determine which variation the user session is served. This randomization ID is a combination of the entity ID and ``randomizationSalt`` . If you omit ``randomizationSalt`` , Evidently uses the experiment name as the ``randomizationSalt`` .
        :param remove_segment: Set this to ``true`` to remove the segment that is associated with this experiment. You can't use this parameter if the experiment is currently running.
        :param running_status: A structure that you can use to start and stop the experiment.
        :param sampling_rate: The portion of the available audience that you want to allocate to this experiment, in thousandths of a percent. The available audience is the total audience minus the audience that you have allocated to overrides or current launches of this feature. This is represented in thousandths of a percent. For example, specify 10,000 to allocate 10% of the available audience.
        :param segment: Specifies an audience *segment* to use in the experiment. When a segment is used in an experiment, only user sessions that match the segment pattern are used in the experiment. For more information, see `Segment rule pattern syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-segments.html#CloudWatch-Evidently-segments-syntax>`_ .
        :param tags: Assigns one or more tags (key-value pairs) to the experiment. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters. You can associate as many as 50 tags with an experiment. For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_evidently as evidently
            
            cfn_experiment_props = evidently.CfnExperimentProps(
                metric_goals=[evidently.CfnExperiment.MetricGoalObjectProperty(
                    desired_change="desiredChange",
                    entity_id_key="entityIdKey",
                    metric_name="metricName",
                    value_key="valueKey",
            
                    # the properties below are optional
                    event_pattern="eventPattern",
                    unit_label="unitLabel"
                )],
                name="name",
                online_ab_config=evidently.CfnExperiment.OnlineAbConfigObjectProperty(
                    control_treatment_name="controlTreatmentName",
                    treatment_weights=[evidently.CfnExperiment.TreatmentToWeightProperty(
                        split_weight=123,
                        treatment="treatment"
                    )]
                ),
                project="project",
                treatments=[evidently.CfnExperiment.TreatmentObjectProperty(
                    feature="feature",
                    treatment_name="treatmentName",
                    variation="variation",
            
                    # the properties below are optional
                    description="description"
                )],
            
                # the properties below are optional
                description="description",
                randomization_salt="randomizationSalt",
                remove_segment=False,
                running_status=evidently.CfnExperiment.RunningStatusObjectProperty(
                    status="status",
            
                    # the properties below are optional
                    analysis_complete_time="analysisCompleteTime",
                    desired_state="desiredState",
                    reason="reason"
                ),
                sampling_rate=123,
                segment="segment",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b511a5b944573df5aa1fb656233057b55fbb2369fc71a21a16cf2485a314559)
            check_type(argname="argument metric_goals", value=metric_goals, expected_type=type_hints["metric_goals"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument online_ab_config", value=online_ab_config, expected_type=type_hints["online_ab_config"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument treatments", value=treatments, expected_type=type_hints["treatments"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument randomization_salt", value=randomization_salt, expected_type=type_hints["randomization_salt"])
            check_type(argname="argument remove_segment", value=remove_segment, expected_type=type_hints["remove_segment"])
            check_type(argname="argument running_status", value=running_status, expected_type=type_hints["running_status"])
            check_type(argname="argument sampling_rate", value=sampling_rate, expected_type=type_hints["sampling_rate"])
            check_type(argname="argument segment", value=segment, expected_type=type_hints["segment"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric_goals": metric_goals,
            "name": name,
            "online_ab_config": online_ab_config,
            "project": project,
            "treatments": treatments,
        }
        if description is not None:
            self._values["description"] = description
        if randomization_salt is not None:
            self._values["randomization_salt"] = randomization_salt
        if remove_segment is not None:
            self._values["remove_segment"] = remove_segment
        if running_status is not None:
            self._values["running_status"] = running_status
        if sampling_rate is not None:
            self._values["sampling_rate"] = sampling_rate
        if segment is not None:
            self._values["segment"] = segment
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def metric_goals(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnExperiment.MetricGoalObjectProperty]]]:
        '''An array of structures that defines the metrics used for the experiment, and whether a higher or lower value for each metric is the goal.

        You can use up to three metrics in an experiment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-metricgoals
        '''
        result = self._values.get("metric_goals")
        assert result is not None, "Required property 'metric_goals' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnExperiment.MetricGoalObjectProperty]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the new experiment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def online_ab_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnExperiment.OnlineAbConfigObjectProperty]:
        '''A structure that contains the configuration of which variation to use as the "control" version.

        The "control" version is used for comparison with other variations. This structure also specifies how much experiment traffic is allocated to each variation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-onlineabconfig
        '''
        result = self._values.get("online_ab_config")
        assert result is not None, "Required property 'online_ab_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnExperiment.OnlineAbConfigObjectProperty], result)

    @builtins.property
    def project(self) -> builtins.str:
        '''The name or the ARN of the project where this experiment is to be created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-project
        '''
        result = self._values.get("project")
        assert result is not None, "Required property 'project' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def treatments(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnExperiment.TreatmentObjectProperty]]]:
        '''An array of structures that describe the configuration of each feature variation used in the experiment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-treatments
        '''
        result = self._values.get("treatments")
        assert result is not None, "Required property 'treatments' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnExperiment.TreatmentObjectProperty]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the experiment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def randomization_salt(self) -> typing.Optional[builtins.str]:
        '''When Evidently assigns a particular user session to an experiment, it must use a randomization ID to determine which variation the user session is served.

        This randomization ID is a combination of the entity ID and ``randomizationSalt`` . If you omit ``randomizationSalt`` , Evidently uses the experiment name as the ``randomizationSalt`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-randomizationsalt
        '''
        result = self._values.get("randomization_salt")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remove_segment(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Set this to ``true`` to remove the segment that is associated with this experiment.

        You can't use this parameter if the experiment is currently running.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-removesegment
        '''
        result = self._values.get("remove_segment")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def running_status(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnExperiment.RunningStatusObjectProperty]]:
        '''A structure that you can use to start and stop the experiment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-runningstatus
        '''
        result = self._values.get("running_status")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnExperiment.RunningStatusObjectProperty]], result)

    @builtins.property
    def sampling_rate(self) -> typing.Optional[jsii.Number]:
        '''The portion of the available audience that you want to allocate to this experiment, in thousandths of a percent.

        The available audience is the total audience minus the audience that you have allocated to overrides or current launches of this feature.

        This is represented in thousandths of a percent. For example, specify 10,000 to allocate 10% of the available audience.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-samplingrate
        '''
        result = self._values.get("sampling_rate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def segment(self) -> typing.Optional[builtins.str]:
        '''Specifies an audience *segment* to use in the experiment.

        When a segment is used in an experiment, only user sessions that match the segment pattern are used in the experiment.

        For more information, see `Segment rule pattern syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-segments.html#CloudWatch-Evidently-segments-syntax>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-segment
        '''
        result = self._values.get("segment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Assigns one or more tags (key-value pairs) to the experiment.

        Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

        Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters.

        You can associate as many as 50 tags with an experiment.

        For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-experiment.html#cfn-evidently-experiment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnExperimentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnFeature(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_evidently.CfnFeature",
):
    '''Creates or updates an Evidently *feature* that you want to launch or test.

    You can define up to five variations of a feature, and use these variations in your launches and experiments. A feature must be created in a project. For information about creating a project, see `CreateProject <https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_CreateProject.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html
    :cloudformationResource: AWS::Evidently::Feature
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_evidently as evidently
        
        cfn_feature = evidently.CfnFeature(self, "MyCfnFeature",
            name="name",
            project="project",
            variations=[evidently.CfnFeature.VariationObjectProperty(
                variation_name="variationName",
        
                # the properties below are optional
                boolean_value=False,
                double_value=123,
                long_value=123,
                string_value="stringValue"
            )],
        
            # the properties below are optional
            default_variation="defaultVariation",
            description="description",
            entity_overrides=[evidently.CfnFeature.EntityOverrideProperty(
                entity_id="entityId",
                variation="variation"
            )],
            evaluation_strategy="evaluationStrategy",
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
        project: builtins.str,
        variations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFeature.VariationObjectProperty", typing.Dict[builtins.str, typing.Any]]]]],
        default_variation: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        entity_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFeature.EntityOverrideProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        evaluation_strategy: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name for the feature. It can include up to 127 characters.
        :param project: The name or ARN of the project that is to contain the new feature.
        :param variations: An array of structures that contain the configuration of the feature's different variations. Each ``VariationObject`` in the ``Variations`` array for a feature must have the same type of value ( ``BooleanValue`` , ``DoubleValue`` , ``LongValue`` or ``StringValue`` ).
        :param default_variation: The name of the variation to use as the default variation. The default variation is served to users who are not allocated to any ongoing launches or experiments of this feature. This variation must also be listed in the ``Variations`` structure. If you omit ``DefaultVariation`` , the first variation listed in the ``Variations`` structure is used as the default variation.
        :param description: An optional description of the feature.
        :param entity_overrides: Specify users that should always be served a specific variation of a feature. Each user is specified by a key-value pair . For each key, specify a user by entering their user ID, account ID, or some other identifier. For the value, specify the name of the variation that they are to be served.
        :param evaluation_strategy: Specify ``ALL_RULES`` to activate the traffic allocation specified by any ongoing launches or experiments. Specify ``DEFAULT_VARIATION`` to serve the default variation to all users instead.
        :param tags: Assigns one or more tags (key-value pairs) to the feature. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters. You can associate as many as 50 tags with a feature. For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__032b8fcb49dd9128128c244f2e15873395777d391323d4e1a7f50f4087f87f94)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFeatureProps(
            name=name,
            project=project,
            variations=variations,
            default_variation=default_variation,
            description=description,
            entity_overrides=entity_overrides,
            evaluation_strategy=evaluation_strategy,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66bc0230fcb2a6c06673de455252150fcbb3b06b62d3db48b94a67af38875a13)
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
            type_hints = typing.get_type_hints(_typecheckingstub__64398b69cc190a0e85ffd77073c8d5be01a1867ed75581308e5c548d5fdf2604)
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
        '''The ARN of the feature.

        For example, ``arn:aws:evidently:us-west-2:0123455678912:project/myProject/feature/myFeature`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
        '''The name for the feature.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83847122ae503fe691e71b7ae222c38d7b58994caa625cbeb30f8718f5e9cffe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        '''The name or ARN of the project that is to contain the new feature.'''
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cce06c18c6aab66f449d3e00e017d519d1438e9f01b0e347c6891a96cff96940)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="variations")
    def variations(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFeature.VariationObjectProperty"]]]:
        '''An array of structures that contain the configuration of the feature's different variations.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFeature.VariationObjectProperty"]]], jsii.get(self, "variations"))

    @variations.setter
    def variations(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFeature.VariationObjectProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6955963eddf06f8bac909ceb0999e345a3de2bab55b1154054f5891fcb0da73d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "variations", value)

    @builtins.property
    @jsii.member(jsii_name="defaultVariation")
    def default_variation(self) -> typing.Optional[builtins.str]:
        '''The name of the variation to use as the default variation.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultVariation"))

    @default_variation.setter
    def default_variation(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49765789b788df887d77d9c6fe7a5f94eb6690b46391f2615967e3bb3c523a73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultVariation", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the feature.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09fb4d9f2430757616faf01218e796a9ca6e1379e14e42daaf88b8eb5ea9af36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="entityOverrides")
    def entity_overrides(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFeature.EntityOverrideProperty"]]]]:
        '''Specify users that should always be served a specific variation of a feature.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFeature.EntityOverrideProperty"]]]], jsii.get(self, "entityOverrides"))

    @entity_overrides.setter
    def entity_overrides(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFeature.EntityOverrideProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92a59dc479738d64f37719a4c84ee0a1aee9546c14b55d9de1e19e98ed4ea8eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entityOverrides", value)

    @builtins.property
    @jsii.member(jsii_name="evaluationStrategy")
    def evaluation_strategy(self) -> typing.Optional[builtins.str]:
        '''Specify ``ALL_RULES`` to activate the traffic allocation specified by any ongoing launches or experiments.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "evaluationStrategy"))

    @evaluation_strategy.setter
    def evaluation_strategy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f401c4f77ac0ecaf262bebe57b7e55013b6a1bee0181c137656d0db9d5ded85c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Assigns one or more tags (key-value pairs) to the feature.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__452ab42f442291f21b09b8398172655babfb13efba8ffa52142570f0b06b2fc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnFeature.EntityOverrideProperty",
        jsii_struct_bases=[],
        name_mapping={"entity_id": "entityId", "variation": "variation"},
    )
    class EntityOverrideProperty:
        def __init__(
            self,
            *,
            entity_id: typing.Optional[builtins.str] = None,
            variation: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A set of key-value pairs that specify users who should always be served a specific variation of a feature.

            Each key specifies a user using their user ID, account ID, or some other identifier. The value specifies the name of the variation that the user is to be served.

            :param entity_id: The entity ID to be served the variation specified in ``Variation`` .
            :param variation: The name of the variation to serve to the user session that matches the ``EntityId`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-entityoverride.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                entity_override_property = evidently.CfnFeature.EntityOverrideProperty(
                    entity_id="entityId",
                    variation="variation"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__71819cf2da9d0a5266c1f2b7d31b8d7fa4079594f6d96dbfd12865119d431c85)
                check_type(argname="argument entity_id", value=entity_id, expected_type=type_hints["entity_id"])
                check_type(argname="argument variation", value=variation, expected_type=type_hints["variation"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if entity_id is not None:
                self._values["entity_id"] = entity_id
            if variation is not None:
                self._values["variation"] = variation

        @builtins.property
        def entity_id(self) -> typing.Optional[builtins.str]:
            '''The entity ID to be served the variation specified in ``Variation`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-entityoverride.html#cfn-evidently-feature-entityoverride-entityid
            '''
            result = self._values.get("entity_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def variation(self) -> typing.Optional[builtins.str]:
            '''The name of the variation to serve to the user session that matches the ``EntityId`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-entityoverride.html#cfn-evidently-feature-entityoverride-variation
            '''
            result = self._values.get("variation")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EntityOverrideProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnFeature.VariationObjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "variation_name": "variationName",
            "boolean_value": "booleanValue",
            "double_value": "doubleValue",
            "long_value": "longValue",
            "string_value": "stringValue",
        },
    )
    class VariationObjectProperty:
        def __init__(
            self,
            *,
            variation_name: builtins.str,
            boolean_value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            double_value: typing.Optional[jsii.Number] = None,
            long_value: typing.Optional[jsii.Number] = None,
            string_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''This structure contains the name and variation value of one variation of a feature.

            It can contain only one of the following parameters: ``BooleanValue`` , ``DoubleValue`` , ``LongValue`` or ``StringValue`` .

            :param variation_name: A name for the variation. It can include up to 127 characters.
            :param boolean_value: The value assigned to this variation, if the variation type is boolean.
            :param double_value: The value assigned to this variation, if the variation type is a double.
            :param long_value: The value assigned to this variation, if the variation type is a long.
            :param string_value: The value assigned to this variation, if the variation type is a string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-variationobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                variation_object_property = evidently.CfnFeature.VariationObjectProperty(
                    variation_name="variationName",
                
                    # the properties below are optional
                    boolean_value=False,
                    double_value=123,
                    long_value=123,
                    string_value="stringValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5d69f83bb962985fff0b5f289781eb2e76e626dd2982d400f93a032205de5739)
                check_type(argname="argument variation_name", value=variation_name, expected_type=type_hints["variation_name"])
                check_type(argname="argument boolean_value", value=boolean_value, expected_type=type_hints["boolean_value"])
                check_type(argname="argument double_value", value=double_value, expected_type=type_hints["double_value"])
                check_type(argname="argument long_value", value=long_value, expected_type=type_hints["long_value"])
                check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "variation_name": variation_name,
            }
            if boolean_value is not None:
                self._values["boolean_value"] = boolean_value
            if double_value is not None:
                self._values["double_value"] = double_value
            if long_value is not None:
                self._values["long_value"] = long_value
            if string_value is not None:
                self._values["string_value"] = string_value

        @builtins.property
        def variation_name(self) -> builtins.str:
            '''A name for the variation.

            It can include up to 127 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-variationobject.html#cfn-evidently-feature-variationobject-variationname
            '''
            result = self._values.get("variation_name")
            assert result is not None, "Required property 'variation_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def boolean_value(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The value assigned to this variation, if the variation type is boolean.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-variationobject.html#cfn-evidently-feature-variationobject-booleanvalue
            '''
            result = self._values.get("boolean_value")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def double_value(self) -> typing.Optional[jsii.Number]:
            '''The value assigned to this variation, if the variation type is a double.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-variationobject.html#cfn-evidently-feature-variationobject-doublevalue
            '''
            result = self._values.get("double_value")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def long_value(self) -> typing.Optional[jsii.Number]:
            '''The value assigned to this variation, if the variation type is a long.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-variationobject.html#cfn-evidently-feature-variationobject-longvalue
            '''
            result = self._values.get("long_value")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def string_value(self) -> typing.Optional[builtins.str]:
            '''The value assigned to this variation, if the variation type is a string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-feature-variationobject.html#cfn-evidently-feature-variationobject-stringvalue
            '''
            result = self._values.get("string_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VariationObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_evidently.CfnFeatureProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "project": "project",
        "variations": "variations",
        "default_variation": "defaultVariation",
        "description": "description",
        "entity_overrides": "entityOverrides",
        "evaluation_strategy": "evaluationStrategy",
        "tags": "tags",
    },
)
class CfnFeatureProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        project: builtins.str,
        variations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFeature.VariationObjectProperty, typing.Dict[builtins.str, typing.Any]]]]],
        default_variation: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        entity_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFeature.EntityOverrideProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        evaluation_strategy: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFeature``.

        :param name: The name for the feature. It can include up to 127 characters.
        :param project: The name or ARN of the project that is to contain the new feature.
        :param variations: An array of structures that contain the configuration of the feature's different variations. Each ``VariationObject`` in the ``Variations`` array for a feature must have the same type of value ( ``BooleanValue`` , ``DoubleValue`` , ``LongValue`` or ``StringValue`` ).
        :param default_variation: The name of the variation to use as the default variation. The default variation is served to users who are not allocated to any ongoing launches or experiments of this feature. This variation must also be listed in the ``Variations`` structure. If you omit ``DefaultVariation`` , the first variation listed in the ``Variations`` structure is used as the default variation.
        :param description: An optional description of the feature.
        :param entity_overrides: Specify users that should always be served a specific variation of a feature. Each user is specified by a key-value pair . For each key, specify a user by entering their user ID, account ID, or some other identifier. For the value, specify the name of the variation that they are to be served.
        :param evaluation_strategy: Specify ``ALL_RULES`` to activate the traffic allocation specified by any ongoing launches or experiments. Specify ``DEFAULT_VARIATION`` to serve the default variation to all users instead.
        :param tags: Assigns one or more tags (key-value pairs) to the feature. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters. You can associate as many as 50 tags with a feature. For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_evidently as evidently
            
            cfn_feature_props = evidently.CfnFeatureProps(
                name="name",
                project="project",
                variations=[evidently.CfnFeature.VariationObjectProperty(
                    variation_name="variationName",
            
                    # the properties below are optional
                    boolean_value=False,
                    double_value=123,
                    long_value=123,
                    string_value="stringValue"
                )],
            
                # the properties below are optional
                default_variation="defaultVariation",
                description="description",
                entity_overrides=[evidently.CfnFeature.EntityOverrideProperty(
                    entity_id="entityId",
                    variation="variation"
                )],
                evaluation_strategy="evaluationStrategy",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fd5d4006d379348c243366df7a4e27203488741fbadb765bad2ae169ac59650)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument variations", value=variations, expected_type=type_hints["variations"])
            check_type(argname="argument default_variation", value=default_variation, expected_type=type_hints["default_variation"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument entity_overrides", value=entity_overrides, expected_type=type_hints["entity_overrides"])
            check_type(argname="argument evaluation_strategy", value=evaluation_strategy, expected_type=type_hints["evaluation_strategy"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "project": project,
            "variations": variations,
        }
        if default_variation is not None:
            self._values["default_variation"] = default_variation
        if description is not None:
            self._values["description"] = description
        if entity_overrides is not None:
            self._values["entity_overrides"] = entity_overrides
        if evaluation_strategy is not None:
            self._values["evaluation_strategy"] = evaluation_strategy
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name for the feature.

        It can include up to 127 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project(self) -> builtins.str:
        '''The name or ARN of the project that is to contain the new feature.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-project
        '''
        result = self._values.get("project")
        assert result is not None, "Required property 'project' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def variations(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFeature.VariationObjectProperty]]]:
        '''An array of structures that contain the configuration of the feature's different variations.

        Each ``VariationObject`` in the ``Variations`` array for a feature must have the same type of value ( ``BooleanValue`` , ``DoubleValue`` , ``LongValue`` or ``StringValue`` ).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-variations
        '''
        result = self._values.get("variations")
        assert result is not None, "Required property 'variations' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFeature.VariationObjectProperty]]], result)

    @builtins.property
    def default_variation(self) -> typing.Optional[builtins.str]:
        '''The name of the variation to use as the default variation.

        The default variation is served to users who are not allocated to any ongoing launches or experiments of this feature.

        This variation must also be listed in the ``Variations`` structure.

        If you omit ``DefaultVariation`` , the first variation listed in the ``Variations`` structure is used as the default variation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-defaultvariation
        '''
        result = self._values.get("default_variation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the feature.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def entity_overrides(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFeature.EntityOverrideProperty]]]]:
        '''Specify users that should always be served a specific variation of a feature.

        Each user is specified by a key-value pair . For each key, specify a user by entering their user ID, account ID, or some other identifier. For the value, specify the name of the variation that they are to be served.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-entityoverrides
        '''
        result = self._values.get("entity_overrides")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFeature.EntityOverrideProperty]]]], result)

    @builtins.property
    def evaluation_strategy(self) -> typing.Optional[builtins.str]:
        '''Specify ``ALL_RULES`` to activate the traffic allocation specified by any ongoing launches or experiments.

        Specify ``DEFAULT_VARIATION`` to serve the default variation to all users instead.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-evaluationstrategy
        '''
        result = self._values.get("evaluation_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Assigns one or more tags (key-value pairs) to the feature.

        Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

        Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters.

        You can associate as many as 50 tags with a feature.

        For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-feature.html#cfn-evidently-feature-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFeatureProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnLaunch(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_evidently.CfnLaunch",
):
    '''Creates or updates a *launch* of a given feature.

    Before you create a launch, you must create the feature to use for the launch.

    You can use a launch to safely validate new features by serving them to a specified percentage of your users while you roll out the feature. You can monitor the performance of the new feature to help you decide when to ramp up traffic to more users. This helps you reduce risk and identify unintended consequences before you fully launch the feature.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html
    :cloudformationResource: AWS::Evidently::Launch
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_evidently as evidently
        
        cfn_launch = evidently.CfnLaunch(self, "MyCfnLaunch",
            groups=[evidently.CfnLaunch.LaunchGroupObjectProperty(
                feature="feature",
                group_name="groupName",
                variation="variation",
        
                # the properties below are optional
                description="description"
            )],
            name="name",
            project="project",
            scheduled_splits_config=[evidently.CfnLaunch.StepConfigProperty(
                group_weights=[evidently.CfnLaunch.GroupToWeightProperty(
                    group_name="groupName",
                    split_weight=123
                )],
                start_time="startTime",
        
                # the properties below are optional
                segment_overrides=[evidently.CfnLaunch.SegmentOverrideProperty(
                    evaluation_order=123,
                    segment="segment",
                    weights=[evidently.CfnLaunch.GroupToWeightProperty(
                        group_name="groupName",
                        split_weight=123
                    )]
                )]
            )],
        
            # the properties below are optional
            description="description",
            execution_status=evidently.CfnLaunch.ExecutionStatusObjectProperty(
                status="status",
        
                # the properties below are optional
                desired_state="desiredState",
                reason="reason"
            ),
            metric_monitors=[evidently.CfnLaunch.MetricDefinitionObjectProperty(
                entity_id_key="entityIdKey",
                metric_name="metricName",
                value_key="valueKey",
        
                # the properties below are optional
                event_pattern="eventPattern",
                unit_label="unitLabel"
            )],
            randomization_salt="randomizationSalt",
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
        groups: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLaunch.LaunchGroupObjectProperty", typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        project: builtins.str,
        scheduled_splits_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLaunch.StepConfigProperty", typing.Dict[builtins.str, typing.Any]]]]],
        description: typing.Optional[builtins.str] = None,
        execution_status: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLaunch.ExecutionStatusObjectProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        metric_monitors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLaunch.MetricDefinitionObjectProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        randomization_salt: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param groups: An array of structures that contains the feature and variations that are to be used for the launch. You can up to five launch groups in a launch.
        :param name: The name for the launch. It can include up to 127 characters.
        :param project: The name or ARN of the project that you want to create the launch in.
        :param scheduled_splits_config: An array of structures that define the traffic allocation percentages among the feature variations during each step of the launch.
        :param description: An optional description for the launch.
        :param execution_status: A structure that you can use to start and stop the launch.
        :param metric_monitors: An array of structures that define the metrics that will be used to monitor the launch performance. You can have up to three metric monitors in the array.
        :param randomization_salt: When Evidently assigns a particular user session to a launch, it must use a randomization ID to determine which variation the user session is served. This randomization ID is a combination of the entity ID and ``randomizationSalt`` . If you omit ``randomizationSalt`` , Evidently uses the launch name as the ``randomizationsSalt`` .
        :param tags: Assigns one or more tags (key-value pairs) to the launch. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters. You can associate as many as 50 tags with a launch. For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07641dd92b44cb3b2e0643d2505ef488edfd1736b97c33b89a8c38fdc3e80e8c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLaunchProps(
            groups=groups,
            name=name,
            project=project,
            scheduled_splits_config=scheduled_splits_config,
            description=description,
            execution_status=execution_status,
            metric_monitors=metric_monitors,
            randomization_salt=randomization_salt,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f82face9c15f40bd628db171784d9b9f26806a3a18f70aa27fee0c7592c5b525)
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
            type_hints = typing.get_type_hints(_typecheckingstub__825ae81705137d3e2f989d5f3384d9fda4bde279fdb877ac1613c131132e0b72)
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
        '''The ARN of the launch.

        For example, ``arn:aws:evidently:us-west-2:0123455678912:project/myProject/launch/myLaunch``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    @jsii.member(jsii_name="groups")
    def groups(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLaunch.LaunchGroupObjectProperty"]]]:
        '''An array of structures that contains the feature and variations that are to be used for the launch.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLaunch.LaunchGroupObjectProperty"]]], jsii.get(self, "groups"))

    @groups.setter
    def groups(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLaunch.LaunchGroupObjectProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd24dbcf6b27e75d516fcab8552edc84e63fbab001d5a0b07fe75bd2161b3d08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groups", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name for the launch.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d883d03ce939a559b1ee5665300adb157d5f5932d26a6a688ffc497ec4acab1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        '''The name or ARN of the project that you want to create the launch in.'''
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__868659d5505d8ceefc8d34d5c4e9a9b227a2f3aee237f2ebf5f5edb362ffb73b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="scheduledSplitsConfig")
    def scheduled_splits_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLaunch.StepConfigProperty"]]]:
        '''An array of structures that define the traffic allocation percentages among the feature variations during each step of the launch.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLaunch.StepConfigProperty"]]], jsii.get(self, "scheduledSplitsConfig"))

    @scheduled_splits_config.setter
    def scheduled_splits_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLaunch.StepConfigProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__353ad69c0312cbb355b090decf45009d0f35cfd3174fb1768cda62970dd90e3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduledSplitsConfig", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description for the launch.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc70efb99bfb081f4aadbdff15dd4f340b1f730d9f6b9e5b55c5d1bce9662aea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="executionStatus")
    def execution_status(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLaunch.ExecutionStatusObjectProperty"]]:
        '''A structure that you can use to start and stop the launch.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLaunch.ExecutionStatusObjectProperty"]], jsii.get(self, "executionStatus"))

    @execution_status.setter
    def execution_status(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLaunch.ExecutionStatusObjectProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62fb950dcca9c33f47ee901068ff569f19d2c54c24fd80f64fe62c91549eb16d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionStatus", value)

    @builtins.property
    @jsii.member(jsii_name="metricMonitors")
    def metric_monitors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLaunch.MetricDefinitionObjectProperty"]]]]:
        '''An array of structures that define the metrics that will be used to monitor the launch performance.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLaunch.MetricDefinitionObjectProperty"]]]], jsii.get(self, "metricMonitors"))

    @metric_monitors.setter
    def metric_monitors(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLaunch.MetricDefinitionObjectProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72d460c5d783a1b583d7e0ff21f1c468740fdd12724891a96b32387d12665ced)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricMonitors", value)

    @builtins.property
    @jsii.member(jsii_name="randomizationSalt")
    def randomization_salt(self) -> typing.Optional[builtins.str]:
        '''When Evidently assigns a particular user session to a launch, it must use a randomization ID to determine which variation the user session is served.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "randomizationSalt"))

    @randomization_salt.setter
    def randomization_salt(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03ac24e1a4c45b370a39be9770f35e0dcec3ca0f42b47fe4dfd61f440ab2465d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "randomizationSalt", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Assigns one or more tags (key-value pairs) to the launch.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10b8aca9ed0c9918ec1dddb03aba9046d4089f9d1d756bd5bc04a138123e650e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnLaunch.ExecutionStatusObjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "status": "status",
            "desired_state": "desiredState",
            "reason": "reason",
        },
    )
    class ExecutionStatusObjectProperty:
        def __init__(
            self,
            *,
            status: builtins.str,
            desired_state: typing.Optional[builtins.str] = None,
            reason: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Use this structure to start and stop the launch.

            :param status: To start the launch now, specify ``START`` for this parameter. If this launch is currently running and you want to stop it now, specify ``STOP`` .
            :param desired_state: If you are using AWS CloudFormation to stop this launch, specify either ``COMPLETED`` or ``CANCELLED`` here to indicate how to classify this experiment. If you omit this parameter, the default of ``COMPLETED`` is used.
            :param reason: If you are using AWS CloudFormation to stop this launch, this is an optional field that you can use to record why the launch is being stopped or cancelled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-executionstatusobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                execution_status_object_property = evidently.CfnLaunch.ExecutionStatusObjectProperty(
                    status="status",
                
                    # the properties below are optional
                    desired_state="desiredState",
                    reason="reason"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c41f2a053e29f11510b61bf4d21e3f30ad6180748b3269a24f3cfbb55ff7907e)
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument desired_state", value=desired_state, expected_type=type_hints["desired_state"])
                check_type(argname="argument reason", value=reason, expected_type=type_hints["reason"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "status": status,
            }
            if desired_state is not None:
                self._values["desired_state"] = desired_state
            if reason is not None:
                self._values["reason"] = reason

        @builtins.property
        def status(self) -> builtins.str:
            '''To start the launch now, specify ``START`` for this parameter.

            If this launch is currently running and you want to stop it now, specify ``STOP`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-executionstatusobject.html#cfn-evidently-launch-executionstatusobject-status
            '''
            result = self._values.get("status")
            assert result is not None, "Required property 'status' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def desired_state(self) -> typing.Optional[builtins.str]:
            '''If you are using AWS CloudFormation to stop this launch, specify either ``COMPLETED`` or ``CANCELLED`` here to indicate how to classify this experiment.

            If you omit this parameter, the default of ``COMPLETED`` is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-executionstatusobject.html#cfn-evidently-launch-executionstatusobject-desiredstate
            '''
            result = self._values.get("desired_state")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def reason(self) -> typing.Optional[builtins.str]:
            '''If you are using AWS CloudFormation to stop this launch, this is an optional field that you can use to record why the launch is being stopped or cancelled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-executionstatusobject.html#cfn-evidently-launch-executionstatusobject-reason
            '''
            result = self._values.get("reason")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExecutionStatusObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnLaunch.GroupToWeightProperty",
        jsii_struct_bases=[],
        name_mapping={"group_name": "groupName", "split_weight": "splitWeight"},
    )
    class GroupToWeightProperty:
        def __init__(
            self,
            *,
            group_name: builtins.str,
            split_weight: jsii.Number,
        ) -> None:
            '''A structure containing the percentage of launch traffic to allocate to one launch group.

            :param group_name: The name of the launch group. It can include up to 127 characters.
            :param split_weight: The portion of launch traffic to allocate to this launch group. This is represented in thousandths of a percent. For example, specify 20,000 to allocate 20% of the launch audience to this launch group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-grouptoweight.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                group_to_weight_property = evidently.CfnLaunch.GroupToWeightProperty(
                    group_name="groupName",
                    split_weight=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__05e698714e343cb2346580a81618d117ef1a248bf020187e7bfb3b438e20a0cc)
                check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
                check_type(argname="argument split_weight", value=split_weight, expected_type=type_hints["split_weight"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "group_name": group_name,
                "split_weight": split_weight,
            }

        @builtins.property
        def group_name(self) -> builtins.str:
            '''The name of the launch group.

            It can include up to 127 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-grouptoweight.html#cfn-evidently-launch-grouptoweight-groupname
            '''
            result = self._values.get("group_name")
            assert result is not None, "Required property 'group_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def split_weight(self) -> jsii.Number:
            '''The portion of launch traffic to allocate to this launch group.

            This is represented in thousandths of a percent. For example, specify 20,000 to allocate 20% of the launch audience to this launch group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-grouptoweight.html#cfn-evidently-launch-grouptoweight-splitweight
            '''
            result = self._values.get("split_weight")
            assert result is not None, "Required property 'split_weight' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GroupToWeightProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnLaunch.LaunchGroupObjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "feature": "feature",
            "group_name": "groupName",
            "variation": "variation",
            "description": "description",
        },
    )
    class LaunchGroupObjectProperty:
        def __init__(
            self,
            *,
            feature: builtins.str,
            group_name: builtins.str,
            variation: builtins.str,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure that defines one launch group in a launch.

            A launch group is a variation of the feature that you are including in the launch.

            :param feature: The feature that this launch is using.
            :param group_name: A name for this launch group. It can include up to 127 characters.
            :param variation: The feature variation to use for this launch group.
            :param description: A description of the launch group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-launchgroupobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                launch_group_object_property = evidently.CfnLaunch.LaunchGroupObjectProperty(
                    feature="feature",
                    group_name="groupName",
                    variation="variation",
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__09b94cd149d14080b3ae78bd1042b93dbc7ae40cdf44fb8dcbe1448aafb2e70e)
                check_type(argname="argument feature", value=feature, expected_type=type_hints["feature"])
                check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
                check_type(argname="argument variation", value=variation, expected_type=type_hints["variation"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "feature": feature,
                "group_name": group_name,
                "variation": variation,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def feature(self) -> builtins.str:
            '''The feature that this launch is using.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-launchgroupobject.html#cfn-evidently-launch-launchgroupobject-feature
            '''
            result = self._values.get("feature")
            assert result is not None, "Required property 'feature' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def group_name(self) -> builtins.str:
            '''A name for this launch group.

            It can include up to 127 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-launchgroupobject.html#cfn-evidently-launch-launchgroupobject-groupname
            '''
            result = self._values.get("group_name")
            assert result is not None, "Required property 'group_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def variation(self) -> builtins.str:
            '''The feature variation to use for this launch group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-launchgroupobject.html#cfn-evidently-launch-launchgroupobject-variation
            '''
            result = self._values.get("variation")
            assert result is not None, "Required property 'variation' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''A description of the launch group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-launchgroupobject.html#cfn-evidently-launch-launchgroupobject-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LaunchGroupObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnLaunch.MetricDefinitionObjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "entity_id_key": "entityIdKey",
            "metric_name": "metricName",
            "value_key": "valueKey",
            "event_pattern": "eventPattern",
            "unit_label": "unitLabel",
        },
    )
    class MetricDefinitionObjectProperty:
        def __init__(
            self,
            *,
            entity_id_key: builtins.str,
            metric_name: builtins.str,
            value_key: builtins.str,
            event_pattern: typing.Optional[builtins.str] = None,
            unit_label: typing.Optional[builtins.str] = None,
        ) -> None:
            '''This structure defines a metric that you want to use to evaluate the variations during a launch or experiment.

            :param entity_id_key: The entity, such as a user or session, that does an action that causes a metric value to be recorded. An example is ``userDetails.userID`` .
            :param metric_name: A name for the metric. It can include up to 255 characters.
            :param value_key: The value that is tracked to produce the metric.
            :param event_pattern: The EventBridge event pattern that defines how the metric is recorded. For more information about EventBridge event patterns, see `Amazon EventBridge event patterns <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html>`_ .
            :param unit_label: A label for the units that the metric is measuring.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-metricdefinitionobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                metric_definition_object_property = evidently.CfnLaunch.MetricDefinitionObjectProperty(
                    entity_id_key="entityIdKey",
                    metric_name="metricName",
                    value_key="valueKey",
                
                    # the properties below are optional
                    event_pattern="eventPattern",
                    unit_label="unitLabel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f0cd0caab401461cbc053e72bbbc53b44f4b9fbe3e9d2221a2eb44f15dbb8d2d)
                check_type(argname="argument entity_id_key", value=entity_id_key, expected_type=type_hints["entity_id_key"])
                check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
                check_type(argname="argument value_key", value=value_key, expected_type=type_hints["value_key"])
                check_type(argname="argument event_pattern", value=event_pattern, expected_type=type_hints["event_pattern"])
                check_type(argname="argument unit_label", value=unit_label, expected_type=type_hints["unit_label"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "entity_id_key": entity_id_key,
                "metric_name": metric_name,
                "value_key": value_key,
            }
            if event_pattern is not None:
                self._values["event_pattern"] = event_pattern
            if unit_label is not None:
                self._values["unit_label"] = unit_label

        @builtins.property
        def entity_id_key(self) -> builtins.str:
            '''The entity, such as a user or session, that does an action that causes a metric value to be recorded.

            An example is ``userDetails.userID`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-metricdefinitionobject.html#cfn-evidently-launch-metricdefinitionobject-entityidkey
            '''
            result = self._values.get("entity_id_key")
            assert result is not None, "Required property 'entity_id_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''A name for the metric.

            It can include up to 255 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-metricdefinitionobject.html#cfn-evidently-launch-metricdefinitionobject-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value_key(self) -> builtins.str:
            '''The value that is tracked to produce the metric.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-metricdefinitionobject.html#cfn-evidently-launch-metricdefinitionobject-valuekey
            '''
            result = self._values.get("value_key")
            assert result is not None, "Required property 'value_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def event_pattern(self) -> typing.Optional[builtins.str]:
            '''The EventBridge event pattern that defines how the metric is recorded.

            For more information about EventBridge event patterns, see `Amazon EventBridge event patterns <https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-metricdefinitionobject.html#cfn-evidently-launch-metricdefinitionobject-eventpattern
            '''
            result = self._values.get("event_pattern")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def unit_label(self) -> typing.Optional[builtins.str]:
            '''A label for the units that the metric is measuring.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-metricdefinitionobject.html#cfn-evidently-launch-metricdefinitionobject-unitlabel
            '''
            result = self._values.get("unit_label")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricDefinitionObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnLaunch.SegmentOverrideProperty",
        jsii_struct_bases=[],
        name_mapping={
            "evaluation_order": "evaluationOrder",
            "segment": "segment",
            "weights": "weights",
        },
    )
    class SegmentOverrideProperty:
        def __init__(
            self,
            *,
            evaluation_order: jsii.Number,
            segment: builtins.str,
            weights: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLaunch.GroupToWeightProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Use this structure to specify different traffic splits for one or more audience *segments* .

            A segment is a portion of your audience that share one or more characteristics. Examples could be Chrome browser users, users in Europe, or Firefox browser users in Europe who also fit other criteria that your application collects, such as age.

            For more information, see `Use segments to focus your audience <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-segments.html>`_ .

            This sructure is an array of up to six segment override objects. Each of these objects specifies a segment that you have already created, and defines the traffic split for that segment.

            :param evaluation_order: A number indicating the order to use to evaluate segment overrides, if there are more than one. Segment overrides with lower numbers are evaluated first.
            :param segment: The ARN of the segment to use for this override.
            :param weights: The traffic allocation percentages among the feature variations to assign to this segment. This is a set of key-value pairs. The keys are variation names. The values represent the amount of traffic to allocate to that variation for this segment. This is expressed in thousandths of a percent, so a weight of 50000 represents 50% of traffic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-segmentoverride.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                segment_override_property = evidently.CfnLaunch.SegmentOverrideProperty(
                    evaluation_order=123,
                    segment="segment",
                    weights=[evidently.CfnLaunch.GroupToWeightProperty(
                        group_name="groupName",
                        split_weight=123
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f2da51a2fd01ffbc20b66c20d0dc6d1a2eecf35edacb6c65b8e4a4c0888426fb)
                check_type(argname="argument evaluation_order", value=evaluation_order, expected_type=type_hints["evaluation_order"])
                check_type(argname="argument segment", value=segment, expected_type=type_hints["segment"])
                check_type(argname="argument weights", value=weights, expected_type=type_hints["weights"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "evaluation_order": evaluation_order,
                "segment": segment,
                "weights": weights,
            }

        @builtins.property
        def evaluation_order(self) -> jsii.Number:
            '''A number indicating the order to use to evaluate segment overrides, if there are more than one.

            Segment overrides with lower numbers are evaluated first.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-segmentoverride.html#cfn-evidently-launch-segmentoverride-evaluationorder
            '''
            result = self._values.get("evaluation_order")
            assert result is not None, "Required property 'evaluation_order' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def segment(self) -> builtins.str:
            '''The ARN of the segment to use for this override.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-segmentoverride.html#cfn-evidently-launch-segmentoverride-segment
            '''
            result = self._values.get("segment")
            assert result is not None, "Required property 'segment' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def weights(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLaunch.GroupToWeightProperty"]]]:
            '''The traffic allocation percentages among the feature variations to assign to this segment.

            This is a set of key-value pairs. The keys are variation names. The values represent the amount of traffic to allocate to that variation for this segment. This is expressed in thousandths of a percent, so a weight of 50000 represents 50% of traffic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-segmentoverride.html#cfn-evidently-launch-segmentoverride-weights
            '''
            result = self._values.get("weights")
            assert result is not None, "Required property 'weights' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLaunch.GroupToWeightProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SegmentOverrideProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnLaunch.StepConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "group_weights": "groupWeights",
            "start_time": "startTime",
            "segment_overrides": "segmentOverrides",
        },
    )
    class StepConfigProperty:
        def __init__(
            self,
            *,
            group_weights: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLaunch.GroupToWeightProperty", typing.Dict[builtins.str, typing.Any]]]]],
            start_time: builtins.str,
            segment_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLaunch.SegmentOverrideProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''A structure that defines when each step of the launch is to start, and how much launch traffic is to be allocated to each variation during each step.

            :param group_weights: An array of structures that define how much launch traffic to allocate to each launch group during this step of the launch.
            :param start_time: The date and time to start this step of the launch. Use UTC format, ``yyyy-MM-ddTHH:mm:ssZ`` . For example, ``2025-11-25T23:59:59Z``
            :param segment_overrides: An array of structures that you can use to specify different traffic splits for one or more audience *segments* . A segment is a portion of your audience that share one or more characteristics. Examples could be Chrome browser users, users in Europe, or Firefox browser users in Europe who also fit other criteria that your application collects, such as age. For more information, see `Use segments to focus your audience <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-segments.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-stepconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                step_config_property = evidently.CfnLaunch.StepConfigProperty(
                    group_weights=[evidently.CfnLaunch.GroupToWeightProperty(
                        group_name="groupName",
                        split_weight=123
                    )],
                    start_time="startTime",
                
                    # the properties below are optional
                    segment_overrides=[evidently.CfnLaunch.SegmentOverrideProperty(
                        evaluation_order=123,
                        segment="segment",
                        weights=[evidently.CfnLaunch.GroupToWeightProperty(
                            group_name="groupName",
                            split_weight=123
                        )]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__53dab4eaa2aacc5ea0d3c97532af5d0ff1af68ac00101231878cc8d514e7aba2)
                check_type(argname="argument group_weights", value=group_weights, expected_type=type_hints["group_weights"])
                check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
                check_type(argname="argument segment_overrides", value=segment_overrides, expected_type=type_hints["segment_overrides"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "group_weights": group_weights,
                "start_time": start_time,
            }
            if segment_overrides is not None:
                self._values["segment_overrides"] = segment_overrides

        @builtins.property
        def group_weights(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLaunch.GroupToWeightProperty"]]]:
            '''An array of structures that define how much launch traffic to allocate to each launch group during this step of the launch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-stepconfig.html#cfn-evidently-launch-stepconfig-groupweights
            '''
            result = self._values.get("group_weights")
            assert result is not None, "Required property 'group_weights' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLaunch.GroupToWeightProperty"]]], result)

        @builtins.property
        def start_time(self) -> builtins.str:
            '''The date and time to start this step of the launch.

            Use UTC format, ``yyyy-MM-ddTHH:mm:ssZ`` . For example, ``2025-11-25T23:59:59Z``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-stepconfig.html#cfn-evidently-launch-stepconfig-starttime
            '''
            result = self._values.get("start_time")
            assert result is not None, "Required property 'start_time' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def segment_overrides(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLaunch.SegmentOverrideProperty"]]]]:
            '''An array of structures that you can use to specify different traffic splits for one or more audience *segments* .

            A segment is a portion of your audience that share one or more characteristics. Examples could be Chrome browser users, users in Europe, or Firefox browser users in Europe who also fit other criteria that your application collects, such as age.

            For more information, see `Use segments to focus your audience <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-segments.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-launch-stepconfig.html#cfn-evidently-launch-stepconfig-segmentoverrides
            '''
            result = self._values.get("segment_overrides")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLaunch.SegmentOverrideProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StepConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_evidently.CfnLaunchProps",
    jsii_struct_bases=[],
    name_mapping={
        "groups": "groups",
        "name": "name",
        "project": "project",
        "scheduled_splits_config": "scheduledSplitsConfig",
        "description": "description",
        "execution_status": "executionStatus",
        "metric_monitors": "metricMonitors",
        "randomization_salt": "randomizationSalt",
        "tags": "tags",
    },
)
class CfnLaunchProps:
    def __init__(
        self,
        *,
        groups: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLaunch.LaunchGroupObjectProperty, typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        project: builtins.str,
        scheduled_splits_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLaunch.StepConfigProperty, typing.Dict[builtins.str, typing.Any]]]]],
        description: typing.Optional[builtins.str] = None,
        execution_status: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLaunch.ExecutionStatusObjectProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        metric_monitors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLaunch.MetricDefinitionObjectProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        randomization_salt: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLaunch``.

        :param groups: An array of structures that contains the feature and variations that are to be used for the launch. You can up to five launch groups in a launch.
        :param name: The name for the launch. It can include up to 127 characters.
        :param project: The name or ARN of the project that you want to create the launch in.
        :param scheduled_splits_config: An array of structures that define the traffic allocation percentages among the feature variations during each step of the launch.
        :param description: An optional description for the launch.
        :param execution_status: A structure that you can use to start and stop the launch.
        :param metric_monitors: An array of structures that define the metrics that will be used to monitor the launch performance. You can have up to three metric monitors in the array.
        :param randomization_salt: When Evidently assigns a particular user session to a launch, it must use a randomization ID to determine which variation the user session is served. This randomization ID is a combination of the entity ID and ``randomizationSalt`` . If you omit ``randomizationSalt`` , Evidently uses the launch name as the ``randomizationsSalt`` .
        :param tags: Assigns one or more tags (key-value pairs) to the launch. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters. You can associate as many as 50 tags with a launch. For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_evidently as evidently
            
            cfn_launch_props = evidently.CfnLaunchProps(
                groups=[evidently.CfnLaunch.LaunchGroupObjectProperty(
                    feature="feature",
                    group_name="groupName",
                    variation="variation",
            
                    # the properties below are optional
                    description="description"
                )],
                name="name",
                project="project",
                scheduled_splits_config=[evidently.CfnLaunch.StepConfigProperty(
                    group_weights=[evidently.CfnLaunch.GroupToWeightProperty(
                        group_name="groupName",
                        split_weight=123
                    )],
                    start_time="startTime",
            
                    # the properties below are optional
                    segment_overrides=[evidently.CfnLaunch.SegmentOverrideProperty(
                        evaluation_order=123,
                        segment="segment",
                        weights=[evidently.CfnLaunch.GroupToWeightProperty(
                            group_name="groupName",
                            split_weight=123
                        )]
                    )]
                )],
            
                # the properties below are optional
                description="description",
                execution_status=evidently.CfnLaunch.ExecutionStatusObjectProperty(
                    status="status",
            
                    # the properties below are optional
                    desired_state="desiredState",
                    reason="reason"
                ),
                metric_monitors=[evidently.CfnLaunch.MetricDefinitionObjectProperty(
                    entity_id_key="entityIdKey",
                    metric_name="metricName",
                    value_key="valueKey",
            
                    # the properties below are optional
                    event_pattern="eventPattern",
                    unit_label="unitLabel"
                )],
                randomization_salt="randomizationSalt",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20a136d1b38127f4fb34c7d6619d1b4038b0d2be6c3ce76d9f52535d191c3021)
            check_type(argname="argument groups", value=groups, expected_type=type_hints["groups"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument scheduled_splits_config", value=scheduled_splits_config, expected_type=type_hints["scheduled_splits_config"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument execution_status", value=execution_status, expected_type=type_hints["execution_status"])
            check_type(argname="argument metric_monitors", value=metric_monitors, expected_type=type_hints["metric_monitors"])
            check_type(argname="argument randomization_salt", value=randomization_salt, expected_type=type_hints["randomization_salt"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "groups": groups,
            "name": name,
            "project": project,
            "scheduled_splits_config": scheduled_splits_config,
        }
        if description is not None:
            self._values["description"] = description
        if execution_status is not None:
            self._values["execution_status"] = execution_status
        if metric_monitors is not None:
            self._values["metric_monitors"] = metric_monitors
        if randomization_salt is not None:
            self._values["randomization_salt"] = randomization_salt
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def groups(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLaunch.LaunchGroupObjectProperty]]]:
        '''An array of structures that contains the feature and variations that are to be used for the launch.

        You can up to five launch groups in a launch.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-groups
        '''
        result = self._values.get("groups")
        assert result is not None, "Required property 'groups' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLaunch.LaunchGroupObjectProperty]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name for the launch.

        It can include up to 127 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project(self) -> builtins.str:
        '''The name or ARN of the project that you want to create the launch in.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-project
        '''
        result = self._values.get("project")
        assert result is not None, "Required property 'project' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scheduled_splits_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLaunch.StepConfigProperty]]]:
        '''An array of structures that define the traffic allocation percentages among the feature variations during each step of the launch.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-scheduledsplitsconfig
        '''
        result = self._values.get("scheduled_splits_config")
        assert result is not None, "Required property 'scheduled_splits_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLaunch.StepConfigProperty]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description for the launch.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_status(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLaunch.ExecutionStatusObjectProperty]]:
        '''A structure that you can use to start and stop the launch.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-executionstatus
        '''
        result = self._values.get("execution_status")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLaunch.ExecutionStatusObjectProperty]], result)

    @builtins.property
    def metric_monitors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLaunch.MetricDefinitionObjectProperty]]]]:
        '''An array of structures that define the metrics that will be used to monitor the launch performance.

        You can have up to three metric monitors in the array.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-metricmonitors
        '''
        result = self._values.get("metric_monitors")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLaunch.MetricDefinitionObjectProperty]]]], result)

    @builtins.property
    def randomization_salt(self) -> typing.Optional[builtins.str]:
        '''When Evidently assigns a particular user session to a launch, it must use a randomization ID to determine which variation the user session is served.

        This randomization ID is a combination of the entity ID and ``randomizationSalt`` . If you omit ``randomizationSalt`` , Evidently uses the launch name as the ``randomizationsSalt`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-randomizationsalt
        '''
        result = self._values.get("randomization_salt")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Assigns one or more tags (key-value pairs) to the launch.

        Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

        Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters.

        You can associate as many as 50 tags with a launch.

        For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-launch.html#cfn-evidently-launch-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLaunchProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnProject(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_evidently.CfnProject",
):
    '''Creates a project, which is the logical object in Evidently that can contain features, launches, and experiments.

    Use projects to group similar features together.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html
    :cloudformationResource: AWS::Evidently::Project
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_evidently as evidently
        
        cfn_project = evidently.CfnProject(self, "MyCfnProject",
            name="name",
        
            # the properties below are optional
            app_config_resource=evidently.CfnProject.AppConfigResourceObjectProperty(
                application_id="applicationId",
                environment_id="environmentId"
            ),
            data_delivery=evidently.CfnProject.DataDeliveryObjectProperty(
                log_group="logGroup",
                s3=evidently.CfnProject.S3DestinationProperty(
                    bucket_name="bucketName",
        
                    # the properties below are optional
                    prefix="prefix"
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
        name: builtins.str,
        app_config_resource: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnProject.AppConfigResourceObjectProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        data_delivery: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnProject.DataDeliveryObjectProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name for the project. It can include up to 127 characters.
        :param app_config_resource: Use this parameter if the project will use *client-side evaluation powered by AWS AppConfig* . Client-side evaluation allows your application to assign variations to user sessions locally instead of by calling the `EvaluateFeature <https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_EvaluateFeature.html>`_ operation. This mitigates the latency and availability risks that come with an API call. For more information, see `Use client-side evaluation - powered by AWS AppConfig . <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-client-side-evaluation.html>`_ This parameter is a structure that contains information about the AWS AppConfig application that will be used as for client-side evaluation. To create a project that uses client-side evaluation, you must have the ``evidently:ExportProjectAsConfiguration`` permission.
        :param data_delivery: A structure that contains information about where Evidently is to store evaluation events for longer term storage, if you choose to do so. If you choose not to store these events, Evidently deletes them after using them to produce metrics and other experiment results that you can view. You can't specify both ``CloudWatchLogs`` and ``S3Destination`` in the same operation.
        :param description: An optional description of the project.
        :param tags: Assigns one or more tags (key-value pairs) to the project. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters. You can associate as many as 50 tags with a project. For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aff4f82edbe2ec588dd5ba5124dc949189afd4900acb296b20585139e3090ef5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProjectProps(
            name=name,
            app_config_resource=app_config_resource,
            data_delivery=data_delivery,
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
            type_hints = typing.get_type_hints(_typecheckingstub__f90a3f01e36e216b5f22034fb6f3bc0441250ad2e5836f18853fd17e2aa28d2b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__211fe4575fffc7e26414586e2fb35b683eb7c77759d1cce9aa3ada8f4c11d62e)
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
        '''The ARN of the project.

        For example, ``arn:aws:evidently:us-west-2:0123455678912:project/myProject``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
        '''The name for the project.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6253b333d7062dea9649fbe8b2a501689621e3306cdfc83ca650b0c286c8180e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="appConfigResource")
    def app_config_resource(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnProject.AppConfigResourceObjectProperty"]]:
        '''Use this parameter if the project will use *client-side evaluation powered by AWS AppConfig* .'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnProject.AppConfigResourceObjectProperty"]], jsii.get(self, "appConfigResource"))

    @app_config_resource.setter
    def app_config_resource(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnProject.AppConfigResourceObjectProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__839d7fab373b2b68743dd50f95e3601bb6fad99024909ea6c4fafc4a1f81f7d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appConfigResource", value)

    @builtins.property
    @jsii.member(jsii_name="dataDelivery")
    def data_delivery(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnProject.DataDeliveryObjectProperty"]]:
        '''A structure that contains information about where Evidently is to store evaluation events for longer term storage, if you choose to do so.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnProject.DataDeliveryObjectProperty"]], jsii.get(self, "dataDelivery"))

    @data_delivery.setter
    def data_delivery(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnProject.DataDeliveryObjectProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8c0d4732b3a336b47854521db2baec1b07649626695e868d1d8ad744e8aeb6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataDelivery", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the project.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecaf44aad5a449686fad8267b62886895dd7a6f65f4eb1c8efa688e27a3c0b1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Assigns one or more tags (key-value pairs) to the project.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf0a54e7cf0c37d82554cdade5042d2b06c498c4099b1925825853dfcfe89060)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnProject.AppConfigResourceObjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "application_id": "applicationId",
            "environment_id": "environmentId",
        },
    )
    class AppConfigResourceObjectProperty:
        def __init__(
            self,
            *,
            application_id: builtins.str,
            environment_id: builtins.str,
        ) -> None:
            '''This is a structure that defines the configuration of how your application integrates with AWS AppConfig to run client-side evaluation.

            :param application_id: The ID of the AWS AppConfig application to use for client-side evaluation.
            :param environment_id: The ID of the AWS AppConfig environment to use for client-side evaluation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-appconfigresourceobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                app_config_resource_object_property = evidently.CfnProject.AppConfigResourceObjectProperty(
                    application_id="applicationId",
                    environment_id="environmentId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9a4d80453cc441893eb52e9312be0179a8a1ca794601606d79106337a21f337d)
                check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
                check_type(argname="argument environment_id", value=environment_id, expected_type=type_hints["environment_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "application_id": application_id,
                "environment_id": environment_id,
            }

        @builtins.property
        def application_id(self) -> builtins.str:
            '''The ID of the AWS AppConfig application to use for client-side evaluation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-appconfigresourceobject.html#cfn-evidently-project-appconfigresourceobject-applicationid
            '''
            result = self._values.get("application_id")
            assert result is not None, "Required property 'application_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def environment_id(self) -> builtins.str:
            '''The ID of the AWS AppConfig environment to use for client-side evaluation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-appconfigresourceobject.html#cfn-evidently-project-appconfigresourceobject-environmentid
            '''
            result = self._values.get("environment_id")
            assert result is not None, "Required property 'environment_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AppConfigResourceObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnProject.DataDeliveryObjectProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group": "logGroup", "s3": "s3"},
    )
    class DataDeliveryObjectProperty:
        def __init__(
            self,
            *,
            log_group: typing.Optional[builtins.str] = None,
            s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnProject.S3DestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A structure that contains information about where Evidently is to store evaluation events for longer term storage.

            :param log_group: If the project stores evaluation events in CloudWatch Logs , this structure stores the log group name.
            :param s3: If the project stores evaluation events in an Amazon S3 bucket, this structure stores the bucket name and bucket prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-datadeliveryobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                data_delivery_object_property = evidently.CfnProject.DataDeliveryObjectProperty(
                    log_group="logGroup",
                    s3=evidently.CfnProject.S3DestinationProperty(
                        bucket_name="bucketName",
                
                        # the properties below are optional
                        prefix="prefix"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ba3358915caa3d43c2df05a1f34987d23fbc194d5df2200428546c99dd9b3487)
                check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_group is not None:
                self._values["log_group"] = log_group
            if s3 is not None:
                self._values["s3"] = s3

        @builtins.property
        def log_group(self) -> typing.Optional[builtins.str]:
            '''If the project stores evaluation events in CloudWatch Logs , this structure stores the log group name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-datadeliveryobject.html#cfn-evidently-project-datadeliveryobject-loggroup
            '''
            result = self._values.get("log_group")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnProject.S3DestinationProperty"]]:
            '''If the project stores evaluation events in an Amazon S3 bucket, this structure stores the bucket name and bucket prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-datadeliveryobject.html#cfn-evidently-project-datadeliveryobject-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnProject.S3DestinationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataDeliveryObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_evidently.CfnProject.S3DestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_name": "bucketName", "prefix": "prefix"},
    )
    class S3DestinationProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''If the project stores evaluation events in an Amazon S3 bucket, this structure stores the bucket name and bucket prefix.

            :param bucket_name: The name of the bucket in which Evidently stores evaluation events.
            :param prefix: The bucket prefix in which Evidently stores evaluation events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-s3destination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_evidently as evidently
                
                s3_destination_property = evidently.CfnProject.S3DestinationProperty(
                    bucket_name="bucketName",
                
                    # the properties below are optional
                    prefix="prefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__935dc8f5ef3388acf3a2b6c49314a8bbe0d39ba91cc2d1a203206a8e7bd273ae)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
            }
            if prefix is not None:
                self._values["prefix"] = prefix

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''The name of the bucket in which Evidently stores evaluation events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-s3destination.html#cfn-evidently-project-s3destination-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''The bucket prefix in which Evidently stores evaluation events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-evidently-project-s3destination.html#cfn-evidently-project-s3destination-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3DestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_evidently.CfnProjectProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "app_config_resource": "appConfigResource",
        "data_delivery": "dataDelivery",
        "description": "description",
        "tags": "tags",
    },
)
class CfnProjectProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        app_config_resource: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProject.AppConfigResourceObjectProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        data_delivery: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProject.DataDeliveryObjectProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnProject``.

        :param name: The name for the project. It can include up to 127 characters.
        :param app_config_resource: Use this parameter if the project will use *client-side evaluation powered by AWS AppConfig* . Client-side evaluation allows your application to assign variations to user sessions locally instead of by calling the `EvaluateFeature <https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_EvaluateFeature.html>`_ operation. This mitigates the latency and availability risks that come with an API call. For more information, see `Use client-side evaluation - powered by AWS AppConfig . <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-client-side-evaluation.html>`_ This parameter is a structure that contains information about the AWS AppConfig application that will be used as for client-side evaluation. To create a project that uses client-side evaluation, you must have the ``evidently:ExportProjectAsConfiguration`` permission.
        :param data_delivery: A structure that contains information about where Evidently is to store evaluation events for longer term storage, if you choose to do so. If you choose not to store these events, Evidently deletes them after using them to produce metrics and other experiment results that you can view. You can't specify both ``CloudWatchLogs`` and ``S3Destination`` in the same operation.
        :param description: An optional description of the project.
        :param tags: Assigns one or more tags (key-value pairs) to the project. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters. You can associate as many as 50 tags with a project. For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_evidently as evidently
            
            cfn_project_props = evidently.CfnProjectProps(
                name="name",
            
                # the properties below are optional
                app_config_resource=evidently.CfnProject.AppConfigResourceObjectProperty(
                    application_id="applicationId",
                    environment_id="environmentId"
                ),
                data_delivery=evidently.CfnProject.DataDeliveryObjectProperty(
                    log_group="logGroup",
                    s3=evidently.CfnProject.S3DestinationProperty(
                        bucket_name="bucketName",
            
                        # the properties below are optional
                        prefix="prefix"
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
            type_hints = typing.get_type_hints(_typecheckingstub__ac738cde3fd44d5472b342dd1f8c8a1576f7a69d882c6c2b152887958091799f)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument app_config_resource", value=app_config_resource, expected_type=type_hints["app_config_resource"])
            check_type(argname="argument data_delivery", value=data_delivery, expected_type=type_hints["data_delivery"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if app_config_resource is not None:
            self._values["app_config_resource"] = app_config_resource
        if data_delivery is not None:
            self._values["data_delivery"] = data_delivery
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name for the project.

        It can include up to 127 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html#cfn-evidently-project-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_config_resource(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnProject.AppConfigResourceObjectProperty]]:
        '''Use this parameter if the project will use *client-side evaluation powered by AWS AppConfig* .

        Client-side evaluation allows your application to assign variations to user sessions locally instead of by calling the `EvaluateFeature <https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_EvaluateFeature.html>`_ operation. This mitigates the latency and availability risks that come with an API call. For more information, see `Use client-side evaluation - powered by AWS AppConfig . <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-client-side-evaluation.html>`_

        This parameter is a structure that contains information about the AWS AppConfig application that will be used as for client-side evaluation.

        To create a project that uses client-side evaluation, you must have the ``evidently:ExportProjectAsConfiguration`` permission.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html#cfn-evidently-project-appconfigresource
        '''
        result = self._values.get("app_config_resource")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnProject.AppConfigResourceObjectProperty]], result)

    @builtins.property
    def data_delivery(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnProject.DataDeliveryObjectProperty]]:
        '''A structure that contains information about where Evidently is to store evaluation events for longer term storage, if you choose to do so.

        If you choose not to store these events, Evidently deletes them after using them to produce metrics and other experiment results that you can view.

        You can't specify both ``CloudWatchLogs`` and ``S3Destination`` in the same operation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html#cfn-evidently-project-datadelivery
        '''
        result = self._values.get("data_delivery")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnProject.DataDeliveryObjectProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of the project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html#cfn-evidently-project-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Assigns one or more tags (key-value pairs) to the project.

        Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

        Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters.

        You can associate as many as 50 tags with a project.

        For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-project.html#cfn-evidently-project-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnSegment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_evidently.CfnSegment",
):
    '''Creates or updates a *segment* of your audience.

    A segment is a portion of your audience that share one or more characteristics. Examples could be Chrome browser users, users in Europe, or Firefox browser users in Europe who also fit other criteria that your application collects, such as age.

    Using a segment in an experiment limits that experiment to evaluate only the users who match the segment criteria. Using one or more segments in a launch allow you to define different traffic splits for the different audience segments.

    For more information about segment pattern syntax, see `Segment rule pattern syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-segments.html#CloudWatch-Evidently-segments-syntax>`_ .

    The pattern that you define for a segment is matched against the value of ``evaluationContext`` , which is passed into Evidently in the `EvaluateFeature <https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_EvaluateFeature.html>`_ operation, when Evidently assigns a feature variation to a user.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-segment.html
    :cloudformationResource: AWS::Evidently::Segment
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_evidently as evidently
        
        cfn_segment = evidently.CfnSegment(self, "MyCfnSegment",
            name="name",
        
            # the properties below are optional
            description="description",
            pattern="pattern",
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
        pattern: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A name for the segment.
        :param description: An optional description for this segment.
        :param pattern: The pattern to use for the segment. For more information about pattern syntax, see `Segment rule pattern syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-segments.html#CloudWatch-Evidently-segments-syntax>`_ .
        :param tags: Assigns one or more tags (key-value pairs) to the feature. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters. You can associate as many as 50 tags with a feature. For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01a413dc152997585ec36406e5b383d22c40c45e581645d850b78404030c0dfd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSegmentProps(
            name=name, description=description, pattern=pattern, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a622c6037fb843d60977430bc61f9f7e2b0c44dd1c2cf7bfc2e2b7ae08d8a17)
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
            type_hints = typing.get_type_hints(_typecheckingstub__38606f42aecabb3dce80160a15b36e97ee5b8ee966a5d9edd8cfd1a89d71fdbb)
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
        '''The ARN of the segment.

        For example, ``arn:aws:evidently:us-west-2:123456789012:segment/australiaSegment``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
        '''A name for the segment.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4c12e082534468891d2612754afb5e5488e6dbbb0fcdcda6469bc8c3f99255c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description for this segment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f83c1d21f957dbab06f61539524a8b714ac5423891b9d2cbf7e5baf6cf4d8cb4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="pattern")
    def pattern(self) -> typing.Optional[builtins.str]:
        '''The pattern to use for the segment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pattern"))

    @pattern.setter
    def pattern(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52f007071723973771838bffd2f7d57f9055fe40d904edd15559d3e3b4792ee4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pattern", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Assigns one or more tags (key-value pairs) to the feature.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__699cd365ca1e9e81d1b1415334e92effb9e6ec1384e6de77039b6fa9552aa28d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_evidently.CfnSegmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "pattern": "pattern",
        "tags": "tags",
    },
)
class CfnSegmentProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        pattern: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSegment``.

        :param name: A name for the segment.
        :param description: An optional description for this segment.
        :param pattern: The pattern to use for the segment. For more information about pattern syntax, see `Segment rule pattern syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-segments.html#CloudWatch-Evidently-segments-syntax>`_ .
        :param tags: Assigns one or more tags (key-value pairs) to the feature. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters. You can associate as many as 50 tags with a feature. For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-segment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_evidently as evidently
            
            cfn_segment_props = evidently.CfnSegmentProps(
                name="name",
            
                # the properties below are optional
                description="description",
                pattern="pattern",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5a222ca964d86153aba5e0b6e9b948b76db2ac5e739383e297480eb342788df)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if pattern is not None:
            self._values["pattern"] = pattern
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the segment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-segment.html#cfn-evidently-segment-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description for this segment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-segment.html#cfn-evidently-segment-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pattern(self) -> typing.Optional[builtins.str]:
        '''The pattern to use for the segment.

        For more information about pattern syntax, see `Segment rule pattern syntax <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-segments.html#CloudWatch-Evidently-segments-syntax>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-segment.html#cfn-evidently-segment-pattern
        '''
        result = self._values.get("pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Assigns one or more tags (key-value pairs) to the feature.

        Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

        Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters.

        You can associate as many as 50 tags with a feature.

        For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-evidently-segment.html#cfn-evidently-segment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSegmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnExperiment",
    "CfnExperimentProps",
    "CfnFeature",
    "CfnFeatureProps",
    "CfnLaunch",
    "CfnLaunchProps",
    "CfnProject",
    "CfnProjectProps",
    "CfnSegment",
    "CfnSegmentProps",
]

publication.publish()

def _typecheckingstub__734b87b8f3689149de24177947f45b4fba5a135b998ba47c50d89ce2cb06add4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    metric_goals: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnExperiment.MetricGoalObjectProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    online_ab_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnExperiment.OnlineAbConfigObjectProperty, typing.Dict[builtins.str, typing.Any]]],
    project: builtins.str,
    treatments: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnExperiment.TreatmentObjectProperty, typing.Dict[builtins.str, typing.Any]]]]],
    description: typing.Optional[builtins.str] = None,
    randomization_salt: typing.Optional[builtins.str] = None,
    remove_segment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    running_status: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnExperiment.RunningStatusObjectProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sampling_rate: typing.Optional[jsii.Number] = None,
    segment: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41b97e94769ee2d783fedafec30d14cbaf6057e49b29e299b13e98dba56880e4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70b9593b4954b7c3230131122acbaf53f869364117e4692d8414ae2ff6e748d9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__608184263fdaf5c6ddc6386129d9fcd580b9dd416b72defa8d9f5ff27dc0ad80(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnExperiment.MetricGoalObjectProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62a1f010ee09d989ee27529a57132add8442518e9b6f2ceb37e2d97f82fcafc6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9651d87c6a5223e7d5416809c8358bf08d64bb82e3e66321fbc5472926f1e38(
    value: typing.Union[_IResolvable_da3f097b, CfnExperiment.OnlineAbConfigObjectProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07be64da4d74661911440a7a55dc7642deba8efb90897ee9599a318f284a9adb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8a944ff8713baacf061323da7bcd1ccc67e8156291e472b1a6e7bfd7c1cf92b(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnExperiment.TreatmentObjectProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__865f432735c9ae2589b5dc0da6b59a080030920590d98d2ded0165c2edeff3c1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b086c5eed82ba0413f95a08c8a909e92a0bbce547efac04b83e6724b6d12d0b8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1c2ff5ffa047cc8e5fe6a3846276a1d082e084a7ec198cae726e776bdd2d4e6(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6064ddcd75be5c188ab7d11fc7107d2eac8214fd898eaf1de24a1cf499a71e0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnExperiment.RunningStatusObjectProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__725630988a0f01ce2a47e4320264c699d35632d1c973571abca74103c37d1b5a(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__396ba0543ba827f0fb88ab5adb79e786937fd037c560627366b5a5ce722b6c91(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5fbe1b3ff9f5bf995bd927d269240a4d47815a9b472e6e6ae669666dd96a2dd(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d37577ea667d695d977083ce595268b133cc268157e79b97ce5a51eb91f1562(
    *,
    desired_change: builtins.str,
    entity_id_key: builtins.str,
    metric_name: builtins.str,
    value_key: builtins.str,
    event_pattern: typing.Optional[builtins.str] = None,
    unit_label: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89b9e3dc636161b952f66372f7de126954391a890d3b4b6c5c9d8ecf9497c969(
    *,
    control_treatment_name: typing.Optional[builtins.str] = None,
    treatment_weights: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnExperiment.TreatmentToWeightProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bb80b983de21b5a767fb926c4b0335e3f64a61afb300308777b1584b59778db(
    *,
    status: builtins.str,
    analysis_complete_time: typing.Optional[builtins.str] = None,
    desired_state: typing.Optional[builtins.str] = None,
    reason: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e275da028c15ab90e130e2dcd1b4cdcb0205addea248b0d3cd8434badd9f7b34(
    *,
    feature: builtins.str,
    treatment_name: builtins.str,
    variation: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c24913e7b4ce7d0ccc2499c81ecea7d897c69c7fbc1291a0521dbb0d3ce04ad(
    *,
    split_weight: jsii.Number,
    treatment: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b511a5b944573df5aa1fb656233057b55fbb2369fc71a21a16cf2485a314559(
    *,
    metric_goals: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnExperiment.MetricGoalObjectProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    online_ab_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnExperiment.OnlineAbConfigObjectProperty, typing.Dict[builtins.str, typing.Any]]],
    project: builtins.str,
    treatments: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnExperiment.TreatmentObjectProperty, typing.Dict[builtins.str, typing.Any]]]]],
    description: typing.Optional[builtins.str] = None,
    randomization_salt: typing.Optional[builtins.str] = None,
    remove_segment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    running_status: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnExperiment.RunningStatusObjectProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sampling_rate: typing.Optional[jsii.Number] = None,
    segment: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__032b8fcb49dd9128128c244f2e15873395777d391323d4e1a7f50f4087f87f94(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    project: builtins.str,
    variations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFeature.VariationObjectProperty, typing.Dict[builtins.str, typing.Any]]]]],
    default_variation: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    entity_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFeature.EntityOverrideProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    evaluation_strategy: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66bc0230fcb2a6c06673de455252150fcbb3b06b62d3db48b94a67af38875a13(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64398b69cc190a0e85ffd77073c8d5be01a1867ed75581308e5c548d5fdf2604(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83847122ae503fe691e71b7ae222c38d7b58994caa625cbeb30f8718f5e9cffe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cce06c18c6aab66f449d3e00e017d519d1438e9f01b0e347c6891a96cff96940(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6955963eddf06f8bac909ceb0999e345a3de2bab55b1154054f5891fcb0da73d(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFeature.VariationObjectProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49765789b788df887d77d9c6fe7a5f94eb6690b46391f2615967e3bb3c523a73(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09fb4d9f2430757616faf01218e796a9ca6e1379e14e42daaf88b8eb5ea9af36(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92a59dc479738d64f37719a4c84ee0a1aee9546c14b55d9de1e19e98ed4ea8eb(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFeature.EntityOverrideProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f401c4f77ac0ecaf262bebe57b7e55013b6a1bee0181c137656d0db9d5ded85c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__452ab42f442291f21b09b8398172655babfb13efba8ffa52142570f0b06b2fc2(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71819cf2da9d0a5266c1f2b7d31b8d7fa4079594f6d96dbfd12865119d431c85(
    *,
    entity_id: typing.Optional[builtins.str] = None,
    variation: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d69f83bb962985fff0b5f289781eb2e76e626dd2982d400f93a032205de5739(
    *,
    variation_name: builtins.str,
    boolean_value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    double_value: typing.Optional[jsii.Number] = None,
    long_value: typing.Optional[jsii.Number] = None,
    string_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fd5d4006d379348c243366df7a4e27203488741fbadb765bad2ae169ac59650(
    *,
    name: builtins.str,
    project: builtins.str,
    variations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFeature.VariationObjectProperty, typing.Dict[builtins.str, typing.Any]]]]],
    default_variation: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    entity_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFeature.EntityOverrideProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    evaluation_strategy: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07641dd92b44cb3b2e0643d2505ef488edfd1736b97c33b89a8c38fdc3e80e8c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    groups: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLaunch.LaunchGroupObjectProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    project: builtins.str,
    scheduled_splits_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLaunch.StepConfigProperty, typing.Dict[builtins.str, typing.Any]]]]],
    description: typing.Optional[builtins.str] = None,
    execution_status: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLaunch.ExecutionStatusObjectProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    metric_monitors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLaunch.MetricDefinitionObjectProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    randomization_salt: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f82face9c15f40bd628db171784d9b9f26806a3a18f70aa27fee0c7592c5b525(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__825ae81705137d3e2f989d5f3384d9fda4bde279fdb877ac1613c131132e0b72(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd24dbcf6b27e75d516fcab8552edc84e63fbab001d5a0b07fe75bd2161b3d08(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLaunch.LaunchGroupObjectProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d883d03ce939a559b1ee5665300adb157d5f5932d26a6a688ffc497ec4acab1e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__868659d5505d8ceefc8d34d5c4e9a9b227a2f3aee237f2ebf5f5edb362ffb73b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__353ad69c0312cbb355b090decf45009d0f35cfd3174fb1768cda62970dd90e3a(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLaunch.StepConfigProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc70efb99bfb081f4aadbdff15dd4f340b1f730d9f6b9e5b55c5d1bce9662aea(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62fb950dcca9c33f47ee901068ff569f19d2c54c24fd80f64fe62c91549eb16d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLaunch.ExecutionStatusObjectProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72d460c5d783a1b583d7e0ff21f1c468740fdd12724891a96b32387d12665ced(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLaunch.MetricDefinitionObjectProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03ac24e1a4c45b370a39be9770f35e0dcec3ca0f42b47fe4dfd61f440ab2465d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10b8aca9ed0c9918ec1dddb03aba9046d4089f9d1d756bd5bc04a138123e650e(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c41f2a053e29f11510b61bf4d21e3f30ad6180748b3269a24f3cfbb55ff7907e(
    *,
    status: builtins.str,
    desired_state: typing.Optional[builtins.str] = None,
    reason: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05e698714e343cb2346580a81618d117ef1a248bf020187e7bfb3b438e20a0cc(
    *,
    group_name: builtins.str,
    split_weight: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09b94cd149d14080b3ae78bd1042b93dbc7ae40cdf44fb8dcbe1448aafb2e70e(
    *,
    feature: builtins.str,
    group_name: builtins.str,
    variation: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0cd0caab401461cbc053e72bbbc53b44f4b9fbe3e9d2221a2eb44f15dbb8d2d(
    *,
    entity_id_key: builtins.str,
    metric_name: builtins.str,
    value_key: builtins.str,
    event_pattern: typing.Optional[builtins.str] = None,
    unit_label: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2da51a2fd01ffbc20b66c20d0dc6d1a2eecf35edacb6c65b8e4a4c0888426fb(
    *,
    evaluation_order: jsii.Number,
    segment: builtins.str,
    weights: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLaunch.GroupToWeightProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53dab4eaa2aacc5ea0d3c97532af5d0ff1af68ac00101231878cc8d514e7aba2(
    *,
    group_weights: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLaunch.GroupToWeightProperty, typing.Dict[builtins.str, typing.Any]]]]],
    start_time: builtins.str,
    segment_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLaunch.SegmentOverrideProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20a136d1b38127f4fb34c7d6619d1b4038b0d2be6c3ce76d9f52535d191c3021(
    *,
    groups: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLaunch.LaunchGroupObjectProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    project: builtins.str,
    scheduled_splits_config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLaunch.StepConfigProperty, typing.Dict[builtins.str, typing.Any]]]]],
    description: typing.Optional[builtins.str] = None,
    execution_status: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLaunch.ExecutionStatusObjectProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    metric_monitors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLaunch.MetricDefinitionObjectProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    randomization_salt: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aff4f82edbe2ec588dd5ba5124dc949189afd4900acb296b20585139e3090ef5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    app_config_resource: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProject.AppConfigResourceObjectProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    data_delivery: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProject.DataDeliveryObjectProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f90a3f01e36e216b5f22034fb6f3bc0441250ad2e5836f18853fd17e2aa28d2b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__211fe4575fffc7e26414586e2fb35b683eb7c77759d1cce9aa3ada8f4c11d62e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6253b333d7062dea9649fbe8b2a501689621e3306cdfc83ca650b0c286c8180e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__839d7fab373b2b68743dd50f95e3601bb6fad99024909ea6c4fafc4a1f81f7d3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnProject.AppConfigResourceObjectProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8c0d4732b3a336b47854521db2baec1b07649626695e868d1d8ad744e8aeb6b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnProject.DataDeliveryObjectProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecaf44aad5a449686fad8267b62886895dd7a6f65f4eb1c8efa688e27a3c0b1a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf0a54e7cf0c37d82554cdade5042d2b06c498c4099b1925825853dfcfe89060(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a4d80453cc441893eb52e9312be0179a8a1ca794601606d79106337a21f337d(
    *,
    application_id: builtins.str,
    environment_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba3358915caa3d43c2df05a1f34987d23fbc194d5df2200428546c99dd9b3487(
    *,
    log_group: typing.Optional[builtins.str] = None,
    s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProject.S3DestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__935dc8f5ef3388acf3a2b6c49314a8bbe0d39ba91cc2d1a203206a8e7bd273ae(
    *,
    bucket_name: builtins.str,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac738cde3fd44d5472b342dd1f8c8a1576f7a69d882c6c2b152887958091799f(
    *,
    name: builtins.str,
    app_config_resource: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProject.AppConfigResourceObjectProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    data_delivery: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProject.DataDeliveryObjectProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01a413dc152997585ec36406e5b383d22c40c45e581645d850b78404030c0dfd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    pattern: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a622c6037fb843d60977430bc61f9f7e2b0c44dd1c2cf7bfc2e2b7ae08d8a17(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38606f42aecabb3dce80160a15b36e97ee5b8ee966a5d9edd8cfd1a89d71fdbb(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4c12e082534468891d2612754afb5e5488e6dbbb0fcdcda6469bc8c3f99255c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f83c1d21f957dbab06f61539524a8b714ac5423891b9d2cbf7e5baf6cf4d8cb4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52f007071723973771838bffd2f7d57f9055fe40d904edd15559d3e3b4792ee4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__699cd365ca1e9e81d1b1415334e92effb9e6ec1384e6de77039b6fa9552aa28d(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5a222ca964d86153aba5e0b6e9b948b76db2ac5e739383e297480eb342788df(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    pattern: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
