'''
# AWS::Chatbot Construct Library

AWS Chatbot is an AWS service that enables DevOps and software development teams to use Slack chat rooms to monitor and respond to operational events in their AWS Cloud. AWS Chatbot processes AWS service notifications from Amazon Simple Notification Service (Amazon SNS), and forwards them to Slack chat rooms so teams can analyze and act on them immediately, regardless of location.

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_chatbot as chatbot
import aws_cdk.aws_sns as sns
import aws_cdk.aws_iam as iam


slack_channel = chatbot.SlackChannelConfiguration(self, "MySlackChannel",
    slack_channel_configuration_name="YOUR_CHANNEL_NAME",
    slack_workspace_id="YOUR_SLACK_WORKSPACE_ID",
    slack_channel_id="YOUR_SLACK_CHANNEL_ID"
)

slack_channel.add_to_role_policy(iam.PolicyStatement(
    effect=iam.Effect.ALLOW,
    actions=["s3:GetObject"
    ],
    resources=["arn:aws:s3:::abc/xyz/123.txt"]
))

slack_channel.add_notification_topic(sns.Topic(self, "MyTopic"))
```

## Log Group

Slack channel configuration automatically create a log group with the name `/aws/chatbot/<configuration-name>` in `us-east-1` upon first execution with
log data set to never expire.

The `logRetention` property can be used to set a different expiration period. A log group will be created if not already exists.
If the log group already exists, it's expiration will be configured to the value specified in this construct (never expire, by default).

By default, CDK uses the AWS SDK retry options when interacting with the log group. The `logRetentionRetryOptions` property
allows you to customize the maximum number of retries and base backoff duration.

*Note* that, if `logRetention` is set, a [CloudFormation custom
resource](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html) is added
to the stack that pre-creates the log group as part of the stack deployment, if it already doesn't exist, and sets the
correct log retention period (never expire, by default).

## Guardrails

By default slack channel will use `AdministratorAccess` managed policy as guardrail policy.
The `guardrailPolicies` property can be used to set a different set of managed policies.
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
    Duration as _Duration_4839e8c3,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    IResource as _IResource_c80c4260,
    Resource as _Resource_45bc6135,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_cloudwatch import (
    Metric as _Metric_e396a4dc,
    MetricOptions as _MetricOptions_1788b62f,
    Unit as _Unit_61bc6f70,
)
from ..aws_codestarnotifications import (
    INotificationRuleTarget as _INotificationRuleTarget_faa3b79b,
    NotificationRuleTargetConfig as _NotificationRuleTargetConfig_ea27e095,
)
from ..aws_iam import (
    IGrantable as _IGrantable_71c4f5de,
    IManagedPolicy as _IManagedPolicy_c3b0dcbf,
    IPrincipal as _IPrincipal_539bb2fd,
    IRole as _IRole_235f5d8e,
    PolicyStatement as _PolicyStatement_0fe33853,
)
from ..aws_logs import (
    LogRetentionRetryOptions as _LogRetentionRetryOptions_62d80a14,
    RetentionDays as _RetentionDays_070f99f0,
)
from ..aws_sns import ITopic as _ITopic_9eca4852


@jsii.implements(_IInspectable_c2943556)
class CfnMicrosoftTeamsChannelConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_chatbot.CfnMicrosoftTeamsChannelConfiguration",
):
    '''The ``AWS::Chatbot::MicrosoftTeamsChannelConfiguration`` resource configures a Microsoft Teams channel to allow users to use AWS Chatbot with AWS CloudFormation templates.

    This resource requires some setup to be done in the AWS Chatbot console. To provide the required Microsoft Teams team and tenant IDs, you must perform the initial authorization flow with Microsoft Teams in the AWS Chatbot console, then copy and paste the IDs from the console. For more details, see steps 1-4 in `Setting Up AWS Chatbot with Microsoft Teams <https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup>`_ in the *AWS Chatbot Administrator Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-microsoftteamschannelconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_chatbot as chatbot
        
        cfn_microsoft_teams_channel_configuration = chatbot.CfnMicrosoftTeamsChannelConfiguration(self, "MyCfnMicrosoftTeamsChannelConfiguration",
            configuration_name="configurationName",
            iam_role_arn="iamRoleArn",
            team_id="teamId",
            teams_channel_id="teamsChannelId",
            teams_tenant_id="teamsTenantId",
        
            # the properties below are optional
            guardrail_policies=["guardrailPolicies"],
            logging_level="loggingLevel",
            sns_topic_arns=["snsTopicArns"],
            user_role_required=False
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        configuration_name: builtins.str,
        iam_role_arn: builtins.str,
        team_id: builtins.str,
        teams_channel_id: builtins.str,
        teams_tenant_id: builtins.str,
        guardrail_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_level: typing.Optional[builtins.str] = None,
        sns_topic_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        user_role_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param configuration_name: The name of the configuration.
        :param iam_role_arn: The ARN of the IAM role that defines the permissions for AWS Chatbot . This is a user-defined role that AWS Chatbot will assume. This is not the service-linked role. For more information, see `IAM Policies for AWS Chatbot <https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html>`_ .
        :param team_id: The ID of the Microsoft Team authorized with AWS Chatbot . To get the team ID, you must perform the initial authorization flow with Microsoft Teams in the AWS Chatbot console. Then you can copy and paste the team ID from the console. For more details, see steps 1-4 in `Get started with Microsoft Teams <https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup>`_ in the *AWS Chatbot Administrator Guide* .
        :param teams_channel_id: The ID of the Microsoft Teams channel. To get the channel ID, open Microsoft Teams, right click on the channel name in the left pane, then choose Copy. An example of the channel ID syntax is: ``19%3ab6ef35dc342d56ba5654e6fc6d25a071%40thread.tacv2`` .
        :param teams_tenant_id: The ID of the Microsoft Teams tenant. To get the tenant ID, you must perform the initial authorization flow with Microsoft Teams in the AWS Chatbot console. Then you can copy and paste the tenant ID from the console. For more details, see steps 1-4 in `Get started with Microsoft Teams <https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup>`_ in the *AWS Chatbot Administrator Guide* .
        :param guardrail_policies: The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed 'AdministratorAccess' policy is applied as a default if this is not set.
        :param logging_level: Specifies the logging level for this configuration. This property affects the log entries pushed to Amazon CloudWatch Logs. Logging levels include ``ERROR`` , ``INFO`` , or ``NONE`` . Default: - "NONE"
        :param sns_topic_arns: The ARNs of the SNS topics that deliver notifications to AWS Chatbot .
        :param user_role_required: Enables use of a user role requirement in your chat configuration. Default: - false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62f6b943071fca79376376fd20660d7b707a1026a9039a0c12c88895d7f39b05)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMicrosoftTeamsChannelConfigurationProps(
            configuration_name=configuration_name,
            iam_role_arn=iam_role_arn,
            team_id=team_id,
            teams_channel_id=teams_channel_id,
            teams_tenant_id=teams_tenant_id,
            guardrail_policies=guardrail_policies,
            logging_level=logging_level,
            sns_topic_arns=sns_topic_arns,
            user_role_required=user_role_required,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46600197e082ba9fc6d055c23e70f7f73de26074b20358edbb7348ae3fb1f908)
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
            type_hints = typing.get_type_hints(_typecheckingstub__89615163f4db8d0acf5a1e87300a200fc030e21f6faf513d0af1e4093b25e33d)
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
        '''Amazon Resource Name (ARN) of the configuration.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="configurationName")
    def configuration_name(self) -> builtins.str:
        '''The name of the configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "configurationName"))

    @configuration_name.setter
    def configuration_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__853492827ec4d32419905b108885cd7dfb3bfcc97356414d7093f3ffde1cc102)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationName", value)

    @builtins.property
    @jsii.member(jsii_name="iamRoleArn")
    def iam_role_arn(self) -> builtins.str:
        '''The ARN of the IAM role that defines the permissions for AWS Chatbot .'''
        return typing.cast(builtins.str, jsii.get(self, "iamRoleArn"))

    @iam_role_arn.setter
    def iam_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__987e0ecb599ccda416801ac47ffed7c93c70f9b18e123c0844428e72e3358835)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="teamId")
    def team_id(self) -> builtins.str:
        '''The ID of the Microsoft Team authorized with AWS Chatbot .'''
        return typing.cast(builtins.str, jsii.get(self, "teamId"))

    @team_id.setter
    def team_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__131496f4a9a76e788b24fe2d55a1ad079352bde04c2a3f0bfef8a70ac84c1005)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teamId", value)

    @builtins.property
    @jsii.member(jsii_name="teamsChannelId")
    def teams_channel_id(self) -> builtins.str:
        '''The ID of the Microsoft Teams channel.'''
        return typing.cast(builtins.str, jsii.get(self, "teamsChannelId"))

    @teams_channel_id.setter
    def teams_channel_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6145a2070eac7c951e39d32cc30d829704d9e69208b996decf844ab814b7565)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teamsChannelId", value)

    @builtins.property
    @jsii.member(jsii_name="teamsTenantId")
    def teams_tenant_id(self) -> builtins.str:
        '''The ID of the Microsoft Teams tenant.'''
        return typing.cast(builtins.str, jsii.get(self, "teamsTenantId"))

    @teams_tenant_id.setter
    def teams_tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__150448116265d03ce90265c34fc82985640b935241cdd8bab0f49cc5e0fe172f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "teamsTenantId", value)

    @builtins.property
    @jsii.member(jsii_name="guardrailPolicies")
    def guardrail_policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of IAM policy ARNs that are applied as channel guardrails.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "guardrailPolicies"))

    @guardrail_policies.setter
    def guardrail_policies(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a369a2e8b97e0da168bc82e338319cde3d1784e8fcc291e9f4bf92f07c0bcea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "guardrailPolicies", value)

    @builtins.property
    @jsii.member(jsii_name="loggingLevel")
    def logging_level(self) -> typing.Optional[builtins.str]:
        '''Specifies the logging level for this configuration.

        This property affects the log entries pushed to Amazon CloudWatch Logs.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loggingLevel"))

    @logging_level.setter
    def logging_level(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3e63597aa6fc4d21805a68bc3ce43b4f04ccce5b12da474578d12919e547287)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggingLevel", value)

    @builtins.property
    @jsii.member(jsii_name="snsTopicArns")
    def sns_topic_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARNs of the SNS topics that deliver notifications to AWS Chatbot .'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "snsTopicArns"))

    @sns_topic_arns.setter
    def sns_topic_arns(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d06bfa455d3724be650436a618deed393ddc0dbcd35406db1f888de73d2babe7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snsTopicArns", value)

    @builtins.property
    @jsii.member(jsii_name="userRoleRequired")
    def user_role_required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Enables use of a user role requirement in your chat configuration.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "userRoleRequired"))

    @user_role_required.setter
    def user_role_required(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a5171a48ffb0d6c3dc8bec2e5eb8774e5e34370819690e508928a264f6e7eda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userRoleRequired", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_chatbot.CfnMicrosoftTeamsChannelConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration_name": "configurationName",
        "iam_role_arn": "iamRoleArn",
        "team_id": "teamId",
        "teams_channel_id": "teamsChannelId",
        "teams_tenant_id": "teamsTenantId",
        "guardrail_policies": "guardrailPolicies",
        "logging_level": "loggingLevel",
        "sns_topic_arns": "snsTopicArns",
        "user_role_required": "userRoleRequired",
    },
)
class CfnMicrosoftTeamsChannelConfigurationProps:
    def __init__(
        self,
        *,
        configuration_name: builtins.str,
        iam_role_arn: builtins.str,
        team_id: builtins.str,
        teams_channel_id: builtins.str,
        teams_tenant_id: builtins.str,
        guardrail_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_level: typing.Optional[builtins.str] = None,
        sns_topic_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        user_role_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMicrosoftTeamsChannelConfiguration``.

        :param configuration_name: The name of the configuration.
        :param iam_role_arn: The ARN of the IAM role that defines the permissions for AWS Chatbot . This is a user-defined role that AWS Chatbot will assume. This is not the service-linked role. For more information, see `IAM Policies for AWS Chatbot <https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html>`_ .
        :param team_id: The ID of the Microsoft Team authorized with AWS Chatbot . To get the team ID, you must perform the initial authorization flow with Microsoft Teams in the AWS Chatbot console. Then you can copy and paste the team ID from the console. For more details, see steps 1-4 in `Get started with Microsoft Teams <https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup>`_ in the *AWS Chatbot Administrator Guide* .
        :param teams_channel_id: The ID of the Microsoft Teams channel. To get the channel ID, open Microsoft Teams, right click on the channel name in the left pane, then choose Copy. An example of the channel ID syntax is: ``19%3ab6ef35dc342d56ba5654e6fc6d25a071%40thread.tacv2`` .
        :param teams_tenant_id: The ID of the Microsoft Teams tenant. To get the tenant ID, you must perform the initial authorization flow with Microsoft Teams in the AWS Chatbot console. Then you can copy and paste the tenant ID from the console. For more details, see steps 1-4 in `Get started with Microsoft Teams <https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup>`_ in the *AWS Chatbot Administrator Guide* .
        :param guardrail_policies: The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed 'AdministratorAccess' policy is applied as a default if this is not set.
        :param logging_level: Specifies the logging level for this configuration. This property affects the log entries pushed to Amazon CloudWatch Logs. Logging levels include ``ERROR`` , ``INFO`` , or ``NONE`` . Default: - "NONE"
        :param sns_topic_arns: The ARNs of the SNS topics that deliver notifications to AWS Chatbot .
        :param user_role_required: Enables use of a user role requirement in your chat configuration. Default: - false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-microsoftteamschannelconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_chatbot as chatbot
            
            cfn_microsoft_teams_channel_configuration_props = chatbot.CfnMicrosoftTeamsChannelConfigurationProps(
                configuration_name="configurationName",
                iam_role_arn="iamRoleArn",
                team_id="teamId",
                teams_channel_id="teamsChannelId",
                teams_tenant_id="teamsTenantId",
            
                # the properties below are optional
                guardrail_policies=["guardrailPolicies"],
                logging_level="loggingLevel",
                sns_topic_arns=["snsTopicArns"],
                user_role_required=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2750e06a244ed0f59003e9954924d4cdea272b2fc67dda92574fc40bddddef7d)
            check_type(argname="argument configuration_name", value=configuration_name, expected_type=type_hints["configuration_name"])
            check_type(argname="argument iam_role_arn", value=iam_role_arn, expected_type=type_hints["iam_role_arn"])
            check_type(argname="argument team_id", value=team_id, expected_type=type_hints["team_id"])
            check_type(argname="argument teams_channel_id", value=teams_channel_id, expected_type=type_hints["teams_channel_id"])
            check_type(argname="argument teams_tenant_id", value=teams_tenant_id, expected_type=type_hints["teams_tenant_id"])
            check_type(argname="argument guardrail_policies", value=guardrail_policies, expected_type=type_hints["guardrail_policies"])
            check_type(argname="argument logging_level", value=logging_level, expected_type=type_hints["logging_level"])
            check_type(argname="argument sns_topic_arns", value=sns_topic_arns, expected_type=type_hints["sns_topic_arns"])
            check_type(argname="argument user_role_required", value=user_role_required, expected_type=type_hints["user_role_required"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration_name": configuration_name,
            "iam_role_arn": iam_role_arn,
            "team_id": team_id,
            "teams_channel_id": teams_channel_id,
            "teams_tenant_id": teams_tenant_id,
        }
        if guardrail_policies is not None:
            self._values["guardrail_policies"] = guardrail_policies
        if logging_level is not None:
            self._values["logging_level"] = logging_level
        if sns_topic_arns is not None:
            self._values["sns_topic_arns"] = sns_topic_arns
        if user_role_required is not None:
            self._values["user_role_required"] = user_role_required

    @builtins.property
    def configuration_name(self) -> builtins.str:
        '''The name of the configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-microsoftteamschannelconfiguration.html#cfn-chatbot-microsoftteamschannelconfiguration-configurationname
        '''
        result = self._values.get("configuration_name")
        assert result is not None, "Required property 'configuration_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def iam_role_arn(self) -> builtins.str:
        '''The ARN of the IAM role that defines the permissions for AWS Chatbot .

        This is a user-defined role that AWS Chatbot will assume. This is not the service-linked role. For more information, see `IAM Policies for AWS Chatbot <https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-microsoftteamschannelconfiguration.html#cfn-chatbot-microsoftteamschannelconfiguration-iamrolearn
        '''
        result = self._values.get("iam_role_arn")
        assert result is not None, "Required property 'iam_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def team_id(self) -> builtins.str:
        '''The ID of the Microsoft Team authorized with AWS Chatbot .

        To get the team ID, you must perform the initial authorization flow with Microsoft Teams in the AWS Chatbot console. Then you can copy and paste the team ID from the console. For more details, see steps 1-4 in `Get started with Microsoft Teams <https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup>`_ in the *AWS Chatbot Administrator Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-microsoftteamschannelconfiguration.html#cfn-chatbot-microsoftteamschannelconfiguration-teamid
        '''
        result = self._values.get("team_id")
        assert result is not None, "Required property 'team_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def teams_channel_id(self) -> builtins.str:
        '''The ID of the Microsoft Teams channel.

        To get the channel ID, open Microsoft Teams, right click on the channel name in the left pane, then choose Copy. An example of the channel ID syntax is: ``19%3ab6ef35dc342d56ba5654e6fc6d25a071%40thread.tacv2`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-microsoftteamschannelconfiguration.html#cfn-chatbot-microsoftteamschannelconfiguration-teamschannelid
        '''
        result = self._values.get("teams_channel_id")
        assert result is not None, "Required property 'teams_channel_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def teams_tenant_id(self) -> builtins.str:
        '''The ID of the Microsoft Teams tenant.

        To get the tenant ID, you must perform the initial authorization flow with Microsoft Teams in the AWS Chatbot console. Then you can copy and paste the tenant ID from the console. For more details, see steps 1-4 in `Get started with Microsoft Teams <https://docs.aws.amazon.com/chatbot/latest/adminguide/teams-setup.html#teams-client-setup>`_ in the *AWS Chatbot Administrator Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-microsoftteamschannelconfiguration.html#cfn-chatbot-microsoftteamschannelconfiguration-teamstenantid
        '''
        result = self._values.get("teams_tenant_id")
        assert result is not None, "Required property 'teams_tenant_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def guardrail_policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of IAM policy ARNs that are applied as channel guardrails.

        The AWS managed 'AdministratorAccess' policy is applied as a default if this is not set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-microsoftteamschannelconfiguration.html#cfn-chatbot-microsoftteamschannelconfiguration-guardrailpolicies
        '''
        result = self._values.get("guardrail_policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def logging_level(self) -> typing.Optional[builtins.str]:
        '''Specifies the logging level for this configuration. This property affects the log entries pushed to Amazon CloudWatch Logs.

        Logging levels include ``ERROR`` , ``INFO`` , or ``NONE`` .

        :default: - "NONE"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-microsoftteamschannelconfiguration.html#cfn-chatbot-microsoftteamschannelconfiguration-logginglevel
        '''
        result = self._values.get("logging_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sns_topic_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARNs of the SNS topics that deliver notifications to AWS Chatbot .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-microsoftteamschannelconfiguration.html#cfn-chatbot-microsoftteamschannelconfiguration-snstopicarns
        '''
        result = self._values.get("sns_topic_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def user_role_required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Enables use of a user role requirement in your chat configuration.

        :default: - false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-microsoftteamschannelconfiguration.html#cfn-chatbot-microsoftteamschannelconfiguration-userrolerequired
        '''
        result = self._values.get("user_role_required")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMicrosoftTeamsChannelConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSlackChannelConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_chatbot.CfnSlackChannelConfiguration",
):
    '''The ``AWS::Chatbot::SlackChannelConfiguration`` resource configures a Slack channel to allow users to use AWS Chatbot with AWS CloudFormation templates.

    This resource requires some setup to be done in the AWS Chatbot console. To provide the required Slack workspace ID, you must perform the initial authorization flow with Slack in the AWS Chatbot console, then copy and paste the workspace ID from the console. For more details, see steps 1-4 in `Setting Up AWS Chatbot with Slack <https://docs.aws.amazon.com/chatbot/latest/adminguide/setting-up.html#Setup_intro>`_ in the *AWS Chatbot User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_chatbot as chatbot
        
        cfn_slack_channel_configuration = chatbot.CfnSlackChannelConfiguration(self, "MyCfnSlackChannelConfiguration",
            configuration_name="configurationName",
            iam_role_arn="iamRoleArn",
            slack_channel_id="slackChannelId",
            slack_workspace_id="slackWorkspaceId",
        
            # the properties below are optional
            guardrail_policies=["guardrailPolicies"],
            logging_level="loggingLevel",
            sns_topic_arns=["snsTopicArns"],
            user_role_required=False
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        configuration_name: builtins.str,
        iam_role_arn: builtins.str,
        slack_channel_id: builtins.str,
        slack_workspace_id: builtins.str,
        guardrail_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_level: typing.Optional[builtins.str] = None,
        sns_topic_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        user_role_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param configuration_name: The name of the configuration.
        :param iam_role_arn: The ARN of the IAM role that defines the permissions for AWS Chatbot . This is a user-defined role that AWS Chatbot will assume. This is not the service-linked role. For more information, see `IAM Policies for AWS Chatbot <https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html>`_ .
        :param slack_channel_id: The ID of the Slack channel. To get the ID, open Slack, right click on the channel name in the left pane, then choose Copy Link. The channel ID is the 9-character string at the end of the URL. For example, ``ABCBBLZZZ`` .
        :param slack_workspace_id: The ID of the Slack workspace authorized with AWS Chatbot . To get the workspace ID, you must perform the initial authorization flow with Slack in the AWS Chatbot console. Then you can copy and paste the workspace ID from the console. For more details, see steps 1-4 in `Setting Up AWS Chatbot with Slack <https://docs.aws.amazon.com/chatbot/latest/adminguide/setting-up.html#Setup_intro>`_ in the *AWS Chatbot User Guide* .
        :param guardrail_policies: The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed 'AdministratorAccess' policy is applied as a default if this is not set.
        :param logging_level: Specifies the logging level for this configuration. This property affects the log entries pushed to Amazon CloudWatch Logs. Logging levels include ``ERROR`` , ``INFO`` , or ``NONE`` . Default: - "NONE"
        :param sns_topic_arns: The ARNs of the SNS topics that deliver notifications to AWS Chatbot .
        :param user_role_required: Enables use of a user role requirement in your chat configuration. Default: - false
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cb3844509a8f0685c3dc0d26d5014fa028976d66c5d0a8984e8284bb5449a06)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSlackChannelConfigurationProps(
            configuration_name=configuration_name,
            iam_role_arn=iam_role_arn,
            slack_channel_id=slack_channel_id,
            slack_workspace_id=slack_workspace_id,
            guardrail_policies=guardrail_policies,
            logging_level=logging_level,
            sns_topic_arns=sns_topic_arns,
            user_role_required=user_role_required,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0261296b0c12a109b073fda5c51b89eb246dd5532eca421703d5283b445517a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__38d562d332aafc1a09cf53790aa1b7302247164c326664bab8100a2a6e231851)
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
        '''Amazon Resource Name (ARN) of the configuration.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="configurationName")
    def configuration_name(self) -> builtins.str:
        '''The name of the configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "configurationName"))

    @configuration_name.setter
    def configuration_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__030a2b3ae9dec64c22063a44869eaa3d17e7c59f6584f8f1f0799b11e5230f0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationName", value)

    @builtins.property
    @jsii.member(jsii_name="iamRoleArn")
    def iam_role_arn(self) -> builtins.str:
        '''The ARN of the IAM role that defines the permissions for AWS Chatbot .'''
        return typing.cast(builtins.str, jsii.get(self, "iamRoleArn"))

    @iam_role_arn.setter
    def iam_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0d6b746086db3f0eee87f2bf185747639960cd160b132fc103d742a505cff83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="slackChannelId")
    def slack_channel_id(self) -> builtins.str:
        '''The ID of the Slack channel.'''
        return typing.cast(builtins.str, jsii.get(self, "slackChannelId"))

    @slack_channel_id.setter
    def slack_channel_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__947633a80a86abcda2924b84b36a3f15557a2db21530c5d6bbce145d2de2baa2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slackChannelId", value)

    @builtins.property
    @jsii.member(jsii_name="slackWorkspaceId")
    def slack_workspace_id(self) -> builtins.str:
        '''The ID of the Slack workspace authorized with AWS Chatbot .'''
        return typing.cast(builtins.str, jsii.get(self, "slackWorkspaceId"))

    @slack_workspace_id.setter
    def slack_workspace_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcd6c259891d90515113fab2b366a0fa3fe65279fa991dfb0c55094b82dfe9a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slackWorkspaceId", value)

    @builtins.property
    @jsii.member(jsii_name="guardrailPolicies")
    def guardrail_policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of IAM policy ARNs that are applied as channel guardrails.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "guardrailPolicies"))

    @guardrail_policies.setter
    def guardrail_policies(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__501b5577e7827d442d9391d6001230a41ff67452706a19ec7b9752f0f819226a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "guardrailPolicies", value)

    @builtins.property
    @jsii.member(jsii_name="loggingLevel")
    def logging_level(self) -> typing.Optional[builtins.str]:
        '''Specifies the logging level for this configuration.

        This property affects the log entries pushed to Amazon CloudWatch Logs.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loggingLevel"))

    @logging_level.setter
    def logging_level(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__246f0b4cf1dfb239b8a4368a76b6f46ebb97fa423b3bcb7bd914513d880e580e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggingLevel", value)

    @builtins.property
    @jsii.member(jsii_name="snsTopicArns")
    def sns_topic_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARNs of the SNS topics that deliver notifications to AWS Chatbot .'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "snsTopicArns"))

    @sns_topic_arns.setter
    def sns_topic_arns(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a484a8dbfe21a414edd0bce1d876d84d2ebba782d953f75cc942e74a58c6dc72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snsTopicArns", value)

    @builtins.property
    @jsii.member(jsii_name="userRoleRequired")
    def user_role_required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Enables use of a user role requirement in your chat configuration.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "userRoleRequired"))

    @user_role_required.setter
    def user_role_required(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fdcebb1f70802057ca456714a5cc7c631ffe294962d8635781dfb0f0a08776f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userRoleRequired", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_chatbot.CfnSlackChannelConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration_name": "configurationName",
        "iam_role_arn": "iamRoleArn",
        "slack_channel_id": "slackChannelId",
        "slack_workspace_id": "slackWorkspaceId",
        "guardrail_policies": "guardrailPolicies",
        "logging_level": "loggingLevel",
        "sns_topic_arns": "snsTopicArns",
        "user_role_required": "userRoleRequired",
    },
)
class CfnSlackChannelConfigurationProps:
    def __init__(
        self,
        *,
        configuration_name: builtins.str,
        iam_role_arn: builtins.str,
        slack_channel_id: builtins.str,
        slack_workspace_id: builtins.str,
        guardrail_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_level: typing.Optional[builtins.str] = None,
        sns_topic_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        user_role_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSlackChannelConfiguration``.

        :param configuration_name: The name of the configuration.
        :param iam_role_arn: The ARN of the IAM role that defines the permissions for AWS Chatbot . This is a user-defined role that AWS Chatbot will assume. This is not the service-linked role. For more information, see `IAM Policies for AWS Chatbot <https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html>`_ .
        :param slack_channel_id: The ID of the Slack channel. To get the ID, open Slack, right click on the channel name in the left pane, then choose Copy Link. The channel ID is the 9-character string at the end of the URL. For example, ``ABCBBLZZZ`` .
        :param slack_workspace_id: The ID of the Slack workspace authorized with AWS Chatbot . To get the workspace ID, you must perform the initial authorization flow with Slack in the AWS Chatbot console. Then you can copy and paste the workspace ID from the console. For more details, see steps 1-4 in `Setting Up AWS Chatbot with Slack <https://docs.aws.amazon.com/chatbot/latest/adminguide/setting-up.html#Setup_intro>`_ in the *AWS Chatbot User Guide* .
        :param guardrail_policies: The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed 'AdministratorAccess' policy is applied as a default if this is not set.
        :param logging_level: Specifies the logging level for this configuration. This property affects the log entries pushed to Amazon CloudWatch Logs. Logging levels include ``ERROR`` , ``INFO`` , or ``NONE`` . Default: - "NONE"
        :param sns_topic_arns: The ARNs of the SNS topics that deliver notifications to AWS Chatbot .
        :param user_role_required: Enables use of a user role requirement in your chat configuration. Default: - false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_chatbot as chatbot
            
            cfn_slack_channel_configuration_props = chatbot.CfnSlackChannelConfigurationProps(
                configuration_name="configurationName",
                iam_role_arn="iamRoleArn",
                slack_channel_id="slackChannelId",
                slack_workspace_id="slackWorkspaceId",
            
                # the properties below are optional
                guardrail_policies=["guardrailPolicies"],
                logging_level="loggingLevel",
                sns_topic_arns=["snsTopicArns"],
                user_role_required=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__277f742a3921d9599de6f4a85fd399fb4b6654557393ff7889e5e52f58775566)
            check_type(argname="argument configuration_name", value=configuration_name, expected_type=type_hints["configuration_name"])
            check_type(argname="argument iam_role_arn", value=iam_role_arn, expected_type=type_hints["iam_role_arn"])
            check_type(argname="argument slack_channel_id", value=slack_channel_id, expected_type=type_hints["slack_channel_id"])
            check_type(argname="argument slack_workspace_id", value=slack_workspace_id, expected_type=type_hints["slack_workspace_id"])
            check_type(argname="argument guardrail_policies", value=guardrail_policies, expected_type=type_hints["guardrail_policies"])
            check_type(argname="argument logging_level", value=logging_level, expected_type=type_hints["logging_level"])
            check_type(argname="argument sns_topic_arns", value=sns_topic_arns, expected_type=type_hints["sns_topic_arns"])
            check_type(argname="argument user_role_required", value=user_role_required, expected_type=type_hints["user_role_required"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration_name": configuration_name,
            "iam_role_arn": iam_role_arn,
            "slack_channel_id": slack_channel_id,
            "slack_workspace_id": slack_workspace_id,
        }
        if guardrail_policies is not None:
            self._values["guardrail_policies"] = guardrail_policies
        if logging_level is not None:
            self._values["logging_level"] = logging_level
        if sns_topic_arns is not None:
            self._values["sns_topic_arns"] = sns_topic_arns
        if user_role_required is not None:
            self._values["user_role_required"] = user_role_required

    @builtins.property
    def configuration_name(self) -> builtins.str:
        '''The name of the configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-configurationname
        '''
        result = self._values.get("configuration_name")
        assert result is not None, "Required property 'configuration_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def iam_role_arn(self) -> builtins.str:
        '''The ARN of the IAM role that defines the permissions for AWS Chatbot .

        This is a user-defined role that AWS Chatbot will assume. This is not the service-linked role. For more information, see `IAM Policies for AWS Chatbot <https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-iamrolearn
        '''
        result = self._values.get("iam_role_arn")
        assert result is not None, "Required property 'iam_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def slack_channel_id(self) -> builtins.str:
        '''The ID of the Slack channel.

        To get the ID, open Slack, right click on the channel name in the left pane, then choose Copy Link. The channel ID is the 9-character string at the end of the URL. For example, ``ABCBBLZZZ`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-slackchannelid
        '''
        result = self._values.get("slack_channel_id")
        assert result is not None, "Required property 'slack_channel_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def slack_workspace_id(self) -> builtins.str:
        '''The ID of the Slack workspace authorized with AWS Chatbot .

        To get the workspace ID, you must perform the initial authorization flow with Slack in the AWS Chatbot console. Then you can copy and paste the workspace ID from the console. For more details, see steps 1-4 in `Setting Up AWS Chatbot with Slack <https://docs.aws.amazon.com/chatbot/latest/adminguide/setting-up.html#Setup_intro>`_ in the *AWS Chatbot User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-slackworkspaceid
        '''
        result = self._values.get("slack_workspace_id")
        assert result is not None, "Required property 'slack_workspace_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def guardrail_policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of IAM policy ARNs that are applied as channel guardrails.

        The AWS managed 'AdministratorAccess' policy is applied as a default if this is not set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-guardrailpolicies
        '''
        result = self._values.get("guardrail_policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def logging_level(self) -> typing.Optional[builtins.str]:
        '''Specifies the logging level for this configuration. This property affects the log entries pushed to Amazon CloudWatch Logs.

        Logging levels include ``ERROR`` , ``INFO`` , or ``NONE`` .

        :default: - "NONE"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-logginglevel
        '''
        result = self._values.get("logging_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sns_topic_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARNs of the SNS topics that deliver notifications to AWS Chatbot .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-snstopicarns
        '''
        result = self._values.get("sns_topic_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def user_role_required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Enables use of a user role requirement in your chat configuration.

        :default: - false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-chatbot-slackchannelconfiguration.html#cfn-chatbot-slackchannelconfiguration-userrolerequired
        '''
        result = self._values.get("user_role_required")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSlackChannelConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_chatbot.ISlackChannelConfiguration")
class ISlackChannelConfiguration(
    _IResource_c80c4260,
    _IGrantable_71c4f5de,
    _INotificationRuleTarget_faa3b79b,
    typing_extensions.Protocol,
):
    '''Represents a Slack channel configuration.'''

    @builtins.property
    @jsii.member(jsii_name="slackChannelConfigurationArn")
    def slack_channel_configuration_arn(self) -> builtins.str:
        '''The ARN of the Slack channel configuration In the form of arn:aws:chatbot:{region}:{account}:chat-configuration/slack-channel/{slackChannelName}.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="slackChannelConfigurationName")
    def slack_channel_configuration_name(self) -> builtins.str:
        '''The name of Slack channel configuration.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The permission role of Slack channel configuration.

        :default: - A role will be created.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="addToRolePolicy")
    def add_to_role_policy(self, statement: _PolicyStatement_0fe33853) -> None:
        '''Adds a statement to the IAM role.

        :param statement: -
        '''
        ...

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Return the given named metric for this SlackChannelConfiguration.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        ...


class _ISlackChannelConfigurationProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
    jsii.proxy_for(_IGrantable_71c4f5de), # type: ignore[misc]
    jsii.proxy_for(_INotificationRuleTarget_faa3b79b), # type: ignore[misc]
):
    '''Represents a Slack channel configuration.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_chatbot.ISlackChannelConfiguration"

    @builtins.property
    @jsii.member(jsii_name="slackChannelConfigurationArn")
    def slack_channel_configuration_arn(self) -> builtins.str:
        '''The ARN of the Slack channel configuration In the form of arn:aws:chatbot:{region}:{account}:chat-configuration/slack-channel/{slackChannelName}.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "slackChannelConfigurationArn"))

    @builtins.property
    @jsii.member(jsii_name="slackChannelConfigurationName")
    def slack_channel_configuration_name(self) -> builtins.str:
        '''The name of Slack channel configuration.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "slackChannelConfigurationName"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The permission role of Slack channel configuration.

        :default: - A role will be created.

        :attribute: true
        '''
        return typing.cast(typing.Optional[_IRole_235f5d8e], jsii.get(self, "role"))

    @jsii.member(jsii_name="addToRolePolicy")
    def add_to_role_policy(self, statement: _PolicyStatement_0fe33853) -> None:
        '''Adds a statement to the IAM role.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12a1f59c54292d1a70e58c79d640391fcc658a0d519721123479d12838219471)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(None, jsii.invoke(self, "addToRolePolicy", [statement]))

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Return the given named metric for this SlackChannelConfiguration.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36f008bf41135b7a58422d2b7c9fd93227d05029491e965085b315e66c8b2dc7)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metric", [metric_name, props]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISlackChannelConfiguration).__jsii_proxy_class__ = lambda : _ISlackChannelConfigurationProxy


