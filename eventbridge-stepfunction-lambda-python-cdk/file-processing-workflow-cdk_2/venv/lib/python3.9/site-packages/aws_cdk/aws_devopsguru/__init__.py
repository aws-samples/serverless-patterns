'''
# AWS::DevOpsGuru Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_devopsguru as devopsguru
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for DevOpsGuru construct libraries](https://constructs.dev/search?q=devopsguru)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::DevOpsGuru resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DevOpsGuru.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::DevOpsGuru](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DevOpsGuru.html).

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
class CfnLogAnomalyDetectionIntegration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_devopsguru.CfnLogAnomalyDetectionIntegration",
):
    '''Information about the integration of DevOps Guru with CloudWatch log groups for log anomaly detection.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-loganomalydetectionintegration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_devopsguru as devopsguru
        
        cfn_log_anomaly_detection_integration = devopsguru.CfnLogAnomalyDetectionIntegration(self, "MyCfnLogAnomalyDetectionIntegration")
    '''

    def __init__(self, scope: _constructs_77d1e7e8.Construct, id: builtins.str) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dc62acf712b07249b67b80a94f4e15a261a6b082a35061105bf54719686ddc1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLogAnomalyDetectionIntegrationProps()

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7d4c4b155787a36eae130b71f2a0e6f6ea7ceac0a4e10dacf22e236d23abb5c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fa7a52625be96af4c4be7ca9f2217bf8ca06cc3966dfa017e8f358dcd7ef4f68)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAccountId")
    def attr_account_id(self) -> builtins.str:
        '''The account ID associated with the integration of DevOps Guru with CloudWatch log groups for log anomaly detection.

        :cloudformationAttribute: AccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAccountId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_devopsguru.CfnLogAnomalyDetectionIntegrationProps",
    jsii_struct_bases=[],
    name_mapping={},
)
class CfnLogAnomalyDetectionIntegrationProps:
    def __init__(self) -> None:
        '''Properties for defining a ``CfnLogAnomalyDetectionIntegration``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-loganomalydetectionintegration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_devopsguru as devopsguru
            
            cfn_log_anomaly_detection_integration_props = devopsguru.CfnLogAnomalyDetectionIntegrationProps()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLogAnomalyDetectionIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnNotificationChannel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_devopsguru.CfnNotificationChannel",
):
    '''Adds a notification channel to DevOps Guru.

    A notification channel is used to notify you about important DevOps Guru events, such as when an insight is generated.

    If you use an Amazon SNS topic in another account, you must attach a policy to it that grants DevOps Guru permission to send it notifications. DevOps Guru adds the required policy on your behalf to send notifications using Amazon SNS in your account. DevOps Guru only supports standard SNS topics. For more information, see `Permissions for Amazon SNS topics <https://docs.aws.amazon.com/devops-guru/latest/userguide/sns-required-permissions.html>`_ .

    If you use an Amazon SNS topic that is encrypted by an AWS Key Management Service customer-managed key (CMK), then you must add permissions to the CMK. For more information, see `Permissions for AWS KMS–encrypted Amazon SNS topics <https://docs.aws.amazon.com/devops-guru/latest/userguide/sns-kms-permissions.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-notificationchannel.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_devopsguru as devopsguru
        
        cfn_notification_channel = devopsguru.CfnNotificationChannel(self, "MyCfnNotificationChannel",
            config=devopsguru.CfnNotificationChannel.NotificationChannelConfigProperty(
                filters=devopsguru.CfnNotificationChannel.NotificationFilterConfigProperty(
                    message_types=["messageTypes"],
                    severities=["severities"]
                ),
                sns=devopsguru.CfnNotificationChannel.SnsChannelConfigProperty(
                    topic_arn="topicArn"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnNotificationChannel.NotificationChannelConfigProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param config: A ``NotificationChannelConfig`` object that contains information about configured notification channels.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd2b521cca5ab7bb045c8de504725accf6a36d02b2e14e71a7be76772481e85a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnNotificationChannelProps(config=config)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0ac80062f41c2e7cc342a8c1e7b5d72173d0a61a2327f3200d834ba97eaca5e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__924773761b0011bd677e0d5082e992c5aa5b0080d1e71be43c14f321e9bdd5a7)
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
        '''The ID of the notification channel.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="config")
    def config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnNotificationChannel.NotificationChannelConfigProperty"]:
        '''A ``NotificationChannelConfig`` object that contains information about configured notification channels.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnNotificationChannel.NotificationChannelConfigProperty"], jsii.get(self, "config"))

    @config.setter
    def config(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnNotificationChannel.NotificationChannelConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99f146c8144832935a31424fa5b73be4a1c94b82c492846dc93af5c622327778)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "config", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsguru.CfnNotificationChannel.NotificationChannelConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"filters": "filters", "sns": "sns"},
    )
    class NotificationChannelConfigProperty:
        def __init__(
            self,
            *,
            filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnNotificationChannel.NotificationFilterConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnNotificationChannel.SnsChannelConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Information about notification channels you have configured with DevOps Guru.

            The one supported notification channel is Amazon Simple Notification Service (Amazon SNS).

            :param filters: The filter configurations for the Amazon SNS notification topic you use with DevOps Guru. If you do not provide filter configurations, the default configurations are to receive notifications for all message types of ``High`` or ``Medium`` severity.
            :param sns: Information about a notification channel configured in DevOps Guru to send notifications when insights are created. If you use an Amazon SNS topic in another account, you must attach a policy to it that grants DevOps Guru permission to send it notifications. DevOps Guru adds the required policy on your behalf to send notifications using Amazon SNS in your account. DevOps Guru only supports standard SNS topics. For more information, see `Permissions for Amazon SNS topics <https://docs.aws.amazon.com/devops-guru/latest/userguide/sns-required-permissions.html>`_ . If you use an Amazon SNS topic that is encrypted by an AWS Key Management Service customer-managed key (CMK), then you must add permissions to the CMK. For more information, see `Permissions for AWS KMS–encrypted Amazon SNS topics <https://docs.aws.amazon.com/devops-guru/latest/userguide/sns-kms-permissions.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-notificationchannelconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsguru as devopsguru
                
                notification_channel_config_property = devopsguru.CfnNotificationChannel.NotificationChannelConfigProperty(
                    filters=devopsguru.CfnNotificationChannel.NotificationFilterConfigProperty(
                        message_types=["messageTypes"],
                        severities=["severities"]
                    ),
                    sns=devopsguru.CfnNotificationChannel.SnsChannelConfigProperty(
                        topic_arn="topicArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__76f3bb02735021484b8466eaa789d614abc785c53daa318d01957c2fb095f05d)
                check_type(argname="argument filters", value=filters, expected_type=type_hints["filters"])
                check_type(argname="argument sns", value=sns, expected_type=type_hints["sns"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if filters is not None:
                self._values["filters"] = filters
            if sns is not None:
                self._values["sns"] = sns

        @builtins.property
        def filters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnNotificationChannel.NotificationFilterConfigProperty"]]:
            '''The filter configurations for the Amazon SNS notification topic you use with DevOps Guru.

            If you do not provide filter configurations, the default configurations are to receive notifications for all message types of ``High`` or ``Medium`` severity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-notificationchannelconfig.html#cfn-devopsguru-notificationchannel-notificationchannelconfig-filters
            '''
            result = self._values.get("filters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnNotificationChannel.NotificationFilterConfigProperty"]], result)

        @builtins.property
        def sns(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnNotificationChannel.SnsChannelConfigProperty"]]:
            '''Information about a notification channel configured in DevOps Guru to send notifications when insights are created.

            If you use an Amazon SNS topic in another account, you must attach a policy to it that grants DevOps Guru permission to send it notifications. DevOps Guru adds the required policy on your behalf to send notifications using Amazon SNS in your account. DevOps Guru only supports standard SNS topics. For more information, see `Permissions for Amazon SNS topics <https://docs.aws.amazon.com/devops-guru/latest/userguide/sns-required-permissions.html>`_ .

            If you use an Amazon SNS topic that is encrypted by an AWS Key Management Service customer-managed key (CMK), then you must add permissions to the CMK. For more information, see `Permissions for AWS KMS–encrypted Amazon SNS topics <https://docs.aws.amazon.com/devops-guru/latest/userguide/sns-kms-permissions.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-notificationchannelconfig.html#cfn-devopsguru-notificationchannel-notificationchannelconfig-sns
            '''
            result = self._values.get("sns")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnNotificationChannel.SnsChannelConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotificationChannelConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsguru.CfnNotificationChannel.NotificationFilterConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"message_types": "messageTypes", "severities": "severities"},
    )
    class NotificationFilterConfigProperty:
        def __init__(
            self,
            *,
            message_types: typing.Optional[typing.Sequence[builtins.str]] = None,
            severities: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The filter configurations for the Amazon SNS notification topic you use with DevOps Guru.

            You can choose to specify which events or message types to receive notifications for. You can also choose to specify which severity levels to receive notifications for.

            :param message_types: The events that you want to receive notifications for. For example, you can choose to receive notifications only when the severity level is upgraded or a new insight is created.
            :param severities: The severity levels that you want to receive notifications for. For example, you can choose to receive notifications only for insights with ``HIGH`` and ``MEDIUM`` severity levels. For more information, see `Understanding insight severities <https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-insights.html#understanding-insights-severities>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-notificationfilterconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsguru as devopsguru
                
                notification_filter_config_property = devopsguru.CfnNotificationChannel.NotificationFilterConfigProperty(
                    message_types=["messageTypes"],
                    severities=["severities"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__811f5641d983a377452e3a6fcaf46dba34bfdb7268a3eede27fe9fa75ef1c4cb)
                check_type(argname="argument message_types", value=message_types, expected_type=type_hints["message_types"])
                check_type(argname="argument severities", value=severities, expected_type=type_hints["severities"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if message_types is not None:
                self._values["message_types"] = message_types
            if severities is not None:
                self._values["severities"] = severities

        @builtins.property
        def message_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The events that you want to receive notifications for.

            For example, you can choose to receive notifications only when the severity level is upgraded or a new insight is created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-notificationfilterconfig.html#cfn-devopsguru-notificationchannel-notificationfilterconfig-messagetypes
            '''
            result = self._values.get("message_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def severities(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The severity levels that you want to receive notifications for.

            For example, you can choose to receive notifications only for insights with ``HIGH`` and ``MEDIUM`` severity levels. For more information, see `Understanding insight severities <https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-insights.html#understanding-insights-severities>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-notificationfilterconfig.html#cfn-devopsguru-notificationchannel-notificationfilterconfig-severities
            '''
            result = self._values.get("severities")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotificationFilterConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsguru.CfnNotificationChannel.SnsChannelConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"topic_arn": "topicArn"},
    )
    class SnsChannelConfigProperty:
        def __init__(self, *, topic_arn: typing.Optional[builtins.str] = None) -> None:
            '''Contains the Amazon Resource Name (ARN) of an Amazon Simple Notification Service topic.

            If you use an Amazon SNS topic in another account, you must attach a policy to it that grants DevOps Guru permission to send it notifications. DevOps Guru adds the required policy on your behalf to send notifications using Amazon SNS in your account. DevOps Guru only supports standard SNS topics. For more information, see `Permissions for Amazon SNS topics <https://docs.aws.amazon.com/devops-guru/latest/userguide/sns-required-permissions.html>`_ .

            If you use an Amazon SNS topic that is encrypted by an AWS Key Management Service customer-managed key (CMK), then you must add permissions to the CMK. For more information, see `Permissions for AWS KMS–encrypted Amazon SNS topics <https://docs.aws.amazon.com/devops-guru/latest/userguide/sns-kms-permissions.html>`_ .

            :param topic_arn: The Amazon Resource Name (ARN) of an Amazon Simple Notification Service topic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-snschannelconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsguru as devopsguru
                
                sns_channel_config_property = devopsguru.CfnNotificationChannel.SnsChannelConfigProperty(
                    topic_arn="topicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f676dd8e13b0e896b4dbd7914e021508023fd604626efc3db37424534f9b3fb7)
                check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if topic_arn is not None:
                self._values["topic_arn"] = topic_arn

        @builtins.property
        def topic_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of an Amazon Simple Notification Service topic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-notificationchannel-snschannelconfig.html#cfn-devopsguru-notificationchannel-snschannelconfig-topicarn
            '''
            result = self._values.get("topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnsChannelConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_devopsguru.CfnNotificationChannelProps",
    jsii_struct_bases=[],
    name_mapping={"config": "config"},
)
class CfnNotificationChannelProps:
    def __init__(
        self,
        *,
        config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnNotificationChannel.NotificationChannelConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnNotificationChannel``.

        :param config: A ``NotificationChannelConfig`` object that contains information about configured notification channels.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-notificationchannel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_devopsguru as devopsguru
            
            cfn_notification_channel_props = devopsguru.CfnNotificationChannelProps(
                config=devopsguru.CfnNotificationChannel.NotificationChannelConfigProperty(
                    filters=devopsguru.CfnNotificationChannel.NotificationFilterConfigProperty(
                        message_types=["messageTypes"],
                        severities=["severities"]
                    ),
                    sns=devopsguru.CfnNotificationChannel.SnsChannelConfigProperty(
                        topic_arn="topicArn"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4355b450ccbaf26da251417cf6bfda7a64bf8f5b28aa2a428ff14983f592a0d)
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "config": config,
        }

    @builtins.property
    def config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnNotificationChannel.NotificationChannelConfigProperty]:
        '''A ``NotificationChannelConfig`` object that contains information about configured notification channels.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-notificationchannel.html#cfn-devopsguru-notificationchannel-config
        '''
        result = self._values.get("config")
        assert result is not None, "Required property 'config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnNotificationChannel.NotificationChannelConfigProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNotificationChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResourceCollection(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_devopsguru.CfnResourceCollection",
):
    '''A collection of AWS resources supported by DevOps Guru.

    The one type of AWS resource collection supported is AWS CloudFormation stacks. DevOps Guru can be configured to analyze only the AWS resources that are defined in the stacks.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-resourcecollection.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_devopsguru as devopsguru
        
        cfn_resource_collection = devopsguru.CfnResourceCollection(self, "MyCfnResourceCollection",
            resource_collection_filter=devopsguru.CfnResourceCollection.ResourceCollectionFilterProperty(
                cloud_formation=devopsguru.CfnResourceCollection.CloudFormationCollectionFilterProperty(
                    stack_names=["stackNames"]
                ),
                tags=[devopsguru.CfnResourceCollection.TagCollectionProperty(
                    app_boundary_key="appBoundaryKey",
                    tag_values=["tagValues"]
                )]
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        resource_collection_filter: typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceCollection.ResourceCollectionFilterProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param resource_collection_filter: Information about a filter used to specify which AWS resources are analyzed for anomalous behavior by DevOps Guru.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3c60a96b04c3d10c4530a8ce94f0b7ce1f25e7d301936f232eea2b553bbd33b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourceCollectionProps(
            resource_collection_filter=resource_collection_filter
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dc1ff2550f5066d44416d68125e4e8107e64ec6ed6d506f793f162842d9285d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9f3a81bf39e1c8c0767e45cfe087e50c2ff4e7c1effa92c5cda47ccc82c1a8bc)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrResourceCollectionType")
    def attr_resource_collection_type(self) -> builtins.str:
        '''The type of AWS resource collections to return.

        The one valid value is ``CLOUD_FORMATION`` for AWS CloudFormation stacks.

        :cloudformationAttribute: ResourceCollectionType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceCollectionType"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="resourceCollectionFilter")
    def resource_collection_filter(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnResourceCollection.ResourceCollectionFilterProperty"]:
        '''Information about a filter used to specify which AWS resources are analyzed for anomalous behavior by DevOps Guru.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnResourceCollection.ResourceCollectionFilterProperty"], jsii.get(self, "resourceCollectionFilter"))

    @resource_collection_filter.setter
    def resource_collection_filter(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnResourceCollection.ResourceCollectionFilterProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__190553b64928ca35dedd8270f4831a7ae6fe3d91f6a7d73828303b5f2ee32926)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceCollectionFilter", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsguru.CfnResourceCollection.CloudFormationCollectionFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"stack_names": "stackNames"},
    )
    class CloudFormationCollectionFilterProperty:
        def __init__(
            self,
            *,
            stack_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Information about AWS CloudFormation stacks.

            You can use up to 1000 stacks to specify which AWS resources in your account to analyze. For more information, see `Stacks <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html>`_ in the *AWS CloudFormation User Guide* .

            :param stack_names: An array of CloudFormation stack names.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-cloudformationcollectionfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsguru as devopsguru
                
                cloud_formation_collection_filter_property = devopsguru.CfnResourceCollection.CloudFormationCollectionFilterProperty(
                    stack_names=["stackNames"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e3128a221e4819c3f66844d7148314a0558e3b18e67159cda565baca77d2d426)
                check_type(argname="argument stack_names", value=stack_names, expected_type=type_hints["stack_names"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if stack_names is not None:
                self._values["stack_names"] = stack_names

        @builtins.property
        def stack_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An array of CloudFormation stack names.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-cloudformationcollectionfilter.html#cfn-devopsguru-resourcecollection-cloudformationcollectionfilter-stacknames
            '''
            result = self._values.get("stack_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudFormationCollectionFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsguru.CfnResourceCollection.ResourceCollectionFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"cloud_formation": "cloudFormation", "tags": "tags"},
    )
    class ResourceCollectionFilterProperty:
        def __init__(
            self,
            *,
            cloud_formation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnResourceCollection.CloudFormationCollectionFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            tags: typing.Optional[typing.Sequence[typing.Union["CfnResourceCollection.TagCollectionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Information about a filter used to specify which AWS resources are analyzed for anomalous behavior by DevOps Guru.

            :param cloud_formation: Information about AWS CloudFormation stacks. You can use up to 1000 stacks to specify which AWS resources in your account to analyze. For more information, see `Stacks <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html>`_ in the *AWS CloudFormation User Guide* .
            :param tags: The AWS tags used to filter the resources in the resource collection. Tags help you identify and organize your AWS resources. Many AWS services support tagging, so you can assign the same tag to resources from different services to indicate that the resources are related. For example, you can assign the same tag to an Amazon DynamoDB table resource that you assign to an AWS Lambda function. For more information about using tags, see the `Tagging best practices <https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html>`_ whitepaper. Each AWS tag has two parts. - A tag *key* (for example, ``CostCenter`` , ``Environment`` , ``Project`` , or ``Secret`` ). Tag *keys* are case-sensitive. - A field known as a tag *value* (for example, ``111122223333`` , ``Production`` , or a team name). Omitting the tag *value* is the same as using an empty string. Like tag *keys* , tag *values* are case-sensitive. The tag value is a required property when AppBoundaryKey is specified. Together these are known as *key* - *value* pairs. .. epigraph:: The string used for a *key* in a tag that you use to define your resource coverage must begin with the prefix ``Devops-guru-`` . The tag *key* might be ``DevOps-Guru-deployment-application`` or ``devops-guru-rds-application`` . When you create a *key* , the case of characters in the *key* can be whatever you choose. After you create a *key* , it is case-sensitive. For example, DevOps Guru works with a *key* named ``devops-guru-rds`` and a *key* named ``DevOps-Guru-RDS`` , and these act as two different *keys* . Possible *key* / *value* pairs in your application might be ``Devops-Guru-production-application/RDS`` or ``Devops-Guru-production-application/containers`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-resourcecollectionfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsguru as devopsguru
                
                resource_collection_filter_property = devopsguru.CfnResourceCollection.ResourceCollectionFilterProperty(
                    cloud_formation=devopsguru.CfnResourceCollection.CloudFormationCollectionFilterProperty(
                        stack_names=["stackNames"]
                    ),
                    tags=[devopsguru.CfnResourceCollection.TagCollectionProperty(
                        app_boundary_key="appBoundaryKey",
                        tag_values=["tagValues"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ee66c55cdc496bbfebd09cac9ffd673aa9559ae002fbf42bf8fc4ee6d1877781)
                check_type(argname="argument cloud_formation", value=cloud_formation, expected_type=type_hints["cloud_formation"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloud_formation is not None:
                self._values["cloud_formation"] = cloud_formation
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def cloud_formation(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceCollection.CloudFormationCollectionFilterProperty"]]:
            '''Information about AWS CloudFormation stacks.

            You can use up to 1000 stacks to specify which AWS resources in your account to analyze. For more information, see `Stacks <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html>`_ in the *AWS CloudFormation User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-resourcecollectionfilter.html#cfn-devopsguru-resourcecollection-resourcecollectionfilter-cloudformation
            '''
            result = self._values.get("cloud_formation")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnResourceCollection.CloudFormationCollectionFilterProperty"]], result)

        @builtins.property
        def tags(
            self,
        ) -> typing.Optional[typing.List["CfnResourceCollection.TagCollectionProperty"]]:
            '''The AWS tags used to filter the resources in the resource collection.

            Tags help you identify and organize your AWS resources. Many AWS services support tagging, so you can assign the same tag to resources from different services to indicate that the resources are related. For example, you can assign the same tag to an Amazon DynamoDB table resource that you assign to an AWS Lambda function. For more information about using tags, see the `Tagging best practices <https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html>`_ whitepaper.

            Each AWS tag has two parts.

            - A tag *key* (for example, ``CostCenter`` , ``Environment`` , ``Project`` , or ``Secret`` ). Tag *keys* are case-sensitive.
            - A field known as a tag *value* (for example, ``111122223333`` , ``Production`` , or a team name). Omitting the tag *value* is the same as using an empty string. Like tag *keys* , tag *values* are case-sensitive. The tag value is a required property when AppBoundaryKey is specified.

            Together these are known as *key* - *value* pairs.
            .. epigraph::

               The string used for a *key* in a tag that you use to define your resource coverage must begin with the prefix ``Devops-guru-`` . The tag *key* might be ``DevOps-Guru-deployment-application`` or ``devops-guru-rds-application`` . When you create a *key* , the case of characters in the *key* can be whatever you choose. After you create a *key* , it is case-sensitive. For example, DevOps Guru works with a *key* named ``devops-guru-rds`` and a *key* named ``DevOps-Guru-RDS`` , and these act as two different *keys* . Possible *key* / *value* pairs in your application might be ``Devops-Guru-production-application/RDS`` or ``Devops-Guru-production-application/containers`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-resourcecollectionfilter.html#cfn-devopsguru-resourcecollection-resourcecollectionfilter-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List["CfnResourceCollection.TagCollectionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceCollectionFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsguru.CfnResourceCollection.TagCollectionProperty",
        jsii_struct_bases=[],
        name_mapping={"app_boundary_key": "appBoundaryKey", "tag_values": "tagValues"},
    )
    class TagCollectionProperty:
        def __init__(
            self,
            *,
            app_boundary_key: typing.Optional[builtins.str] = None,
            tag_values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A collection of AWS tags.

            Tags help you identify and organize your AWS resources. Many AWS services support tagging, so you can assign the same tag to resources from different services to indicate that the resources are related. For example, you can assign the same tag to an Amazon DynamoDB table resource that you assign to an AWS Lambda function. For more information about using tags, see the `Tagging best practices <https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html>`_ whitepaper.

            Each AWS tag has two parts.

            - A tag *key* (for example, ``CostCenter`` , ``Environment`` , ``Project`` , or ``Secret`` ). Tag *keys* are case-sensitive.
            - A field known as a tag *value* (for example, ``111122223333`` , ``Production`` , or a team name). Omitting the tag *value* is the same as using an empty string. Like tag *keys* , tag *values* are case-sensitive. The tag value is a required property when *AppBoundaryKey* is specified.

            Together these are known as *key* - *value* pairs.
            .. epigraph::

               The string used for a *key* in a tag that you use to define your resource coverage must begin with the prefix ``Devops-guru-`` . The tag *key* might be ``DevOps-Guru-deployment-application`` or ``devops-guru-rds-application`` . When you create a *key* , the case of characters in the *key* can be whatever you choose. After you create a *key* , it is case-sensitive. For example, DevOps Guru works with a *key* named ``devops-guru-rds`` and a *key* named ``DevOps-Guru-RDS`` , and these act as two different *keys* . Possible *key* / *value* pairs in your application might be ``Devops-Guru-production-application/RDS`` or ``Devops-Guru-production-application/containers`` .

            :param app_boundary_key: An AWS tag *key* that is used to identify the AWS resources that DevOps Guru analyzes. All AWS resources in your account and Region tagged with this *key* make up your DevOps Guru application and analysis boundary. .. epigraph:: The string used for a *key* in a tag that you use to define your resource coverage must begin with the prefix ``Devops-guru-`` . The tag *key* might be ``DevOps-Guru-deployment-application`` or ``devops-guru-rds-application`` . When you create a *key* , the case of characters in the *key* can be whatever you choose. After you create a *key* , it is case-sensitive. For example, DevOps Guru works with a *key* named ``devops-guru-rds`` and a *key* named ``DevOps-Guru-RDS`` , and these act as two different *keys* . Possible *key* / *value* pairs in your application might be ``Devops-Guru-production-application/RDS`` or ``Devops-Guru-production-application/containers`` .
            :param tag_values: The values in an AWS tag collection. The tag's *value* is a field used to associate a string with the tag *key* (for example, ``111122223333`` , ``Production`` , or a team name). The *key* and *value* are the tag's *key* pair. Omitting the tag *value* is the same as using an empty string. Like tag *keys* , tag *values* are case-sensitive. You can specify a maximum of 256 characters for a tag value. The tag value is a required property when *AppBoundaryKey* is specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-tagcollection.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsguru as devopsguru
                
                tag_collection_property = devopsguru.CfnResourceCollection.TagCollectionProperty(
                    app_boundary_key="appBoundaryKey",
                    tag_values=["tagValues"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0b4f37d65023f55182ed11e895b64bf88216adbee73234d0310a2bd1c59defbf)
                check_type(argname="argument app_boundary_key", value=app_boundary_key, expected_type=type_hints["app_boundary_key"])
                check_type(argname="argument tag_values", value=tag_values, expected_type=type_hints["tag_values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if app_boundary_key is not None:
                self._values["app_boundary_key"] = app_boundary_key
            if tag_values is not None:
                self._values["tag_values"] = tag_values

        @builtins.property
        def app_boundary_key(self) -> typing.Optional[builtins.str]:
            '''An AWS tag *key* that is used to identify the AWS resources that DevOps Guru analyzes.

            All AWS resources in your account and Region tagged with this *key* make up your DevOps Guru application and analysis boundary.
            .. epigraph::

               The string used for a *key* in a tag that you use to define your resource coverage must begin with the prefix ``Devops-guru-`` . The tag *key* might be ``DevOps-Guru-deployment-application`` or ``devops-guru-rds-application`` . When you create a *key* , the case of characters in the *key* can be whatever you choose. After you create a *key* , it is case-sensitive. For example, DevOps Guru works with a *key* named ``devops-guru-rds`` and a *key* named ``DevOps-Guru-RDS`` , and these act as two different *keys* . Possible *key* / *value* pairs in your application might be ``Devops-Guru-production-application/RDS`` or ``Devops-Guru-production-application/containers`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-tagcollection.html#cfn-devopsguru-resourcecollection-tagcollection-appboundarykey
            '''
            result = self._values.get("app_boundary_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tag_values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The values in an AWS tag collection.

            The tag's *value* is a field used to associate a string with the tag *key* (for example, ``111122223333`` , ``Production`` , or a team name). The *key* and *value* are the tag's *key* pair. Omitting the tag *value* is the same as using an empty string. Like tag *keys* , tag *values* are case-sensitive. You can specify a maximum of 256 characters for a tag value. The tag value is a required property when *AppBoundaryKey* is specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsguru-resourcecollection-tagcollection.html#cfn-devopsguru-resourcecollection-tagcollection-tagvalues
            '''
            result = self._values.get("tag_values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagCollectionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_devopsguru.CfnResourceCollectionProps",
    jsii_struct_bases=[],
    name_mapping={"resource_collection_filter": "resourceCollectionFilter"},
)
class CfnResourceCollectionProps:
    def __init__(
        self,
        *,
        resource_collection_filter: typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceCollection.ResourceCollectionFilterProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnResourceCollection``.

        :param resource_collection_filter: Information about a filter used to specify which AWS resources are analyzed for anomalous behavior by DevOps Guru.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-resourcecollection.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_devopsguru as devopsguru
            
            cfn_resource_collection_props = devopsguru.CfnResourceCollectionProps(
                resource_collection_filter=devopsguru.CfnResourceCollection.ResourceCollectionFilterProperty(
                    cloud_formation=devopsguru.CfnResourceCollection.CloudFormationCollectionFilterProperty(
                        stack_names=["stackNames"]
                    ),
                    tags=[devopsguru.CfnResourceCollection.TagCollectionProperty(
                        app_boundary_key="appBoundaryKey",
                        tag_values=["tagValues"]
                    )]
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a350f923367858b1db2669f34b07661e6fd7d789e23538549313574a16f2ed62)
            check_type(argname="argument resource_collection_filter", value=resource_collection_filter, expected_type=type_hints["resource_collection_filter"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_collection_filter": resource_collection_filter,
        }

    @builtins.property
    def resource_collection_filter(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnResourceCollection.ResourceCollectionFilterProperty]:
        '''Information about a filter used to specify which AWS resources are analyzed for anomalous behavior by DevOps Guru.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsguru-resourcecollection.html#cfn-devopsguru-resourcecollection-resourcecollectionfilter
        '''
        result = self._values.get("resource_collection_filter")
        assert result is not None, "Required property 'resource_collection_filter' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnResourceCollection.ResourceCollectionFilterProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceCollectionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnLogAnomalyDetectionIntegration",
    "CfnLogAnomalyDetectionIntegrationProps",
    "CfnNotificationChannel",
    "CfnNotificationChannelProps",
    "CfnResourceCollection",
    "CfnResourceCollectionProps",
]

publication.publish()

def _typecheckingstub__7dc62acf712b07249b67b80a94f4e15a261a6b082a35061105bf54719686ddc1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7d4c4b155787a36eae130b71f2a0e6f6ea7ceac0a4e10dacf22e236d23abb5c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa7a52625be96af4c4be7ca9f2217bf8ca06cc3966dfa017e8f358dcd7ef4f68(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd2b521cca5ab7bb045c8de504725accf6a36d02b2e14e71a7be76772481e85a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnNotificationChannel.NotificationChannelConfigProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0ac80062f41c2e7cc342a8c1e7b5d72173d0a61a2327f3200d834ba97eaca5e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__924773761b0011bd677e0d5082e992c5aa5b0080d1e71be43c14f321e9bdd5a7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99f146c8144832935a31424fa5b73be4a1c94b82c492846dc93af5c622327778(
    value: typing.Union[_IResolvable_da3f097b, CfnNotificationChannel.NotificationChannelConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76f3bb02735021484b8466eaa789d614abc785c53daa318d01957c2fb095f05d(
    *,
    filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnNotificationChannel.NotificationFilterConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnNotificationChannel.SnsChannelConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__811f5641d983a377452e3a6fcaf46dba34bfdb7268a3eede27fe9fa75ef1c4cb(
    *,
    message_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    severities: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f676dd8e13b0e896b4dbd7914e021508023fd604626efc3db37424534f9b3fb7(
    *,
    topic_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4355b450ccbaf26da251417cf6bfda7a64bf8f5b28aa2a428ff14983f592a0d(
    *,
    config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnNotificationChannel.NotificationChannelConfigProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3c60a96b04c3d10c4530a8ce94f0b7ce1f25e7d301936f232eea2b553bbd33b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    resource_collection_filter: typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceCollection.ResourceCollectionFilterProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dc1ff2550f5066d44416d68125e4e8107e64ec6ed6d506f793f162842d9285d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f3a81bf39e1c8c0767e45cfe087e50c2ff4e7c1effa92c5cda47ccc82c1a8bc(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__190553b64928ca35dedd8270f4831a7ae6fe3d91f6a7d73828303b5f2ee32926(
    value: typing.Union[_IResolvable_da3f097b, CfnResourceCollection.ResourceCollectionFilterProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3128a221e4819c3f66844d7148314a0558e3b18e67159cda565baca77d2d426(
    *,
    stack_names: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee66c55cdc496bbfebd09cac9ffd673aa9559ae002fbf42bf8fc4ee6d1877781(
    *,
    cloud_formation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceCollection.CloudFormationCollectionFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnResourceCollection.TagCollectionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b4f37d65023f55182ed11e895b64bf88216adbee73234d0310a2bd1c59defbf(
    *,
    app_boundary_key: typing.Optional[builtins.str] = None,
    tag_values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a350f923367858b1db2669f34b07661e6fd7d789e23538549313574a16f2ed62(
    *,
    resource_collection_filter: typing.Union[_IResolvable_da3f097b, typing.Union[CfnResourceCollection.ResourceCollectionFilterProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass
