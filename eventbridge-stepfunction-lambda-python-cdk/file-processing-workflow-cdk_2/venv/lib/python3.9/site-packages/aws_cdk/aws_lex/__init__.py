'''
# AWS::Lex Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_lex as lex
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Lex construct libraries](https://constructs.dev/search?q=lex)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Lex resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Lex.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Lex](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Lex.html).

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
class CfnBot(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lex.CfnBot",
):
    '''.. epigraph::

   Amazon Lex V2 is the only supported version in AWS CloudFormation .

    Specifies an Amazon Lex conversational bot.

    You must configure an intent based on the ``AMAZON.FallbackIntent`` built-in intent. If you don't add one, creating the bot will fail.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html
    :exampleMetadata: fixture=_generated

    Example::

        
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        data_privacy: typing.Any,
        idle_session_ttl_in_seconds: jsii.Number,
        name: builtins.str,
        role_arn: builtins.str,
        auto_build_bot_locales: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        bot_file_s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        bot_locales: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.BotLocaleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        bot_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        test_bot_alias_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.TestBotAliasSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        test_bot_alias_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param data_privacy: By default, data stored by Amazon Lex is encrypted. The ``DataPrivacy`` structure provides settings that determine how Amazon Lex handles special cases of securing the data for your bot.
        :param idle_session_ttl_in_seconds: The time, in seconds, that Amazon Lex should keep information about a user's conversation with the bot. A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Lex deletes any data provided before the timeout. You can specify between 60 (1 minute) and 86,400 (24 hours) seconds.
        :param name: The name of the bot locale.
        :param role_arn: The Amazon Resource Name (ARN) of the IAM role used to build and run the bot.
        :param auto_build_bot_locales: Indicates whether Amazon Lex V2 should automatically build the locales for the bot after a change.
        :param bot_file_s3_location: The Amazon S3 location of files used to import a bot. The files must be in the import format specified in `JSON format for importing and exporting <https://docs.aws.amazon.com/lexv2/latest/dg/import-export-format.html>`_ in the *Amazon Lex developer guide.*
        :param bot_locales: A list of locales for the bot.
        :param bot_tags: A list of tags to add to the bot. You can only add tags when you import a bot. You can't use the ``UpdateBot`` operation to update tags. To update tags, use the ``TagResource`` operation.
        :param description: The description of the version.
        :param test_bot_alias_settings: Specifies configuration settings for the alias used to test the bot. If the ``TestBotAliasSettings`` property is not specified, the settings are configured with default values.
        :param test_bot_alias_tags: A list of tags to add to the test alias for a bot. You can only add tags when you import a bot. You can't use the ``UpdateAlias`` operation to update tags. To update tags on the test alias, use the ``TagResource`` operation.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c185fb71324df3b939f1cbff6a813b57733510cba6989dac147b9a3a7e6e7b3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBotProps(
            data_privacy=data_privacy,
            idle_session_ttl_in_seconds=idle_session_ttl_in_seconds,
            name=name,
            role_arn=role_arn,
            auto_build_bot_locales=auto_build_bot_locales,
            bot_file_s3_location=bot_file_s3_location,
            bot_locales=bot_locales,
            bot_tags=bot_tags,
            description=description,
            test_bot_alias_settings=test_bot_alias_settings,
            test_bot_alias_tags=test_bot_alias_tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bab436ed9466bb2dfbcffe8f150f71a01f02f724db7a515af356b7604eb2360)
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
            type_hints = typing.get_type_hints(_typecheckingstub__15efeb50c94c0f4bdd170a08e39d1bbdaa11e3843d27eb6072816f7a53086d91)
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
        '''The Amazon Resource Name (ARN) of the bot.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The unique identifier of the bot.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="dataPrivacy")
    def data_privacy(self) -> typing.Any:
        '''By default, data stored by Amazon Lex is encrypted.'''
        return typing.cast(typing.Any, jsii.get(self, "dataPrivacy"))

    @data_privacy.setter
    def data_privacy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4668d6cdd4af2b7befaa16f723e10618c13be75aa15d81ef3fc5b0a2938929db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataPrivacy", value)

    @builtins.property
    @jsii.member(jsii_name="idleSessionTtlInSeconds")
    def idle_session_ttl_in_seconds(self) -> jsii.Number:
        '''The time, in seconds, that Amazon Lex should keep information about a user's conversation with the bot.'''
        return typing.cast(jsii.Number, jsii.get(self, "idleSessionTtlInSeconds"))

    @idle_session_ttl_in_seconds.setter
    def idle_session_ttl_in_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05337531f67ab566e1a76fe38a76cf27ac63ce8fc8e6e724aed15fa7b8d31908)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleSessionTtlInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the bot locale.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a1ea37ce191acf8a9698c1b06f93041142aa612fff3e59774240d1192fecc1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role used to build and run the bot.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d1de1b03449680ed86d6f014b455506f65035803afa60f89e339dd978cc28af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="autoBuildBotLocales")
    def auto_build_bot_locales(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether Amazon Lex V2 should automatically build the locales for the bot after a change.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "autoBuildBotLocales"))

    @auto_build_bot_locales.setter
    def auto_build_bot_locales(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d59168298bb6c73c8a29b497da006fc40603973cb71aba43e2f0ea0bc3c1c61a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoBuildBotLocales", value)

    @builtins.property
    @jsii.member(jsii_name="botFileS3Location")
    def bot_file_s3_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.S3LocationProperty"]]:
        '''The Amazon S3 location of files used to import a bot.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.S3LocationProperty"]], jsii.get(self, "botFileS3Location"))

    @bot_file_s3_location.setter
    def bot_file_s3_location(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.S3LocationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49ad642c7a6232d4347e9dde2e04bc042cd7d8744c9896121505bc4969f28056)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "botFileS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="botLocales")
    def bot_locales(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.BotLocaleProperty"]]]]:
        '''A list of locales for the bot.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.BotLocaleProperty"]]]], jsii.get(self, "botLocales"))

    @bot_locales.setter
    def bot_locales(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.BotLocaleProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99af8c5daefa40203f5f0fbdfe98fccbc452c26d2c2bf3b4b00da732bcbfcb5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "botLocales", value)

    @builtins.property
    @jsii.member(jsii_name="botTags")
    def bot_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]]:
        '''A list of tags to add to the bot.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]], jsii.get(self, "botTags"))

    @bot_tags.setter
    def bot_tags(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebd0622909df38949fb95f9e4bfc9d82f922d11b6e1fee1b78ed955a197015d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "botTags", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the version.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72103623fa216232524c89f3e94b6a4e2056c1e8ad43603db83275506363e42f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="testBotAliasSettings")
    def test_bot_alias_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.TestBotAliasSettingsProperty"]]:
        '''Specifies configuration settings for the alias used to test the bot.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.TestBotAliasSettingsProperty"]], jsii.get(self, "testBotAliasSettings"))

    @test_bot_alias_settings.setter
    def test_bot_alias_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.TestBotAliasSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8af2b15d1ec9a6dfbd927bbbf7b4b9c006697a2b575338beae8d16e49680244f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "testBotAliasSettings", value)

    @builtins.property
    @jsii.member(jsii_name="testBotAliasTags")
    def test_bot_alias_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]]:
        '''A list of tags to add to the test alias for a bot.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]], jsii.get(self, "testBotAliasTags"))

    @test_bot_alias_tags.setter
    def test_bot_alias_tags(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6da956c0f46d2bfe7dd17bc9ad27b754c6943b2b1d68f58963bb394ff73cf731)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "testBotAliasTags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.AdvancedRecognitionSettingProperty",
        jsii_struct_bases=[],
        name_mapping={"audio_recognition_strategy": "audioRecognitionStrategy"},
    )
    class AdvancedRecognitionSettingProperty:
        def __init__(
            self,
            *,
            audio_recognition_strategy: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides settings that enable advanced recognition settings for slot values.

            :param audio_recognition_strategy: Enables using the slot values as a custom vocabulary for recognizing user utterances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-advancedrecognitionsetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                advanced_recognition_setting_property = lex.CfnBot.AdvancedRecognitionSettingProperty(
                    audio_recognition_strategy="audioRecognitionStrategy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c440956da77e8147763a47aa43d8d996eeb914994200503203ad8dc1de5b8df3)
                check_type(argname="argument audio_recognition_strategy", value=audio_recognition_strategy, expected_type=type_hints["audio_recognition_strategy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if audio_recognition_strategy is not None:
                self._values["audio_recognition_strategy"] = audio_recognition_strategy

        @builtins.property
        def audio_recognition_strategy(self) -> typing.Optional[builtins.str]:
            '''Enables using the slot values as a custom vocabulary for recognizing user utterances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-advancedrecognitionsetting.html#cfn-lex-bot-advancedrecognitionsetting-audiorecognitionstrategy
            '''
            result = self._values.get("audio_recognition_strategy")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdvancedRecognitionSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.AllowedInputTypesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allow_audio_input": "allowAudioInput",
            "allow_dtmf_input": "allowDtmfInput",
        },
    )
    class AllowedInputTypesProperty:
        def __init__(
            self,
            *,
            allow_audio_input: typing.Union[builtins.bool, _IResolvable_da3f097b],
            allow_dtmf_input: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''Specifies the allowed input types.

            :param allow_audio_input: Indicates whether audio input is allowed.
            :param allow_dtmf_input: Indicates whether DTMF input is allowed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-allowedinputtypes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                allowed_input_types_property = lex.CfnBot.AllowedInputTypesProperty(
                    allow_audio_input=False,
                    allow_dtmf_input=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b3838670eeffedef2bc12112ab8648963f9cefc6b5d549db48de7c20c23377df)
                check_type(argname="argument allow_audio_input", value=allow_audio_input, expected_type=type_hints["allow_audio_input"])
                check_type(argname="argument allow_dtmf_input", value=allow_dtmf_input, expected_type=type_hints["allow_dtmf_input"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "allow_audio_input": allow_audio_input,
                "allow_dtmf_input": allow_dtmf_input,
            }

        @builtins.property
        def allow_audio_input(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether audio input is allowed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-allowedinputtypes.html#cfn-lex-bot-allowedinputtypes-allowaudioinput
            '''
            result = self._values.get("allow_audio_input")
            assert result is not None, "Required property 'allow_audio_input' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def allow_dtmf_input(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether DTMF input is allowed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-allowedinputtypes.html#cfn-lex-bot-allowedinputtypes-allowdtmfinput
            '''
            result = self._values.get("allow_dtmf_input")
            assert result is not None, "Required property 'allow_dtmf_input' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AllowedInputTypesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.AudioAndDTMFInputSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "start_timeout_ms": "startTimeoutMs",
            "audio_specification": "audioSpecification",
            "dtmf_specification": "dtmfSpecification",
        },
    )
    class AudioAndDTMFInputSpecificationProperty:
        def __init__(
            self,
            *,
            start_timeout_ms: jsii.Number,
            audio_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.AudioSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            dtmf_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.DTMFSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the audio and DTMF input specification.

            :param start_timeout_ms: Time for which a bot waits before assuming that the customer isn't going to speak or press a key. This timeout is shared between Audio and DTMF inputs.
            :param audio_specification: Specifies the settings on audio input.
            :param dtmf_specification: Specifies the settings on DTMF input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audioanddtmfinputspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                audio_and_dTMFInput_specification_property = lex.CfnBot.AudioAndDTMFInputSpecificationProperty(
                    start_timeout_ms=123,
                
                    # the properties below are optional
                    audio_specification=lex.CfnBot.AudioSpecificationProperty(
                        end_timeout_ms=123,
                        max_length_ms=123
                    ),
                    dtmf_specification=lex.CfnBot.DTMFSpecificationProperty(
                        deletion_character="deletionCharacter",
                        end_character="endCharacter",
                        end_timeout_ms=123,
                        max_length=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c052ee345e65d8dccab612f97fe193228903fbbb67e70bcb8f742a6105953515)
                check_type(argname="argument start_timeout_ms", value=start_timeout_ms, expected_type=type_hints["start_timeout_ms"])
                check_type(argname="argument audio_specification", value=audio_specification, expected_type=type_hints["audio_specification"])
                check_type(argname="argument dtmf_specification", value=dtmf_specification, expected_type=type_hints["dtmf_specification"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "start_timeout_ms": start_timeout_ms,
            }
            if audio_specification is not None:
                self._values["audio_specification"] = audio_specification
            if dtmf_specification is not None:
                self._values["dtmf_specification"] = dtmf_specification

        @builtins.property
        def start_timeout_ms(self) -> jsii.Number:
            '''Time for which a bot waits before assuming that the customer isn't going to speak or press a key.

            This timeout is shared between Audio and DTMF inputs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audioanddtmfinputspecification.html#cfn-lex-bot-audioanddtmfinputspecification-starttimeoutms
            '''
            result = self._values.get("start_timeout_ms")
            assert result is not None, "Required property 'start_timeout_ms' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def audio_specification(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.AudioSpecificationProperty"]]:
            '''Specifies the settings on audio input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audioanddtmfinputspecification.html#cfn-lex-bot-audioanddtmfinputspecification-audiospecification
            '''
            result = self._values.get("audio_specification")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.AudioSpecificationProperty"]], result)

        @builtins.property
        def dtmf_specification(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DTMFSpecificationProperty"]]:
            '''Specifies the settings on DTMF input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audioanddtmfinputspecification.html#cfn-lex-bot-audioanddtmfinputspecification-dtmfspecification
            '''
            result = self._values.get("dtmf_specification")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DTMFSpecificationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioAndDTMFInputSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.AudioLogDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_bucket": "s3Bucket"},
    )
    class AudioLogDestinationProperty:
        def __init__(
            self,
            *,
            s3_bucket: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.S3BucketLogDestinationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The location of audio log files collected when conversation logging is enabled for a bot.

            :param s3_bucket: Specifies the Amazon S3 bucket where the audio files are stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audiologdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                audio_log_destination_property = lex.CfnBot.AudioLogDestinationProperty(
                    s3_bucket=lex.CfnBot.S3BucketLogDestinationProperty(
                        log_prefix="logPrefix",
                        s3_bucket_arn="s3BucketArn",
                
                        # the properties below are optional
                        kms_key_arn="kmsKeyArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f63a4e17f071cd3f1324d2209c869ca77ffb749d83b8046aa835feea80b9c16c)
                check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3_bucket": s3_bucket,
            }

        @builtins.property
        def s3_bucket(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnBot.S3BucketLogDestinationProperty"]:
            '''Specifies the Amazon S3 bucket where the audio files are stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audiologdestination.html#cfn-lex-bot-audiologdestination-s3bucket
            '''
            result = self._values.get("s3_bucket")
            assert result is not None, "Required property 's3_bucket' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBot.S3BucketLogDestinationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioLogDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.AudioLogSettingProperty",
        jsii_struct_bases=[],
        name_mapping={"destination": "destination", "enabled": "enabled"},
    )
    class AudioLogSettingProperty:
        def __init__(
            self,
            *,
            destination: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.AudioLogDestinationProperty", typing.Dict[builtins.str, typing.Any]]],
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''Settings for logging audio of conversations between Amazon Lex and a user.

            You specify whether to log audio and the Amazon S3 bucket where the audio file is stored.

            :param destination: Specifies the location of the audio log files collected when conversation logging is enabled for a bot.
            :param enabled: Determines whether audio logging in enabled for the bot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audiologsetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                audio_log_setting_property = lex.CfnBot.AudioLogSettingProperty(
                    destination=lex.CfnBot.AudioLogDestinationProperty(
                        s3_bucket=lex.CfnBot.S3BucketLogDestinationProperty(
                            log_prefix="logPrefix",
                            s3_bucket_arn="s3BucketArn",
                
                            # the properties below are optional
                            kms_key_arn="kmsKeyArn"
                        )
                    ),
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4382bc3265af37750e55e2a9b53a7a5b403a0a22fa40facd692ffdb2a075b9cc)
                check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination": destination,
                "enabled": enabled,
            }

        @builtins.property
        def destination(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnBot.AudioLogDestinationProperty"]:
            '''Specifies the location of the audio log files collected when conversation logging is enabled for a bot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audiologsetting.html#cfn-lex-bot-audiologsetting-destination
            '''
            result = self._values.get("destination")
            assert result is not None, "Required property 'destination' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBot.AudioLogDestinationProperty"], result)

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Determines whether audio logging in enabled for the bot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audiologsetting.html#cfn-lex-bot-audiologsetting-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioLogSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.AudioSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "end_timeout_ms": "endTimeoutMs",
            "max_length_ms": "maxLengthMs",
        },
    )
    class AudioSpecificationProperty:
        def __init__(
            self,
            *,
            end_timeout_ms: jsii.Number,
            max_length_ms: jsii.Number,
        ) -> None:
            '''Specifies the audio input specifications.

            :param end_timeout_ms: Time for which a bot waits after the customer stops speaking to assume the utterance is finished.
            :param max_length_ms: Time for how long Amazon Lex waits before speech input is truncated and the speech is returned to application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audiospecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                audio_specification_property = lex.CfnBot.AudioSpecificationProperty(
                    end_timeout_ms=123,
                    max_length_ms=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2e44ef412e3afcfbf71cf2299bd8cea4e94f42bf7c72d8f4699c80d7c4f63b76)
                check_type(argname="argument end_timeout_ms", value=end_timeout_ms, expected_type=type_hints["end_timeout_ms"])
                check_type(argname="argument max_length_ms", value=max_length_ms, expected_type=type_hints["max_length_ms"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "end_timeout_ms": end_timeout_ms,
                "max_length_ms": max_length_ms,
            }

        @builtins.property
        def end_timeout_ms(self) -> jsii.Number:
            '''Time for which a bot waits after the customer stops speaking to assume the utterance is finished.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audiospecification.html#cfn-lex-bot-audiospecification-endtimeoutms
            '''
            result = self._values.get("end_timeout_ms")
            assert result is not None, "Required property 'end_timeout_ms' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def max_length_ms(self) -> jsii.Number:
            '''Time for how long Amazon Lex waits before speech input is truncated and the speech is returned to application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-audiospecification.html#cfn-lex-bot-audiospecification-maxlengthms
            '''
            result = self._values.get("max_length_ms")
            assert result is not None, "Required property 'max_length_ms' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.BotAliasLocaleSettingsItemProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bot_alias_locale_setting": "botAliasLocaleSetting",
            "locale_id": "localeId",
        },
    )
    class BotAliasLocaleSettingsItemProperty:
        def __init__(
            self,
            *,
            bot_alias_locale_setting: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.BotAliasLocaleSettingsProperty", typing.Dict[builtins.str, typing.Any]]],
            locale_id: builtins.str,
        ) -> None:
            '''Specifies locale settings for a single locale.

            :param bot_alias_locale_setting: Specifies locale settings for a locale.
            :param locale_id: Specifies the locale that the settings apply to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botaliaslocalesettingsitem.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                bot_alias_locale_settings_item_property = lex.CfnBot.BotAliasLocaleSettingsItemProperty(
                    bot_alias_locale_setting=lex.CfnBot.BotAliasLocaleSettingsProperty(
                        enabled=False,
                
                        # the properties below are optional
                        code_hook_specification=lex.CfnBot.CodeHookSpecificationProperty(
                            lambda_code_hook=lex.CfnBot.LambdaCodeHookProperty(
                                code_hook_interface_version="codeHookInterfaceVersion",
                                lambda_arn="lambdaArn"
                            )
                        )
                    ),
                    locale_id="localeId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b8cb59d3ac7a8ae237407b5df223685e38d3b85ded672a3f1009115577aea63a)
                check_type(argname="argument bot_alias_locale_setting", value=bot_alias_locale_setting, expected_type=type_hints["bot_alias_locale_setting"])
                check_type(argname="argument locale_id", value=locale_id, expected_type=type_hints["locale_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bot_alias_locale_setting": bot_alias_locale_setting,
                "locale_id": locale_id,
            }

        @builtins.property
        def bot_alias_locale_setting(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnBot.BotAliasLocaleSettingsProperty"]:
            '''Specifies locale settings for a locale.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botaliaslocalesettingsitem.html#cfn-lex-bot-botaliaslocalesettingsitem-botaliaslocalesetting
            '''
            result = self._values.get("bot_alias_locale_setting")
            assert result is not None, "Required property 'bot_alias_locale_setting' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBot.BotAliasLocaleSettingsProperty"], result)

        @builtins.property
        def locale_id(self) -> builtins.str:
            '''Specifies the locale that the settings apply to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botaliaslocalesettingsitem.html#cfn-lex-bot-botaliaslocalesettingsitem-localeid
            '''
            result = self._values.get("locale_id")
            assert result is not None, "Required property 'locale_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BotAliasLocaleSettingsItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.BotAliasLocaleSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "code_hook_specification": "codeHookSpecification",
        },
    )
    class BotAliasLocaleSettingsProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
            code_hook_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.CodeHookSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies settings that are unique to a locale.

            For example, you can use different Lambda function depending on the bot's locale.

            :param enabled: Determines whether the locale is enabled for the bot. If the value is ``false`` , the locale isn't available for use.
            :param code_hook_specification: Specifies the Lambda function that should be used in the locale.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botaliaslocalesettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                bot_alias_locale_settings_property = lex.CfnBot.BotAliasLocaleSettingsProperty(
                    enabled=False,
                
                    # the properties below are optional
                    code_hook_specification=lex.CfnBot.CodeHookSpecificationProperty(
                        lambda_code_hook=lex.CfnBot.LambdaCodeHookProperty(
                            code_hook_interface_version="codeHookInterfaceVersion",
                            lambda_arn="lambdaArn"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fccab71cd793cc569d18b739e52d926af862173e626b31edeb7b0ec09a1b8fa7)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument code_hook_specification", value=code_hook_specification, expected_type=type_hints["code_hook_specification"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled": enabled,
            }
            if code_hook_specification is not None:
                self._values["code_hook_specification"] = code_hook_specification

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Determines whether the locale is enabled for the bot.

            If the value is ``false`` , the locale isn't available for use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botaliaslocalesettings.html#cfn-lex-bot-botaliaslocalesettings-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def code_hook_specification(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.CodeHookSpecificationProperty"]]:
            '''Specifies the Lambda function that should be used in the locale.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botaliaslocalesettings.html#cfn-lex-bot-botaliaslocalesettings-codehookspecification
            '''
            result = self._values.get("code_hook_specification")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.CodeHookSpecificationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BotAliasLocaleSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.BotLocaleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "locale_id": "localeId",
            "nlu_confidence_threshold": "nluConfidenceThreshold",
            "custom_vocabulary": "customVocabulary",
            "description": "description",
            "intents": "intents",
            "slot_types": "slotTypes",
            "voice_settings": "voiceSettings",
        },
    )
    class BotLocaleProperty:
        def __init__(
            self,
            *,
            locale_id: builtins.str,
            nlu_confidence_threshold: jsii.Number,
            custom_vocabulary: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.CustomVocabularyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            description: typing.Optional[builtins.str] = None,
            intents: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.IntentProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            slot_types: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.SlotTypeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            voice_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.VoiceSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Provides configuration information for a locale.

            :param locale_id: The identifier of the language and locale that the bot will be used in. The string must match one of the supported locales.
            :param nlu_confidence_threshold: Determines the threshold where Amazon Lex will insert the ``AMAZON.FallbackIntent`` , ``AMAZON.KendraSearchIntent`` , or both when returning alternative intents. You must configure an ``AMAZON.FallbackIntent`` . ``AMAZON.KendraSearchIntent`` is only inserted if it is configured for the bot.
            :param custom_vocabulary: Specifies a custom vocabulary to use with a specific locale.
            :param description: A description of the bot locale. Use this to help identify the bot locale in lists.
            :param intents: One or more intents defined for the locale.
            :param slot_types: One or more slot types defined for the locale.
            :param voice_settings: Defines settings for using an Amazon Polly voice to communicate with a user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html
            :exampleMetadata: fixture=_generated

            Example::

                
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2ad20956b5309c4b6154f09c947ce4023f20ed7a602b3cfa60f2bd3cfda11dd4)
                check_type(argname="argument locale_id", value=locale_id, expected_type=type_hints["locale_id"])
                check_type(argname="argument nlu_confidence_threshold", value=nlu_confidence_threshold, expected_type=type_hints["nlu_confidence_threshold"])
                check_type(argname="argument custom_vocabulary", value=custom_vocabulary, expected_type=type_hints["custom_vocabulary"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument intents", value=intents, expected_type=type_hints["intents"])
                check_type(argname="argument slot_types", value=slot_types, expected_type=type_hints["slot_types"])
                check_type(argname="argument voice_settings", value=voice_settings, expected_type=type_hints["voice_settings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "locale_id": locale_id,
                "nlu_confidence_threshold": nlu_confidence_threshold,
            }
            if custom_vocabulary is not None:
                self._values["custom_vocabulary"] = custom_vocabulary
            if description is not None:
                self._values["description"] = description
            if intents is not None:
                self._values["intents"] = intents
            if slot_types is not None:
                self._values["slot_types"] = slot_types
            if voice_settings is not None:
                self._values["voice_settings"] = voice_settings

        @builtins.property
        def locale_id(self) -> builtins.str:
            '''The identifier of the language and locale that the bot will be used in.

            The string must match one of the supported locales.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-localeid
            '''
            result = self._values.get("locale_id")
            assert result is not None, "Required property 'locale_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def nlu_confidence_threshold(self) -> jsii.Number:
            '''Determines the threshold where Amazon Lex will insert the ``AMAZON.FallbackIntent`` , ``AMAZON.KendraSearchIntent`` , or both when returning alternative intents. You must configure an ``AMAZON.FallbackIntent`` . ``AMAZON.KendraSearchIntent`` is only inserted if it is configured for the bot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-nluconfidencethreshold
            '''
            result = self._values.get("nlu_confidence_threshold")
            assert result is not None, "Required property 'nlu_confidence_threshold' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def custom_vocabulary(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.CustomVocabularyProperty"]]:
            '''Specifies a custom vocabulary to use with a specific locale.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-customvocabulary
            '''
            result = self._values.get("custom_vocabulary")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.CustomVocabularyProperty"]], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''A description of the bot locale.

            Use this to help identify the bot locale in lists.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def intents(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.IntentProperty"]]]]:
            '''One or more intents defined for the locale.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-intents
            '''
            result = self._values.get("intents")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.IntentProperty"]]]], result)

        @builtins.property
        def slot_types(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotTypeProperty"]]]]:
            '''One or more slot types defined for the locale.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-slottypes
            '''
            result = self._values.get("slot_types")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotTypeProperty"]]]], result)

        @builtins.property
        def voice_settings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.VoiceSettingsProperty"]]:
            '''Defines settings for using an Amazon Polly voice to communicate with a user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-botlocale.html#cfn-lex-bot-botlocale-voicesettings
            '''
            result = self._values.get("voice_settings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.VoiceSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BotLocaleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.ButtonProperty",
        jsii_struct_bases=[],
        name_mapping={"text": "text", "value": "value"},
    )
    class ButtonProperty:
        def __init__(self, *, text: builtins.str, value: builtins.str) -> None:
            '''Describes a button to use on a response card used to gather slot values from a user.

            :param text: The text that appears on the button. Use this to tell the user what value is returned when they choose this button.
            :param value: The value returned to Amazon Lex when the user chooses this button. This must be one of the slot values configured for the slot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-button.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                button_property = lex.CfnBot.ButtonProperty(
                    text="text",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d0208df4d8ce79e1029770ef72acb7332713a8684db0810b60ddcd684dc98bcd)
                check_type(argname="argument text", value=text, expected_type=type_hints["text"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "text": text,
                "value": value,
            }

        @builtins.property
        def text(self) -> builtins.str:
            '''The text that appears on the button.

            Use this to tell the user what value is returned when they choose this button.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-button.html#cfn-lex-bot-button-text
            '''
            result = self._values.get("text")
            assert result is not None, "Required property 'text' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value returned to Amazon Lex when the user chooses this button.

            This must be one of the slot values configured for the slot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-button.html#cfn-lex-bot-button-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ButtonProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.CloudWatchLogGroupLogDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_log_group_arn": "cloudWatchLogGroupArn",
            "log_prefix": "logPrefix",
        },
    )
    class CloudWatchLogGroupLogDestinationProperty:
        def __init__(
            self,
            *,
            cloud_watch_log_group_arn: builtins.str,
            log_prefix: builtins.str,
        ) -> None:
            '''The Amazon CloudWatch Logs log group where the text and metadata logs are delivered.

            The log group must exist before you enable logging.

            :param cloud_watch_log_group_arn: The Amazon Resource Name (ARN) of the log group where text and metadata logs are delivered.
            :param log_prefix: The prefix of the log stream name within the log group that you specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-cloudwatchloggrouplogdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                cloud_watch_log_group_log_destination_property = lex.CfnBot.CloudWatchLogGroupLogDestinationProperty(
                    cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                    log_prefix="logPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f146fd3bf196dbdf204053031018bcc0244c9347c6ceace1ea6dcdeec4b168de)
                check_type(argname="argument cloud_watch_log_group_arn", value=cloud_watch_log_group_arn, expected_type=type_hints["cloud_watch_log_group_arn"])
                check_type(argname="argument log_prefix", value=log_prefix, expected_type=type_hints["log_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cloud_watch_log_group_arn": cloud_watch_log_group_arn,
                "log_prefix": log_prefix,
            }

        @builtins.property
        def cloud_watch_log_group_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the log group where text and metadata logs are delivered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-cloudwatchloggrouplogdestination.html#cfn-lex-bot-cloudwatchloggrouplogdestination-cloudwatchloggrouparn
            '''
            result = self._values.get("cloud_watch_log_group_arn")
            assert result is not None, "Required property 'cloud_watch_log_group_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def log_prefix(self) -> builtins.str:
            '''The prefix of the log stream name within the log group that you specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-cloudwatchloggrouplogdestination.html#cfn-lex-bot-cloudwatchloggrouplogdestination-logprefix
            '''
            result = self._values.get("log_prefix")
            assert result is not None, "Required property 'log_prefix' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLogGroupLogDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.CodeHookSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"lambda_code_hook": "lambdaCodeHook"},
    )
    class CodeHookSpecificationProperty:
        def __init__(
            self,
            *,
            lambda_code_hook: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.LambdaCodeHookProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Contains information about code hooks that Amazon Lex calls during a conversation.

            :param lambda_code_hook: Specifies a Lambda function that verifies requests to a bot or fulfills the user's request to a bot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-codehookspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                code_hook_specification_property = lex.CfnBot.CodeHookSpecificationProperty(
                    lambda_code_hook=lex.CfnBot.LambdaCodeHookProperty(
                        code_hook_interface_version="codeHookInterfaceVersion",
                        lambda_arn="lambdaArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__da6a0a3d3181926b6600cb1e93e0bf761a0d23d96eb57f580dcef39cc7d85734)
                check_type(argname="argument lambda_code_hook", value=lambda_code_hook, expected_type=type_hints["lambda_code_hook"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "lambda_code_hook": lambda_code_hook,
            }

        @builtins.property
        def lambda_code_hook(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnBot.LambdaCodeHookProperty"]:
            '''Specifies a Lambda function that verifies requests to a bot or fulfills the user's request to a bot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-codehookspecification.html#cfn-lex-bot-codehookspecification-lambdacodehook
            '''
            result = self._values.get("lambda_code_hook")
            assert result is not None, "Required property 'lambda_code_hook' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBot.LambdaCodeHookProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeHookSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.ConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"expression_string": "expressionString"},
    )
    class ConditionProperty:
        def __init__(self, *, expression_string: builtins.str) -> None:
            '''Provides an expression that evaluates to true or false.

            :param expression_string: The expression string that is evaluated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-condition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                condition_property = lex.CfnBot.ConditionProperty(
                    expression_string="expressionString"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__955a721d21fa1f19bf91fc3c341e8f185dbe2e44d2e52eefdfc64abc889f0959)
                check_type(argname="argument expression_string", value=expression_string, expected_type=type_hints["expression_string"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "expression_string": expression_string,
            }

        @builtins.property
        def expression_string(self) -> builtins.str:
            '''The expression string that is evaluated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-condition.html#cfn-lex-bot-condition-expressionstring
            '''
            result = self._values.get("expression_string")
            assert result is not None, "Required property 'expression_string' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.ConditionalBranchProperty",
        jsii_struct_bases=[],
        name_mapping={
            "condition": "condition",
            "name": "name",
            "next_step": "nextStep",
            "response": "response",
        },
    )
    class ConditionalBranchProperty:
        def __init__(
            self,
            *,
            condition: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ConditionProperty", typing.Dict[builtins.str, typing.Any]]],
            name: builtins.str,
            next_step: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.DialogStateProperty", typing.Dict[builtins.str, typing.Any]]],
            response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ResponseSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A set of actions that Amazon Lex should run if the condition is matched.

            :param condition: Contains the expression to evaluate. If the condition is true, the branch's actions are taken.
            :param name: The name of the branch.
            :param next_step: The next step in the conversation.
            :param response: Specifies a list of message groups that Amazon Lex uses to respond the user input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-conditionalbranch.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                # slot_value_override_property_: lex.CfnBot.SlotValueOverrideProperty
                
                conditional_branch_property = lex.CfnBot.ConditionalBranchProperty(
                    condition=lex.CfnBot.ConditionProperty(
                        expression_string="expressionString"
                    ),
                    name="name",
                    next_step=lex.CfnBot.DialogStateProperty(
                        dialog_action=lex.CfnBot.DialogActionProperty(
                            type="type",
                
                            # the properties below are optional
                            slot_to_elicit="slotToElicit",
                            suppress_next_message=False
                        ),
                        intent=lex.CfnBot.IntentOverrideProperty(
                            name="name",
                            slots=[lex.CfnBot.SlotValueOverrideMapProperty(
                                slot_name="slotName",
                                slot_value_override=lex.CfnBot.SlotValueOverrideProperty(
                                    shape="shape",
                                    value=lex.CfnBot.SlotValueProperty(
                                        interpreted_value="interpretedValue"
                                    ),
                                    values=[slot_value_override_property_]
                                )
                            )]
                        ),
                        session_attributes=[lex.CfnBot.SessionAttributeProperty(
                            key="key",
                
                            # the properties below are optional
                            value="value"
                        )]
                    ),
                
                    # the properties below are optional
                    response=lex.CfnBot.ResponseSpecificationProperty(
                        message_groups_list=[lex.CfnBot.MessageGroupProperty(
                            message=lex.CfnBot.MessageProperty(
                                custom_payload=lex.CfnBot.CustomPayloadProperty(
                                    value="value"
                                ),
                                image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                    title="title",
                
                                    # the properties below are optional
                                    buttons=[lex.CfnBot.ButtonProperty(
                                        text="text",
                                        value="value"
                                    )],
                                    image_url="imageUrl",
                                    subtitle="subtitle"
                                ),
                                plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                    value="value"
                                ),
                                ssml_message=lex.CfnBot.SSMLMessageProperty(
                                    value="value"
                                )
                            ),
                
                            # the properties below are optional
                            variations=[lex.CfnBot.MessageProperty(
                                custom_payload=lex.CfnBot.CustomPayloadProperty(
                                    value="value"
                                ),
                                image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                    title="title",
                
                                    # the properties below are optional
                                    buttons=[lex.CfnBot.ButtonProperty(
                                        text="text",
                                        value="value"
                                    )],
                                    image_url="imageUrl",
                                    subtitle="subtitle"
                                ),
                                plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                    value="value"
                                ),
                                ssml_message=lex.CfnBot.SSMLMessageProperty(
                                    value="value"
                                )
                            )]
                        )],
                
                        # the properties below are optional
                        allow_interrupt=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fc5c77c3d99e5efee20bf629186ee9b96fd242aa9b1f1e923dec8bf6554cd229)
                check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument next_step", value=next_step, expected_type=type_hints["next_step"])
                check_type(argname="argument response", value=response, expected_type=type_hints["response"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "condition": condition,
                "name": name,
                "next_step": next_step,
            }
            if response is not None:
                self._values["response"] = response

        @builtins.property
        def condition(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionProperty"]:
            '''Contains the expression to evaluate.

            If the condition is true, the branch's actions are taken.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-conditionalbranch.html#cfn-lex-bot-conditionalbranch-condition
            '''
            result = self._values.get("condition")
            assert result is not None, "Required property 'condition' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionProperty"], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the branch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-conditionalbranch.html#cfn-lex-bot-conditionalbranch-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def next_step(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]:
            '''The next step in the conversation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-conditionalbranch.html#cfn-lex-bot-conditionalbranch-nextstep
            '''
            result = self._values.get("next_step")
            assert result is not None, "Required property 'next_step' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"], result)

        @builtins.property
        def response(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]]:
            '''Specifies a list of message groups that Amazon Lex uses to respond the user input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-conditionalbranch.html#cfn-lex-bot-conditionalbranch-response
            '''
            result = self._values.get("response")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConditionalBranchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.ConditionalSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "conditional_branches": "conditionalBranches",
            "default_branch": "defaultBranch",
            "is_active": "isActive",
        },
    )
    class ConditionalSpecificationProperty:
        def __init__(
            self,
            *,
            conditional_branches: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ConditionalBranchProperty", typing.Dict[builtins.str, typing.Any]]]]],
            default_branch: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.DefaultConditionalBranchProperty", typing.Dict[builtins.str, typing.Any]]],
            is_active: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''Provides a list of conditional branches.

            Branches are evaluated in the order that they are entered in the list. The first branch with a condition that evaluates to true is executed. The last branch in the list is the default branch. The default branch should not have any condition expression. The default branch is executed if no other branch has a matching condition.

            :param conditional_branches: A list of conditional branches. A conditional branch is made up of a condition, a response and a next step. The response and next step are executed when the condition is true.
            :param default_branch: The conditional branch that should be followed when the conditions for other branches are not satisfied. A conditional branch is made up of a condition, a response and a next step.
            :param is_active: Determines whether a conditional branch is active. When ``IsActive`` is false, the conditions are not evaluated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-conditionalspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                # slot_value_override_property_: lex.CfnBot.SlotValueOverrideProperty
                
                conditional_specification_property = lex.CfnBot.ConditionalSpecificationProperty(
                    conditional_branches=[lex.CfnBot.ConditionalBranchProperty(
                        condition=lex.CfnBot.ConditionProperty(
                            expression_string="expressionString"
                        ),
                        name="name",
                        next_step=lex.CfnBot.DialogStateProperty(
                            dialog_action=lex.CfnBot.DialogActionProperty(
                                type="type",
                
                                # the properties below are optional
                                slot_to_elicit="slotToElicit",
                                suppress_next_message=False
                            ),
                            intent=lex.CfnBot.IntentOverrideProperty(
                                name="name",
                                slots=[lex.CfnBot.SlotValueOverrideMapProperty(
                                    slot_name="slotName",
                                    slot_value_override=lex.CfnBot.SlotValueOverrideProperty(
                                        shape="shape",
                                        value=lex.CfnBot.SlotValueProperty(
                                            interpreted_value="interpretedValue"
                                        ),
                                        values=[slot_value_override_property_]
                                    )
                                )]
                            ),
                            session_attributes=[lex.CfnBot.SessionAttributeProperty(
                                key="key",
                
                                # the properties below are optional
                                value="value"
                            )]
                        ),
                
                        # the properties below are optional
                        response=lex.CfnBot.ResponseSpecificationProperty(
                            message_groups_list=[lex.CfnBot.MessageGroupProperty(
                                message=lex.CfnBot.MessageProperty(
                                    custom_payload=lex.CfnBot.CustomPayloadProperty(
                                        value="value"
                                    ),
                                    image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                        title="title",
                
                                        # the properties below are optional
                                        buttons=[lex.CfnBot.ButtonProperty(
                                            text="text",
                                            value="value"
                                        )],
                                        image_url="imageUrl",
                                        subtitle="subtitle"
                                    ),
                                    plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                        value="value"
                                    ),
                                    ssml_message=lex.CfnBot.SSMLMessageProperty(
                                        value="value"
                                    )
                                ),
                
                                # the properties below are optional
                                variations=[lex.CfnBot.MessageProperty(
                                    custom_payload=lex.CfnBot.CustomPayloadProperty(
                                        value="value"
                                    ),
                                    image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                        title="title",
                
                                        # the properties below are optional
                                        buttons=[lex.CfnBot.ButtonProperty(
                                            text="text",
                                            value="value"
                                        )],
                                        image_url="imageUrl",
                                        subtitle="subtitle"
                                    ),
                                    plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                        value="value"
                                    ),
                                    ssml_message=lex.CfnBot.SSMLMessageProperty(
                                        value="value"
                                    )
                                )]
                            )],
                
                            # the properties below are optional
                            allow_interrupt=False
                        )
                    )],
                    default_branch=lex.CfnBot.DefaultConditionalBranchProperty(
                        next_step=lex.CfnBot.DialogStateProperty(
                            dialog_action=lex.CfnBot.DialogActionProperty(
                                type="type",
                
                                # the properties below are optional
                                slot_to_elicit="slotToElicit",
                                suppress_next_message=False
                            ),
                            intent=lex.CfnBot.IntentOverrideProperty(
                                name="name",
                                slots=[lex.CfnBot.SlotValueOverrideMapProperty(
                                    slot_name="slotName",
                                    slot_value_override=lex.CfnBot.SlotValueOverrideProperty(
                                        shape="shape",
                                        value=lex.CfnBot.SlotValueProperty(
                                            interpreted_value="interpretedValue"
                                        ),
                                        values=[slot_value_override_property_]
                                    )
                                )]
                            ),
                            session_attributes=[lex.CfnBot.SessionAttributeProperty(
                                key="key",
                
                                # the properties below are optional
                                value="value"
                            )]
                        ),
                        response=lex.CfnBot.ResponseSpecificationProperty(
                            message_groups_list=[lex.CfnBot.MessageGroupProperty(
                                message=lex.CfnBot.MessageProperty(
                                    custom_payload=lex.CfnBot.CustomPayloadProperty(
                                        value="value"
                                    ),
                                    image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                        title="title",
                
                                        # the properties below are optional
                                        buttons=[lex.CfnBot.ButtonProperty(
                                            text="text",
                                            value="value"
                                        )],
                                        image_url="imageUrl",
                                        subtitle="subtitle"
                                    ),
                                    plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                        value="value"
                                    ),
                                    ssml_message=lex.CfnBot.SSMLMessageProperty(
                                        value="value"
                                    )
                                ),
                
                                # the properties below are optional
                                variations=[lex.CfnBot.MessageProperty(
                                    custom_payload=lex.CfnBot.CustomPayloadProperty(
                                        value="value"
                                    ),
                                    image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                        title="title",
                
                                        # the properties below are optional
                                        buttons=[lex.CfnBot.ButtonProperty(
                                            text="text",
                                            value="value"
                                        )],
                                        image_url="imageUrl",
                                        subtitle="subtitle"
                                    ),
                                    plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                        value="value"
                                    ),
                                    ssml_message=lex.CfnBot.SSMLMessageProperty(
                                        value="value"
                                    )
                                )]
                            )],
                
                            # the properties below are optional
                            allow_interrupt=False
                        )
                    ),
                    is_active=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__de4586a5996f5a859b3286e8e34d08872ebb2261aed1437d975e7fcb4b3c77b3)
                check_type(argname="argument conditional_branches", value=conditional_branches, expected_type=type_hints["conditional_branches"])
                check_type(argname="argument default_branch", value=default_branch, expected_type=type_hints["default_branch"])
                check_type(argname="argument is_active", value=is_active, expected_type=type_hints["is_active"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "conditional_branches": conditional_branches,
                "default_branch": default_branch,
                "is_active": is_active,
            }

        @builtins.property
        def conditional_branches(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalBranchProperty"]]]:
            '''A list of conditional branches.

            A conditional branch is made up of a condition, a response and a next step. The response and next step are executed when the condition is true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-conditionalspecification.html#cfn-lex-bot-conditionalspecification-conditionalbranches
            '''
            result = self._values.get("conditional_branches")
            assert result is not None, "Required property 'conditional_branches' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalBranchProperty"]]], result)

        @builtins.property
        def default_branch(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnBot.DefaultConditionalBranchProperty"]:
            '''The conditional branch that should be followed when the conditions for other branches are not satisfied.

            A conditional branch is made up of a condition, a response and a next step.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-conditionalspecification.html#cfn-lex-bot-conditionalspecification-defaultbranch
            '''
            result = self._values.get("default_branch")
            assert result is not None, "Required property 'default_branch' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBot.DefaultConditionalBranchProperty"], result)

        @builtins.property
        def is_active(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Determines whether a conditional branch is active.

            When ``IsActive`` is false, the conditions are not evaluated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-conditionalspecification.html#cfn-lex-bot-conditionalspecification-isactive
            '''
            result = self._values.get("is_active")
            assert result is not None, "Required property 'is_active' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConditionalSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.ConversationLogSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_log_settings": "audioLogSettings",
            "text_log_settings": "textLogSettings",
        },
    )
    class ConversationLogSettingsProperty:
        def __init__(
            self,
            *,
            audio_log_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.AudioLogSettingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            text_log_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.TextLogSettingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Configures conversation logging that saves audio, text, and metadata for the conversations with your users.

            :param audio_log_settings: The Amazon S3 settings for logging audio to an S3 bucket.
            :param text_log_settings: The Amazon CloudWatch Logs settings for logging text and metadata.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-conversationlogsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                conversation_log_settings_property = lex.CfnBot.ConversationLogSettingsProperty(
                    audio_log_settings=[lex.CfnBot.AudioLogSettingProperty(
                        destination=lex.CfnBot.AudioLogDestinationProperty(
                            s3_bucket=lex.CfnBot.S3BucketLogDestinationProperty(
                                log_prefix="logPrefix",
                                s3_bucket_arn="s3BucketArn",
                
                                # the properties below are optional
                                kms_key_arn="kmsKeyArn"
                            )
                        ),
                        enabled=False
                    )],
                    text_log_settings=[lex.CfnBot.TextLogSettingProperty(
                        destination=lex.CfnBot.TextLogDestinationProperty(
                            cloud_watch=lex.CfnBot.CloudWatchLogGroupLogDestinationProperty(
                                cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                                log_prefix="logPrefix"
                            )
                        ),
                        enabled=False
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fadbc804342400e1fe72580d2c49c87b48a4dcb178861f1caaff4692f0fc551a)
                check_type(argname="argument audio_log_settings", value=audio_log_settings, expected_type=type_hints["audio_log_settings"])
                check_type(argname="argument text_log_settings", value=text_log_settings, expected_type=type_hints["text_log_settings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if audio_log_settings is not None:
                self._values["audio_log_settings"] = audio_log_settings
            if text_log_settings is not None:
                self._values["text_log_settings"] = text_log_settings

        @builtins.property
        def audio_log_settings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.AudioLogSettingProperty"]]]]:
            '''The Amazon S3 settings for logging audio to an S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-conversationlogsettings.html#cfn-lex-bot-conversationlogsettings-audiologsettings
            '''
            result = self._values.get("audio_log_settings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.AudioLogSettingProperty"]]]], result)

        @builtins.property
        def text_log_settings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.TextLogSettingProperty"]]]]:
            '''The Amazon CloudWatch Logs settings for logging text and metadata.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-conversationlogsettings.html#cfn-lex-bot-conversationlogsettings-textlogsettings
            '''
            result = self._values.get("text_log_settings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.TextLogSettingProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConversationLogSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.CustomPayloadProperty",
        jsii_struct_bases=[],
        name_mapping={"value": "value"},
    )
    class CustomPayloadProperty:
        def __init__(self, *, value: builtins.str) -> None:
            '''A custom response string that Amazon Lex sends to your application.

            You define the content and structure the string.

            :param value: The string that is sent to your application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-custompayload.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                custom_payload_property = lex.CfnBot.CustomPayloadProperty(
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__63c440afe8abb656f1b6b5cc4bdf73214fb7e5ec559d4ecaceee87d143691138)
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "value": value,
            }

        @builtins.property
        def value(self) -> builtins.str:
            '''The string that is sent to your application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-custompayload.html#cfn-lex-bot-custompayload-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomPayloadProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.CustomVocabularyItemProperty",
        jsii_struct_bases=[],
        name_mapping={
            "phrase": "phrase",
            "display_as": "displayAs",
            "weight": "weight",
        },
    )
    class CustomVocabularyItemProperty:
        def __init__(
            self,
            *,
            phrase: builtins.str,
            display_as: typing.Optional[builtins.str] = None,
            weight: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Specifies an entry in a custom vocabulary.

            :param phrase: Specifies 1 - 4 words that should be recognized.
            :param display_as: The DisplayAs value for the custom vocabulary item from the custom vocabulary list.
            :param weight: Specifies the degree to which the phrase recognition is boosted. The default value is 1.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-customvocabularyitem.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                custom_vocabulary_item_property = lex.CfnBot.CustomVocabularyItemProperty(
                    phrase="phrase",
                
                    # the properties below are optional
                    display_as="displayAs",
                    weight=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2fdc21221bc0867aec831c3ffab8dd3d47a44075876c837b023a9eecc83af7ee)
                check_type(argname="argument phrase", value=phrase, expected_type=type_hints["phrase"])
                check_type(argname="argument display_as", value=display_as, expected_type=type_hints["display_as"])
                check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "phrase": phrase,
            }
            if display_as is not None:
                self._values["display_as"] = display_as
            if weight is not None:
                self._values["weight"] = weight

        @builtins.property
        def phrase(self) -> builtins.str:
            '''Specifies 1 - 4 words that should be recognized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-customvocabularyitem.html#cfn-lex-bot-customvocabularyitem-phrase
            '''
            result = self._values.get("phrase")
            assert result is not None, "Required property 'phrase' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def display_as(self) -> typing.Optional[builtins.str]:
            '''The DisplayAs value for the custom vocabulary item from the custom vocabulary list.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-customvocabularyitem.html#cfn-lex-bot-customvocabularyitem-displayas
            '''
            result = self._values.get("display_as")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def weight(self) -> typing.Optional[jsii.Number]:
            '''Specifies the degree to which the phrase recognition is boosted.

            The default value is 1.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-customvocabularyitem.html#cfn-lex-bot-customvocabularyitem-weight
            '''
            result = self._values.get("weight")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomVocabularyItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.CustomVocabularyProperty",
        jsii_struct_bases=[],
        name_mapping={"custom_vocabulary_items": "customVocabularyItems"},
    )
    class CustomVocabularyProperty:
        def __init__(
            self,
            *,
            custom_vocabulary_items: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.CustomVocabularyItemProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Specifies a custom vocabulary.

            A custom vocabulary is a list of words that you expect to be used during a conversation with your bot.

            :param custom_vocabulary_items: Specifies a list of words that you expect to be used during a conversation with your bot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-customvocabulary.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                custom_vocabulary_property = lex.CfnBot.CustomVocabularyProperty(
                    custom_vocabulary_items=[lex.CfnBot.CustomVocabularyItemProperty(
                        phrase="phrase",
                
                        # the properties below are optional
                        display_as="displayAs",
                        weight=123
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fb16bf8e83aadced4f623ac7b6a54e675fb78bc9a1a5a9aec3fa5a5f1e63a1bb)
                check_type(argname="argument custom_vocabulary_items", value=custom_vocabulary_items, expected_type=type_hints["custom_vocabulary_items"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "custom_vocabulary_items": custom_vocabulary_items,
            }

        @builtins.property
        def custom_vocabulary_items(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.CustomVocabularyItemProperty"]]]:
            '''Specifies a list of words that you expect to be used during a conversation with your bot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-customvocabulary.html#cfn-lex-bot-customvocabulary-customvocabularyitems
            '''
            result = self._values.get("custom_vocabulary_items")
            assert result is not None, "Required property 'custom_vocabulary_items' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.CustomVocabularyItemProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomVocabularyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.DTMFSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "deletion_character": "deletionCharacter",
            "end_character": "endCharacter",
            "end_timeout_ms": "endTimeoutMs",
            "max_length": "maxLength",
        },
    )
    class DTMFSpecificationProperty:
        def __init__(
            self,
            *,
            deletion_character: builtins.str,
            end_character: builtins.str,
            end_timeout_ms: jsii.Number,
            max_length: jsii.Number,
        ) -> None:
            '''Specifies the DTMF input specifications.

            :param deletion_character: The DTMF character that clears the accumulated DTMF digits and immediately ends the input.
            :param end_character: The DTMF character that immediately ends input. If the user does not press this character, the input ends after the end timeout.
            :param end_timeout_ms: How long the bot should wait after the last DTMF character input before assuming that the input has concluded.
            :param max_length: The maximum number of DTMF digits allowed in an utterance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dtmfspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                d_tMFSpecification_property = lex.CfnBot.DTMFSpecificationProperty(
                    deletion_character="deletionCharacter",
                    end_character="endCharacter",
                    end_timeout_ms=123,
                    max_length=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0381b9c530c5df0d1792837611cfb9e0aabde7240383f67b78c9378632b3c2dc)
                check_type(argname="argument deletion_character", value=deletion_character, expected_type=type_hints["deletion_character"])
                check_type(argname="argument end_character", value=end_character, expected_type=type_hints["end_character"])
                check_type(argname="argument end_timeout_ms", value=end_timeout_ms, expected_type=type_hints["end_timeout_ms"])
                check_type(argname="argument max_length", value=max_length, expected_type=type_hints["max_length"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "deletion_character": deletion_character,
                "end_character": end_character,
                "end_timeout_ms": end_timeout_ms,
                "max_length": max_length,
            }

        @builtins.property
        def deletion_character(self) -> builtins.str:
            '''The DTMF character that clears the accumulated DTMF digits and immediately ends the input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dtmfspecification.html#cfn-lex-bot-dtmfspecification-deletioncharacter
            '''
            result = self._values.get("deletion_character")
            assert result is not None, "Required property 'deletion_character' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def end_character(self) -> builtins.str:
            '''The DTMF character that immediately ends input.

            If the user does not press this character, the input ends after the end timeout.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dtmfspecification.html#cfn-lex-bot-dtmfspecification-endcharacter
            '''
            result = self._values.get("end_character")
            assert result is not None, "Required property 'end_character' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def end_timeout_ms(self) -> jsii.Number:
            '''How long the bot should wait after the last DTMF character input before assuming that the input has concluded.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dtmfspecification.html#cfn-lex-bot-dtmfspecification-endtimeoutms
            '''
            result = self._values.get("end_timeout_ms")
            assert result is not None, "Required property 'end_timeout_ms' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def max_length(self) -> jsii.Number:
            '''The maximum number of DTMF digits allowed in an utterance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dtmfspecification.html#cfn-lex-bot-dtmfspecification-maxlength
            '''
            result = self._values.get("max_length")
            assert result is not None, "Required property 'max_length' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DTMFSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.DataPrivacyProperty",
        jsii_struct_bases=[],
        name_mapping={"child_directed": "childDirected"},
    )
    class DataPrivacyProperty:
        def __init__(
            self,
            *,
            child_directed: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''By default, data stored by Amazon Lex is encrypted.

            The ``DataPrivacy`` structure provides settings that determine how Amazon Lex handles special cases of securing the data for your bot.

            :param child_directed: For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to the Children's Online Privacy Protection Act (COPPA) by specifying ``true`` or ``false`` in the ``childDirected`` field. By specifying ``true`` in the ``childDirected`` field, you confirm that your use of Amazon Lex *is* related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. By specifying ``false`` in the ``childDirected`` field, you confirm that your use of Amazon Lex *is not* related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not specify a default value for the ``childDirected`` field that does not accurately reflect whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. If your use of Amazon Lex relates to a website, program, or other application that is directed in whole or in part, to children under age 13, you must obtain any required verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in connection with websites, programs, or other applications that are directed or targeted, in whole or in part, to children under age 13, see the `Amazon Lex FAQ <https://docs.aws.amazon.com/lex/faqs#data-security>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dataprivacy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                data_privacy_property = lex.CfnBot.DataPrivacyProperty(
                    child_directed=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8413726661c5259fdaa87f5eb1adab8b9e36f411a5b42163e14d40d5aca25121)
                check_type(argname="argument child_directed", value=child_directed, expected_type=type_hints["child_directed"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "child_directed": child_directed,
            }

        @builtins.property
        def child_directed(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to the Children's Online Privacy Protection Act (COPPA) by specifying ``true`` or ``false`` in the ``childDirected`` field.

            By specifying ``true`` in the ``childDirected`` field, you confirm that your use of Amazon Lex *is* related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. By specifying ``false`` in the ``childDirected`` field, you confirm that your use of Amazon Lex *is not* related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not specify a default value for the ``childDirected`` field that does not accurately reflect whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. If your use of Amazon Lex relates to a website, program, or other application that is directed in whole or in part, to children under age 13, you must obtain any required verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in connection with websites, programs, or other applications that are directed or targeted, in whole or in part, to children under age 13, see the `Amazon Lex FAQ <https://docs.aws.amazon.com/lex/faqs#data-security>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dataprivacy.html#cfn-lex-bot-dataprivacy-childdirected
            '''
            result = self._values.get("child_directed")
            assert result is not None, "Required property 'child_directed' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataPrivacyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.DefaultConditionalBranchProperty",
        jsii_struct_bases=[],
        name_mapping={"next_step": "nextStep", "response": "response"},
    )
    class DefaultConditionalBranchProperty:
        def __init__(
            self,
            *,
            next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.DialogStateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ResponseSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A set of actions that Amazon Lex should run if none of the other conditions are met.

            :param next_step: The next step in the conversation.
            :param response: Specifies a list of message groups that Amazon Lex uses to respond the user input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-defaultconditionalbranch.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                # slot_value_override_property_: lex.CfnBot.SlotValueOverrideProperty
                
                default_conditional_branch_property = lex.CfnBot.DefaultConditionalBranchProperty(
                    next_step=lex.CfnBot.DialogStateProperty(
                        dialog_action=lex.CfnBot.DialogActionProperty(
                            type="type",
                
                            # the properties below are optional
                            slot_to_elicit="slotToElicit",
                            suppress_next_message=False
                        ),
                        intent=lex.CfnBot.IntentOverrideProperty(
                            name="name",
                            slots=[lex.CfnBot.SlotValueOverrideMapProperty(
                                slot_name="slotName",
                                slot_value_override=lex.CfnBot.SlotValueOverrideProperty(
                                    shape="shape",
                                    value=lex.CfnBot.SlotValueProperty(
                                        interpreted_value="interpretedValue"
                                    ),
                                    values=[slot_value_override_property_]
                                )
                            )]
                        ),
                        session_attributes=[lex.CfnBot.SessionAttributeProperty(
                            key="key",
                
                            # the properties below are optional
                            value="value"
                        )]
                    ),
                    response=lex.CfnBot.ResponseSpecificationProperty(
                        message_groups_list=[lex.CfnBot.MessageGroupProperty(
                            message=lex.CfnBot.MessageProperty(
                                custom_payload=lex.CfnBot.CustomPayloadProperty(
                                    value="value"
                                ),
                                image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                    title="title",
                
                                    # the properties below are optional
                                    buttons=[lex.CfnBot.ButtonProperty(
                                        text="text",
                                        value="value"
                                    )],
                                    image_url="imageUrl",
                                    subtitle="subtitle"
                                ),
                                plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                    value="value"
                                ),
                                ssml_message=lex.CfnBot.SSMLMessageProperty(
                                    value="value"
                                )
                            ),
                
                            # the properties below are optional
                            variations=[lex.CfnBot.MessageProperty(
                                custom_payload=lex.CfnBot.CustomPayloadProperty(
                                    value="value"
                                ),
                                image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                    title="title",
                
                                    # the properties below are optional
                                    buttons=[lex.CfnBot.ButtonProperty(
                                        text="text",
                                        value="value"
                                    )],
                                    image_url="imageUrl",
                                    subtitle="subtitle"
                                ),
                                plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                    value="value"
                                ),
                                ssml_message=lex.CfnBot.SSMLMessageProperty(
                                    value="value"
                                )
                            )]
                        )],
                
                        # the properties below are optional
                        allow_interrupt=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b17d7f375530a3080dd7a04795acd6231e37882d54e677880209844b34b66963)
                check_type(argname="argument next_step", value=next_step, expected_type=type_hints["next_step"])
                check_type(argname="argument response", value=response, expected_type=type_hints["response"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if next_step is not None:
                self._values["next_step"] = next_step
            if response is not None:
                self._values["response"] = response

        @builtins.property
        def next_step(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]]:
            '''The next step in the conversation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-defaultconditionalbranch.html#cfn-lex-bot-defaultconditionalbranch-nextstep
            '''
            result = self._values.get("next_step")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]], result)

        @builtins.property
        def response(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]]:
            '''Specifies a list of message groups that Amazon Lex uses to respond the user input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-defaultconditionalbranch.html#cfn-lex-bot-defaultconditionalbranch-response
            '''
            result = self._values.get("response")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DefaultConditionalBranchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.DialogActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "type": "type",
            "slot_to_elicit": "slotToElicit",
            "suppress_next_message": "suppressNextMessage",
        },
    )
    class DialogActionProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            slot_to_elicit: typing.Optional[builtins.str] = None,
            suppress_next_message: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Defines the action that the bot executes at runtime when the conversation reaches this step.

            :param type: The action that the bot should execute.
            :param slot_to_elicit: If the dialog action is ``ElicitSlot`` , defines the slot to elicit from the user.
            :param suppress_next_message: When true the next message for the intent is not used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                dialog_action_property = lex.CfnBot.DialogActionProperty(
                    type="type",
                
                    # the properties below are optional
                    slot_to_elicit="slotToElicit",
                    suppress_next_message=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e376869d573dbc5f07a8bacbcb08139f9ccf20789d86cfdc88afd3db242dd177)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument slot_to_elicit", value=slot_to_elicit, expected_type=type_hints["slot_to_elicit"])
                check_type(argname="argument suppress_next_message", value=suppress_next_message, expected_type=type_hints["suppress_next_message"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if slot_to_elicit is not None:
                self._values["slot_to_elicit"] = slot_to_elicit
            if suppress_next_message is not None:
                self._values["suppress_next_message"] = suppress_next_message

        @builtins.property
        def type(self) -> builtins.str:
            '''The action that the bot should execute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogaction.html#cfn-lex-bot-dialogaction-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def slot_to_elicit(self) -> typing.Optional[builtins.str]:
            '''If the dialog action is ``ElicitSlot`` , defines the slot to elicit from the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogaction.html#cfn-lex-bot-dialogaction-slottoelicit
            '''
            result = self._values.get("slot_to_elicit")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def suppress_next_message(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When true the next message for the intent is not used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogaction.html#cfn-lex-bot-dialogaction-suppressnextmessage
            '''
            result = self._values.get("suppress_next_message")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DialogActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.DialogCodeHookInvocationSettingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_code_hook_invocation": "enableCodeHookInvocation",
            "is_active": "isActive",
            "post_code_hook_specification": "postCodeHookSpecification",
            "invocation_label": "invocationLabel",
        },
    )
    class DialogCodeHookInvocationSettingProperty:
        def __init__(
            self,
            *,
            enable_code_hook_invocation: typing.Union[builtins.bool, _IResolvable_da3f097b],
            is_active: typing.Union[builtins.bool, _IResolvable_da3f097b],
            post_code_hook_specification: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.PostDialogCodeHookInvocationSpecificationProperty", typing.Dict[builtins.str, typing.Any]]],
            invocation_label: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Settings that specify the dialog code hook that is called by Amazon Lex at a step of the conversation.

            :param enable_code_hook_invocation: Indicates whether a Lambda function should be invoked for the dialog.
            :param is_active: Determines whether a dialog code hook is used when the intent is activated.
            :param post_code_hook_specification: Contains the responses and actions that Amazon Lex takes after the Lambda function is complete.
            :param invocation_label: A label that indicates the dialog step from which the dialog code hook is happening.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogcodehookinvocationsetting.html
            :exampleMetadata: fixture=_generated

            Example::

                
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e19b7a3cd9426f9feac0cd76771e4f412c686860e6db49495e9732e3e2c2e2ad)
                check_type(argname="argument enable_code_hook_invocation", value=enable_code_hook_invocation, expected_type=type_hints["enable_code_hook_invocation"])
                check_type(argname="argument is_active", value=is_active, expected_type=type_hints["is_active"])
                check_type(argname="argument post_code_hook_specification", value=post_code_hook_specification, expected_type=type_hints["post_code_hook_specification"])
                check_type(argname="argument invocation_label", value=invocation_label, expected_type=type_hints["invocation_label"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enable_code_hook_invocation": enable_code_hook_invocation,
                "is_active": is_active,
                "post_code_hook_specification": post_code_hook_specification,
            }
            if invocation_label is not None:
                self._values["invocation_label"] = invocation_label

        @builtins.property
        def enable_code_hook_invocation(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether a Lambda function should be invoked for the dialog.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogcodehookinvocationsetting.html#cfn-lex-bot-dialogcodehookinvocationsetting-enablecodehookinvocation
            '''
            result = self._values.get("enable_code_hook_invocation")
            assert result is not None, "Required property 'enable_code_hook_invocation' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def is_active(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Determines whether a dialog code hook is used when the intent is activated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogcodehookinvocationsetting.html#cfn-lex-bot-dialogcodehookinvocationsetting-isactive
            '''
            result = self._values.get("is_active")
            assert result is not None, "Required property 'is_active' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def post_code_hook_specification(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnBot.PostDialogCodeHookInvocationSpecificationProperty"]:
            '''Contains the responses and actions that Amazon Lex takes after the Lambda function is complete.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogcodehookinvocationsetting.html#cfn-lex-bot-dialogcodehookinvocationsetting-postcodehookspecification
            '''
            result = self._values.get("post_code_hook_specification")
            assert result is not None, "Required property 'post_code_hook_specification' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBot.PostDialogCodeHookInvocationSpecificationProperty"], result)

        @builtins.property
        def invocation_label(self) -> typing.Optional[builtins.str]:
            '''A label that indicates the dialog step from which the dialog code hook is happening.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogcodehookinvocationsetting.html#cfn-lex-bot-dialogcodehookinvocationsetting-invocationlabel
            '''
            result = self._values.get("invocation_label")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DialogCodeHookInvocationSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.DialogCodeHookSettingProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class DialogCodeHookSettingProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''Settings that determine the Lambda function that Amazon Lex uses for processing user responses.

            :param enabled: Enables the dialog code hook so that it processes user requests.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogcodehooksetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                dialog_code_hook_setting_property = lex.CfnBot.DialogCodeHookSettingProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fcf037ef78d32218b7b41dd7215a0c084b74ce9ea1d291027573be2d214e57f4)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled": enabled,
            }

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Enables the dialog code hook so that it processes user requests.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogcodehooksetting.html#cfn-lex-bot-dialogcodehooksetting-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DialogCodeHookSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.DialogStateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dialog_action": "dialogAction",
            "intent": "intent",
            "session_attributes": "sessionAttributes",
        },
    )
    class DialogStateProperty:
        def __init__(
            self,
            *,
            dialog_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.DialogActionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            intent: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.IntentOverrideProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            session_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.SessionAttributeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The current state of the conversation with the user.

            :param dialog_action: Defines the action that the bot executes at runtime when the conversation reaches this step.
            :param intent: Override settings to configure the intent state.
            :param session_attributes: Map of key/value pairs representing session-specific context information. It contains application information passed between Amazon Lex and a client application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogstate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                # slot_value_override_property_: lex.CfnBot.SlotValueOverrideProperty
                
                dialog_state_property = lex.CfnBot.DialogStateProperty(
                    dialog_action=lex.CfnBot.DialogActionProperty(
                        type="type",
                
                        # the properties below are optional
                        slot_to_elicit="slotToElicit",
                        suppress_next_message=False
                    ),
                    intent=lex.CfnBot.IntentOverrideProperty(
                        name="name",
                        slots=[lex.CfnBot.SlotValueOverrideMapProperty(
                            slot_name="slotName",
                            slot_value_override=lex.CfnBot.SlotValueOverrideProperty(
                                shape="shape",
                                value=lex.CfnBot.SlotValueProperty(
                                    interpreted_value="interpretedValue"
                                ),
                                values=[slot_value_override_property_]
                            )
                        )]
                    ),
                    session_attributes=[lex.CfnBot.SessionAttributeProperty(
                        key="key",
                
                        # the properties below are optional
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8c7dde88739182f4b4a30f1ef8b12c227c3e086e46bea8e39b20f1c51623d165)
                check_type(argname="argument dialog_action", value=dialog_action, expected_type=type_hints["dialog_action"])
                check_type(argname="argument intent", value=intent, expected_type=type_hints["intent"])
                check_type(argname="argument session_attributes", value=session_attributes, expected_type=type_hints["session_attributes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dialog_action is not None:
                self._values["dialog_action"] = dialog_action
            if intent is not None:
                self._values["intent"] = intent
            if session_attributes is not None:
                self._values["session_attributes"] = session_attributes

        @builtins.property
        def dialog_action(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogActionProperty"]]:
            '''Defines the action that the bot executes at runtime when the conversation reaches this step.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogstate.html#cfn-lex-bot-dialogstate-dialogaction
            '''
            result = self._values.get("dialog_action")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogActionProperty"]], result)

        @builtins.property
        def intent(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.IntentOverrideProperty"]]:
            '''Override settings to configure the intent state.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogstate.html#cfn-lex-bot-dialogstate-intent
            '''
            result = self._values.get("intent")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.IntentOverrideProperty"]], result)

        @builtins.property
        def session_attributes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.SessionAttributeProperty"]]]]:
            '''Map of key/value pairs representing session-specific context information.

            It contains application information passed between Amazon Lex and a client application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-dialogstate.html#cfn-lex-bot-dialogstate-sessionattributes
            '''
            result = self._values.get("session_attributes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.SessionAttributeProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DialogStateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.ElicitationCodeHookInvocationSettingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_code_hook_invocation": "enableCodeHookInvocation",
            "invocation_label": "invocationLabel",
        },
    )
    class ElicitationCodeHookInvocationSettingProperty:
        def __init__(
            self,
            *,
            enable_code_hook_invocation: typing.Union[builtins.bool, _IResolvable_da3f097b],
            invocation_label: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Settings that specify the dialog code hook that is called by Amazon Lex between eliciting slot values.

            :param enable_code_hook_invocation: Indicates whether a Lambda function should be invoked for the dialog.
            :param invocation_label: A label that indicates the dialog step from which the dialog code hook is happening.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-elicitationcodehookinvocationsetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                elicitation_code_hook_invocation_setting_property = lex.CfnBot.ElicitationCodeHookInvocationSettingProperty(
                    enable_code_hook_invocation=False,
                
                    # the properties below are optional
                    invocation_label="invocationLabel"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__60b6686b2f7d08316ec6f3906c1eb41b85065d8e1d623e4ccb84213bea7eb37e)
                check_type(argname="argument enable_code_hook_invocation", value=enable_code_hook_invocation, expected_type=type_hints["enable_code_hook_invocation"])
                check_type(argname="argument invocation_label", value=invocation_label, expected_type=type_hints["invocation_label"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enable_code_hook_invocation": enable_code_hook_invocation,
            }
            if invocation_label is not None:
                self._values["invocation_label"] = invocation_label

        @builtins.property
        def enable_code_hook_invocation(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether a Lambda function should be invoked for the dialog.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-elicitationcodehookinvocationsetting.html#cfn-lex-bot-elicitationcodehookinvocationsetting-enablecodehookinvocation
            '''
            result = self._values.get("enable_code_hook_invocation")
            assert result is not None, "Required property 'enable_code_hook_invocation' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def invocation_label(self) -> typing.Optional[builtins.str]:
            '''A label that indicates the dialog step from which the dialog code hook is happening.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-elicitationcodehookinvocationsetting.html#cfn-lex-bot-elicitationcodehookinvocationsetting-invocationlabel
            '''
            result = self._values.get("invocation_label")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ElicitationCodeHookInvocationSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.ExternalSourceSettingProperty",
        jsii_struct_bases=[],
        name_mapping={"grammar_slot_type_setting": "grammarSlotTypeSetting"},
    )
    class ExternalSourceSettingProperty:
        def __init__(
            self,
            *,
            grammar_slot_type_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.GrammarSlotTypeSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Provides information about the external source of the slot type's definition.

            :param grammar_slot_type_setting: Settings required for a slot type based on a grammar that you provide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-externalsourcesetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                external_source_setting_property = lex.CfnBot.ExternalSourceSettingProperty(
                    grammar_slot_type_setting=lex.CfnBot.GrammarSlotTypeSettingProperty(
                        source=lex.CfnBot.GrammarSlotTypeSourceProperty(
                            s3_bucket_name="s3BucketName",
                            s3_object_key="s3ObjectKey",
                
                            # the properties below are optional
                            kms_key_arn="kmsKeyArn"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__88fba332915fbf5259a0c253d1363ad0ff0183417cfced04eef9822b50aecb7a)
                check_type(argname="argument grammar_slot_type_setting", value=grammar_slot_type_setting, expected_type=type_hints["grammar_slot_type_setting"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if grammar_slot_type_setting is not None:
                self._values["grammar_slot_type_setting"] = grammar_slot_type_setting

        @builtins.property
        def grammar_slot_type_setting(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.GrammarSlotTypeSettingProperty"]]:
            '''Settings required for a slot type based on a grammar that you provide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-externalsourcesetting.html#cfn-lex-bot-externalsourcesetting-grammarslottypesetting
            '''
            result = self._values.get("grammar_slot_type_setting")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.GrammarSlotTypeSettingProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExternalSourceSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.FulfillmentCodeHookSettingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "fulfillment_updates_specification": "fulfillmentUpdatesSpecification",
            "is_active": "isActive",
            "post_fulfillment_status_specification": "postFulfillmentStatusSpecification",
        },
    )
    class FulfillmentCodeHookSettingProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
            fulfillment_updates_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.FulfillmentUpdatesSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            is_active: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            post_fulfillment_status_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.PostFulfillmentStatusSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Determines if a Lambda function should be invoked for a specific intent.

            :param enabled: Indicates whether a Lambda function should be invoked to fulfill a specific intent.
            :param fulfillment_updates_specification: Provides settings for update messages sent to the user for long-running Lambda fulfillment functions. Fulfillment updates can be used only with streaming conversations.
            :param is_active: Determines whether the fulfillment code hook is used. When ``active`` is false, the code hook doesn't run.
            :param post_fulfillment_status_specification: Provides settings for messages sent to the user for after the Lambda fulfillment function completes. Post-fulfillment messages can be sent for both streaming and non-streaming conversations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentcodehooksetting.html
            :exampleMetadata: fixture=_generated

            Example::

                
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__05de122265994f52129837a3bda602f910b4b269167e3110405de9650ec1b200)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument fulfillment_updates_specification", value=fulfillment_updates_specification, expected_type=type_hints["fulfillment_updates_specification"])
                check_type(argname="argument is_active", value=is_active, expected_type=type_hints["is_active"])
                check_type(argname="argument post_fulfillment_status_specification", value=post_fulfillment_status_specification, expected_type=type_hints["post_fulfillment_status_specification"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled": enabled,
            }
            if fulfillment_updates_specification is not None:
                self._values["fulfillment_updates_specification"] = fulfillment_updates_specification
            if is_active is not None:
                self._values["is_active"] = is_active
            if post_fulfillment_status_specification is not None:
                self._values["post_fulfillment_status_specification"] = post_fulfillment_status_specification

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Indicates whether a Lambda function should be invoked to fulfill a specific intent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentcodehooksetting.html#cfn-lex-bot-fulfillmentcodehooksetting-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def fulfillment_updates_specification(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.FulfillmentUpdatesSpecificationProperty"]]:
            '''Provides settings for update messages sent to the user for long-running Lambda fulfillment functions.

            Fulfillment updates can be used only with streaming conversations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentcodehooksetting.html#cfn-lex-bot-fulfillmentcodehooksetting-fulfillmentupdatesspecification
            '''
            result = self._values.get("fulfillment_updates_specification")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.FulfillmentUpdatesSpecificationProperty"]], result)

        @builtins.property
        def is_active(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Determines whether the fulfillment code hook is used.

            When ``active`` is false, the code hook doesn't run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentcodehooksetting.html#cfn-lex-bot-fulfillmentcodehooksetting-isactive
            '''
            result = self._values.get("is_active")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def post_fulfillment_status_specification(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.PostFulfillmentStatusSpecificationProperty"]]:
            '''Provides settings for messages sent to the user for after the Lambda fulfillment function completes.

            Post-fulfillment messages can be sent for both streaming and non-streaming conversations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentcodehooksetting.html#cfn-lex-bot-fulfillmentcodehooksetting-postfulfillmentstatusspecification
            '''
            result = self._values.get("post_fulfillment_status_specification")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.PostFulfillmentStatusSpecificationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FulfillmentCodeHookSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.FulfillmentStartResponseSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delay_in_seconds": "delayInSeconds",
            "message_groups": "messageGroups",
            "allow_interrupt": "allowInterrupt",
        },
    )
    class FulfillmentStartResponseSpecificationProperty:
        def __init__(
            self,
            *,
            delay_in_seconds: jsii.Number,
            message_groups: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.MessageGroupProperty", typing.Dict[builtins.str, typing.Any]]]]],
            allow_interrupt: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Provides settings for a message that is sent to the user when a fulfillment Lambda function starts running.

            :param delay_in_seconds: The delay between when the Lambda fulfillment function starts running and the start message is played. If the Lambda function returns before the delay is over, the start message isn't played.
            :param message_groups: 1 - 5 message groups that contain start messages. Amazon Lex chooses one of the messages to play to the user.
            :param allow_interrupt: Determines whether the user can interrupt the start message while it is playing.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentstartresponsespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                fulfillment_start_response_specification_property = lex.CfnBot.FulfillmentStartResponseSpecificationProperty(
                    delay_in_seconds=123,
                    message_groups=[lex.CfnBot.MessageGroupProperty(
                        message=lex.CfnBot.MessageProperty(
                            custom_payload=lex.CfnBot.CustomPayloadProperty(
                                value="value"
                            ),
                            image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                title="title",
                
                                # the properties below are optional
                                buttons=[lex.CfnBot.ButtonProperty(
                                    text="text",
                                    value="value"
                                )],
                                image_url="imageUrl",
                                subtitle="subtitle"
                            ),
                            plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                value="value"
                            ),
                            ssml_message=lex.CfnBot.SSMLMessageProperty(
                                value="value"
                            )
                        ),
                
                        # the properties below are optional
                        variations=[lex.CfnBot.MessageProperty(
                            custom_payload=lex.CfnBot.CustomPayloadProperty(
                                value="value"
                            ),
                            image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                title="title",
                
                                # the properties below are optional
                                buttons=[lex.CfnBot.ButtonProperty(
                                    text="text",
                                    value="value"
                                )],
                                image_url="imageUrl",
                                subtitle="subtitle"
                            ),
                            plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                value="value"
                            ),
                            ssml_message=lex.CfnBot.SSMLMessageProperty(
                                value="value"
                            )
                        )]
                    )],
                
                    # the properties below are optional
                    allow_interrupt=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e3c656f733b90fca865d240233e420cba1e6738d89391b29144453b4d799898f)
                check_type(argname="argument delay_in_seconds", value=delay_in_seconds, expected_type=type_hints["delay_in_seconds"])
                check_type(argname="argument message_groups", value=message_groups, expected_type=type_hints["message_groups"])
                check_type(argname="argument allow_interrupt", value=allow_interrupt, expected_type=type_hints["allow_interrupt"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "delay_in_seconds": delay_in_seconds,
                "message_groups": message_groups,
            }
            if allow_interrupt is not None:
                self._values["allow_interrupt"] = allow_interrupt

        @builtins.property
        def delay_in_seconds(self) -> jsii.Number:
            '''The delay between when the Lambda fulfillment function starts running and the start message is played.

            If the Lambda function returns before the delay is over, the start message isn't played.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentstartresponsespecification.html#cfn-lex-bot-fulfillmentstartresponsespecification-delayinseconds
            '''
            result = self._values.get("delay_in_seconds")
            assert result is not None, "Required property 'delay_in_seconds' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def message_groups(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.MessageGroupProperty"]]]:
            '''1 - 5 message groups that contain start messages.

            Amazon Lex chooses one of the messages to play to the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentstartresponsespecification.html#cfn-lex-bot-fulfillmentstartresponsespecification-messagegroups
            '''
            result = self._values.get("message_groups")
            assert result is not None, "Required property 'message_groups' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.MessageGroupProperty"]]], result)

        @builtins.property
        def allow_interrupt(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Determines whether the user can interrupt the start message while it is playing.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentstartresponsespecification.html#cfn-lex-bot-fulfillmentstartresponsespecification-allowinterrupt
            '''
            result = self._values.get("allow_interrupt")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FulfillmentStartResponseSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.FulfillmentUpdateResponseSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "frequency_in_seconds": "frequencyInSeconds",
            "message_groups": "messageGroups",
            "allow_interrupt": "allowInterrupt",
        },
    )
    class FulfillmentUpdateResponseSpecificationProperty:
        def __init__(
            self,
            *,
            frequency_in_seconds: jsii.Number,
            message_groups: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.MessageGroupProperty", typing.Dict[builtins.str, typing.Any]]]]],
            allow_interrupt: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Provides settings for a message that is sent periodically to the user while a fulfillment Lambda function is running.

            :param frequency_in_seconds: The frequency that a message is sent to the user. When the period ends, Amazon Lex chooses a message from the message groups and plays it to the user. If the fulfillment Lambda returns before the first period ends, an update message is not played to the user.
            :param message_groups: 1 - 5 message groups that contain update messages. Amazon Lex chooses one of the messages to play to the user.
            :param allow_interrupt: Determines whether the user can interrupt an update message while it is playing.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdateresponsespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                fulfillment_update_response_specification_property = lex.CfnBot.FulfillmentUpdateResponseSpecificationProperty(
                    frequency_in_seconds=123,
                    message_groups=[lex.CfnBot.MessageGroupProperty(
                        message=lex.CfnBot.MessageProperty(
                            custom_payload=lex.CfnBot.CustomPayloadProperty(
                                value="value"
                            ),
                            image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                title="title",
                
                                # the properties below are optional
                                buttons=[lex.CfnBot.ButtonProperty(
                                    text="text",
                                    value="value"
                                )],
                                image_url="imageUrl",
                                subtitle="subtitle"
                            ),
                            plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                value="value"
                            ),
                            ssml_message=lex.CfnBot.SSMLMessageProperty(
                                value="value"
                            )
                        ),
                
                        # the properties below are optional
                        variations=[lex.CfnBot.MessageProperty(
                            custom_payload=lex.CfnBot.CustomPayloadProperty(
                                value="value"
                            ),
                            image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                title="title",
                
                                # the properties below are optional
                                buttons=[lex.CfnBot.ButtonProperty(
                                    text="text",
                                    value="value"
                                )],
                                image_url="imageUrl",
                                subtitle="subtitle"
                            ),
                            plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                value="value"
                            ),
                            ssml_message=lex.CfnBot.SSMLMessageProperty(
                                value="value"
                            )
                        )]
                    )],
                
                    # the properties below are optional
                    allow_interrupt=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a875cefaa538cfe3904d9bce7ca2b745f46320a3cbb89881519d72278e20b2fd)
                check_type(argname="argument frequency_in_seconds", value=frequency_in_seconds, expected_type=type_hints["frequency_in_seconds"])
                check_type(argname="argument message_groups", value=message_groups, expected_type=type_hints["message_groups"])
                check_type(argname="argument allow_interrupt", value=allow_interrupt, expected_type=type_hints["allow_interrupt"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "frequency_in_seconds": frequency_in_seconds,
                "message_groups": message_groups,
            }
            if allow_interrupt is not None:
                self._values["allow_interrupt"] = allow_interrupt

        @builtins.property
        def frequency_in_seconds(self) -> jsii.Number:
            '''The frequency that a message is sent to the user.

            When the period ends, Amazon Lex chooses a message from the message groups and plays it to the user. If the fulfillment Lambda returns before the first period ends, an update message is not played to the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdateresponsespecification.html#cfn-lex-bot-fulfillmentupdateresponsespecification-frequencyinseconds
            '''
            result = self._values.get("frequency_in_seconds")
            assert result is not None, "Required property 'frequency_in_seconds' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def message_groups(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.MessageGroupProperty"]]]:
            '''1 - 5 message groups that contain update messages.

            Amazon Lex chooses one of the messages to play to the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdateresponsespecification.html#cfn-lex-bot-fulfillmentupdateresponsespecification-messagegroups
            '''
            result = self._values.get("message_groups")
            assert result is not None, "Required property 'message_groups' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.MessageGroupProperty"]]], result)

        @builtins.property
        def allow_interrupt(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Determines whether the user can interrupt an update message while it is playing.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdateresponsespecification.html#cfn-lex-bot-fulfillmentupdateresponsespecification-allowinterrupt
            '''
            result = self._values.get("allow_interrupt")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FulfillmentUpdateResponseSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.FulfillmentUpdatesSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "active": "active",
            "start_response": "startResponse",
            "timeout_in_seconds": "timeoutInSeconds",
            "update_response": "updateResponse",
        },
    )
    class FulfillmentUpdatesSpecificationProperty:
        def __init__(
            self,
            *,
            active: typing.Union[builtins.bool, _IResolvable_da3f097b],
            start_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.FulfillmentStartResponseSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            timeout_in_seconds: typing.Optional[jsii.Number] = None,
            update_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.FulfillmentUpdateResponseSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Provides information for updating the user on the progress of fulfilling an intent.

            :param active: Determines whether fulfillment updates are sent to the user. When this field is true, updates are sent. If the ``active`` field is set to true, the ``startResponse`` , ``updateResponse`` , and ``timeoutInSeconds`` fields are required.
            :param start_response: Provides configuration information for the message sent to users when the fulfillment Lambda functions starts running.
            :param timeout_in_seconds: The length of time that the fulfillment Lambda function should run before it times out.
            :param update_response: Provides configuration information for messages sent periodically to the user while the fulfillment Lambda function is running.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdatesspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                fulfillment_updates_specification_property = lex.CfnBot.FulfillmentUpdatesSpecificationProperty(
                    active=False,
                
                    # the properties below are optional
                    start_response=lex.CfnBot.FulfillmentStartResponseSpecificationProperty(
                        delay_in_seconds=123,
                        message_groups=[lex.CfnBot.MessageGroupProperty(
                            message=lex.CfnBot.MessageProperty(
                                custom_payload=lex.CfnBot.CustomPayloadProperty(
                                    value="value"
                                ),
                                image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                    title="title",
                
                                    # the properties below are optional
                                    buttons=[lex.CfnBot.ButtonProperty(
                                        text="text",
                                        value="value"
                                    )],
                                    image_url="imageUrl",
                                    subtitle="subtitle"
                                ),
                                plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                    value="value"
                                ),
                                ssml_message=lex.CfnBot.SSMLMessageProperty(
                                    value="value"
                                )
                            ),
                
                            # the properties below are optional
                            variations=[lex.CfnBot.MessageProperty(
                                custom_payload=lex.CfnBot.CustomPayloadProperty(
                                    value="value"
                                ),
                                image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                    title="title",
                
                                    # the properties below are optional
                                    buttons=[lex.CfnBot.ButtonProperty(
                                        text="text",
                                        value="value"
                                    )],
                                    image_url="imageUrl",
                                    subtitle="subtitle"
                                ),
                                plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                    value="value"
                                ),
                                ssml_message=lex.CfnBot.SSMLMessageProperty(
                                    value="value"
                                )
                            )]
                        )],
                
                        # the properties below are optional
                        allow_interrupt=False
                    ),
                    timeout_in_seconds=123,
                    update_response=lex.CfnBot.FulfillmentUpdateResponseSpecificationProperty(
                        frequency_in_seconds=123,
                        message_groups=[lex.CfnBot.MessageGroupProperty(
                            message=lex.CfnBot.MessageProperty(
                                custom_payload=lex.CfnBot.CustomPayloadProperty(
                                    value="value"
                                ),
                                image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                    title="title",
                
                                    # the properties below are optional
                                    buttons=[lex.CfnBot.ButtonProperty(
                                        text="text",
                                        value="value"
                                    )],
                                    image_url="imageUrl",
                                    subtitle="subtitle"
                                ),
                                plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                    value="value"
                                ),
                                ssml_message=lex.CfnBot.SSMLMessageProperty(
                                    value="value"
                                )
                            ),
                
                            # the properties below are optional
                            variations=[lex.CfnBot.MessageProperty(
                                custom_payload=lex.CfnBot.CustomPayloadProperty(
                                    value="value"
                                ),
                                image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                    title="title",
                
                                    # the properties below are optional
                                    buttons=[lex.CfnBot.ButtonProperty(
                                        text="text",
                                        value="value"
                                    )],
                                    image_url="imageUrl",
                                    subtitle="subtitle"
                                ),
                                plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                    value="value"
                                ),
                                ssml_message=lex.CfnBot.SSMLMessageProperty(
                                    value="value"
                                )
                            )]
                        )],
                
                        # the properties below are optional
                        allow_interrupt=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__500ed503fae8fece46360727878fdf9250149c5d237d5f4414d8191ffbb1cb55)
                check_type(argname="argument active", value=active, expected_type=type_hints["active"])
                check_type(argname="argument start_response", value=start_response, expected_type=type_hints["start_response"])
                check_type(argname="argument timeout_in_seconds", value=timeout_in_seconds, expected_type=type_hints["timeout_in_seconds"])
                check_type(argname="argument update_response", value=update_response, expected_type=type_hints["update_response"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "active": active,
            }
            if start_response is not None:
                self._values["start_response"] = start_response
            if timeout_in_seconds is not None:
                self._values["timeout_in_seconds"] = timeout_in_seconds
            if update_response is not None:
                self._values["update_response"] = update_response

        @builtins.property
        def active(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Determines whether fulfillment updates are sent to the user. When this field is true, updates are sent.

            If the ``active`` field is set to true, the ``startResponse`` , ``updateResponse`` , and ``timeoutInSeconds`` fields are required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdatesspecification.html#cfn-lex-bot-fulfillmentupdatesspecification-active
            '''
            result = self._values.get("active")
            assert result is not None, "Required property 'active' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def start_response(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.FulfillmentStartResponseSpecificationProperty"]]:
            '''Provides configuration information for the message sent to users when the fulfillment Lambda functions starts running.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdatesspecification.html#cfn-lex-bot-fulfillmentupdatesspecification-startresponse
            '''
            result = self._values.get("start_response")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.FulfillmentStartResponseSpecificationProperty"]], result)

        @builtins.property
        def timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The length of time that the fulfillment Lambda function should run before it times out.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdatesspecification.html#cfn-lex-bot-fulfillmentupdatesspecification-timeoutinseconds
            '''
            result = self._values.get("timeout_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def update_response(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.FulfillmentUpdateResponseSpecificationProperty"]]:
            '''Provides configuration information for messages sent periodically to the user while the fulfillment Lambda function is running.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-fulfillmentupdatesspecification.html#cfn-lex-bot-fulfillmentupdatesspecification-updateresponse
            '''
            result = self._values.get("update_response")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.FulfillmentUpdateResponseSpecificationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FulfillmentUpdatesSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.GrammarSlotTypeSettingProperty",
        jsii_struct_bases=[],
        name_mapping={"source": "source"},
    )
    class GrammarSlotTypeSettingProperty:
        def __init__(
            self,
            *,
            source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.GrammarSlotTypeSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Settings requried for a slot type based on a grammar that you provide.

            :param source: The source of the grammar used to create the slot type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-grammarslottypesetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                grammar_slot_type_setting_property = lex.CfnBot.GrammarSlotTypeSettingProperty(
                    source=lex.CfnBot.GrammarSlotTypeSourceProperty(
                        s3_bucket_name="s3BucketName",
                        s3_object_key="s3ObjectKey",
                
                        # the properties below are optional
                        kms_key_arn="kmsKeyArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7607729da805dba490266bfccf35e40fc22f0e3b3c4d78038e129d897dd21483)
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if source is not None:
                self._values["source"] = source

        @builtins.property
        def source(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.GrammarSlotTypeSourceProperty"]]:
            '''The source of the grammar used to create the slot type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-grammarslottypesetting.html#cfn-lex-bot-grammarslottypesetting-source
            '''
            result = self._values.get("source")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.GrammarSlotTypeSourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GrammarSlotTypeSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.GrammarSlotTypeSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "s3_bucket_name": "s3BucketName",
            "s3_object_key": "s3ObjectKey",
            "kms_key_arn": "kmsKeyArn",
        },
    )
    class GrammarSlotTypeSourceProperty:
        def __init__(
            self,
            *,
            s3_bucket_name: builtins.str,
            s3_object_key: builtins.str,
            kms_key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the Amazon S3 bucket name and location for the grammar that is the source for the slot type.

            :param s3_bucket_name: The name of the Amazon S3 bucket that contains the grammar source.
            :param s3_object_key: The path to the grammar in the Amazon S3 bucket.
            :param kms_key_arn: The AWS KMS key required to decrypt the contents of the grammar, if any.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-grammarslottypesource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                grammar_slot_type_source_property = lex.CfnBot.GrammarSlotTypeSourceProperty(
                    s3_bucket_name="s3BucketName",
                    s3_object_key="s3ObjectKey",
                
                    # the properties below are optional
                    kms_key_arn="kmsKeyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3a3142398a960ac78cf821387c99b655d930f71dfa164c7937ee4315b875aa78)
                check_type(argname="argument s3_bucket_name", value=s3_bucket_name, expected_type=type_hints["s3_bucket_name"])
                check_type(argname="argument s3_object_key", value=s3_object_key, expected_type=type_hints["s3_object_key"])
                check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3_bucket_name": s3_bucket_name,
                "s3_object_key": s3_object_key,
            }
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn

        @builtins.property
        def s3_bucket_name(self) -> builtins.str:
            '''The name of the Amazon S3 bucket that contains the grammar source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-grammarslottypesource.html#cfn-lex-bot-grammarslottypesource-s3bucketname
            '''
            result = self._values.get("s3_bucket_name")
            assert result is not None, "Required property 's3_bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_object_key(self) -> builtins.str:
            '''The path to the grammar in the Amazon S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-grammarslottypesource.html#cfn-lex-bot-grammarslottypesource-s3objectkey
            '''
            result = self._values.get("s3_object_key")
            assert result is not None, "Required property 's3_object_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''The AWS KMS key required to decrypt the contents of the grammar, if any.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-grammarslottypesource.html#cfn-lex-bot-grammarslottypesource-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GrammarSlotTypeSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.ImageResponseCardProperty",
        jsii_struct_bases=[],
        name_mapping={
            "title": "title",
            "buttons": "buttons",
            "image_url": "imageUrl",
            "subtitle": "subtitle",
        },
    )
    class ImageResponseCardProperty:
        def __init__(
            self,
            *,
            title: builtins.str,
            buttons: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ButtonProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            image_url: typing.Optional[builtins.str] = None,
            subtitle: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A card that is shown to the user by a messaging platform.

            You define the contents of the card, the card is displayed by the platform.

            When you use a response card, the response from the user is constrained to the text associated with a button on the card.

            :param title: The title to display on the response card. The format of the title is determined by the platform displaying the response card.
            :param buttons: A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.
            :param image_url: The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.
            :param subtitle: The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-imageresponsecard.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                image_response_card_property = lex.CfnBot.ImageResponseCardProperty(
                    title="title",
                
                    # the properties below are optional
                    buttons=[lex.CfnBot.ButtonProperty(
                        text="text",
                        value="value"
                    )],
                    image_url="imageUrl",
                    subtitle="subtitle"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a1ea1c8338736803aba15b8d47a2bb101596e1e5acf68885a2b6456ea5eef357)
                check_type(argname="argument title", value=title, expected_type=type_hints["title"])
                check_type(argname="argument buttons", value=buttons, expected_type=type_hints["buttons"])
                check_type(argname="argument image_url", value=image_url, expected_type=type_hints["image_url"])
                check_type(argname="argument subtitle", value=subtitle, expected_type=type_hints["subtitle"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "title": title,
            }
            if buttons is not None:
                self._values["buttons"] = buttons
            if image_url is not None:
                self._values["image_url"] = image_url
            if subtitle is not None:
                self._values["subtitle"] = subtitle

        @builtins.property
        def title(self) -> builtins.str:
            '''The title to display on the response card.

            The format of the title is determined by the platform displaying the response card.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-imageresponsecard.html#cfn-lex-bot-imageresponsecard-title
            '''
            result = self._values.get("title")
            assert result is not None, "Required property 'title' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def buttons(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.ButtonProperty"]]]]:
            '''A list of buttons that should be displayed on the response card.

            The arrangement of the buttons is determined by the platform that displays the button.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-imageresponsecard.html#cfn-lex-bot-imageresponsecard-buttons
            '''
            result = self._values.get("buttons")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.ButtonProperty"]]]], result)

        @builtins.property
        def image_url(self) -> typing.Optional[builtins.str]:
            '''The URL of an image to display on the response card.

            The image URL must be publicly available so that the platform displaying the response card has access to the image.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-imageresponsecard.html#cfn-lex-bot-imageresponsecard-imageurl
            '''
            result = self._values.get("image_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def subtitle(self) -> typing.Optional[builtins.str]:
            '''The subtitle to display on the response card.

            The format of the subtitle is determined by the platform displaying the response card.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-imageresponsecard.html#cfn-lex-bot-imageresponsecard-subtitle
            '''
            result = self._values.get("subtitle")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageResponseCardProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.InitialResponseSettingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "code_hook": "codeHook",
            "conditional": "conditional",
            "initial_response": "initialResponse",
            "next_step": "nextStep",
        },
    )
    class InitialResponseSettingProperty:
        def __init__(
            self,
            *,
            code_hook: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.DialogCodeHookInvocationSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ConditionalSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            initial_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ResponseSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.DialogStateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration setting for a response sent to the user before Amazon Lex starts eliciting slots.

            :param code_hook: Settings that specify the dialog code hook that is called by Amazon Lex at a step of the conversation.
            :param conditional: Provides a list of conditional branches. Branches are evaluated in the order that they are entered in the list. The first branch with a condition that evaluates to true is executed. The last branch in the list is the default branch. The default branch should not have any condition expression. The default branch is executed if no other branch has a matching condition.
            :param initial_response: Specifies a list of message groups that Amazon Lex uses to respond the user input.
            :param next_step: The next step in the conversation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-initialresponsesetting.html
            :exampleMetadata: fixture=_generated

            Example::

                
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__83749e2d6df5ca331ee019977e124fea7c18720ee7ffc2d63919bab99cc81a09)
                check_type(argname="argument code_hook", value=code_hook, expected_type=type_hints["code_hook"])
                check_type(argname="argument conditional", value=conditional, expected_type=type_hints["conditional"])
                check_type(argname="argument initial_response", value=initial_response, expected_type=type_hints["initial_response"])
                check_type(argname="argument next_step", value=next_step, expected_type=type_hints["next_step"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if code_hook is not None:
                self._values["code_hook"] = code_hook
            if conditional is not None:
                self._values["conditional"] = conditional
            if initial_response is not None:
                self._values["initial_response"] = initial_response
            if next_step is not None:
                self._values["next_step"] = next_step

        @builtins.property
        def code_hook(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogCodeHookInvocationSettingProperty"]]:
            '''Settings that specify the dialog code hook that is called by Amazon Lex at a step of the conversation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-initialresponsesetting.html#cfn-lex-bot-initialresponsesetting-codehook
            '''
            result = self._values.get("code_hook")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogCodeHookInvocationSettingProperty"]], result)

        @builtins.property
        def conditional(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]]:
            '''Provides a list of conditional branches.

            Branches are evaluated in the order that they are entered in the list. The first branch with a condition that evaluates to true is executed. The last branch in the list is the default branch. The default branch should not have any condition expression. The default branch is executed if no other branch has a matching condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-initialresponsesetting.html#cfn-lex-bot-initialresponsesetting-conditional
            '''
            result = self._values.get("conditional")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]], result)

        @builtins.property
        def initial_response(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]]:
            '''Specifies a list of message groups that Amazon Lex uses to respond the user input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-initialresponsesetting.html#cfn-lex-bot-initialresponsesetting-initialresponse
            '''
            result = self._values.get("initial_response")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]], result)

        @builtins.property
        def next_step(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]]:
            '''The next step in the conversation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-initialresponsesetting.html#cfn-lex-bot-initialresponsesetting-nextstep
            '''
            result = self._values.get("next_step")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InitialResponseSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.InputContextProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name"},
    )
    class InputContextProperty:
        def __init__(self, *, name: builtins.str) -> None:
            '''A context that must be active for an intent to be selected by Amazon Lex.

            :param name: The name of the context.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-inputcontext.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                input_context_property = lex.CfnBot.InputContextProperty(
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__18309cb7fa78967eacac40a963eac7e414bca89983d05643328e0ca42fdd145f)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the context.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-inputcontext.html#cfn-lex-bot-inputcontext-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputContextProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.IntentClosingSettingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "closing_response": "closingResponse",
            "conditional": "conditional",
            "is_active": "isActive",
            "next_step": "nextStep",
        },
    )
    class IntentClosingSettingProperty:
        def __init__(
            self,
            *,
            closing_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ResponseSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ConditionalSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            is_active: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.DialogStateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Provides a statement the Amazon Lex conveys to the user when the intent is successfully fulfilled.

            :param closing_response: The response that Amazon Lex sends to the user when the intent is complete.
            :param conditional: A list of conditional branches associated with the intent's closing response. These branches are executed when the ``nextStep`` attribute is set to ``EvalutateConditional`` .
            :param is_active: Specifies whether an intent's closing response is used. When this field is false, the closing response isn't sent to the user. If the ``IsActive`` field isn't specified, the default is true.
            :param next_step: Specifies the next step that the bot executes after playing the intent's closing response.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentclosingsetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                # slot_value_override_property_: lex.CfnBot.SlotValueOverrideProperty
                
                intent_closing_setting_property = lex.CfnBot.IntentClosingSettingProperty(
                    closing_response=lex.CfnBot.ResponseSpecificationProperty(
                        message_groups_list=[lex.CfnBot.MessageGroupProperty(
                            message=lex.CfnBot.MessageProperty(
                                custom_payload=lex.CfnBot.CustomPayloadProperty(
                                    value="value"
                                ),
                                image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                    title="title",
                
                                    # the properties below are optional
                                    buttons=[lex.CfnBot.ButtonProperty(
                                        text="text",
                                        value="value"
                                    )],
                                    image_url="imageUrl",
                                    subtitle="subtitle"
                                ),
                                plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                    value="value"
                                ),
                                ssml_message=lex.CfnBot.SSMLMessageProperty(
                                    value="value"
                                )
                            ),
                
                            # the properties below are optional
                            variations=[lex.CfnBot.MessageProperty(
                                custom_payload=lex.CfnBot.CustomPayloadProperty(
                                    value="value"
                                ),
                                image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                    title="title",
                
                                    # the properties below are optional
                                    buttons=[lex.CfnBot.ButtonProperty(
                                        text="text",
                                        value="value"
                                    )],
                                    image_url="imageUrl",
                                    subtitle="subtitle"
                                ),
                                plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                    value="value"
                                ),
                                ssml_message=lex.CfnBot.SSMLMessageProperty(
                                    value="value"
                                )
                            )]
                        )],
                
                        # the properties below are optional
                        allow_interrupt=False
                    ),
                    conditional=lex.CfnBot.ConditionalSpecificationProperty(
                        conditional_branches=[lex.CfnBot.ConditionalBranchProperty(
                            condition=lex.CfnBot.ConditionProperty(
                                expression_string="expressionString"
                            ),
                            name="name",
                            next_step=lex.CfnBot.DialogStateProperty(
                                dialog_action=lex.CfnBot.DialogActionProperty(
                                    type="type",
                
                                    # the properties below are optional
                                    slot_to_elicit="slotToElicit",
                                    suppress_next_message=False
                                ),
                                intent=lex.CfnBot.IntentOverrideProperty(
                                    name="name",
                                    slots=[lex.CfnBot.SlotValueOverrideMapProperty(
                                        slot_name="slotName",
                                        slot_value_override=lex.CfnBot.SlotValueOverrideProperty(
                                            shape="shape",
                                            value=lex.CfnBot.SlotValueProperty(
                                                interpreted_value="interpretedValue"
                                            ),
                                            values=[slot_value_override_property_]
                                        )
                                    )]
                                ),
                                session_attributes=[lex.CfnBot.SessionAttributeProperty(
                                    key="key",
                
                                    # the properties below are optional
                                    value="value"
                                )]
                            ),
                
                            # the properties below are optional
                            response=lex.CfnBot.ResponseSpecificationProperty(
                                message_groups_list=[lex.CfnBot.MessageGroupProperty(
                                    message=lex.CfnBot.MessageProperty(
                                        custom_payload=lex.CfnBot.CustomPayloadProperty(
                                            value="value"
                                        ),
                                        image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                            title="title",
                
                                            # the properties below are optional
                                            buttons=[lex.CfnBot.ButtonProperty(
                                                text="text",
                                                value="value"
                                            )],
                                            image_url="imageUrl",
                                            subtitle="subtitle"
                                        ),
                                        plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                            value="value"
                                        ),
                                        ssml_message=lex.CfnBot.SSMLMessageProperty(
                                            value="value"
                                        )
                                    ),
                
                                    # the properties below are optional
                                    variations=[lex.CfnBot.MessageProperty(
                                        custom_payload=lex.CfnBot.CustomPayloadProperty(
                                            value="value"
                                        ),
                                        image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                            title="title",
                
                                            # the properties below are optional
                                            buttons=[lex.CfnBot.ButtonProperty(
                                                text="text",
                                                value="value"
                                            )],
                                            image_url="imageUrl",
                                            subtitle="subtitle"
                                        ),
                                        plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                            value="value"
                                        ),
                                        ssml_message=lex.CfnBot.SSMLMessageProperty(
                                            value="value"
                                        )
                                    )]
                                )],
                
                                # the properties below are optional
                                allow_interrupt=False
                            )
                        )],
                        default_branch=lex.CfnBot.DefaultConditionalBranchProperty(
                            next_step=lex.CfnBot.DialogStateProperty(
                                dialog_action=lex.CfnBot.DialogActionProperty(
                                    type="type",
                
                                    # the properties below are optional
                                    slot_to_elicit="slotToElicit",
                                    suppress_next_message=False
                                ),
                                intent=lex.CfnBot.IntentOverrideProperty(
                                    name="name",
                                    slots=[lex.CfnBot.SlotValueOverrideMapProperty(
                                        slot_name="slotName",
                                        slot_value_override=lex.CfnBot.SlotValueOverrideProperty(
                                            shape="shape",
                                            value=lex.CfnBot.SlotValueProperty(
                                                interpreted_value="interpretedValue"
                                            ),
                                            values=[slot_value_override_property_]
                                        )
                                    )]
                                ),
                                session_attributes=[lex.CfnBot.SessionAttributeProperty(
                                    key="key",
                
                                    # the properties below are optional
                                    value="value"
                                )]
                            ),
                            response=lex.CfnBot.ResponseSpecificationProperty(
                                message_groups_list=[lex.CfnBot.MessageGroupProperty(
                                    message=lex.CfnBot.MessageProperty(
                                        custom_payload=lex.CfnBot.CustomPayloadProperty(
                                            value="value"
                                        ),
                                        image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                            title="title",
                
                                            # the properties below are optional
                                            buttons=[lex.CfnBot.ButtonProperty(
                                                text="text",
                                                value="value"
                                            )],
                                            image_url="imageUrl",
                                            subtitle="subtitle"
                                        ),
                                        plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                            value="value"
                                        ),
                                        ssml_message=lex.CfnBot.SSMLMessageProperty(
                                            value="value"
                                        )
                                    ),
                
                                    # the properties below are optional
                                    variations=[lex.CfnBot.MessageProperty(
                                        custom_payload=lex.CfnBot.CustomPayloadProperty(
                                            value="value"
                                        ),
                                        image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                            title="title",
                
                                            # the properties below are optional
                                            buttons=[lex.CfnBot.ButtonProperty(
                                                text="text",
                                                value="value"
                                            )],
                                            image_url="imageUrl",
                                            subtitle="subtitle"
                                        ),
                                        plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                            value="value"
                                        ),
                                        ssml_message=lex.CfnBot.SSMLMessageProperty(
                                            value="value"
                                        )
                                    )]
                                )],
                
                                # the properties below are optional
                                allow_interrupt=False
                            )
                        ),
                        is_active=False
                    ),
                    is_active=False,
                    next_step=lex.CfnBot.DialogStateProperty(
                        dialog_action=lex.CfnBot.DialogActionProperty(
                            type="type",
                
                            # the properties below are optional
                            slot_to_elicit="slotToElicit",
                            suppress_next_message=False
                        ),
                        intent=lex.CfnBot.IntentOverrideProperty(
                            name="name",
                            slots=[lex.CfnBot.SlotValueOverrideMapProperty(
                                slot_name="slotName",
                                slot_value_override=lex.CfnBot.SlotValueOverrideProperty(
                                    shape="shape",
                                    value=lex.CfnBot.SlotValueProperty(
                                        interpreted_value="interpretedValue"
                                    ),
                                    values=[slot_value_override_property_]
                                )
                            )]
                        ),
                        session_attributes=[lex.CfnBot.SessionAttributeProperty(
                            key="key",
                
                            # the properties below are optional
                            value="value"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4f90beb01727c97ae08801c759994a2a3947843959af8080718d29916dbe9e44)
                check_type(argname="argument closing_response", value=closing_response, expected_type=type_hints["closing_response"])
                check_type(argname="argument conditional", value=conditional, expected_type=type_hints["conditional"])
                check_type(argname="argument is_active", value=is_active, expected_type=type_hints["is_active"])
                check_type(argname="argument next_step", value=next_step, expected_type=type_hints["next_step"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if closing_response is not None:
                self._values["closing_response"] = closing_response
            if conditional is not None:
                self._values["conditional"] = conditional
            if is_active is not None:
                self._values["is_active"] = is_active
            if next_step is not None:
                self._values["next_step"] = next_step

        @builtins.property
        def closing_response(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]]:
            '''The response that Amazon Lex sends to the user when the intent is complete.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentclosingsetting.html#cfn-lex-bot-intentclosingsetting-closingresponse
            '''
            result = self._values.get("closing_response")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]], result)

        @builtins.property
        def conditional(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]]:
            '''A list of conditional branches associated with the intent's closing response.

            These branches are executed when the ``nextStep`` attribute is set to ``EvalutateConditional`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentclosingsetting.html#cfn-lex-bot-intentclosingsetting-conditional
            '''
            result = self._values.get("conditional")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]], result)

        @builtins.property
        def is_active(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether an intent's closing response is used.

            When this field is false, the closing response isn't sent to the user. If the ``IsActive`` field isn't specified, the default is true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentclosingsetting.html#cfn-lex-bot-intentclosingsetting-isactive
            '''
            result = self._values.get("is_active")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def next_step(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]]:
            '''Specifies the next step that the bot executes after playing the intent's closing response.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentclosingsetting.html#cfn-lex-bot-intentclosingsetting-nextstep
            '''
            result = self._values.get("next_step")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IntentClosingSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.IntentConfirmationSettingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "prompt_specification": "promptSpecification",
            "code_hook": "codeHook",
            "confirmation_conditional": "confirmationConditional",
            "confirmation_next_step": "confirmationNextStep",
            "confirmation_response": "confirmationResponse",
            "declination_conditional": "declinationConditional",
            "declination_next_step": "declinationNextStep",
            "declination_response": "declinationResponse",
            "elicitation_code_hook": "elicitationCodeHook",
            "failure_conditional": "failureConditional",
            "failure_next_step": "failureNextStep",
            "failure_response": "failureResponse",
            "is_active": "isActive",
        },
    )
    class IntentConfirmationSettingProperty:
        def __init__(
            self,
            *,
            prompt_specification: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.PromptSpecificationProperty", typing.Dict[builtins.str, typing.Any]]],
            code_hook: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.DialogCodeHookInvocationSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            confirmation_conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ConditionalSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            confirmation_next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.DialogStateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            confirmation_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ResponseSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            declination_conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ConditionalSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            declination_next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.DialogStateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            declination_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ResponseSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            elicitation_code_hook: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ElicitationCodeHookInvocationSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            failure_conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ConditionalSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            failure_next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.DialogStateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            failure_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ResponseSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            is_active: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Provides a prompt for making sure that the user is ready for the intent to be fulfilled.

            :param prompt_specification: Prompts the user to confirm the intent. This question should have a yes or no answer. Amazon Lex uses this prompt to ensure that the user acknowledges that the intent is ready for fulfillment. For example, with the ``OrderPizza`` intent, you might want to confirm that the order is correct before placing it. For other intents, such as intents that simply respond to user questions, you might not need to ask the user for confirmation before providing the information.
            :param code_hook: The ``DialogCodeHookInvocationSetting`` object associated with intent's confirmation step. The dialog code hook is triggered based on these invocation settings when the confirmation next step or declination next step or failure next step is ``InvokeDialogCodeHook`` .
            :param confirmation_conditional: A list of conditional branches to evaluate after the intent is closed.
            :param confirmation_next_step: Specifies the next step that the bot executes when the customer confirms the intent.
            :param confirmation_response: Specifies a list of message groups that Amazon Lex uses to respond the user input.
            :param declination_conditional: A list of conditional branches to evaluate after the intent is declined.
            :param declination_next_step: Specifies the next step that the bot executes when the customer declines the intent.
            :param declination_response: When the user answers "no" to the question defined in ``promptSpecification`` , Amazon Lex responds with this response to acknowledge that the intent was canceled.
            :param elicitation_code_hook: The ``DialogCodeHookInvocationSetting`` used when the code hook is invoked during confirmation prompt retries.
            :param failure_conditional: Provides a list of conditional branches. Branches are evaluated in the order that they are entered in the list. The first branch with a condition that evaluates to true is executed. The last branch in the list is the default branch. The default branch should not have any condition expression. The default branch is executed if no other branch has a matching condition.
            :param failure_next_step: The next step to take in the conversation if the confirmation step fails.
            :param failure_response: Specifies a list of message groups that Amazon Lex uses to respond the user input when the intent confirmation fails.
            :param is_active: Specifies whether the intent's confirmation is sent to the user. When this field is false, confirmation and declination responses aren't sent. If the ``IsActive`` field isn't specified, the default is true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html
            :exampleMetadata: fixture=_generated

            Example::

                
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8f96318abd0c4c68e9988644e0bef2c84730aaab41035ffb210f18a937b52ccc)
                check_type(argname="argument prompt_specification", value=prompt_specification, expected_type=type_hints["prompt_specification"])
                check_type(argname="argument code_hook", value=code_hook, expected_type=type_hints["code_hook"])
                check_type(argname="argument confirmation_conditional", value=confirmation_conditional, expected_type=type_hints["confirmation_conditional"])
                check_type(argname="argument confirmation_next_step", value=confirmation_next_step, expected_type=type_hints["confirmation_next_step"])
                check_type(argname="argument confirmation_response", value=confirmation_response, expected_type=type_hints["confirmation_response"])
                check_type(argname="argument declination_conditional", value=declination_conditional, expected_type=type_hints["declination_conditional"])
                check_type(argname="argument declination_next_step", value=declination_next_step, expected_type=type_hints["declination_next_step"])
                check_type(argname="argument declination_response", value=declination_response, expected_type=type_hints["declination_response"])
                check_type(argname="argument elicitation_code_hook", value=elicitation_code_hook, expected_type=type_hints["elicitation_code_hook"])
                check_type(argname="argument failure_conditional", value=failure_conditional, expected_type=type_hints["failure_conditional"])
                check_type(argname="argument failure_next_step", value=failure_next_step, expected_type=type_hints["failure_next_step"])
                check_type(argname="argument failure_response", value=failure_response, expected_type=type_hints["failure_response"])
                check_type(argname="argument is_active", value=is_active, expected_type=type_hints["is_active"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "prompt_specification": prompt_specification,
            }
            if code_hook is not None:
                self._values["code_hook"] = code_hook
            if confirmation_conditional is not None:
                self._values["confirmation_conditional"] = confirmation_conditional
            if confirmation_next_step is not None:
                self._values["confirmation_next_step"] = confirmation_next_step
            if confirmation_response is not None:
                self._values["confirmation_response"] = confirmation_response
            if declination_conditional is not None:
                self._values["declination_conditional"] = declination_conditional
            if declination_next_step is not None:
                self._values["declination_next_step"] = declination_next_step
            if declination_response is not None:
                self._values["declination_response"] = declination_response
            if elicitation_code_hook is not None:
                self._values["elicitation_code_hook"] = elicitation_code_hook
            if failure_conditional is not None:
                self._values["failure_conditional"] = failure_conditional
            if failure_next_step is not None:
                self._values["failure_next_step"] = failure_next_step
            if failure_response is not None:
                self._values["failure_response"] = failure_response
            if is_active is not None:
                self._values["is_active"] = is_active

        @builtins.property
        def prompt_specification(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnBot.PromptSpecificationProperty"]:
            '''Prompts the user to confirm the intent. This question should have a yes or no answer.

            Amazon Lex uses this prompt to ensure that the user acknowledges that the intent is ready for fulfillment. For example, with the ``OrderPizza`` intent, you might want to confirm that the order is correct before placing it. For other intents, such as intents that simply respond to user questions, you might not need to ask the user for confirmation before providing the information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-promptspecification
            '''
            result = self._values.get("prompt_specification")
            assert result is not None, "Required property 'prompt_specification' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBot.PromptSpecificationProperty"], result)

        @builtins.property
        def code_hook(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogCodeHookInvocationSettingProperty"]]:
            '''The ``DialogCodeHookInvocationSetting`` object associated with intent's confirmation step.

            The dialog code hook is triggered based on these invocation settings when the confirmation next step or declination next step or failure next step is ``InvokeDialogCodeHook`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-codehook
            '''
            result = self._values.get("code_hook")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogCodeHookInvocationSettingProperty"]], result)

        @builtins.property
        def confirmation_conditional(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]]:
            '''A list of conditional branches to evaluate after the intent is closed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-confirmationconditional
            '''
            result = self._values.get("confirmation_conditional")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]], result)

        @builtins.property
        def confirmation_next_step(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]]:
            '''Specifies the next step that the bot executes when the customer confirms the intent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-confirmationnextstep
            '''
            result = self._values.get("confirmation_next_step")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]], result)

        @builtins.property
        def confirmation_response(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]]:
            '''Specifies a list of message groups that Amazon Lex uses to respond the user input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-confirmationresponse
            '''
            result = self._values.get("confirmation_response")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]], result)

        @builtins.property
        def declination_conditional(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]]:
            '''A list of conditional branches to evaluate after the intent is declined.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-declinationconditional
            '''
            result = self._values.get("declination_conditional")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]], result)

        @builtins.property
        def declination_next_step(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]]:
            '''Specifies the next step that the bot executes when the customer declines the intent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-declinationnextstep
            '''
            result = self._values.get("declination_next_step")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]], result)

        @builtins.property
        def declination_response(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]]:
            '''When the user answers "no" to the question defined in ``promptSpecification`` , Amazon Lex responds with this response to acknowledge that the intent was canceled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-declinationresponse
            '''
            result = self._values.get("declination_response")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]], result)

        @builtins.property
        def elicitation_code_hook(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ElicitationCodeHookInvocationSettingProperty"]]:
            '''The ``DialogCodeHookInvocationSetting`` used when the code hook is invoked during confirmation prompt retries.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-elicitationcodehook
            '''
            result = self._values.get("elicitation_code_hook")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ElicitationCodeHookInvocationSettingProperty"]], result)

        @builtins.property
        def failure_conditional(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]]:
            '''Provides a list of conditional branches.

            Branches are evaluated in the order that they are entered in the list. The first branch with a condition that evaluates to true is executed. The last branch in the list is the default branch. The default branch should not have any condition expression. The default branch is executed if no other branch has a matching condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-failureconditional
            '''
            result = self._values.get("failure_conditional")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]], result)

        @builtins.property
        def failure_next_step(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]]:
            '''The next step to take in the conversation if the confirmation step fails.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-failurenextstep
            '''
            result = self._values.get("failure_next_step")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]], result)

        @builtins.property
        def failure_response(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]]:
            '''Specifies a list of message groups that Amazon Lex uses to respond the user input when the intent confirmation fails.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-failureresponse
            '''
            result = self._values.get("failure_response")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]], result)

        @builtins.property
        def is_active(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether the intent's confirmation is sent to the user.

            When this field is false, confirmation and declination responses aren't sent. If the ``IsActive`` field isn't specified, the default is true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentconfirmationsetting.html#cfn-lex-bot-intentconfirmationsetting-isactive
            '''
            result = self._values.get("is_active")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IntentConfirmationSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.IntentOverrideProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "slots": "slots"},
    )
    class IntentOverrideProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            slots: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.SlotValueOverrideMapProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Override settings to configure the intent state.

            :param name: The name of the intent. Only required when you're switching intents.
            :param slots: A map of all of the slot value overrides for the intent. The name of the slot maps to the value of the slot. Slots that are not included in the map aren't overridden.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentoverride.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                # slot_value_override_property_: lex.CfnBot.SlotValueOverrideProperty
                
                intent_override_property = lex.CfnBot.IntentOverrideProperty(
                    name="name",
                    slots=[lex.CfnBot.SlotValueOverrideMapProperty(
                        slot_name="slotName",
                        slot_value_override=lex.CfnBot.SlotValueOverrideProperty(
                            shape="shape",
                            value=lex.CfnBot.SlotValueProperty(
                                interpreted_value="interpretedValue"
                            ),
                            values=[slot_value_override_property_]
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__493166c423a1b45288ba10b5982fc7d58c8aa28aab6ecb53239e5da527e7fb9d)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument slots", value=slots, expected_type=type_hints["slots"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if slots is not None:
                self._values["slots"] = slots

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the intent.

            Only required when you're switching intents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentoverride.html#cfn-lex-bot-intentoverride-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def slots(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotValueOverrideMapProperty"]]]]:
            '''A map of all of the slot value overrides for the intent.

            The name of the slot maps to the value of the slot. Slots that are not included in the map aren't overridden.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intentoverride.html#cfn-lex-bot-intentoverride-slots
            '''
            result = self._values.get("slots")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotValueOverrideMapProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IntentOverrideProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.IntentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "description": "description",
            "dialog_code_hook": "dialogCodeHook",
            "fulfillment_code_hook": "fulfillmentCodeHook",
            "initial_response_setting": "initialResponseSetting",
            "input_contexts": "inputContexts",
            "intent_closing_setting": "intentClosingSetting",
            "intent_confirmation_setting": "intentConfirmationSetting",
            "kendra_configuration": "kendraConfiguration",
            "output_contexts": "outputContexts",
            "parent_intent_signature": "parentIntentSignature",
            "sample_utterances": "sampleUtterances",
            "slot_priorities": "slotPriorities",
            "slots": "slots",
        },
    )
    class IntentProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            description: typing.Optional[builtins.str] = None,
            dialog_code_hook: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.DialogCodeHookSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            fulfillment_code_hook: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.FulfillmentCodeHookSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            initial_response_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.InitialResponseSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            input_contexts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.InputContextProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            intent_closing_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.IntentClosingSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            intent_confirmation_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.IntentConfirmationSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            kendra_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.KendraConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            output_contexts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.OutputContextProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            parent_intent_signature: typing.Optional[builtins.str] = None,
            sample_utterances: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.SampleUtteranceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            slot_priorities: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.SlotPriorityProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            slots: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.SlotProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Represents an action that the user wants to perform.

            :param name: The name of the intent. Intent names must be unique within the locale that contains the intent and can't match the name of any built-in intent.
            :param description: A description of the intent. Use the description to help identify the intent in lists.
            :param dialog_code_hook: Specifies that Amazon Lex invokes the alias Lambda function for each user input. You can invoke this Lambda function to personalize user interaction.
            :param fulfillment_code_hook: Specifies that Amazon Lex invokes the alias Lambda function when the intent is ready for fulfillment. You can invoke this function to complete the bot's transaction with the user.
            :param initial_response_setting: Configuration setting for a response sent to the user before Amazon Lex starts eliciting slots.
            :param input_contexts: A list of contexts that must be active for this intent to be considered by Amazon Lex .
            :param intent_closing_setting: Sets the response that Amazon Lex sends to the user when the intent is closed.
            :param intent_confirmation_setting: Provides prompts that Amazon Lex sends to the user to confirm the completion of an intent. If the user answers "no," the settings contain a statement that is sent to the user to end the intent.
            :param kendra_configuration: Provides configuration information for the ``AMAZON.KendraSearchIntent`` intent. When you use this intent, Amazon Lex searches the specified Amazon Kendra index and returns documents from the index that match the user's utterance.
            :param output_contexts: A list of contexts that the intent activates when it is fulfilled.
            :param parent_intent_signature: A unique identifier for the built-in intent to base this intent on.
            :param sample_utterances: A list of utterances that a user might say to signal the intent.
            :param slot_priorities: Indicates the priority for slots. Amazon Lex prompts the user for slot values in priority order.
            :param slots: A list of slots that the intent requires for fulfillment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html
            :exampleMetadata: fixture=_generated

            Example::

                
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f105b684583292473a5d75a0aba26d4641f8f29746b1658a4a7b400367c1112f)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument dialog_code_hook", value=dialog_code_hook, expected_type=type_hints["dialog_code_hook"])
                check_type(argname="argument fulfillment_code_hook", value=fulfillment_code_hook, expected_type=type_hints["fulfillment_code_hook"])
                check_type(argname="argument initial_response_setting", value=initial_response_setting, expected_type=type_hints["initial_response_setting"])
                check_type(argname="argument input_contexts", value=input_contexts, expected_type=type_hints["input_contexts"])
                check_type(argname="argument intent_closing_setting", value=intent_closing_setting, expected_type=type_hints["intent_closing_setting"])
                check_type(argname="argument intent_confirmation_setting", value=intent_confirmation_setting, expected_type=type_hints["intent_confirmation_setting"])
                check_type(argname="argument kendra_configuration", value=kendra_configuration, expected_type=type_hints["kendra_configuration"])
                check_type(argname="argument output_contexts", value=output_contexts, expected_type=type_hints["output_contexts"])
                check_type(argname="argument parent_intent_signature", value=parent_intent_signature, expected_type=type_hints["parent_intent_signature"])
                check_type(argname="argument sample_utterances", value=sample_utterances, expected_type=type_hints["sample_utterances"])
                check_type(argname="argument slot_priorities", value=slot_priorities, expected_type=type_hints["slot_priorities"])
                check_type(argname="argument slots", value=slots, expected_type=type_hints["slots"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if description is not None:
                self._values["description"] = description
            if dialog_code_hook is not None:
                self._values["dialog_code_hook"] = dialog_code_hook
            if fulfillment_code_hook is not None:
                self._values["fulfillment_code_hook"] = fulfillment_code_hook
            if initial_response_setting is not None:
                self._values["initial_response_setting"] = initial_response_setting
            if input_contexts is not None:
                self._values["input_contexts"] = input_contexts
            if intent_closing_setting is not None:
                self._values["intent_closing_setting"] = intent_closing_setting
            if intent_confirmation_setting is not None:
                self._values["intent_confirmation_setting"] = intent_confirmation_setting
            if kendra_configuration is not None:
                self._values["kendra_configuration"] = kendra_configuration
            if output_contexts is not None:
                self._values["output_contexts"] = output_contexts
            if parent_intent_signature is not None:
                self._values["parent_intent_signature"] = parent_intent_signature
            if sample_utterances is not None:
                self._values["sample_utterances"] = sample_utterances
            if slot_priorities is not None:
                self._values["slot_priorities"] = slot_priorities
            if slots is not None:
                self._values["slots"] = slots

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the intent.

            Intent names must be unique within the locale that contains the intent and can't match the name of any built-in intent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''A description of the intent.

            Use the description to help identify the intent in lists.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dialog_code_hook(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogCodeHookSettingProperty"]]:
            '''Specifies that Amazon Lex invokes the alias Lambda function for each user input.

            You can invoke this Lambda function to personalize user interaction.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-dialogcodehook
            '''
            result = self._values.get("dialog_code_hook")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogCodeHookSettingProperty"]], result)

        @builtins.property
        def fulfillment_code_hook(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.FulfillmentCodeHookSettingProperty"]]:
            '''Specifies that Amazon Lex invokes the alias Lambda function when the intent is ready for fulfillment.

            You can invoke this function to complete the bot's transaction with the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-fulfillmentcodehook
            '''
            result = self._values.get("fulfillment_code_hook")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.FulfillmentCodeHookSettingProperty"]], result)

        @builtins.property
        def initial_response_setting(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.InitialResponseSettingProperty"]]:
            '''Configuration setting for a response sent to the user before Amazon Lex starts eliciting slots.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-initialresponsesetting
            '''
            result = self._values.get("initial_response_setting")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.InitialResponseSettingProperty"]], result)

        @builtins.property
        def input_contexts(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.InputContextProperty"]]]]:
            '''A list of contexts that must be active for this intent to be considered by Amazon Lex .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-inputcontexts
            '''
            result = self._values.get("input_contexts")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.InputContextProperty"]]]], result)

        @builtins.property
        def intent_closing_setting(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.IntentClosingSettingProperty"]]:
            '''Sets the response that Amazon Lex sends to the user when the intent is closed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-intentclosingsetting
            '''
            result = self._values.get("intent_closing_setting")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.IntentClosingSettingProperty"]], result)

        @builtins.property
        def intent_confirmation_setting(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.IntentConfirmationSettingProperty"]]:
            '''Provides prompts that Amazon Lex sends to the user to confirm the completion of an intent.

            If the user answers "no," the settings contain a statement that is sent to the user to end the intent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-intentconfirmationsetting
            '''
            result = self._values.get("intent_confirmation_setting")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.IntentConfirmationSettingProperty"]], result)

        @builtins.property
        def kendra_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.KendraConfigurationProperty"]]:
            '''Provides configuration information for the ``AMAZON.KendraSearchIntent`` intent. When you use this intent, Amazon Lex searches the specified Amazon Kendra index and returns documents from the index that match the user's utterance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-kendraconfiguration
            '''
            result = self._values.get("kendra_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.KendraConfigurationProperty"]], result)

        @builtins.property
        def output_contexts(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.OutputContextProperty"]]]]:
            '''A list of contexts that the intent activates when it is fulfilled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-outputcontexts
            '''
            result = self._values.get("output_contexts")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.OutputContextProperty"]]]], result)

        @builtins.property
        def parent_intent_signature(self) -> typing.Optional[builtins.str]:
            '''A unique identifier for the built-in intent to base this intent on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-parentintentsignature
            '''
            result = self._values.get("parent_intent_signature")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sample_utterances(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.SampleUtteranceProperty"]]]]:
            '''A list of utterances that a user might say to signal the intent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-sampleutterances
            '''
            result = self._values.get("sample_utterances")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.SampleUtteranceProperty"]]]], result)

        @builtins.property
        def slot_priorities(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotPriorityProperty"]]]]:
            '''Indicates the priority for slots.

            Amazon Lex prompts the user for slot values in priority order.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-slotpriorities
            '''
            result = self._values.get("slot_priorities")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotPriorityProperty"]]]], result)

        @builtins.property
        def slots(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotProperty"]]]]:
            '''A list of slots that the intent requires for fulfillment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-intent.html#cfn-lex-bot-intent-slots
            '''
            result = self._values.get("slots")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IntentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.KendraConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "kendra_index": "kendraIndex",
            "query_filter_string": "queryFilterString",
            "query_filter_string_enabled": "queryFilterStringEnabled",
        },
    )
    class KendraConfigurationProperty:
        def __init__(
            self,
            *,
            kendra_index: builtins.str,
            query_filter_string: typing.Optional[builtins.str] = None,
            query_filter_string_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Provides configuration information for the ``AMAZON.KendraSearchIntent`` intent. When you use this intent, Amazon Lex searches the specified Amazon Kendra index and returns documents from the index that match the user's utterance.

            :param kendra_index: The Amazon Resource Name (ARN) of the Amazon Kendra index that you want the ``AMAZON.KendraSearchIntent`` intent to search. The index must be in the same account and Region as the Amazon Lex bot.
            :param query_filter_string: A query filter that Amazon Lex sends to Amazon Kendra to filter the response from a query. The filter is in the format defined by Amazon Kendra. For more information, see `Filtering queries <https://docs.aws.amazon.com/kendra/latest/dg/filtering.html>`_ .
            :param query_filter_string_enabled: Determines whether the ``AMAZON.KendraSearchIntent`` intent uses a custom query string to query the Amazon Kendra index.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-kendraconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                kendra_configuration_property = lex.CfnBot.KendraConfigurationProperty(
                    kendra_index="kendraIndex",
                
                    # the properties below are optional
                    query_filter_string="queryFilterString",
                    query_filter_string_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__befde100c4754003fd17718bb74770d3516503d02c4db787eec9bec0d6ca499c)
                check_type(argname="argument kendra_index", value=kendra_index, expected_type=type_hints["kendra_index"])
                check_type(argname="argument query_filter_string", value=query_filter_string, expected_type=type_hints["query_filter_string"])
                check_type(argname="argument query_filter_string_enabled", value=query_filter_string_enabled, expected_type=type_hints["query_filter_string_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "kendra_index": kendra_index,
            }
            if query_filter_string is not None:
                self._values["query_filter_string"] = query_filter_string
            if query_filter_string_enabled is not None:
                self._values["query_filter_string_enabled"] = query_filter_string_enabled

        @builtins.property
        def kendra_index(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Amazon Kendra index that you want the ``AMAZON.KendraSearchIntent`` intent to search. The index must be in the same account and Region as the Amazon Lex bot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-kendraconfiguration.html#cfn-lex-bot-kendraconfiguration-kendraindex
            '''
            result = self._values.get("kendra_index")
            assert result is not None, "Required property 'kendra_index' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def query_filter_string(self) -> typing.Optional[builtins.str]:
            '''A query filter that Amazon Lex sends to Amazon Kendra to filter the response from a query.

            The filter is in the format defined by Amazon Kendra. For more information, see `Filtering queries <https://docs.aws.amazon.com/kendra/latest/dg/filtering.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-kendraconfiguration.html#cfn-lex-bot-kendraconfiguration-queryfilterstring
            '''
            result = self._values.get("query_filter_string")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def query_filter_string_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Determines whether the ``AMAZON.KendraSearchIntent`` intent uses a custom query string to query the Amazon Kendra index.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-kendraconfiguration.html#cfn-lex-bot-kendraconfiguration-queryfilterstringenabled
            '''
            result = self._values.get("query_filter_string_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KendraConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.LambdaCodeHookProperty",
        jsii_struct_bases=[],
        name_mapping={
            "code_hook_interface_version": "codeHookInterfaceVersion",
            "lambda_arn": "lambdaArn",
        },
    )
    class LambdaCodeHookProperty:
        def __init__(
            self,
            *,
            code_hook_interface_version: builtins.str,
            lambda_arn: builtins.str,
        ) -> None:
            '''Specifies a Lambda function that verifies requests to a bot or fulfills the user's request to a bot.

            :param code_hook_interface_version: The version of the request-response that you want Amazon Lex to use to invoke your Lambda function.
            :param lambda_arn: The Amazon Resource Name (ARN) of the Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-lambdacodehook.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                lambda_code_hook_property = lex.CfnBot.LambdaCodeHookProperty(
                    code_hook_interface_version="codeHookInterfaceVersion",
                    lambda_arn="lambdaArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ed25dece9631c2040723f44578a5a17d48f87a06be94d6d8ca47636248f12356)
                check_type(argname="argument code_hook_interface_version", value=code_hook_interface_version, expected_type=type_hints["code_hook_interface_version"])
                check_type(argname="argument lambda_arn", value=lambda_arn, expected_type=type_hints["lambda_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "code_hook_interface_version": code_hook_interface_version,
                "lambda_arn": lambda_arn,
            }

        @builtins.property
        def code_hook_interface_version(self) -> builtins.str:
            '''The version of the request-response that you want Amazon Lex to use to invoke your Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-lambdacodehook.html#cfn-lex-bot-lambdacodehook-codehookinterfaceversion
            '''
            result = self._values.get("code_hook_interface_version")
            assert result is not None, "Required property 'code_hook_interface_version' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def lambda_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-lambdacodehook.html#cfn-lex-bot-lambdacodehook-lambdaarn
            '''
            result = self._values.get("lambda_arn")
            assert result is not None, "Required property 'lambda_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaCodeHookProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.MessageGroupProperty",
        jsii_struct_bases=[],
        name_mapping={"message": "message", "variations": "variations"},
    )
    class MessageGroupProperty:
        def __init__(
            self,
            *,
            message: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.MessageProperty", typing.Dict[builtins.str, typing.Any]]],
            variations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.MessageProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Provides one or more messages that Amazon Lex should send to the user.

            :param message: The primary message that Amazon Lex should send to the user.
            :param variations: Message variations to send to the user. When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-messagegroup.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                message_group_property = lex.CfnBot.MessageGroupProperty(
                    message=lex.CfnBot.MessageProperty(
                        custom_payload=lex.CfnBot.CustomPayloadProperty(
                            value="value"
                        ),
                        image_response_card=lex.CfnBot.ImageResponseCardProperty(
                            title="title",
                
                            # the properties below are optional
                            buttons=[lex.CfnBot.ButtonProperty(
                                text="text",
                                value="value"
                            )],
                            image_url="imageUrl",
                            subtitle="subtitle"
                        ),
                        plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                            value="value"
                        ),
                        ssml_message=lex.CfnBot.SSMLMessageProperty(
                            value="value"
                        )
                    ),
                
                    # the properties below are optional
                    variations=[lex.CfnBot.MessageProperty(
                        custom_payload=lex.CfnBot.CustomPayloadProperty(
                            value="value"
                        ),
                        image_response_card=lex.CfnBot.ImageResponseCardProperty(
                            title="title",
                
                            # the properties below are optional
                            buttons=[lex.CfnBot.ButtonProperty(
                                text="text",
                                value="value"
                            )],
                            image_url="imageUrl",
                            subtitle="subtitle"
                        ),
                        plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                            value="value"
                        ),
                        ssml_message=lex.CfnBot.SSMLMessageProperty(
                            value="value"
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2b7bb98ebf9b78a6faa1470a130c8f32a0caa08de5353c4b06f938ca5f4ac01c)
                check_type(argname="argument message", value=message, expected_type=type_hints["message"])
                check_type(argname="argument variations", value=variations, expected_type=type_hints["variations"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "message": message,
            }
            if variations is not None:
                self._values["variations"] = variations

        @builtins.property
        def message(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnBot.MessageProperty"]:
            '''The primary message that Amazon Lex should send to the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-messagegroup.html#cfn-lex-bot-messagegroup-message
            '''
            result = self._values.get("message")
            assert result is not None, "Required property 'message' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBot.MessageProperty"], result)

        @builtins.property
        def variations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.MessageProperty"]]]]:
            '''Message variations to send to the user.

            When variations are defined, Amazon Lex chooses the primary message or one of the variations to send to the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-messagegroup.html#cfn-lex-bot-messagegroup-variations
            '''
            result = self._values.get("variations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.MessageProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MessageGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.MessageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "custom_payload": "customPayload",
            "image_response_card": "imageResponseCard",
            "plain_text_message": "plainTextMessage",
            "ssml_message": "ssmlMessage",
        },
    )
    class MessageProperty:
        def __init__(
            self,
            *,
            custom_payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.CustomPayloadProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            image_response_card: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ImageResponseCardProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            plain_text_message: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.PlainTextMessageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ssml_message: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.SSMLMessageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The object that provides message text and its type.

            :param custom_payload: A message in a custom format defined by the client application.
            :param image_response_card: A message that defines a response card that the client application can show to the user.
            :param plain_text_message: A message in plain text format.
            :param ssml_message: A message in Speech Synthesis Markup Language (SSML).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-message.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                message_property = lex.CfnBot.MessageProperty(
                    custom_payload=lex.CfnBot.CustomPayloadProperty(
                        value="value"
                    ),
                    image_response_card=lex.CfnBot.ImageResponseCardProperty(
                        title="title",
                
                        # the properties below are optional
                        buttons=[lex.CfnBot.ButtonProperty(
                            text="text",
                            value="value"
                        )],
                        image_url="imageUrl",
                        subtitle="subtitle"
                    ),
                    plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                        value="value"
                    ),
                    ssml_message=lex.CfnBot.SSMLMessageProperty(
                        value="value"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d4f93a57e245b677dfd69332cad697189343a98fda98898783b942417844c5e9)
                check_type(argname="argument custom_payload", value=custom_payload, expected_type=type_hints["custom_payload"])
                check_type(argname="argument image_response_card", value=image_response_card, expected_type=type_hints["image_response_card"])
                check_type(argname="argument plain_text_message", value=plain_text_message, expected_type=type_hints["plain_text_message"])
                check_type(argname="argument ssml_message", value=ssml_message, expected_type=type_hints["ssml_message"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if custom_payload is not None:
                self._values["custom_payload"] = custom_payload
            if image_response_card is not None:
                self._values["image_response_card"] = image_response_card
            if plain_text_message is not None:
                self._values["plain_text_message"] = plain_text_message
            if ssml_message is not None:
                self._values["ssml_message"] = ssml_message

        @builtins.property
        def custom_payload(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.CustomPayloadProperty"]]:
            '''A message in a custom format defined by the client application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-message.html#cfn-lex-bot-message-custompayload
            '''
            result = self._values.get("custom_payload")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.CustomPayloadProperty"]], result)

        @builtins.property
        def image_response_card(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ImageResponseCardProperty"]]:
            '''A message that defines a response card that the client application can show to the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-message.html#cfn-lex-bot-message-imageresponsecard
            '''
            result = self._values.get("image_response_card")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ImageResponseCardProperty"]], result)

        @builtins.property
        def plain_text_message(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.PlainTextMessageProperty"]]:
            '''A message in plain text format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-message.html#cfn-lex-bot-message-plaintextmessage
            '''
            result = self._values.get("plain_text_message")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.PlainTextMessageProperty"]], result)

        @builtins.property
        def ssml_message(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.SSMLMessageProperty"]]:
            '''A message in Speech Synthesis Markup Language (SSML).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-message.html#cfn-lex-bot-message-ssmlmessage
            '''
            result = self._values.get("ssml_message")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.SSMLMessageProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MessageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.MultipleValuesSettingProperty",
        jsii_struct_bases=[],
        name_mapping={"allow_multiple_values": "allowMultipleValues"},
    )
    class MultipleValuesSettingProperty:
        def __init__(
            self,
            *,
            allow_multiple_values: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Indicates whether a slot can return multiple values.

            :param allow_multiple_values: Indicates whether a slot can return multiple values. When ``true`` , the slot may return more than one value in a response. When ``false`` , the slot returns only a single value. Multi-value slots are only available in the en-US locale. If you set this value to ``true`` in any other locale, Amazon Lex throws a ``ValidationException`` . If the ``allowMutlipleValues`` is not set, the default value is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-multiplevaluessetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                multiple_values_setting_property = lex.CfnBot.MultipleValuesSettingProperty(
                    allow_multiple_values=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5d243896aac9e5978582c7a17b393ee26ecc4d0b53d8eeecb47f9b8e6de9baeb)
                check_type(argname="argument allow_multiple_values", value=allow_multiple_values, expected_type=type_hints["allow_multiple_values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if allow_multiple_values is not None:
                self._values["allow_multiple_values"] = allow_multiple_values

        @builtins.property
        def allow_multiple_values(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether a slot can return multiple values.

            When ``true`` , the slot may return more than one value in a response. When ``false`` , the slot returns only a single value.

            Multi-value slots are only available in the en-US locale. If you set this value to ``true`` in any other locale, Amazon Lex throws a ``ValidationException`` .

            If the ``allowMutlipleValues`` is not set, the default value is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-multiplevaluessetting.html#cfn-lex-bot-multiplevaluessetting-allowmultiplevalues
            '''
            result = self._values.get("allow_multiple_values")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MultipleValuesSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.ObfuscationSettingProperty",
        jsii_struct_bases=[],
        name_mapping={"obfuscation_setting_type": "obfuscationSettingType"},
    )
    class ObfuscationSettingProperty:
        def __init__(self, *, obfuscation_setting_type: builtins.str) -> None:
            '''Determines whether Amazon Lex obscures slot values in conversation logs.

            :param obfuscation_setting_type: Value that determines whether Amazon Lex obscures slot values in conversation logs. The default is to obscure the values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-obfuscationsetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                obfuscation_setting_property = lex.CfnBot.ObfuscationSettingProperty(
                    obfuscation_setting_type="obfuscationSettingType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a795f3c1800daacb8fa1b1f53ef1260088f1fa8ef905157a69c25f1fb6aaf260)
                check_type(argname="argument obfuscation_setting_type", value=obfuscation_setting_type, expected_type=type_hints["obfuscation_setting_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "obfuscation_setting_type": obfuscation_setting_type,
            }

        @builtins.property
        def obfuscation_setting_type(self) -> builtins.str:
            '''Value that determines whether Amazon Lex obscures slot values in conversation logs.

            The default is to obscure the values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-obfuscationsetting.html#cfn-lex-bot-obfuscationsetting-obfuscationsettingtype
            '''
            result = self._values.get("obfuscation_setting_type")
            assert result is not None, "Required property 'obfuscation_setting_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ObfuscationSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.OutputContextProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "time_to_live_in_seconds": "timeToLiveInSeconds",
            "turns_to_live": "turnsToLive",
        },
    )
    class OutputContextProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            time_to_live_in_seconds: jsii.Number,
            turns_to_live: jsii.Number,
        ) -> None:
            '''Describes a session context that is activated when an intent is fulfilled.

            :param name: The name of the output context.
            :param time_to_live_in_seconds: The amount of time, in seconds, that the output context should remain active. The time is figured from the first time the context is sent to the user.
            :param turns_to_live: The number of conversation turns that the output context should remain active. The number of turns is counted from the first time that the context is sent to the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-outputcontext.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                output_context_property = lex.CfnBot.OutputContextProperty(
                    name="name",
                    time_to_live_in_seconds=123,
                    turns_to_live=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6778b57b5a02264308db760307dd896938ee6291e49f511015f350056cc54059)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument time_to_live_in_seconds", value=time_to_live_in_seconds, expected_type=type_hints["time_to_live_in_seconds"])
                check_type(argname="argument turns_to_live", value=turns_to_live, expected_type=type_hints["turns_to_live"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "time_to_live_in_seconds": time_to_live_in_seconds,
                "turns_to_live": turns_to_live,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the output context.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-outputcontext.html#cfn-lex-bot-outputcontext-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def time_to_live_in_seconds(self) -> jsii.Number:
            '''The amount of time, in seconds, that the output context should remain active.

            The time is figured from the first time the context is sent to the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-outputcontext.html#cfn-lex-bot-outputcontext-timetoliveinseconds
            '''
            result = self._values.get("time_to_live_in_seconds")
            assert result is not None, "Required property 'time_to_live_in_seconds' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def turns_to_live(self) -> jsii.Number:
            '''The number of conversation turns that the output context should remain active.

            The number of turns is counted from the first time that the context is sent to the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-outputcontext.html#cfn-lex-bot-outputcontext-turnstolive
            '''
            result = self._values.get("turns_to_live")
            assert result is not None, "Required property 'turns_to_live' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputContextProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.PlainTextMessageProperty",
        jsii_struct_bases=[],
        name_mapping={"value": "value"},
    )
    class PlainTextMessageProperty:
        def __init__(self, *, value: builtins.str) -> None:
            '''Defines an ASCII text message to send to the user.

            :param value: The message to send to the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-plaintextmessage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                plain_text_message_property = lex.CfnBot.PlainTextMessageProperty(
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ba4054ec5399c78441e6f8c9140c893660759acdecf2641d77e755440453f99b)
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "value": value,
            }

        @builtins.property
        def value(self) -> builtins.str:
            '''The message to send to the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-plaintextmessage.html#cfn-lex-bot-plaintextmessage-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PlainTextMessageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.PostDialogCodeHookInvocationSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "failure_conditional": "failureConditional",
            "failure_next_step": "failureNextStep",
            "failure_response": "failureResponse",
            "success_conditional": "successConditional",
            "success_next_step": "successNextStep",
            "success_response": "successResponse",
            "timeout_conditional": "timeoutConditional",
            "timeout_next_step": "timeoutNextStep",
            "timeout_response": "timeoutResponse",
        },
    )
    class PostDialogCodeHookInvocationSpecificationProperty:
        def __init__(
            self,
            *,
            failure_conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ConditionalSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            failure_next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.DialogStateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            failure_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ResponseSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            success_conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ConditionalSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            success_next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.DialogStateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            success_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ResponseSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            timeout_conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ConditionalSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            timeout_next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.DialogStateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            timeout_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ResponseSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies next steps to run after the dialog code hook finishes.

            :param failure_conditional: A list of conditional branches to evaluate after the dialog code hook throws an exception or returns with the ``State`` field of the ``Intent`` object set to ``Failed`` .
            :param failure_next_step: Specifies the next step the bot runs after the dialog code hook throws an exception or returns with the ``State`` field of the ``Intent`` object set to ``Failed`` .
            :param failure_response: Specifies a list of message groups that Amazon Lex uses to respond the user input when the code hook fails.
            :param success_conditional: A list of conditional branches to evaluate after the dialog code hook finishes successfully.
            :param success_next_step: Specifics the next step the bot runs after the dialog code hook finishes successfully.
            :param success_response: Specifies a list of message groups that Amazon Lex uses to respond when the code hook succeeds.
            :param timeout_conditional: A list of conditional branches to evaluate if the code hook times out.
            :param timeout_next_step: Specifies the next step that the bot runs when the code hook times out.
            :param timeout_response: Specifies a list of message groups that Amazon Lex uses to respond to the user input when the code hook times out.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postdialogcodehookinvocationspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__62eb1599f0b57eb49828d92c80a33151b817e1ccbd2af63d8044bc26a704044c)
                check_type(argname="argument failure_conditional", value=failure_conditional, expected_type=type_hints["failure_conditional"])
                check_type(argname="argument failure_next_step", value=failure_next_step, expected_type=type_hints["failure_next_step"])
                check_type(argname="argument failure_response", value=failure_response, expected_type=type_hints["failure_response"])
                check_type(argname="argument success_conditional", value=success_conditional, expected_type=type_hints["success_conditional"])
                check_type(argname="argument success_next_step", value=success_next_step, expected_type=type_hints["success_next_step"])
                check_type(argname="argument success_response", value=success_response, expected_type=type_hints["success_response"])
                check_type(argname="argument timeout_conditional", value=timeout_conditional, expected_type=type_hints["timeout_conditional"])
                check_type(argname="argument timeout_next_step", value=timeout_next_step, expected_type=type_hints["timeout_next_step"])
                check_type(argname="argument timeout_response", value=timeout_response, expected_type=type_hints["timeout_response"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if failure_conditional is not None:
                self._values["failure_conditional"] = failure_conditional
            if failure_next_step is not None:
                self._values["failure_next_step"] = failure_next_step
            if failure_response is not None:
                self._values["failure_response"] = failure_response
            if success_conditional is not None:
                self._values["success_conditional"] = success_conditional
            if success_next_step is not None:
                self._values["success_next_step"] = success_next_step
            if success_response is not None:
                self._values["success_response"] = success_response
            if timeout_conditional is not None:
                self._values["timeout_conditional"] = timeout_conditional
            if timeout_next_step is not None:
                self._values["timeout_next_step"] = timeout_next_step
            if timeout_response is not None:
                self._values["timeout_response"] = timeout_response

        @builtins.property
        def failure_conditional(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]]:
            '''A list of conditional branches to evaluate after the dialog code hook throws an exception or returns with the ``State`` field of the ``Intent`` object set to ``Failed`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postdialogcodehookinvocationspecification.html#cfn-lex-bot-postdialogcodehookinvocationspecification-failureconditional
            '''
            result = self._values.get("failure_conditional")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]], result)

        @builtins.property
        def failure_next_step(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]]:
            '''Specifies the next step the bot runs after the dialog code hook throws an exception or returns with the ``State`` field of the ``Intent`` object set to ``Failed`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postdialogcodehookinvocationspecification.html#cfn-lex-bot-postdialogcodehookinvocationspecification-failurenextstep
            '''
            result = self._values.get("failure_next_step")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]], result)

        @builtins.property
        def failure_response(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]]:
            '''Specifies a list of message groups that Amazon Lex uses to respond the user input when the code hook fails.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postdialogcodehookinvocationspecification.html#cfn-lex-bot-postdialogcodehookinvocationspecification-failureresponse
            '''
            result = self._values.get("failure_response")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]], result)

        @builtins.property
        def success_conditional(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]]:
            '''A list of conditional branches to evaluate after the dialog code hook finishes successfully.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postdialogcodehookinvocationspecification.html#cfn-lex-bot-postdialogcodehookinvocationspecification-successconditional
            '''
            result = self._values.get("success_conditional")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]], result)

        @builtins.property
        def success_next_step(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]]:
            '''Specifics the next step the bot runs after the dialog code hook finishes successfully.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postdialogcodehookinvocationspecification.html#cfn-lex-bot-postdialogcodehookinvocationspecification-successnextstep
            '''
            result = self._values.get("success_next_step")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]], result)

        @builtins.property
        def success_response(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]]:
            '''Specifies a list of message groups that Amazon Lex uses to respond when the code hook succeeds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postdialogcodehookinvocationspecification.html#cfn-lex-bot-postdialogcodehookinvocationspecification-successresponse
            '''
            result = self._values.get("success_response")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]], result)

        @builtins.property
        def timeout_conditional(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]]:
            '''A list of conditional branches to evaluate if the code hook times out.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postdialogcodehookinvocationspecification.html#cfn-lex-bot-postdialogcodehookinvocationspecification-timeoutconditional
            '''
            result = self._values.get("timeout_conditional")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]], result)

        @builtins.property
        def timeout_next_step(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]]:
            '''Specifies the next step that the bot runs when the code hook times out.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postdialogcodehookinvocationspecification.html#cfn-lex-bot-postdialogcodehookinvocationspecification-timeoutnextstep
            '''
            result = self._values.get("timeout_next_step")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]], result)

        @builtins.property
        def timeout_response(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]]:
            '''Specifies a list of message groups that Amazon Lex uses to respond to the user input when the code hook times out.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postdialogcodehookinvocationspecification.html#cfn-lex-bot-postdialogcodehookinvocationspecification-timeoutresponse
            '''
            result = self._values.get("timeout_response")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PostDialogCodeHookInvocationSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.PostFulfillmentStatusSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "failure_conditional": "failureConditional",
            "failure_next_step": "failureNextStep",
            "failure_response": "failureResponse",
            "success_conditional": "successConditional",
            "success_next_step": "successNextStep",
            "success_response": "successResponse",
            "timeout_conditional": "timeoutConditional",
            "timeout_next_step": "timeoutNextStep",
            "timeout_response": "timeoutResponse",
        },
    )
    class PostFulfillmentStatusSpecificationProperty:
        def __init__(
            self,
            *,
            failure_conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ConditionalSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            failure_next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.DialogStateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            failure_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ResponseSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            success_conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ConditionalSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            success_next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.DialogStateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            success_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ResponseSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            timeout_conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ConditionalSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            timeout_next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.DialogStateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            timeout_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ResponseSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Provides a setting that determines whether the post-fulfillment response is sent to the user.

            For more information, see ` <https://docs.aws.amazon.com/lexv2/latest/dg/streaming-progress.html#progress-complete>`_

            :param failure_conditional: A list of conditional branches to evaluate after the fulfillment code hook throws an exception or returns with the ``State`` field of the ``Intent`` object set to ``Failed`` .
            :param failure_next_step: Specifies the next step the bot runs after the fulfillment code hook throws an exception or returns with the ``State`` field of the ``Intent`` object set to ``Failed`` .
            :param failure_response: Specifies a list of message groups that Amazon Lex uses to respond when fulfillment isn't successful.
            :param success_conditional: A list of conditional branches to evaluate after the fulfillment code hook finishes successfully.
            :param success_next_step: Specifies the next step in the conversation that Amazon Lex invokes when the fulfillment code hook completes successfully.
            :param success_response: Specifies a list of message groups that Amazon Lex uses to respond when the fulfillment is successful.
            :param timeout_conditional: A list of conditional branches to evaluate if the fulfillment code hook times out.
            :param timeout_next_step: Specifies the next step that the bot runs when the fulfillment code hook times out.
            :param timeout_response: Specifies a list of message groups that Amazon Lex uses to respond when fulfillment isn't completed within the timeout period.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fbd6476d58fabc3c7113634854ca2260b61ab0c7b242040db795c0c8a814f541)
                check_type(argname="argument failure_conditional", value=failure_conditional, expected_type=type_hints["failure_conditional"])
                check_type(argname="argument failure_next_step", value=failure_next_step, expected_type=type_hints["failure_next_step"])
                check_type(argname="argument failure_response", value=failure_response, expected_type=type_hints["failure_response"])
                check_type(argname="argument success_conditional", value=success_conditional, expected_type=type_hints["success_conditional"])
                check_type(argname="argument success_next_step", value=success_next_step, expected_type=type_hints["success_next_step"])
                check_type(argname="argument success_response", value=success_response, expected_type=type_hints["success_response"])
                check_type(argname="argument timeout_conditional", value=timeout_conditional, expected_type=type_hints["timeout_conditional"])
                check_type(argname="argument timeout_next_step", value=timeout_next_step, expected_type=type_hints["timeout_next_step"])
                check_type(argname="argument timeout_response", value=timeout_response, expected_type=type_hints["timeout_response"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if failure_conditional is not None:
                self._values["failure_conditional"] = failure_conditional
            if failure_next_step is not None:
                self._values["failure_next_step"] = failure_next_step
            if failure_response is not None:
                self._values["failure_response"] = failure_response
            if success_conditional is not None:
                self._values["success_conditional"] = success_conditional
            if success_next_step is not None:
                self._values["success_next_step"] = success_next_step
            if success_response is not None:
                self._values["success_response"] = success_response
            if timeout_conditional is not None:
                self._values["timeout_conditional"] = timeout_conditional
            if timeout_next_step is not None:
                self._values["timeout_next_step"] = timeout_next_step
            if timeout_response is not None:
                self._values["timeout_response"] = timeout_response

        @builtins.property
        def failure_conditional(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]]:
            '''A list of conditional branches to evaluate after the fulfillment code hook throws an exception or returns with the ``State`` field of the ``Intent`` object set to ``Failed`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html#cfn-lex-bot-postfulfillmentstatusspecification-failureconditional
            '''
            result = self._values.get("failure_conditional")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]], result)

        @builtins.property
        def failure_next_step(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]]:
            '''Specifies the next step the bot runs after the fulfillment code hook throws an exception or returns with the ``State`` field of the ``Intent`` object set to ``Failed`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html#cfn-lex-bot-postfulfillmentstatusspecification-failurenextstep
            '''
            result = self._values.get("failure_next_step")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]], result)

        @builtins.property
        def failure_response(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]]:
            '''Specifies a list of message groups that Amazon Lex uses to respond when fulfillment isn't successful.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html#cfn-lex-bot-postfulfillmentstatusspecification-failureresponse
            '''
            result = self._values.get("failure_response")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]], result)

        @builtins.property
        def success_conditional(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]]:
            '''A list of conditional branches to evaluate after the fulfillment code hook finishes successfully.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html#cfn-lex-bot-postfulfillmentstatusspecification-successconditional
            '''
            result = self._values.get("success_conditional")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]], result)

        @builtins.property
        def success_next_step(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]]:
            '''Specifies the next step in the conversation that Amazon Lex invokes when the fulfillment code hook completes successfully.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html#cfn-lex-bot-postfulfillmentstatusspecification-successnextstep
            '''
            result = self._values.get("success_next_step")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]], result)

        @builtins.property
        def success_response(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]]:
            '''Specifies a list of message groups that Amazon Lex uses to respond when the fulfillment is successful.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html#cfn-lex-bot-postfulfillmentstatusspecification-successresponse
            '''
            result = self._values.get("success_response")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]], result)

        @builtins.property
        def timeout_conditional(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]]:
            '''A list of conditional branches to evaluate if the fulfillment code hook times out.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html#cfn-lex-bot-postfulfillmentstatusspecification-timeoutconditional
            '''
            result = self._values.get("timeout_conditional")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]], result)

        @builtins.property
        def timeout_next_step(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]]:
            '''Specifies the next step that the bot runs when the fulfillment code hook times out.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html#cfn-lex-bot-postfulfillmentstatusspecification-timeoutnextstep
            '''
            result = self._values.get("timeout_next_step")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]], result)

        @builtins.property
        def timeout_response(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]]:
            '''Specifies a list of message groups that Amazon Lex uses to respond when fulfillment isn't completed within the timeout period.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-postfulfillmentstatusspecification.html#cfn-lex-bot-postfulfillmentstatusspecification-timeoutresponse
            '''
            result = self._values.get("timeout_response")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PostFulfillmentStatusSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.PromptAttemptSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allowed_input_types": "allowedInputTypes",
            "allow_interrupt": "allowInterrupt",
            "audio_and_dtmf_input_specification": "audioAndDtmfInputSpecification",
            "text_input_specification": "textInputSpecification",
        },
    )
    class PromptAttemptSpecificationProperty:
        def __init__(
            self,
            *,
            allowed_input_types: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.AllowedInputTypesProperty", typing.Dict[builtins.str, typing.Any]]],
            allow_interrupt: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            audio_and_dtmf_input_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.AudioAndDTMFInputSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            text_input_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.TextInputSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the settings on a prompt attempt.

            :param allowed_input_types: Indicates the allowed input types of the prompt attempt.
            :param allow_interrupt: Indicates whether the user can interrupt a speech prompt attempt from the bot.
            :param audio_and_dtmf_input_specification: Specifies the settings on audio and DTMF input.
            :param text_input_specification: Specifies the settings on text input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptattemptspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                prompt_attempt_specification_property = lex.CfnBot.PromptAttemptSpecificationProperty(
                    allowed_input_types=lex.CfnBot.AllowedInputTypesProperty(
                        allow_audio_input=False,
                        allow_dtmf_input=False
                    ),
                
                    # the properties below are optional
                    allow_interrupt=False,
                    audio_and_dtmf_input_specification=lex.CfnBot.AudioAndDTMFInputSpecificationProperty(
                        start_timeout_ms=123,
                
                        # the properties below are optional
                        audio_specification=lex.CfnBot.AudioSpecificationProperty(
                            end_timeout_ms=123,
                            max_length_ms=123
                        ),
                        dtmf_specification=lex.CfnBot.DTMFSpecificationProperty(
                            deletion_character="deletionCharacter",
                            end_character="endCharacter",
                            end_timeout_ms=123,
                            max_length=123
                        )
                    ),
                    text_input_specification=lex.CfnBot.TextInputSpecificationProperty(
                        start_timeout_ms=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__943a427e65ce74bc55f71dc759e0b2b2e36381bcfbb7a02e474b7679c58966ff)
                check_type(argname="argument allowed_input_types", value=allowed_input_types, expected_type=type_hints["allowed_input_types"])
                check_type(argname="argument allow_interrupt", value=allow_interrupt, expected_type=type_hints["allow_interrupt"])
                check_type(argname="argument audio_and_dtmf_input_specification", value=audio_and_dtmf_input_specification, expected_type=type_hints["audio_and_dtmf_input_specification"])
                check_type(argname="argument text_input_specification", value=text_input_specification, expected_type=type_hints["text_input_specification"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "allowed_input_types": allowed_input_types,
            }
            if allow_interrupt is not None:
                self._values["allow_interrupt"] = allow_interrupt
            if audio_and_dtmf_input_specification is not None:
                self._values["audio_and_dtmf_input_specification"] = audio_and_dtmf_input_specification
            if text_input_specification is not None:
                self._values["text_input_specification"] = text_input_specification

        @builtins.property
        def allowed_input_types(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnBot.AllowedInputTypesProperty"]:
            '''Indicates the allowed input types of the prompt attempt.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptattemptspecification.html#cfn-lex-bot-promptattemptspecification-allowedinputtypes
            '''
            result = self._values.get("allowed_input_types")
            assert result is not None, "Required property 'allowed_input_types' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBot.AllowedInputTypesProperty"], result)

        @builtins.property
        def allow_interrupt(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the user can interrupt a speech prompt attempt from the bot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptattemptspecification.html#cfn-lex-bot-promptattemptspecification-allowinterrupt
            '''
            result = self._values.get("allow_interrupt")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def audio_and_dtmf_input_specification(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.AudioAndDTMFInputSpecificationProperty"]]:
            '''Specifies the settings on audio and DTMF input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptattemptspecification.html#cfn-lex-bot-promptattemptspecification-audioanddtmfinputspecification
            '''
            result = self._values.get("audio_and_dtmf_input_specification")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.AudioAndDTMFInputSpecificationProperty"]], result)

        @builtins.property
        def text_input_specification(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.TextInputSpecificationProperty"]]:
            '''Specifies the settings on text input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptattemptspecification.html#cfn-lex-bot-promptattemptspecification-textinputspecification
            '''
            result = self._values.get("text_input_specification")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.TextInputSpecificationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PromptAttemptSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.PromptSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_retries": "maxRetries",
            "message_groups_list": "messageGroupsList",
            "allow_interrupt": "allowInterrupt",
            "message_selection_strategy": "messageSelectionStrategy",
            "prompt_attempts_specification": "promptAttemptsSpecification",
        },
    )
    class PromptSpecificationProperty:
        def __init__(
            self,
            *,
            max_retries: jsii.Number,
            message_groups_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.MessageGroupProperty", typing.Dict[builtins.str, typing.Any]]]]],
            allow_interrupt: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            message_selection_strategy: typing.Optional[builtins.str] = None,
            prompt_attempts_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.PromptAttemptSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Specifies a list of message groups that Amazon Lex sends to a user to elicit a response.

            :param max_retries: The maximum number of times the bot tries to elicit a response from the user using this prompt.
            :param message_groups_list: A collection of messages that Amazon Lex can send to the user. Amazon Lex chooses the actual message to send at runtime.
            :param allow_interrupt: Indicates whether the user can interrupt a speech prompt from the bot.
            :param message_selection_strategy: Indicates how a message is selected from a message group among retries.
            :param prompt_attempts_specification: Specifies the advanced settings on each attempt of the prompt.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                prompt_specification_property = lex.CfnBot.PromptSpecificationProperty(
                    max_retries=123,
                    message_groups_list=[lex.CfnBot.MessageGroupProperty(
                        message=lex.CfnBot.MessageProperty(
                            custom_payload=lex.CfnBot.CustomPayloadProperty(
                                value="value"
                            ),
                            image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                title="title",
                
                                # the properties below are optional
                                buttons=[lex.CfnBot.ButtonProperty(
                                    text="text",
                                    value="value"
                                )],
                                image_url="imageUrl",
                                subtitle="subtitle"
                            ),
                            plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                value="value"
                            ),
                            ssml_message=lex.CfnBot.SSMLMessageProperty(
                                value="value"
                            )
                        ),
                
                        # the properties below are optional
                        variations=[lex.CfnBot.MessageProperty(
                            custom_payload=lex.CfnBot.CustomPayloadProperty(
                                value="value"
                            ),
                            image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                title="title",
                
                                # the properties below are optional
                                buttons=[lex.CfnBot.ButtonProperty(
                                    text="text",
                                    value="value"
                                )],
                                image_url="imageUrl",
                                subtitle="subtitle"
                            ),
                            plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                value="value"
                            ),
                            ssml_message=lex.CfnBot.SSMLMessageProperty(
                                value="value"
                            )
                        )]
                    )],
                
                    # the properties below are optional
                    allow_interrupt=False,
                    message_selection_strategy="messageSelectionStrategy",
                    prompt_attempts_specification={
                        "prompt_attempts_specification_key": lex.CfnBot.PromptAttemptSpecificationProperty(
                            allowed_input_types=lex.CfnBot.AllowedInputTypesProperty(
                                allow_audio_input=False,
                                allow_dtmf_input=False
                            ),
                
                            # the properties below are optional
                            allow_interrupt=False,
                            audio_and_dtmf_input_specification=lex.CfnBot.AudioAndDTMFInputSpecificationProperty(
                                start_timeout_ms=123,
                
                                # the properties below are optional
                                audio_specification=lex.CfnBot.AudioSpecificationProperty(
                                    end_timeout_ms=123,
                                    max_length_ms=123
                                ),
                                dtmf_specification=lex.CfnBot.DTMFSpecificationProperty(
                                    deletion_character="deletionCharacter",
                                    end_character="endCharacter",
                                    end_timeout_ms=123,
                                    max_length=123
                                )
                            ),
                            text_input_specification=lex.CfnBot.TextInputSpecificationProperty(
                                start_timeout_ms=123
                            )
                        )
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dfee20d6cdf119a2c07cbe82b4eed1c4619bb7cefa041af9edd5327509e497e4)
                check_type(argname="argument max_retries", value=max_retries, expected_type=type_hints["max_retries"])
                check_type(argname="argument message_groups_list", value=message_groups_list, expected_type=type_hints["message_groups_list"])
                check_type(argname="argument allow_interrupt", value=allow_interrupt, expected_type=type_hints["allow_interrupt"])
                check_type(argname="argument message_selection_strategy", value=message_selection_strategy, expected_type=type_hints["message_selection_strategy"])
                check_type(argname="argument prompt_attempts_specification", value=prompt_attempts_specification, expected_type=type_hints["prompt_attempts_specification"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "max_retries": max_retries,
                "message_groups_list": message_groups_list,
            }
            if allow_interrupt is not None:
                self._values["allow_interrupt"] = allow_interrupt
            if message_selection_strategy is not None:
                self._values["message_selection_strategy"] = message_selection_strategy
            if prompt_attempts_specification is not None:
                self._values["prompt_attempts_specification"] = prompt_attempts_specification

        @builtins.property
        def max_retries(self) -> jsii.Number:
            '''The maximum number of times the bot tries to elicit a response from the user using this prompt.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptspecification.html#cfn-lex-bot-promptspecification-maxretries
            '''
            result = self._values.get("max_retries")
            assert result is not None, "Required property 'max_retries' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def message_groups_list(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.MessageGroupProperty"]]]:
            '''A collection of messages that Amazon Lex can send to the user.

            Amazon Lex chooses the actual message to send at runtime.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptspecification.html#cfn-lex-bot-promptspecification-messagegroupslist
            '''
            result = self._values.get("message_groups_list")
            assert result is not None, "Required property 'message_groups_list' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.MessageGroupProperty"]]], result)

        @builtins.property
        def allow_interrupt(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the user can interrupt a speech prompt from the bot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptspecification.html#cfn-lex-bot-promptspecification-allowinterrupt
            '''
            result = self._values.get("allow_interrupt")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def message_selection_strategy(self) -> typing.Optional[builtins.str]:
            '''Indicates how a message is selected from a message group among retries.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptspecification.html#cfn-lex-bot-promptspecification-messageselectionstrategy
            '''
            result = self._values.get("message_selection_strategy")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prompt_attempts_specification(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnBot.PromptAttemptSpecificationProperty"]]]]:
            '''Specifies the advanced settings on each attempt of the prompt.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-promptspecification.html#cfn-lex-bot-promptspecification-promptattemptsspecification
            '''
            result = self._values.get("prompt_attempts_specification")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnBot.PromptAttemptSpecificationProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PromptSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.ResponseSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "message_groups_list": "messageGroupsList",
            "allow_interrupt": "allowInterrupt",
        },
    )
    class ResponseSpecificationProperty:
        def __init__(
            self,
            *,
            message_groups_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.MessageGroupProperty", typing.Dict[builtins.str, typing.Any]]]]],
            allow_interrupt: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Specifies a list of message groups that Amazon Lex uses to respond the user input.

            :param message_groups_list: A collection of responses that Amazon Lex can send to the user. Amazon Lex chooses the actual response to send at runtime.
            :param allow_interrupt: Indicates whether the user can interrupt a speech response from Amazon Lex.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-responsespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                response_specification_property = lex.CfnBot.ResponseSpecificationProperty(
                    message_groups_list=[lex.CfnBot.MessageGroupProperty(
                        message=lex.CfnBot.MessageProperty(
                            custom_payload=lex.CfnBot.CustomPayloadProperty(
                                value="value"
                            ),
                            image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                title="title",
                
                                # the properties below are optional
                                buttons=[lex.CfnBot.ButtonProperty(
                                    text="text",
                                    value="value"
                                )],
                                image_url="imageUrl",
                                subtitle="subtitle"
                            ),
                            plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                value="value"
                            ),
                            ssml_message=lex.CfnBot.SSMLMessageProperty(
                                value="value"
                            )
                        ),
                
                        # the properties below are optional
                        variations=[lex.CfnBot.MessageProperty(
                            custom_payload=lex.CfnBot.CustomPayloadProperty(
                                value="value"
                            ),
                            image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                title="title",
                
                                # the properties below are optional
                                buttons=[lex.CfnBot.ButtonProperty(
                                    text="text",
                                    value="value"
                                )],
                                image_url="imageUrl",
                                subtitle="subtitle"
                            ),
                            plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                value="value"
                            ),
                            ssml_message=lex.CfnBot.SSMLMessageProperty(
                                value="value"
                            )
                        )]
                    )],
                
                    # the properties below are optional
                    allow_interrupt=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__41b902a3461c6b590e44c1b70d9b5197da38bf30395535518dbeee15b931cb17)
                check_type(argname="argument message_groups_list", value=message_groups_list, expected_type=type_hints["message_groups_list"])
                check_type(argname="argument allow_interrupt", value=allow_interrupt, expected_type=type_hints["allow_interrupt"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "message_groups_list": message_groups_list,
            }
            if allow_interrupt is not None:
                self._values["allow_interrupt"] = allow_interrupt

        @builtins.property
        def message_groups_list(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.MessageGroupProperty"]]]:
            '''A collection of responses that Amazon Lex can send to the user.

            Amazon Lex chooses the actual response to send at runtime.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-responsespecification.html#cfn-lex-bot-responsespecification-messagegroupslist
            '''
            result = self._values.get("message_groups_list")
            assert result is not None, "Required property 'message_groups_list' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.MessageGroupProperty"]]], result)

        @builtins.property
        def allow_interrupt(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the user can interrupt a speech response from Amazon Lex.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-responsespecification.html#cfn-lex-bot-responsespecification-allowinterrupt
            '''
            result = self._values.get("allow_interrupt")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResponseSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.S3BucketLogDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "log_prefix": "logPrefix",
            "s3_bucket_arn": "s3BucketArn",
            "kms_key_arn": "kmsKeyArn",
        },
    )
    class S3BucketLogDestinationProperty:
        def __init__(
            self,
            *,
            log_prefix: builtins.str,
            s3_bucket_arn: builtins.str,
            kms_key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies an Amazon S3 bucket for logging audio conversations.

            :param log_prefix: The S3 prefix to assign to audio log files.
            :param s3_bucket_arn: The Amazon Resource Name (ARN) of an Amazon S3 bucket where audio log files are stored.
            :param kms_key_arn: The Amazon Resource Name (ARN) of an AWS Key Management Service (KMS) key for encrypting audio log files stored in an Amazon S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-s3bucketlogdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                s3_bucket_log_destination_property = lex.CfnBot.S3BucketLogDestinationProperty(
                    log_prefix="logPrefix",
                    s3_bucket_arn="s3BucketArn",
                
                    # the properties below are optional
                    kms_key_arn="kmsKeyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ded78dd4eccaf929584502bf9d04303df195ccea074a52fa76a797748ee0e43b)
                check_type(argname="argument log_prefix", value=log_prefix, expected_type=type_hints["log_prefix"])
                check_type(argname="argument s3_bucket_arn", value=s3_bucket_arn, expected_type=type_hints["s3_bucket_arn"])
                check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "log_prefix": log_prefix,
                "s3_bucket_arn": s3_bucket_arn,
            }
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn

        @builtins.property
        def log_prefix(self) -> builtins.str:
            '''The S3 prefix to assign to audio log files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-s3bucketlogdestination.html#cfn-lex-bot-s3bucketlogdestination-logprefix
            '''
            result = self._values.get("log_prefix")
            assert result is not None, "Required property 'log_prefix' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_bucket_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of an Amazon S3 bucket where audio log files are stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-s3bucketlogdestination.html#cfn-lex-bot-s3bucketlogdestination-s3bucketarn
            '''
            result = self._values.get("s3_bucket_arn")
            assert result is not None, "Required property 's3_bucket_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of an AWS Key Management Service (KMS) key for encrypting audio log files stored in an Amazon S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-s3bucketlogdestination.html#cfn-lex-bot-s3bucketlogdestination-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3BucketLogDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "s3_bucket": "s3Bucket",
            "s3_object_key": "s3ObjectKey",
            "s3_object_version": "s3ObjectVersion",
        },
    )
    class S3LocationProperty:
        def __init__(
            self,
            *,
            s3_bucket: builtins.str,
            s3_object_key: builtins.str,
            s3_object_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines an Amazon S3 bucket location.

            :param s3_bucket: The S3 bucket name.
            :param s3_object_key: The path and file name to the object in the S3 bucket.
            :param s3_object_version: The version of the object in the S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                s3_location_property = lex.CfnBot.S3LocationProperty(
                    s3_bucket="s3Bucket",
                    s3_object_key="s3ObjectKey",
                
                    # the properties below are optional
                    s3_object_version="s3ObjectVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7d6aeb756ee3b20901b9c635f0dea5af9d930212d89c2181e88d0fdb1d2b13a6)
                check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
                check_type(argname="argument s3_object_key", value=s3_object_key, expected_type=type_hints["s3_object_key"])
                check_type(argname="argument s3_object_version", value=s3_object_version, expected_type=type_hints["s3_object_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3_bucket": s3_bucket,
                "s3_object_key": s3_object_key,
            }
            if s3_object_version is not None:
                self._values["s3_object_version"] = s3_object_version

        @builtins.property
        def s3_bucket(self) -> builtins.str:
            '''The S3 bucket name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-s3location.html#cfn-lex-bot-s3location-s3bucket
            '''
            result = self._values.get("s3_bucket")
            assert result is not None, "Required property 's3_bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_object_key(self) -> builtins.str:
            '''The path and file name to the object in the S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-s3location.html#cfn-lex-bot-s3location-s3objectkey
            '''
            result = self._values.get("s3_object_key")
            assert result is not None, "Required property 's3_object_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_object_version(self) -> typing.Optional[builtins.str]:
            '''The version of the object in the S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-s3location.html#cfn-lex-bot-s3location-s3objectversion
            '''
            result = self._values.get("s3_object_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.SSMLMessageProperty",
        jsii_struct_bases=[],
        name_mapping={"value": "value"},
    )
    class SSMLMessageProperty:
        def __init__(self, *, value: builtins.str) -> None:
            '''Defines a Speech Synthesis Markup Language (SSML) prompt.

            :param value: The SSML text that defines the prompt.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-ssmlmessage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                s_sMLMessage_property = lex.CfnBot.SSMLMessageProperty(
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0c9fd5a338093c2843c71a2fd67ef382cd74c7db746e18dcc56d46f706d264fe)
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "value": value,
            }

        @builtins.property
        def value(self) -> builtins.str:
            '''The SSML text that defines the prompt.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-ssmlmessage.html#cfn-lex-bot-ssmlmessage-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SSMLMessageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.SampleUtteranceProperty",
        jsii_struct_bases=[],
        name_mapping={"utterance": "utterance"},
    )
    class SampleUtteranceProperty:
        def __init__(self, *, utterance: builtins.str) -> None:
            '''A sample utterance that invokes an intent or respond to a slot elicitation prompt.

            :param utterance: A sample utterance that invokes an intent or respond to a slot elicitation prompt.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-sampleutterance.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                sample_utterance_property = lex.CfnBot.SampleUtteranceProperty(
                    utterance="utterance"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0142d6efc46c3cefacaba45fb4bc73266bcc186db01a160e97d3c9792a68f815)
                check_type(argname="argument utterance", value=utterance, expected_type=type_hints["utterance"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "utterance": utterance,
            }

        @builtins.property
        def utterance(self) -> builtins.str:
            '''A sample utterance that invokes an intent or respond to a slot elicitation prompt.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-sampleutterance.html#cfn-lex-bot-sampleutterance-utterance
            '''
            result = self._values.get("utterance")
            assert result is not None, "Required property 'utterance' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SampleUtteranceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.SampleValueProperty",
        jsii_struct_bases=[],
        name_mapping={"value": "value"},
    )
    class SampleValueProperty:
        def __init__(self, *, value: builtins.str) -> None:
            '''Defines one of the values for a slot type.

            :param value: The value that can be used for a slot type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-samplevalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                sample_value_property = lex.CfnBot.SampleValueProperty(
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cff5ea6d93f253339453f883c74d2692982ebd9b801acbfa83d5dc5e23650414)
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "value": value,
            }

        @builtins.property
        def value(self) -> builtins.str:
            '''The value that can be used for a slot type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-samplevalue.html#cfn-lex-bot-samplevalue-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SampleValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.SentimentAnalysisSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"detect_sentiment": "detectSentiment"},
    )
    class SentimentAnalysisSettingsProperty:
        def __init__(
            self,
            *,
            detect_sentiment: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''Determines whether Amazon Lex will use Amazon Comprehend to detect the sentiment of user utterances.

            :param detect_sentiment: Sets whether Amazon Lex uses Amazon Comprehend to detect the sentiment of user utterances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-sentimentanalysissettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                sentiment_analysis_settings_property = lex.CfnBot.SentimentAnalysisSettingsProperty(
                    detect_sentiment=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a9e4f3b0a606b026d5c930a078922f49440e9a195321a00c7a7a07508bf2d5d4)
                check_type(argname="argument detect_sentiment", value=detect_sentiment, expected_type=type_hints["detect_sentiment"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "detect_sentiment": detect_sentiment,
            }

        @builtins.property
        def detect_sentiment(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Sets whether Amazon Lex uses Amazon Comprehend to detect the sentiment of user utterances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-sentimentanalysissettings.html#cfn-lex-bot-sentimentanalysissettings-detectsentiment
            '''
            result = self._values.get("detect_sentiment")
            assert result is not None, "Required property 'detect_sentiment' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SentimentAnalysisSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.SessionAttributeProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class SessionAttributeProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A key/value pair representing session-specific context information.

            It contains application information passed between Amazon Lex V2 and a client application.

            :param key: The name of the session attribute.
            :param value: The session-specific context information for the session attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-sessionattribute.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                session_attribute_property = lex.CfnBot.SessionAttributeProperty(
                    key="key",
                
                    # the properties below are optional
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__be28e1d53db74d4e8f722a5f55abe5546d71fcda9d0b48a83fc4f86184b5dfe3)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
            }
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> builtins.str:
            '''The name of the session attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-sessionattribute.html#cfn-lex-bot-sessionattribute-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The session-specific context information for the session attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-sessionattribute.html#cfn-lex-bot-sessionattribute-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SessionAttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.SlotCaptureSettingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "capture_conditional": "captureConditional",
            "capture_next_step": "captureNextStep",
            "capture_response": "captureResponse",
            "code_hook": "codeHook",
            "elicitation_code_hook": "elicitationCodeHook",
            "failure_conditional": "failureConditional",
            "failure_next_step": "failureNextStep",
            "failure_response": "failureResponse",
        },
    )
    class SlotCaptureSettingProperty:
        def __init__(
            self,
            *,
            capture_conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ConditionalSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            capture_next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.DialogStateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            capture_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ResponseSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            code_hook: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.DialogCodeHookInvocationSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            elicitation_code_hook: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ElicitationCodeHookInvocationSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            failure_conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ConditionalSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            failure_next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.DialogStateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            failure_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ResponseSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Settings used when Amazon Lex successfully captures a slot value from a user.

            :param capture_conditional: A list of conditional branches to evaluate after the slot value is captured.
            :param capture_next_step: Specifies the next step that the bot runs when the slot value is captured before the code hook times out.
            :param capture_response: Specifies a list of message groups that Amazon Lex uses to respond the user input.
            :param code_hook: Code hook called after Amazon Lex successfully captures a slot value.
            :param elicitation_code_hook: Code hook called when Amazon Lex doesn't capture a slot value.
            :param failure_conditional: A list of conditional branches to evaluate when the slot value isn't captured.
            :param failure_next_step: Specifies the next step that the bot runs when the slot value code is not recognized.
            :param failure_response: Specifies a list of message groups that Amazon Lex uses to respond the user input when the slot fails to be captured.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotcapturesetting.html
            :exampleMetadata: fixture=_generated

            Example::

                
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0631539d23156c87283aee086bca2fb1e2b925a511e4ecec896a467b44f7bf65)
                check_type(argname="argument capture_conditional", value=capture_conditional, expected_type=type_hints["capture_conditional"])
                check_type(argname="argument capture_next_step", value=capture_next_step, expected_type=type_hints["capture_next_step"])
                check_type(argname="argument capture_response", value=capture_response, expected_type=type_hints["capture_response"])
                check_type(argname="argument code_hook", value=code_hook, expected_type=type_hints["code_hook"])
                check_type(argname="argument elicitation_code_hook", value=elicitation_code_hook, expected_type=type_hints["elicitation_code_hook"])
                check_type(argname="argument failure_conditional", value=failure_conditional, expected_type=type_hints["failure_conditional"])
                check_type(argname="argument failure_next_step", value=failure_next_step, expected_type=type_hints["failure_next_step"])
                check_type(argname="argument failure_response", value=failure_response, expected_type=type_hints["failure_response"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if capture_conditional is not None:
                self._values["capture_conditional"] = capture_conditional
            if capture_next_step is not None:
                self._values["capture_next_step"] = capture_next_step
            if capture_response is not None:
                self._values["capture_response"] = capture_response
            if code_hook is not None:
                self._values["code_hook"] = code_hook
            if elicitation_code_hook is not None:
                self._values["elicitation_code_hook"] = elicitation_code_hook
            if failure_conditional is not None:
                self._values["failure_conditional"] = failure_conditional
            if failure_next_step is not None:
                self._values["failure_next_step"] = failure_next_step
            if failure_response is not None:
                self._values["failure_response"] = failure_response

        @builtins.property
        def capture_conditional(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]]:
            '''A list of conditional branches to evaluate after the slot value is captured.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotcapturesetting.html#cfn-lex-bot-slotcapturesetting-captureconditional
            '''
            result = self._values.get("capture_conditional")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]], result)

        @builtins.property
        def capture_next_step(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]]:
            '''Specifies the next step that the bot runs when the slot value is captured before the code hook times out.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotcapturesetting.html#cfn-lex-bot-slotcapturesetting-capturenextstep
            '''
            result = self._values.get("capture_next_step")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]], result)

        @builtins.property
        def capture_response(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]]:
            '''Specifies a list of message groups that Amazon Lex uses to respond the user input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotcapturesetting.html#cfn-lex-bot-slotcapturesetting-captureresponse
            '''
            result = self._values.get("capture_response")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]], result)

        @builtins.property
        def code_hook(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogCodeHookInvocationSettingProperty"]]:
            '''Code hook called after Amazon Lex successfully captures a slot value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotcapturesetting.html#cfn-lex-bot-slotcapturesetting-codehook
            '''
            result = self._values.get("code_hook")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogCodeHookInvocationSettingProperty"]], result)

        @builtins.property
        def elicitation_code_hook(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ElicitationCodeHookInvocationSettingProperty"]]:
            '''Code hook called when Amazon Lex doesn't capture a slot value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotcapturesetting.html#cfn-lex-bot-slotcapturesetting-elicitationcodehook
            '''
            result = self._values.get("elicitation_code_hook")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ElicitationCodeHookInvocationSettingProperty"]], result)

        @builtins.property
        def failure_conditional(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]]:
            '''A list of conditional branches to evaluate when the slot value isn't captured.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotcapturesetting.html#cfn-lex-bot-slotcapturesetting-failureconditional
            '''
            result = self._values.get("failure_conditional")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConditionalSpecificationProperty"]], result)

        @builtins.property
        def failure_next_step(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]]:
            '''Specifies the next step that the bot runs when the slot value code is not recognized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotcapturesetting.html#cfn-lex-bot-slotcapturesetting-failurenextstep
            '''
            result = self._values.get("failure_next_step")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.DialogStateProperty"]], result)

        @builtins.property
        def failure_response(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]]:
            '''Specifies a list of message groups that Amazon Lex uses to respond the user input when the slot fails to be captured.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotcapturesetting.html#cfn-lex-bot-slotcapturesetting-failureresponse
            '''
            result = self._values.get("failure_response")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SlotCaptureSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.SlotDefaultValueProperty",
        jsii_struct_bases=[],
        name_mapping={"default_value": "defaultValue"},
    )
    class SlotDefaultValueProperty:
        def __init__(self, *, default_value: builtins.str) -> None:
            '''Specifies the default value to use when a user doesn't provide a value for a slot.

            :param default_value: The default value to use when a user doesn't provide a value for a slot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotdefaultvalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                slot_default_value_property = lex.CfnBot.SlotDefaultValueProperty(
                    default_value="defaultValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__33675db47c04e880974f8c48a0f7cf7c1b37ebf701f07d0c6cc8364e832c872b)
                check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "default_value": default_value,
            }

        @builtins.property
        def default_value(self) -> builtins.str:
            '''The default value to use when a user doesn't provide a value for a slot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotdefaultvalue.html#cfn-lex-bot-slotdefaultvalue-defaultvalue
            '''
            result = self._values.get("default_value")
            assert result is not None, "Required property 'default_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SlotDefaultValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.SlotDefaultValueSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"default_value_list": "defaultValueList"},
    )
    class SlotDefaultValueSpecificationProperty:
        def __init__(
            self,
            *,
            default_value_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.SlotDefaultValueProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''The default value to use when a user doesn't provide a value for a slot.

            :param default_value_list: A list of default values. Amazon Lex chooses the default value to use in the order that they are presented in the list.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotdefaultvaluespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                slot_default_value_specification_property = lex.CfnBot.SlotDefaultValueSpecificationProperty(
                    default_value_list=[lex.CfnBot.SlotDefaultValueProperty(
                        default_value="defaultValue"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__34b3d6924ee488b2942420ad151d4eacdd239979cd109bb95fe9c198976ad4fb)
                check_type(argname="argument default_value_list", value=default_value_list, expected_type=type_hints["default_value_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "default_value_list": default_value_list,
            }

        @builtins.property
        def default_value_list(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotDefaultValueProperty"]]]:
            '''A list of default values.

            Amazon Lex chooses the default value to use in the order that they are presented in the list.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotdefaultvaluespecification.html#cfn-lex-bot-slotdefaultvaluespecification-defaultvaluelist
            '''
            result = self._values.get("default_value_list")
            assert result is not None, "Required property 'default_value_list' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotDefaultValueProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SlotDefaultValueSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.SlotPriorityProperty",
        jsii_struct_bases=[],
        name_mapping={"priority": "priority", "slot_name": "slotName"},
    )
    class SlotPriorityProperty:
        def __init__(self, *, priority: jsii.Number, slot_name: builtins.str) -> None:
            '''Sets the priority that Amazon Lex should use when eliciting slot values from a user.

            :param priority: The priority that Amazon Lex should apply to the slot.
            :param slot_name: The name of the slot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotpriority.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                slot_priority_property = lex.CfnBot.SlotPriorityProperty(
                    priority=123,
                    slot_name="slotName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__244bb657ccf2ab8e922d85bf2dde92e8cbdaea5ac16a97de6a5a5c08112ce93d)
                check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
                check_type(argname="argument slot_name", value=slot_name, expected_type=type_hints["slot_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "priority": priority,
                "slot_name": slot_name,
            }

        @builtins.property
        def priority(self) -> jsii.Number:
            '''The priority that Amazon Lex should apply to the slot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotpriority.html#cfn-lex-bot-slotpriority-priority
            '''
            result = self._values.get("priority")
            assert result is not None, "Required property 'priority' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def slot_name(self) -> builtins.str:
            '''The name of the slot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotpriority.html#cfn-lex-bot-slotpriority-slotname
            '''
            result = self._values.get("slot_name")
            assert result is not None, "Required property 'slot_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SlotPriorityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.SlotProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "slot_type_name": "slotTypeName",
            "value_elicitation_setting": "valueElicitationSetting",
            "description": "description",
            "multiple_values_setting": "multipleValuesSetting",
            "obfuscation_setting": "obfuscationSetting",
        },
    )
    class SlotProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            slot_type_name: builtins.str,
            value_elicitation_setting: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.SlotValueElicitationSettingProperty", typing.Dict[builtins.str, typing.Any]]],
            description: typing.Optional[builtins.str] = None,
            multiple_values_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.MultipleValuesSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            obfuscation_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ObfuscationSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the definition of a slot.

            Amazon Lex elicits slot values from uses to fulfill the user's intent.

            :param name: The name given to the slot.
            :param slot_type_name: The name of the slot type that this slot is based on. The slot type defines the acceptable values for the slot.
            :param value_elicitation_setting: Determines the slot resolution strategy that Amazon Lex uses to return slot type values. The field can be set to one of the following values: - ORIGINAL_VALUE - Returns the value entered by the user, if the user value is similar to a slot value. - TOP_RESOLUTION - If there is a resolution list for the slot, return the first value in the resolution list as the slot type value. If there is no resolution list, null is returned. If you don't specify the ``valueSelectionStrategy`` , the default is ``ORIGINAL_VALUE`` .
            :param description: The description of the slot.
            :param multiple_values_setting: Indicates whether a slot can return multiple values.
            :param obfuscation_setting: Determines whether the contents of the slot are obfuscated in Amazon CloudWatch Logs logs. Use obfuscated slots to protect information such as personally identifiable information (PII) in logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html
            :exampleMetadata: fixture=_generated

            Example::

                
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ef126475ab56636b361ebc97f72cf09bd8480c4e5dad06e8da998fba1a7c6112)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument slot_type_name", value=slot_type_name, expected_type=type_hints["slot_type_name"])
                check_type(argname="argument value_elicitation_setting", value=value_elicitation_setting, expected_type=type_hints["value_elicitation_setting"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument multiple_values_setting", value=multiple_values_setting, expected_type=type_hints["multiple_values_setting"])
                check_type(argname="argument obfuscation_setting", value=obfuscation_setting, expected_type=type_hints["obfuscation_setting"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "slot_type_name": slot_type_name,
                "value_elicitation_setting": value_elicitation_setting,
            }
            if description is not None:
                self._values["description"] = description
            if multiple_values_setting is not None:
                self._values["multiple_values_setting"] = multiple_values_setting
            if obfuscation_setting is not None:
                self._values["obfuscation_setting"] = obfuscation_setting

        @builtins.property
        def name(self) -> builtins.str:
            '''The name given to the slot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html#cfn-lex-bot-slot-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def slot_type_name(self) -> builtins.str:
            '''The name of the slot type that this slot is based on.

            The slot type defines the acceptable values for the slot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html#cfn-lex-bot-slot-slottypename
            '''
            result = self._values.get("slot_type_name")
            assert result is not None, "Required property 'slot_type_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value_elicitation_setting(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnBot.SlotValueElicitationSettingProperty"]:
            '''Determines the slot resolution strategy that Amazon Lex uses to return slot type values.

            The field can be set to one of the following values:

            - ORIGINAL_VALUE - Returns the value entered by the user, if the user value is similar to a slot value.
            - TOP_RESOLUTION - If there is a resolution list for the slot, return the first value in the resolution list as the slot type value. If there is no resolution list, null is returned.

            If you don't specify the ``valueSelectionStrategy`` , the default is ``ORIGINAL_VALUE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html#cfn-lex-bot-slot-valueelicitationsetting
            '''
            result = self._values.get("value_elicitation_setting")
            assert result is not None, "Required property 'value_elicitation_setting' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBot.SlotValueElicitationSettingProperty"], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description of the slot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html#cfn-lex-bot-slot-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def multiple_values_setting(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.MultipleValuesSettingProperty"]]:
            '''Indicates whether a slot can return multiple values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html#cfn-lex-bot-slot-multiplevaluessetting
            '''
            result = self._values.get("multiple_values_setting")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.MultipleValuesSettingProperty"]], result)

        @builtins.property
        def obfuscation_setting(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ObfuscationSettingProperty"]]:
            '''Determines whether the contents of the slot are obfuscated in Amazon CloudWatch Logs logs.

            Use obfuscated slots to protect information such as personally identifiable information (PII) in logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slot.html#cfn-lex-bot-slot-obfuscationsetting
            '''
            result = self._values.get("obfuscation_setting")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ObfuscationSettingProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SlotProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.SlotTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "description": "description",
            "external_source_setting": "externalSourceSetting",
            "parent_slot_type_signature": "parentSlotTypeSignature",
            "slot_type_values": "slotTypeValues",
            "value_selection_setting": "valueSelectionSetting",
        },
    )
    class SlotTypeProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            description: typing.Optional[builtins.str] = None,
            external_source_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ExternalSourceSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            parent_slot_type_signature: typing.Optional[builtins.str] = None,
            slot_type_values: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.SlotTypeValueProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            value_selection_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.SlotValueSelectionSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes a slot type.

            :param name: The name of the slot type. A slot type name must be unique withing the account.
            :param description: A description of the slot type. Use the description to help identify the slot type in lists.
            :param external_source_setting: Sets the type of external information used to create the slot type.
            :param parent_slot_type_signature: The built-in slot type used as a parent of this slot type. When you define a parent slot type, the new slot type has the configuration of the parent lot type. Only ``AMAZON.AlphaNumeric`` is supported.
            :param slot_type_values: A list of SlotTypeValue objects that defines the values that the slot type can take. Each value can have a list of synonyms, additional values that help train the machine learning model about the values that it resolves for the slot.
            :param value_selection_setting: Determines the slot resolution strategy that Amazon Lex uses to return slot type values. The field can be set to one of the following values: - ``ORIGINAL_VALUE`` - Returns the value entered by the user, if the user value is similar to the slot value. - ``TOP_RESOLUTION`` - If there is a resolution list for the slot, return the first value in the resolution list as the slot type value. If there is no resolution list, null is returned. If you don't specify the ``valueSelectionStrategy`` , the default is ``ORIGINAL_VALUE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                slot_type_property = lex.CfnBot.SlotTypeProperty(
                    name="name",
                
                    # the properties below are optional
                    description="description",
                    external_source_setting=lex.CfnBot.ExternalSourceSettingProperty(
                        grammar_slot_type_setting=lex.CfnBot.GrammarSlotTypeSettingProperty(
                            source=lex.CfnBot.GrammarSlotTypeSourceProperty(
                                s3_bucket_name="s3BucketName",
                                s3_object_key="s3ObjectKey",
                
                                # the properties below are optional
                                kms_key_arn="kmsKeyArn"
                            )
                        )
                    ),
                    parent_slot_type_signature="parentSlotTypeSignature",
                    slot_type_values=[lex.CfnBot.SlotTypeValueProperty(
                        sample_value=lex.CfnBot.SampleValueProperty(
                            value="value"
                        ),
                
                        # the properties below are optional
                        synonyms=[lex.CfnBot.SampleValueProperty(
                            value="value"
                        )]
                    )],
                    value_selection_setting=lex.CfnBot.SlotValueSelectionSettingProperty(
                        resolution_strategy="resolutionStrategy",
                
                        # the properties below are optional
                        advanced_recognition_setting=lex.CfnBot.AdvancedRecognitionSettingProperty(
                            audio_recognition_strategy="audioRecognitionStrategy"
                        ),
                        regex_filter=lex.CfnBot.SlotValueRegexFilterProperty(
                            pattern="pattern"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d99d82598958085799a77f6b5114773dd5d435a8eed078da9626b631bffcfeea)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument external_source_setting", value=external_source_setting, expected_type=type_hints["external_source_setting"])
                check_type(argname="argument parent_slot_type_signature", value=parent_slot_type_signature, expected_type=type_hints["parent_slot_type_signature"])
                check_type(argname="argument slot_type_values", value=slot_type_values, expected_type=type_hints["slot_type_values"])
                check_type(argname="argument value_selection_setting", value=value_selection_setting, expected_type=type_hints["value_selection_setting"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if description is not None:
                self._values["description"] = description
            if external_source_setting is not None:
                self._values["external_source_setting"] = external_source_setting
            if parent_slot_type_signature is not None:
                self._values["parent_slot_type_signature"] = parent_slot_type_signature
            if slot_type_values is not None:
                self._values["slot_type_values"] = slot_type_values
            if value_selection_setting is not None:
                self._values["value_selection_setting"] = value_selection_setting

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the slot type.

            A slot type name must be unique withing the account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html#cfn-lex-bot-slottype-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''A description of the slot type.

            Use the description to help identify the slot type in lists.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html#cfn-lex-bot-slottype-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def external_source_setting(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ExternalSourceSettingProperty"]]:
            '''Sets the type of external information used to create the slot type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html#cfn-lex-bot-slottype-externalsourcesetting
            '''
            result = self._values.get("external_source_setting")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ExternalSourceSettingProperty"]], result)

        @builtins.property
        def parent_slot_type_signature(self) -> typing.Optional[builtins.str]:
            '''The built-in slot type used as a parent of this slot type.

            When you define a parent slot type, the new slot type has the configuration of the parent lot type.

            Only ``AMAZON.AlphaNumeric`` is supported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html#cfn-lex-bot-slottype-parentslottypesignature
            '''
            result = self._values.get("parent_slot_type_signature")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def slot_type_values(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotTypeValueProperty"]]]]:
            '''A list of SlotTypeValue objects that defines the values that the slot type can take.

            Each value can have a list of synonyms, additional values that help train the machine learning model about the values that it resolves for the slot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html#cfn-lex-bot-slottype-slottypevalues
            '''
            result = self._values.get("slot_type_values")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotTypeValueProperty"]]]], result)

        @builtins.property
        def value_selection_setting(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotValueSelectionSettingProperty"]]:
            '''Determines the slot resolution strategy that Amazon Lex uses to return slot type values.

            The field can be set to one of the following values:

            - ``ORIGINAL_VALUE`` - Returns the value entered by the user, if the user value is similar to the slot value.
            - ``TOP_RESOLUTION`` - If there is a resolution list for the slot, return the first value in the resolution list as the slot type value. If there is no resolution list, null is returned.

            If you don't specify the ``valueSelectionStrategy`` , the default is ``ORIGINAL_VALUE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottype.html#cfn-lex-bot-slottype-valueselectionsetting
            '''
            result = self._values.get("value_selection_setting")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotValueSelectionSettingProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SlotTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.SlotTypeValueProperty",
        jsii_struct_bases=[],
        name_mapping={"sample_value": "sampleValue", "synonyms": "synonyms"},
    )
    class SlotTypeValueProperty:
        def __init__(
            self,
            *,
            sample_value: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.SampleValueProperty", typing.Dict[builtins.str, typing.Any]]],
            synonyms: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.SampleValueProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Each slot type can have a set of values.

            Each ``SlotTypeValue`` represents a value that the slot type can take.

            :param sample_value: The value of the slot type entry.
            :param synonyms: Additional values related to the slot type entry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottypevalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                slot_type_value_property = lex.CfnBot.SlotTypeValueProperty(
                    sample_value=lex.CfnBot.SampleValueProperty(
                        value="value"
                    ),
                
                    # the properties below are optional
                    synonyms=[lex.CfnBot.SampleValueProperty(
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4980167aa5887813c0d207005609f7ad5f62c2160739ca34ec554de05bd9904a)
                check_type(argname="argument sample_value", value=sample_value, expected_type=type_hints["sample_value"])
                check_type(argname="argument synonyms", value=synonyms, expected_type=type_hints["synonyms"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "sample_value": sample_value,
            }
            if synonyms is not None:
                self._values["synonyms"] = synonyms

        @builtins.property
        def sample_value(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnBot.SampleValueProperty"]:
            '''The value of the slot type entry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottypevalue.html#cfn-lex-bot-slottypevalue-samplevalue
            '''
            result = self._values.get("sample_value")
            assert result is not None, "Required property 'sample_value' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBot.SampleValueProperty"], result)

        @builtins.property
        def synonyms(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.SampleValueProperty"]]]]:
            '''Additional values related to the slot type entry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slottypevalue.html#cfn-lex-bot-slottypevalue-synonyms
            '''
            result = self._values.get("synonyms")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.SampleValueProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SlotTypeValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.SlotValueElicitationSettingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "slot_constraint": "slotConstraint",
            "default_value_specification": "defaultValueSpecification",
            "prompt_specification": "promptSpecification",
            "sample_utterances": "sampleUtterances",
            "slot_capture_setting": "slotCaptureSetting",
            "wait_and_continue_specification": "waitAndContinueSpecification",
        },
    )
    class SlotValueElicitationSettingProperty:
        def __init__(
            self,
            *,
            slot_constraint: builtins.str,
            default_value_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.SlotDefaultValueSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            prompt_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.PromptSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sample_utterances: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.SampleUtteranceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            slot_capture_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.SlotCaptureSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            wait_and_continue_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.WaitAndContinueSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the elicitation setting details eliciting a slot.

            :param slot_constraint: Specifies whether the slot is required or optional.
            :param default_value_specification: A list of default values for a slot. Default values are used when Amazon Lex hasn't determined a value for a slot. You can specify default values from context variables, session attributes, and defined values.
            :param prompt_specification: The prompt that Amazon Lex uses to elicit the slot value from the user.
            :param sample_utterances: If you know a specific pattern that users might respond to an Amazon Lex request for a slot value, you can provide those utterances to improve accuracy. This is optional. In most cases, Amazon Lex is capable of understanding user utterances.
            :param slot_capture_setting: Specifies the settings that Amazon Lex uses when a slot value is successfully entered by a user.
            :param wait_and_continue_specification: Specifies the prompts that Amazon Lex uses while a bot is waiting for customer input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html
            :exampleMetadata: fixture=_generated

            Example::

                
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ce7cc5d5d9c242f068967edd6fef626bfeba8ad54b83c65f26b5e9c76f33bff3)
                check_type(argname="argument slot_constraint", value=slot_constraint, expected_type=type_hints["slot_constraint"])
                check_type(argname="argument default_value_specification", value=default_value_specification, expected_type=type_hints["default_value_specification"])
                check_type(argname="argument prompt_specification", value=prompt_specification, expected_type=type_hints["prompt_specification"])
                check_type(argname="argument sample_utterances", value=sample_utterances, expected_type=type_hints["sample_utterances"])
                check_type(argname="argument slot_capture_setting", value=slot_capture_setting, expected_type=type_hints["slot_capture_setting"])
                check_type(argname="argument wait_and_continue_specification", value=wait_and_continue_specification, expected_type=type_hints["wait_and_continue_specification"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "slot_constraint": slot_constraint,
            }
            if default_value_specification is not None:
                self._values["default_value_specification"] = default_value_specification
            if prompt_specification is not None:
                self._values["prompt_specification"] = prompt_specification
            if sample_utterances is not None:
                self._values["sample_utterances"] = sample_utterances
            if slot_capture_setting is not None:
                self._values["slot_capture_setting"] = slot_capture_setting
            if wait_and_continue_specification is not None:
                self._values["wait_and_continue_specification"] = wait_and_continue_specification

        @builtins.property
        def slot_constraint(self) -> builtins.str:
            '''Specifies whether the slot is required or optional.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html#cfn-lex-bot-slotvalueelicitationsetting-slotconstraint
            '''
            result = self._values.get("slot_constraint")
            assert result is not None, "Required property 'slot_constraint' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def default_value_specification(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotDefaultValueSpecificationProperty"]]:
            '''A list of default values for a slot.

            Default values are used when Amazon Lex hasn't determined a value for a slot. You can specify default values from context variables, session attributes, and defined values.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html#cfn-lex-bot-slotvalueelicitationsetting-defaultvaluespecification
            '''
            result = self._values.get("default_value_specification")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotDefaultValueSpecificationProperty"]], result)

        @builtins.property
        def prompt_specification(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.PromptSpecificationProperty"]]:
            '''The prompt that Amazon Lex uses to elicit the slot value from the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html#cfn-lex-bot-slotvalueelicitationsetting-promptspecification
            '''
            result = self._values.get("prompt_specification")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.PromptSpecificationProperty"]], result)

        @builtins.property
        def sample_utterances(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.SampleUtteranceProperty"]]]]:
            '''If you know a specific pattern that users might respond to an Amazon Lex request for a slot value, you can provide those utterances to improve accuracy.

            This is optional. In most cases, Amazon Lex is capable of understanding user utterances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html#cfn-lex-bot-slotvalueelicitationsetting-sampleutterances
            '''
            result = self._values.get("sample_utterances")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.SampleUtteranceProperty"]]]], result)

        @builtins.property
        def slot_capture_setting(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotCaptureSettingProperty"]]:
            '''Specifies the settings that Amazon Lex uses when a slot value is successfully entered by a user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html#cfn-lex-bot-slotvalueelicitationsetting-slotcapturesetting
            '''
            result = self._values.get("slot_capture_setting")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotCaptureSettingProperty"]], result)

        @builtins.property
        def wait_and_continue_specification(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.WaitAndContinueSpecificationProperty"]]:
            '''Specifies the prompts that Amazon Lex uses while a bot is waiting for customer input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueelicitationsetting.html#cfn-lex-bot-slotvalueelicitationsetting-waitandcontinuespecification
            '''
            result = self._values.get("wait_and_continue_specification")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.WaitAndContinueSpecificationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SlotValueElicitationSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.SlotValueOverrideMapProperty",
        jsii_struct_bases=[],
        name_mapping={
            "slot_name": "slotName",
            "slot_value_override": "slotValueOverride",
        },
    )
    class SlotValueOverrideMapProperty:
        def __init__(
            self,
            *,
            slot_name: typing.Optional[builtins.str] = None,
            slot_value_override: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.SlotValueOverrideProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Maps a slot name to the `SlotValueOverride <https://docs.aws.amazon.com/lexv2/latest/APIReference/API_SlotValueOverride.html>`_ object.

            :param slot_name: The name of the slot.
            :param slot_value_override: The SlotValueOverride object to which the slot name will be mapped.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueoverridemap.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                # slot_value_override_property_: lex.CfnBot.SlotValueOverrideProperty
                
                slot_value_override_map_property = lex.CfnBot.SlotValueOverrideMapProperty(
                    slot_name="slotName",
                    slot_value_override=lex.CfnBot.SlotValueOverrideProperty(
                        shape="shape",
                        value=lex.CfnBot.SlotValueProperty(
                            interpreted_value="interpretedValue"
                        ),
                        values=[slot_value_override_property_]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9d81fb72fae48bda11549c52cc7d70c5c0b7e2f4273a0bfdb8e7159f62a4f854)
                check_type(argname="argument slot_name", value=slot_name, expected_type=type_hints["slot_name"])
                check_type(argname="argument slot_value_override", value=slot_value_override, expected_type=type_hints["slot_value_override"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if slot_name is not None:
                self._values["slot_name"] = slot_name
            if slot_value_override is not None:
                self._values["slot_value_override"] = slot_value_override

        @builtins.property
        def slot_name(self) -> typing.Optional[builtins.str]:
            '''The name of the slot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueoverridemap.html#cfn-lex-bot-slotvalueoverridemap-slotname
            '''
            result = self._values.get("slot_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def slot_value_override(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotValueOverrideProperty"]]:
            '''The SlotValueOverride object to which the slot name will be mapped.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueoverridemap.html#cfn-lex-bot-slotvalueoverridemap-slotvalueoverride
            '''
            result = self._values.get("slot_value_override")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotValueOverrideProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SlotValueOverrideMapProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.SlotValueOverrideProperty",
        jsii_struct_bases=[],
        name_mapping={"shape": "shape", "value": "value", "values": "values"},
    )
    class SlotValueOverrideProperty:
        def __init__(
            self,
            *,
            shape: typing.Optional[builtins.str] = None,
            value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.SlotValueProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            values: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.SlotValueOverrideProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The slot values that Amazon Lex uses when it sets slot values in a dialog step.

            :param shape: When the shape value is ``List`` , it indicates that the ``values`` field contains a list of slot values. When the value is ``Scalar`` , it indicates that the ``value`` field contains a single value.
            :param value: The current value of the slot.
            :param values: A list of one or more values that the user provided for the slot. For example, for a slot that elicits pizza toppings, the values might be "pepperoni" and "pineapple."

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueoverride.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                # slot_value_override_property_: lex.CfnBot.SlotValueOverrideProperty
                
                slot_value_override_property = lex.CfnBot.SlotValueOverrideProperty(
                    shape="shape",
                    value=lex.CfnBot.SlotValueProperty(
                        interpreted_value="interpretedValue"
                    ),
                    values=[slot_value_override_property_]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3ff2a20d96561d546b729ca1c6e001b71dd8660a7430b36467df603c304e847b)
                check_type(argname="argument shape", value=shape, expected_type=type_hints["shape"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if shape is not None:
                self._values["shape"] = shape
            if value is not None:
                self._values["value"] = value
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def shape(self) -> typing.Optional[builtins.str]:
            '''When the shape value is ``List`` , it indicates that the ``values`` field contains a list of slot values.

            When the value is ``Scalar`` , it indicates that the ``value`` field contains a single value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueoverride.html#cfn-lex-bot-slotvalueoverride-shape
            '''
            result = self._values.get("shape")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotValueProperty"]]:
            '''The current value of the slot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueoverride.html#cfn-lex-bot-slotvalueoverride-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotValueProperty"]], result)

        @builtins.property
        def values(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotValueOverrideProperty"]]]]:
            '''A list of one or more values that the user provided for the slot.

            For example, for a slot that elicits pizza toppings, the values might be "pepperoni" and "pineapple."

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueoverride.html#cfn-lex-bot-slotvalueoverride-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotValueOverrideProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SlotValueOverrideProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.SlotValueProperty",
        jsii_struct_bases=[],
        name_mapping={"interpreted_value": "interpretedValue"},
    )
    class SlotValueProperty:
        def __init__(
            self,
            *,
            interpreted_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The value to set in a slot.

            :param interpreted_value: The value that Amazon Lex determines for the slot. The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the ``resolvedValues`` list.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                slot_value_property = lex.CfnBot.SlotValueProperty(
                    interpreted_value="interpretedValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bc3bcf0314f94e50ecf8c32547e6dcf7dd41e4579aad48e2fbf208dd1e976cfa)
                check_type(argname="argument interpreted_value", value=interpreted_value, expected_type=type_hints["interpreted_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if interpreted_value is not None:
                self._values["interpreted_value"] = interpreted_value

        @builtins.property
        def interpreted_value(self) -> typing.Optional[builtins.str]:
            '''The value that Amazon Lex determines for the slot.

            The actual value depends on the setting of the value selection strategy for the bot. You can choose to use the value entered by the user, or you can have Amazon Lex choose the first value in the ``resolvedValues`` list.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalue.html#cfn-lex-bot-slotvalue-interpretedvalue
            '''
            result = self._values.get("interpreted_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SlotValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.SlotValueRegexFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"pattern": "pattern"},
    )
    class SlotValueRegexFilterProperty:
        def __init__(self, *, pattern: builtins.str) -> None:
            '''Provides a regular expression used to validate the value of a slot.

            :param pattern: A regular expression used to validate the value of a slot. Use a standard regular expression. Amazon Lex supports the following characters in the regular expression: - A-Z, a-z - 0-9 - Unicode characters ("\\⁠u") Represent Unicode characters with four digits, for example "\\⁠u0041" or "\\⁠u005A". The following regular expression operators are not supported: - Infinite repeaters: *, +, or {x,} with no upper bound. - Wild card (.)

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueregexfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                slot_value_regex_filter_property = lex.CfnBot.SlotValueRegexFilterProperty(
                    pattern="pattern"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__47fc35e110af5848c29f6beb9a83c5fb75061e0fd18a87c5ac25be2748bf153f)
                check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "pattern": pattern,
            }

        @builtins.property
        def pattern(self) -> builtins.str:
            '''A regular expression used to validate the value of a slot.

            Use a standard regular expression. Amazon Lex supports the following characters in the regular expression:

            - A-Z, a-z
            - 0-9
            - Unicode characters ("\\⁠u")

            Represent Unicode characters with four digits, for example "\\⁠u0041" or "\\⁠u005A".

            The following regular expression operators are not supported:

            - Infinite repeaters: *, +, or {x,} with no upper bound.
            - Wild card (.)

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueregexfilter.html#cfn-lex-bot-slotvalueregexfilter-pattern
            '''
            result = self._values.get("pattern")
            assert result is not None, "Required property 'pattern' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SlotValueRegexFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.SlotValueSelectionSettingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "resolution_strategy": "resolutionStrategy",
            "advanced_recognition_setting": "advancedRecognitionSetting",
            "regex_filter": "regexFilter",
        },
    )
    class SlotValueSelectionSettingProperty:
        def __init__(
            self,
            *,
            resolution_strategy: builtins.str,
            advanced_recognition_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.AdvancedRecognitionSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            regex_filter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.SlotValueRegexFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains settings used by Amazon Lex to select a slot value.

            :param resolution_strategy: Determines the slot resolution strategy that Amazon Lex uses to return slot type values. The field can be set to one of the following values: - ``ORIGINAL_VALUE`` - Returns the value entered by the user, if the user value is similar to the slot value. - ``TOP_RESOLUTION`` - If there is a resolution list for the slot, return the first value in the resolution list as the slot type value. If there is no resolution list, null is returned. If you don't specify the ``valueSelectionStrategy`` , the default is ``ORIGINAL_VALUE`` .
            :param advanced_recognition_setting: Provides settings that enable advanced recognition settings for slot values. You can use this to enable using slot values as a custom vocabulary for recognizing user utterances.
            :param regex_filter: A regular expression used to validate the value of a slot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueselectionsetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                slot_value_selection_setting_property = lex.CfnBot.SlotValueSelectionSettingProperty(
                    resolution_strategy="resolutionStrategy",
                
                    # the properties below are optional
                    advanced_recognition_setting=lex.CfnBot.AdvancedRecognitionSettingProperty(
                        audio_recognition_strategy="audioRecognitionStrategy"
                    ),
                    regex_filter=lex.CfnBot.SlotValueRegexFilterProperty(
                        pattern="pattern"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7982c47931169a42f1aa99bdc61da96e42f63e5371b26a267f1cdadef30b4142)
                check_type(argname="argument resolution_strategy", value=resolution_strategy, expected_type=type_hints["resolution_strategy"])
                check_type(argname="argument advanced_recognition_setting", value=advanced_recognition_setting, expected_type=type_hints["advanced_recognition_setting"])
                check_type(argname="argument regex_filter", value=regex_filter, expected_type=type_hints["regex_filter"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resolution_strategy": resolution_strategy,
            }
            if advanced_recognition_setting is not None:
                self._values["advanced_recognition_setting"] = advanced_recognition_setting
            if regex_filter is not None:
                self._values["regex_filter"] = regex_filter

        @builtins.property
        def resolution_strategy(self) -> builtins.str:
            '''Determines the slot resolution strategy that Amazon Lex uses to return slot type values.

            The field can be set to one of the following values:

            - ``ORIGINAL_VALUE`` - Returns the value entered by the user, if the user value is similar to the slot value.
            - ``TOP_RESOLUTION`` - If there is a resolution list for the slot, return the first value in the resolution list as the slot type value. If there is no resolution list, null is returned.

            If you don't specify the ``valueSelectionStrategy`` , the default is ``ORIGINAL_VALUE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueselectionsetting.html#cfn-lex-bot-slotvalueselectionsetting-resolutionstrategy
            '''
            result = self._values.get("resolution_strategy")
            assert result is not None, "Required property 'resolution_strategy' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def advanced_recognition_setting(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.AdvancedRecognitionSettingProperty"]]:
            '''Provides settings that enable advanced recognition settings for slot values.

            You can use this to enable using slot values as a custom vocabulary for recognizing user utterances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueselectionsetting.html#cfn-lex-bot-slotvalueselectionsetting-advancedrecognitionsetting
            '''
            result = self._values.get("advanced_recognition_setting")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.AdvancedRecognitionSettingProperty"]], result)

        @builtins.property
        def regex_filter(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotValueRegexFilterProperty"]]:
            '''A regular expression used to validate the value of a slot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-slotvalueselectionsetting.html#cfn-lex-bot-slotvalueselectionsetting-regexfilter
            '''
            result = self._values.get("regex_filter")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.SlotValueRegexFilterProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SlotValueSelectionSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.StillWaitingResponseSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "frequency_in_seconds": "frequencyInSeconds",
            "message_groups_list": "messageGroupsList",
            "timeout_in_seconds": "timeoutInSeconds",
            "allow_interrupt": "allowInterrupt",
        },
    )
    class StillWaitingResponseSpecificationProperty:
        def __init__(
            self,
            *,
            frequency_in_seconds: jsii.Number,
            message_groups_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.MessageGroupProperty", typing.Dict[builtins.str, typing.Any]]]]],
            timeout_in_seconds: jsii.Number,
            allow_interrupt: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Defines the messages that Amazon Lex sends to a user to remind them that the bot is waiting for a response.

            :param frequency_in_seconds: How often a message should be sent to the user. Minimum of 1 second, maximum of 5 minutes.
            :param message_groups_list: One or more message groups, each containing one or more messages, that define the prompts that Amazon Lex sends to the user.
            :param timeout_in_seconds: If Amazon Lex waits longer than this length of time for a response, it will stop sending messages.
            :param allow_interrupt: Indicates that the user can interrupt the response by speaking while the message is being played.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-stillwaitingresponsespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                still_waiting_response_specification_property = lex.CfnBot.StillWaitingResponseSpecificationProperty(
                    frequency_in_seconds=123,
                    message_groups_list=[lex.CfnBot.MessageGroupProperty(
                        message=lex.CfnBot.MessageProperty(
                            custom_payload=lex.CfnBot.CustomPayloadProperty(
                                value="value"
                            ),
                            image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                title="title",
                
                                # the properties below are optional
                                buttons=[lex.CfnBot.ButtonProperty(
                                    text="text",
                                    value="value"
                                )],
                                image_url="imageUrl",
                                subtitle="subtitle"
                            ),
                            plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                value="value"
                            ),
                            ssml_message=lex.CfnBot.SSMLMessageProperty(
                                value="value"
                            )
                        ),
                
                        # the properties below are optional
                        variations=[lex.CfnBot.MessageProperty(
                            custom_payload=lex.CfnBot.CustomPayloadProperty(
                                value="value"
                            ),
                            image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                title="title",
                
                                # the properties below are optional
                                buttons=[lex.CfnBot.ButtonProperty(
                                    text="text",
                                    value="value"
                                )],
                                image_url="imageUrl",
                                subtitle="subtitle"
                            ),
                            plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                value="value"
                            ),
                            ssml_message=lex.CfnBot.SSMLMessageProperty(
                                value="value"
                            )
                        )]
                    )],
                    timeout_in_seconds=123,
                
                    # the properties below are optional
                    allow_interrupt=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4b29454e1c72d163c3d5c059ab5734a392267a9f5ea3476cbc3a7c07126ce2e5)
                check_type(argname="argument frequency_in_seconds", value=frequency_in_seconds, expected_type=type_hints["frequency_in_seconds"])
                check_type(argname="argument message_groups_list", value=message_groups_list, expected_type=type_hints["message_groups_list"])
                check_type(argname="argument timeout_in_seconds", value=timeout_in_seconds, expected_type=type_hints["timeout_in_seconds"])
                check_type(argname="argument allow_interrupt", value=allow_interrupt, expected_type=type_hints["allow_interrupt"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "frequency_in_seconds": frequency_in_seconds,
                "message_groups_list": message_groups_list,
                "timeout_in_seconds": timeout_in_seconds,
            }
            if allow_interrupt is not None:
                self._values["allow_interrupt"] = allow_interrupt

        @builtins.property
        def frequency_in_seconds(self) -> jsii.Number:
            '''How often a message should be sent to the user.

            Minimum of 1 second, maximum of 5 minutes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-stillwaitingresponsespecification.html#cfn-lex-bot-stillwaitingresponsespecification-frequencyinseconds
            '''
            result = self._values.get("frequency_in_seconds")
            assert result is not None, "Required property 'frequency_in_seconds' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def message_groups_list(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.MessageGroupProperty"]]]:
            '''One or more message groups, each containing one or more messages, that define the prompts that Amazon Lex sends to the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-stillwaitingresponsespecification.html#cfn-lex-bot-stillwaitingresponsespecification-messagegroupslist
            '''
            result = self._values.get("message_groups_list")
            assert result is not None, "Required property 'message_groups_list' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.MessageGroupProperty"]]], result)

        @builtins.property
        def timeout_in_seconds(self) -> jsii.Number:
            '''If Amazon Lex waits longer than this length of time for a response, it will stop sending messages.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-stillwaitingresponsespecification.html#cfn-lex-bot-stillwaitingresponsespecification-timeoutinseconds
            '''
            result = self._values.get("timeout_in_seconds")
            assert result is not None, "Required property 'timeout_in_seconds' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def allow_interrupt(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates that the user can interrupt the response by speaking while the message is being played.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-stillwaitingresponsespecification.html#cfn-lex-bot-stillwaitingresponsespecification-allowinterrupt
            '''
            result = self._values.get("allow_interrupt")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StillWaitingResponseSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.TestBotAliasSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bot_alias_locale_settings": "botAliasLocaleSettings",
            "conversation_log_settings": "conversationLogSettings",
            "description": "description",
            "sentiment_analysis_settings": "sentimentAnalysisSettings",
        },
    )
    class TestBotAliasSettingsProperty:
        def __init__(
            self,
            *,
            bot_alias_locale_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.BotAliasLocaleSettingsItemProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            conversation_log_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ConversationLogSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            description: typing.Optional[builtins.str] = None,
            sentiment_analysis_settings: typing.Any = None,
        ) -> None:
            '''Specifies configuration settings for the alias used to test the bot.

            If the ``TestBotAliasSettings`` property is not specified, the settings are configured with default values.

            :param bot_alias_locale_settings: Specifies settings that are unique to a locale. For example, you can use a different Lambda function depending on the bot's locale.
            :param conversation_log_settings: Specifies settings for conversation logs that save audio, text, and metadata information for conversations with your users.
            :param description: Specifies a description for the test bot alias.
            :param sentiment_analysis_settings: Specifies whether Amazon Lex will use Amazon Comprehend to detect the sentiment of user utterances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-testbotaliassettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                # sentiment_analysis_settings: Any
                
                test_bot_alias_settings_property = lex.CfnBot.TestBotAliasSettingsProperty(
                    bot_alias_locale_settings=[lex.CfnBot.BotAliasLocaleSettingsItemProperty(
                        bot_alias_locale_setting=lex.CfnBot.BotAliasLocaleSettingsProperty(
                            enabled=False,
                
                            # the properties below are optional
                            code_hook_specification=lex.CfnBot.CodeHookSpecificationProperty(
                                lambda_code_hook=lex.CfnBot.LambdaCodeHookProperty(
                                    code_hook_interface_version="codeHookInterfaceVersion",
                                    lambda_arn="lambdaArn"
                                )
                            )
                        ),
                        locale_id="localeId"
                    )],
                    conversation_log_settings=lex.CfnBot.ConversationLogSettingsProperty(
                        audio_log_settings=[lex.CfnBot.AudioLogSettingProperty(
                            destination=lex.CfnBot.AudioLogDestinationProperty(
                                s3_bucket=lex.CfnBot.S3BucketLogDestinationProperty(
                                    log_prefix="logPrefix",
                                    s3_bucket_arn="s3BucketArn",
                
                                    # the properties below are optional
                                    kms_key_arn="kmsKeyArn"
                                )
                            ),
                            enabled=False
                        )],
                        text_log_settings=[lex.CfnBot.TextLogSettingProperty(
                            destination=lex.CfnBot.TextLogDestinationProperty(
                                cloud_watch=lex.CfnBot.CloudWatchLogGroupLogDestinationProperty(
                                    cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                                    log_prefix="logPrefix"
                                )
                            ),
                            enabled=False
                        )]
                    ),
                    description="description",
                    sentiment_analysis_settings=sentiment_analysis_settings
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9e4446d39358c5287d9df3b2990e64fd6f58a3cb8c75321845b0c566e4ddd896)
                check_type(argname="argument bot_alias_locale_settings", value=bot_alias_locale_settings, expected_type=type_hints["bot_alias_locale_settings"])
                check_type(argname="argument conversation_log_settings", value=conversation_log_settings, expected_type=type_hints["conversation_log_settings"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument sentiment_analysis_settings", value=sentiment_analysis_settings, expected_type=type_hints["sentiment_analysis_settings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bot_alias_locale_settings is not None:
                self._values["bot_alias_locale_settings"] = bot_alias_locale_settings
            if conversation_log_settings is not None:
                self._values["conversation_log_settings"] = conversation_log_settings
            if description is not None:
                self._values["description"] = description
            if sentiment_analysis_settings is not None:
                self._values["sentiment_analysis_settings"] = sentiment_analysis_settings

        @builtins.property
        def bot_alias_locale_settings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.BotAliasLocaleSettingsItemProperty"]]]]:
            '''Specifies settings that are unique to a locale.

            For example, you can use a different Lambda function depending on the bot's locale.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-testbotaliassettings.html#cfn-lex-bot-testbotaliassettings-botaliaslocalesettings
            '''
            result = self._values.get("bot_alias_locale_settings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBot.BotAliasLocaleSettingsItemProperty"]]]], result)

        @builtins.property
        def conversation_log_settings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConversationLogSettingsProperty"]]:
            '''Specifies settings for conversation logs that save audio, text, and metadata information for conversations with your users.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-testbotaliassettings.html#cfn-lex-bot-testbotaliassettings-conversationlogsettings
            '''
            result = self._values.get("conversation_log_settings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.ConversationLogSettingsProperty"]], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''Specifies a description for the test bot alias.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-testbotaliassettings.html#cfn-lex-bot-testbotaliassettings-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sentiment_analysis_settings(self) -> typing.Any:
            '''Specifies whether Amazon Lex will use Amazon Comprehend to detect the sentiment of user utterances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-testbotaliassettings.html#cfn-lex-bot-testbotaliassettings-sentimentanalysissettings
            '''
            result = self._values.get("sentiment_analysis_settings")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TestBotAliasSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.TextInputSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"start_timeout_ms": "startTimeoutMs"},
    )
    class TextInputSpecificationProperty:
        def __init__(self, *, start_timeout_ms: jsii.Number) -> None:
            '''Specifies the text input specifications.

            :param start_timeout_ms: Time for which a bot waits before re-prompting a customer for text input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-textinputspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                text_input_specification_property = lex.CfnBot.TextInputSpecificationProperty(
                    start_timeout_ms=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__257481b35f3cd3f858136fad730402a318d316c1dab41bb5193ce3e69d9cd906)
                check_type(argname="argument start_timeout_ms", value=start_timeout_ms, expected_type=type_hints["start_timeout_ms"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "start_timeout_ms": start_timeout_ms,
            }

        @builtins.property
        def start_timeout_ms(self) -> jsii.Number:
            '''Time for which a bot waits before re-prompting a customer for text input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-textinputspecification.html#cfn-lex-bot-textinputspecification-starttimeoutms
            '''
            result = self._values.get("start_timeout_ms")
            assert result is not None, "Required property 'start_timeout_ms' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TextInputSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.TextLogDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"cloud_watch": "cloudWatch"},
    )
    class TextLogDestinationProperty:
        def __init__(
            self,
            *,
            cloud_watch: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.CloudWatchLogGroupLogDestinationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Defines the Amazon CloudWatch Logs destination log group for conversation text logs.

            :param cloud_watch: Defines the Amazon CloudWatch Logs log group where text and metadata logs are delivered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-textlogdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                text_log_destination_property = lex.CfnBot.TextLogDestinationProperty(
                    cloud_watch=lex.CfnBot.CloudWatchLogGroupLogDestinationProperty(
                        cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                        log_prefix="logPrefix"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8a830897331ded62c92882647499d6a847245a4419c9fd8cfd8605d13d3eac2f)
                check_type(argname="argument cloud_watch", value=cloud_watch, expected_type=type_hints["cloud_watch"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cloud_watch": cloud_watch,
            }

        @builtins.property
        def cloud_watch(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnBot.CloudWatchLogGroupLogDestinationProperty"]:
            '''Defines the Amazon CloudWatch Logs log group where text and metadata logs are delivered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-textlogdestination.html#cfn-lex-bot-textlogdestination-cloudwatch
            '''
            result = self._values.get("cloud_watch")
            assert result is not None, "Required property 'cloud_watch' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBot.CloudWatchLogGroupLogDestinationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TextLogDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.TextLogSettingProperty",
        jsii_struct_bases=[],
        name_mapping={"destination": "destination", "enabled": "enabled"},
    )
    class TextLogSettingProperty:
        def __init__(
            self,
            *,
            destination: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.TextLogDestinationProperty", typing.Dict[builtins.str, typing.Any]]],
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''Defines settings to enable text conversation logs.

            :param destination: Specifies the Amazon CloudWatch Logs destination log group for conversation text logs.
            :param enabled: Determines whether conversation logs should be stored for an alias.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-textlogsetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                text_log_setting_property = lex.CfnBot.TextLogSettingProperty(
                    destination=lex.CfnBot.TextLogDestinationProperty(
                        cloud_watch=lex.CfnBot.CloudWatchLogGroupLogDestinationProperty(
                            cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                            log_prefix="logPrefix"
                        )
                    ),
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__717dfd593b69b20586c4b1f6c63f5b97efa12a2e8cd727b96b019101a312bcc2)
                check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination": destination,
                "enabled": enabled,
            }

        @builtins.property
        def destination(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnBot.TextLogDestinationProperty"]:
            '''Specifies the Amazon CloudWatch Logs destination log group for conversation text logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-textlogsetting.html#cfn-lex-bot-textlogsetting-destination
            '''
            result = self._values.get("destination")
            assert result is not None, "Required property 'destination' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBot.TextLogDestinationProperty"], result)

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Determines whether conversation logs should be stored for an alias.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-textlogsetting.html#cfn-lex-bot-textlogsetting-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TextLogSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.VoiceSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"voice_id": "voiceId", "engine": "engine"},
    )
    class VoiceSettingsProperty:
        def __init__(
            self,
            *,
            voice_id: builtins.str,
            engine: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines settings for using an Amazon Polly voice to communicate with a user.

            :param voice_id: The identifier of the Amazon Polly voice to use.
            :param engine: Indicates the type of Amazon Polly voice that Amazon Lex should use for voice interaction with the user. For more information, see the ```engine`` parameter of the ``SynthesizeSpeech`` operation <https://docs.aws.amazon.com/polly/latest/dg/API_SynthesizeSpeech.html#polly-SynthesizeSpeech-request-Engine>`_ in the *Amazon Polly developer guide* . If you do not specify a value, the default is ``standard`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-voicesettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                voice_settings_property = lex.CfnBot.VoiceSettingsProperty(
                    voice_id="voiceId",
                
                    # the properties below are optional
                    engine="engine"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__afa285d252c1df4a0956dfe0bb68d0cc1b9d6ee0f0ea8e02d91cd9f1c9c53aab)
                check_type(argname="argument voice_id", value=voice_id, expected_type=type_hints["voice_id"])
                check_type(argname="argument engine", value=engine, expected_type=type_hints["engine"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "voice_id": voice_id,
            }
            if engine is not None:
                self._values["engine"] = engine

        @builtins.property
        def voice_id(self) -> builtins.str:
            '''The identifier of the Amazon Polly voice to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-voicesettings.html#cfn-lex-bot-voicesettings-voiceid
            '''
            result = self._values.get("voice_id")
            assert result is not None, "Required property 'voice_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def engine(self) -> typing.Optional[builtins.str]:
            '''Indicates the type of Amazon Polly voice that Amazon Lex should use for voice interaction with the user.

            For more information, see the ```engine`` parameter of the ``SynthesizeSpeech`` operation <https://docs.aws.amazon.com/polly/latest/dg/API_SynthesizeSpeech.html#polly-SynthesizeSpeech-request-Engine>`_ in the *Amazon Polly developer guide* .

            If you do not specify a value, the default is ``standard`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-voicesettings.html#cfn-lex-bot-voicesettings-engine
            '''
            result = self._values.get("engine")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VoiceSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBot.WaitAndContinueSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "continue_response": "continueResponse",
            "waiting_response": "waitingResponse",
            "is_active": "isActive",
            "still_waiting_response": "stillWaitingResponse",
        },
    )
    class WaitAndContinueSpecificationProperty:
        def __init__(
            self,
            *,
            continue_response: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ResponseSpecificationProperty", typing.Dict[builtins.str, typing.Any]]],
            waiting_response: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.ResponseSpecificationProperty", typing.Dict[builtins.str, typing.Any]]],
            is_active: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            still_waiting_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBot.StillWaitingResponseSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the prompts that Amazon Lex uses while a bot is waiting for customer input.

            :param continue_response: The response that Amazon Lex sends to indicate that the bot is ready to continue the conversation.
            :param waiting_response: The response that Amazon Lex sends to indicate that the bot is waiting for the conversation to continue.
            :param is_active: Specifies whether the bot will wait for a user to respond. When this field is false, wait and continue responses for a slot aren't used. If the ``IsActive`` field isn't specified, the default is true.
            :param still_waiting_response: A response that Amazon Lex sends periodically to the user to indicate that the bot is still waiting for input from the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-waitandcontinuespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                wait_and_continue_specification_property = lex.CfnBot.WaitAndContinueSpecificationProperty(
                    continue_response=lex.CfnBot.ResponseSpecificationProperty(
                        message_groups_list=[lex.CfnBot.MessageGroupProperty(
                            message=lex.CfnBot.MessageProperty(
                                custom_payload=lex.CfnBot.CustomPayloadProperty(
                                    value="value"
                                ),
                                image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                    title="title",
                
                                    # the properties below are optional
                                    buttons=[lex.CfnBot.ButtonProperty(
                                        text="text",
                                        value="value"
                                    )],
                                    image_url="imageUrl",
                                    subtitle="subtitle"
                                ),
                                plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                    value="value"
                                ),
                                ssml_message=lex.CfnBot.SSMLMessageProperty(
                                    value="value"
                                )
                            ),
                
                            # the properties below are optional
                            variations=[lex.CfnBot.MessageProperty(
                                custom_payload=lex.CfnBot.CustomPayloadProperty(
                                    value="value"
                                ),
                                image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                    title="title",
                
                                    # the properties below are optional
                                    buttons=[lex.CfnBot.ButtonProperty(
                                        text="text",
                                        value="value"
                                    )],
                                    image_url="imageUrl",
                                    subtitle="subtitle"
                                ),
                                plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                    value="value"
                                ),
                                ssml_message=lex.CfnBot.SSMLMessageProperty(
                                    value="value"
                                )
                            )]
                        )],
                
                        # the properties below are optional
                        allow_interrupt=False
                    ),
                    waiting_response=lex.CfnBot.ResponseSpecificationProperty(
                        message_groups_list=[lex.CfnBot.MessageGroupProperty(
                            message=lex.CfnBot.MessageProperty(
                                custom_payload=lex.CfnBot.CustomPayloadProperty(
                                    value="value"
                                ),
                                image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                    title="title",
                
                                    # the properties below are optional
                                    buttons=[lex.CfnBot.ButtonProperty(
                                        text="text",
                                        value="value"
                                    )],
                                    image_url="imageUrl",
                                    subtitle="subtitle"
                                ),
                                plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                    value="value"
                                ),
                                ssml_message=lex.CfnBot.SSMLMessageProperty(
                                    value="value"
                                )
                            ),
                
                            # the properties below are optional
                            variations=[lex.CfnBot.MessageProperty(
                                custom_payload=lex.CfnBot.CustomPayloadProperty(
                                    value="value"
                                ),
                                image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                    title="title",
                
                                    # the properties below are optional
                                    buttons=[lex.CfnBot.ButtonProperty(
                                        text="text",
                                        value="value"
                                    )],
                                    image_url="imageUrl",
                                    subtitle="subtitle"
                                ),
                                plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                    value="value"
                                ),
                                ssml_message=lex.CfnBot.SSMLMessageProperty(
                                    value="value"
                                )
                            )]
                        )],
                
                        # the properties below are optional
                        allow_interrupt=False
                    ),
                
                    # the properties below are optional
                    is_active=False,
                    still_waiting_response=lex.CfnBot.StillWaitingResponseSpecificationProperty(
                        frequency_in_seconds=123,
                        message_groups_list=[lex.CfnBot.MessageGroupProperty(
                            message=lex.CfnBot.MessageProperty(
                                custom_payload=lex.CfnBot.CustomPayloadProperty(
                                    value="value"
                                ),
                                image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                    title="title",
                
                                    # the properties below are optional
                                    buttons=[lex.CfnBot.ButtonProperty(
                                        text="text",
                                        value="value"
                                    )],
                                    image_url="imageUrl",
                                    subtitle="subtitle"
                                ),
                                plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                    value="value"
                                ),
                                ssml_message=lex.CfnBot.SSMLMessageProperty(
                                    value="value"
                                )
                            ),
                
                            # the properties below are optional
                            variations=[lex.CfnBot.MessageProperty(
                                custom_payload=lex.CfnBot.CustomPayloadProperty(
                                    value="value"
                                ),
                                image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                    title="title",
                
                                    # the properties below are optional
                                    buttons=[lex.CfnBot.ButtonProperty(
                                        text="text",
                                        value="value"
                                    )],
                                    image_url="imageUrl",
                                    subtitle="subtitle"
                                ),
                                plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                    value="value"
                                ),
                                ssml_message=lex.CfnBot.SSMLMessageProperty(
                                    value="value"
                                )
                            )]
                        )],
                        timeout_in_seconds=123,
                
                        # the properties below are optional
                        allow_interrupt=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__21656b0cba2d8c5320337a8a5bc150ba2c7097fdcd22e75137a6284ac3c9ab3d)
                check_type(argname="argument continue_response", value=continue_response, expected_type=type_hints["continue_response"])
                check_type(argname="argument waiting_response", value=waiting_response, expected_type=type_hints["waiting_response"])
                check_type(argname="argument is_active", value=is_active, expected_type=type_hints["is_active"])
                check_type(argname="argument still_waiting_response", value=still_waiting_response, expected_type=type_hints["still_waiting_response"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "continue_response": continue_response,
                "waiting_response": waiting_response,
            }
            if is_active is not None:
                self._values["is_active"] = is_active
            if still_waiting_response is not None:
                self._values["still_waiting_response"] = still_waiting_response

        @builtins.property
        def continue_response(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]:
            '''The response that Amazon Lex sends to indicate that the bot is ready to continue the conversation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-waitandcontinuespecification.html#cfn-lex-bot-waitandcontinuespecification-continueresponse
            '''
            result = self._values.get("continue_response")
            assert result is not None, "Required property 'continue_response' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"], result)

        @builtins.property
        def waiting_response(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"]:
            '''The response that Amazon Lex sends to indicate that the bot is waiting for the conversation to continue.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-waitandcontinuespecification.html#cfn-lex-bot-waitandcontinuespecification-waitingresponse
            '''
            result = self._values.get("waiting_response")
            assert result is not None, "Required property 'waiting_response' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBot.ResponseSpecificationProperty"], result)

        @builtins.property
        def is_active(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether the bot will wait for a user to respond.

            When this field is false, wait and continue responses for a slot aren't used. If the ``IsActive`` field isn't specified, the default is true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-waitandcontinuespecification.html#cfn-lex-bot-waitandcontinuespecification-isactive
            '''
            result = self._values.get("is_active")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def still_waiting_response(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.StillWaitingResponseSpecificationProperty"]]:
            '''A response that Amazon Lex sends periodically to the user to indicate that the bot is still waiting for input from the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-bot-waitandcontinuespecification.html#cfn-lex-bot-waitandcontinuespecification-stillwaitingresponse
            '''
            result = self._values.get("still_waiting_response")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBot.StillWaitingResponseSpecificationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WaitAndContinueSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnBotAlias(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lex.CfnBotAlias",
):
    '''.. epigraph::

   Amazon Lex V2 is the only supported version in AWS CloudFormation .

    Specifies an alias for the specified version of a bot. Use an alias to enable you to change the version of a bot without updating applications that use the bot.

    For example, you can specify an alias called "PROD" that your applications use to call the Amazon Lex bot.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lex as lex
        
        # sentiment_analysis_settings: Any
        
        cfn_bot_alias = lex.CfnBotAlias(self, "MyCfnBotAlias",
            bot_alias_name="botAliasName",
            bot_id="botId",
        
            # the properties below are optional
            bot_alias_locale_settings=[lex.CfnBotAlias.BotAliasLocaleSettingsItemProperty(
                bot_alias_locale_setting=lex.CfnBotAlias.BotAliasLocaleSettingsProperty(
                    enabled=False,
        
                    # the properties below are optional
                    code_hook_specification=lex.CfnBotAlias.CodeHookSpecificationProperty(
                        lambda_code_hook=lex.CfnBotAlias.LambdaCodeHookProperty(
                            code_hook_interface_version="codeHookInterfaceVersion",
                            lambda_arn="lambdaArn"
                        )
                    )
                ),
                locale_id="localeId"
            )],
            bot_alias_tags=[CfnTag(
                key="key",
                value="value"
            )],
            bot_version="botVersion",
            conversation_log_settings=lex.CfnBotAlias.ConversationLogSettingsProperty(
                audio_log_settings=[lex.CfnBotAlias.AudioLogSettingProperty(
                    destination=lex.CfnBotAlias.AudioLogDestinationProperty(
                        s3_bucket=lex.CfnBotAlias.S3BucketLogDestinationProperty(
                            log_prefix="logPrefix",
                            s3_bucket_arn="s3BucketArn",
        
                            # the properties below are optional
                            kms_key_arn="kmsKeyArn"
                        )
                    ),
                    enabled=False
                )],
                text_log_settings=[lex.CfnBotAlias.TextLogSettingProperty(
                    destination=lex.CfnBotAlias.TextLogDestinationProperty(
                        cloud_watch=lex.CfnBotAlias.CloudWatchLogGroupLogDestinationProperty(
                            cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                            log_prefix="logPrefix"
                        )
                    ),
                    enabled=False
                )]
            ),
            description="description",
            sentiment_analysis_settings=sentiment_analysis_settings
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        bot_alias_name: builtins.str,
        bot_id: builtins.str,
        bot_alias_locale_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBotAlias.BotAliasLocaleSettingsItemProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        bot_alias_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        bot_version: typing.Optional[builtins.str] = None,
        conversation_log_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBotAlias.ConversationLogSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        sentiment_analysis_settings: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param bot_alias_name: The name of the bot alias.
        :param bot_id: The unique identifier of the bot.
        :param bot_alias_locale_settings: Specifies settings that are unique to a locale. For example, you can use different Lambda function depending on the bot's locale.
        :param bot_alias_tags: An array of key-value pairs to apply to this resource. You can only add tags when you specify an alias. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param bot_version: The version of the bot that the bot alias references.
        :param conversation_log_settings: Specifies whether Amazon Lex logs text and audio for conversations with the bot. When you enable conversation logs, text logs store text input, transcripts of audio input, and associated metadata in Amazon CloudWatch logs. Audio logs store input in Amazon S3 .
        :param description: The description of the bot alias.
        :param sentiment_analysis_settings: Determines whether Amazon Lex will use Amazon Comprehend to detect the sentiment of user utterances.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57cf179c443f74ff3b1c43c56eef686f369711792e444e53d5668f07ac682866)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBotAliasProps(
            bot_alias_name=bot_alias_name,
            bot_id=bot_id,
            bot_alias_locale_settings=bot_alias_locale_settings,
            bot_alias_tags=bot_alias_tags,
            bot_version=bot_version,
            conversation_log_settings=conversation_log_settings,
            description=description,
            sentiment_analysis_settings=sentiment_analysis_settings,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69e306fef7aca1ecd05a385248f8253ae3fef56958f84e69c038125bb4b466d0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__82906237840a0ec10e1166b52ceb1e62975a24e550f8f48c4e2935150c7960fe)
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
        '''The Amazon Resource Name (ARN) of the bot alias.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrBotAliasId")
    def attr_bot_alias_id(self) -> builtins.str:
        '''The unique identifier of the bot alias.

        :cloudformationAttribute: BotAliasId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBotAliasId"))

    @builtins.property
    @jsii.member(jsii_name="attrBotAliasStatus")
    def attr_bot_alias_status(self) -> builtins.str:
        '''The current status of the bot alias.

        When the status is Available the alias is ready for use with your bot.

        :cloudformationAttribute: BotAliasStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBotAliasStatus"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="botAliasName")
    def bot_alias_name(self) -> builtins.str:
        '''The name of the bot alias.'''
        return typing.cast(builtins.str, jsii.get(self, "botAliasName"))

    @bot_alias_name.setter
    def bot_alias_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7c080b499a50788ae164c44975b98220147f762edd4ec214c0e6f9124445093)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "botAliasName", value)

    @builtins.property
    @jsii.member(jsii_name="botId")
    def bot_id(self) -> builtins.str:
        '''The unique identifier of the bot.'''
        return typing.cast(builtins.str, jsii.get(self, "botId"))

    @bot_id.setter
    def bot_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43cce0d64f81ea520d08b83a4aa6aece3a2341b6dde0b7fcd65a8f847f5de3f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "botId", value)

    @builtins.property
    @jsii.member(jsii_name="botAliasLocaleSettings")
    def bot_alias_locale_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBotAlias.BotAliasLocaleSettingsItemProperty"]]]]:
        '''Specifies settings that are unique to a locale.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBotAlias.BotAliasLocaleSettingsItemProperty"]]]], jsii.get(self, "botAliasLocaleSettings"))

    @bot_alias_locale_settings.setter
    def bot_alias_locale_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBotAlias.BotAliasLocaleSettingsItemProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__917790158810f6fc38fb5d4372a10a9584fb6d4764bb1d87be8244cc727936e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "botAliasLocaleSettings", value)

    @builtins.property
    @jsii.member(jsii_name="botAliasTags")
    def bot_alias_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]], jsii.get(self, "botAliasTags"))

    @bot_alias_tags.setter
    def bot_alias_tags(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71d610b69d60b87626f698f0118b5837b8126b661b02cb75b4961dfeaead9834)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "botAliasTags", value)

    @builtins.property
    @jsii.member(jsii_name="botVersion")
    def bot_version(self) -> typing.Optional[builtins.str]:
        '''The version of the bot that the bot alias references.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "botVersion"))

    @bot_version.setter
    def bot_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__607e7a3cdff2bc65c8c76ca1d05837350e81ade44a258da16439fc17f283acda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "botVersion", value)

    @builtins.property
    @jsii.member(jsii_name="conversationLogSettings")
    def conversation_log_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBotAlias.ConversationLogSettingsProperty"]]:
        '''Specifies whether Amazon Lex logs text and audio for conversations with the bot.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBotAlias.ConversationLogSettingsProperty"]], jsii.get(self, "conversationLogSettings"))

    @conversation_log_settings.setter
    def conversation_log_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBotAlias.ConversationLogSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26855f93261461e56c873baf08145fa32c74a011917251399c4d61392913f877)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "conversationLogSettings", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the bot alias.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf77d628ea97246a31f89b41559277e6cfb829aa4bde51a21dce2c884995deb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="sentimentAnalysisSettings")
    def sentiment_analysis_settings(self) -> typing.Any:
        '''Determines whether Amazon Lex will use Amazon Comprehend to detect the sentiment of user utterances.'''
        return typing.cast(typing.Any, jsii.get(self, "sentimentAnalysisSettings"))

    @sentiment_analysis_settings.setter
    def sentiment_analysis_settings(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8cbd98c4bdfe82bcb165ec91638c6ad68086348b28345eeda6f375cb1a7fcd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sentimentAnalysisSettings", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBotAlias.AudioLogDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_bucket": "s3Bucket"},
    )
    class AudioLogDestinationProperty:
        def __init__(
            self,
            *,
            s3_bucket: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBotAlias.S3BucketLogDestinationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Specifies the S3 bucket location where audio logs are stored.

            :param s3_bucket: The S3 bucket location where audio logs are stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-audiologdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                audio_log_destination_property = lex.CfnBotAlias.AudioLogDestinationProperty(
                    s3_bucket=lex.CfnBotAlias.S3BucketLogDestinationProperty(
                        log_prefix="logPrefix",
                        s3_bucket_arn="s3BucketArn",
                
                        # the properties below are optional
                        kms_key_arn="kmsKeyArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d41a4792f6acf503d602b95e02a66bebf212a7b6908e2a7af00574350149fb86)
                check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3_bucket": s3_bucket,
            }

        @builtins.property
        def s3_bucket(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnBotAlias.S3BucketLogDestinationProperty"]:
            '''The S3 bucket location where audio logs are stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-audiologdestination.html#cfn-lex-botalias-audiologdestination-s3bucket
            '''
            result = self._values.get("s3_bucket")
            assert result is not None, "Required property 's3_bucket' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBotAlias.S3BucketLogDestinationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioLogDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBotAlias.AudioLogSettingProperty",
        jsii_struct_bases=[],
        name_mapping={"destination": "destination", "enabled": "enabled"},
    )
    class AudioLogSettingProperty:
        def __init__(
            self,
            *,
            destination: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBotAlias.AudioLogDestinationProperty", typing.Dict[builtins.str, typing.Any]]],
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''Settings for logging audio of conversations between Amazon Lex and a user.

            You specify whether to log audio and the Amazon S3 bucket where the audio file is stored.

            :param destination: The location of audio log files collected when conversation logging is enabled for a bot.
            :param enabled: Determines whether audio logging in enabled for the bot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-audiologsetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                audio_log_setting_property = lex.CfnBotAlias.AudioLogSettingProperty(
                    destination=lex.CfnBotAlias.AudioLogDestinationProperty(
                        s3_bucket=lex.CfnBotAlias.S3BucketLogDestinationProperty(
                            log_prefix="logPrefix",
                            s3_bucket_arn="s3BucketArn",
                
                            # the properties below are optional
                            kms_key_arn="kmsKeyArn"
                        )
                    ),
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__64da9bcfbd2b2bd9dba3eb1c7ddae66c5d2eeb778bfa000ca200015ca8968205)
                check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination": destination,
                "enabled": enabled,
            }

        @builtins.property
        def destination(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnBotAlias.AudioLogDestinationProperty"]:
            '''The location of audio log files collected when conversation logging is enabled for a bot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-audiologsetting.html#cfn-lex-botalias-audiologsetting-destination
            '''
            result = self._values.get("destination")
            assert result is not None, "Required property 'destination' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBotAlias.AudioLogDestinationProperty"], result)

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Determines whether audio logging in enabled for the bot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-audiologsetting.html#cfn-lex-botalias-audiologsetting-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioLogSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBotAlias.BotAliasLocaleSettingsItemProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bot_alias_locale_setting": "botAliasLocaleSetting",
            "locale_id": "localeId",
        },
    )
    class BotAliasLocaleSettingsItemProperty:
        def __init__(
            self,
            *,
            bot_alias_locale_setting: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBotAlias.BotAliasLocaleSettingsProperty", typing.Dict[builtins.str, typing.Any]]],
            locale_id: builtins.str,
        ) -> None:
            '''Specifies settings that are unique to a locale.

            For example, you can use different Lambda function depending on the bot's locale.

            :param bot_alias_locale_setting: Specifies settings that are unique to a locale.
            :param locale_id: The unique identifier of the locale.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-botaliaslocalesettingsitem.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                bot_alias_locale_settings_item_property = lex.CfnBotAlias.BotAliasLocaleSettingsItemProperty(
                    bot_alias_locale_setting=lex.CfnBotAlias.BotAliasLocaleSettingsProperty(
                        enabled=False,
                
                        # the properties below are optional
                        code_hook_specification=lex.CfnBotAlias.CodeHookSpecificationProperty(
                            lambda_code_hook=lex.CfnBotAlias.LambdaCodeHookProperty(
                                code_hook_interface_version="codeHookInterfaceVersion",
                                lambda_arn="lambdaArn"
                            )
                        )
                    ),
                    locale_id="localeId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4fa90f2791fe89d6201e6271583ea7f187021e13990dfc56fb5b9d21cd0597fc)
                check_type(argname="argument bot_alias_locale_setting", value=bot_alias_locale_setting, expected_type=type_hints["bot_alias_locale_setting"])
                check_type(argname="argument locale_id", value=locale_id, expected_type=type_hints["locale_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bot_alias_locale_setting": bot_alias_locale_setting,
                "locale_id": locale_id,
            }

        @builtins.property
        def bot_alias_locale_setting(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnBotAlias.BotAliasLocaleSettingsProperty"]:
            '''Specifies settings that are unique to a locale.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-botaliaslocalesettingsitem.html#cfn-lex-botalias-botaliaslocalesettingsitem-botaliaslocalesetting
            '''
            result = self._values.get("bot_alias_locale_setting")
            assert result is not None, "Required property 'bot_alias_locale_setting' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBotAlias.BotAliasLocaleSettingsProperty"], result)

        @builtins.property
        def locale_id(self) -> builtins.str:
            '''The unique identifier of the locale.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-botaliaslocalesettingsitem.html#cfn-lex-botalias-botaliaslocalesettingsitem-localeid
            '''
            result = self._values.get("locale_id")
            assert result is not None, "Required property 'locale_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BotAliasLocaleSettingsItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBotAlias.BotAliasLocaleSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "code_hook_specification": "codeHookSpecification",
        },
    )
    class BotAliasLocaleSettingsProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
            code_hook_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBotAlias.CodeHookSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies settings that are unique to a locale.

            For example, you can use different Lambda function depending on the bot's locale.

            :param enabled: Determines whether the locale is enabled for the bot. If the value is ``false`` , the locale isn't available for use.
            :param code_hook_specification: Specifies the Lambda function that should be used in the locale.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-botaliaslocalesettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                bot_alias_locale_settings_property = lex.CfnBotAlias.BotAliasLocaleSettingsProperty(
                    enabled=False,
                
                    # the properties below are optional
                    code_hook_specification=lex.CfnBotAlias.CodeHookSpecificationProperty(
                        lambda_code_hook=lex.CfnBotAlias.LambdaCodeHookProperty(
                            code_hook_interface_version="codeHookInterfaceVersion",
                            lambda_arn="lambdaArn"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dafc846484ddd046f32610ca8300607ee344e453911b95e386338096b5265a0b)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument code_hook_specification", value=code_hook_specification, expected_type=type_hints["code_hook_specification"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled": enabled,
            }
            if code_hook_specification is not None:
                self._values["code_hook_specification"] = code_hook_specification

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Determines whether the locale is enabled for the bot.

            If the value is ``false`` , the locale isn't available for use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-botaliaslocalesettings.html#cfn-lex-botalias-botaliaslocalesettings-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def code_hook_specification(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBotAlias.CodeHookSpecificationProperty"]]:
            '''Specifies the Lambda function that should be used in the locale.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-botaliaslocalesettings.html#cfn-lex-botalias-botaliaslocalesettings-codehookspecification
            '''
            result = self._values.get("code_hook_specification")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBotAlias.CodeHookSpecificationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BotAliasLocaleSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBotAlias.CloudWatchLogGroupLogDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_log_group_arn": "cloudWatchLogGroupArn",
            "log_prefix": "logPrefix",
        },
    )
    class CloudWatchLogGroupLogDestinationProperty:
        def __init__(
            self,
            *,
            cloud_watch_log_group_arn: builtins.str,
            log_prefix: builtins.str,
        ) -> None:
            '''The Amazon CloudWatch Logs log group where the text and metadata logs are delivered.

            The log group must exist before you enable logging.

            :param cloud_watch_log_group_arn: The Amazon Resource Name (ARN) of the log group where text and metadata logs are delivered.
            :param log_prefix: The prefix of the log stream name within the log group that you specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-cloudwatchloggrouplogdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                cloud_watch_log_group_log_destination_property = lex.CfnBotAlias.CloudWatchLogGroupLogDestinationProperty(
                    cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                    log_prefix="logPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d4b6c748ce549d24594ec045dcb720ee3c78bdc65181ef3fcc7e7270aac3dd45)
                check_type(argname="argument cloud_watch_log_group_arn", value=cloud_watch_log_group_arn, expected_type=type_hints["cloud_watch_log_group_arn"])
                check_type(argname="argument log_prefix", value=log_prefix, expected_type=type_hints["log_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cloud_watch_log_group_arn": cloud_watch_log_group_arn,
                "log_prefix": log_prefix,
            }

        @builtins.property
        def cloud_watch_log_group_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the log group where text and metadata logs are delivered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-cloudwatchloggrouplogdestination.html#cfn-lex-botalias-cloudwatchloggrouplogdestination-cloudwatchloggrouparn
            '''
            result = self._values.get("cloud_watch_log_group_arn")
            assert result is not None, "Required property 'cloud_watch_log_group_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def log_prefix(self) -> builtins.str:
            '''The prefix of the log stream name within the log group that you specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-cloudwatchloggrouplogdestination.html#cfn-lex-botalias-cloudwatchloggrouplogdestination-logprefix
            '''
            result = self._values.get("log_prefix")
            assert result is not None, "Required property 'log_prefix' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLogGroupLogDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBotAlias.CodeHookSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"lambda_code_hook": "lambdaCodeHook"},
    )
    class CodeHookSpecificationProperty:
        def __init__(
            self,
            *,
            lambda_code_hook: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBotAlias.LambdaCodeHookProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Contains information about code hooks that Amazon Lex calls during a conversation.

            :param lambda_code_hook: Specifies a Lambda function that verifies requests to a bot or fulfills the user's request to a bot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-codehookspecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                code_hook_specification_property = lex.CfnBotAlias.CodeHookSpecificationProperty(
                    lambda_code_hook=lex.CfnBotAlias.LambdaCodeHookProperty(
                        code_hook_interface_version="codeHookInterfaceVersion",
                        lambda_arn="lambdaArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6cd567ca149d2ddc4a15e2c8b606a157b295d21d28be7cf8887e0415dc7d1f70)
                check_type(argname="argument lambda_code_hook", value=lambda_code_hook, expected_type=type_hints["lambda_code_hook"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "lambda_code_hook": lambda_code_hook,
            }

        @builtins.property
        def lambda_code_hook(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnBotAlias.LambdaCodeHookProperty"]:
            '''Specifies a Lambda function that verifies requests to a bot or fulfills the user's request to a bot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-codehookspecification.html#cfn-lex-botalias-codehookspecification-lambdacodehook
            '''
            result = self._values.get("lambda_code_hook")
            assert result is not None, "Required property 'lambda_code_hook' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBotAlias.LambdaCodeHookProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeHookSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBotAlias.ConversationLogSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_log_settings": "audioLogSettings",
            "text_log_settings": "textLogSettings",
        },
    )
    class ConversationLogSettingsProperty:
        def __init__(
            self,
            *,
            audio_log_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBotAlias.AudioLogSettingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            text_log_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBotAlias.TextLogSettingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Configures conversation logging that saves audio, text, and metadata for the conversations with your users.

            :param audio_log_settings: The Amazon S3 settings for logging audio to an S3 bucket.
            :param text_log_settings: The Amazon CloudWatch Logs settings for logging text and metadata.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-conversationlogsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                conversation_log_settings_property = lex.CfnBotAlias.ConversationLogSettingsProperty(
                    audio_log_settings=[lex.CfnBotAlias.AudioLogSettingProperty(
                        destination=lex.CfnBotAlias.AudioLogDestinationProperty(
                            s3_bucket=lex.CfnBotAlias.S3BucketLogDestinationProperty(
                                log_prefix="logPrefix",
                                s3_bucket_arn="s3BucketArn",
                
                                # the properties below are optional
                                kms_key_arn="kmsKeyArn"
                            )
                        ),
                        enabled=False
                    )],
                    text_log_settings=[lex.CfnBotAlias.TextLogSettingProperty(
                        destination=lex.CfnBotAlias.TextLogDestinationProperty(
                            cloud_watch=lex.CfnBotAlias.CloudWatchLogGroupLogDestinationProperty(
                                cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                                log_prefix="logPrefix"
                            )
                        ),
                        enabled=False
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6b3bbd49ff07926107022ac3da1633a850323778ca95a0336ced992c0fa69295)
                check_type(argname="argument audio_log_settings", value=audio_log_settings, expected_type=type_hints["audio_log_settings"])
                check_type(argname="argument text_log_settings", value=text_log_settings, expected_type=type_hints["text_log_settings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if audio_log_settings is not None:
                self._values["audio_log_settings"] = audio_log_settings
            if text_log_settings is not None:
                self._values["text_log_settings"] = text_log_settings

        @builtins.property
        def audio_log_settings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBotAlias.AudioLogSettingProperty"]]]]:
            '''The Amazon S3 settings for logging audio to an S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-conversationlogsettings.html#cfn-lex-botalias-conversationlogsettings-audiologsettings
            '''
            result = self._values.get("audio_log_settings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBotAlias.AudioLogSettingProperty"]]]], result)

        @builtins.property
        def text_log_settings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBotAlias.TextLogSettingProperty"]]]]:
            '''The Amazon CloudWatch Logs settings for logging text and metadata.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-conversationlogsettings.html#cfn-lex-botalias-conversationlogsettings-textlogsettings
            '''
            result = self._values.get("text_log_settings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBotAlias.TextLogSettingProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConversationLogSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBotAlias.LambdaCodeHookProperty",
        jsii_struct_bases=[],
        name_mapping={
            "code_hook_interface_version": "codeHookInterfaceVersion",
            "lambda_arn": "lambdaArn",
        },
    )
    class LambdaCodeHookProperty:
        def __init__(
            self,
            *,
            code_hook_interface_version: builtins.str,
            lambda_arn: builtins.str,
        ) -> None:
            '''Specifies a Lambda function that verifies requests to a bot or fulfills the user's request to a bot.

            :param code_hook_interface_version: The version of the request-response that you want Amazon Lex to use to invoke your Lambda function.
            :param lambda_arn: The Amazon Resource Name (ARN) of the Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-lambdacodehook.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                lambda_code_hook_property = lex.CfnBotAlias.LambdaCodeHookProperty(
                    code_hook_interface_version="codeHookInterfaceVersion",
                    lambda_arn="lambdaArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__237ac618bd82501cc4eeef1b6bef37b79a6a110591930a7ca2bdf70a7469971a)
                check_type(argname="argument code_hook_interface_version", value=code_hook_interface_version, expected_type=type_hints["code_hook_interface_version"])
                check_type(argname="argument lambda_arn", value=lambda_arn, expected_type=type_hints["lambda_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "code_hook_interface_version": code_hook_interface_version,
                "lambda_arn": lambda_arn,
            }

        @builtins.property
        def code_hook_interface_version(self) -> builtins.str:
            '''The version of the request-response that you want Amazon Lex to use to invoke your Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-lambdacodehook.html#cfn-lex-botalias-lambdacodehook-codehookinterfaceversion
            '''
            result = self._values.get("code_hook_interface_version")
            assert result is not None, "Required property 'code_hook_interface_version' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def lambda_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-lambdacodehook.html#cfn-lex-botalias-lambdacodehook-lambdaarn
            '''
            result = self._values.get("lambda_arn")
            assert result is not None, "Required property 'lambda_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaCodeHookProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBotAlias.S3BucketLogDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "log_prefix": "logPrefix",
            "s3_bucket_arn": "s3BucketArn",
            "kms_key_arn": "kmsKeyArn",
        },
    )
    class S3BucketLogDestinationProperty:
        def __init__(
            self,
            *,
            log_prefix: builtins.str,
            s3_bucket_arn: builtins.str,
            kms_key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies an Amazon S3 bucket for logging audio conversations.

            :param log_prefix: The S3 prefix to assign to audio log files.
            :param s3_bucket_arn: The Amazon Resource Name (ARN) of an Amazon S3 bucket where audio log files are stored.
            :param kms_key_arn: The Amazon Resource Name (ARN) of an AWS Key Management Service (KMS) key for encrypting audio log files stored in an Amazon S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-s3bucketlogdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                s3_bucket_log_destination_property = lex.CfnBotAlias.S3BucketLogDestinationProperty(
                    log_prefix="logPrefix",
                    s3_bucket_arn="s3BucketArn",
                
                    # the properties below are optional
                    kms_key_arn="kmsKeyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8b1ee0eb3567ddc82ad62e8f5ce649b310fc9a1ef0580dc3d8203fe333ba91cb)
                check_type(argname="argument log_prefix", value=log_prefix, expected_type=type_hints["log_prefix"])
                check_type(argname="argument s3_bucket_arn", value=s3_bucket_arn, expected_type=type_hints["s3_bucket_arn"])
                check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "log_prefix": log_prefix,
                "s3_bucket_arn": s3_bucket_arn,
            }
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn

        @builtins.property
        def log_prefix(self) -> builtins.str:
            '''The S3 prefix to assign to audio log files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-s3bucketlogdestination.html#cfn-lex-botalias-s3bucketlogdestination-logprefix
            '''
            result = self._values.get("log_prefix")
            assert result is not None, "Required property 'log_prefix' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_bucket_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of an Amazon S3 bucket where audio log files are stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-s3bucketlogdestination.html#cfn-lex-botalias-s3bucketlogdestination-s3bucketarn
            '''
            result = self._values.get("s3_bucket_arn")
            assert result is not None, "Required property 's3_bucket_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of an AWS Key Management Service (KMS) key for encrypting audio log files stored in an Amazon S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-s3bucketlogdestination.html#cfn-lex-botalias-s3bucketlogdestination-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3BucketLogDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBotAlias.SentimentAnalysisSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"detect_sentiment": "detectSentiment"},
    )
    class SentimentAnalysisSettingsProperty:
        def __init__(
            self,
            *,
            detect_sentiment: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''Determines whether Amazon Lex will use Amazon Comprehend to detect the sentiment of user utterances.

            :param detect_sentiment: Sets whether Amazon Lex uses Amazon Comprehend to detect the sentiment of user utterances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-sentimentanalysissettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                sentiment_analysis_settings_property = lex.CfnBotAlias.SentimentAnalysisSettingsProperty(
                    detect_sentiment=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__964fd3d3c5e4dd05d12a570da3c37d53cad4c1eb4b1978b3fdb092a2f7ea63be)
                check_type(argname="argument detect_sentiment", value=detect_sentiment, expected_type=type_hints["detect_sentiment"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "detect_sentiment": detect_sentiment,
            }

        @builtins.property
        def detect_sentiment(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Sets whether Amazon Lex uses Amazon Comprehend to detect the sentiment of user utterances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-sentimentanalysissettings.html#cfn-lex-botalias-sentimentanalysissettings-detectsentiment
            '''
            result = self._values.get("detect_sentiment")
            assert result is not None, "Required property 'detect_sentiment' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SentimentAnalysisSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBotAlias.TextLogDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"cloud_watch": "cloudWatch"},
    )
    class TextLogDestinationProperty:
        def __init__(
            self,
            *,
            cloud_watch: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBotAlias.CloudWatchLogGroupLogDestinationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Defines the Amazon CloudWatch Logs destination log group for conversation text logs.

            :param cloud_watch: Defines the Amazon CloudWatch Logs log group where text and metadata logs are delivered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-textlogdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                text_log_destination_property = lex.CfnBotAlias.TextLogDestinationProperty(
                    cloud_watch=lex.CfnBotAlias.CloudWatchLogGroupLogDestinationProperty(
                        cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                        log_prefix="logPrefix"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bedf1e9b290471f5b443d8e1d723d7bf856489156d6ae34dc0371643449b3287)
                check_type(argname="argument cloud_watch", value=cloud_watch, expected_type=type_hints["cloud_watch"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cloud_watch": cloud_watch,
            }

        @builtins.property
        def cloud_watch(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnBotAlias.CloudWatchLogGroupLogDestinationProperty"]:
            '''Defines the Amazon CloudWatch Logs log group where text and metadata logs are delivered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-textlogdestination.html#cfn-lex-botalias-textlogdestination-cloudwatch
            '''
            result = self._values.get("cloud_watch")
            assert result is not None, "Required property 'cloud_watch' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBotAlias.CloudWatchLogGroupLogDestinationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TextLogDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBotAlias.TextLogSettingProperty",
        jsii_struct_bases=[],
        name_mapping={"destination": "destination", "enabled": "enabled"},
    )
    class TextLogSettingProperty:
        def __init__(
            self,
            *,
            destination: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBotAlias.TextLogDestinationProperty", typing.Dict[builtins.str, typing.Any]]],
            enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''Defines settings to enable text conversation logs.

            :param destination: Defines the Amazon CloudWatch Logs destination log group for conversation text logs.
            :param enabled: Determines whether conversation logs should be stored for an alias.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-textlogsetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                text_log_setting_property = lex.CfnBotAlias.TextLogSettingProperty(
                    destination=lex.CfnBotAlias.TextLogDestinationProperty(
                        cloud_watch=lex.CfnBotAlias.CloudWatchLogGroupLogDestinationProperty(
                            cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                            log_prefix="logPrefix"
                        )
                    ),
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__36c17e23b7248b4c9083a2060e90ef8caa965339b7f35431c3d9740cb6accfa8)
                check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination": destination,
                "enabled": enabled,
            }

        @builtins.property
        def destination(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnBotAlias.TextLogDestinationProperty"]:
            '''Defines the Amazon CloudWatch Logs destination log group for conversation text logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-textlogsetting.html#cfn-lex-botalias-textlogsetting-destination
            '''
            result = self._values.get("destination")
            assert result is not None, "Required property 'destination' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBotAlias.TextLogDestinationProperty"], result)

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Determines whether conversation logs should be stored for an alias.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botalias-textlogsetting.html#cfn-lex-botalias-textlogsetting-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TextLogSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lex.CfnBotAliasProps",
    jsii_struct_bases=[],
    name_mapping={
        "bot_alias_name": "botAliasName",
        "bot_id": "botId",
        "bot_alias_locale_settings": "botAliasLocaleSettings",
        "bot_alias_tags": "botAliasTags",
        "bot_version": "botVersion",
        "conversation_log_settings": "conversationLogSettings",
        "description": "description",
        "sentiment_analysis_settings": "sentimentAnalysisSettings",
    },
)
class CfnBotAliasProps:
    def __init__(
        self,
        *,
        bot_alias_name: builtins.str,
        bot_id: builtins.str,
        bot_alias_locale_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBotAlias.BotAliasLocaleSettingsItemProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        bot_alias_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        bot_version: typing.Optional[builtins.str] = None,
        conversation_log_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBotAlias.ConversationLogSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        sentiment_analysis_settings: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnBotAlias``.

        :param bot_alias_name: The name of the bot alias.
        :param bot_id: The unique identifier of the bot.
        :param bot_alias_locale_settings: Specifies settings that are unique to a locale. For example, you can use different Lambda function depending on the bot's locale.
        :param bot_alias_tags: An array of key-value pairs to apply to this resource. You can only add tags when you specify an alias. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param bot_version: The version of the bot that the bot alias references.
        :param conversation_log_settings: Specifies whether Amazon Lex logs text and audio for conversations with the bot. When you enable conversation logs, text logs store text input, transcripts of audio input, and associated metadata in Amazon CloudWatch logs. Audio logs store input in Amazon S3 .
        :param description: The description of the bot alias.
        :param sentiment_analysis_settings: Determines whether Amazon Lex will use Amazon Comprehend to detect the sentiment of user utterances.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lex as lex
            
            # sentiment_analysis_settings: Any
            
            cfn_bot_alias_props = lex.CfnBotAliasProps(
                bot_alias_name="botAliasName",
                bot_id="botId",
            
                # the properties below are optional
                bot_alias_locale_settings=[lex.CfnBotAlias.BotAliasLocaleSettingsItemProperty(
                    bot_alias_locale_setting=lex.CfnBotAlias.BotAliasLocaleSettingsProperty(
                        enabled=False,
            
                        # the properties below are optional
                        code_hook_specification=lex.CfnBotAlias.CodeHookSpecificationProperty(
                            lambda_code_hook=lex.CfnBotAlias.LambdaCodeHookProperty(
                                code_hook_interface_version="codeHookInterfaceVersion",
                                lambda_arn="lambdaArn"
                            )
                        )
                    ),
                    locale_id="localeId"
                )],
                bot_alias_tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                bot_version="botVersion",
                conversation_log_settings=lex.CfnBotAlias.ConversationLogSettingsProperty(
                    audio_log_settings=[lex.CfnBotAlias.AudioLogSettingProperty(
                        destination=lex.CfnBotAlias.AudioLogDestinationProperty(
                            s3_bucket=lex.CfnBotAlias.S3BucketLogDestinationProperty(
                                log_prefix="logPrefix",
                                s3_bucket_arn="s3BucketArn",
            
                                # the properties below are optional
                                kms_key_arn="kmsKeyArn"
                            )
                        ),
                        enabled=False
                    )],
                    text_log_settings=[lex.CfnBotAlias.TextLogSettingProperty(
                        destination=lex.CfnBotAlias.TextLogDestinationProperty(
                            cloud_watch=lex.CfnBotAlias.CloudWatchLogGroupLogDestinationProperty(
                                cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                                log_prefix="logPrefix"
                            )
                        ),
                        enabled=False
                    )]
                ),
                description="description",
                sentiment_analysis_settings=sentiment_analysis_settings
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__738c59c8472d47ce88d44e92ffd9f33e52944ccc1849febc9bf2f7edbd7c3db2)
            check_type(argname="argument bot_alias_name", value=bot_alias_name, expected_type=type_hints["bot_alias_name"])
            check_type(argname="argument bot_id", value=bot_id, expected_type=type_hints["bot_id"])
            check_type(argname="argument bot_alias_locale_settings", value=bot_alias_locale_settings, expected_type=type_hints["bot_alias_locale_settings"])
            check_type(argname="argument bot_alias_tags", value=bot_alias_tags, expected_type=type_hints["bot_alias_tags"])
            check_type(argname="argument bot_version", value=bot_version, expected_type=type_hints["bot_version"])
            check_type(argname="argument conversation_log_settings", value=conversation_log_settings, expected_type=type_hints["conversation_log_settings"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument sentiment_analysis_settings", value=sentiment_analysis_settings, expected_type=type_hints["sentiment_analysis_settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bot_alias_name": bot_alias_name,
            "bot_id": bot_id,
        }
        if bot_alias_locale_settings is not None:
            self._values["bot_alias_locale_settings"] = bot_alias_locale_settings
        if bot_alias_tags is not None:
            self._values["bot_alias_tags"] = bot_alias_tags
        if bot_version is not None:
            self._values["bot_version"] = bot_version
        if conversation_log_settings is not None:
            self._values["conversation_log_settings"] = conversation_log_settings
        if description is not None:
            self._values["description"] = description
        if sentiment_analysis_settings is not None:
            self._values["sentiment_analysis_settings"] = sentiment_analysis_settings

    @builtins.property
    def bot_alias_name(self) -> builtins.str:
        '''The name of the bot alias.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-botaliasname
        '''
        result = self._values.get("bot_alias_name")
        assert result is not None, "Required property 'bot_alias_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bot_id(self) -> builtins.str:
        '''The unique identifier of the bot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-botid
        '''
        result = self._values.get("bot_id")
        assert result is not None, "Required property 'bot_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bot_alias_locale_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBotAlias.BotAliasLocaleSettingsItemProperty]]]]:
        '''Specifies settings that are unique to a locale.

        For example, you can use different Lambda function depending on the bot's locale.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-botaliaslocalesettings
        '''
        result = self._values.get("bot_alias_locale_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBotAlias.BotAliasLocaleSettingsItemProperty]]]], result)

    @builtins.property
    def bot_alias_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]]:
        '''An array of key-value pairs to apply to this resource.

        You can only add tags when you specify an alias.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-botaliastags
        '''
        result = self._values.get("bot_alias_tags")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]], result)

    @builtins.property
    def bot_version(self) -> typing.Optional[builtins.str]:
        '''The version of the bot that the bot alias references.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-botversion
        '''
        result = self._values.get("bot_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def conversation_log_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBotAlias.ConversationLogSettingsProperty]]:
        '''Specifies whether Amazon Lex logs text and audio for conversations with the bot.

        When you enable conversation logs, text logs store text input, transcripts of audio input, and associated metadata in Amazon CloudWatch logs. Audio logs store input in Amazon S3 .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-conversationlogsettings
        '''
        result = self._values.get("conversation_log_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBotAlias.ConversationLogSettingsProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the bot alias.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sentiment_analysis_settings(self) -> typing.Any:
        '''Determines whether Amazon Lex will use Amazon Comprehend to detect the sentiment of user utterances.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botalias.html#cfn-lex-botalias-sentimentanalysissettings
        '''
        result = self._values.get("sentiment_analysis_settings")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBotAliasProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lex.CfnBotProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_privacy": "dataPrivacy",
        "idle_session_ttl_in_seconds": "idleSessionTtlInSeconds",
        "name": "name",
        "role_arn": "roleArn",
        "auto_build_bot_locales": "autoBuildBotLocales",
        "bot_file_s3_location": "botFileS3Location",
        "bot_locales": "botLocales",
        "bot_tags": "botTags",
        "description": "description",
        "test_bot_alias_settings": "testBotAliasSettings",
        "test_bot_alias_tags": "testBotAliasTags",
    },
)
class CfnBotProps:
    def __init__(
        self,
        *,
        data_privacy: typing.Any,
        idle_session_ttl_in_seconds: jsii.Number,
        name: builtins.str,
        role_arn: builtins.str,
        auto_build_bot_locales: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        bot_file_s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        bot_locales: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.BotLocaleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        bot_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        test_bot_alias_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.TestBotAliasSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        test_bot_alias_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnBot``.

        :param data_privacy: By default, data stored by Amazon Lex is encrypted. The ``DataPrivacy`` structure provides settings that determine how Amazon Lex handles special cases of securing the data for your bot.
        :param idle_session_ttl_in_seconds: The time, in seconds, that Amazon Lex should keep information about a user's conversation with the bot. A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Lex deletes any data provided before the timeout. You can specify between 60 (1 minute) and 86,400 (24 hours) seconds.
        :param name: The name of the bot locale.
        :param role_arn: The Amazon Resource Name (ARN) of the IAM role used to build and run the bot.
        :param auto_build_bot_locales: Indicates whether Amazon Lex V2 should automatically build the locales for the bot after a change.
        :param bot_file_s3_location: The Amazon S3 location of files used to import a bot. The files must be in the import format specified in `JSON format for importing and exporting <https://docs.aws.amazon.com/lexv2/latest/dg/import-export-format.html>`_ in the *Amazon Lex developer guide.*
        :param bot_locales: A list of locales for the bot.
        :param bot_tags: A list of tags to add to the bot. You can only add tags when you import a bot. You can't use the ``UpdateBot`` operation to update tags. To update tags, use the ``TagResource`` operation.
        :param description: The description of the version.
        :param test_bot_alias_settings: Specifies configuration settings for the alias used to test the bot. If the ``TestBotAliasSettings`` property is not specified, the settings are configured with default values.
        :param test_bot_alias_tags: A list of tags to add to the test alias for a bot. You can only add tags when you import a bot. You can't use the ``UpdateAlias`` operation to update tags. To update tags on the test alias, use the ``TagResource`` operation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html
        :exampleMetadata: fixture=_generated

        Example::

            
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bd27c18d3e2a58ae9aef768e05a25ed92243f8298c9575d9ff15c1d7f1aae83)
            check_type(argname="argument data_privacy", value=data_privacy, expected_type=type_hints["data_privacy"])
            check_type(argname="argument idle_session_ttl_in_seconds", value=idle_session_ttl_in_seconds, expected_type=type_hints["idle_session_ttl_in_seconds"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument auto_build_bot_locales", value=auto_build_bot_locales, expected_type=type_hints["auto_build_bot_locales"])
            check_type(argname="argument bot_file_s3_location", value=bot_file_s3_location, expected_type=type_hints["bot_file_s3_location"])
            check_type(argname="argument bot_locales", value=bot_locales, expected_type=type_hints["bot_locales"])
            check_type(argname="argument bot_tags", value=bot_tags, expected_type=type_hints["bot_tags"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument test_bot_alias_settings", value=test_bot_alias_settings, expected_type=type_hints["test_bot_alias_settings"])
            check_type(argname="argument test_bot_alias_tags", value=test_bot_alias_tags, expected_type=type_hints["test_bot_alias_tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_privacy": data_privacy,
            "idle_session_ttl_in_seconds": idle_session_ttl_in_seconds,
            "name": name,
            "role_arn": role_arn,
        }
        if auto_build_bot_locales is not None:
            self._values["auto_build_bot_locales"] = auto_build_bot_locales
        if bot_file_s3_location is not None:
            self._values["bot_file_s3_location"] = bot_file_s3_location
        if bot_locales is not None:
            self._values["bot_locales"] = bot_locales
        if bot_tags is not None:
            self._values["bot_tags"] = bot_tags
        if description is not None:
            self._values["description"] = description
        if test_bot_alias_settings is not None:
            self._values["test_bot_alias_settings"] = test_bot_alias_settings
        if test_bot_alias_tags is not None:
            self._values["test_bot_alias_tags"] = test_bot_alias_tags

    @builtins.property
    def data_privacy(self) -> typing.Any:
        '''By default, data stored by Amazon Lex is encrypted.

        The ``DataPrivacy`` structure provides settings that determine how Amazon Lex handles special cases of securing the data for your bot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-dataprivacy
        '''
        result = self._values.get("data_privacy")
        assert result is not None, "Required property 'data_privacy' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def idle_session_ttl_in_seconds(self) -> jsii.Number:
        '''The time, in seconds, that Amazon Lex should keep information about a user's conversation with the bot.

        A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Lex deletes any data provided before the timeout.

        You can specify between 60 (1 minute) and 86,400 (24 hours) seconds.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-idlesessionttlinseconds
        '''
        result = self._values.get("idle_session_ttl_in_seconds")
        assert result is not None, "Required property 'idle_session_ttl_in_seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the bot locale.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role used to build and run the bot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_build_bot_locales(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether Amazon Lex V2 should automatically build the locales for the bot after a change.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-autobuildbotlocales
        '''
        result = self._values.get("auto_build_bot_locales")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def bot_file_s3_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBot.S3LocationProperty]]:
        '''The Amazon S3 location of files used to import a bot.

        The files must be in the import format specified in `JSON format for importing and exporting <https://docs.aws.amazon.com/lexv2/latest/dg/import-export-format.html>`_ in the *Amazon Lex developer guide.*

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-botfiles3location
        '''
        result = self._values.get("bot_file_s3_location")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBot.S3LocationProperty]], result)

    @builtins.property
    def bot_locales(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBot.BotLocaleProperty]]]]:
        '''A list of locales for the bot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-botlocales
        '''
        result = self._values.get("bot_locales")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBot.BotLocaleProperty]]]], result)

    @builtins.property
    def bot_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]]:
        '''A list of tags to add to the bot.

        You can only add tags when you import a bot. You can't use the ``UpdateBot`` operation to update tags. To update tags, use the ``TagResource`` operation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-bottags
        '''
        result = self._values.get("bot_tags")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def test_bot_alias_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBot.TestBotAliasSettingsProperty]]:
        '''Specifies configuration settings for the alias used to test the bot.

        If the ``TestBotAliasSettings`` property is not specified, the settings are configured with default values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-testbotaliassettings
        '''
        result = self._values.get("test_bot_alias_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBot.TestBotAliasSettingsProperty]], result)

    @builtins.property
    def test_bot_alias_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]]:
        '''A list of tags to add to the test alias for a bot.

        You can only add tags when you import a bot. You can't use the ``UpdateAlias`` operation to update tags. To update tags on the test alias, use the ``TagResource`` operation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-bot.html#cfn-lex-bot-testbotaliastags
        '''
        result = self._values.get("test_bot_alias_tags")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBotProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnBotVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lex.CfnBotVersion",
):
    '''.. epigraph::

   Amazon Lex V2 is the only supported version in AWS CloudFormation .

    Specifies a new version of the bot based on the ``DRAFT`` version. If the ``DRAFT`` version of this resource hasn't changed since you created the last version, Amazon Lex doesn't create a new version, it returns the last created version.

    When you specify the first version of a bot, Amazon Lex sets the version to 1. Subsequent versions increment by 1.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botversion.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lex as lex
        
        cfn_bot_version = lex.CfnBotVersion(self, "MyCfnBotVersion",
            bot_id="botId",
            bot_version_locale_specification=[lex.CfnBotVersion.BotVersionLocaleSpecificationProperty(
                bot_version_locale_details=lex.CfnBotVersion.BotVersionLocaleDetailsProperty(
                    source_bot_version="sourceBotVersion"
                ),
                locale_id="localeId"
            )],
        
            # the properties below are optional
            description="description"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        bot_id: builtins.str,
        bot_version_locale_specification: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBotVersion.BotVersionLocaleSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]]],
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param bot_id: The unique identifier of the bot.
        :param bot_version_locale_specification: Specifies the locales that Amazon Lex adds to this version. You can choose the Draft version or any other previously published version for each locale. When you specify a source version, the locale data is copied from the source version to the new version.
        :param description: The description of the version.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f9a25d6b442565e4ffb72003af0c316d38fe2ab4bfc804150cdde827b2a9544)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBotVersionProps(
            bot_id=bot_id,
            bot_version_locale_specification=bot_version_locale_specification,
            description=description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__021d517039d5a6a9e565ebda539e800914ac9e27a462b68b4f16c736f973ecaa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ed72c6648e5beaf5c609fdc25822e27c9d7d030f222a3590f88326fd6d4ef9d)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrBotVersion")
    def attr_bot_version(self) -> builtins.str:
        '''The version of the bot.

        :cloudformationAttribute: BotVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBotVersion"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="botId")
    def bot_id(self) -> builtins.str:
        '''The unique identifier of the bot.'''
        return typing.cast(builtins.str, jsii.get(self, "botId"))

    @bot_id.setter
    def bot_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3695fdd3e0dc7398529cc6a7cac33b2ce01960db4218cbd75288c1c43ba138a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "botId", value)

    @builtins.property
    @jsii.member(jsii_name="botVersionLocaleSpecification")
    def bot_version_locale_specification(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBotVersion.BotVersionLocaleSpecificationProperty"]]]:
        '''Specifies the locales that Amazon Lex adds to this version.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBotVersion.BotVersionLocaleSpecificationProperty"]]], jsii.get(self, "botVersionLocaleSpecification"))

    @bot_version_locale_specification.setter
    def bot_version_locale_specification(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBotVersion.BotVersionLocaleSpecificationProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59417360b74b60eeb0ab210b6bdfe82a4a6edef5d905cb893286714abdbbfa99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "botVersionLocaleSpecification", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the version.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15e61488889e270b05ad7dfb944cf4d12160347f937d69379819be904fe1a59e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBotVersion.BotVersionLocaleDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"source_bot_version": "sourceBotVersion"},
    )
    class BotVersionLocaleDetailsProperty:
        def __init__(self, *, source_bot_version: builtins.str) -> None:
            '''The version of a bot used for a bot locale.

            :param source_bot_version: The version of a bot used for a bot locale.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botversion-botversionlocaledetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                bot_version_locale_details_property = lex.CfnBotVersion.BotVersionLocaleDetailsProperty(
                    source_bot_version="sourceBotVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ab455ef0a33df88b4f34bc9b9a0a95974e19be27d0ca983866a8393ea952e077)
                check_type(argname="argument source_bot_version", value=source_bot_version, expected_type=type_hints["source_bot_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "source_bot_version": source_bot_version,
            }

        @builtins.property
        def source_bot_version(self) -> builtins.str:
            '''The version of a bot used for a bot locale.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botversion-botversionlocaledetails.html#cfn-lex-botversion-botversionlocaledetails-sourcebotversion
            '''
            result = self._values.get("source_bot_version")
            assert result is not None, "Required property 'source_bot_version' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BotVersionLocaleDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnBotVersion.BotVersionLocaleSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bot_version_locale_details": "botVersionLocaleDetails",
            "locale_id": "localeId",
        },
    )
    class BotVersionLocaleSpecificationProperty:
        def __init__(
            self,
            *,
            bot_version_locale_details: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBotVersion.BotVersionLocaleDetailsProperty", typing.Dict[builtins.str, typing.Any]]],
            locale_id: builtins.str,
        ) -> None:
            '''Specifies the locale that Amazon Lex adds to this version.

            You can choose the Draft version or any other previously published version for each locale. When you specify a source version, the locale data is copied from the source version to the new version.

            :param bot_version_locale_details: The version of a bot used for a bot locale.
            :param locale_id: The identifier of the locale to add to the version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botversion-botversionlocalespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                bot_version_locale_specification_property = lex.CfnBotVersion.BotVersionLocaleSpecificationProperty(
                    bot_version_locale_details=lex.CfnBotVersion.BotVersionLocaleDetailsProperty(
                        source_bot_version="sourceBotVersion"
                    ),
                    locale_id="localeId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4802f8ce0abbf146138354d6e73113a70e24b8b7c9612564e44de4c4aabef220)
                check_type(argname="argument bot_version_locale_details", value=bot_version_locale_details, expected_type=type_hints["bot_version_locale_details"])
                check_type(argname="argument locale_id", value=locale_id, expected_type=type_hints["locale_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bot_version_locale_details": bot_version_locale_details,
                "locale_id": locale_id,
            }

        @builtins.property
        def bot_version_locale_details(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnBotVersion.BotVersionLocaleDetailsProperty"]:
            '''The version of a bot used for a bot locale.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botversion-botversionlocalespecification.html#cfn-lex-botversion-botversionlocalespecification-botversionlocaledetails
            '''
            result = self._values.get("bot_version_locale_details")
            assert result is not None, "Required property 'bot_version_locale_details' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBotVersion.BotVersionLocaleDetailsProperty"], result)

        @builtins.property
        def locale_id(self) -> builtins.str:
            '''The identifier of the locale to add to the version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-botversion-botversionlocalespecification.html#cfn-lex-botversion-botversionlocalespecification-localeid
            '''
            result = self._values.get("locale_id")
            assert result is not None, "Required property 'locale_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BotVersionLocaleSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lex.CfnBotVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "bot_id": "botId",
        "bot_version_locale_specification": "botVersionLocaleSpecification",
        "description": "description",
    },
)
class CfnBotVersionProps:
    def __init__(
        self,
        *,
        bot_id: builtins.str,
        bot_version_locale_specification: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBotVersion.BotVersionLocaleSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]]],
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnBotVersion``.

        :param bot_id: The unique identifier of the bot.
        :param bot_version_locale_specification: Specifies the locales that Amazon Lex adds to this version. You can choose the Draft version or any other previously published version for each locale. When you specify a source version, the locale data is copied from the source version to the new version.
        :param description: The description of the version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lex as lex
            
            cfn_bot_version_props = lex.CfnBotVersionProps(
                bot_id="botId",
                bot_version_locale_specification=[lex.CfnBotVersion.BotVersionLocaleSpecificationProperty(
                    bot_version_locale_details=lex.CfnBotVersion.BotVersionLocaleDetailsProperty(
                        source_bot_version="sourceBotVersion"
                    ),
                    locale_id="localeId"
                )],
            
                # the properties below are optional
                description="description"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7e84893518e25327247dbe2e6a44e1ceeb51478dafbe33bce09ea7685937be5)
            check_type(argname="argument bot_id", value=bot_id, expected_type=type_hints["bot_id"])
            check_type(argname="argument bot_version_locale_specification", value=bot_version_locale_specification, expected_type=type_hints["bot_version_locale_specification"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bot_id": bot_id,
            "bot_version_locale_specification": bot_version_locale_specification,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def bot_id(self) -> builtins.str:
        '''The unique identifier of the bot.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botversion.html#cfn-lex-botversion-botid
        '''
        result = self._values.get("bot_id")
        assert result is not None, "Required property 'bot_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bot_version_locale_specification(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBotVersion.BotVersionLocaleSpecificationProperty]]]:
        '''Specifies the locales that Amazon Lex adds to this version.

        You can choose the Draft version or any other previously published version for each locale. When you specify a source version, the locale data is copied from the source version to the new version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botversion.html#cfn-lex-botversion-botversionlocalespecification
        '''
        result = self._values.get("bot_version_locale_specification")
        assert result is not None, "Required property 'bot_version_locale_specification' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBotVersion.BotVersionLocaleSpecificationProperty]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-botversion.html#cfn-lex-botversion-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBotVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnResourcePolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_lex.CfnResourcePolicy",
):
    '''.. epigraph::

   Amazon Lex V2 is the only supported version in AWS CloudFormation .

    Specifies a new resource policy with the specified policy statements.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-resourcepolicy.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_lex as lex
        
        # policy: Any
        
        cfn_resource_policy = lex.CfnResourcePolicy(self, "MyCfnResourcePolicy",
            policy=policy,
            resource_arn="resourceArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        policy: typing.Any,
        resource_arn: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param policy: A resource policy to add to the resource. The policy is a JSON structure that contains one or more statements that define the policy. The policy must follow IAM syntax. If the policy isn't valid, Amazon Lex returns a validation exception.
        :param resource_arn: The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c4e37a39c1961787db85c32c8fd5d0f194dd3d7ace3f425501ca99f4a6bfaf9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourcePolicyProps(policy=policy, resource_arn=resource_arn)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8c541ffb1f95d8385c5fc1630139769cb4b5f9cddce5c2c4030383b10cbc93c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__df22f9d7fb82d11696f2f7cc324ce147d61b2a46468bfd676f2d1ffa9e888e7a)
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
        '''The identifier of the resource policy.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrRevisionId")
    def attr_revision_id(self) -> builtins.str:
        '''Specifies the current revision of a resource policy.

        :cloudformationAttribute: RevisionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRevisionId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> typing.Any:
        '''A resource policy to add to the resource.'''
        return typing.cast(typing.Any, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bedb04f3a7639ce6dd847afa27b9015e9c5a45e10d0185b1e422d001d936196)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value)

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2269eb87c059c5d27aab85364fde6b4ccb6e21ca5bc766b939d038b5294665a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_lex.CfnResourcePolicy.PolicyProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class PolicyProperty:
        def __init__(self) -> None:
            '''A resource policy to add to the resource.

            The policy is a JSON structure following the IAM syntax that contains one or more statements that define the policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lex-resourcepolicy-policy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_lex as lex
                
                policy_property = lex.CfnResourcePolicy.PolicyProperty()
            '''
            self._values: typing.Dict[builtins.str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_lex.CfnResourcePolicyProps",
    jsii_struct_bases=[],
    name_mapping={"policy": "policy", "resource_arn": "resourceArn"},
)
class CfnResourcePolicyProps:
    def __init__(self, *, policy: typing.Any, resource_arn: builtins.str) -> None:
        '''Properties for defining a ``CfnResourcePolicy``.

        :param policy: A resource policy to add to the resource. The policy is a JSON structure that contains one or more statements that define the policy. The policy must follow IAM syntax. If the policy isn't valid, Amazon Lex returns a validation exception.
        :param resource_arn: The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-resourcepolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_lex as lex
            
            # policy: Any
            
            cfn_resource_policy_props = lex.CfnResourcePolicyProps(
                policy=policy,
                resource_arn="resourceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26bba8594196376d121fda2be732c9f29e1f3796c7e460c1a716addfae4eb1ae)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy": policy,
            "resource_arn": resource_arn,
        }

    @builtins.property
    def policy(self) -> typing.Any:
        '''A resource policy to add to the resource.

        The policy is a JSON structure that contains one or more statements that define the policy. The policy must follow IAM syntax. If the policy isn't valid, Amazon Lex returns a validation exception.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-resourcepolicy.html#cfn-lex-resourcepolicy-policy
        '''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lex-resourcepolicy.html#cfn-lex-resourcepolicy-resourcearn
        '''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourcePolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnBot",
    "CfnBotAlias",
    "CfnBotAliasProps",
    "CfnBotProps",
    "CfnBotVersion",
    "CfnBotVersionProps",
    "CfnResourcePolicy",
    "CfnResourcePolicyProps",
]

publication.publish()

def _typecheckingstub__5c185fb71324df3b939f1cbff6a813b57733510cba6989dac147b9a3a7e6e7b3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    data_privacy: typing.Any,
    idle_session_ttl_in_seconds: jsii.Number,
    name: builtins.str,
    role_arn: builtins.str,
    auto_build_bot_locales: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    bot_file_s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    bot_locales: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.BotLocaleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    bot_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    test_bot_alias_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.TestBotAliasSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    test_bot_alias_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bab436ed9466bb2dfbcffe8f150f71a01f02f724db7a515af356b7604eb2360(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15efeb50c94c0f4bdd170a08e39d1bbdaa11e3843d27eb6072816f7a53086d91(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4668d6cdd4af2b7befaa16f723e10618c13be75aa15d81ef3fc5b0a2938929db(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05337531f67ab566e1a76fe38a76cf27ac63ce8fc8e6e724aed15fa7b8d31908(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a1ea37ce191acf8a9698c1b06f93041142aa612fff3e59774240d1192fecc1c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d1de1b03449680ed86d6f014b455506f65035803afa60f89e339dd978cc28af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d59168298bb6c73c8a29b497da006fc40603973cb71aba43e2f0ea0bc3c1c61a(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49ad642c7a6232d4347e9dde2e04bc042cd7d8744c9896121505bc4969f28056(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBot.S3LocationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99af8c5daefa40203f5f0fbdfe98fccbc452c26d2c2bf3b4b00da732bcbfcb5e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBot.BotLocaleProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebd0622909df38949fb95f9e4bfc9d82f922d11b6e1fee1b78ed955a197015d7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72103623fa216232524c89f3e94b6a4e2056c1e8ad43603db83275506363e42f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8af2b15d1ec9a6dfbd927bbbf7b4b9c006697a2b575338beae8d16e49680244f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBot.TestBotAliasSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6da956c0f46d2bfe7dd17bc9ad27b754c6943b2b1d68f58963bb394ff73cf731(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c440956da77e8147763a47aa43d8d996eeb914994200503203ad8dc1de5b8df3(
    *,
    audio_recognition_strategy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3838670eeffedef2bc12112ab8648963f9cefc6b5d549db48de7c20c23377df(
    *,
    allow_audio_input: typing.Union[builtins.bool, _IResolvable_da3f097b],
    allow_dtmf_input: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c052ee345e65d8dccab612f97fe193228903fbbb67e70bcb8f742a6105953515(
    *,
    start_timeout_ms: jsii.Number,
    audio_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.AudioSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dtmf_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.DTMFSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f63a4e17f071cd3f1324d2209c869ca77ffb749d83b8046aa835feea80b9c16c(
    *,
    s3_bucket: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.S3BucketLogDestinationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4382bc3265af37750e55e2a9b53a7a5b403a0a22fa40facd692ffdb2a075b9cc(
    *,
    destination: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.AudioLogDestinationProperty, typing.Dict[builtins.str, typing.Any]]],
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e44ef412e3afcfbf71cf2299bd8cea4e94f42bf7c72d8f4699c80d7c4f63b76(
    *,
    end_timeout_ms: jsii.Number,
    max_length_ms: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8cb59d3ac7a8ae237407b5df223685e38d3b85ded672a3f1009115577aea63a(
    *,
    bot_alias_locale_setting: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.BotAliasLocaleSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
    locale_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fccab71cd793cc569d18b739e52d926af862173e626b31edeb7b0ec09a1b8fa7(
    *,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
    code_hook_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.CodeHookSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ad20956b5309c4b6154f09c947ce4023f20ed7a602b3cfa60f2bd3cfda11dd4(
    *,
    locale_id: builtins.str,
    nlu_confidence_threshold: jsii.Number,
    custom_vocabulary: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.CustomVocabularyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    intents: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.IntentProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    slot_types: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.SlotTypeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    voice_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.VoiceSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0208df4d8ce79e1029770ef72acb7332713a8684db0810b60ddcd684dc98bcd(
    *,
    text: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f146fd3bf196dbdf204053031018bcc0244c9347c6ceace1ea6dcdeec4b168de(
    *,
    cloud_watch_log_group_arn: builtins.str,
    log_prefix: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da6a0a3d3181926b6600cb1e93e0bf761a0d23d96eb57f580dcef39cc7d85734(
    *,
    lambda_code_hook: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.LambdaCodeHookProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__955a721d21fa1f19bf91fc3c341e8f185dbe2e44d2e52eefdfc64abc889f0959(
    *,
    expression_string: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc5c77c3d99e5efee20bf629186ee9b96fd242aa9b1f1e923dec8bf6554cd229(
    *,
    condition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ConditionProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    next_step: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.DialogStateProperty, typing.Dict[builtins.str, typing.Any]]],
    response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ResponseSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de4586a5996f5a859b3286e8e34d08872ebb2261aed1437d975e7fcb4b3c77b3(
    *,
    conditional_branches: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ConditionalBranchProperty, typing.Dict[builtins.str, typing.Any]]]]],
    default_branch: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.DefaultConditionalBranchProperty, typing.Dict[builtins.str, typing.Any]]],
    is_active: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fadbc804342400e1fe72580d2c49c87b48a4dcb178861f1caaff4692f0fc551a(
    *,
    audio_log_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.AudioLogSettingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    text_log_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.TextLogSettingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63c440afe8abb656f1b6b5cc4bdf73214fb7e5ec559d4ecaceee87d143691138(
    *,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fdc21221bc0867aec831c3ffab8dd3d47a44075876c837b023a9eecc83af7ee(
    *,
    phrase: builtins.str,
    display_as: typing.Optional[builtins.str] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb16bf8e83aadced4f623ac7b6a54e675fb78bc9a1a5a9aec3fa5a5f1e63a1bb(
    *,
    custom_vocabulary_items: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.CustomVocabularyItemProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0381b9c530c5df0d1792837611cfb9e0aabde7240383f67b78c9378632b3c2dc(
    *,
    deletion_character: builtins.str,
    end_character: builtins.str,
    end_timeout_ms: jsii.Number,
    max_length: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8413726661c5259fdaa87f5eb1adab8b9e36f411a5b42163e14d40d5aca25121(
    *,
    child_directed: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b17d7f375530a3080dd7a04795acd6231e37882d54e677880209844b34b66963(
    *,
    next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.DialogStateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ResponseSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e376869d573dbc5f07a8bacbcb08139f9ccf20789d86cfdc88afd3db242dd177(
    *,
    type: builtins.str,
    slot_to_elicit: typing.Optional[builtins.str] = None,
    suppress_next_message: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e19b7a3cd9426f9feac0cd76771e4f412c686860e6db49495e9732e3e2c2e2ad(
    *,
    enable_code_hook_invocation: typing.Union[builtins.bool, _IResolvable_da3f097b],
    is_active: typing.Union[builtins.bool, _IResolvable_da3f097b],
    post_code_hook_specification: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.PostDialogCodeHookInvocationSpecificationProperty, typing.Dict[builtins.str, typing.Any]]],
    invocation_label: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcf037ef78d32218b7b41dd7215a0c084b74ce9ea1d291027573be2d214e57f4(
    *,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c7dde88739182f4b4a30f1ef8b12c227c3e086e46bea8e39b20f1c51623d165(
    *,
    dialog_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.DialogActionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    intent: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.IntentOverrideProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    session_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.SessionAttributeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60b6686b2f7d08316ec6f3906c1eb41b85065d8e1d623e4ccb84213bea7eb37e(
    *,
    enable_code_hook_invocation: typing.Union[builtins.bool, _IResolvable_da3f097b],
    invocation_label: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88fba332915fbf5259a0c253d1363ad0ff0183417cfced04eef9822b50aecb7a(
    *,
    grammar_slot_type_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.GrammarSlotTypeSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05de122265994f52129837a3bda602f910b4b269167e3110405de9650ec1b200(
    *,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
    fulfillment_updates_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.FulfillmentUpdatesSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    is_active: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    post_fulfillment_status_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.PostFulfillmentStatusSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3c656f733b90fca865d240233e420cba1e6738d89391b29144453b4d799898f(
    *,
    delay_in_seconds: jsii.Number,
    message_groups: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.MessageGroupProperty, typing.Dict[builtins.str, typing.Any]]]]],
    allow_interrupt: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a875cefaa538cfe3904d9bce7ca2b745f46320a3cbb89881519d72278e20b2fd(
    *,
    frequency_in_seconds: jsii.Number,
    message_groups: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.MessageGroupProperty, typing.Dict[builtins.str, typing.Any]]]]],
    allow_interrupt: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__500ed503fae8fece46360727878fdf9250149c5d237d5f4414d8191ffbb1cb55(
    *,
    active: typing.Union[builtins.bool, _IResolvable_da3f097b],
    start_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.FulfillmentStartResponseSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    timeout_in_seconds: typing.Optional[jsii.Number] = None,
    update_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.FulfillmentUpdateResponseSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7607729da805dba490266bfccf35e40fc22f0e3b3c4d78038e129d897dd21483(
    *,
    source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.GrammarSlotTypeSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a3142398a960ac78cf821387c99b655d930f71dfa164c7937ee4315b875aa78(
    *,
    s3_bucket_name: builtins.str,
    s3_object_key: builtins.str,
    kms_key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1ea1c8338736803aba15b8d47a2bb101596e1e5acf68885a2b6456ea5eef357(
    *,
    title: builtins.str,
    buttons: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ButtonProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    image_url: typing.Optional[builtins.str] = None,
    subtitle: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83749e2d6df5ca331ee019977e124fea7c18720ee7ffc2d63919bab99cc81a09(
    *,
    code_hook: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.DialogCodeHookInvocationSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ConditionalSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    initial_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ResponseSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.DialogStateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18309cb7fa78967eacac40a963eac7e414bca89983d05643328e0ca42fdd145f(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f90beb01727c97ae08801c759994a2a3947843959af8080718d29916dbe9e44(
    *,
    closing_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ResponseSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ConditionalSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    is_active: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.DialogStateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f96318abd0c4c68e9988644e0bef2c84730aaab41035ffb210f18a937b52ccc(
    *,
    prompt_specification: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.PromptSpecificationProperty, typing.Dict[builtins.str, typing.Any]]],
    code_hook: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.DialogCodeHookInvocationSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    confirmation_conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ConditionalSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    confirmation_next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.DialogStateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    confirmation_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ResponseSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    declination_conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ConditionalSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    declination_next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.DialogStateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    declination_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ResponseSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    elicitation_code_hook: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ElicitationCodeHookInvocationSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    failure_conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ConditionalSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    failure_next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.DialogStateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    failure_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ResponseSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    is_active: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__493166c423a1b45288ba10b5982fc7d58c8aa28aab6ecb53239e5da527e7fb9d(
    *,
    name: typing.Optional[builtins.str] = None,
    slots: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.SlotValueOverrideMapProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f105b684583292473a5d75a0aba26d4641f8f29746b1658a4a7b400367c1112f(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    dialog_code_hook: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.DialogCodeHookSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    fulfillment_code_hook: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.FulfillmentCodeHookSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    initial_response_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.InitialResponseSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    input_contexts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.InputContextProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    intent_closing_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.IntentClosingSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    intent_confirmation_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.IntentConfirmationSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kendra_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.KendraConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    output_contexts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.OutputContextProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    parent_intent_signature: typing.Optional[builtins.str] = None,
    sample_utterances: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.SampleUtteranceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    slot_priorities: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.SlotPriorityProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    slots: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.SlotProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__befde100c4754003fd17718bb74770d3516503d02c4db787eec9bec0d6ca499c(
    *,
    kendra_index: builtins.str,
    query_filter_string: typing.Optional[builtins.str] = None,
    query_filter_string_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed25dece9631c2040723f44578a5a17d48f87a06be94d6d8ca47636248f12356(
    *,
    code_hook_interface_version: builtins.str,
    lambda_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b7bb98ebf9b78a6faa1470a130c8f32a0caa08de5353c4b06f938ca5f4ac01c(
    *,
    message: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.MessageProperty, typing.Dict[builtins.str, typing.Any]]],
    variations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.MessageProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4f93a57e245b677dfd69332cad697189343a98fda98898783b942417844c5e9(
    *,
    custom_payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.CustomPayloadProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_response_card: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ImageResponseCardProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    plain_text_message: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.PlainTextMessageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ssml_message: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.SSMLMessageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d243896aac9e5978582c7a17b393ee26ecc4d0b53d8eeecb47f9b8e6de9baeb(
    *,
    allow_multiple_values: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a795f3c1800daacb8fa1b1f53ef1260088f1fa8ef905157a69c25f1fb6aaf260(
    *,
    obfuscation_setting_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6778b57b5a02264308db760307dd896938ee6291e49f511015f350056cc54059(
    *,
    name: builtins.str,
    time_to_live_in_seconds: jsii.Number,
    turns_to_live: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba4054ec5399c78441e6f8c9140c893660759acdecf2641d77e755440453f99b(
    *,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62eb1599f0b57eb49828d92c80a33151b817e1ccbd2af63d8044bc26a704044c(
    *,
    failure_conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ConditionalSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    failure_next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.DialogStateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    failure_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ResponseSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    success_conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ConditionalSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    success_next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.DialogStateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    success_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ResponseSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    timeout_conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ConditionalSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    timeout_next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.DialogStateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    timeout_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ResponseSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbd6476d58fabc3c7113634854ca2260b61ab0c7b242040db795c0c8a814f541(
    *,
    failure_conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ConditionalSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    failure_next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.DialogStateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    failure_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ResponseSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    success_conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ConditionalSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    success_next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.DialogStateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    success_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ResponseSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    timeout_conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ConditionalSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    timeout_next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.DialogStateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    timeout_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ResponseSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__943a427e65ce74bc55f71dc759e0b2b2e36381bcfbb7a02e474b7679c58966ff(
    *,
    allowed_input_types: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.AllowedInputTypesProperty, typing.Dict[builtins.str, typing.Any]]],
    allow_interrupt: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    audio_and_dtmf_input_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.AudioAndDTMFInputSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    text_input_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.TextInputSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfee20d6cdf119a2c07cbe82b4eed1c4619bb7cefa041af9edd5327509e497e4(
    *,
    max_retries: jsii.Number,
    message_groups_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.MessageGroupProperty, typing.Dict[builtins.str, typing.Any]]]]],
    allow_interrupt: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    message_selection_strategy: typing.Optional[builtins.str] = None,
    prompt_attempts_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.PromptAttemptSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41b902a3461c6b590e44c1b70d9b5197da38bf30395535518dbeee15b931cb17(
    *,
    message_groups_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.MessageGroupProperty, typing.Dict[builtins.str, typing.Any]]]]],
    allow_interrupt: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ded78dd4eccaf929584502bf9d04303df195ccea074a52fa76a797748ee0e43b(
    *,
    log_prefix: builtins.str,
    s3_bucket_arn: builtins.str,
    kms_key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d6aeb756ee3b20901b9c635f0dea5af9d930212d89c2181e88d0fdb1d2b13a6(
    *,
    s3_bucket: builtins.str,
    s3_object_key: builtins.str,
    s3_object_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c9fd5a338093c2843c71a2fd67ef382cd74c7db746e18dcc56d46f706d264fe(
    *,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0142d6efc46c3cefacaba45fb4bc73266bcc186db01a160e97d3c9792a68f815(
    *,
    utterance: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cff5ea6d93f253339453f883c74d2692982ebd9b801acbfa83d5dc5e23650414(
    *,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9e4f3b0a606b026d5c930a078922f49440e9a195321a00c7a7a07508bf2d5d4(
    *,
    detect_sentiment: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be28e1d53db74d4e8f722a5f55abe5546d71fcda9d0b48a83fc4f86184b5dfe3(
    *,
    key: builtins.str,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0631539d23156c87283aee086bca2fb1e2b925a511e4ecec896a467b44f7bf65(
    *,
    capture_conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ConditionalSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    capture_next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.DialogStateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    capture_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ResponseSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    code_hook: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.DialogCodeHookInvocationSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    elicitation_code_hook: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ElicitationCodeHookInvocationSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    failure_conditional: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ConditionalSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    failure_next_step: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.DialogStateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    failure_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ResponseSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33675db47c04e880974f8c48a0f7cf7c1b37ebf701f07d0c6cc8364e832c872b(
    *,
    default_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34b3d6924ee488b2942420ad151d4eacdd239979cd109bb95fe9c198976ad4fb(
    *,
    default_value_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.SlotDefaultValueProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__244bb657ccf2ab8e922d85bf2dde92e8cbdaea5ac16a97de6a5a5c08112ce93d(
    *,
    priority: jsii.Number,
    slot_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef126475ab56636b361ebc97f72cf09bd8480c4e5dad06e8da998fba1a7c6112(
    *,
    name: builtins.str,
    slot_type_name: builtins.str,
    value_elicitation_setting: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.SlotValueElicitationSettingProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    multiple_values_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.MultipleValuesSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    obfuscation_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ObfuscationSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d99d82598958085799a77f6b5114773dd5d435a8eed078da9626b631bffcfeea(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    external_source_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ExternalSourceSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    parent_slot_type_signature: typing.Optional[builtins.str] = None,
    slot_type_values: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.SlotTypeValueProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    value_selection_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.SlotValueSelectionSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4980167aa5887813c0d207005609f7ad5f62c2160739ca34ec554de05bd9904a(
    *,
    sample_value: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.SampleValueProperty, typing.Dict[builtins.str, typing.Any]]],
    synonyms: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.SampleValueProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce7cc5d5d9c242f068967edd6fef626bfeba8ad54b83c65f26b5e9c76f33bff3(
    *,
    slot_constraint: builtins.str,
    default_value_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.SlotDefaultValueSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    prompt_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.PromptSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sample_utterances: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.SampleUtteranceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    slot_capture_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.SlotCaptureSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    wait_and_continue_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.WaitAndContinueSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d81fb72fae48bda11549c52cc7d70c5c0b7e2f4273a0bfdb8e7159f62a4f854(
    *,
    slot_name: typing.Optional[builtins.str] = None,
    slot_value_override: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.SlotValueOverrideProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ff2a20d96561d546b729ca1c6e001b71dd8660a7430b36467df603c304e847b(
    *,
    shape: typing.Optional[builtins.str] = None,
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.SlotValueProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    values: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.SlotValueOverrideProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc3bcf0314f94e50ecf8c32547e6dcf7dd41e4579aad48e2fbf208dd1e976cfa(
    *,
    interpreted_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47fc35e110af5848c29f6beb9a83c5fb75061e0fd18a87c5ac25be2748bf153f(
    *,
    pattern: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7982c47931169a42f1aa99bdc61da96e42f63e5371b26a267f1cdadef30b4142(
    *,
    resolution_strategy: builtins.str,
    advanced_recognition_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.AdvancedRecognitionSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    regex_filter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.SlotValueRegexFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b29454e1c72d163c3d5c059ab5734a392267a9f5ea3476cbc3a7c07126ce2e5(
    *,
    frequency_in_seconds: jsii.Number,
    message_groups_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.MessageGroupProperty, typing.Dict[builtins.str, typing.Any]]]]],
    timeout_in_seconds: jsii.Number,
    allow_interrupt: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e4446d39358c5287d9df3b2990e64fd6f58a3cb8c75321845b0c566e4ddd896(
    *,
    bot_alias_locale_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.BotAliasLocaleSettingsItemProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    conversation_log_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ConversationLogSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    sentiment_analysis_settings: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__257481b35f3cd3f858136fad730402a318d316c1dab41bb5193ce3e69d9cd906(
    *,
    start_timeout_ms: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a830897331ded62c92882647499d6a847245a4419c9fd8cfd8605d13d3eac2f(
    *,
    cloud_watch: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.CloudWatchLogGroupLogDestinationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__717dfd593b69b20586c4b1f6c63f5b97efa12a2e8cd727b96b019101a312bcc2(
    *,
    destination: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.TextLogDestinationProperty, typing.Dict[builtins.str, typing.Any]]],
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afa285d252c1df4a0956dfe0bb68d0cc1b9d6ee0f0ea8e02d91cd9f1c9c53aab(
    *,
    voice_id: builtins.str,
    engine: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21656b0cba2d8c5320337a8a5bc150ba2c7097fdcd22e75137a6284ac3c9ab3d(
    *,
    continue_response: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ResponseSpecificationProperty, typing.Dict[builtins.str, typing.Any]]],
    waiting_response: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.ResponseSpecificationProperty, typing.Dict[builtins.str, typing.Any]]],
    is_active: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    still_waiting_response: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.StillWaitingResponseSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57cf179c443f74ff3b1c43c56eef686f369711792e444e53d5668f07ac682866(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bot_alias_name: builtins.str,
    bot_id: builtins.str,
    bot_alias_locale_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBotAlias.BotAliasLocaleSettingsItemProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    bot_alias_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    bot_version: typing.Optional[builtins.str] = None,
    conversation_log_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBotAlias.ConversationLogSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    sentiment_analysis_settings: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69e306fef7aca1ecd05a385248f8253ae3fef56958f84e69c038125bb4b466d0(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82906237840a0ec10e1166b52ceb1e62975a24e550f8f48c4e2935150c7960fe(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7c080b499a50788ae164c44975b98220147f762edd4ec214c0e6f9124445093(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43cce0d64f81ea520d08b83a4aa6aece3a2341b6dde0b7fcd65a8f847f5de3f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__917790158810f6fc38fb5d4372a10a9584fb6d4764bb1d87be8244cc727936e5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBotAlias.BotAliasLocaleSettingsItemProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71d610b69d60b87626f698f0118b5837b8126b661b02cb75b4961dfeaead9834(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__607e7a3cdff2bc65c8c76ca1d05837350e81ade44a258da16439fc17f283acda(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26855f93261461e56c873baf08145fa32c74a011917251399c4d61392913f877(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBotAlias.ConversationLogSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf77d628ea97246a31f89b41559277e6cfb829aa4bde51a21dce2c884995deb9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8cbd98c4bdfe82bcb165ec91638c6ad68086348b28345eeda6f375cb1a7fcd1(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d41a4792f6acf503d602b95e02a66bebf212a7b6908e2a7af00574350149fb86(
    *,
    s3_bucket: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBotAlias.S3BucketLogDestinationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64da9bcfbd2b2bd9dba3eb1c7ddae66c5d2eeb778bfa000ca200015ca8968205(
    *,
    destination: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBotAlias.AudioLogDestinationProperty, typing.Dict[builtins.str, typing.Any]]],
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fa90f2791fe89d6201e6271583ea7f187021e13990dfc56fb5b9d21cd0597fc(
    *,
    bot_alias_locale_setting: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBotAlias.BotAliasLocaleSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
    locale_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dafc846484ddd046f32610ca8300607ee344e453911b95e386338096b5265a0b(
    *,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
    code_hook_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBotAlias.CodeHookSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4b6c748ce549d24594ec045dcb720ee3c78bdc65181ef3fcc7e7270aac3dd45(
    *,
    cloud_watch_log_group_arn: builtins.str,
    log_prefix: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cd567ca149d2ddc4a15e2c8b606a157b295d21d28be7cf8887e0415dc7d1f70(
    *,
    lambda_code_hook: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBotAlias.LambdaCodeHookProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b3bbd49ff07926107022ac3da1633a850323778ca95a0336ced992c0fa69295(
    *,
    audio_log_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBotAlias.AudioLogSettingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    text_log_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBotAlias.TextLogSettingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__237ac618bd82501cc4eeef1b6bef37b79a6a110591930a7ca2bdf70a7469971a(
    *,
    code_hook_interface_version: builtins.str,
    lambda_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b1ee0eb3567ddc82ad62e8f5ce649b310fc9a1ef0580dc3d8203fe333ba91cb(
    *,
    log_prefix: builtins.str,
    s3_bucket_arn: builtins.str,
    kms_key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__964fd3d3c5e4dd05d12a570da3c37d53cad4c1eb4b1978b3fdb092a2f7ea63be(
    *,
    detect_sentiment: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bedf1e9b290471f5b443d8e1d723d7bf856489156d6ae34dc0371643449b3287(
    *,
    cloud_watch: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBotAlias.CloudWatchLogGroupLogDestinationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36c17e23b7248b4c9083a2060e90ef8caa965339b7f35431c3d9740cb6accfa8(
    *,
    destination: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBotAlias.TextLogDestinationProperty, typing.Dict[builtins.str, typing.Any]]],
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__738c59c8472d47ce88d44e92ffd9f33e52944ccc1849febc9bf2f7edbd7c3db2(
    *,
    bot_alias_name: builtins.str,
    bot_id: builtins.str,
    bot_alias_locale_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBotAlias.BotAliasLocaleSettingsItemProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    bot_alias_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    bot_version: typing.Optional[builtins.str] = None,
    conversation_log_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBotAlias.ConversationLogSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    sentiment_analysis_settings: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bd27c18d3e2a58ae9aef768e05a25ed92243f8298c9575d9ff15c1d7f1aae83(
    *,
    data_privacy: typing.Any,
    idle_session_ttl_in_seconds: jsii.Number,
    name: builtins.str,
    role_arn: builtins.str,
    auto_build_bot_locales: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    bot_file_s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    bot_locales: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.BotLocaleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    bot_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    test_bot_alias_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBot.TestBotAliasSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    test_bot_alias_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f9a25d6b442565e4ffb72003af0c316d38fe2ab4bfc804150cdde827b2a9544(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bot_id: builtins.str,
    bot_version_locale_specification: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBotVersion.BotVersionLocaleSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__021d517039d5a6a9e565ebda539e800914ac9e27a462b68b4f16c736f973ecaa(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ed72c6648e5beaf5c609fdc25822e27c9d7d030f222a3590f88326fd6d4ef9d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3695fdd3e0dc7398529cc6a7cac33b2ce01960db4218cbd75288c1c43ba138a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59417360b74b60eeb0ab210b6bdfe82a4a6edef5d905cb893286714abdbbfa99(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBotVersion.BotVersionLocaleSpecificationProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15e61488889e270b05ad7dfb944cf4d12160347f937d69379819be904fe1a59e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab455ef0a33df88b4f34bc9b9a0a95974e19be27d0ca983866a8393ea952e077(
    *,
    source_bot_version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4802f8ce0abbf146138354d6e73113a70e24b8b7c9612564e44de4c4aabef220(
    *,
    bot_version_locale_details: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBotVersion.BotVersionLocaleDetailsProperty, typing.Dict[builtins.str, typing.Any]]],
    locale_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7e84893518e25327247dbe2e6a44e1ceeb51478dafbe33bce09ea7685937be5(
    *,
    bot_id: builtins.str,
    bot_version_locale_specification: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBotVersion.BotVersionLocaleSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c4e37a39c1961787db85c32c8fd5d0f194dd3d7ace3f425501ca99f4a6bfaf9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy: typing.Any,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8c541ffb1f95d8385c5fc1630139769cb4b5f9cddce5c2c4030383b10cbc93c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df22f9d7fb82d11696f2f7cc324ce147d61b2a46468bfd676f2d1ffa9e888e7a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bedb04f3a7639ce6dd847afa27b9015e9c5a45e10d0185b1e422d001d936196(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2269eb87c059c5d27aab85364fde6b4ccb6e21ca5bc766b939d038b5294665a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26bba8594196376d121fda2be732c9f29e1f3796c7e460c1a716addfae4eb1ae(
    *,
    policy: typing.Any,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