@jsii.enum(jsii_type="aws-cdk-lib.aws_chatbot.LoggingLevel")
class LoggingLevel(enum.Enum):
    '''Logging levels include ERROR, INFO, or NONE.'''

    ERROR = "ERROR"
    '''ERROR.'''
    INFO = "INFO"
    '''INFO.'''
    NONE = "NONE"
    '''NONE.'''


@jsii.implements(ISlackChannelConfiguration)
class SlackChannelConfiguration(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_chatbot.SlackChannelConfiguration",
):
    '''A new Slack channel configuration.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_chatbot as chatbot
        
        # project: codebuild.Project
        
        
        target = chatbot.SlackChannelConfiguration(self, "MySlackChannel",
            slack_channel_configuration_name="YOUR_CHANNEL_NAME",
            slack_workspace_id="YOUR_SLACK_WORKSPACE_ID",
            slack_channel_id="YOUR_SLACK_CHANNEL_ID"
        )
        
        rule = project.notify_on_build_succeeded("NotifyOnBuildSucceeded", target)
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        slack_channel_configuration_name: builtins.str,
        slack_channel_id: builtins.str,
        slack_workspace_id: builtins.str,
        guardrail_policies: typing.Optional[typing.Sequence[_IManagedPolicy_c3b0dcbf]] = None,
        logging_level: typing.Optional[LoggingLevel] = None,
        log_retention: typing.Optional[_RetentionDays_070f99f0] = None,
        log_retention_retry_options: typing.Optional[typing.Union[_LogRetentionRetryOptions_62d80a14, typing.Dict[builtins.str, typing.Any]]] = None,
        log_retention_role: typing.Optional[_IRole_235f5d8e] = None,
        notification_topics: typing.Optional[typing.Sequence[_ITopic_9eca4852]] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param slack_channel_configuration_name: The name of Slack channel configuration.
        :param slack_channel_id: The ID of the Slack channel. To get the ID, open Slack, right click on the channel name in the left pane, then choose Copy Link. The channel ID is the 9-character string at the end of the URL. For example, ABCBBLZZZ.
        :param slack_workspace_id: The ID of the Slack workspace authorized with AWS Chatbot. To get the workspace ID, you must perform the initial authorization flow with Slack in the AWS Chatbot console. Then you can copy and paste the workspace ID from the console. For more details, see steps 1-4 in Setting Up AWS Chatbot with Slack in the AWS Chatbot User Guide.
        :param guardrail_policies: A list of IAM managed policies that are applied as channel guardrails. Default: - The AWS managed 'AdministratorAccess' policy is applied as a default if this is not set.
        :param logging_level: Specifies the logging level for this configuration. This property affects the log entries pushed to Amazon CloudWatch Logs. Default: LoggingLevel.NONE
        :param log_retention: The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.INFINITE
        :param log_retention_retry_options: When log retention is specified, a custom resource attempts to create the CloudWatch log group. These options control the retry policy when interacting with CloudWatch APIs. Default: - Default AWS SDK retry options.
        :param log_retention_role: The IAM role for the Lambda function associated with the custom resource that sets the retention policy. Default: - A new role is created.
        :param notification_topics: The SNS topics that deliver notifications to AWS Chatbot. Default: None
        :param role: The permission role of Slack channel configuration. Default: - A role will be created.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efdd5da37140f8254b4a44f567a060e15106ce03d4f75880500b5d15d8076be9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SlackChannelConfigurationProps(
            slack_channel_configuration_name=slack_channel_configuration_name,
            slack_channel_id=slack_channel_id,
            slack_workspace_id=slack_workspace_id,
            guardrail_policies=guardrail_policies,
            logging_level=logging_level,
            log_retention=log_retention,
            log_retention_retry_options=log_retention_retry_options,
            log_retention_role=log_retention_role,
            notification_topics=notification_topics,
            role=role,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromSlackChannelConfigurationArn")
    @builtins.classmethod
    def from_slack_channel_configuration_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        slack_channel_configuration_arn: builtins.str,
    ) -> ISlackChannelConfiguration:
        '''Import an existing Slack channel configuration provided an ARN.

        :param scope: The parent creating construct.
        :param id: The construct's name.
        :param slack_channel_configuration_arn: configuration ARN (i.e. arn:aws:chatbot::1234567890:chat-configuration/slack-channel/my-slack).

        :return: a reference to the existing Slack channel configuration
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e75cb1cdfc69c0061e7e14a213dbf05c29e1a935dcb7a67925658a77a7db90c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument slack_channel_configuration_arn", value=slack_channel_configuration_arn, expected_type=type_hints["slack_channel_configuration_arn"])
        return typing.cast(ISlackChannelConfiguration, jsii.sinvoke(cls, "fromSlackChannelConfigurationArn", [scope, id, slack_channel_configuration_arn]))

    @jsii.member(jsii_name="metricAll")
    @builtins.classmethod
    def metric_all(
        cls,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Return the given named metric for All SlackChannelConfigurations.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12b8814a68917d1077846377a05d9a9cfd41105cef24a78340753723cc2a1bba)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.sinvoke(cls, "metricAll", [metric_name, props]))

    @jsii.member(jsii_name="addNotificationTopic")
    def add_notification_topic(self, notification_topic: _ITopic_9eca4852) -> None:
        '''Adds a SNS topic that deliver notifications to AWS Chatbot.

        :param notification_topic: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eea860b468671b227582daf10c3d3148668ac959f57270e1f8344d9557655b61)
            check_type(argname="argument notification_topic", value=notification_topic, expected_type=type_hints["notification_topic"])
        return typing.cast(None, jsii.invoke(self, "addNotificationTopic", [notification_topic]))

    @jsii.member(jsii_name="addToRolePolicy")
    def add_to_role_policy(self, statement: _PolicyStatement_0fe33853) -> None:
        '''Adds extra permission to iam-role of Slack channel configuration.

        :param statement: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49e66b2c4dfeec8a0cf1c5b5553dd1790b6d2225450f587cff9eca3a6512d30a)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
        return typing.cast(None, jsii.invoke(self, "addToRolePolicy", [statement]))

    @jsii.member(jsii_name="bindAsNotificationRuleTarget")
    def bind_as_notification_rule_target(
        self,
        _scope: _constructs_77d1e7e8.Construct,
    ) -> _NotificationRuleTargetConfig_ea27e095:
        '''Returns a target configuration for notification rule.

        :param _scope: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25e09f2c57162b8550c76214659f09aeb2f611c74c290175199f993a4e33afe9)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
        return typing.cast(_NotificationRuleTargetConfig_ea27e095, jsii.invoke(self, "bindAsNotificationRuleTarget", [_scope]))

    @jsii.member(jsii_name="metric")
    def metric(
        self,
        metric_name: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Return the given named metric for this SlackChannelConfiguration.

        :param metric_name: -
        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73a006622b0f5bc2a3fc133c38aeeb0fffe167bf0457064024d2adc8ffe005ff)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metric", [metric_name, props]))

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> _IPrincipal_539bb2fd:
        '''The principal to grant permissions to.'''
        return typing.cast(_IPrincipal_539bb2fd, jsii.get(self, "grantPrincipal"))

    @builtins.property
    @jsii.member(jsii_name="slackChannelConfigurationArn")
    def slack_channel_configuration_arn(self) -> builtins.str:
        '''The ARN of the Slack channel configuration In the form of arn:aws:chatbot:{region}:{account}:chat-configuration/slack-channel/{slackChannelName}.'''
        return typing.cast(builtins.str, jsii.get(self, "slackChannelConfigurationArn"))

    @builtins.property
    @jsii.member(jsii_name="slackChannelConfigurationName")
    def slack_channel_configuration_name(self) -> builtins.str:
        '''The name of Slack channel configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "slackChannelConfigurationName"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The permission role of Slack channel configuration.'''
        return typing.cast(typing.Optional[_IRole_235f5d8e], jsii.get(self, "role"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_chatbot.SlackChannelConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "slack_channel_configuration_name": "slackChannelConfigurationName",
        "slack_channel_id": "slackChannelId",
        "slack_workspace_id": "slackWorkspaceId",
        "guardrail_policies": "guardrailPolicies",
        "logging_level": "loggingLevel",
        "log_retention": "logRetention",
        "log_retention_retry_options": "logRetentionRetryOptions",
        "log_retention_role": "logRetentionRole",
        "notification_topics": "notificationTopics",
        "role": "role",
    },
)
class SlackChannelConfigurationProps:
    def __init__(
        self,
        *,
        slack_channel_configuration_name: builtins.str,
        slack_channel_id: builtins.str,
        slack_workspace_id: builtins.str,
        guardrail_policies: typing.Optional[typing.Sequence[_IManagedPolicy_c3b0dcbf]] = None,
        logging_level: typing.Optional[LoggingLevel] = None,
        log_retention: typing.Optional[_RetentionDays_070f99f0] = None,
        log_retention_retry_options: typing.Optional[typing.Union[_LogRetentionRetryOptions_62d80a14, typing.Dict[builtins.str, typing.Any]]] = None,
        log_retention_role: typing.Optional[_IRole_235f5d8e] = None,
        notification_topics: typing.Optional[typing.Sequence[_ITopic_9eca4852]] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''Properties for a new Slack channel configuration.

        :param slack_channel_configuration_name: The name of Slack channel configuration.
        :param slack_channel_id: The ID of the Slack channel. To get the ID, open Slack, right click on the channel name in the left pane, then choose Copy Link. The channel ID is the 9-character string at the end of the URL. For example, ABCBBLZZZ.
        :param slack_workspace_id: The ID of the Slack workspace authorized with AWS Chatbot. To get the workspace ID, you must perform the initial authorization flow with Slack in the AWS Chatbot console. Then you can copy and paste the workspace ID from the console. For more details, see steps 1-4 in Setting Up AWS Chatbot with Slack in the AWS Chatbot User Guide.
        :param guardrail_policies: A list of IAM managed policies that are applied as channel guardrails. Default: - The AWS managed 'AdministratorAccess' policy is applied as a default if this is not set.
        :param logging_level: Specifies the logging level for this configuration. This property affects the log entries pushed to Amazon CloudWatch Logs. Default: LoggingLevel.NONE
        :param log_retention: The number of days log events are kept in CloudWatch Logs. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE``. Default: logs.RetentionDays.INFINITE
        :param log_retention_retry_options: When log retention is specified, a custom resource attempts to create the CloudWatch log group. These options control the retry policy when interacting with CloudWatch APIs. Default: - Default AWS SDK retry options.
        :param log_retention_role: The IAM role for the Lambda function associated with the custom resource that sets the retention policy. Default: - A new role is created.
        :param notification_topics: The SNS topics that deliver notifications to AWS Chatbot. Default: None
        :param role: The permission role of Slack channel configuration. Default: - A role will be created.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_chatbot as chatbot
            
            # project: codebuild.Project
            
            
            target = chatbot.SlackChannelConfiguration(self, "MySlackChannel",
                slack_channel_configuration_name="YOUR_CHANNEL_NAME",
                slack_workspace_id="YOUR_SLACK_WORKSPACE_ID",
                slack_channel_id="YOUR_SLACK_CHANNEL_ID"
            )
            
            rule = project.notify_on_build_succeeded("NotifyOnBuildSucceeded", target)
        '''
        if isinstance(log_retention_retry_options, dict):
            log_retention_retry_options = _LogRetentionRetryOptions_62d80a14(**log_retention_retry_options)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ac26e048cc95c25fe58a4f6af5e010a7fb045d511f758ebcd363a166cd781fc)
            check_type(argname="argument slack_channel_configuration_name", value=slack_channel_configuration_name, expected_type=type_hints["slack_channel_configuration_name"])
            check_type(argname="argument slack_channel_id", value=slack_channel_id, expected_type=type_hints["slack_channel_id"])
            check_type(argname="argument slack_workspace_id", value=slack_workspace_id, expected_type=type_hints["slack_workspace_id"])
            check_type(argname="argument guardrail_policies", value=guardrail_policies, expected_type=type_hints["guardrail_policies"])
            check_type(argname="argument logging_level", value=logging_level, expected_type=type_hints["logging_level"])
            check_type(argname="argument log_retention", value=log_retention, expected_type=type_hints["log_retention"])
            check_type(argname="argument log_retention_retry_options", value=log_retention_retry_options, expected_type=type_hints["log_retention_retry_options"])
            check_type(argname="argument log_retention_role", value=log_retention_role, expected_type=type_hints["log_retention_role"])
            check_type(argname="argument notification_topics", value=notification_topics, expected_type=type_hints["notification_topics"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "slack_channel_configuration_name": slack_channel_configuration_name,
            "slack_channel_id": slack_channel_id,
            "slack_workspace_id": slack_workspace_id,
        }
        if guardrail_policies is not None:
            self._values["guardrail_policies"] = guardrail_policies
        if logging_level is not None:
            self._values["logging_level"] = logging_level
        if log_retention is not None:
            self._values["log_retention"] = log_retention
        if log_retention_retry_options is not None:
            self._values["log_retention_retry_options"] = log_retention_retry_options
        if log_retention_role is not None:
            self._values["log_retention_role"] = log_retention_role
        if notification_topics is not None:
            self._values["notification_topics"] = notification_topics
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def slack_channel_configuration_name(self) -> builtins.str:
        '''The name of Slack channel configuration.'''
        result = self._values.get("slack_channel_configuration_name")
        assert result is not None, "Required property 'slack_channel_configuration_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def slack_channel_id(self) -> builtins.str:
        '''The ID of the Slack channel.

        To get the ID, open Slack, right click on the channel name in the left pane, then choose Copy Link.
        The channel ID is the 9-character string at the end of the URL. For example, ABCBBLZZZ.
        '''
        result = self._values.get("slack_channel_id")
        assert result is not None, "Required property 'slack_channel_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def slack_workspace_id(self) -> builtins.str:
        '''The ID of the Slack workspace authorized with AWS Chatbot.

        To get the workspace ID, you must perform the initial authorization flow with Slack in the AWS Chatbot console.
        Then you can copy and paste the workspace ID from the console.
        For more details, see steps 1-4 in Setting Up AWS Chatbot with Slack in the AWS Chatbot User Guide.

        :see: https://docs.aws.amazon.com/chatbot/latest/adminguide/setting-up.html#Setup_intro
        '''
        result = self._values.get("slack_workspace_id")
        assert result is not None, "Required property 'slack_workspace_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def guardrail_policies(
        self,
    ) -> typing.Optional[typing.List[_IManagedPolicy_c3b0dcbf]]:
        '''A list of IAM managed policies that are applied as channel guardrails.

        :default: - The AWS managed 'AdministratorAccess' policy is applied as a default if this is not set.
        '''
        result = self._values.get("guardrail_policies")
        return typing.cast(typing.Optional[typing.List[_IManagedPolicy_c3b0dcbf]], result)

    @builtins.property
    def logging_level(self) -> typing.Optional[LoggingLevel]:
        '''Specifies the logging level for this configuration.

        This property affects the log entries pushed to Amazon CloudWatch Logs.

        :default: LoggingLevel.NONE
        '''
        result = self._values.get("logging_level")
        return typing.cast(typing.Optional[LoggingLevel], result)

    @builtins.property
    def log_retention(self) -> typing.Optional[_RetentionDays_070f99f0]:
        '''The number of days log events are kept in CloudWatch Logs.

        When updating
        this property, unsetting it doesn't remove the log retention policy. To
        remove the retention policy, set the value to ``INFINITE``.

        :default: logs.RetentionDays.INFINITE
        '''
        result = self._values.get("log_retention")
        return typing.cast(typing.Optional[_RetentionDays_070f99f0], result)

    @builtins.property
    def log_retention_retry_options(
        self,
    ) -> typing.Optional[_LogRetentionRetryOptions_62d80a14]:
        '''When log retention is specified, a custom resource attempts to create the CloudWatch log group.

        These options control the retry policy when interacting with CloudWatch APIs.

        :default: - Default AWS SDK retry options.
        '''
        result = self._values.get("log_retention_retry_options")
        return typing.cast(typing.Optional[_LogRetentionRetryOptions_62d80a14], result)

    @builtins.property
    def log_retention_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The IAM role for the Lambda function associated with the custom resource that sets the retention policy.

        :default: - A new role is created.
        '''
        result = self._values.get("log_retention_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def notification_topics(self) -> typing.Optional[typing.List[_ITopic_9eca4852]]:
        '''The SNS topics that deliver notifications to AWS Chatbot.

        :default: None
        '''
        result = self._values.get("notification_topics")
        return typing.cast(typing.Optional[typing.List[_ITopic_9eca4852]], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The permission role of Slack channel configuration.

        :default: - A role will be created.
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SlackChannelConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnMicrosoftTeamsChannelConfiguration",
    "CfnMicrosoftTeamsChannelConfigurationProps",
    "CfnSlackChannelConfiguration",
    "CfnSlackChannelConfigurationProps",
    "ISlackChannelConfiguration",
    "LoggingLevel",
    "SlackChannelConfiguration",
    "SlackChannelConfigurationProps",
]

publication.publish()

def _typecheckingstub__62f6b943071fca79376376fd20660d7b707a1026a9039a0c12c88895d7f39b05(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configuration_name: builtins.str,
    iam_role_arn: builtins.str,
    team_id: builtins.str,
    teams_channel_id: builtins.str,
    teams_tenant_id: builtins.str,
    guardrail_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    logging_level: typing.Optional[builtins.str] = None,
    sns_topic_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    user_role_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46600197e082ba9fc6d055c23e70f7f73de26074b20358edbb7348ae3fb1f908(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89615163f4db8d0acf5a1e87300a200fc030e21f6faf513d0af1e4093b25e33d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__853492827ec4d32419905b108885cd7dfb3bfcc97356414d7093f3ffde1cc102(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__987e0ecb599ccda416801ac47ffed7c93c70f9b18e123c0844428e72e3358835(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__131496f4a9a76e788b24fe2d55a1ad079352bde04c2a3f0bfef8a70ac84c1005(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6145a2070eac7c951e39d32cc30d829704d9e69208b996decf844ab814b7565(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__150448116265d03ce90265c34fc82985640b935241cdd8bab0f49cc5e0fe172f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a369a2e8b97e0da168bc82e338319cde3d1784e8fcc291e9f4bf92f07c0bcea(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3e63597aa6fc4d21805a68bc3ce43b4f04ccce5b12da474578d12919e547287(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d06bfa455d3724be650436a618deed393ddc0dbcd35406db1f888de73d2babe7(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a5171a48ffb0d6c3dc8bec2e5eb8774e5e34370819690e508928a264f6e7eda(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2750e06a244ed0f59003e9954924d4cdea272b2fc67dda92574fc40bddddef7d(
    *,
    configuration_name: builtins.str,
    iam_role_arn: builtins.str,
    team_id: builtins.str,
    teams_channel_id: builtins.str,
    teams_tenant_id: builtins.str,
    guardrail_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    logging_level: typing.Optional[builtins.str] = None,
    sns_topic_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    user_role_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cb3844509a8f0685c3dc0d26d5014fa028976d66c5d0a8984e8284bb5449a06(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configuration_name: builtins.str,
    iam_role_arn: builtins.str,
    slack_channel_id: builtins.str,
    slack_workspace_id: builtins.str,
    guardrail_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    logging_level: typing.Optional[builtins.str] = None,
    sns_topic_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    user_role_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0261296b0c12a109b073fda5c51b89eb246dd5532eca421703d5283b445517a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38d562d332aafc1a09cf53790aa1b7302247164c326664bab8100a2a6e231851(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__030a2b3ae9dec64c22063a44869eaa3d17e7c59f6584f8f1f0799b11e5230f0b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0d6b746086db3f0eee87f2bf185747639960cd160b132fc103d742a505cff83(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__947633a80a86abcda2924b84b36a3f15557a2db21530c5d6bbce145d2de2baa2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcd6c259891d90515113fab2b366a0fa3fe65279fa991dfb0c55094b82dfe9a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__501b5577e7827d442d9391d6001230a41ff67452706a19ec7b9752f0f819226a(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__246f0b4cf1dfb239b8a4368a76b6f46ebb97fa423b3bcb7bd914513d880e580e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a484a8dbfe21a414edd0bce1d876d84d2ebba782d953f75cc942e74a58c6dc72(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fdcebb1f70802057ca456714a5cc7c631ffe294962d8635781dfb0f0a08776f(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__277f742a3921d9599de6f4a85fd399fb4b6654557393ff7889e5e52f58775566(
    *,
    configuration_name: builtins.str,
    iam_role_arn: builtins.str,
    slack_channel_id: builtins.str,
    slack_workspace_id: builtins.str,
    guardrail_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    logging_level: typing.Optional[builtins.str] = None,
    sns_topic_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    user_role_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12a1f59c54292d1a70e58c79d640391fcc658a0d519721123479d12838219471(
    statement: _PolicyStatement_0fe33853,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36f008bf41135b7a58422d2b7c9fd93227d05029491e965085b315e66c8b2dc7(
    metric_name: builtins.str,
    *,
    account: typing.Optional[builtins.str] = None,
    color: typing.Optional[builtins.str] = None,
    dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    label: typing.Optional[builtins.str] = None,
    period: typing.Optional[_Duration_4839e8c3] = None,
    region: typing.Optional[builtins.str] = None,
    statistic: typing.Optional[builtins.str] = None,
    unit: typing.Optional[_Unit_61bc6f70] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efdd5da37140f8254b4a44f567a060e15106ce03d4f75880500b5d15d8076be9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    slack_channel_configuration_name: builtins.str,
    slack_channel_id: builtins.str,
    slack_workspace_id: builtins.str,
    guardrail_policies: typing.Optional[typing.Sequence[_IManagedPolicy_c3b0dcbf]] = None,
    logging_level: typing.Optional[LoggingLevel] = None,
    log_retention: typing.Optional[_RetentionDays_070f99f0] = None,
    log_retention_retry_options: typing.Optional[typing.Union[_LogRetentionRetryOptions_62d80a14, typing.Dict[builtins.str, typing.Any]]] = None,
    log_retention_role: typing.Optional[_IRole_235f5d8e] = None,
    notification_topics: typing.Optional[typing.Sequence[_ITopic_9eca4852]] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e75cb1cdfc69c0061e7e14a213dbf05c29e1a935dcb7a67925658a77a7db90c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    slack_channel_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12b8814a68917d1077846377a05d9a9cfd41105cef24a78340753723cc2a1bba(
    metric_name: builtins.str,
    *,
    account: typing.Optional[builtins.str] = None,
    color: typing.Optional[builtins.str] = None,
    dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    label: typing.Optional[builtins.str] = None,
    period: typing.Optional[_Duration_4839e8c3] = None,
    region: typing.Optional[builtins.str] = None,
    statistic: typing.Optional[builtins.str] = None,
    unit: typing.Optional[_Unit_61bc6f70] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eea860b468671b227582daf10c3d3148668ac959f57270e1f8344d9557655b61(
    notification_topic: _ITopic_9eca4852,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49e66b2c4dfeec8a0cf1c5b5553dd1790b6d2225450f587cff9eca3a6512d30a(
    statement: _PolicyStatement_0fe33853,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25e09f2c57162b8550c76214659f09aeb2f611c74c290175199f993a4e33afe9(
    _scope: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73a006622b0f5bc2a3fc133c38aeeb0fffe167bf0457064024d2adc8ffe005ff(
    metric_name: builtins.str,
    *,
    account: typing.Optional[builtins.str] = None,
    color: typing.Optional[builtins.str] = None,
    dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    label: typing.Optional[builtins.str] = None,
    period: typing.Optional[_Duration_4839e8c3] = None,
    region: typing.Optional[builtins.str] = None,
    statistic: typing.Optional[builtins.str] = None,
    unit: typing.Optional[_Unit_61bc6f70] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ac26e048cc95c25fe58a4f6af5e010a7fb045d511f758ebcd363a166cd781fc(
    *,
    slack_channel_configuration_name: builtins.str,
    slack_channel_id: builtins.str,
    slack_workspace_id: builtins.str,
    guardrail_policies: typing.Optional[typing.Sequence[_IManagedPolicy_c3b0dcbf]] = None,
    logging_level: typing.Optional[LoggingLevel] = None,
    log_retention: typing.Optional[_RetentionDays_070f99f0] = None,
    log_retention_retry_options: typing.Optional[typing.Union[_LogRetentionRetryOptions_62d80a14, typing.Dict[builtins.str, typing.Any]]] = None,
    log_retention_role: typing.Optional[_IRole_235f5d8e] = None,
    notification_topics: typing.Optional[typing.Sequence[_ITopic_9eca4852]] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass
