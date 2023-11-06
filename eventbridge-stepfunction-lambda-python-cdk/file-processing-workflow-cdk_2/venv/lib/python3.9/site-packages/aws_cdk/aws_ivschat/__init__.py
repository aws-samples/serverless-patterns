'''
# AWS::IVSChat Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_ivschat as ivschat
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for IVSChat construct libraries](https://constructs.dev/search?q=ivschat)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::IVSChat resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IVSChat.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::IVSChat](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IVSChat.html).

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
class CfnLoggingConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ivschat.CfnLoggingConfiguration",
):
    '''The ``AWS::IVSChat::LoggingConfiguration`` resource specifies an  logging configuration that allows clients to store and record sent messages.

    For more information, see `CreateLoggingConfiguration <https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_CreateLoggingConfiguration.html>`_ in the *Amazon Interactive Video Service Chat API Reference* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivschat-loggingconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ivschat as ivschat
        
        cfn_logging_configuration = ivschat.CfnLoggingConfiguration(self, "MyCfnLoggingConfiguration",
            destination_configuration=ivschat.CfnLoggingConfiguration.DestinationConfigurationProperty(
                cloud_watch_logs=ivschat.CfnLoggingConfiguration.CloudWatchLogsDestinationConfigurationProperty(
                    log_group_name="logGroupName"
                ),
                firehose=ivschat.CfnLoggingConfiguration.FirehoseDestinationConfigurationProperty(
                    delivery_stream_name="deliveryStreamName"
                ),
                s3=ivschat.CfnLoggingConfiguration.S3DestinationConfigurationProperty(
                    bucket_name="bucketName"
                )
            ),
        
            # the properties below are optional
            name="name",
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
        destination_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnLoggingConfiguration.DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param destination_configuration: The DestinationConfiguration is a complex type that contains information about where chat content will be logged.
        :param name: Logging-configuration name. The value does not need to be unique.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f95aa7fbca48607e1b7f21599890b14234d06edef03619f810c807a7b1121eb9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLoggingConfigurationProps(
            destination_configuration=destination_configuration, name=name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27c1d1ba5ffc0c9e4e4e7ece89f8cc2e8faaf83bbca86ce90359f6b2f8ce3bcd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__960cfee712ac9c0a17c9e88a4c6409009f6eab60519ca06d434746d8c82a22e1)
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
        '''The logging-configuration ARN.

        For example: ``arn:aws:ivschat:us-west-2:123456789012:logging-configuration/abcdABCDefgh``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The logging-configuration ID.

        For example: ``abcdABCDefgh``

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''Indicates the current state of the logging configuration.

        When the state is ``ACTIVE`` , the configuration is ready to log a chat session. Valid values: ``CREATING`` | ``CREATE_FAILED`` | ``DELETING`` | ``DELETE_FAILED`` | ``UPDATING`` | ``UPDATE_FAILED`` | ``ACTIVE`` .

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

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
    @jsii.member(jsii_name="destinationConfiguration")
    def destination_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnLoggingConfiguration.DestinationConfigurationProperty"]:
        '''The DestinationConfiguration is a complex type that contains information about where chat content will be logged.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnLoggingConfiguration.DestinationConfigurationProperty"], jsii.get(self, "destinationConfiguration"))

    @destination_configuration.setter
    def destination_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnLoggingConfiguration.DestinationConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e46decd1e1c506586056a4500db47bf530da54ddb65e39302dbbaf6ec3a931d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''Logging-configuration name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26ed8c160f39e69de50d5c80393304dffb844ea45ad771cb30d8defdb30ce9f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__836b5ee2ad1b8daae63f67c3a8136ba0d9480523fa98563aacd6b2dbb595de39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ivschat.CfnLoggingConfiguration.CloudWatchLogsDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_name": "logGroupName"},
    )
    class CloudWatchLogsDestinationConfigurationProperty:
        def __init__(self, *, log_group_name: builtins.str) -> None:
            '''The CloudWatchLogsDestinationConfiguration property type specifies a CloudWatch Logs location where chat logs will be stored.

            :param log_group_name: Name of the Amazon Cloudwatch Logs destination where chat activity will be logged.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-loggingconfiguration-cloudwatchlogsdestinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ivschat as ivschat
                
                cloud_watch_logs_destination_configuration_property = ivschat.CfnLoggingConfiguration.CloudWatchLogsDestinationConfigurationProperty(
                    log_group_name="logGroupName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__692a23b9c3f78e60addd9b8dcdcc9084e9ccef85c62bfcb7da6c98b0c8e17021)
                check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "log_group_name": log_group_name,
            }

        @builtins.property
        def log_group_name(self) -> builtins.str:
            '''Name of the Amazon Cloudwatch Logs destination where chat activity will be logged.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-loggingconfiguration-cloudwatchlogsdestinationconfiguration.html#cfn-ivschat-loggingconfiguration-cloudwatchlogsdestinationconfiguration-loggroupname
            '''
            result = self._values.get("log_group_name")
            assert result is not None, "Required property 'log_group_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLogsDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ivschat.CfnLoggingConfiguration.DestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_logs": "cloudWatchLogs",
            "firehose": "firehose",
            "s3": "s3",
        },
    )
    class DestinationConfigurationProperty:
        def __init__(
            self,
            *,
            cloud_watch_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLoggingConfiguration.CloudWatchLogsDestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            firehose: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLoggingConfiguration.FirehoseDestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLoggingConfiguration.S3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The DestinationConfiguration property type describes a location where chat logs will be stored.

            Each member represents the configuration of one log destination. For logging, you define only one type of destination.

            :param cloud_watch_logs: An Amazon CloudWatch Logs destination configuration where chat activity will be logged.
            :param firehose: An Amazon Kinesis Data Firehose destination configuration where chat activity will be logged.
            :param s3: An Amazon S3 destination configuration where chat activity will be logged.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-loggingconfiguration-destinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ivschat as ivschat
                
                destination_configuration_property = ivschat.CfnLoggingConfiguration.DestinationConfigurationProperty(
                    cloud_watch_logs=ivschat.CfnLoggingConfiguration.CloudWatchLogsDestinationConfigurationProperty(
                        log_group_name="logGroupName"
                    ),
                    firehose=ivschat.CfnLoggingConfiguration.FirehoseDestinationConfigurationProperty(
                        delivery_stream_name="deliveryStreamName"
                    ),
                    s3=ivschat.CfnLoggingConfiguration.S3DestinationConfigurationProperty(
                        bucket_name="bucketName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__444c65021c218d7e77439678be8af18e8e2dc2bccc2bfac5f3047a512bcda98c)
                check_type(argname="argument cloud_watch_logs", value=cloud_watch_logs, expected_type=type_hints["cloud_watch_logs"])
                check_type(argname="argument firehose", value=firehose, expected_type=type_hints["firehose"])
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloud_watch_logs is not None:
                self._values["cloud_watch_logs"] = cloud_watch_logs
            if firehose is not None:
                self._values["firehose"] = firehose
            if s3 is not None:
                self._values["s3"] = s3

        @builtins.property
        def cloud_watch_logs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLoggingConfiguration.CloudWatchLogsDestinationConfigurationProperty"]]:
            '''An Amazon CloudWatch Logs destination configuration where chat activity will be logged.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-loggingconfiguration-destinationconfiguration.html#cfn-ivschat-loggingconfiguration-destinationconfiguration-cloudwatchlogs
            '''
            result = self._values.get("cloud_watch_logs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLoggingConfiguration.CloudWatchLogsDestinationConfigurationProperty"]], result)

        @builtins.property
        def firehose(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLoggingConfiguration.FirehoseDestinationConfigurationProperty"]]:
            '''An Amazon Kinesis Data Firehose destination configuration where chat activity will be logged.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-loggingconfiguration-destinationconfiguration.html#cfn-ivschat-loggingconfiguration-destinationconfiguration-firehose
            '''
            result = self._values.get("firehose")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLoggingConfiguration.FirehoseDestinationConfigurationProperty"]], result)

        @builtins.property
        def s3(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLoggingConfiguration.S3DestinationConfigurationProperty"]]:
            '''An Amazon S3 destination configuration where chat activity will be logged.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-loggingconfiguration-destinationconfiguration.html#cfn-ivschat-loggingconfiguration-destinationconfiguration-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLoggingConfiguration.S3DestinationConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ivschat.CfnLoggingConfiguration.FirehoseDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"delivery_stream_name": "deliveryStreamName"},
    )
    class FirehoseDestinationConfigurationProperty:
        def __init__(self, *, delivery_stream_name: builtins.str) -> None:
            '''The FirehoseDestinationConfiguration property type specifies a Kinesis Firehose location where chat logs will be stored.

            :param delivery_stream_name: Name of the Amazon Kinesis Firehose delivery stream where chat activity will be logged.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-loggingconfiguration-firehosedestinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ivschat as ivschat
                
                firehose_destination_configuration_property = ivschat.CfnLoggingConfiguration.FirehoseDestinationConfigurationProperty(
                    delivery_stream_name="deliveryStreamName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a25c4e628ef47763b45189497fc2d57f8d09166b892dda63567ac89ab67a4125)
                check_type(argname="argument delivery_stream_name", value=delivery_stream_name, expected_type=type_hints["delivery_stream_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "delivery_stream_name": delivery_stream_name,
            }

        @builtins.property
        def delivery_stream_name(self) -> builtins.str:
            '''Name of the Amazon Kinesis Firehose delivery stream where chat activity will be logged.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-loggingconfiguration-firehosedestinationconfiguration.html#cfn-ivschat-loggingconfiguration-firehosedestinationconfiguration-deliverystreamname
            '''
            result = self._values.get("delivery_stream_name")
            assert result is not None, "Required property 'delivery_stream_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FirehoseDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ivschat.CfnLoggingConfiguration.S3DestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_name": "bucketName"},
    )
    class S3DestinationConfigurationProperty:
        def __init__(self, *, bucket_name: builtins.str) -> None:
            '''The S3DestinationConfiguration property type specifies an S3 location where chat logs will be stored.

            :param bucket_name: Name of the Amazon S3 bucket where chat activity will be logged.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-loggingconfiguration-s3destinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ivschat as ivschat
                
                s3_destination_configuration_property = ivschat.CfnLoggingConfiguration.S3DestinationConfigurationProperty(
                    bucket_name="bucketName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c037cb3283641604b00606142bfc019ab700b409deb4e9436a93bc4c24eb662f)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
            }

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''Name of the Amazon S3 bucket where chat activity will be logged.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-loggingconfiguration-s3destinationconfiguration.html#cfn-ivschat-loggingconfiguration-s3destinationconfiguration-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3DestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ivschat.CfnLoggingConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "destination_configuration": "destinationConfiguration",
        "name": "name",
        "tags": "tags",
    },
)
class CfnLoggingConfigurationProps:
    def __init__(
        self,
        *,
        destination_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLoggingConfiguration.DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLoggingConfiguration``.

        :param destination_configuration: The DestinationConfiguration is a complex type that contains information about where chat content will be logged.
        :param name: Logging-configuration name. The value does not need to be unique.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivschat-loggingconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ivschat as ivschat
            
            cfn_logging_configuration_props = ivschat.CfnLoggingConfigurationProps(
                destination_configuration=ivschat.CfnLoggingConfiguration.DestinationConfigurationProperty(
                    cloud_watch_logs=ivschat.CfnLoggingConfiguration.CloudWatchLogsDestinationConfigurationProperty(
                        log_group_name="logGroupName"
                    ),
                    firehose=ivschat.CfnLoggingConfiguration.FirehoseDestinationConfigurationProperty(
                        delivery_stream_name="deliveryStreamName"
                    ),
                    s3=ivschat.CfnLoggingConfiguration.S3DestinationConfigurationProperty(
                        bucket_name="bucketName"
                    )
                ),
            
                # the properties below are optional
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd8211326716cc0769a314101b6dc245bc511241754ebffa1df713e7defb4688)
            check_type(argname="argument destination_configuration", value=destination_configuration, expected_type=type_hints["destination_configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_configuration": destination_configuration,
        }
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def destination_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnLoggingConfiguration.DestinationConfigurationProperty]:
        '''The DestinationConfiguration is a complex type that contains information about where chat content will be logged.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivschat-loggingconfiguration.html#cfn-ivschat-loggingconfiguration-destinationconfiguration
        '''
        result = self._values.get("destination_configuration")
        assert result is not None, "Required property 'destination_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnLoggingConfiguration.DestinationConfigurationProperty], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Logging-configuration name.

        The value does not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivschat-loggingconfiguration.html#cfn-ivschat-loggingconfiguration-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivschat-loggingconfiguration.html#cfn-ivschat-loggingconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLoggingConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnRoom(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ivschat.CfnRoom",
):
    '''The ``AWS::IVSChat::Room`` resource specifies an  room that allows clients to connect and pass messages.

    For more information, see `CreateRoom <https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_CreateRoom.html>`_ in the *Amazon Interactive Video Service Chat API Reference* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivschat-room.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ivschat as ivschat
        
        cfn_room = ivschat.CfnRoom(self, "MyCfnRoom",
            logging_configuration_identifiers=["loggingConfigurationIdentifiers"],
            maximum_message_length=123,
            maximum_message_rate_per_second=123,
            message_review_handler=ivschat.CfnRoom.MessageReviewHandlerProperty(
                fallback_result="fallbackResult",
                uri="uri"
            ),
            name="name",
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
        logging_configuration_identifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
        maximum_message_length: typing.Optional[jsii.Number] = None,
        maximum_message_rate_per_second: typing.Optional[jsii.Number] = None,
        message_review_handler: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRoom.MessageReviewHandlerProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param logging_configuration_identifiers: List of logging-configuration identifiers attached to the room.
        :param maximum_message_length: Maximum number of characters in a single message. Messages are expected to be UTF-8 encoded and this limit applies specifically to rune/code-point count, not number of bytes. Default: - 500
        :param maximum_message_rate_per_second: Maximum number of messages per second that can be sent to the room (by all clients). Default: - 10
        :param message_review_handler: Configuration information for optional review of messages.
        :param name: Room name. The value does not need to be unique.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b4e5ca285f18f1e8f75ce6f44ea1cf5cd39a13086ac408f0f6de6c51064f22d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRoomProps(
            logging_configuration_identifiers=logging_configuration_identifiers,
            maximum_message_length=maximum_message_length,
            maximum_message_rate_per_second=maximum_message_rate_per_second,
            message_review_handler=message_review_handler,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ce1c1c052b08ab9350a756228819c19dc398433872a68be1f852466c2eb1f71)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d783e239ad0d8f6dfc82d8df73722abb0544413600c3439c3777ac5e52cc5e4e)
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
        '''The room ARN.

        For example: ``arn:aws:ivschat:us-west-2:123456789012:room/abcdABCDefgh``

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The room ID.

        For example: ``abcdABCDefgh``

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
    @jsii.member(jsii_name="loggingConfigurationIdentifiers")
    def logging_configuration_identifiers(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''List of logging-configuration identifiers attached to the room.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "loggingConfigurationIdentifiers"))

    @logging_configuration_identifiers.setter
    def logging_configuration_identifiers(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__715c94a6d3106670ad6914a07671851743aaab45133544bce1c05e91ef1afee3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggingConfigurationIdentifiers", value)

    @builtins.property
    @jsii.member(jsii_name="maximumMessageLength")
    def maximum_message_length(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of characters in a single message.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumMessageLength"))

    @maximum_message_length.setter
    def maximum_message_length(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ad0052f323da91d86d28797dbfe265aad9f18133d2aed326936401d24e74e5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumMessageLength", value)

    @builtins.property
    @jsii.member(jsii_name="maximumMessageRatePerSecond")
    def maximum_message_rate_per_second(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of messages per second that can be sent to the room (by all clients).'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumMessageRatePerSecond"))

    @maximum_message_rate_per_second.setter
    def maximum_message_rate_per_second(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b897f8b0aae144b6ad3e2979d91ce62b5b66428bf3306bc6bc790b664db0f053)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumMessageRatePerSecond", value)

    @builtins.property
    @jsii.member(jsii_name="messageReviewHandler")
    def message_review_handler(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRoom.MessageReviewHandlerProperty"]]:
        '''Configuration information for optional review of messages.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRoom.MessageReviewHandlerProperty"]], jsii.get(self, "messageReviewHandler"))

    @message_review_handler.setter
    def message_review_handler(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRoom.MessageReviewHandlerProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e799bee581432f25d4ae8c52d6061972639da5726d12f7994dd765f9dce685f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageReviewHandler", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''Room name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1321d29c7baab529603b109b828d2f7d3139eb364593ec2f54a0ff1585184366)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c129383c713cecd593f8d586f57442188747729d3736326bbf0a38bacba4a349)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ivschat.CfnRoom.MessageReviewHandlerProperty",
        jsii_struct_bases=[],
        name_mapping={"fallback_result": "fallbackResult", "uri": "uri"},
    )
    class MessageReviewHandlerProperty:
        def __init__(
            self,
            *,
            fallback_result: typing.Optional[builtins.str] = None,
            uri: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The MessageReviewHandler property type specifies configuration information for optional message review.

            :param fallback_result: Specifies the fallback behavior (whether the message is allowed or denied) if the handler does not return a valid response, encounters an error, or times out. (For the timeout period, see `Service Quotas <https://docs.aws.amazon.com/ivs/latest/userguide/service-quotas.html>`_ .) If allowed, the message is delivered with returned content to all users connected to the room. If denied, the message is not delivered to any user. *Default* : ``ALLOW`` Default: - "ALLOW"
            :param uri: Identifier of the message review handler. Currently this must be an ARN of a lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-room-messagereviewhandler.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ivschat as ivschat
                
                message_review_handler_property = ivschat.CfnRoom.MessageReviewHandlerProperty(
                    fallback_result="fallbackResult",
                    uri="uri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b8de671f791820abae21cf6b0bd8d2f03cbf454fb6af42a06db0dd74e9fa2d28)
                check_type(argname="argument fallback_result", value=fallback_result, expected_type=type_hints["fallback_result"])
                check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if fallback_result is not None:
                self._values["fallback_result"] = fallback_result
            if uri is not None:
                self._values["uri"] = uri

        @builtins.property
        def fallback_result(self) -> typing.Optional[builtins.str]:
            '''Specifies the fallback behavior (whether the message is allowed or denied) if the handler does not return a valid response, encounters an error, or times out.

            (For the timeout period, see `Service Quotas <https://docs.aws.amazon.com/ivs/latest/userguide/service-quotas.html>`_ .) If allowed, the message is delivered with returned content to all users connected to the room. If denied, the message is not delivered to any user.

            *Default* : ``ALLOW``

            :default: - "ALLOW"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-room-messagereviewhandler.html#cfn-ivschat-room-messagereviewhandler-fallbackresult
            '''
            result = self._values.get("fallback_result")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def uri(self) -> typing.Optional[builtins.str]:
            '''Identifier of the message review handler.

            Currently this must be an ARN of a lambda function.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ivschat-room-messagereviewhandler.html#cfn-ivschat-room-messagereviewhandler-uri
            '''
            result = self._values.get("uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MessageReviewHandlerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ivschat.CfnRoomProps",
    jsii_struct_bases=[],
    name_mapping={
        "logging_configuration_identifiers": "loggingConfigurationIdentifiers",
        "maximum_message_length": "maximumMessageLength",
        "maximum_message_rate_per_second": "maximumMessageRatePerSecond",
        "message_review_handler": "messageReviewHandler",
        "name": "name",
        "tags": "tags",
    },
)
class CfnRoomProps:
    def __init__(
        self,
        *,
        logging_configuration_identifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
        maximum_message_length: typing.Optional[jsii.Number] = None,
        maximum_message_rate_per_second: typing.Optional[jsii.Number] = None,
        message_review_handler: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRoom.MessageReviewHandlerProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRoom``.

        :param logging_configuration_identifiers: List of logging-configuration identifiers attached to the room.
        :param maximum_message_length: Maximum number of characters in a single message. Messages are expected to be UTF-8 encoded and this limit applies specifically to rune/code-point count, not number of bytes. Default: - 500
        :param maximum_message_rate_per_second: Maximum number of messages per second that can be sent to the room (by all clients). Default: - 10
        :param message_review_handler: Configuration information for optional review of messages.
        :param name: Room name. The value does not need to be unique.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivschat-room.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ivschat as ivschat
            
            cfn_room_props = ivschat.CfnRoomProps(
                logging_configuration_identifiers=["loggingConfigurationIdentifiers"],
                maximum_message_length=123,
                maximum_message_rate_per_second=123,
                message_review_handler=ivschat.CfnRoom.MessageReviewHandlerProperty(
                    fallback_result="fallbackResult",
                    uri="uri"
                ),
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f899c64588038b94c1a897b6415ff71753daa2f6faffb1c99564c9bc3fec95e3)
            check_type(argname="argument logging_configuration_identifiers", value=logging_configuration_identifiers, expected_type=type_hints["logging_configuration_identifiers"])
            check_type(argname="argument maximum_message_length", value=maximum_message_length, expected_type=type_hints["maximum_message_length"])
            check_type(argname="argument maximum_message_rate_per_second", value=maximum_message_rate_per_second, expected_type=type_hints["maximum_message_rate_per_second"])
            check_type(argname="argument message_review_handler", value=message_review_handler, expected_type=type_hints["message_review_handler"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if logging_configuration_identifiers is not None:
            self._values["logging_configuration_identifiers"] = logging_configuration_identifiers
        if maximum_message_length is not None:
            self._values["maximum_message_length"] = maximum_message_length
        if maximum_message_rate_per_second is not None:
            self._values["maximum_message_rate_per_second"] = maximum_message_rate_per_second
        if message_review_handler is not None:
            self._values["message_review_handler"] = message_review_handler
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def logging_configuration_identifiers(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''List of logging-configuration identifiers attached to the room.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivschat-room.html#cfn-ivschat-room-loggingconfigurationidentifiers
        '''
        result = self._values.get("logging_configuration_identifiers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def maximum_message_length(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of characters in a single message.

        Messages are expected to be UTF-8 encoded and this limit applies specifically to rune/code-point count, not number of bytes.

        :default: - 500

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivschat-room.html#cfn-ivschat-room-maximummessagelength
        '''
        result = self._values.get("maximum_message_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maximum_message_rate_per_second(self) -> typing.Optional[jsii.Number]:
        '''Maximum number of messages per second that can be sent to the room (by all clients).

        :default: - 10

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivschat-room.html#cfn-ivschat-room-maximummessageratepersecond
        '''
        result = self._values.get("maximum_message_rate_per_second")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def message_review_handler(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRoom.MessageReviewHandlerProperty]]:
        '''Configuration information for optional review of messages.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivschat-room.html#cfn-ivschat-room-messagereviewhandler
        '''
        result = self._values.get("message_review_handler")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRoom.MessageReviewHandlerProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Room name.

        The value does not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivschat-room.html#cfn-ivschat-room-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivschat-room.html#cfn-ivschat-room-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRoomProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnLoggingConfiguration",
    "CfnLoggingConfigurationProps",
    "CfnRoom",
    "CfnRoomProps",
]

publication.publish()

def _typecheckingstub__f95aa7fbca48607e1b7f21599890b14234d06edef03619f810c807a7b1121eb9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    destination_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLoggingConfiguration.DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27c1d1ba5ffc0c9e4e4e7ece89f8cc2e8faaf83bbca86ce90359f6b2f8ce3bcd(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__960cfee712ac9c0a17c9e88a4c6409009f6eab60519ca06d434746d8c82a22e1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e46decd1e1c506586056a4500db47bf530da54ddb65e39302dbbaf6ec3a931d1(
    value: typing.Union[_IResolvable_da3f097b, CfnLoggingConfiguration.DestinationConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26ed8c160f39e69de50d5c80393304dffb844ea45ad771cb30d8defdb30ce9f8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__836b5ee2ad1b8daae63f67c3a8136ba0d9480523fa98563aacd6b2dbb595de39(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__692a23b9c3f78e60addd9b8dcdcc9084e9ccef85c62bfcb7da6c98b0c8e17021(
    *,
    log_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__444c65021c218d7e77439678be8af18e8e2dc2bccc2bfac5f3047a512bcda98c(
    *,
    cloud_watch_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLoggingConfiguration.CloudWatchLogsDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    firehose: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLoggingConfiguration.FirehoseDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLoggingConfiguration.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a25c4e628ef47763b45189497fc2d57f8d09166b892dda63567ac89ab67a4125(
    *,
    delivery_stream_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c037cb3283641604b00606142bfc019ab700b409deb4e9436a93bc4c24eb662f(
    *,
    bucket_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd8211326716cc0769a314101b6dc245bc511241754ebffa1df713e7defb4688(
    *,
    destination_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLoggingConfiguration.DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b4e5ca285f18f1e8f75ce6f44ea1cf5cd39a13086ac408f0f6de6c51064f22d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    logging_configuration_identifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
    maximum_message_length: typing.Optional[jsii.Number] = None,
    maximum_message_rate_per_second: typing.Optional[jsii.Number] = None,
    message_review_handler: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRoom.MessageReviewHandlerProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ce1c1c052b08ab9350a756228819c19dc398433872a68be1f852466c2eb1f71(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d783e239ad0d8f6dfc82d8df73722abb0544413600c3439c3777ac5e52cc5e4e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__715c94a6d3106670ad6914a07671851743aaab45133544bce1c05e91ef1afee3(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ad0052f323da91d86d28797dbfe265aad9f18133d2aed326936401d24e74e5f(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b897f8b0aae144b6ad3e2979d91ce62b5b66428bf3306bc6bc790b664db0f053(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e799bee581432f25d4ae8c52d6061972639da5726d12f7994dd765f9dce685f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRoom.MessageReviewHandlerProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1321d29c7baab529603b109b828d2f7d3139eb364593ec2f54a0ff1585184366(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c129383c713cecd593f8d586f57442188747729d3736326bbf0a38bacba4a349(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8de671f791820abae21cf6b0bd8d2f03cbf454fb6af42a06db0dd74e9fa2d28(
    *,
    fallback_result: typing.Optional[builtins.str] = None,
    uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f899c64588038b94c1a897b6415ff71753daa2f6faffb1c99564c9bc3fec95e3(
    *,
    logging_configuration_identifiers: typing.Optional[typing.Sequence[builtins.str]] = None,
    maximum_message_length: typing.Optional[jsii.Number] = None,
    maximum_message_rate_per_second: typing.Optional[jsii.Number] = None,
    message_review_handler: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRoom.MessageReviewHandlerProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
