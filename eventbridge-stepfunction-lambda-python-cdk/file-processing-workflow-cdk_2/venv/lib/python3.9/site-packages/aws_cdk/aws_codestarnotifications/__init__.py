'''
# AWS CodeStarNotifications Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

## NotificationRule

The `NotificationRule` construct defines an AWS CodeStarNotifications rule.
The rule specifies the events you want notifications about and the targets
(such as Amazon SNS topics or AWS Chatbot clients configured for Slack)
where you want to receive them.
Notification targets are objects that implement the `INotificationRuleTarget`
interface and notification source is object that implement the `INotificationRuleSource` interface.

## Notification Targets

This module includes classes that implement the `INotificationRuleTarget` interface for SNS and slack in AWS Chatbot.

The following targets are supported:

* `SNS`: specify event and notify to SNS topic.
* `AWS Chatbot`: specify event and notify to slack channel and only support `SlackChannelConfiguration`.

## Examples

```python
import aws_cdk.aws_codestarnotifications as notifications
import aws_cdk.aws_codebuild as codebuild
import aws_cdk.aws_sns as sns
import aws_cdk.aws_chatbot as chatbot


project = codebuild.PipelineProject(self, "MyProject")

topic = sns.Topic(self, "MyTopic1")

slack = chatbot.SlackChannelConfiguration(self, "MySlackChannel",
    slack_channel_configuration_name="YOUR_CHANNEL_NAME",
    slack_workspace_id="YOUR_SLACK_WORKSPACE_ID",
    slack_channel_id="YOUR_SLACK_CHANNEL_ID"
)

rule = notifications.NotificationRule(self, "NotificationRule",
    source=project,
    events=["codebuild-project-build-state-succeeded", "codebuild-project-build-state-failed"
    ],
    targets=[topic]
)
rule.add_target(slack)
```

## Notification Source

This module includes classes that implement the `INotificationRuleSource` interface for AWS CodeBuild,
AWS CodePipeline and will support AWS CodeCommit, AWS CodeDeploy in future.

The following sources are supported:

* `AWS CodeBuild`: support codebuild project to trigger notification when event specified.
* `AWS CodePipeline`: support codepipeline to trigger notification when event specified.

## Events

For the complete list of supported event types for CodeBuild and CodePipeline, see:

* [Events for notification rules on build projects](https://docs.aws.amazon.com/dtconsole/latest/userguide/concepts.html#events-ref-buildproject).
* [Events for notification rules on pipelines](https://docs.aws.amazon.com/dtconsole/latest/userguide/concepts.html#events-ref-pipeline).
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
    IResource as _IResource_c80c4260,
    ITaggable as _ITaggable_36806126,
    Resource as _Resource_45bc6135,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnNotificationRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codestarnotifications.CfnNotificationRule",
):
    '''Creates a notification rule for a resource.

    The rule specifies the events you want notifications about and the targets (such as AWS Chatbot topics or AWS Chatbot clients configured for Slack) where you want to receive them.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_codestarnotifications as codestarnotifications
        
        cfn_notification_rule = codestarnotifications.CfnNotificationRule(self, "MyCfnNotificationRule",
            detail_type="detailType",
            event_type_ids=["eventTypeIds"],
            name="name",
            resource="resource",
            targets=[codestarnotifications.CfnNotificationRule.TargetProperty(
                target_address="targetAddress",
                target_type="targetType"
            )],
        
            # the properties below are optional
            created_by="createdBy",
            event_type_id="eventTypeId",
            status="status",
            tags={
                "tags_key": "tags"
            },
            target_address="targetAddress"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        detail_type: builtins.str,
        event_type_ids: typing.Sequence[builtins.str],
        name: builtins.str,
        resource: builtins.str,
        targets: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnNotificationRule.TargetProperty", typing.Dict[builtins.str, typing.Any]]]]],
        created_by: typing.Optional[builtins.str] = None,
        event_type_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        target_address: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param detail_type: The level of detail to include in the notifications for this resource. ``BASIC`` will include only the contents of the event as it would appear in Amazon CloudWatch. ``FULL`` will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created.
        :param event_type_ids: A list of event types associated with this notification rule. For a complete list of event types and IDs, see `Notification concepts <https://docs.aws.amazon.com/dtconsole/latest/userguide/concepts.html#concepts-api>`_ in the *Developer Tools Console User Guide* .
        :param name: The name for the notification rule. Notification rule names must be unique in your AWS account .
        :param resource: The Amazon Resource Name (ARN) of the resource to associate with the notification rule. Supported resources include pipelines in AWS CodePipeline , repositories in AWS CodeCommit , and build projects in AWS CodeBuild .
        :param targets: A list of Amazon Resource Names (ARNs) of Amazon Simple Notification Service topics and AWS Chatbot clients to associate with the notification rule.
        :param created_by: 
        :param event_type_id: 
        :param status: The status of the notification rule. The default value is ``ENABLED`` . If the status is set to ``DISABLED`` , notifications aren't sent for the notification rule.
        :param tags: A list of tags to apply to this notification rule. Key names cannot start with " ``aws`` ".
        :param target_address: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__724996b7b605c1ccec7fc232a8e933db042d262c4932936112f67cf6c1086ace)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnNotificationRuleProps(
            detail_type=detail_type,
            event_type_ids=event_type_ids,
            name=name,
            resource=resource,
            targets=targets,
            created_by=created_by,
            event_type_id=event_type_id,
            status=status,
            tags=tags,
            target_address=target_address,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87ef25f46cfb8cebf7f1dcf20988342af27ada2610c31d3973ea93bae9079a0c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__40d4fee78d1cb9b3932feffc8bdedc027a5eb171eb25256c49259b1081959e4d)
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
        '''
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
    @jsii.member(jsii_name="detailType")
    def detail_type(self) -> builtins.str:
        '''The level of detail to include in the notifications for this resource.'''
        return typing.cast(builtins.str, jsii.get(self, "detailType"))

    @detail_type.setter
    def detail_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e77575e9e7fed1aaa856782984f55190cacebb0127b3a420e5abd83c05124eb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "detailType", value)

    @builtins.property
    @jsii.member(jsii_name="eventTypeIds")
    def event_type_ids(self) -> typing.List[builtins.str]:
        '''A list of event types associated with this notification rule.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "eventTypeIds"))

    @event_type_ids.setter
    def event_type_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb90cf2b1d4d9f08c073745d794c6b1baab1fbeeb5c0bbda2d12a48b0d9f5108)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventTypeIds", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name for the notification rule.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5204aa375f9e4e9997555d623037738864aa5e6cea213dafa3cc2dbd08fe4b5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the resource to associate with the notification rule.'''
        return typing.cast(builtins.str, jsii.get(self, "resource"))

    @resource.setter
    def resource(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9e7eb7809f54a6ab1cc7633e54f753ffc88aee5242769abb918737ba1ece93e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resource", value)

    @builtins.property
    @jsii.member(jsii_name="targets")
    def targets(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnNotificationRule.TargetProperty"]]]:
        '''A list of Amazon Resource Names (ARNs) of Amazon Simple Notification Service topics and AWS Chatbot clients to associate with the notification rule.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnNotificationRule.TargetProperty"]]], jsii.get(self, "targets"))

    @targets.setter
    def targets(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnNotificationRule.TargetProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4259d2e21a6aa16f5b382a6da87f39d19bce9c3ff108949185b9a52a0cdc3fb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targets", value)

    @builtins.property
    @jsii.member(jsii_name="createdBy")
    def created_by(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createdBy"))

    @created_by.setter
    def created_by(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3a38c963a2f57c2eef37336737a4291ab12ddbea2f275489ad41a0f3b1626c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createdBy", value)

    @builtins.property
    @jsii.member(jsii_name="eventTypeId")
    def event_type_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eventTypeId"))

    @event_type_id.setter
    def event_type_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f4c0a2f101ac5756c08ca6fb073dca683dc73b0a107311500211b14b0fa45bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventTypeId", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the notification rule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__912dbe323db8cf96405e266076a8cdf4072b4a2dd758c0d981017c758190eab3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of tags to apply to this notification rule.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__659b0f3db6d4ef27d56157bd416c0c93d14864433c289b856f1de2e84a2263eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="targetAddress")
    def target_address(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetAddress"))

    @target_address.setter
    def target_address(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b60a2bf9b823ac3550ee164c0b5272642cbc4e5c916ec347fa569051a338b1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetAddress", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codestarnotifications.CfnNotificationRule.TargetProperty",
        jsii_struct_bases=[],
        name_mapping={"target_address": "targetAddress", "target_type": "targetType"},
    )
    class TargetProperty:
        def __init__(
            self,
            *,
            target_address: builtins.str,
            target_type: builtins.str,
        ) -> None:
            '''Information about the AWS Chatbot topics or AWS Chatbot clients associated with a notification rule.

            :param target_address: The Amazon Resource Name (ARN) of the AWS Chatbot topic or AWS Chatbot client.
            :param target_type: The target type. Can be an Amazon Simple Notification Service topic or AWS Chatbot client. - Amazon Simple Notification Service topics are specified as ``SNS`` . - AWS Chatbot clients are specified as ``AWSChatbotSlack`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestarnotifications-notificationrule-target.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codestarnotifications as codestarnotifications
                
                target_property = codestarnotifications.CfnNotificationRule.TargetProperty(
                    target_address="targetAddress",
                    target_type="targetType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c5808f80235ebed2f288b2e5e65437084fde23b48cb2a5daa84d6bf156a1aa57)
                check_type(argname="argument target_address", value=target_address, expected_type=type_hints["target_address"])
                check_type(argname="argument target_type", value=target_type, expected_type=type_hints["target_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "target_address": target_address,
                "target_type": target_type,
            }

        @builtins.property
        def target_address(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the AWS Chatbot topic or AWS Chatbot client.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestarnotifications-notificationrule-target.html#cfn-codestarnotifications-notificationrule-target-targetaddress
            '''
            result = self._values.get("target_address")
            assert result is not None, "Required property 'target_address' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target_type(self) -> builtins.str:
            '''The target type. Can be an Amazon Simple Notification Service topic or AWS Chatbot client.

            - Amazon Simple Notification Service topics are specified as ``SNS`` .
            - AWS Chatbot clients are specified as ``AWSChatbotSlack`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codestarnotifications-notificationrule-target.html#cfn-codestarnotifications-notificationrule-target-targettype
            '''
            result = self._values.get("target_type")
            assert result is not None, "Required property 'target_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codestarnotifications.CfnNotificationRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "detail_type": "detailType",
        "event_type_ids": "eventTypeIds",
        "name": "name",
        "resource": "resource",
        "targets": "targets",
        "created_by": "createdBy",
        "event_type_id": "eventTypeId",
        "status": "status",
        "tags": "tags",
        "target_address": "targetAddress",
    },
)
class CfnNotificationRuleProps:
    def __init__(
        self,
        *,
        detail_type: builtins.str,
        event_type_ids: typing.Sequence[builtins.str],
        name: builtins.str,
        resource: builtins.str,
        targets: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnNotificationRule.TargetProperty, typing.Dict[builtins.str, typing.Any]]]]],
        created_by: typing.Optional[builtins.str] = None,
        event_type_id: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        target_address: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnNotificationRule``.

        :param detail_type: The level of detail to include in the notifications for this resource. ``BASIC`` will include only the contents of the event as it would appear in Amazon CloudWatch. ``FULL`` will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created.
        :param event_type_ids: A list of event types associated with this notification rule. For a complete list of event types and IDs, see `Notification concepts <https://docs.aws.amazon.com/dtconsole/latest/userguide/concepts.html#concepts-api>`_ in the *Developer Tools Console User Guide* .
        :param name: The name for the notification rule. Notification rule names must be unique in your AWS account .
        :param resource: The Amazon Resource Name (ARN) of the resource to associate with the notification rule. Supported resources include pipelines in AWS CodePipeline , repositories in AWS CodeCommit , and build projects in AWS CodeBuild .
        :param targets: A list of Amazon Resource Names (ARNs) of Amazon Simple Notification Service topics and AWS Chatbot clients to associate with the notification rule.
        :param created_by: 
        :param event_type_id: 
        :param status: The status of the notification rule. The default value is ``ENABLED`` . If the status is set to ``DISABLED`` , notifications aren't sent for the notification rule.
        :param tags: A list of tags to apply to this notification rule. Key names cannot start with " ``aws`` ".
        :param target_address: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codestarnotifications as codestarnotifications
            
            cfn_notification_rule_props = codestarnotifications.CfnNotificationRuleProps(
                detail_type="detailType",
                event_type_ids=["eventTypeIds"],
                name="name",
                resource="resource",
                targets=[codestarnotifications.CfnNotificationRule.TargetProperty(
                    target_address="targetAddress",
                    target_type="targetType"
                )],
            
                # the properties below are optional
                created_by="createdBy",
                event_type_id="eventTypeId",
                status="status",
                tags={
                    "tags_key": "tags"
                },
                target_address="targetAddress"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__952abbe5911505f5e5382fd91146586f2692114d447a4f16d4f5749cae4799fe)
            check_type(argname="argument detail_type", value=detail_type, expected_type=type_hints["detail_type"])
            check_type(argname="argument event_type_ids", value=event_type_ids, expected_type=type_hints["event_type_ids"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            check_type(argname="argument targets", value=targets, expected_type=type_hints["targets"])
            check_type(argname="argument created_by", value=created_by, expected_type=type_hints["created_by"])
            check_type(argname="argument event_type_id", value=event_type_id, expected_type=type_hints["event_type_id"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument target_address", value=target_address, expected_type=type_hints["target_address"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "detail_type": detail_type,
            "event_type_ids": event_type_ids,
            "name": name,
            "resource": resource,
            "targets": targets,
        }
        if created_by is not None:
            self._values["created_by"] = created_by
        if event_type_id is not None:
            self._values["event_type_id"] = event_type_id
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags
        if target_address is not None:
            self._values["target_address"] = target_address

    @builtins.property
    def detail_type(self) -> builtins.str:
        '''The level of detail to include in the notifications for this resource.

        ``BASIC`` will include only the contents of the event as it would appear in Amazon CloudWatch. ``FULL`` will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-detailtype
        '''
        result = self._values.get("detail_type")
        assert result is not None, "Required property 'detail_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_type_ids(self) -> typing.List[builtins.str]:
        '''A list of event types associated with this notification rule.

        For a complete list of event types and IDs, see `Notification concepts <https://docs.aws.amazon.com/dtconsole/latest/userguide/concepts.html#concepts-api>`_ in the *Developer Tools Console User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-eventtypeids
        '''
        result = self._values.get("event_type_ids")
        assert result is not None, "Required property 'event_type_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name for the notification rule.

        Notification rule names must be unique in your AWS account .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the resource to associate with the notification rule.

        Supported resources include pipelines in AWS CodePipeline , repositories in AWS CodeCommit , and build projects in AWS CodeBuild .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-resource
        '''
        result = self._values.get("resource")
        assert result is not None, "Required property 'resource' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def targets(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnNotificationRule.TargetProperty]]]:
        '''A list of Amazon Resource Names (ARNs) of Amazon Simple Notification Service topics and AWS Chatbot clients to associate with the notification rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-targets
        '''
        result = self._values.get("targets")
        assert result is not None, "Required property 'targets' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnNotificationRule.TargetProperty]]], result)

    @builtins.property
    def created_by(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-createdby
        '''
        result = self._values.get("created_by")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_type_id(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-eventtypeid
        '''
        result = self._values.get("event_type_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the notification rule.

        The default value is ``ENABLED`` . If the status is set to ``DISABLED`` , notifications aren't sent for the notification rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of tags to apply to this notification rule.

        Key names cannot start with " ``aws`` ".

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def target_address(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-targetaddress
        '''
        result = self._values.get("target_address")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNotificationRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_codestarnotifications.DetailType")
class DetailType(enum.Enum):
    '''The level of detail to include in the notifications for this resource.'''

    BASIC = "BASIC"
    '''BASIC will include only the contents of the event as it would appear in AWS CloudWatch.'''
    FULL = "FULL"
    '''FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created.'''


@jsii.interface(jsii_type="aws-cdk-lib.aws_codestarnotifications.INotificationRule")
class INotificationRule(_IResource_c80c4260, typing_extensions.Protocol):
    '''Represents a notification rule.'''

    @builtins.property
    @jsii.member(jsii_name="notificationRuleArn")
    def notification_rule_arn(self) -> builtins.str:
        '''The ARN of the notification rule (i.e. arn:aws:codestar-notifications:::notificationrule/01234abcde).

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="addTarget")
    def add_target(self, target: "INotificationRuleTarget") -> builtins.bool:
        '''Adds target to notification rule.

        :param target: The SNS topic or AWS Chatbot Slack target.

        :return: boolean - return true if it had any effect
        '''
        ...


class _INotificationRuleProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''Represents a notification rule.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_codestarnotifications.INotificationRule"

    @builtins.property
    @jsii.member(jsii_name="notificationRuleArn")
    def notification_rule_arn(self) -> builtins.str:
        '''The ARN of the notification rule (i.e. arn:aws:codestar-notifications:::notificationrule/01234abcde).

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "notificationRuleArn"))

    @jsii.member(jsii_name="addTarget")
    def add_target(self, target: "INotificationRuleTarget") -> builtins.bool:
        '''Adds target to notification rule.

        :param target: The SNS topic or AWS Chatbot Slack target.

        :return: boolean - return true if it had any effect
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83568cba2bd196cd0611084c807a07f3158a16140c8d6c4d35238d6419431a3e)
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        return typing.cast(builtins.bool, jsii.invoke(self, "addTarget", [target]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INotificationRule).__jsii_proxy_class__ = lambda : _INotificationRuleProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.aws_codestarnotifications.INotificationRuleSource"
)
class INotificationRuleSource(typing_extensions.Protocol):
    '''Represents a notification source The source that allows CodeBuild and CodePipeline to associate with this rule.'''

    @jsii.member(jsii_name="bindAsNotificationRuleSource")
    def bind_as_notification_rule_source(
        self,
        scope: _constructs_77d1e7e8.Construct,
    ) -> "NotificationRuleSourceConfig":
        '''Returns a source configuration for notification rule.

        :param scope: -
        '''
        ...


class _INotificationRuleSourceProxy:
    '''Represents a notification source The source that allows CodeBuild and CodePipeline to associate with this rule.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_codestarnotifications.INotificationRuleSource"

    @jsii.member(jsii_name="bindAsNotificationRuleSource")
    def bind_as_notification_rule_source(
        self,
        scope: _constructs_77d1e7e8.Construct,
    ) -> "NotificationRuleSourceConfig":
        '''Returns a source configuration for notification rule.

        :param scope: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5450ef736fad66a5746a2acf129158273757bccca5695cd9088cbd31c1190d4a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast("NotificationRuleSourceConfig", jsii.invoke(self, "bindAsNotificationRuleSource", [scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INotificationRuleSource).__jsii_proxy_class__ = lambda : _INotificationRuleSourceProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.aws_codestarnotifications.INotificationRuleTarget"
)
class INotificationRuleTarget(typing_extensions.Protocol):
    '''Represents a notification target That allows AWS Chatbot and SNS topic to associate with this rule target.'''

    @jsii.member(jsii_name="bindAsNotificationRuleTarget")
    def bind_as_notification_rule_target(
        self,
        scope: _constructs_77d1e7e8.Construct,
    ) -> "NotificationRuleTargetConfig":
        '''Returns a target configuration for notification rule.

        :param scope: -
        '''
        ...


class _INotificationRuleTargetProxy:
    '''Represents a notification target That allows AWS Chatbot and SNS topic to associate with this rule target.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_codestarnotifications.INotificationRuleTarget"

    @jsii.member(jsii_name="bindAsNotificationRuleTarget")
    def bind_as_notification_rule_target(
        self,
        scope: _constructs_77d1e7e8.Construct,
    ) -> "NotificationRuleTargetConfig":
        '''Returns a target configuration for notification rule.

        :param scope: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1aabe87bcc3bcfcb31e776adf52a667c84dfa7282f1c25dd08dd858cf88b5792)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast("NotificationRuleTargetConfig", jsii.invoke(self, "bindAsNotificationRuleTarget", [scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INotificationRuleTarget).__jsii_proxy_class__ = lambda : _INotificationRuleTargetProxy


@jsii.implements(INotificationRule)
class NotificationRule(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codestarnotifications.NotificationRule",
):
    '''A new notification rule.

    :resource: AWS::CodeStarNotifications::NotificationRule
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_codestarnotifications as notifications
        import aws_cdk.aws_codebuild as codebuild
        import aws_cdk.aws_sns as sns
        import aws_cdk.aws_chatbot as chatbot
        
        
        project = codebuild.PipelineProject(self, "MyProject")
        
        topic = sns.Topic(self, "MyTopic1")
        
        slack = chatbot.SlackChannelConfiguration(self, "MySlackChannel",
            slack_channel_configuration_name="YOUR_CHANNEL_NAME",
            slack_workspace_id="YOUR_SLACK_WORKSPACE_ID",
            slack_channel_id="YOUR_SLACK_CHANNEL_ID"
        )
        
        rule = notifications.NotificationRule(self, "NotificationRule",
            source=project,
            events=["codebuild-project-build-state-succeeded", "codebuild-project-build-state-failed"
            ],
            targets=[topic]
        )
        rule.add_target(slack)
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        events: typing.Sequence[builtins.str],
        source: INotificationRuleSource,
        targets: typing.Optional[typing.Sequence[INotificationRuleTarget]] = None,
        detail_type: typing.Optional[DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param events: A list of event types associated with this notification rule. For a complete list of event types and IDs, see Notification concepts in the Developer Tools Console User Guide.
        :param source: The Amazon Resource Name (ARN) of the resource to associate with the notification rule. Currently, Supported sources include pipelines in AWS CodePipeline, build projects in AWS CodeBuild, and repositories in AWS CodeCommit in this L2 constructor.
        :param targets: The targets to register for the notification destination. Default: - No targets are added to the rule. Use ``addTarget()`` to add a target.
        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ee042127cf39a85f944067772f0419c8ac6769379b69d847458271eeb8ab318)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = NotificationRuleProps(
            events=events,
            source=source,
            targets=targets,
            detail_type=detail_type,
            enabled=enabled,
            notification_rule_name=notification_rule_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromNotificationRuleArn")
    @builtins.classmethod
    def from_notification_rule_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        notification_rule_arn: builtins.str,
    ) -> INotificationRule:
        '''Import an existing notification rule provided an ARN.

        :param scope: The parent creating construct.
        :param id: The construct's name.
        :param notification_rule_arn: Notification rule ARN (i.e. arn:aws:codestar-notifications:::notificationrule/01234abcde).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c632c338e62acde6cbe6e9a621df456c5b97c1a83557f6e8004c96305cca6d53)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument notification_rule_arn", value=notification_rule_arn, expected_type=type_hints["notification_rule_arn"])
        return typing.cast(INotificationRule, jsii.sinvoke(cls, "fromNotificationRuleArn", [scope, id, notification_rule_arn]))

    @jsii.member(jsii_name="addTarget")
    def add_target(self, target: INotificationRuleTarget) -> builtins.bool:
        '''Adds target to notification rule.

        :param target: The SNS topic or AWS Chatbot Slack target.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ae4822f460efa58f235b9774da89d7f779da55fe51601a3cdfdf7b24e56913c)
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        return typing.cast(builtins.bool, jsii.invoke(self, "addTarget", [target]))

    @builtins.property
    @jsii.member(jsii_name="notificationRuleArn")
    def notification_rule_arn(self) -> builtins.str:
        '''The ARN of the notification rule (i.e. arn:aws:codestar-notifications:::notificationrule/01234abcde).

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "notificationRuleArn"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codestarnotifications.NotificationRuleOptions",
    jsii_struct_bases=[],
    name_mapping={
        "detail_type": "detailType",
        "enabled": "enabled",
        "notification_rule_name": "notificationRuleName",
    },
)
class NotificationRuleOptions:
    def __init__(
        self,
        *,
        detail_type: typing.Optional[DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Standard set of options for ``notifyOnXxx`` codestar notification handler on construct.

        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codestarnotifications as codestarnotifications
            
            notification_rule_options = codestarnotifications.NotificationRuleOptions(
                detail_type=codestarnotifications.DetailType.BASIC,
                enabled=False,
                notification_rule_name="notificationRuleName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eefabcfdf7bed8d3d87d052ee762b71c3b6147378fc2dcef592f76197869ec52)
            check_type(argname="argument detail_type", value=detail_type, expected_type=type_hints["detail_type"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument notification_rule_name", value=notification_rule_name, expected_type=type_hints["notification_rule_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if detail_type is not None:
            self._values["detail_type"] = detail_type
        if enabled is not None:
            self._values["enabled"] = enabled
        if notification_rule_name is not None:
            self._values["notification_rule_name"] = notification_rule_name

    @builtins.property
    def detail_type(self) -> typing.Optional[DetailType]:
        '''The level of detail to include in the notifications for this resource.

        BASIC will include only the contents of the event as it would appear in AWS CloudWatch.
        FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created.

        :default: DetailType.FULL
        '''
        result = self._values.get("detail_type")
        return typing.cast(typing.Optional[DetailType], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''The status of the notification rule.

        If the enabled is set to DISABLED, notifications aren't sent for the notification rule.

        :default: true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def notification_rule_name(self) -> typing.Optional[builtins.str]:
        '''The name for the notification rule.

        Notification rule names must be unique in your AWS account.

        :default: - generated from the ``id``
        '''
        result = self._values.get("notification_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationRuleOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codestarnotifications.NotificationRuleProps",
    jsii_struct_bases=[NotificationRuleOptions],
    name_mapping={
        "detail_type": "detailType",
        "enabled": "enabled",
        "notification_rule_name": "notificationRuleName",
        "events": "events",
        "source": "source",
        "targets": "targets",
    },
)
class NotificationRuleProps(NotificationRuleOptions):
    def __init__(
        self,
        *,
        detail_type: typing.Optional[DetailType] = None,
        enabled: typing.Optional[builtins.bool] = None,
        notification_rule_name: typing.Optional[builtins.str] = None,
        events: typing.Sequence[builtins.str],
        source: INotificationRuleSource,
        targets: typing.Optional[typing.Sequence[INotificationRuleTarget]] = None,
    ) -> None:
        '''Properties for a new notification rule.

        :param detail_type: The level of detail to include in the notifications for this resource. BASIC will include only the contents of the event as it would appear in AWS CloudWatch. FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created. Default: DetailType.FULL
        :param enabled: The status of the notification rule. If the enabled is set to DISABLED, notifications aren't sent for the notification rule. Default: true
        :param notification_rule_name: The name for the notification rule. Notification rule names must be unique in your AWS account. Default: - generated from the ``id``
        :param events: A list of event types associated with this notification rule. For a complete list of event types and IDs, see Notification concepts in the Developer Tools Console User Guide.
        :param source: The Amazon Resource Name (ARN) of the resource to associate with the notification rule. Currently, Supported sources include pipelines in AWS CodePipeline, build projects in AWS CodeBuild, and repositories in AWS CodeCommit in this L2 constructor.
        :param targets: The targets to register for the notification destination. Default: - No targets are added to the rule. Use ``addTarget()`` to add a target.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_codestarnotifications as notifications
            import aws_cdk.aws_codebuild as codebuild
            import aws_cdk.aws_sns as sns
            import aws_cdk.aws_chatbot as chatbot
            
            
            project = codebuild.PipelineProject(self, "MyProject")
            
            topic = sns.Topic(self, "MyTopic1")
            
            slack = chatbot.SlackChannelConfiguration(self, "MySlackChannel",
                slack_channel_configuration_name="YOUR_CHANNEL_NAME",
                slack_workspace_id="YOUR_SLACK_WORKSPACE_ID",
                slack_channel_id="YOUR_SLACK_CHANNEL_ID"
            )
            
            rule = notifications.NotificationRule(self, "NotificationRule",
                source=project,
                events=["codebuild-project-build-state-succeeded", "codebuild-project-build-state-failed"
                ],
                targets=[topic]
            )
            rule.add_target(slack)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07e191339712f728b76ba8a634b1678dff009608132b685c7342315eab988d78)
            check_type(argname="argument detail_type", value=detail_type, expected_type=type_hints["detail_type"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument notification_rule_name", value=notification_rule_name, expected_type=type_hints["notification_rule_name"])
            check_type(argname="argument events", value=events, expected_type=type_hints["events"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument targets", value=targets, expected_type=type_hints["targets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "events": events,
            "source": source,
        }
        if detail_type is not None:
            self._values["detail_type"] = detail_type
        if enabled is not None:
            self._values["enabled"] = enabled
        if notification_rule_name is not None:
            self._values["notification_rule_name"] = notification_rule_name
        if targets is not None:
            self._values["targets"] = targets

    @builtins.property
    def detail_type(self) -> typing.Optional[DetailType]:
        '''The level of detail to include in the notifications for this resource.

        BASIC will include only the contents of the event as it would appear in AWS CloudWatch.
        FULL will include any supplemental information provided by AWS CodeStar Notifications and/or the service for the resource for which the notification is created.

        :default: DetailType.FULL
        '''
        result = self._values.get("detail_type")
        return typing.cast(typing.Optional[DetailType], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''The status of the notification rule.

        If the enabled is set to DISABLED, notifications aren't sent for the notification rule.

        :default: true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def notification_rule_name(self) -> typing.Optional[builtins.str]:
        '''The name for the notification rule.

        Notification rule names must be unique in your AWS account.

        :default: - generated from the ``id``
        '''
        result = self._values.get("notification_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def events(self) -> typing.List[builtins.str]:
        '''A list of event types associated with this notification rule.

        For a complete list of event types and IDs, see Notification concepts in the Developer Tools Console User Guide.

        :see: https://docs.aws.amazon.com/dtconsole/latest/userguide/concepts.html#concepts-api
        '''
        result = self._values.get("events")
        assert result is not None, "Required property 'events' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def source(self) -> INotificationRuleSource:
        '''The Amazon Resource Name (ARN) of the resource to associate with the notification rule.

        Currently, Supported sources include pipelines in AWS CodePipeline, build projects in AWS CodeBuild, and repositories in AWS CodeCommit in this L2 constructor.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.html#cfn-codestarnotifications-notificationrule-resource
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(INotificationRuleSource, result)

    @builtins.property
    def targets(self) -> typing.Optional[typing.List[INotificationRuleTarget]]:
        '''The targets to register for the notification destination.

        :default: - No targets are added to the rule. Use ``addTarget()`` to add a target.
        '''
        result = self._values.get("targets")
        return typing.cast(typing.Optional[typing.List[INotificationRuleTarget]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codestarnotifications.NotificationRuleSourceConfig",
    jsii_struct_bases=[],
    name_mapping={"source_arn": "sourceArn"},
)
class NotificationRuleSourceConfig:
    def __init__(self, *, source_arn: builtins.str) -> None:
        '''Information about the Codebuild or CodePipeline associated with a notification source.

        :param source_arn: The Amazon Resource Name (ARN) of the notification source.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codestarnotifications as codestarnotifications
            
            notification_rule_source_config = codestarnotifications.NotificationRuleSourceConfig(
                source_arn="sourceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d360e17c334b6a0f70e67ffff0c1887ea63e43f8b4efcce27df4db191f21ce0)
            check_type(argname="argument source_arn", value=source_arn, expected_type=type_hints["source_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "source_arn": source_arn,
        }

    @builtins.property
    def source_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the notification source.'''
        result = self._values.get("source_arn")
        assert result is not None, "Required property 'source_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationRuleSourceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codestarnotifications.NotificationRuleTargetConfig",
    jsii_struct_bases=[],
    name_mapping={"target_address": "targetAddress", "target_type": "targetType"},
)
class NotificationRuleTargetConfig:
    def __init__(
        self,
        *,
        target_address: builtins.str,
        target_type: builtins.str,
    ) -> None:
        '''Information about the SNS topic or AWS Chatbot client associated with a notification target.

        :param target_address: The Amazon Resource Name (ARN) of the Amazon SNS topic or AWS Chatbot client.
        :param target_type: The target type. Can be an Amazon SNS topic or AWS Chatbot client.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codestarnotifications as codestarnotifications
            
            notification_rule_target_config = codestarnotifications.NotificationRuleTargetConfig(
                target_address="targetAddress",
                target_type="targetType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6f32c99ca69e59363f10dc680579548d678dad8805ff6c48b7a60d0aa5f940c)
            check_type(argname="argument target_address", value=target_address, expected_type=type_hints["target_address"])
            check_type(argname="argument target_type", value=target_type, expected_type=type_hints["target_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_address": target_address,
            "target_type": target_type,
        }

    @builtins.property
    def target_address(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic or AWS Chatbot client.'''
        result = self._values.get("target_address")
        assert result is not None, "Required property 'target_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_type(self) -> builtins.str:
        '''The target type.

        Can be an Amazon SNS topic or AWS Chatbot client.
        '''
        result = self._values.get("target_type")
        assert result is not None, "Required property 'target_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationRuleTargetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnNotificationRule",
    "CfnNotificationRuleProps",
    "DetailType",
    "INotificationRule",
    "INotificationRuleSource",
    "INotificationRuleTarget",
    "NotificationRule",
    "NotificationRuleOptions",
    "NotificationRuleProps",
    "NotificationRuleSourceConfig",
    "NotificationRuleTargetConfig",
]

publication.publish()

def _typecheckingstub__724996b7b605c1ccec7fc232a8e933db042d262c4932936112f67cf6c1086ace(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    detail_type: builtins.str,
    event_type_ids: typing.Sequence[builtins.str],
    name: builtins.str,
    resource: builtins.str,
    targets: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnNotificationRule.TargetProperty, typing.Dict[builtins.str, typing.Any]]]]],
    created_by: typing.Optional[builtins.str] = None,
    event_type_id: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    target_address: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87ef25f46cfb8cebf7f1dcf20988342af27ada2610c31d3973ea93bae9079a0c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40d4fee78d1cb9b3932feffc8bdedc027a5eb171eb25256c49259b1081959e4d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e77575e9e7fed1aaa856782984f55190cacebb0127b3a420e5abd83c05124eb6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb90cf2b1d4d9f08c073745d794c6b1baab1fbeeb5c0bbda2d12a48b0d9f5108(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5204aa375f9e4e9997555d623037738864aa5e6cea213dafa3cc2dbd08fe4b5f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9e7eb7809f54a6ab1cc7633e54f753ffc88aee5242769abb918737ba1ece93e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4259d2e21a6aa16f5b382a6da87f39d19bce9c3ff108949185b9a52a0cdc3fb1(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnNotificationRule.TargetProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3a38c963a2f57c2eef37336737a4291ab12ddbea2f275489ad41a0f3b1626c2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f4c0a2f101ac5756c08ca6fb073dca683dc73b0a107311500211b14b0fa45bd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__912dbe323db8cf96405e266076a8cdf4072b4a2dd758c0d981017c758190eab3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__659b0f3db6d4ef27d56157bd416c0c93d14864433c289b856f1de2e84a2263eb(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b60a2bf9b823ac3550ee164c0b5272642cbc4e5c916ec347fa569051a338b1b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5808f80235ebed2f288b2e5e65437084fde23b48cb2a5daa84d6bf156a1aa57(
    *,
    target_address: builtins.str,
    target_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__952abbe5911505f5e5382fd91146586f2692114d447a4f16d4f5749cae4799fe(
    *,
    detail_type: builtins.str,
    event_type_ids: typing.Sequence[builtins.str],
    name: builtins.str,
    resource: builtins.str,
    targets: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnNotificationRule.TargetProperty, typing.Dict[builtins.str, typing.Any]]]]],
    created_by: typing.Optional[builtins.str] = None,
    event_type_id: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    target_address: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83568cba2bd196cd0611084c807a07f3158a16140c8d6c4d35238d6419431a3e(
    target: INotificationRuleTarget,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5450ef736fad66a5746a2acf129158273757bccca5695cd9088cbd31c1190d4a(
    scope: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1aabe87bcc3bcfcb31e776adf52a667c84dfa7282f1c25dd08dd858cf88b5792(
    scope: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ee042127cf39a85f944067772f0419c8ac6769379b69d847458271eeb8ab318(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    events: typing.Sequence[builtins.str],
    source: INotificationRuleSource,
    targets: typing.Optional[typing.Sequence[INotificationRuleTarget]] = None,
    detail_type: typing.Optional[DetailType] = None,
    enabled: typing.Optional[builtins.bool] = None,
    notification_rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c632c338e62acde6cbe6e9a621df456c5b97c1a83557f6e8004c96305cca6d53(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    notification_rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ae4822f460efa58f235b9774da89d7f779da55fe51601a3cdfdf7b24e56913c(
    target: INotificationRuleTarget,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eefabcfdf7bed8d3d87d052ee762b71c3b6147378fc2dcef592f76197869ec52(
    *,
    detail_type: typing.Optional[DetailType] = None,
    enabled: typing.Optional[builtins.bool] = None,
    notification_rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07e191339712f728b76ba8a634b1678dff009608132b685c7342315eab988d78(
    *,
    detail_type: typing.Optional[DetailType] = None,
    enabled: typing.Optional[builtins.bool] = None,
    notification_rule_name: typing.Optional[builtins.str] = None,
    events: typing.Sequence[builtins.str],
    source: INotificationRuleSource,
    targets: typing.Optional[typing.Sequence[INotificationRuleTarget]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d360e17c334b6a0f70e67ffff0c1887ea63e43f8b4efcce27df4db191f21ce0(
    *,
    source_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6f32c99ca69e59363f10dc680579548d678dad8805ff6c48b7a60d0aa5f940c(
    *,
    target_address: builtins.str,
    target_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
