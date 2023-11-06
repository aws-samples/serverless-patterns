'''
# Amazon Simple Email Service Actions Library

This module contains integration classes to add action to SES email receiving rules.
Instances of these classes should be passed to the `rule.addAction()` method.

Currently supported are:

* [Add header](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-action-add-header.html)
* [Bounce](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-action-bounce.html)
* [Lambda](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-action-lambda.html)
* [S3](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-action-s3.html)
* [SNS](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-action-sns.html)
* [Stop](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-action-stop.html)

See the README of `aws-cdk-lib/aws-ses` for more information.
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

from ..aws_kms import IKey as _IKey_5f11635f
from ..aws_lambda import IFunction as _IFunction_6adb0ab8
from ..aws_s3 import IBucket as _IBucket_42e086fd
from ..aws_ses import (
    IReceiptRule as _IReceiptRule_20f5161a,
    IReceiptRuleAction as _IReceiptRuleAction_941d7a8d,
    ReceiptRuleActionConfig as _ReceiptRuleActionConfig_6feb97ed,
)
from ..aws_sns import ITopic as _ITopic_9eca4852


@jsii.implements(_IReceiptRuleAction_941d7a8d)
class AddHeader(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses_actions.AddHeader",
):
    '''Adds a header to the received email.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_s3 as s3
        import aws_cdk.aws_ses_actions as actions
        
        
        bucket = s3.Bucket(self, "Bucket")
        topic = sns.Topic(self, "Topic")
        
        ses.ReceiptRuleSet(self, "RuleSet",
            rules=[ses.ReceiptRuleOptions(
                recipients=["hello@aws.com"],
                actions=[
                    actions.AddHeader(
                        name="X-Special-Header",
                        value="aws"
                    ),
                    actions.S3(
                        bucket=bucket,
                        object_key_prefix="emails/",
                        topic=topic
                    )
                ]
            ), ses.ReceiptRuleOptions(
                recipients=["aws.com"],
                actions=[
                    actions.Sns(
                        topic=topic
                    )
                ]
            )
            ]
        )
    '''

    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''
        :param name: The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.
        :param value: The value of the header to add. Must be less than 2048 characters, and must not contain newline characters ("\\r" or "\\n").
        '''
        props = AddHeaderProps(name=name, value=value)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bind")
    def bind(self, _rule: _IReceiptRule_20f5161a) -> _ReceiptRuleActionConfig_6feb97ed:
        '''Returns the receipt rule action specification.

        :param _rule: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__105fc3c3cd165ab670ed7315f6f8772759f997da89c1f47dcd5abcdd5b8a67d4)
            check_type(argname="argument _rule", value=_rule, expected_type=type_hints["_rule"])
        return typing.cast(_ReceiptRuleActionConfig_6feb97ed, jsii.invoke(self, "bind", [_rule]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses_actions.AddHeaderProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class AddHeaderProps:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''Construction properties for a add header action.

        :param name: The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.
        :param value: The value of the header to add. Must be less than 2048 characters, and must not contain newline characters ("\\r" or "\\n").

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_s3 as s3
            import aws_cdk.aws_ses_actions as actions
            
            
            bucket = s3.Bucket(self, "Bucket")
            topic = sns.Topic(self, "Topic")
            
            ses.ReceiptRuleSet(self, "RuleSet",
                rules=[ses.ReceiptRuleOptions(
                    recipients=["hello@aws.com"],
                    actions=[
                        actions.AddHeader(
                            name="X-Special-Header",
                            value="aws"
                        ),
                        actions.S3(
                            bucket=bucket,
                            object_key_prefix="emails/",
                            topic=topic
                        )
                    ]
                ), ses.ReceiptRuleOptions(
                    recipients=["aws.com"],
                    actions=[
                        actions.Sns(
                            topic=topic
                        )
                    ]
                )
                ]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8074b8d36e00e09d13e403cb0144597d401c4b4212de69cf794e357f2044bbc6)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the header to add.

        Must be between 1 and 50 characters,
        inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters
        and dashes only.
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The value of the header to add.

        Must be less than 2048 characters,
        and must not contain newline characters ("\\r" or "\\n").
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AddHeaderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IReceiptRuleAction_941d7a8d)
class Bounce(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.aws_ses_actions.Bounce"):
    '''Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon SNS.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ses_actions as ses_actions
        from aws_cdk import aws_sns as sns
        
        # bounce_template: ses_actions.BounceTemplate
        # topic: sns.Topic
        
        bounce = ses_actions.Bounce(
            sender="sender",
            template=bounce_template,
        
            # the properties below are optional
            topic=topic
        )
    '''

    def __init__(
        self,
        *,
        sender: builtins.str,
        template: "BounceTemplate",
        topic: typing.Optional[_ITopic_9eca4852] = None,
    ) -> None:
        '''
        :param sender: The email address of the sender of the bounced email. This is the address from which the bounce message will be sent.
        :param template: The template containing the message, reply code and status code.
        :param topic: The SNS topic to notify when the bounce action is taken. Default: no notification
        '''
        props = BounceProps(sender=sender, template=template, topic=topic)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bind")
    def bind(self, _rule: _IReceiptRule_20f5161a) -> _ReceiptRuleActionConfig_6feb97ed:
        '''Returns the receipt rule action specification.

        :param _rule: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2f996c58d36c8115f8cab70b8032eaa964550fcbc5df1791bde6faa8deaf815)
            check_type(argname="argument _rule", value=_rule, expected_type=type_hints["_rule"])
        return typing.cast(_ReceiptRuleActionConfig_6feb97ed, jsii.invoke(self, "bind", [_rule]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses_actions.BounceProps",
    jsii_struct_bases=[],
    name_mapping={"sender": "sender", "template": "template", "topic": "topic"},
)
class BounceProps:
    def __init__(
        self,
        *,
        sender: builtins.str,
        template: "BounceTemplate",
        topic: typing.Optional[_ITopic_9eca4852] = None,
    ) -> None:
        '''Construction properties for a bounce action.

        :param sender: The email address of the sender of the bounced email. This is the address from which the bounce message will be sent.
        :param template: The template containing the message, reply code and status code.
        :param topic: The SNS topic to notify when the bounce action is taken. Default: no notification

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses_actions as ses_actions
            from aws_cdk import aws_sns as sns
            
            # bounce_template: ses_actions.BounceTemplate
            # topic: sns.Topic
            
            bounce_props = ses_actions.BounceProps(
                sender="sender",
                template=bounce_template,
            
                # the properties below are optional
                topic=topic
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10becc64374e762d000b185a3f737684b96a3b21fb43c820f58bbcad29f8dfef)
            check_type(argname="argument sender", value=sender, expected_type=type_hints["sender"])
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "sender": sender,
            "template": template,
        }
        if topic is not None:
            self._values["topic"] = topic

    @builtins.property
    def sender(self) -> builtins.str:
        '''The email address of the sender of the bounced email.

        This is the address
        from which the bounce message will be sent.
        '''
        result = self._values.get("sender")
        assert result is not None, "Required property 'sender' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template(self) -> "BounceTemplate":
        '''The template containing the message, reply code and status code.'''
        result = self._values.get("template")
        assert result is not None, "Required property 'template' is missing"
        return typing.cast("BounceTemplate", result)

    @builtins.property
    def topic(self) -> typing.Optional[_ITopic_9eca4852]:
        '''The SNS topic to notify when the bounce action is taken.

        :default: no notification
        '''
        result = self._values.get("topic")
        return typing.cast(typing.Optional[_ITopic_9eca4852], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BounceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BounceTemplate(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses_actions.BounceTemplate",
):
    '''A bounce template.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ses_actions as ses_actions
        
        bounce_template = ses_actions.BounceTemplate.MAILBOX_DOES_NOT_EXIST
    '''

    def __init__(
        self,
        *,
        message: builtins.str,
        smtp_reply_code: builtins.str,
        status_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: Human-readable text to include in the bounce message.
        :param smtp_reply_code: The SMTP reply code, as defined by RFC 5321.
        :param status_code: The SMTP enhanced status code, as defined by RFC 3463.
        '''
        props = BounceTemplateProps(
            message=message, smtp_reply_code=smtp_reply_code, status_code=status_code
        )

        jsii.create(self.__class__, self, [props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="MAILBOX_DOES_NOT_EXIST")
    def MAILBOX_DOES_NOT_EXIST(cls) -> "BounceTemplate":
        return typing.cast("BounceTemplate", jsii.sget(cls, "MAILBOX_DOES_NOT_EXIST"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="MAILBOX_FULL")
    def MAILBOX_FULL(cls) -> "BounceTemplate":
        return typing.cast("BounceTemplate", jsii.sget(cls, "MAILBOX_FULL"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="MESSAGE_CONTENT_REJECTED")
    def MESSAGE_CONTENT_REJECTED(cls) -> "BounceTemplate":
        return typing.cast("BounceTemplate", jsii.sget(cls, "MESSAGE_CONTENT_REJECTED"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="MESSAGE_TOO_LARGE")
    def MESSAGE_TOO_LARGE(cls) -> "BounceTemplate":
        return typing.cast("BounceTemplate", jsii.sget(cls, "MESSAGE_TOO_LARGE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="TEMPORARY_FAILURE")
    def TEMPORARY_FAILURE(cls) -> "BounceTemplate":
        return typing.cast("BounceTemplate", jsii.sget(cls, "TEMPORARY_FAILURE"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "BounceTemplateProps":
        return typing.cast("BounceTemplateProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses_actions.BounceTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "message": "message",
        "smtp_reply_code": "smtpReplyCode",
        "status_code": "statusCode",
    },
)
class BounceTemplateProps:
    def __init__(
        self,
        *,
        message: builtins.str,
        smtp_reply_code: builtins.str,
        status_code: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Construction properties for a BounceTemplate.

        :param message: Human-readable text to include in the bounce message.
        :param smtp_reply_code: The SMTP reply code, as defined by RFC 5321.
        :param status_code: The SMTP enhanced status code, as defined by RFC 3463.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses_actions as ses_actions
            
            bounce_template_props = ses_actions.BounceTemplateProps(
                message="message",
                smtp_reply_code="smtpReplyCode",
            
                # the properties below are optional
                status_code="statusCode"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14a3bcf1f5997a06acbd35725068d819e7cc13cc462249861c26d1b6c72cfd29)
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument smtp_reply_code", value=smtp_reply_code, expected_type=type_hints["smtp_reply_code"])
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "message": message,
            "smtp_reply_code": smtp_reply_code,
        }
        if status_code is not None:
            self._values["status_code"] = status_code

    @builtins.property
    def message(self) -> builtins.str:
        '''Human-readable text to include in the bounce message.'''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def smtp_reply_code(self) -> builtins.str:
        '''The SMTP reply code, as defined by RFC 5321.

        :see: https://tools.ietf.org/html/rfc5321
        '''
        result = self._values.get("smtp_reply_code")
        assert result is not None, "Required property 'smtp_reply_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status_code(self) -> typing.Optional[builtins.str]:
        '''The SMTP enhanced status code, as defined by RFC 3463.

        :see: https://tools.ietf.org/html/rfc3463
        '''
        result = self._values.get("status_code")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BounceTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_ses_actions.EmailEncoding")
class EmailEncoding(enum.Enum):
    '''The type of email encoding to use for a SNS action.'''

    BASE64 = "BASE64"
    '''Base 64.'''
    UTF8 = "UTF8"
    '''UTF-8.'''


@jsii.implements(_IReceiptRuleAction_941d7a8d)
class Lambda(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.aws_ses_actions.Lambda"):
    '''Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lambda as lambda_
        from aws_cdk import aws_ses_actions as ses_actions
        from aws_cdk import aws_sns as sns
        
        # function_: lambda.Function
        # topic: sns.Topic
        
        lambda_ = ses_actions.Lambda(
            function=function_,
        
            # the properties below are optional
            invocation_type=ses_actions.LambdaInvocationType.EVENT,
            topic=topic
        )
    '''

    def __init__(
        self,
        *,
        function: _IFunction_6adb0ab8,
        invocation_type: typing.Optional["LambdaInvocationType"] = None,
        topic: typing.Optional[_ITopic_9eca4852] = None,
    ) -> None:
        '''
        :param function: The Lambda function to invoke.
        :param invocation_type: The invocation type of the Lambda function. Default: Event
        :param topic: The SNS topic to notify when the Lambda action is taken. Default: no notification
        '''
        props = LambdaProps(
            function=function, invocation_type=invocation_type, topic=topic
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bind")
    def bind(self, rule: _IReceiptRule_20f5161a) -> _ReceiptRuleActionConfig_6feb97ed:
        '''Returns the receipt rule action specification.

        :param rule: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d93726e71fd780c819e83cd0e14b221830680dac424ed3f6cfaf667ae223bd1)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
        return typing.cast(_ReceiptRuleActionConfig_6feb97ed, jsii.invoke(self, "bind", [rule]))


@jsii.enum(jsii_type="aws-cdk-lib.aws_ses_actions.LambdaInvocationType")
class LambdaInvocationType(enum.Enum):
    '''The type of invocation to use for a Lambda Action.'''

    EVENT = "EVENT"
    '''The function will be invoked asynchronously.'''
    REQUEST_RESPONSE = "REQUEST_RESPONSE"
    '''The function will be invoked sychronously.

    Use RequestResponse only when
    you want to make a mail flow decision, such as whether to stop the receipt
    rule or the receipt rule set.
    '''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses_actions.LambdaProps",
    jsii_struct_bases=[],
    name_mapping={
        "function": "function",
        "invocation_type": "invocationType",
        "topic": "topic",
    },
)
class LambdaProps:
    def __init__(
        self,
        *,
        function: _IFunction_6adb0ab8,
        invocation_type: typing.Optional[LambdaInvocationType] = None,
        topic: typing.Optional[_ITopic_9eca4852] = None,
    ) -> None:
        '''Construction properties for a Lambda action.

        :param function: The Lambda function to invoke.
        :param invocation_type: The invocation type of the Lambda function. Default: Event
        :param topic: The SNS topic to notify when the Lambda action is taken. Default: no notification

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lambda as lambda_
            from aws_cdk import aws_ses_actions as ses_actions
            from aws_cdk import aws_sns as sns
            
            # function_: lambda.Function
            # topic: sns.Topic
            
            lambda_props = ses_actions.LambdaProps(
                function=function_,
            
                # the properties below are optional
                invocation_type=ses_actions.LambdaInvocationType.EVENT,
                topic=topic
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b90a6708b72eec383955e1dee897c153062b0d56e272e25d405eb8bb889276f7)
            check_type(argname="argument function", value=function, expected_type=type_hints["function"])
            check_type(argname="argument invocation_type", value=invocation_type, expected_type=type_hints["invocation_type"])
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "function": function,
        }
        if invocation_type is not None:
            self._values["invocation_type"] = invocation_type
        if topic is not None:
            self._values["topic"] = topic

    @builtins.property
    def function(self) -> _IFunction_6adb0ab8:
        '''The Lambda function to invoke.'''
        result = self._values.get("function")
        assert result is not None, "Required property 'function' is missing"
        return typing.cast(_IFunction_6adb0ab8, result)

    @builtins.property
    def invocation_type(self) -> typing.Optional[LambdaInvocationType]:
        '''The invocation type of the Lambda function.

        :default: Event
        '''
        result = self._values.get("invocation_type")
        return typing.cast(typing.Optional[LambdaInvocationType], result)

    @builtins.property
    def topic(self) -> typing.Optional[_ITopic_9eca4852]:
        '''The SNS topic to notify when the Lambda action is taken.

        :default: no notification
        '''
        result = self._values.get("topic")
        return typing.cast(typing.Optional[_ITopic_9eca4852], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IReceiptRuleAction_941d7a8d)
class S3(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.aws_ses_actions.S3"):
    '''Saves the received message to an Amazon S3 bucket and, optionally, publishes a notification to Amazon SNS.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_s3 as s3
        import aws_cdk.aws_ses_actions as actions
        
        
        bucket = s3.Bucket(self, "Bucket")
        topic = sns.Topic(self, "Topic")
        
        ses.ReceiptRuleSet(self, "RuleSet",
            rules=[ses.ReceiptRuleOptions(
                recipients=["hello@aws.com"],
                actions=[
                    actions.AddHeader(
                        name="X-Special-Header",
                        value="aws"
                    ),
                    actions.S3(
                        bucket=bucket,
                        object_key_prefix="emails/",
                        topic=topic
                    )
                ]
            ), ses.ReceiptRuleOptions(
                recipients=["aws.com"],
                actions=[
                    actions.Sns(
                        topic=topic
                    )
                ]
            )
            ]
        )
    '''

    def __init__(
        self,
        *,
        bucket: _IBucket_42e086fd,
        kms_key: typing.Optional[_IKey_5f11635f] = None,
        object_key_prefix: typing.Optional[builtins.str] = None,
        topic: typing.Optional[_ITopic_9eca4852] = None,
    ) -> None:
        '''
        :param bucket: The S3 bucket that incoming email will be saved to.
        :param kms_key: The master key that SES should use to encrypt your emails before saving them to the S3 bucket. Default: no encryption
        :param object_key_prefix: The key prefix of the S3 bucket. Default: no prefix
        :param topic: The SNS topic to notify when the S3 action is taken. Default: no notification
        '''
        props = S3Props(
            bucket=bucket,
            kms_key=kms_key,
            object_key_prefix=object_key_prefix,
            topic=topic,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bind")
    def bind(self, rule: _IReceiptRule_20f5161a) -> _ReceiptRuleActionConfig_6feb97ed:
        '''Returns the receipt rule action specification.

        :param rule: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f2e6c8d98ea2e24878b8790662d46dbd681afc3be87064c425c1be30d91c1a4)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
        return typing.cast(_ReceiptRuleActionConfig_6feb97ed, jsii.invoke(self, "bind", [rule]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses_actions.S3Props",
    jsii_struct_bases=[],
    name_mapping={
        "bucket": "bucket",
        "kms_key": "kmsKey",
        "object_key_prefix": "objectKeyPrefix",
        "topic": "topic",
    },
)
class S3Props:
    def __init__(
        self,
        *,
        bucket: _IBucket_42e086fd,
        kms_key: typing.Optional[_IKey_5f11635f] = None,
        object_key_prefix: typing.Optional[builtins.str] = None,
        topic: typing.Optional[_ITopic_9eca4852] = None,
    ) -> None:
        '''Construction properties for a S3 action.

        :param bucket: The S3 bucket that incoming email will be saved to.
        :param kms_key: The master key that SES should use to encrypt your emails before saving them to the S3 bucket. Default: no encryption
        :param object_key_prefix: The key prefix of the S3 bucket. Default: no prefix
        :param topic: The SNS topic to notify when the S3 action is taken. Default: no notification

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_s3 as s3
            import aws_cdk.aws_ses_actions as actions
            
            
            bucket = s3.Bucket(self, "Bucket")
            topic = sns.Topic(self, "Topic")
            
            ses.ReceiptRuleSet(self, "RuleSet",
                rules=[ses.ReceiptRuleOptions(
                    recipients=["hello@aws.com"],
                    actions=[
                        actions.AddHeader(
                            name="X-Special-Header",
                            value="aws"
                        ),
                        actions.S3(
                            bucket=bucket,
                            object_key_prefix="emails/",
                            topic=topic
                        )
                    ]
                ), ses.ReceiptRuleOptions(
                    recipients=["aws.com"],
                    actions=[
                        actions.Sns(
                            topic=topic
                        )
                    ]
                )
                ]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c3ffb5d7305f7f8cdd0eda6dbf1af4894ccfe04c1d809df6e1bc2c3d2678903)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument object_key_prefix", value=object_key_prefix, expected_type=type_hints["object_key_prefix"])
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
        }
        if kms_key is not None:
            self._values["kms_key"] = kms_key
        if object_key_prefix is not None:
            self._values["object_key_prefix"] = object_key_prefix
        if topic is not None:
            self._values["topic"] = topic

    @builtins.property
    def bucket(self) -> _IBucket_42e086fd:
        '''The S3 bucket that incoming email will be saved to.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(_IBucket_42e086fd, result)

    @builtins.property
    def kms_key(self) -> typing.Optional[_IKey_5f11635f]:
        '''The master key that SES should use to encrypt your emails before saving them to the S3 bucket.

        :default: no encryption
        '''
        result = self._values.get("kms_key")
        return typing.cast(typing.Optional[_IKey_5f11635f], result)

    @builtins.property
    def object_key_prefix(self) -> typing.Optional[builtins.str]:
        '''The key prefix of the S3 bucket.

        :default: no prefix
        '''
        result = self._values.get("object_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def topic(self) -> typing.Optional[_ITopic_9eca4852]:
        '''The SNS topic to notify when the S3 action is taken.

        :default: no notification
        '''
        result = self._values.get("topic")
        return typing.cast(typing.Optional[_ITopic_9eca4852], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IReceiptRuleAction_941d7a8d)
class Sns(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.aws_ses_actions.Sns"):
    '''Publishes the email content within a notification to Amazon SNS.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_s3 as s3
        import aws_cdk.aws_ses_actions as actions
        
        
        bucket = s3.Bucket(self, "Bucket")
        topic = sns.Topic(self, "Topic")
        
        ses.ReceiptRuleSet(self, "RuleSet",
            rules=[ses.ReceiptRuleOptions(
                recipients=["hello@aws.com"],
                actions=[
                    actions.AddHeader(
                        name="X-Special-Header",
                        value="aws"
                    ),
                    actions.S3(
                        bucket=bucket,
                        object_key_prefix="emails/",
                        topic=topic
                    )
                ]
            ), ses.ReceiptRuleOptions(
                recipients=["aws.com"],
                actions=[
                    actions.Sns(
                        topic=topic
                    )
                ]
            )
            ]
        )
    '''

    def __init__(
        self,
        *,
        topic: _ITopic_9eca4852,
        encoding: typing.Optional[EmailEncoding] = None,
    ) -> None:
        '''
        :param topic: The SNS topic to notify.
        :param encoding: The encoding to use for the email within the Amazon SNS notification. Default: UTF-8
        '''
        props = SnsProps(topic=topic, encoding=encoding)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bind")
    def bind(self, _rule: _IReceiptRule_20f5161a) -> _ReceiptRuleActionConfig_6feb97ed:
        '''Returns the receipt rule action specification.

        :param _rule: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ff99cf1ca046ba2b5e78b383a458654e8e7ed33211833f3e2c32db58c5fb6da)
            check_type(argname="argument _rule", value=_rule, expected_type=type_hints["_rule"])
        return typing.cast(_ReceiptRuleActionConfig_6feb97ed, jsii.invoke(self, "bind", [_rule]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses_actions.SnsProps",
    jsii_struct_bases=[],
    name_mapping={"topic": "topic", "encoding": "encoding"},
)
class SnsProps:
    def __init__(
        self,
        *,
        topic: _ITopic_9eca4852,
        encoding: typing.Optional[EmailEncoding] = None,
    ) -> None:
        '''Construction properties for a SNS action.

        :param topic: The SNS topic to notify.
        :param encoding: The encoding to use for the email within the Amazon SNS notification. Default: UTF-8

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_s3 as s3
            import aws_cdk.aws_ses_actions as actions
            
            
            bucket = s3.Bucket(self, "Bucket")
            topic = sns.Topic(self, "Topic")
            
            ses.ReceiptRuleSet(self, "RuleSet",
                rules=[ses.ReceiptRuleOptions(
                    recipients=["hello@aws.com"],
                    actions=[
                        actions.AddHeader(
                            name="X-Special-Header",
                            value="aws"
                        ),
                        actions.S3(
                            bucket=bucket,
                            object_key_prefix="emails/",
                            topic=topic
                        )
                    ]
                ), ses.ReceiptRuleOptions(
                    recipients=["aws.com"],
                    actions=[
                        actions.Sns(
                            topic=topic
                        )
                    ]
                )
                ]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4dd57a2c36b5d96081bf27df6a5f5dc9664fb1e62b39c68b0245127c87131ee)
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
            check_type(argname="argument encoding", value=encoding, expected_type=type_hints["encoding"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "topic": topic,
        }
        if encoding is not None:
            self._values["encoding"] = encoding

    @builtins.property
    def topic(self) -> _ITopic_9eca4852:
        '''The SNS topic to notify.'''
        result = self._values.get("topic")
        assert result is not None, "Required property 'topic' is missing"
        return typing.cast(_ITopic_9eca4852, result)

    @builtins.property
    def encoding(self) -> typing.Optional[EmailEncoding]:
        '''The encoding to use for the email within the Amazon SNS notification.

        :default: UTF-8
        '''
        result = self._values.get("encoding")
        return typing.cast(typing.Optional[EmailEncoding], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SnsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IReceiptRuleAction_941d7a8d)
class Stop(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.aws_ses_actions.Stop"):
    '''Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ses_actions as ses_actions
        from aws_cdk import aws_sns as sns
        
        # topic: sns.Topic
        
        stop = ses_actions.Stop(
            topic=topic
        )
    '''

    def __init__(self, *, topic: typing.Optional[_ITopic_9eca4852] = None) -> None:
        '''
        :param topic: The SNS topic to notify when the stop action is taken.
        '''
        props = StopProps(topic=topic)

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bind")
    def bind(self, _rule: _IReceiptRule_20f5161a) -> _ReceiptRuleActionConfig_6feb97ed:
        '''Returns the receipt rule action specification.

        :param _rule: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d7cfda51e1b6dca326f94431fbe823fade0f7fc9f4b9974e8c545b215ce3a8c)
            check_type(argname="argument _rule", value=_rule, expected_type=type_hints["_rule"])
        return typing.cast(_ReceiptRuleActionConfig_6feb97ed, jsii.invoke(self, "bind", [_rule]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses_actions.StopProps",
    jsii_struct_bases=[],
    name_mapping={"topic": "topic"},
)
class StopProps:
    def __init__(self, *, topic: typing.Optional[_ITopic_9eca4852] = None) -> None:
        '''Construction properties for a stop action.

        :param topic: The SNS topic to notify when the stop action is taken.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses_actions as ses_actions
            from aws_cdk import aws_sns as sns
            
            # topic: sns.Topic
            
            stop_props = ses_actions.StopProps(
                topic=topic
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73591009ec257744526587f77beba227d032486c4c60371ab35e8f381e2ef341)
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if topic is not None:
            self._values["topic"] = topic

    @builtins.property
    def topic(self) -> typing.Optional[_ITopic_9eca4852]:
        '''The SNS topic to notify when the stop action is taken.'''
        result = self._values.get("topic")
        return typing.cast(typing.Optional[_ITopic_9eca4852], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StopProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AddHeader",
    "AddHeaderProps",
    "Bounce",
    "BounceProps",
    "BounceTemplate",
    "BounceTemplateProps",
    "EmailEncoding",
    "Lambda",
    "LambdaInvocationType",
    "LambdaProps",
    "S3",
    "S3Props",
    "Sns",
    "SnsProps",
    "Stop",
    "StopProps",
]

publication.publish()

def _typecheckingstub__105fc3c3cd165ab670ed7315f6f8772759f997da89c1f47dcd5abcdd5b8a67d4(
    _rule: _IReceiptRule_20f5161a,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8074b8d36e00e09d13e403cb0144597d401c4b4212de69cf794e357f2044bbc6(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2f996c58d36c8115f8cab70b8032eaa964550fcbc5df1791bde6faa8deaf815(
    _rule: _IReceiptRule_20f5161a,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10becc64374e762d000b185a3f737684b96a3b21fb43c820f58bbcad29f8dfef(
    *,
    sender: builtins.str,
    template: BounceTemplate,
    topic: typing.Optional[_ITopic_9eca4852] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14a3bcf1f5997a06acbd35725068d819e7cc13cc462249861c26d1b6c72cfd29(
    *,
    message: builtins.str,
    smtp_reply_code: builtins.str,
    status_code: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d93726e71fd780c819e83cd0e14b221830680dac424ed3f6cfaf667ae223bd1(
    rule: _IReceiptRule_20f5161a,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b90a6708b72eec383955e1dee897c153062b0d56e272e25d405eb8bb889276f7(
    *,
    function: _IFunction_6adb0ab8,
    invocation_type: typing.Optional[LambdaInvocationType] = None,
    topic: typing.Optional[_ITopic_9eca4852] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f2e6c8d98ea2e24878b8790662d46dbd681afc3be87064c425c1be30d91c1a4(
    rule: _IReceiptRule_20f5161a,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c3ffb5d7305f7f8cdd0eda6dbf1af4894ccfe04c1d809df6e1bc2c3d2678903(
    *,
    bucket: _IBucket_42e086fd,
    kms_key: typing.Optional[_IKey_5f11635f] = None,
    object_key_prefix: typing.Optional[builtins.str] = None,
    topic: typing.Optional[_ITopic_9eca4852] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ff99cf1ca046ba2b5e78b383a458654e8e7ed33211833f3e2c32db58c5fb6da(
    _rule: _IReceiptRule_20f5161a,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4dd57a2c36b5d96081bf27df6a5f5dc9664fb1e62b39c68b0245127c87131ee(
    *,
    topic: _ITopic_9eca4852,
    encoding: typing.Optional[EmailEncoding] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d7cfda51e1b6dca326f94431fbe823fade0f7fc9f4b9974e8c545b215ce3a8c(
    _rule: _IReceiptRule_20f5161a,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73591009ec257744526587f77beba227d032486c4c60371ab35e8f381e2ef341(
    *,
    topic: typing.Optional[_ITopic_9eca4852] = None,
) -> None:
    """Type checking stubs"""
    pass
