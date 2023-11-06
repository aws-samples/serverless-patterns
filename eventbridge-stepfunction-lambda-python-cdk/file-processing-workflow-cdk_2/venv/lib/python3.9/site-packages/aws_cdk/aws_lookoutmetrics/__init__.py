'''
# AWS::LookoutMetrics Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_lookoutmetrics as lookoutmetrics
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for LookoutMetrics construct libraries](https://constructs.dev/search?q=lookoutmetrics)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::LookoutMetrics resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_LookoutMetrics.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::LookoutMetrics](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_LookoutMetrics.html).

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
class CfnAlert(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lookoutmetrics.CfnAlert",
):
    '''The ``AWS::LookoutMetrics::Alert`` type creates an alert for an anomaly detector.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lookoutmetrics as lookoutmetrics
        
        cfn_alert = lookoutmetrics.CfnAlert(self, "MyCfnAlert",
            action=lookoutmetrics.CfnAlert.ActionProperty(
                lambda_configuration=lookoutmetrics.CfnAlert.LambdaConfigurationProperty(
                    lambda_arn="lambdaArn",
                    role_arn="roleArn"
                ),
                sns_configuration=lookoutmetrics.CfnAlert.SNSConfigurationProperty(
                    role_arn="roleArn",
                    sns_topic_arn="snsTopicArn"
                )
            ),
            alert_sensitivity_threshold=123,
            anomaly_detector_arn="anomalyDetectorArn",
        
            # the properties below are optional
            alert_description="alertDescription",
            alert_name="alertName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        action: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlert.ActionProperty", typing.Dict[builtins.str, typing.Any]]],
        alert_sensitivity_threshold: jsii.Number,
        anomaly_detector_arn: builtins.str,
        alert_description: typing.Optional[builtins.str] = None,
        alert_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param action: Action that will be triggered when there is an alert.
        :param alert_sensitivity_threshold: An integer from 0 to 100 specifying the alert sensitivity threshold.
        :param anomaly_detector_arn: The ARN of the detector to which the alert is attached.
        :param alert_description: A description of the alert.
        :param alert_name: The name of the alert.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8728605cf8a8c3531f6dae116746c94e17fc40f4b10454ed68253f7594f37b5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAlertProps(
            action=action,
            alert_sensitivity_threshold=alert_sensitivity_threshold,
            anomaly_detector_arn=anomaly_detector_arn,
            alert_description=alert_description,
            alert_name=alert_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af2583fccb79de99e1ffd4367cdbaef6fc5d3286d05c49c0757a5d05f7d45ebb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__11e72e40d199761b2debe19287dd74d247a4d6bf2de19a1586683619b6e42d40)
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
        '''The Amazon Resource Name (ARN) of the alert.

        For example, ``arn:aws:lookoutmetrics:us-east-2:123456789012:Alert:my-alert``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> typing.Union[_IResolvable_da3f097b, "CfnAlert.ActionProperty"]:
        '''Action that will be triggered when there is an alert.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAlert.ActionProperty"], jsii.get(self, "action"))

    @action.setter
    def action(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnAlert.ActionProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bca437e28138e0e51d01ea6b47ad80cc5df1f7e9796134c417b7df120770fed4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="alertSensitivityThreshold")
    def alert_sensitivity_threshold(self) -> jsii.Number:
        '''An integer from 0 to 100 specifying the alert sensitivity threshold.'''
        return typing.cast(jsii.Number, jsii.get(self, "alertSensitivityThreshold"))

    @alert_sensitivity_threshold.setter
    def alert_sensitivity_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16575316da180caba7d7b4d5bca451d1f5f4a58ac27976f3452052604cfeeab9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alertSensitivityThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="anomalyDetectorArn")
    def anomaly_detector_arn(self) -> builtins.str:
        '''The ARN of the detector to which the alert is attached.'''
        return typing.cast(builtins.str, jsii.get(self, "anomalyDetectorArn"))

    @anomaly_detector_arn.setter
    def anomaly_detector_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b0f01224b76c8ec6ed095f7d3914505315c1b87ad5c6bc322c51fc2182dd83d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anomalyDetectorArn", value)

    @builtins.property
    @jsii.member(jsii_name="alertDescription")
    def alert_description(self) -> typing.Optional[builtins.str]:
        '''A description of the alert.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alertDescription"))

    @alert_description.setter
    def alert_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c25b3f5e9ac3683a05d71bfdb651b264c95f00f413c50591d5f27474ca682a9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alertDescription", value)

    @builtins.property
    @jsii.member(jsii_name="alertName")
    def alert_name(self) -> typing.Optional[builtins.str]:
        '''The name of the alert.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alertName"))

    @alert_name.setter
    def alert_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3becde2093abb52b7666e46cd4095e177005405e86d6ea69e3f94b9f0519d0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alertName", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lookoutmetrics.CfnAlert.ActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "lambda_configuration": "lambdaConfiguration",
            "sns_configuration": "snsConfiguration",
        },
    )
    class ActionProperty:
        def __init__(
            self,
            *,
            lambda_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlert.LambdaConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sns_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlert.SNSConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A configuration that specifies the action to perform when anomalies are detected.

            :param lambda_configuration: A configuration for an AWS Lambda channel.
            :param sns_configuration: A configuration for an Amazon SNS channel.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lookoutmetrics as lookoutmetrics
                
                action_property = lookoutmetrics.CfnAlert.ActionProperty(
                    lambda_configuration=lookoutmetrics.CfnAlert.LambdaConfigurationProperty(
                        lambda_arn="lambdaArn",
                        role_arn="roleArn"
                    ),
                    sns_configuration=lookoutmetrics.CfnAlert.SNSConfigurationProperty(
                        role_arn="roleArn",
                        sns_topic_arn="snsTopicArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__918d1f90fc4698783779ca3d567c1aa1dbcc1df7f6364d530056c55317bb3300)
                check_type(argname="argument lambda_configuration", value=lambda_configuration, expected_type=type_hints["lambda_configuration"])
                check_type(argname="argument sns_configuration", value=sns_configuration, expected_type=type_hints["sns_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if lambda_configuration is not None:
                self._values["lambda_configuration"] = lambda_configuration
            if sns_configuration is not None:
                self._values["sns_configuration"] = sns_configuration

        @builtins.property
        def lambda_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlert.LambdaConfigurationProperty"]]:
            '''A configuration for an AWS Lambda channel.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-action.html#cfn-lookoutmetrics-alert-action-lambdaconfiguration
            '''
            result = self._values.get("lambda_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlert.LambdaConfigurationProperty"]], result)

        @builtins.property
        def sns_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlert.SNSConfigurationProperty"]]:
            '''A configuration for an Amazon SNS channel.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-action.html#cfn-lookoutmetrics-alert-action-snsconfiguration
            '''
            result = self._values.get("sns_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAlert.SNSConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lookoutmetrics.CfnAlert.LambdaConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"lambda_arn": "lambdaArn", "role_arn": "roleArn"},
    )
    class LambdaConfigurationProperty:
        def __init__(self, *, lambda_arn: builtins.str, role_arn: builtins.str) -> None:
            '''Contains information about a Lambda configuration.

            :param lambda_arn: The ARN of the Lambda function.
            :param role_arn: The ARN of an IAM role that has permission to invoke the Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-lambdaconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lookoutmetrics as lookoutmetrics
                
                lambda_configuration_property = lookoutmetrics.CfnAlert.LambdaConfigurationProperty(
                    lambda_arn="lambdaArn",
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5a2741bd0f93f3161ddbbe1989db143d59b7d60f454031f9a7b4d003c7baa9dd)
                check_type(argname="argument lambda_arn", value=lambda_arn, expected_type=type_hints["lambda_arn"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "lambda_arn": lambda_arn,
                "role_arn": role_arn,
            }

        @builtins.property
        def lambda_arn(self) -> builtins.str:
            '''The ARN of the Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-lambdaconfiguration.html#cfn-lookoutmetrics-alert-lambdaconfiguration-lambdaarn
            '''
            result = self._values.get("lambda_arn")
            assert result is not None, "Required property 'lambda_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of an IAM role that has permission to invoke the Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-lambdaconfiguration.html#cfn-lookoutmetrics-alert-lambdaconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lookoutmetrics.CfnAlert.SNSConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"role_arn": "roleArn", "sns_topic_arn": "snsTopicArn"},
    )
    class SNSConfigurationProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            sns_topic_arn: builtins.str,
        ) -> None:
            '''Contains information about the SNS topic to which you want to send your alerts and the IAM role that has access to that topic.

            :param role_arn: The ARN of the IAM role that has access to the target SNS topic.
            :param sns_topic_arn: The ARN of the target SNS topic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-snsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lookoutmetrics as lookoutmetrics
                
                s_nSConfiguration_property = lookoutmetrics.CfnAlert.SNSConfigurationProperty(
                    role_arn="roleArn",
                    sns_topic_arn="snsTopicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__408298e997cc645a10d8bca48400dc1f10d0a9d3264e454b49baf80bbe20c6c6)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument sns_topic_arn", value=sns_topic_arn, expected_type=type_hints["sns_topic_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
                "sns_topic_arn": sns_topic_arn,
            }

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the IAM role that has access to the target SNS topic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-snsconfiguration.html#cfn-lookoutmetrics-alert-snsconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sns_topic_arn(self) -> builtins.str:
            '''The ARN of the target SNS topic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-alert-snsconfiguration.html#cfn-lookoutmetrics-alert-snsconfiguration-snstopicarn
            '''
            result = self._values.get("sns_topic_arn")
            assert result is not None, "Required property 'sns_topic_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SNSConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lookoutmetrics.CfnAlertProps",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "alert_sensitivity_threshold": "alertSensitivityThreshold",
        "anomaly_detector_arn": "anomalyDetectorArn",
        "alert_description": "alertDescription",
        "alert_name": "alertName",
    },
)
class CfnAlertProps:
    def __init__(
        self,
        *,
        action: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlert.ActionProperty, typing.Dict[builtins.str, typing.Any]]],
        alert_sensitivity_threshold: jsii.Number,
        anomaly_detector_arn: builtins.str,
        alert_description: typing.Optional[builtins.str] = None,
        alert_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnAlert``.

        :param action: Action that will be triggered when there is an alert.
        :param alert_sensitivity_threshold: An integer from 0 to 100 specifying the alert sensitivity threshold.
        :param anomaly_detector_arn: The ARN of the detector to which the alert is attached.
        :param alert_description: A description of the alert.
        :param alert_name: The name of the alert.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lookoutmetrics as lookoutmetrics
            
            cfn_alert_props = lookoutmetrics.CfnAlertProps(
                action=lookoutmetrics.CfnAlert.ActionProperty(
                    lambda_configuration=lookoutmetrics.CfnAlert.LambdaConfigurationProperty(
                        lambda_arn="lambdaArn",
                        role_arn="roleArn"
                    ),
                    sns_configuration=lookoutmetrics.CfnAlert.SNSConfigurationProperty(
                        role_arn="roleArn",
                        sns_topic_arn="snsTopicArn"
                    )
                ),
                alert_sensitivity_threshold=123,
                anomaly_detector_arn="anomalyDetectorArn",
            
                # the properties below are optional
                alert_description="alertDescription",
                alert_name="alertName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37b5e7a084e60c1889b63e691905589769e7d3d6e42edfe3ff8deb1be27e9b12)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument alert_sensitivity_threshold", value=alert_sensitivity_threshold, expected_type=type_hints["alert_sensitivity_threshold"])
            check_type(argname="argument anomaly_detector_arn", value=anomaly_detector_arn, expected_type=type_hints["anomaly_detector_arn"])
            check_type(argname="argument alert_description", value=alert_description, expected_type=type_hints["alert_description"])
            check_type(argname="argument alert_name", value=alert_name, expected_type=type_hints["alert_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "alert_sensitivity_threshold": alert_sensitivity_threshold,
            "anomaly_detector_arn": anomaly_detector_arn,
        }
        if alert_description is not None:
            self._values["alert_description"] = alert_description
        if alert_name is not None:
            self._values["alert_name"] = alert_name

    @builtins.property
    def action(self) -> typing.Union[_IResolvable_da3f097b, CfnAlert.ActionProperty]:
        '''Action that will be triggered when there is an alert.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-action
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnAlert.ActionProperty], result)

    @builtins.property
    def alert_sensitivity_threshold(self) -> jsii.Number:
        '''An integer from 0 to 100 specifying the alert sensitivity threshold.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-alertsensitivitythreshold
        '''
        result = self._values.get("alert_sensitivity_threshold")
        assert result is not None, "Required property 'alert_sensitivity_threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def anomaly_detector_arn(self) -> builtins.str:
        '''The ARN of the detector to which the alert is attached.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-anomalydetectorarn
        '''
        result = self._values.get("anomaly_detector_arn")
        assert result is not None, "Required property 'anomaly_detector_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alert_description(self) -> typing.Optional[builtins.str]:
        '''A description of the alert.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-alertdescription
        '''
        result = self._values.get("alert_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alert_name(self) -> typing.Optional[builtins.str]:
        '''The name of the alert.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-alert.html#cfn-lookoutmetrics-alert-alertname
        '''
        result = self._values.get("alert_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAlertProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnAnomalyDetector(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lookoutmetrics.CfnAnomalyDetector",
):
    '''The ``AWS::LookoutMetrics::AnomalyDetector`` type creates an anomaly detector.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lookoutmetrics as lookoutmetrics
        
        cfn_anomaly_detector = lookoutmetrics.CfnAnomalyDetector(self, "MyCfnAnomalyDetector",
            anomaly_detector_config=lookoutmetrics.CfnAnomalyDetector.AnomalyDetectorConfigProperty(
                anomaly_detector_frequency="anomalyDetectorFrequency"
            ),
            metric_set_list=[lookoutmetrics.CfnAnomalyDetector.MetricSetProperty(
                metric_list=[lookoutmetrics.CfnAnomalyDetector.MetricProperty(
                    aggregation_function="aggregationFunction",
                    metric_name="metricName",
        
                    # the properties below are optional
                    namespace="namespace"
                )],
                metric_set_name="metricSetName",
                metric_source=lookoutmetrics.CfnAnomalyDetector.MetricSourceProperty(
                    app_flow_config=lookoutmetrics.CfnAnomalyDetector.AppFlowConfigProperty(
                        flow_name="flowName",
                        role_arn="roleArn"
                    ),
                    cloudwatch_config=lookoutmetrics.CfnAnomalyDetector.CloudwatchConfigProperty(
                        role_arn="roleArn"
                    ),
                    rds_source_config=lookoutmetrics.CfnAnomalyDetector.RDSSourceConfigProperty(
                        database_host="databaseHost",
                        database_name="databaseName",
                        database_port=123,
                        db_instance_identifier="dbInstanceIdentifier",
                        role_arn="roleArn",
                        secret_manager_arn="secretManagerArn",
                        table_name="tableName",
                        vpc_configuration=lookoutmetrics.CfnAnomalyDetector.VpcConfigurationProperty(
                            security_group_id_list=["securityGroupIdList"],
                            subnet_id_list=["subnetIdList"]
                        )
                    ),
                    redshift_source_config=lookoutmetrics.CfnAnomalyDetector.RedshiftSourceConfigProperty(
                        cluster_identifier="clusterIdentifier",
                        database_host="databaseHost",
                        database_name="databaseName",
                        database_port=123,
                        role_arn="roleArn",
                        secret_manager_arn="secretManagerArn",
                        table_name="tableName",
                        vpc_configuration=lookoutmetrics.CfnAnomalyDetector.VpcConfigurationProperty(
                            security_group_id_list=["securityGroupIdList"],
                            subnet_id_list=["subnetIdList"]
                        )
                    ),
                    s3_source_config=lookoutmetrics.CfnAnomalyDetector.S3SourceConfigProperty(
                        file_format_descriptor=lookoutmetrics.CfnAnomalyDetector.FileFormatDescriptorProperty(
                            csv_format_descriptor=lookoutmetrics.CfnAnomalyDetector.CsvFormatDescriptorProperty(
                                charset="charset",
                                contains_header=False,
                                delimiter="delimiter",
                                file_compression="fileCompression",
                                header_list=["headerList"],
                                quote_symbol="quoteSymbol"
                            ),
                            json_format_descriptor=lookoutmetrics.CfnAnomalyDetector.JsonFormatDescriptorProperty(
                                charset="charset",
                                file_compression="fileCompression"
                            )
                        ),
                        role_arn="roleArn",
        
                        # the properties below are optional
                        historical_data_path_list=["historicalDataPathList"],
                        templated_path_list=["templatedPathList"]
                    )
                ),
        
                # the properties below are optional
                dimension_list=["dimensionList"],
                metric_set_description="metricSetDescription",
                metric_set_frequency="metricSetFrequency",
                offset=123,
                timestamp_column=lookoutmetrics.CfnAnomalyDetector.TimestampColumnProperty(
                    column_format="columnFormat",
                    column_name="columnName"
                ),
                timezone="timezone"
            )],
        
            # the properties below are optional
            anomaly_detector_description="anomalyDetectorDescription",
            anomaly_detector_name="anomalyDetectorName",
            kms_key_arn="kmsKeyArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        anomaly_detector_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.AnomalyDetectorConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        metric_set_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.MetricSetProperty", typing.Dict[builtins.str, typing.Any]]]]],
        anomaly_detector_description: typing.Optional[builtins.str] = None,
        anomaly_detector_name: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param anomaly_detector_config: Contains information about the configuration of the anomaly detector.
        :param metric_set_list: The detector's dataset.
        :param anomaly_detector_description: A description of the detector.
        :param anomaly_detector_name: The name of the detector.
        :param kms_key_arn: The ARN of the KMS key to use to encrypt your data.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31ab81393e1b85b97eacf8fc50ccdd65726ebe4cd344f89434267d135a724809)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAnomalyDetectorProps(
            anomaly_detector_config=anomaly_detector_config,
            metric_set_list=metric_set_list,
            anomaly_detector_description=anomaly_detector_description,
            anomaly_detector_name=anomaly_detector_name,
            kms_key_arn=kms_key_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dee8e95c5e0cd07fbf662c30c7577d6e82a165f56df5909679a83e680a28d4cc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__faaf017f46f2465273ce5085976d9c929a7fd12ab5e5a73a9cf4cdcd90f8fa69)
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
        '''The Amazon Resource Name (ARN) of the detector.

        For example, ``arn:aws:lookoutmetrics:us-east-2:123456789012:AnomalyDetector:my-detector``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="anomalyDetectorConfig")
    def anomaly_detector_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.AnomalyDetectorConfigProperty"]:
        '''Contains information about the configuration of the anomaly detector.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.AnomalyDetectorConfigProperty"], jsii.get(self, "anomalyDetectorConfig"))

    @anomaly_detector_config.setter
    def anomaly_detector_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.AnomalyDetectorConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b781658d3f414a12c1a279f742c28faf8517d54f6c4bb78a545064da65050d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anomalyDetectorConfig", value)

    @builtins.property
    @jsii.member(jsii_name="metricSetList")
    def metric_set_list(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.MetricSetProperty"]]]:
        '''The detector's dataset.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.MetricSetProperty"]]], jsii.get(self, "metricSetList"))

    @metric_set_list.setter
    def metric_set_list(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.MetricSetProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__330a8461f141824d57906ef5a9c3660a9eb1a3a24dcf63724b3baff3125fdb5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricSetList", value)

    @builtins.property
    @jsii.member(jsii_name="anomalyDetectorDescription")
    def anomaly_detector_description(self) -> typing.Optional[builtins.str]:
        '''A description of the detector.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "anomalyDetectorDescription"))

    @anomaly_detector_description.setter
    def anomaly_detector_description(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18032fc3311c5d9f05368698835d2318d81a643b30222e23b5caa19113e42533)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anomalyDetectorDescription", value)

    @builtins.property
    @jsii.member(jsii_name="anomalyDetectorName")
    def anomaly_detector_name(self) -> typing.Optional[builtins.str]:
        '''The name of the detector.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "anomalyDetectorName"))

    @anomaly_detector_name.setter
    def anomaly_detector_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3d3884d4fbb282a3dfdfc2e9f5a32ab31ec34ceef9bbe86c037573ea6f57857)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anomalyDetectorName", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the KMS key to use to encrypt your data.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de024c053da6aec678335abd185c8c42f862ff0569545085611551174f93883e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lookoutmetrics.CfnAnomalyDetector.AnomalyDetectorConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"anomaly_detector_frequency": "anomalyDetectorFrequency"},
    )
    class AnomalyDetectorConfigProperty:
        def __init__(self, *, anomaly_detector_frequency: builtins.str) -> None:
            '''Contains information about a detector's configuration.

            :param anomaly_detector_frequency: The frequency at which the detector analyzes its source data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-anomalydetectorconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lookoutmetrics as lookoutmetrics
                
                anomaly_detector_config_property = lookoutmetrics.CfnAnomalyDetector.AnomalyDetectorConfigProperty(
                    anomaly_detector_frequency="anomalyDetectorFrequency"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0a2fc99e8c1708c8e763f7b1eca903086d6ac7320bf7c3dfc662e7d2fd357cac)
                check_type(argname="argument anomaly_detector_frequency", value=anomaly_detector_frequency, expected_type=type_hints["anomaly_detector_frequency"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "anomaly_detector_frequency": anomaly_detector_frequency,
            }

        @builtins.property
        def anomaly_detector_frequency(self) -> builtins.str:
            '''The frequency at which the detector analyzes its source data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-anomalydetectorconfig.html#cfn-lookoutmetrics-anomalydetector-anomalydetectorconfig-anomalydetectorfrequency
            '''
            result = self._values.get("anomaly_detector_frequency")
            assert result is not None, "Required property 'anomaly_detector_frequency' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnomalyDetectorConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lookoutmetrics.CfnAnomalyDetector.AppFlowConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"flow_name": "flowName", "role_arn": "roleArn"},
    )
    class AppFlowConfigProperty:
        def __init__(self, *, flow_name: builtins.str, role_arn: builtins.str) -> None:
            '''Details about an Amazon AppFlow flow datasource.

            :param flow_name: name of the flow.
            :param role_arn: An IAM role that gives Amazon Lookout for Metrics permission to access the flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-appflowconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lookoutmetrics as lookoutmetrics
                
                app_flow_config_property = lookoutmetrics.CfnAnomalyDetector.AppFlowConfigProperty(
                    flow_name="flowName",
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__38ea2c3771b7e331cc37cb9c01ea3318b3ac0b3dde9e431f4a06d9500e2280af)
                check_type(argname="argument flow_name", value=flow_name, expected_type=type_hints["flow_name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "flow_name": flow_name,
                "role_arn": role_arn,
            }

        @builtins.property
        def flow_name(self) -> builtins.str:
            '''name of the flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-appflowconfig.html#cfn-lookoutmetrics-anomalydetector-appflowconfig-flowname
            '''
            result = self._values.get("flow_name")
            assert result is not None, "Required property 'flow_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''An IAM role that gives Amazon Lookout for Metrics permission to access the flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-appflowconfig.html#cfn-lookoutmetrics-anomalydetector-appflowconfig-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AppFlowConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lookoutmetrics.CfnAnomalyDetector.CloudwatchConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"role_arn": "roleArn"},
    )
    class CloudwatchConfigProperty:
        def __init__(self, *, role_arn: builtins.str) -> None:
            '''Details about an Amazon CloudWatch datasource.

            :param role_arn: An IAM role that gives Amazon Lookout for Metrics permission to access data in Amazon CloudWatch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-cloudwatchconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lookoutmetrics as lookoutmetrics
                
                cloudwatch_config_property = lookoutmetrics.CfnAnomalyDetector.CloudwatchConfigProperty(
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__724145604a2914634c7f2cf211053a9a2c2360fb02a943d0423285d69de7373f)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
            }

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''An IAM role that gives Amazon Lookout for Metrics permission to access data in Amazon CloudWatch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-cloudwatchconfig.html#cfn-lookoutmetrics-anomalydetector-cloudwatchconfig-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudwatchConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lookoutmetrics.CfnAnomalyDetector.CsvFormatDescriptorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "charset": "charset",
            "contains_header": "containsHeader",
            "delimiter": "delimiter",
            "file_compression": "fileCompression",
            "header_list": "headerList",
            "quote_symbol": "quoteSymbol",
        },
    )
    class CsvFormatDescriptorProperty:
        def __init__(
            self,
            *,
            charset: typing.Optional[builtins.str] = None,
            contains_header: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            delimiter: typing.Optional[builtins.str] = None,
            file_compression: typing.Optional[builtins.str] = None,
            header_list: typing.Optional[typing.Sequence[builtins.str]] = None,
            quote_symbol: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about how a source CSV data file should be analyzed.

            :param charset: The character set in which the source CSV file is written.
            :param contains_header: Whether or not the source CSV file contains a header.
            :param delimiter: The character used to delimit the source CSV file.
            :param file_compression: The level of compression of the source CSV file.
            :param header_list: A list of the source CSV file's headers, if any.
            :param quote_symbol: The character used as a quote character.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lookoutmetrics as lookoutmetrics
                
                csv_format_descriptor_property = lookoutmetrics.CfnAnomalyDetector.CsvFormatDescriptorProperty(
                    charset="charset",
                    contains_header=False,
                    delimiter="delimiter",
                    file_compression="fileCompression",
                    header_list=["headerList"],
                    quote_symbol="quoteSymbol"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7ba6cc8b192874991eb7b5ee2a82eb0aa9331612cf5907ca69728d2b36baa8fc)
                check_type(argname="argument charset", value=charset, expected_type=type_hints["charset"])
                check_type(argname="argument contains_header", value=contains_header, expected_type=type_hints["contains_header"])
                check_type(argname="argument delimiter", value=delimiter, expected_type=type_hints["delimiter"])
                check_type(argname="argument file_compression", value=file_compression, expected_type=type_hints["file_compression"])
                check_type(argname="argument header_list", value=header_list, expected_type=type_hints["header_list"])
                check_type(argname="argument quote_symbol", value=quote_symbol, expected_type=type_hints["quote_symbol"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if charset is not None:
                self._values["charset"] = charset
            if contains_header is not None:
                self._values["contains_header"] = contains_header
            if delimiter is not None:
                self._values["delimiter"] = delimiter
            if file_compression is not None:
                self._values["file_compression"] = file_compression
            if header_list is not None:
                self._values["header_list"] = header_list
            if quote_symbol is not None:
                self._values["quote_symbol"] = quote_symbol

        @builtins.property
        def charset(self) -> typing.Optional[builtins.str]:
            '''The character set in which the source CSV file is written.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-charset
            '''
            result = self._values.get("charset")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def contains_header(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether or not the source CSV file contains a header.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-containsheader
            '''
            result = self._values.get("contains_header")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def delimiter(self) -> typing.Optional[builtins.str]:
            '''The character used to delimit the source CSV file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-delimiter
            '''
            result = self._values.get("delimiter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def file_compression(self) -> typing.Optional[builtins.str]:
            '''The level of compression of the source CSV file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-filecompression
            '''
            result = self._values.get("file_compression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def header_list(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of the source CSV file's headers, if any.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-headerlist
            '''
            result = self._values.get("header_list")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def quote_symbol(self) -> typing.Optional[builtins.str]:
            '''The character used as a quote character.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-csvformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-csvformatdescriptor-quotesymbol
            '''
            result = self._values.get("quote_symbol")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CsvFormatDescriptorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lookoutmetrics.CfnAnomalyDetector.FileFormatDescriptorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "csv_format_descriptor": "csvFormatDescriptor",
            "json_format_descriptor": "jsonFormatDescriptor",
        },
    )
    class FileFormatDescriptorProperty:
        def __init__(
            self,
            *,
            csv_format_descriptor: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.CsvFormatDescriptorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            json_format_descriptor: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.JsonFormatDescriptorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains information about a source file's formatting.

            :param csv_format_descriptor: Contains information about how a source CSV data file should be analyzed.
            :param json_format_descriptor: Contains information about how a source JSON data file should be analyzed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-fileformatdescriptor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lookoutmetrics as lookoutmetrics
                
                file_format_descriptor_property = lookoutmetrics.CfnAnomalyDetector.FileFormatDescriptorProperty(
                    csv_format_descriptor=lookoutmetrics.CfnAnomalyDetector.CsvFormatDescriptorProperty(
                        charset="charset",
                        contains_header=False,
                        delimiter="delimiter",
                        file_compression="fileCompression",
                        header_list=["headerList"],
                        quote_symbol="quoteSymbol"
                    ),
                    json_format_descriptor=lookoutmetrics.CfnAnomalyDetector.JsonFormatDescriptorProperty(
                        charset="charset",
                        file_compression="fileCompression"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8ddbd19438ab1247dbbe4eea827d6515d16a62ef2f2a3edd7eb00edd00e6f448)
                check_type(argname="argument csv_format_descriptor", value=csv_format_descriptor, expected_type=type_hints["csv_format_descriptor"])
                check_type(argname="argument json_format_descriptor", value=json_format_descriptor, expected_type=type_hints["json_format_descriptor"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if csv_format_descriptor is not None:
                self._values["csv_format_descriptor"] = csv_format_descriptor
            if json_format_descriptor is not None:
                self._values["json_format_descriptor"] = json_format_descriptor

        @builtins.property
        def csv_format_descriptor(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.CsvFormatDescriptorProperty"]]:
            '''Contains information about how a source CSV data file should be analyzed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-fileformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-fileformatdescriptor-csvformatdescriptor
            '''
            result = self._values.get("csv_format_descriptor")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.CsvFormatDescriptorProperty"]], result)

        @builtins.property
        def json_format_descriptor(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.JsonFormatDescriptorProperty"]]:
            '''Contains information about how a source JSON data file should be analyzed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-fileformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-fileformatdescriptor-jsonformatdescriptor
            '''
            result = self._values.get("json_format_descriptor")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.JsonFormatDescriptorProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FileFormatDescriptorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lookoutmetrics.CfnAnomalyDetector.JsonFormatDescriptorProperty",
        jsii_struct_bases=[],
        name_mapping={"charset": "charset", "file_compression": "fileCompression"},
    )
    class JsonFormatDescriptorProperty:
        def __init__(
            self,
            *,
            charset: typing.Optional[builtins.str] = None,
            file_compression: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about how a source JSON data file should be analyzed.

            :param charset: The character set in which the source JSON file is written.
            :param file_compression: The level of compression of the source CSV file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-jsonformatdescriptor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lookoutmetrics as lookoutmetrics
                
                json_format_descriptor_property = lookoutmetrics.CfnAnomalyDetector.JsonFormatDescriptorProperty(
                    charset="charset",
                    file_compression="fileCompression"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__67e3166c183fb9595b36477950349ad78f5d3c5aa01cca2e5ceb5531c04426af)
                check_type(argname="argument charset", value=charset, expected_type=type_hints["charset"])
                check_type(argname="argument file_compression", value=file_compression, expected_type=type_hints["file_compression"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if charset is not None:
                self._values["charset"] = charset
            if file_compression is not None:
                self._values["file_compression"] = file_compression

        @builtins.property
        def charset(self) -> typing.Optional[builtins.str]:
            '''The character set in which the source JSON file is written.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-jsonformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-jsonformatdescriptor-charset
            '''
            result = self._values.get("charset")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def file_compression(self) -> typing.Optional[builtins.str]:
            '''The level of compression of the source CSV file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-jsonformatdescriptor.html#cfn-lookoutmetrics-anomalydetector-jsonformatdescriptor-filecompression
            '''
            result = self._values.get("file_compression")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JsonFormatDescriptorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lookoutmetrics.CfnAnomalyDetector.MetricProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aggregation_function": "aggregationFunction",
            "metric_name": "metricName",
            "namespace": "namespace",
        },
    )
    class MetricProperty:
        def __init__(
            self,
            *,
            aggregation_function: builtins.str,
            metric_name: builtins.str,
            namespace: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A calculation made by contrasting a measure and a dimension from your source data.

            :param aggregation_function: The function with which the metric is calculated.
            :param metric_name: The name of the metric.
            :param namespace: The namespace for the metric.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metric.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lookoutmetrics as lookoutmetrics
                
                metric_property = lookoutmetrics.CfnAnomalyDetector.MetricProperty(
                    aggregation_function="aggregationFunction",
                    metric_name="metricName",
                
                    # the properties below are optional
                    namespace="namespace"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__df50eca477a61eb4e0b022a28e366212f515bdb4840ba1ebe300d9251e3d9240)
                check_type(argname="argument aggregation_function", value=aggregation_function, expected_type=type_hints["aggregation_function"])
                check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
                check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "aggregation_function": aggregation_function,
                "metric_name": metric_name,
            }
            if namespace is not None:
                self._values["namespace"] = namespace

        @builtins.property
        def aggregation_function(self) -> builtins.str:
            '''The function with which the metric is calculated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metric.html#cfn-lookoutmetrics-anomalydetector-metric-aggregationfunction
            '''
            result = self._values.get("aggregation_function")
            assert result is not None, "Required property 'aggregation_function' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''The name of the metric.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metric.html#cfn-lookoutmetrics-anomalydetector-metric-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def namespace(self) -> typing.Optional[builtins.str]:
            '''The namespace for the metric.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metric.html#cfn-lookoutmetrics-anomalydetector-metric-namespace
            '''
            result = self._values.get("namespace")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lookoutmetrics.CfnAnomalyDetector.MetricSetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "metric_list": "metricList",
            "metric_set_name": "metricSetName",
            "metric_source": "metricSource",
            "dimension_list": "dimensionList",
            "metric_set_description": "metricSetDescription",
            "metric_set_frequency": "metricSetFrequency",
            "offset": "offset",
            "timestamp_column": "timestampColumn",
            "timezone": "timezone",
        },
    )
    class MetricSetProperty:
        def __init__(
            self,
            *,
            metric_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.MetricProperty", typing.Dict[builtins.str, typing.Any]]]]],
            metric_set_name: builtins.str,
            metric_source: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.MetricSourceProperty", typing.Dict[builtins.str, typing.Any]]],
            dimension_list: typing.Optional[typing.Sequence[builtins.str]] = None,
            metric_set_description: typing.Optional[builtins.str] = None,
            metric_set_frequency: typing.Optional[builtins.str] = None,
            offset: typing.Optional[jsii.Number] = None,
            timestamp_column: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.TimestampColumnProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            timezone: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about a dataset.

            :param metric_list: A list of metrics that the dataset will contain.
            :param metric_set_name: The name of the dataset.
            :param metric_source: Contains information about how the source data should be interpreted.
            :param dimension_list: A list of the fields you want to treat as dimensions.
            :param metric_set_description: A description of the dataset you are creating.
            :param metric_set_frequency: The frequency with which the source data will be analyzed for anomalies.
            :param offset: After an interval ends, the amount of seconds that the detector waits before importing data. Offset is only supported for S3, Redshift, Athena and datasources.
            :param timestamp_column: Contains information about the column used for tracking time in your source data.
            :param timezone: The time zone in which your source data was recorded.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lookoutmetrics as lookoutmetrics
                
                metric_set_property = lookoutmetrics.CfnAnomalyDetector.MetricSetProperty(
                    metric_list=[lookoutmetrics.CfnAnomalyDetector.MetricProperty(
                        aggregation_function="aggregationFunction",
                        metric_name="metricName",
                
                        # the properties below are optional
                        namespace="namespace"
                    )],
                    metric_set_name="metricSetName",
                    metric_source=lookoutmetrics.CfnAnomalyDetector.MetricSourceProperty(
                        app_flow_config=lookoutmetrics.CfnAnomalyDetector.AppFlowConfigProperty(
                            flow_name="flowName",
                            role_arn="roleArn"
                        ),
                        cloudwatch_config=lookoutmetrics.CfnAnomalyDetector.CloudwatchConfigProperty(
                            role_arn="roleArn"
                        ),
                        rds_source_config=lookoutmetrics.CfnAnomalyDetector.RDSSourceConfigProperty(
                            database_host="databaseHost",
                            database_name="databaseName",
                            database_port=123,
                            db_instance_identifier="dbInstanceIdentifier",
                            role_arn="roleArn",
                            secret_manager_arn="secretManagerArn",
                            table_name="tableName",
                            vpc_configuration=lookoutmetrics.CfnAnomalyDetector.VpcConfigurationProperty(
                                security_group_id_list=["securityGroupIdList"],
                                subnet_id_list=["subnetIdList"]
                            )
                        ),
                        redshift_source_config=lookoutmetrics.CfnAnomalyDetector.RedshiftSourceConfigProperty(
                            cluster_identifier="clusterIdentifier",
                            database_host="databaseHost",
                            database_name="databaseName",
                            database_port=123,
                            role_arn="roleArn",
                            secret_manager_arn="secretManagerArn",
                            table_name="tableName",
                            vpc_configuration=lookoutmetrics.CfnAnomalyDetector.VpcConfigurationProperty(
                                security_group_id_list=["securityGroupIdList"],
                                subnet_id_list=["subnetIdList"]
                            )
                        ),
                        s3_source_config=lookoutmetrics.CfnAnomalyDetector.S3SourceConfigProperty(
                            file_format_descriptor=lookoutmetrics.CfnAnomalyDetector.FileFormatDescriptorProperty(
                                csv_format_descriptor=lookoutmetrics.CfnAnomalyDetector.CsvFormatDescriptorProperty(
                                    charset="charset",
                                    contains_header=False,
                                    delimiter="delimiter",
                                    file_compression="fileCompression",
                                    header_list=["headerList"],
                                    quote_symbol="quoteSymbol"
                                ),
                                json_format_descriptor=lookoutmetrics.CfnAnomalyDetector.JsonFormatDescriptorProperty(
                                    charset="charset",
                                    file_compression="fileCompression"
                                )
                            ),
                            role_arn="roleArn",
                
                            # the properties below are optional
                            historical_data_path_list=["historicalDataPathList"],
                            templated_path_list=["templatedPathList"]
                        )
                    ),
                
                    # the properties below are optional
                    dimension_list=["dimensionList"],
                    metric_set_description="metricSetDescription",
                    metric_set_frequency="metricSetFrequency",
                    offset=123,
                    timestamp_column=lookoutmetrics.CfnAnomalyDetector.TimestampColumnProperty(
                        column_format="columnFormat",
                        column_name="columnName"
                    ),
                    timezone="timezone"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2cce3005d3d219e3d045e48a5c12869a1fe9bcaf7f759c45e1ec58e3888d0e70)
                check_type(argname="argument metric_list", value=metric_list, expected_type=type_hints["metric_list"])
                check_type(argname="argument metric_set_name", value=metric_set_name, expected_type=type_hints["metric_set_name"])
                check_type(argname="argument metric_source", value=metric_source, expected_type=type_hints["metric_source"])
                check_type(argname="argument dimension_list", value=dimension_list, expected_type=type_hints["dimension_list"])
                check_type(argname="argument metric_set_description", value=metric_set_description, expected_type=type_hints["metric_set_description"])
                check_type(argname="argument metric_set_frequency", value=metric_set_frequency, expected_type=type_hints["metric_set_frequency"])
                check_type(argname="argument offset", value=offset, expected_type=type_hints["offset"])
                check_type(argname="argument timestamp_column", value=timestamp_column, expected_type=type_hints["timestamp_column"])
                check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "metric_list": metric_list,
                "metric_set_name": metric_set_name,
                "metric_source": metric_source,
            }
            if dimension_list is not None:
                self._values["dimension_list"] = dimension_list
            if metric_set_description is not None:
                self._values["metric_set_description"] = metric_set_description
            if metric_set_frequency is not None:
                self._values["metric_set_frequency"] = metric_set_frequency
            if offset is not None:
                self._values["offset"] = offset
            if timestamp_column is not None:
                self._values["timestamp_column"] = timestamp_column
            if timezone is not None:
                self._values["timezone"] = timezone

        @builtins.property
        def metric_list(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.MetricProperty"]]]:
            '''A list of metrics that the dataset will contain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-metriclist
            '''
            result = self._values.get("metric_list")
            assert result is not None, "Required property 'metric_list' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.MetricProperty"]]], result)

        @builtins.property
        def metric_set_name(self) -> builtins.str:
            '''The name of the dataset.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-metricsetname
            '''
            result = self._values.get("metric_set_name")
            assert result is not None, "Required property 'metric_set_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def metric_source(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.MetricSourceProperty"]:
            '''Contains information about how the source data should be interpreted.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-metricsource
            '''
            result = self._values.get("metric_source")
            assert result is not None, "Required property 'metric_source' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.MetricSourceProperty"], result)

        @builtins.property
        def dimension_list(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of the fields you want to treat as dimensions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-dimensionlist
            '''
            result = self._values.get("dimension_list")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def metric_set_description(self) -> typing.Optional[builtins.str]:
            '''A description of the dataset you are creating.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-metricsetdescription
            '''
            result = self._values.get("metric_set_description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def metric_set_frequency(self) -> typing.Optional[builtins.str]:
            '''The frequency with which the source data will be analyzed for anomalies.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-metricsetfrequency
            '''
            result = self._values.get("metric_set_frequency")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def offset(self) -> typing.Optional[jsii.Number]:
            '''After an interval ends, the amount of seconds that the detector waits before importing data.

            Offset is only supported for S3, Redshift, Athena and datasources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-offset
            '''
            result = self._values.get("offset")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def timestamp_column(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.TimestampColumnProperty"]]:
            '''Contains information about the column used for tracking time in your source data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-timestampcolumn
            '''
            result = self._values.get("timestamp_column")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.TimestampColumnProperty"]], result)

        @builtins.property
        def timezone(self) -> typing.Optional[builtins.str]:
            '''The time zone in which your source data was recorded.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricset.html#cfn-lookoutmetrics-anomalydetector-metricset-timezone
            '''
            result = self._values.get("timezone")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricSetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lookoutmetrics.CfnAnomalyDetector.MetricSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "app_flow_config": "appFlowConfig",
            "cloudwatch_config": "cloudwatchConfig",
            "rds_source_config": "rdsSourceConfig",
            "redshift_source_config": "redshiftSourceConfig",
            "s3_source_config": "s3SourceConfig",
        },
    )
    class MetricSourceProperty:
        def __init__(
            self,
            *,
            app_flow_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.AppFlowConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cloudwatch_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.CloudwatchConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            rds_source_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.RDSSourceConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            redshift_source_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.RedshiftSourceConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_source_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.S3SourceConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains information about how the source data should be interpreted.

            :param app_flow_config: Details about an AppFlow datasource.
            :param cloudwatch_config: Details about an Amazon CloudWatch monitoring datasource.
            :param rds_source_config: Details about an Amazon Relational Database Service (RDS) datasource.
            :param redshift_source_config: Details about an Amazon Redshift database datasource.
            :param s3_source_config: Contains information about the configuration of the S3 bucket that contains source files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lookoutmetrics as lookoutmetrics
                
                metric_source_property = lookoutmetrics.CfnAnomalyDetector.MetricSourceProperty(
                    app_flow_config=lookoutmetrics.CfnAnomalyDetector.AppFlowConfigProperty(
                        flow_name="flowName",
                        role_arn="roleArn"
                    ),
                    cloudwatch_config=lookoutmetrics.CfnAnomalyDetector.CloudwatchConfigProperty(
                        role_arn="roleArn"
                    ),
                    rds_source_config=lookoutmetrics.CfnAnomalyDetector.RDSSourceConfigProperty(
                        database_host="databaseHost",
                        database_name="databaseName",
                        database_port=123,
                        db_instance_identifier="dbInstanceIdentifier",
                        role_arn="roleArn",
                        secret_manager_arn="secretManagerArn",
                        table_name="tableName",
                        vpc_configuration=lookoutmetrics.CfnAnomalyDetector.VpcConfigurationProperty(
                            security_group_id_list=["securityGroupIdList"],
                            subnet_id_list=["subnetIdList"]
                        )
                    ),
                    redshift_source_config=lookoutmetrics.CfnAnomalyDetector.RedshiftSourceConfigProperty(
                        cluster_identifier="clusterIdentifier",
                        database_host="databaseHost",
                        database_name="databaseName",
                        database_port=123,
                        role_arn="roleArn",
                        secret_manager_arn="secretManagerArn",
                        table_name="tableName",
                        vpc_configuration=lookoutmetrics.CfnAnomalyDetector.VpcConfigurationProperty(
                            security_group_id_list=["securityGroupIdList"],
                            subnet_id_list=["subnetIdList"]
                        )
                    ),
                    s3_source_config=lookoutmetrics.CfnAnomalyDetector.S3SourceConfigProperty(
                        file_format_descriptor=lookoutmetrics.CfnAnomalyDetector.FileFormatDescriptorProperty(
                            csv_format_descriptor=lookoutmetrics.CfnAnomalyDetector.CsvFormatDescriptorProperty(
                                charset="charset",
                                contains_header=False,
                                delimiter="delimiter",
                                file_compression="fileCompression",
                                header_list=["headerList"],
                                quote_symbol="quoteSymbol"
                            ),
                            json_format_descriptor=lookoutmetrics.CfnAnomalyDetector.JsonFormatDescriptorProperty(
                                charset="charset",
                                file_compression="fileCompression"
                            )
                        ),
                        role_arn="roleArn",
                
                        # the properties below are optional
                        historical_data_path_list=["historicalDataPathList"],
                        templated_path_list=["templatedPathList"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1339cbdc783ac0ba8f9fe1fabef3ca626523dad00e283af466740e6de7c4e41c)
                check_type(argname="argument app_flow_config", value=app_flow_config, expected_type=type_hints["app_flow_config"])
                check_type(argname="argument cloudwatch_config", value=cloudwatch_config, expected_type=type_hints["cloudwatch_config"])
                check_type(argname="argument rds_source_config", value=rds_source_config, expected_type=type_hints["rds_source_config"])
                check_type(argname="argument redshift_source_config", value=redshift_source_config, expected_type=type_hints["redshift_source_config"])
                check_type(argname="argument s3_source_config", value=s3_source_config, expected_type=type_hints["s3_source_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if app_flow_config is not None:
                self._values["app_flow_config"] = app_flow_config
            if cloudwatch_config is not None:
                self._values["cloudwatch_config"] = cloudwatch_config
            if rds_source_config is not None:
                self._values["rds_source_config"] = rds_source_config
            if redshift_source_config is not None:
                self._values["redshift_source_config"] = redshift_source_config
            if s3_source_config is not None:
                self._values["s3_source_config"] = s3_source_config

        @builtins.property
        def app_flow_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.AppFlowConfigProperty"]]:
            '''Details about an AppFlow datasource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html#cfn-lookoutmetrics-anomalydetector-metricsource-appflowconfig
            '''
            result = self._values.get("app_flow_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.AppFlowConfigProperty"]], result)

        @builtins.property
        def cloudwatch_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.CloudwatchConfigProperty"]]:
            '''Details about an Amazon CloudWatch monitoring datasource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html#cfn-lookoutmetrics-anomalydetector-metricsource-cloudwatchconfig
            '''
            result = self._values.get("cloudwatch_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.CloudwatchConfigProperty"]], result)

        @builtins.property
        def rds_source_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.RDSSourceConfigProperty"]]:
            '''Details about an Amazon Relational Database Service (RDS) datasource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html#cfn-lookoutmetrics-anomalydetector-metricsource-rdssourceconfig
            '''
            result = self._values.get("rds_source_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.RDSSourceConfigProperty"]], result)

        @builtins.property
        def redshift_source_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.RedshiftSourceConfigProperty"]]:
            '''Details about an Amazon Redshift database datasource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html#cfn-lookoutmetrics-anomalydetector-metricsource-redshiftsourceconfig
            '''
            result = self._values.get("redshift_source_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.RedshiftSourceConfigProperty"]], result)

        @builtins.property
        def s3_source_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.S3SourceConfigProperty"]]:
            '''Contains information about the configuration of the S3 bucket that contains source files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-metricsource.html#cfn-lookoutmetrics-anomalydetector-metricsource-s3sourceconfig
            '''
            result = self._values.get("s3_source_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.S3SourceConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lookoutmetrics.CfnAnomalyDetector.RDSSourceConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database_host": "databaseHost",
            "database_name": "databaseName",
            "database_port": "databasePort",
            "db_instance_identifier": "dbInstanceIdentifier",
            "role_arn": "roleArn",
            "secret_manager_arn": "secretManagerArn",
            "table_name": "tableName",
            "vpc_configuration": "vpcConfiguration",
        },
    )
    class RDSSourceConfigProperty:
        def __init__(
            self,
            *,
            database_host: builtins.str,
            database_name: builtins.str,
            database_port: jsii.Number,
            db_instance_identifier: builtins.str,
            role_arn: builtins.str,
            secret_manager_arn: builtins.str,
            table_name: builtins.str,
            vpc_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.VpcConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Contains information about the Amazon Relational Database Service (RDS) configuration.

            :param database_host: The host name of the database.
            :param database_name: The name of the RDS database.
            :param database_port: The port number where the database can be accessed.
            :param db_instance_identifier: A string identifying the database instance.
            :param role_arn: The Amazon Resource Name (ARN) of the role.
            :param secret_manager_arn: The Amazon Resource Name (ARN) of the AWS Secrets Manager role.
            :param table_name: The name of the table in the database.
            :param vpc_configuration: An object containing information about the Amazon Virtual Private Cloud (VPC) configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lookoutmetrics as lookoutmetrics
                
                r_dSSource_config_property = lookoutmetrics.CfnAnomalyDetector.RDSSourceConfigProperty(
                    database_host="databaseHost",
                    database_name="databaseName",
                    database_port=123,
                    db_instance_identifier="dbInstanceIdentifier",
                    role_arn="roleArn",
                    secret_manager_arn="secretManagerArn",
                    table_name="tableName",
                    vpc_configuration=lookoutmetrics.CfnAnomalyDetector.VpcConfigurationProperty(
                        security_group_id_list=["securityGroupIdList"],
                        subnet_id_list=["subnetIdList"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f8feffc16f2d3df708e99199b419cda14195606cdd79f15131d328b2f5f9a6e6)
                check_type(argname="argument database_host", value=database_host, expected_type=type_hints["database_host"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument database_port", value=database_port, expected_type=type_hints["database_port"])
                check_type(argname="argument db_instance_identifier", value=db_instance_identifier, expected_type=type_hints["db_instance_identifier"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument secret_manager_arn", value=secret_manager_arn, expected_type=type_hints["secret_manager_arn"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
                check_type(argname="argument vpc_configuration", value=vpc_configuration, expected_type=type_hints["vpc_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "database_host": database_host,
                "database_name": database_name,
                "database_port": database_port,
                "db_instance_identifier": db_instance_identifier,
                "role_arn": role_arn,
                "secret_manager_arn": secret_manager_arn,
                "table_name": table_name,
                "vpc_configuration": vpc_configuration,
            }

        @builtins.property
        def database_host(self) -> builtins.str:
            '''The host name of the database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-databasehost
            '''
            result = self._values.get("database_host")
            assert result is not None, "Required property 'database_host' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_name(self) -> builtins.str:
            '''The name of the RDS database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_port(self) -> jsii.Number:
            '''The port number where the database can be accessed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-databaseport
            '''
            result = self._values.get("database_port")
            assert result is not None, "Required property 'database_port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def db_instance_identifier(self) -> builtins.str:
            '''A string identifying the database instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-dbinstanceidentifier
            '''
            result = self._values.get("db_instance_identifier")
            assert result is not None, "Required property 'db_instance_identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secret_manager_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the AWS Secrets Manager role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-secretmanagerarn
            '''
            result = self._values.get("secret_manager_arn")
            assert result is not None, "Required property 'secret_manager_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''The name of the table in the database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def vpc_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.VpcConfigurationProperty"]:
            '''An object containing information about the Amazon Virtual Private Cloud (VPC) configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-rdssourceconfig.html#cfn-lookoutmetrics-anomalydetector-rdssourceconfig-vpcconfiguration
            '''
            result = self._values.get("vpc_configuration")
            assert result is not None, "Required property 'vpc_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.VpcConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RDSSourceConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lookoutmetrics.CfnAnomalyDetector.RedshiftSourceConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cluster_identifier": "clusterIdentifier",
            "database_host": "databaseHost",
            "database_name": "databaseName",
            "database_port": "databasePort",
            "role_arn": "roleArn",
            "secret_manager_arn": "secretManagerArn",
            "table_name": "tableName",
            "vpc_configuration": "vpcConfiguration",
        },
    )
    class RedshiftSourceConfigProperty:
        def __init__(
            self,
            *,
            cluster_identifier: builtins.str,
            database_host: builtins.str,
            database_name: builtins.str,
            database_port: jsii.Number,
            role_arn: builtins.str,
            secret_manager_arn: builtins.str,
            table_name: builtins.str,
            vpc_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.VpcConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Provides information about the Amazon Redshift database configuration.

            :param cluster_identifier: A string identifying the Redshift cluster.
            :param database_host: The name of the database host.
            :param database_name: The Redshift database name.
            :param database_port: The port number where the database can be accessed.
            :param role_arn: The Amazon Resource Name (ARN) of the role providing access to the database.
            :param secret_manager_arn: The Amazon Resource Name (ARN) of the AWS Secrets Manager role.
            :param table_name: The table name of the Redshift database.
            :param vpc_configuration: Contains information about the Amazon Virtual Private Cloud (VPC) configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lookoutmetrics as lookoutmetrics
                
                redshift_source_config_property = lookoutmetrics.CfnAnomalyDetector.RedshiftSourceConfigProperty(
                    cluster_identifier="clusterIdentifier",
                    database_host="databaseHost",
                    database_name="databaseName",
                    database_port=123,
                    role_arn="roleArn",
                    secret_manager_arn="secretManagerArn",
                    table_name="tableName",
                    vpc_configuration=lookoutmetrics.CfnAnomalyDetector.VpcConfigurationProperty(
                        security_group_id_list=["securityGroupIdList"],
                        subnet_id_list=["subnetIdList"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__569a554d8877d6747add9f55cb258a09d4a6172adb0b3966b0377ce8a3f0dd44)
                check_type(argname="argument cluster_identifier", value=cluster_identifier, expected_type=type_hints["cluster_identifier"])
                check_type(argname="argument database_host", value=database_host, expected_type=type_hints["database_host"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument database_port", value=database_port, expected_type=type_hints["database_port"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument secret_manager_arn", value=secret_manager_arn, expected_type=type_hints["secret_manager_arn"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
                check_type(argname="argument vpc_configuration", value=vpc_configuration, expected_type=type_hints["vpc_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cluster_identifier": cluster_identifier,
                "database_host": database_host,
                "database_name": database_name,
                "database_port": database_port,
                "role_arn": role_arn,
                "secret_manager_arn": secret_manager_arn,
                "table_name": table_name,
                "vpc_configuration": vpc_configuration,
            }

        @builtins.property
        def cluster_identifier(self) -> builtins.str:
            '''A string identifying the Redshift cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-clusteridentifier
            '''
            result = self._values.get("cluster_identifier")
            assert result is not None, "Required property 'cluster_identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_host(self) -> builtins.str:
            '''The name of the database host.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-databasehost
            '''
            result = self._values.get("database_host")
            assert result is not None, "Required property 'database_host' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_name(self) -> builtins.str:
            '''The Redshift database name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database_port(self) -> jsii.Number:
            '''The port number where the database can be accessed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-databaseport
            '''
            result = self._values.get("database_port")
            assert result is not None, "Required property 'database_port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the role providing access to the database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secret_manager_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the AWS Secrets Manager role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-secretmanagerarn
            '''
            result = self._values.get("secret_manager_arn")
            assert result is not None, "Required property 'secret_manager_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''The table name of the Redshift database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def vpc_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.VpcConfigurationProperty"]:
            '''Contains information about the Amazon Virtual Private Cloud (VPC) configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-redshiftsourceconfig.html#cfn-lookoutmetrics-anomalydetector-redshiftsourceconfig-vpcconfiguration
            '''
            result = self._values.get("vpc_configuration")
            assert result is not None, "Required property 'vpc_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.VpcConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftSourceConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lookoutmetrics.CfnAnomalyDetector.S3SourceConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "file_format_descriptor": "fileFormatDescriptor",
            "role_arn": "roleArn",
            "historical_data_path_list": "historicalDataPathList",
            "templated_path_list": "templatedPathList",
        },
    )
    class S3SourceConfigProperty:
        def __init__(
            self,
            *,
            file_format_descriptor: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnomalyDetector.FileFormatDescriptorProperty", typing.Dict[builtins.str, typing.Any]]],
            role_arn: builtins.str,
            historical_data_path_list: typing.Optional[typing.Sequence[builtins.str]] = None,
            templated_path_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Contains information about the configuration of the S3 bucket that contains source files.

            :param file_format_descriptor: Contains information about a source file's formatting.
            :param role_arn: The ARN of an IAM role that has read and write access permissions to the source S3 bucket.
            :param historical_data_path_list: A list of paths to the historical data files.
            :param templated_path_list: A list of templated paths to the source files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lookoutmetrics as lookoutmetrics
                
                s3_source_config_property = lookoutmetrics.CfnAnomalyDetector.S3SourceConfigProperty(
                    file_format_descriptor=lookoutmetrics.CfnAnomalyDetector.FileFormatDescriptorProperty(
                        csv_format_descriptor=lookoutmetrics.CfnAnomalyDetector.CsvFormatDescriptorProperty(
                            charset="charset",
                            contains_header=False,
                            delimiter="delimiter",
                            file_compression="fileCompression",
                            header_list=["headerList"],
                            quote_symbol="quoteSymbol"
                        ),
                        json_format_descriptor=lookoutmetrics.CfnAnomalyDetector.JsonFormatDescriptorProperty(
                            charset="charset",
                            file_compression="fileCompression"
                        )
                    ),
                    role_arn="roleArn",
                
                    # the properties below are optional
                    historical_data_path_list=["historicalDataPathList"],
                    templated_path_list=["templatedPathList"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a2104594e6dc20e604e9ef34cec5e3b48affde655dd8871d134d43d67ed6135b)
                check_type(argname="argument file_format_descriptor", value=file_format_descriptor, expected_type=type_hints["file_format_descriptor"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument historical_data_path_list", value=historical_data_path_list, expected_type=type_hints["historical_data_path_list"])
                check_type(argname="argument templated_path_list", value=templated_path_list, expected_type=type_hints["templated_path_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "file_format_descriptor": file_format_descriptor,
                "role_arn": role_arn,
            }
            if historical_data_path_list is not None:
                self._values["historical_data_path_list"] = historical_data_path_list
            if templated_path_list is not None:
                self._values["templated_path_list"] = templated_path_list

        @builtins.property
        def file_format_descriptor(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.FileFormatDescriptorProperty"]:
            '''Contains information about a source file's formatting.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html#cfn-lookoutmetrics-anomalydetector-s3sourceconfig-fileformatdescriptor
            '''
            result = self._values.get("file_format_descriptor")
            assert result is not None, "Required property 'file_format_descriptor' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAnomalyDetector.FileFormatDescriptorProperty"], result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of an IAM role that has read and write access permissions to the source S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html#cfn-lookoutmetrics-anomalydetector-s3sourceconfig-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def historical_data_path_list(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of paths to the historical data files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html#cfn-lookoutmetrics-anomalydetector-s3sourceconfig-historicaldatapathlist
            '''
            result = self._values.get("historical_data_path_list")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def templated_path_list(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of templated paths to the source files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-s3sourceconfig.html#cfn-lookoutmetrics-anomalydetector-s3sourceconfig-templatedpathlist
            '''
            result = self._values.get("templated_path_list")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3SourceConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lookoutmetrics.CfnAnomalyDetector.TimestampColumnProperty",
        jsii_struct_bases=[],
        name_mapping={"column_format": "columnFormat", "column_name": "columnName"},
    )
    class TimestampColumnProperty:
        def __init__(
            self,
            *,
            column_format: typing.Optional[builtins.str] = None,
            column_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about the column used to track time in a source data file.

            :param column_format: The format of the timestamp column.
            :param column_name: The name of the timestamp column.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-timestampcolumn.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lookoutmetrics as lookoutmetrics
                
                timestamp_column_property = lookoutmetrics.CfnAnomalyDetector.TimestampColumnProperty(
                    column_format="columnFormat",
                    column_name="columnName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3aecf2888a0d1c17cdd4142e3c7ce9f01564679e174b26b805a0fd35e5fd4441)
                check_type(argname="argument column_format", value=column_format, expected_type=type_hints["column_format"])
                check_type(argname="argument column_name", value=column_name, expected_type=type_hints["column_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if column_format is not None:
                self._values["column_format"] = column_format
            if column_name is not None:
                self._values["column_name"] = column_name

        @builtins.property
        def column_format(self) -> typing.Optional[builtins.str]:
            '''The format of the timestamp column.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-timestampcolumn.html#cfn-lookoutmetrics-anomalydetector-timestampcolumn-columnformat
            '''
            result = self._values.get("column_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def column_name(self) -> typing.Optional[builtins.str]:
            '''The name of the timestamp column.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-timestampcolumn.html#cfn-lookoutmetrics-anomalydetector-timestampcolumn-columnname
            '''
            result = self._values.get("column_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimestampColumnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lookoutmetrics.CfnAnomalyDetector.VpcConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_id_list": "securityGroupIdList",
            "subnet_id_list": "subnetIdList",
        },
    )
    class VpcConfigurationProperty:
        def __init__(
            self,
            *,
            security_group_id_list: typing.Sequence[builtins.str],
            subnet_id_list: typing.Sequence[builtins.str],
        ) -> None:
            '''Contains configuration information about the Amazon Virtual Private Cloud (VPC).

            :param security_group_id_list: An array of strings containing the list of security groups.
            :param subnet_id_list: An array of strings containing the Amazon VPC subnet IDs (e.g., ``subnet-0bb1c79de3EXAMPLE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-vpcconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lookoutmetrics as lookoutmetrics
                
                vpc_configuration_property = lookoutmetrics.CfnAnomalyDetector.VpcConfigurationProperty(
                    security_group_id_list=["securityGroupIdList"],
                    subnet_id_list=["subnetIdList"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b0e193c483b7f0f4ee9e4f34c456400f9886edb4320e33f47274503e4e8bd07b)
                check_type(argname="argument security_group_id_list", value=security_group_id_list, expected_type=type_hints["security_group_id_list"])
                check_type(argname="argument subnet_id_list", value=subnet_id_list, expected_type=type_hints["subnet_id_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "security_group_id_list": security_group_id_list,
                "subnet_id_list": subnet_id_list,
            }

        @builtins.property
        def security_group_id_list(self) -> typing.List[builtins.str]:
            '''An array of strings containing the list of security groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-vpcconfiguration.html#cfn-lookoutmetrics-anomalydetector-vpcconfiguration-securitygroupidlist
            '''
            result = self._values.get("security_group_id_list")
            assert result is not None, "Required property 'security_group_id_list' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnet_id_list(self) -> typing.List[builtins.str]:
            '''An array of strings containing the Amazon VPC subnet IDs (e.g., ``subnet-0bb1c79de3EXAMPLE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lookoutmetrics-anomalydetector-vpcconfiguration.html#cfn-lookoutmetrics-anomalydetector-vpcconfiguration-subnetidlist
            '''
            result = self._values.get("subnet_id_list")
            assert result is not None, "Required property 'subnet_id_list' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lookoutmetrics.CfnAnomalyDetectorProps",
    jsii_struct_bases=[],
    name_mapping={
        "anomaly_detector_config": "anomalyDetectorConfig",
        "metric_set_list": "metricSetList",
        "anomaly_detector_description": "anomalyDetectorDescription",
        "anomaly_detector_name": "anomalyDetectorName",
        "kms_key_arn": "kmsKeyArn",
    },
)
class CfnAnomalyDetectorProps:
    def __init__(
        self,
        *,
        anomaly_detector_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.AnomalyDetectorConfigProperty, typing.Dict[builtins.str, typing.Any]]],
        metric_set_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.MetricSetProperty, typing.Dict[builtins.str, typing.Any]]]]],
        anomaly_detector_description: typing.Optional[builtins.str] = None,
        anomaly_detector_name: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnAnomalyDetector``.

        :param anomaly_detector_config: Contains information about the configuration of the anomaly detector.
        :param metric_set_list: The detector's dataset.
        :param anomaly_detector_description: A description of the detector.
        :param anomaly_detector_name: The name of the detector.
        :param kms_key_arn: The ARN of the KMS key to use to encrypt your data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lookoutmetrics as lookoutmetrics
            
            cfn_anomaly_detector_props = lookoutmetrics.CfnAnomalyDetectorProps(
                anomaly_detector_config=lookoutmetrics.CfnAnomalyDetector.AnomalyDetectorConfigProperty(
                    anomaly_detector_frequency="anomalyDetectorFrequency"
                ),
                metric_set_list=[lookoutmetrics.CfnAnomalyDetector.MetricSetProperty(
                    metric_list=[lookoutmetrics.CfnAnomalyDetector.MetricProperty(
                        aggregation_function="aggregationFunction",
                        metric_name="metricName",
            
                        # the properties below are optional
                        namespace="namespace"
                    )],
                    metric_set_name="metricSetName",
                    metric_source=lookoutmetrics.CfnAnomalyDetector.MetricSourceProperty(
                        app_flow_config=lookoutmetrics.CfnAnomalyDetector.AppFlowConfigProperty(
                            flow_name="flowName",
                            role_arn="roleArn"
                        ),
                        cloudwatch_config=lookoutmetrics.CfnAnomalyDetector.CloudwatchConfigProperty(
                            role_arn="roleArn"
                        ),
                        rds_source_config=lookoutmetrics.CfnAnomalyDetector.RDSSourceConfigProperty(
                            database_host="databaseHost",
                            database_name="databaseName",
                            database_port=123,
                            db_instance_identifier="dbInstanceIdentifier",
                            role_arn="roleArn",
                            secret_manager_arn="secretManagerArn",
                            table_name="tableName",
                            vpc_configuration=lookoutmetrics.CfnAnomalyDetector.VpcConfigurationProperty(
                                security_group_id_list=["securityGroupIdList"],
                                subnet_id_list=["subnetIdList"]
                            )
                        ),
                        redshift_source_config=lookoutmetrics.CfnAnomalyDetector.RedshiftSourceConfigProperty(
                            cluster_identifier="clusterIdentifier",
                            database_host="databaseHost",
                            database_name="databaseName",
                            database_port=123,
                            role_arn="roleArn",
                            secret_manager_arn="secretManagerArn",
                            table_name="tableName",
                            vpc_configuration=lookoutmetrics.CfnAnomalyDetector.VpcConfigurationProperty(
                                security_group_id_list=["securityGroupIdList"],
                                subnet_id_list=["subnetIdList"]
                            )
                        ),
                        s3_source_config=lookoutmetrics.CfnAnomalyDetector.S3SourceConfigProperty(
                            file_format_descriptor=lookoutmetrics.CfnAnomalyDetector.FileFormatDescriptorProperty(
                                csv_format_descriptor=lookoutmetrics.CfnAnomalyDetector.CsvFormatDescriptorProperty(
                                    charset="charset",
                                    contains_header=False,
                                    delimiter="delimiter",
                                    file_compression="fileCompression",
                                    header_list=["headerList"],
                                    quote_symbol="quoteSymbol"
                                ),
                                json_format_descriptor=lookoutmetrics.CfnAnomalyDetector.JsonFormatDescriptorProperty(
                                    charset="charset",
                                    file_compression="fileCompression"
                                )
                            ),
                            role_arn="roleArn",
            
                            # the properties below are optional
                            historical_data_path_list=["historicalDataPathList"],
                            templated_path_list=["templatedPathList"]
                        )
                    ),
            
                    # the properties below are optional
                    dimension_list=["dimensionList"],
                    metric_set_description="metricSetDescription",
                    metric_set_frequency="metricSetFrequency",
                    offset=123,
                    timestamp_column=lookoutmetrics.CfnAnomalyDetector.TimestampColumnProperty(
                        column_format="columnFormat",
                        column_name="columnName"
                    ),
                    timezone="timezone"
                )],
            
                # the properties below are optional
                anomaly_detector_description="anomalyDetectorDescription",
                anomaly_detector_name="anomalyDetectorName",
                kms_key_arn="kmsKeyArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac2e9b61e4663a0d7be16c47f2f04bda869f46de5537627485274ac9d915adb1)
            check_type(argname="argument anomaly_detector_config", value=anomaly_detector_config, expected_type=type_hints["anomaly_detector_config"])
            check_type(argname="argument metric_set_list", value=metric_set_list, expected_type=type_hints["metric_set_list"])
            check_type(argname="argument anomaly_detector_description", value=anomaly_detector_description, expected_type=type_hints["anomaly_detector_description"])
            check_type(argname="argument anomaly_detector_name", value=anomaly_detector_name, expected_type=type_hints["anomaly_detector_name"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "anomaly_detector_config": anomaly_detector_config,
            "metric_set_list": metric_set_list,
        }
        if anomaly_detector_description is not None:
            self._values["anomaly_detector_description"] = anomaly_detector_description
        if anomaly_detector_name is not None:
            self._values["anomaly_detector_name"] = anomaly_detector_name
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn

    @builtins.property
    def anomaly_detector_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnAnomalyDetector.AnomalyDetectorConfigProperty]:
        '''Contains information about the configuration of the anomaly detector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-anomalydetectorconfig
        '''
        result = self._values.get("anomaly_detector_config")
        assert result is not None, "Required property 'anomaly_detector_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnAnomalyDetector.AnomalyDetectorConfigProperty], result)

    @builtins.property
    def metric_set_list(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAnomalyDetector.MetricSetProperty]]]:
        '''The detector's dataset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-metricsetlist
        '''
        result = self._values.get("metric_set_list")
        assert result is not None, "Required property 'metric_set_list' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAnomalyDetector.MetricSetProperty]]], result)

    @builtins.property
    def anomaly_detector_description(self) -> typing.Optional[builtins.str]:
        '''A description of the detector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-anomalydetectordescription
        '''
        result = self._values.get("anomaly_detector_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def anomaly_detector_name(self) -> typing.Optional[builtins.str]:
        '''The name of the detector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-anomalydetectorname
        '''
        result = self._values.get("anomaly_detector_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the KMS key to use to encrypt your data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lookoutmetrics-anomalydetector.html#cfn-lookoutmetrics-anomalydetector-kmskeyarn
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAnomalyDetectorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAlert",
    "CfnAlertProps",
    "CfnAnomalyDetector",
    "CfnAnomalyDetectorProps",
]

publication.publish()

def _typecheckingstub__f8728605cf8a8c3531f6dae116746c94e17fc40f4b10454ed68253f7594f37b5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    action: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlert.ActionProperty, typing.Dict[builtins.str, typing.Any]]],
    alert_sensitivity_threshold: jsii.Number,
    anomaly_detector_arn: builtins.str,
    alert_description: typing.Optional[builtins.str] = None,
    alert_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af2583fccb79de99e1ffd4367cdbaef6fc5d3286d05c49c0757a5d05f7d45ebb(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11e72e40d199761b2debe19287dd74d247a4d6bf2de19a1586683619b6e42d40(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bca437e28138e0e51d01ea6b47ad80cc5df1f7e9796134c417b7df120770fed4(
    value: typing.Union[_IResolvable_da3f097b, CfnAlert.ActionProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16575316da180caba7d7b4d5bca451d1f5f4a58ac27976f3452052604cfeeab9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b0f01224b76c8ec6ed095f7d3914505315c1b87ad5c6bc322c51fc2182dd83d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c25b3f5e9ac3683a05d71bfdb651b264c95f00f413c50591d5f27474ca682a9b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3becde2093abb52b7666e46cd4095e177005405e86d6ea69e3f94b9f0519d0d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__918d1f90fc4698783779ca3d567c1aa1dbcc1df7f6364d530056c55317bb3300(
    *,
    lambda_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlert.LambdaConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sns_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlert.SNSConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a2741bd0f93f3161ddbbe1989db143d59b7d60f454031f9a7b4d003c7baa9dd(
    *,
    lambda_arn: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__408298e997cc645a10d8bca48400dc1f10d0a9d3264e454b49baf80bbe20c6c6(
    *,
    role_arn: builtins.str,
    sns_topic_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37b5e7a084e60c1889b63e691905589769e7d3d6e42edfe3ff8deb1be27e9b12(
    *,
    action: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlert.ActionProperty, typing.Dict[builtins.str, typing.Any]]],
    alert_sensitivity_threshold: jsii.Number,
    anomaly_detector_arn: builtins.str,
    alert_description: typing.Optional[builtins.str] = None,
    alert_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31ab81393e1b85b97eacf8fc50ccdd65726ebe4cd344f89434267d135a724809(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    anomaly_detector_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.AnomalyDetectorConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    metric_set_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.MetricSetProperty, typing.Dict[builtins.str, typing.Any]]]]],
    anomaly_detector_description: typing.Optional[builtins.str] = None,
    anomaly_detector_name: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dee8e95c5e0cd07fbf662c30c7577d6e82a165f56df5909679a83e680a28d4cc(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faaf017f46f2465273ce5085976d9c929a7fd12ab5e5a73a9cf4cdcd90f8fa69(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b781658d3f414a12c1a279f742c28faf8517d54f6c4bb78a545064da65050d8(
    value: typing.Union[_IResolvable_da3f097b, CfnAnomalyDetector.AnomalyDetectorConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__330a8461f141824d57906ef5a9c3660a9eb1a3a24dcf63724b3baff3125fdb5d(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAnomalyDetector.MetricSetProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18032fc3311c5d9f05368698835d2318d81a643b30222e23b5caa19113e42533(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3d3884d4fbb282a3dfdfc2e9f5a32ab31ec34ceef9bbe86c037573ea6f57857(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de024c053da6aec678335abd185c8c42f862ff0569545085611551174f93883e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a2fc99e8c1708c8e763f7b1eca903086d6ac7320bf7c3dfc662e7d2fd357cac(
    *,
    anomaly_detector_frequency: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38ea2c3771b7e331cc37cb9c01ea3318b3ac0b3dde9e431f4a06d9500e2280af(
    *,
    flow_name: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__724145604a2914634c7f2cf211053a9a2c2360fb02a943d0423285d69de7373f(
    *,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ba6cc8b192874991eb7b5ee2a82eb0aa9331612cf5907ca69728d2b36baa8fc(
    *,
    charset: typing.Optional[builtins.str] = None,
    contains_header: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    delimiter: typing.Optional[builtins.str] = None,
    file_compression: typing.Optional[builtins.str] = None,
    header_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    quote_symbol: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ddbd19438ab1247dbbe4eea827d6515d16a62ef2f2a3edd7eb00edd00e6f448(
    *,
    csv_format_descriptor: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.CsvFormatDescriptorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    json_format_descriptor: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.JsonFormatDescriptorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67e3166c183fb9595b36477950349ad78f5d3c5aa01cca2e5ceb5531c04426af(
    *,
    charset: typing.Optional[builtins.str] = None,
    file_compression: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df50eca477a61eb4e0b022a28e366212f515bdb4840ba1ebe300d9251e3d9240(
    *,
    aggregation_function: builtins.str,
    metric_name: builtins.str,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cce3005d3d219e3d045e48a5c12869a1fe9bcaf7f759c45e1ec58e3888d0e70(
    *,
    metric_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.MetricProperty, typing.Dict[builtins.str, typing.Any]]]]],
    metric_set_name: builtins.str,
    metric_source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.MetricSourceProperty, typing.Dict[builtins.str, typing.Any]]],
    dimension_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    metric_set_description: typing.Optional[builtins.str] = None,
    metric_set_frequency: typing.Optional[builtins.str] = None,
    offset: typing.Optional[jsii.Number] = None,
    timestamp_column: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.TimestampColumnProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    timezone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1339cbdc783ac0ba8f9fe1fabef3ca626523dad00e283af466740e6de7c4e41c(
    *,
    app_flow_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.AppFlowConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cloudwatch_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.CloudwatchConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    rds_source_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.RDSSourceConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    redshift_source_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.RedshiftSourceConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_source_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.S3SourceConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8feffc16f2d3df708e99199b419cda14195606cdd79f15131d328b2f5f9a6e6(
    *,
    database_host: builtins.str,
    database_name: builtins.str,
    database_port: jsii.Number,
    db_instance_identifier: builtins.str,
    role_arn: builtins.str,
    secret_manager_arn: builtins.str,
    table_name: builtins.str,
    vpc_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.VpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__569a554d8877d6747add9f55cb258a09d4a6172adb0b3966b0377ce8a3f0dd44(
    *,
    cluster_identifier: builtins.str,
    database_host: builtins.str,
    database_name: builtins.str,
    database_port: jsii.Number,
    role_arn: builtins.str,
    secret_manager_arn: builtins.str,
    table_name: builtins.str,
    vpc_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.VpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2104594e6dc20e604e9ef34cec5e3b48affde655dd8871d134d43d67ed6135b(
    *,
    file_format_descriptor: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.FileFormatDescriptorProperty, typing.Dict[builtins.str, typing.Any]]],
    role_arn: builtins.str,
    historical_data_path_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    templated_path_list: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aecf2888a0d1c17cdd4142e3c7ce9f01564679e174b26b805a0fd35e5fd4441(
    *,
    column_format: typing.Optional[builtins.str] = None,
    column_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0e193c483b7f0f4ee9e4f34c456400f9886edb4320e33f47274503e4e8bd07b(
    *,
    security_group_id_list: typing.Sequence[builtins.str],
    subnet_id_list: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac2e9b61e4663a0d7be16c47f2f04bda869f46de5537627485274ac9d915adb1(
    *,
    anomaly_detector_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.AnomalyDetectorConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    metric_set_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.MetricSetProperty, typing.Dict[builtins.str, typing.Any]]]]],
    anomaly_detector_description: typing.Optional[builtins.str] = None,
    anomaly_detector_name: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
