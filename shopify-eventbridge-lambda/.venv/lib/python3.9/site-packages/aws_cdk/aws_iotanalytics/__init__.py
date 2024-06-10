'''
# AWS IoT Analytics Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_iotanalytics as iotanalytics
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for IoTAnalytics construct libraries](https://constructs.dev/search?q=iotanalytics)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::IoTAnalytics resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTAnalytics.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::IoTAnalytics](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTAnalytics.html).

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
class CfnChannel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotanalytics.CfnChannel",
):
    '''The AWS::IoTAnalytics::Channel resource collects data from an MQTT topic and archives the raw, unprocessed messages before publishing the data to a pipeline.

    For more information, see `How to Use AWS IoT Analytics <https://docs.aws.amazon.com/iotanalytics/latest/userguide/welcome.html#aws-iot-analytics-how>`_ in the *AWS IoT Analytics User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html
    :cloudformationResource: AWS::IoTAnalytics::Channel
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotanalytics as iotanalytics
        
        # service_managed_s3: Any
        
        cfn_channel = iotanalytics.CfnChannel(self, "MyCfnChannel",
            channel_name="channelName",
            channel_storage=iotanalytics.CfnChannel.ChannelStorageProperty(
                customer_managed_s3=iotanalytics.CfnChannel.CustomerManagedS3Property(
                    bucket="bucket",
                    role_arn="roleArn",
        
                    # the properties below are optional
                    key_prefix="keyPrefix"
                ),
                service_managed_s3=service_managed_s3
            ),
            retention_period=iotanalytics.CfnChannel.RetentionPeriodProperty(
                number_of_days=123,
                unlimited=False
            ),
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
        channel_name: typing.Optional[builtins.str] = None,
        channel_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnChannel.ChannelStorageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        retention_period: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnChannel.RetentionPeriodProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param channel_name: The name of the channel.
        :param channel_storage: Where channel data is stored.
        :param retention_period: How long, in days, message data is kept for the channel.
        :param tags: Metadata which can be used to manage the channel. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8332c208b00865f2cfdad255e86ebeabe2b2b68a70b8fa26b96ec9b8c1e25499)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnChannelProps(
            channel_name=channel_name,
            channel_storage=channel_storage,
            retention_period=retention_period,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3afdfadc9a4edd9b5c35f5d06ae9f61c5c1ebaa012686da4a923c736b3fa979b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8e6a928cd907de244850e605fb376bc7dc51306fe95d12a79b27dbb27038d241)
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
        '''
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
    @jsii.member(jsii_name="channelName")
    def channel_name(self) -> typing.Optional[builtins.str]:
        '''The name of the channel.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelName"))

    @channel_name.setter
    def channel_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65896b87ac00168069b3023b993de25e4b6e0d2f7062c80b2bd040584f8e7e1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelName", value)

    @builtins.property
    @jsii.member(jsii_name="channelStorage")
    def channel_storage(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.ChannelStorageProperty"]]:
        '''Where channel data is stored.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.ChannelStorageProperty"]], jsii.get(self, "channelStorage"))

    @channel_storage.setter
    def channel_storage(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.ChannelStorageProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__897830b597b7f068ad39137a599c6bcc3329380b80a31c457e181b64e3c87677)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelStorage", value)

    @builtins.property
    @jsii.member(jsii_name="retentionPeriod")
    def retention_period(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.RetentionPeriodProperty"]]:
        '''How long, in days, message data is kept for the channel.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.RetentionPeriodProperty"]], jsii.get(self, "retentionPeriod"))

    @retention_period.setter
    def retention_period(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.RetentionPeriodProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e6072ad5478c8c43508f65ecec006c8dfe38ec650f0a67eb9970771e8d1484e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata which can be used to manage the channel.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32eb80eb4a923d8935d89ce4d4e01a0cfaf3d7c894b3102ee7c33c63cf554635)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnChannel.ChannelStorageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "customer_managed_s3": "customerManagedS3",
            "service_managed_s3": "serviceManagedS3",
        },
    )
    class ChannelStorageProperty:
        def __init__(
            self,
            *,
            customer_managed_s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnChannel.CustomerManagedS3Property", typing.Dict[builtins.str, typing.Any]]]] = None,
            service_managed_s3: typing.Any = None,
        ) -> None:
            '''Where channel data is stored.

            You may choose one of ``serviceManagedS3`` , ``customerManagedS3`` storage. If not specified, the default is ``serviceManagedS3`` . This can't be changed after creation of the channel.

            :param customer_managed_s3: Used to store channel data in an S3 bucket that you manage. If customer managed storage is selected, the ``retentionPeriod`` parameter is ignored. You can't change the choice of S3 storage after the data store is created.
            :param service_managed_s3: Used to store channel data in an S3 bucket managed by AWS IoT Analytics . You can't change the choice of S3 storage after the data store is created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-channelstorage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                # service_managed_s3: Any
                
                channel_storage_property = iotanalytics.CfnChannel.ChannelStorageProperty(
                    customer_managed_s3=iotanalytics.CfnChannel.CustomerManagedS3Property(
                        bucket="bucket",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        key_prefix="keyPrefix"
                    ),
                    service_managed_s3=service_managed_s3
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cbc8b32257128c3df6a233f408369201793dc955662fe4cece76a7bdcaec3ecd)
                check_type(argname="argument customer_managed_s3", value=customer_managed_s3, expected_type=type_hints["customer_managed_s3"])
                check_type(argname="argument service_managed_s3", value=service_managed_s3, expected_type=type_hints["service_managed_s3"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if customer_managed_s3 is not None:
                self._values["customer_managed_s3"] = customer_managed_s3
            if service_managed_s3 is not None:
                self._values["service_managed_s3"] = service_managed_s3

        @builtins.property
        def customer_managed_s3(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.CustomerManagedS3Property"]]:
            '''Used to store channel data in an S3 bucket that you manage.

            If customer managed storage is selected, the ``retentionPeriod`` parameter is ignored. You can't change the choice of S3 storage after the data store is created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-channelstorage.html#cfn-iotanalytics-channel-channelstorage-customermanageds3
            '''
            result = self._values.get("customer_managed_s3")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.CustomerManagedS3Property"]], result)

        @builtins.property
        def service_managed_s3(self) -> typing.Any:
            '''Used to store channel data in an S3 bucket managed by AWS IoT Analytics .

            You can't change the choice of S3 storage after the data store is created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-channelstorage.html#cfn-iotanalytics-channel-channelstorage-servicemanageds3
            '''
            result = self._values.get("service_managed_s3")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ChannelStorageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnChannel.CustomerManagedS3Property",
        jsii_struct_bases=[],
        name_mapping={
            "bucket": "bucket",
            "role_arn": "roleArn",
            "key_prefix": "keyPrefix",
        },
    )
    class CustomerManagedS3Property:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            role_arn: builtins.str,
            key_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Used to store channel data in an S3 bucket that you manage.

            :param bucket: The name of the S3 bucket in which channel data is stored.
            :param role_arn: The ARN of the role that grants AWS IoT Analytics permission to interact with your Amazon S3 resources.
            :param key_prefix: (Optional) The prefix used to create the keys of the channel data objects. Each object in an S3 bucket has a key that is its unique identifier within the bucket (each object in a bucket has exactly one key). The prefix must end with a forward slash (/).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-customermanageds3.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                customer_managed_s3_property = iotanalytics.CfnChannel.CustomerManagedS3Property(
                    bucket="bucket",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    key_prefix="keyPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__44d2e287ab890d34114c77aaedf5da8bf78be529b28b900b0f298f1e6f2eca2e)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument key_prefix", value=key_prefix, expected_type=type_hints["key_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "role_arn": role_arn,
            }
            if key_prefix is not None:
                self._values["key_prefix"] = key_prefix

        @builtins.property
        def bucket(self) -> builtins.str:
            '''The name of the S3 bucket in which channel data is stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-customermanageds3.html#cfn-iotanalytics-channel-customermanageds3-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the role that grants AWS IoT Analytics permission to interact with your Amazon S3 resources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-customermanageds3.html#cfn-iotanalytics-channel-customermanageds3-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_prefix(self) -> typing.Optional[builtins.str]:
            '''(Optional) The prefix used to create the keys of the channel data objects.

            Each object in an S3 bucket has a key that is its unique identifier within the bucket (each object in a bucket has exactly one key). The prefix must end with a forward slash (/).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-customermanageds3.html#cfn-iotanalytics-channel-customermanageds3-keyprefix
            '''
            result = self._values.get("key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomerManagedS3Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnChannel.RetentionPeriodProperty",
        jsii_struct_bases=[],
        name_mapping={"number_of_days": "numberOfDays", "unlimited": "unlimited"},
    )
    class RetentionPeriodProperty:
        def __init__(
            self,
            *,
            number_of_days: typing.Optional[jsii.Number] = None,
            unlimited: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''How long, in days, message data is kept.

            :param number_of_days: The number of days that message data is kept. The ``unlimited`` parameter must be false.
            :param unlimited: If true, message data is kept indefinitely.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-retentionperiod.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                retention_period_property = iotanalytics.CfnChannel.RetentionPeriodProperty(
                    number_of_days=123,
                    unlimited=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c61da11bbb4ca5d43e4fd9639491db4447e4c3f71df13bf8e176559eab373cb2)
                check_type(argname="argument number_of_days", value=number_of_days, expected_type=type_hints["number_of_days"])
                check_type(argname="argument unlimited", value=unlimited, expected_type=type_hints["unlimited"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if number_of_days is not None:
                self._values["number_of_days"] = number_of_days
            if unlimited is not None:
                self._values["unlimited"] = unlimited

        @builtins.property
        def number_of_days(self) -> typing.Optional[jsii.Number]:
            '''The number of days that message data is kept.

            The ``unlimited`` parameter must be false.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-retentionperiod.html#cfn-iotanalytics-channel-retentionperiod-numberofdays
            '''
            result = self._values.get("number_of_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def unlimited(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If true, message data is kept indefinitely.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-channel-retentionperiod.html#cfn-iotanalytics-channel-retentionperiod-unlimited
            '''
            result = self._values.get("unlimited")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RetentionPeriodProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotanalytics.CfnChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "channel_name": "channelName",
        "channel_storage": "channelStorage",
        "retention_period": "retentionPeriod",
        "tags": "tags",
    },
)
class CfnChannelProps:
    def __init__(
        self,
        *,
        channel_name: typing.Optional[builtins.str] = None,
        channel_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.ChannelStorageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        retention_period: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.RetentionPeriodProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnChannel``.

        :param channel_name: The name of the channel.
        :param channel_storage: Where channel data is stored.
        :param retention_period: How long, in days, message data is kept for the channel.
        :param tags: Metadata which can be used to manage the channel. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotanalytics as iotanalytics
            
            # service_managed_s3: Any
            
            cfn_channel_props = iotanalytics.CfnChannelProps(
                channel_name="channelName",
                channel_storage=iotanalytics.CfnChannel.ChannelStorageProperty(
                    customer_managed_s3=iotanalytics.CfnChannel.CustomerManagedS3Property(
                        bucket="bucket",
                        role_arn="roleArn",
            
                        # the properties below are optional
                        key_prefix="keyPrefix"
                    ),
                    service_managed_s3=service_managed_s3
                ),
                retention_period=iotanalytics.CfnChannel.RetentionPeriodProperty(
                    number_of_days=123,
                    unlimited=False
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1389944a7a7c5ae7ccfca31343abcc6dd4bb78b250fa7c33a3787f169cd7fdb3)
            check_type(argname="argument channel_name", value=channel_name, expected_type=type_hints["channel_name"])
            check_type(argname="argument channel_storage", value=channel_storage, expected_type=type_hints["channel_storage"])
            check_type(argname="argument retention_period", value=retention_period, expected_type=type_hints["retention_period"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if channel_name is not None:
            self._values["channel_name"] = channel_name
        if channel_storage is not None:
            self._values["channel_storage"] = channel_storage
        if retention_period is not None:
            self._values["retention_period"] = retention_period
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def channel_name(self) -> typing.Optional[builtins.str]:
        '''The name of the channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html#cfn-iotanalytics-channel-channelname
        '''
        result = self._values.get("channel_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def channel_storage(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnChannel.ChannelStorageProperty]]:
        '''Where channel data is stored.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html#cfn-iotanalytics-channel-channelstorage
        '''
        result = self._values.get("channel_storage")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnChannel.ChannelStorageProperty]], result)

    @builtins.property
    def retention_period(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnChannel.RetentionPeriodProperty]]:
        '''How long, in days, message data is kept for the channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html#cfn-iotanalytics-channel-retentionperiod
        '''
        result = self._values.get("retention_period")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnChannel.RetentionPeriodProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata which can be used to manage the channel.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html#cfn-iotanalytics-channel-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDataset(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDataset",
):
    '''The AWS::IoTAnalytics::Dataset resource stores data retrieved from a data store by applying a ``queryAction`` (an SQL query) or a ``containerAction`` (executing a containerized application).

    The data set can be populated manually by calling ``CreateDatasetContent`` or automatically according to a ``trigger`` you specify. For more information, see `How to Use AWS IoT Analytics <https://docs.aws.amazon.com/iotanalytics/latest/userguide/welcome.html#aws-iot-analytics-how>`_ in the *AWS IoT Analytics User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html
    :cloudformationResource: AWS::IoTAnalytics::Dataset
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotanalytics as iotanalytics
        
        cfn_dataset = iotanalytics.CfnDataset(self, "MyCfnDataset",
            actions=[iotanalytics.CfnDataset.ActionProperty(
                action_name="actionName",
        
                # the properties below are optional
                container_action=iotanalytics.CfnDataset.ContainerActionProperty(
                    execution_role_arn="executionRoleArn",
                    image="image",
                    resource_configuration=iotanalytics.CfnDataset.ResourceConfigurationProperty(
                        compute_type="computeType",
                        volume_size_in_gb=123
                    ),
        
                    # the properties below are optional
                    variables=[iotanalytics.CfnDataset.VariableProperty(
                        variable_name="variableName",
        
                        # the properties below are optional
                        dataset_content_version_value=iotanalytics.CfnDataset.DatasetContentVersionValueProperty(
                            dataset_name="datasetName"
                        ),
                        double_value=123,
                        output_file_uri_value=iotanalytics.CfnDataset.OutputFileUriValueProperty(
                            file_name="fileName"
                        ),
                        string_value="stringValue"
                    )]
                ),
                query_action=iotanalytics.CfnDataset.QueryActionProperty(
                    sql_query="sqlQuery",
        
                    # the properties below are optional
                    filters=[iotanalytics.CfnDataset.FilterProperty(
                        delta_time=iotanalytics.CfnDataset.DeltaTimeProperty(
                            offset_seconds=123,
                            time_expression="timeExpression"
                        )
                    )]
                )
            )],
        
            # the properties below are optional
            content_delivery_rules=[iotanalytics.CfnDataset.DatasetContentDeliveryRuleProperty(
                destination=iotanalytics.CfnDataset.DatasetContentDeliveryRuleDestinationProperty(
                    iot_events_destination_configuration=iotanalytics.CfnDataset.IotEventsDestinationConfigurationProperty(
                        input_name="inputName",
                        role_arn="roleArn"
                    ),
                    s3_destination_configuration=iotanalytics.CfnDataset.S3DestinationConfigurationProperty(
                        bucket="bucket",
                        key="key",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        glue_configuration=iotanalytics.CfnDataset.GlueConfigurationProperty(
                            database_name="databaseName",
                            table_name="tableName"
                        )
                    )
                ),
        
                # the properties below are optional
                entry_name="entryName"
            )],
            dataset_name="datasetName",
            late_data_rules=[iotanalytics.CfnDataset.LateDataRuleProperty(
                rule_configuration=iotanalytics.CfnDataset.LateDataRuleConfigurationProperty(
                    delta_time_session_window_configuration=iotanalytics.CfnDataset.DeltaTimeSessionWindowConfigurationProperty(
                        timeout_in_minutes=123
                    )
                ),
        
                # the properties below are optional
                rule_name="ruleName"
            )],
            retention_period=iotanalytics.CfnDataset.RetentionPeriodProperty(
                number_of_days=123,
                unlimited=False
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            triggers=[iotanalytics.CfnDataset.TriggerProperty(
                schedule=iotanalytics.CfnDataset.ScheduleProperty(
                    schedule_expression="scheduleExpression"
                ),
                triggering_dataset=iotanalytics.CfnDataset.TriggeringDatasetProperty(
                    dataset_name="datasetName"
                )
            )],
            versioning_configuration=iotanalytics.CfnDataset.VersioningConfigurationProperty(
                max_versions=123,
                unlimited=False
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        actions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.ActionProperty", typing.Dict[builtins.str, typing.Any]]]]],
        content_delivery_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.DatasetContentDeliveryRuleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        dataset_name: typing.Optional[builtins.str] = None,
        late_data_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.LateDataRuleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        retention_period: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.RetentionPeriodProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        triggers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.TriggerProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        versioning_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.VersioningConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param actions: The ``DatasetAction`` objects that automatically create the dataset contents.
        :param content_delivery_rules: When dataset contents are created they are delivered to destinations specified here.
        :param dataset_name: The name of the dataset.
        :param late_data_rules: A list of data rules that send notifications to CloudWatch, when data arrives late. To specify ``lateDataRules`` , the dataset must use a `DeltaTimer <https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_DeltaTime.html>`_ filter.
        :param retention_period: Optional. How long, in days, message data is kept for the dataset.
        :param tags: Metadata which can be used to manage the data set. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param triggers: The ``DatasetTrigger`` objects that specify when the dataset is automatically updated.
        :param versioning_configuration: Optional. How many versions of dataset contents are kept. If not specified or set to null, only the latest version plus the latest succeeded version (if they are different) are kept for the time period specified by the ``retentionPeriod`` parameter. For more information, see `Keeping Multiple Versions of AWS IoT Analytics datasets <https://docs.aws.amazon.com/iotanalytics/latest/userguide/getting-started.html#aws-iot-analytics-dataset-versions>`_ in the *AWS IoT Analytics User Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28e622d1f32fa52fab95276ceeda7ad3576bf8992514bb441ca9b4ec4c53e656)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDatasetProps(
            actions=actions,
            content_delivery_rules=content_delivery_rules,
            dataset_name=dataset_name,
            late_data_rules=late_data_rules,
            retention_period=retention_period,
            tags=tags,
            triggers=triggers,
            versioning_configuration=versioning_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f43abe364fcb83fda3cc5c4f98b2e4482fe72474205d310be98d8daa35ad70e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__022ee74ca256ae166d4ad18e647fce9936f9dc0446dac904fa6bfc5c57e0d328)
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
        '''
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
    @jsii.member(jsii_name="actions")
    def actions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataset.ActionProperty"]]]:
        '''The ``DatasetAction`` objects that automatically create the dataset contents.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataset.ActionProperty"]]], jsii.get(self, "actions"))

    @actions.setter
    def actions(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataset.ActionProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bea1d7db65ef2e1dd07cc6ad0511bc305600ada926a081f4afb5441eab9862f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actions", value)

    @builtins.property
    @jsii.member(jsii_name="contentDeliveryRules")
    def content_delivery_rules(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataset.DatasetContentDeliveryRuleProperty"]]]]:
        '''When dataset contents are created they are delivered to destinations specified here.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataset.DatasetContentDeliveryRuleProperty"]]]], jsii.get(self, "contentDeliveryRules"))

    @content_delivery_rules.setter
    def content_delivery_rules(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataset.DatasetContentDeliveryRuleProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1191be1b889318deb878087580e18a33f2b1eb69287f1988f9589d01097e71d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentDeliveryRules", value)

    @builtins.property
    @jsii.member(jsii_name="datasetName")
    def dataset_name(self) -> typing.Optional[builtins.str]:
        '''The name of the dataset.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetName"))

    @dataset_name.setter
    def dataset_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e08086740a66aa7f8dc6e47ec6c22172a3100d1ca2502cf801db5c180d0a6d13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetName", value)

    @builtins.property
    @jsii.member(jsii_name="lateDataRules")
    def late_data_rules(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataset.LateDataRuleProperty"]]]]:
        '''A list of data rules that send notifications to CloudWatch, when data arrives late.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataset.LateDataRuleProperty"]]]], jsii.get(self, "lateDataRules"))

    @late_data_rules.setter
    def late_data_rules(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataset.LateDataRuleProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bc1deb3c6d08c1c1ca7ffa721da938a0b604bf7e64fde45dd87c4e7478ce691)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lateDataRules", value)

    @builtins.property
    @jsii.member(jsii_name="retentionPeriod")
    def retention_period(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.RetentionPeriodProperty"]]:
        '''Optional.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.RetentionPeriodProperty"]], jsii.get(self, "retentionPeriod"))

    @retention_period.setter
    def retention_period(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.RetentionPeriodProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36003a82d5901d6085a6056449c0d0dae73bc495f138ce413f2a3940ca19669c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata which can be used to manage the data set.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__201d27101e415eb7f1fb30604fdbd5f5dab782974340b049d78678175f90e844)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="triggers")
    def triggers(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataset.TriggerProperty"]]]]:
        '''The ``DatasetTrigger`` objects that specify when the dataset is automatically updated.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataset.TriggerProperty"]]]], jsii.get(self, "triggers"))

    @triggers.setter
    def triggers(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataset.TriggerProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db66da5cbfc6b7c7e9db0e44713028b1f68bef47ecead6ba507500a1bc85c1d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggers", value)

    @builtins.property
    @jsii.member(jsii_name="versioningConfiguration")
    def versioning_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.VersioningConfigurationProperty"]]:
        '''Optional.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.VersioningConfigurationProperty"]], jsii.get(self, "versioningConfiguration"))

    @versioning_configuration.setter
    def versioning_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.VersioningConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1446f217595acd6056460044992a066513ba69220f2ecb77d8dc7122679ac975)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versioningConfiguration", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDataset.ActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action_name": "actionName",
            "container_action": "containerAction",
            "query_action": "queryAction",
        },
    )
    class ActionProperty:
        def __init__(
            self,
            *,
            action_name: builtins.str,
            container_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.ContainerActionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            query_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.QueryActionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Information needed to run the "containerAction" to produce data set contents.

            :param action_name: The name of the data set action by which data set contents are automatically created.
            :param container_action: Information which allows the system to run a containerized application in order to create the data set contents. The application must be in a Docker container along with any needed support libraries.
            :param query_action: An "SqlQueryDatasetAction" object that uses an SQL query to automatically create data set contents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                action_property = iotanalytics.CfnDataset.ActionProperty(
                    action_name="actionName",
                
                    # the properties below are optional
                    container_action=iotanalytics.CfnDataset.ContainerActionProperty(
                        execution_role_arn="executionRoleArn",
                        image="image",
                        resource_configuration=iotanalytics.CfnDataset.ResourceConfigurationProperty(
                            compute_type="computeType",
                            volume_size_in_gb=123
                        ),
                
                        # the properties below are optional
                        variables=[iotanalytics.CfnDataset.VariableProperty(
                            variable_name="variableName",
                
                            # the properties below are optional
                            dataset_content_version_value=iotanalytics.CfnDataset.DatasetContentVersionValueProperty(
                                dataset_name="datasetName"
                            ),
                            double_value=123,
                            output_file_uri_value=iotanalytics.CfnDataset.OutputFileUriValueProperty(
                                file_name="fileName"
                            ),
                            string_value="stringValue"
                        )]
                    ),
                    query_action=iotanalytics.CfnDataset.QueryActionProperty(
                        sql_query="sqlQuery",
                
                        # the properties below are optional
                        filters=[iotanalytics.CfnDataset.FilterProperty(
                            delta_time=iotanalytics.CfnDataset.DeltaTimeProperty(
                                offset_seconds=123,
                                time_expression="timeExpression"
                            )
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a3c3351641f2ce5cf26f289df6ae1a9b894c17bc061f16ff20ea18c0dab7ba8a)
                check_type(argname="argument action_name", value=action_name, expected_type=type_hints["action_name"])
                check_type(argname="argument container_action", value=container_action, expected_type=type_hints["container_action"])
                check_type(argname="argument query_action", value=query_action, expected_type=type_hints["query_action"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action_name": action_name,
            }
            if container_action is not None:
                self._values["container_action"] = container_action
            if query_action is not None:
                self._values["query_action"] = query_action

        @builtins.property
        def action_name(self) -> builtins.str:
            '''The name of the data set action by which data set contents are automatically created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-action.html#cfn-iotanalytics-dataset-action-actionname
            '''
            result = self._values.get("action_name")
            assert result is not None, "Required property 'action_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def container_action(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.ContainerActionProperty"]]:
            '''Information which allows the system to run a containerized application in order to create the data set contents.

            The application must be in a Docker container along with any needed support libraries.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-action.html#cfn-iotanalytics-dataset-action-containeraction
            '''
            result = self._values.get("container_action")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.ContainerActionProperty"]], result)

        @builtins.property
        def query_action(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.QueryActionProperty"]]:
            '''An "SqlQueryDatasetAction" object that uses an SQL query to automatically create data set contents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-action.html#cfn-iotanalytics-dataset-action-queryaction
            '''
            result = self._values.get("query_action")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.QueryActionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDataset.ContainerActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "execution_role_arn": "executionRoleArn",
            "image": "image",
            "resource_configuration": "resourceConfiguration",
            "variables": "variables",
        },
    )
    class ContainerActionProperty:
        def __init__(
            self,
            *,
            execution_role_arn: builtins.str,
            image: builtins.str,
            resource_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.ResourceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.VariableProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Information needed to run the "containerAction" to produce data set contents.

            :param execution_role_arn: The ARN of the role which gives permission to the system to access needed resources in order to run the "containerAction". This includes, at minimum, permission to retrieve the data set contents which are the input to the containerized application.
            :param image: The ARN of the Docker container stored in your account. The Docker container contains an application and needed support libraries and is used to generate data set contents.
            :param resource_configuration: Configuration of the resource which executes the "containerAction".
            :param variables: The values of variables used within the context of the execution of the containerized application (basically, parameters passed to the application). Each variable must have a name and a value given by one of "stringValue", "datasetContentVersionValue", or "outputFileUriValue".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-containeraction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                container_action_property = iotanalytics.CfnDataset.ContainerActionProperty(
                    execution_role_arn="executionRoleArn",
                    image="image",
                    resource_configuration=iotanalytics.CfnDataset.ResourceConfigurationProperty(
                        compute_type="computeType",
                        volume_size_in_gb=123
                    ),
                
                    # the properties below are optional
                    variables=[iotanalytics.CfnDataset.VariableProperty(
                        variable_name="variableName",
                
                        # the properties below are optional
                        dataset_content_version_value=iotanalytics.CfnDataset.DatasetContentVersionValueProperty(
                            dataset_name="datasetName"
                        ),
                        double_value=123,
                        output_file_uri_value=iotanalytics.CfnDataset.OutputFileUriValueProperty(
                            file_name="fileName"
                        ),
                        string_value="stringValue"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6242d8a947c41a4804fe02dc984b064df367b06752dc26316c0ae4eca8f5075d)
                check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
                check_type(argname="argument image", value=image, expected_type=type_hints["image"])
                check_type(argname="argument resource_configuration", value=resource_configuration, expected_type=type_hints["resource_configuration"])
                check_type(argname="argument variables", value=variables, expected_type=type_hints["variables"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "execution_role_arn": execution_role_arn,
                "image": image,
                "resource_configuration": resource_configuration,
            }
            if variables is not None:
                self._values["variables"] = variables

        @builtins.property
        def execution_role_arn(self) -> builtins.str:
            '''The ARN of the role which gives permission to the system to access needed resources in order to run the "containerAction".

            This includes, at minimum, permission to retrieve the data set contents which are the input to the containerized application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-containeraction.html#cfn-iotanalytics-dataset-containeraction-executionrolearn
            '''
            result = self._values.get("execution_role_arn")
            assert result is not None, "Required property 'execution_role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def image(self) -> builtins.str:
            '''The ARN of the Docker container stored in your account.

            The Docker container contains an application and needed support libraries and is used to generate data set contents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-containeraction.html#cfn-iotanalytics-dataset-containeraction-image
            '''
            result = self._values.get("image")
            assert result is not None, "Required property 'image' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDataset.ResourceConfigurationProperty"]:
            '''Configuration of the resource which executes the "containerAction".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-containeraction.html#cfn-iotanalytics-dataset-containeraction-resourceconfiguration
            '''
            result = self._values.get("resource_configuration")
            assert result is not None, "Required property 'resource_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDataset.ResourceConfigurationProperty"], result)

        @builtins.property
        def variables(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataset.VariableProperty"]]]]:
            '''The values of variables used within the context of the execution of the containerized application (basically, parameters passed to the application).

            Each variable must have a name and a value given by one of "stringValue", "datasetContentVersionValue", or "outputFileUriValue".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-containeraction.html#cfn-iotanalytics-dataset-containeraction-variables
            '''
            result = self._values.get("variables")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataset.VariableProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDataset.DatasetContentDeliveryRuleDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "iot_events_destination_configuration": "iotEventsDestinationConfiguration",
            "s3_destination_configuration": "s3DestinationConfiguration",
        },
    )
    class DatasetContentDeliveryRuleDestinationProperty:
        def __init__(
            self,
            *,
            iot_events_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.IotEventsDestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.S3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The destination to which dataset contents are delivered.

            :param iot_events_destination_configuration: Configuration information for delivery of dataset contents to AWS IoT Events .
            :param s3_destination_configuration: Configuration information for delivery of dataset contents to Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentdeliveryruledestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                dataset_content_delivery_rule_destination_property = iotanalytics.CfnDataset.DatasetContentDeliveryRuleDestinationProperty(
                    iot_events_destination_configuration=iotanalytics.CfnDataset.IotEventsDestinationConfigurationProperty(
                        input_name="inputName",
                        role_arn="roleArn"
                    ),
                    s3_destination_configuration=iotanalytics.CfnDataset.S3DestinationConfigurationProperty(
                        bucket="bucket",
                        key="key",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        glue_configuration=iotanalytics.CfnDataset.GlueConfigurationProperty(
                            database_name="databaseName",
                            table_name="tableName"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5fa6d9df2b2748545080f3145accff6d8b456a3f97c1e9f9a1f20b39000073b3)
                check_type(argname="argument iot_events_destination_configuration", value=iot_events_destination_configuration, expected_type=type_hints["iot_events_destination_configuration"])
                check_type(argname="argument s3_destination_configuration", value=s3_destination_configuration, expected_type=type_hints["s3_destination_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if iot_events_destination_configuration is not None:
                self._values["iot_events_destination_configuration"] = iot_events_destination_configuration
            if s3_destination_configuration is not None:
                self._values["s3_destination_configuration"] = s3_destination_configuration

        @builtins.property
        def iot_events_destination_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.IotEventsDestinationConfigurationProperty"]]:
            '''Configuration information for delivery of dataset contents to AWS IoT Events .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentdeliveryruledestination.html#cfn-iotanalytics-dataset-datasetcontentdeliveryruledestination-ioteventsdestinationconfiguration
            '''
            result = self._values.get("iot_events_destination_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.IotEventsDestinationConfigurationProperty"]], result)

        @builtins.property
        def s3_destination_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.S3DestinationConfigurationProperty"]]:
            '''Configuration information for delivery of dataset contents to Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentdeliveryruledestination.html#cfn-iotanalytics-dataset-datasetcontentdeliveryruledestination-s3destinationconfiguration
            '''
            result = self._values.get("s3_destination_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.S3DestinationConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatasetContentDeliveryRuleDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDataset.DatasetContentDeliveryRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"destination": "destination", "entry_name": "entryName"},
    )
    class DatasetContentDeliveryRuleProperty:
        def __init__(
            self,
            *,
            destination: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.DatasetContentDeliveryRuleDestinationProperty", typing.Dict[builtins.str, typing.Any]]],
            entry_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''When dataset contents are created, they are delivered to destination specified here.

            :param destination: The destination to which dataset contents are delivered.
            :param entry_name: The name of the dataset content delivery rules entry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentdeliveryrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                dataset_content_delivery_rule_property = iotanalytics.CfnDataset.DatasetContentDeliveryRuleProperty(
                    destination=iotanalytics.CfnDataset.DatasetContentDeliveryRuleDestinationProperty(
                        iot_events_destination_configuration=iotanalytics.CfnDataset.IotEventsDestinationConfigurationProperty(
                            input_name="inputName",
                            role_arn="roleArn"
                        ),
                        s3_destination_configuration=iotanalytics.CfnDataset.S3DestinationConfigurationProperty(
                            bucket="bucket",
                            key="key",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            glue_configuration=iotanalytics.CfnDataset.GlueConfigurationProperty(
                                database_name="databaseName",
                                table_name="tableName"
                            )
                        )
                    ),
                
                    # the properties below are optional
                    entry_name="entryName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0f19bbb35f806c8e28f81b57dec9b64e4ce3204e27bd015c548f0bbba4ed1001)
                check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
                check_type(argname="argument entry_name", value=entry_name, expected_type=type_hints["entry_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination": destination,
            }
            if entry_name is not None:
                self._values["entry_name"] = entry_name

        @builtins.property
        def destination(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDataset.DatasetContentDeliveryRuleDestinationProperty"]:
            '''The destination to which dataset contents are delivered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentdeliveryrule.html#cfn-iotanalytics-dataset-datasetcontentdeliveryrule-destination
            '''
            result = self._values.get("destination")
            assert result is not None, "Required property 'destination' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDataset.DatasetContentDeliveryRuleDestinationProperty"], result)

        @builtins.property
        def entry_name(self) -> typing.Optional[builtins.str]:
            '''The name of the dataset content delivery rules entry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentdeliveryrule.html#cfn-iotanalytics-dataset-datasetcontentdeliveryrule-entryname
            '''
            result = self._values.get("entry_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatasetContentDeliveryRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDataset.DatasetContentVersionValueProperty",
        jsii_struct_bases=[],
        name_mapping={"dataset_name": "datasetName"},
    )
    class DatasetContentVersionValueProperty:
        def __init__(self, *, dataset_name: builtins.str) -> None:
            '''The dataset whose latest contents are used as input to the notebook or application.

            :param dataset_name: The name of the dataset whose latest contents are used as input to the notebook or application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentversionvalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                dataset_content_version_value_property = iotanalytics.CfnDataset.DatasetContentVersionValueProperty(
                    dataset_name="datasetName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9627e37a604313ddab69d513bf6df569a93f856ba451e38f6882334fb43968b8)
                check_type(argname="argument dataset_name", value=dataset_name, expected_type=type_hints["dataset_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "dataset_name": dataset_name,
            }

        @builtins.property
        def dataset_name(self) -> builtins.str:
            '''The name of the dataset whose latest contents are used as input to the notebook or application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-datasetcontentversionvalue.html#cfn-iotanalytics-dataset-datasetcontentversionvalue-datasetname
            '''
            result = self._values.get("dataset_name")
            assert result is not None, "Required property 'dataset_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatasetContentVersionValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDataset.DeltaTimeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "offset_seconds": "offsetSeconds",
            "time_expression": "timeExpression",
        },
    )
    class DeltaTimeProperty:
        def __init__(
            self,
            *,
            offset_seconds: jsii.Number,
            time_expression: builtins.str,
        ) -> None:
            '''Used to limit data to that which has arrived since the last execution of the action.

            :param offset_seconds: The number of seconds of estimated in-flight lag time of message data. When you create dataset contents using message data from a specified timeframe, some message data might still be in flight when processing begins, and so do not arrive in time to be processed. Use this field to make allowances for the in flight time of your message data, so that data not processed from a previous timeframe is included with the next timeframe. Otherwise, missed message data would be excluded from processing during the next timeframe too, because its timestamp places it within the previous timeframe.
            :param time_expression: An expression by which the time of the message data might be determined. This can be the name of a timestamp field or a SQL expression that is used to derive the time the message data was generated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-deltatime.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                delta_time_property = iotanalytics.CfnDataset.DeltaTimeProperty(
                    offset_seconds=123,
                    time_expression="timeExpression"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__be02cd80d95071c31b45ce101d8562e196ddc6e85436afb5709305d83e344d41)
                check_type(argname="argument offset_seconds", value=offset_seconds, expected_type=type_hints["offset_seconds"])
                check_type(argname="argument time_expression", value=time_expression, expected_type=type_hints["time_expression"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "offset_seconds": offset_seconds,
                "time_expression": time_expression,
            }

        @builtins.property
        def offset_seconds(self) -> jsii.Number:
            '''The number of seconds of estimated in-flight lag time of message data.

            When you create dataset contents using message data from a specified timeframe, some message data might still be in flight when processing begins, and so do not arrive in time to be processed. Use this field to make allowances for the in flight time of your message data, so that data not processed from a previous timeframe is included with the next timeframe. Otherwise, missed message data would be excluded from processing during the next timeframe too, because its timestamp places it within the previous timeframe.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-deltatime.html#cfn-iotanalytics-dataset-deltatime-offsetseconds
            '''
            result = self._values.get("offset_seconds")
            assert result is not None, "Required property 'offset_seconds' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def time_expression(self) -> builtins.str:
            '''An expression by which the time of the message data might be determined.

            This can be the name of a timestamp field or a SQL expression that is used to derive the time the message data was generated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-deltatime.html#cfn-iotanalytics-dataset-deltatime-timeexpression
            '''
            result = self._values.get("time_expression")
            assert result is not None, "Required property 'time_expression' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeltaTimeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDataset.DeltaTimeSessionWindowConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"timeout_in_minutes": "timeoutInMinutes"},
    )
    class DeltaTimeSessionWindowConfigurationProperty:
        def __init__(self, *, timeout_in_minutes: jsii.Number) -> None:
            '''A structure that contains the configuration information of a delta time session window.

            ```DeltaTime`` <https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_DeltaTime.html>`_ specifies a time interval. You can use ``DeltaTime`` to create dataset contents with data that has arrived in the data store since the last execution. For an example of ``DeltaTime`` , see `Creating a SQL dataset with a delta window (CLI) <https://docs.aws.amazon.com/iotanalytics/latest/userguide/automate-create-dataset.html#automate-example6>`_ in the *AWS IoT Analytics User Guide* .

            :param timeout_in_minutes: A time interval. You can use ``timeoutInMinutes`` so that AWS IoT Analytics can batch up late data notifications that have been generated since the last execution. AWS IoT Analytics sends one batch of notifications to Amazon CloudWatch Events at one time. For more information about how to write a timestamp expression, see `Date and Time Functions and Operators <https://docs.aws.amazon.com/https://prestodb.io/docs/current/functions/datetime.html>`_ , in the *Presto 0.172 Documentation* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-deltatimesessionwindowconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                delta_time_session_window_configuration_property = iotanalytics.CfnDataset.DeltaTimeSessionWindowConfigurationProperty(
                    timeout_in_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__eb8e8f18aa3ead62f5ae202a1709d61bdf2b12ef7326a6cf4ff2263f0a7eff1a)
                check_type(argname="argument timeout_in_minutes", value=timeout_in_minutes, expected_type=type_hints["timeout_in_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "timeout_in_minutes": timeout_in_minutes,
            }

        @builtins.property
        def timeout_in_minutes(self) -> jsii.Number:
            '''A time interval.

            You can use ``timeoutInMinutes`` so that AWS IoT Analytics can batch up late data notifications that have been generated since the last execution. AWS IoT Analytics sends one batch of notifications to Amazon CloudWatch Events at one time.

            For more information about how to write a timestamp expression, see `Date and Time Functions and Operators <https://docs.aws.amazon.com/https://prestodb.io/docs/current/functions/datetime.html>`_ , in the *Presto 0.172 Documentation* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-deltatimesessionwindowconfiguration.html#cfn-iotanalytics-dataset-deltatimesessionwindowconfiguration-timeoutinminutes
            '''
            result = self._values.get("timeout_in_minutes")
            assert result is not None, "Required property 'timeout_in_minutes' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeltaTimeSessionWindowConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDataset.FilterProperty",
        jsii_struct_bases=[],
        name_mapping={"delta_time": "deltaTime"},
    )
    class FilterProperty:
        def __init__(
            self,
            *,
            delta_time: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.DeltaTimeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Information which is used to filter message data, to segregate it according to the time frame in which it arrives.

            :param delta_time: Used to limit data to that which has arrived since the last execution of the action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-filter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                filter_property = iotanalytics.CfnDataset.FilterProperty(
                    delta_time=iotanalytics.CfnDataset.DeltaTimeProperty(
                        offset_seconds=123,
                        time_expression="timeExpression"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bfd8c6d60abf268a0c3bab812403ca3b57768d51d4c8d5e8797b17c47d006a0a)
                check_type(argname="argument delta_time", value=delta_time, expected_type=type_hints["delta_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if delta_time is not None:
                self._values["delta_time"] = delta_time

        @builtins.property
        def delta_time(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.DeltaTimeProperty"]]:
            '''Used to limit data to that which has arrived since the last execution of the action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-filter.html#cfn-iotanalytics-dataset-filter-deltatime
            '''
            result = self._values.get("delta_time")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.DeltaTimeProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDataset.GlueConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"database_name": "databaseName", "table_name": "tableName"},
    )
    class GlueConfigurationProperty:
        def __init__(
            self,
            *,
            database_name: builtins.str,
            table_name: builtins.str,
        ) -> None:
            '''Configuration information for coordination with AWS Glue , a fully managed extract, transform and load (ETL) service.

            :param database_name: The name of the database in your AWS Glue Data Catalog in which the table is located. An AWS Glue Data Catalog database contains metadata tables.
            :param table_name: The name of the table in your AWS Glue Data Catalog that is used to perform the ETL operations. An AWS Glue Data Catalog table contains partitioned data and descriptions of data sources and targets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-glueconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                glue_configuration_property = iotanalytics.CfnDataset.GlueConfigurationProperty(
                    database_name="databaseName",
                    table_name="tableName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__66cdd212b38725bdb16f7222a75d297d4b793a295ab37b2fc13715220449280c)
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "database_name": database_name,
                "table_name": table_name,
            }

        @builtins.property
        def database_name(self) -> builtins.str:
            '''The name of the database in your AWS Glue Data Catalog in which the table is located.

            An AWS Glue Data Catalog database contains metadata tables.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-glueconfiguration.html#cfn-iotanalytics-dataset-glueconfiguration-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''The name of the table in your AWS Glue Data Catalog that is used to perform the ETL operations.

            An AWS Glue Data Catalog table contains partitioned data and descriptions of data sources and targets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-glueconfiguration.html#cfn-iotanalytics-dataset-glueconfiguration-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GlueConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDataset.IotEventsDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"input_name": "inputName", "role_arn": "roleArn"},
    )
    class IotEventsDestinationConfigurationProperty:
        def __init__(self, *, input_name: builtins.str, role_arn: builtins.str) -> None:
            '''Configuration information for delivery of dataset contents to AWS IoT Events .

            :param input_name: The name of the AWS IoT Events input to which dataset contents are delivered.
            :param role_arn: The ARN of the role that grants AWS IoT Analytics permission to deliver dataset contents to an AWS IoT Events input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-ioteventsdestinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                iot_events_destination_configuration_property = iotanalytics.CfnDataset.IotEventsDestinationConfigurationProperty(
                    input_name="inputName",
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__846e71e501ac1e6310b413155464156cb586e0fd915c8ac73e9992c0c401c16a)
                check_type(argname="argument input_name", value=input_name, expected_type=type_hints["input_name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "input_name": input_name,
                "role_arn": role_arn,
            }

        @builtins.property
        def input_name(self) -> builtins.str:
            '''The name of the AWS IoT Events input to which dataset contents are delivered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-ioteventsdestinationconfiguration.html#cfn-iotanalytics-dataset-ioteventsdestinationconfiguration-inputname
            '''
            result = self._values.get("input_name")
            assert result is not None, "Required property 'input_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the role that grants AWS IoT Analytics permission to deliver dataset contents to an AWS IoT Events input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-ioteventsdestinationconfiguration.html#cfn-iotanalytics-dataset-ioteventsdestinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IotEventsDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDataset.LateDataRuleConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delta_time_session_window_configuration": "deltaTimeSessionWindowConfiguration",
        },
    )
    class LateDataRuleConfigurationProperty:
        def __init__(
            self,
            *,
            delta_time_session_window_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.DeltaTimeSessionWindowConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The information needed to configure a delta time session window.

            :param delta_time_session_window_configuration: The information needed to configure a delta time session window.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-latedataruleconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                late_data_rule_configuration_property = iotanalytics.CfnDataset.LateDataRuleConfigurationProperty(
                    delta_time_session_window_configuration=iotanalytics.CfnDataset.DeltaTimeSessionWindowConfigurationProperty(
                        timeout_in_minutes=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ea0a5734ae5d70864971efc665d2a95b42f5f7fb3ccc748bd86497539309ed35)
                check_type(argname="argument delta_time_session_window_configuration", value=delta_time_session_window_configuration, expected_type=type_hints["delta_time_session_window_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if delta_time_session_window_configuration is not None:
                self._values["delta_time_session_window_configuration"] = delta_time_session_window_configuration

        @builtins.property
        def delta_time_session_window_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.DeltaTimeSessionWindowConfigurationProperty"]]:
            '''The information needed to configure a delta time session window.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-latedataruleconfiguration.html#cfn-iotanalytics-dataset-latedataruleconfiguration-deltatimesessionwindowconfiguration
            '''
            result = self._values.get("delta_time_session_window_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.DeltaTimeSessionWindowConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LateDataRuleConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDataset.LateDataRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "rule_configuration": "ruleConfiguration",
            "rule_name": "ruleName",
        },
    )
    class LateDataRuleProperty:
        def __init__(
            self,
            *,
            rule_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.LateDataRuleConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            rule_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure that contains the name and configuration information of a late data rule.

            :param rule_configuration: The information needed to configure the late data rule.
            :param rule_name: The name of the late data rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-latedatarule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                late_data_rule_property = iotanalytics.CfnDataset.LateDataRuleProperty(
                    rule_configuration=iotanalytics.CfnDataset.LateDataRuleConfigurationProperty(
                        delta_time_session_window_configuration=iotanalytics.CfnDataset.DeltaTimeSessionWindowConfigurationProperty(
                            timeout_in_minutes=123
                        )
                    ),
                
                    # the properties below are optional
                    rule_name="ruleName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6fa8dab9d3a3aa7ec10a97f6790a0d96684a968619f309c9c509577e2d399f1e)
                check_type(argname="argument rule_configuration", value=rule_configuration, expected_type=type_hints["rule_configuration"])
                check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "rule_configuration": rule_configuration,
            }
            if rule_name is not None:
                self._values["rule_name"] = rule_name

        @builtins.property
        def rule_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDataset.LateDataRuleConfigurationProperty"]:
            '''The information needed to configure the late data rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-latedatarule.html#cfn-iotanalytics-dataset-latedatarule-ruleconfiguration
            '''
            result = self._values.get("rule_configuration")
            assert result is not None, "Required property 'rule_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDataset.LateDataRuleConfigurationProperty"], result)

        @builtins.property
        def rule_name(self) -> typing.Optional[builtins.str]:
            '''The name of the late data rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-latedatarule.html#cfn-iotanalytics-dataset-latedatarule-rulename
            '''
            result = self._values.get("rule_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LateDataRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDataset.OutputFileUriValueProperty",
        jsii_struct_bases=[],
        name_mapping={"file_name": "fileName"},
    )
    class OutputFileUriValueProperty:
        def __init__(self, *, file_name: builtins.str) -> None:
            '''The value of the variable as a structure that specifies an output file URI.

            :param file_name: The URI of the location where dataset contents are stored, usually the URI of a file in an S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-outputfileurivalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                output_file_uri_value_property = iotanalytics.CfnDataset.OutputFileUriValueProperty(
                    file_name="fileName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__40ca34490c1eeedddc3e02770d487e08b263b4c1b33b1e11d3bff8beed84028f)
                check_type(argname="argument file_name", value=file_name, expected_type=type_hints["file_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "file_name": file_name,
            }

        @builtins.property
        def file_name(self) -> builtins.str:
            '''The URI of the location where dataset contents are stored, usually the URI of a file in an S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-outputfileurivalue.html#cfn-iotanalytics-dataset-outputfileurivalue-filename
            '''
            result = self._values.get("file_name")
            assert result is not None, "Required property 'file_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputFileUriValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDataset.QueryActionProperty",
        jsii_struct_bases=[],
        name_mapping={"sql_query": "sqlQuery", "filters": "filters"},
    )
    class QueryActionProperty:
        def __init__(
            self,
            *,
            sql_query: builtins.str,
            filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.FilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''An "SqlQueryDatasetAction" object that uses an SQL query to automatically create data set contents.

            :param sql_query: An "SqlQueryDatasetAction" object that uses an SQL query to automatically create data set contents.
            :param filters: Pre-filters applied to message data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-queryaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                query_action_property = iotanalytics.CfnDataset.QueryActionProperty(
                    sql_query="sqlQuery",
                
                    # the properties below are optional
                    filters=[iotanalytics.CfnDataset.FilterProperty(
                        delta_time=iotanalytics.CfnDataset.DeltaTimeProperty(
                            offset_seconds=123,
                            time_expression="timeExpression"
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__de5c5b0c96d44386f201894780b99dc31af0d8ffa106e6450f8d677406e216a6)
                check_type(argname="argument sql_query", value=sql_query, expected_type=type_hints["sql_query"])
                check_type(argname="argument filters", value=filters, expected_type=type_hints["filters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "sql_query": sql_query,
            }
            if filters is not None:
                self._values["filters"] = filters

        @builtins.property
        def sql_query(self) -> builtins.str:
            '''An "SqlQueryDatasetAction" object that uses an SQL query to automatically create data set contents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-queryaction.html#cfn-iotanalytics-dataset-queryaction-sqlquery
            '''
            result = self._values.get("sql_query")
            assert result is not None, "Required property 'sql_query' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def filters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataset.FilterProperty"]]]]:
            '''Pre-filters applied to message data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-queryaction.html#cfn-iotanalytics-dataset-queryaction-filters
            '''
            result = self._values.get("filters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataset.FilterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QueryActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDataset.ResourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "compute_type": "computeType",
            "volume_size_in_gb": "volumeSizeInGb",
        },
    )
    class ResourceConfigurationProperty:
        def __init__(
            self,
            *,
            compute_type: builtins.str,
            volume_size_in_gb: jsii.Number,
        ) -> None:
            '''The configuration of the resource used to execute the ``containerAction`` .

            :param compute_type: The type of the compute resource used to execute the ``containerAction`` . Possible values are: ``ACU_1`` (vCPU=4, memory=16 GiB) or ``ACU_2`` (vCPU=8, memory=32 GiB).
            :param volume_size_in_gb: The size, in GB, of the persistent storage available to the resource instance used to execute the ``containerAction`` (min: 1, max: 50).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-resourceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                resource_configuration_property = iotanalytics.CfnDataset.ResourceConfigurationProperty(
                    compute_type="computeType",
                    volume_size_in_gb=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4caca4363dbddfd7d8d63d5ed7437e9806b6f864fd4ce7d7a3d9ae4d12c2026c)
                check_type(argname="argument compute_type", value=compute_type, expected_type=type_hints["compute_type"])
                check_type(argname="argument volume_size_in_gb", value=volume_size_in_gb, expected_type=type_hints["volume_size_in_gb"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "compute_type": compute_type,
                "volume_size_in_gb": volume_size_in_gb,
            }

        @builtins.property
        def compute_type(self) -> builtins.str:
            '''The type of the compute resource used to execute the ``containerAction`` .

            Possible values are: ``ACU_1`` (vCPU=4, memory=16 GiB) or ``ACU_2`` (vCPU=8, memory=32 GiB).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-resourceconfiguration.html#cfn-iotanalytics-dataset-resourceconfiguration-computetype
            '''
            result = self._values.get("compute_type")
            assert result is not None, "Required property 'compute_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def volume_size_in_gb(self) -> jsii.Number:
            '''The size, in GB, of the persistent storage available to the resource instance used to execute the ``containerAction`` (min: 1, max: 50).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-resourceconfiguration.html#cfn-iotanalytics-dataset-resourceconfiguration-volumesizeingb
            '''
            result = self._values.get("volume_size_in_gb")
            assert result is not None, "Required property 'volume_size_in_gb' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDataset.RetentionPeriodProperty",
        jsii_struct_bases=[],
        name_mapping={"number_of_days": "numberOfDays", "unlimited": "unlimited"},
    )
    class RetentionPeriodProperty:
        def __init__(
            self,
            *,
            number_of_days: typing.Optional[jsii.Number] = None,
            unlimited: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''How long, in days, message data is kept.

            :param number_of_days: The number of days that message data is kept. The ``unlimited`` parameter must be false.
            :param unlimited: If true, message data is kept indefinitely.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-retentionperiod.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                retention_period_property = iotanalytics.CfnDataset.RetentionPeriodProperty(
                    number_of_days=123,
                    unlimited=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f25a34ec948131db017888ecc72a87f38ca9edc34e4f905c095fe6219d526f82)
                check_type(argname="argument number_of_days", value=number_of_days, expected_type=type_hints["number_of_days"])
                check_type(argname="argument unlimited", value=unlimited, expected_type=type_hints["unlimited"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if number_of_days is not None:
                self._values["number_of_days"] = number_of_days
            if unlimited is not None:
                self._values["unlimited"] = unlimited

        @builtins.property
        def number_of_days(self) -> typing.Optional[jsii.Number]:
            '''The number of days that message data is kept.

            The ``unlimited`` parameter must be false.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-retentionperiod.html#cfn-iotanalytics-dataset-retentionperiod-numberofdays
            '''
            result = self._values.get("number_of_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def unlimited(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If true, message data is kept indefinitely.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-retentionperiod.html#cfn-iotanalytics-dataset-retentionperiod-unlimited
            '''
            result = self._values.get("unlimited")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RetentionPeriodProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDataset.S3DestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket": "bucket",
            "key": "key",
            "role_arn": "roleArn",
            "glue_configuration": "glueConfiguration",
        },
    )
    class S3DestinationConfigurationProperty:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            key: builtins.str,
            role_arn: builtins.str,
            glue_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.GlueConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration information for delivery of dataset contents to Amazon Simple Storage Service (Amazon S3).

            :param bucket: The name of the S3 bucket to which dataset contents are delivered.
            :param key: The key of the dataset contents object in an S3 bucket. Each object has a key that is a unique identifier. Each object has exactly one key. You can create a unique key with the following options: - Use ``!{iotanalytics:scheduleTime}`` to insert the time of a scheduled SQL query run. - Use ``!{iotanalytics:versionId}`` to insert a unique hash that identifies a dataset content. - Use ``!{iotanalytics:creationTime}`` to insert the creation time of a dataset content. The following example creates a unique key for a CSV file: ``dataset/mydataset/!{iotanalytics:scheduleTime}/!{iotanalytics:versionId}.csv`` .. epigraph:: If you don't use ``!{iotanalytics:versionId}`` to specify the key, you might get duplicate keys. For example, you might have two dataset contents with the same ``scheduleTime`` but different ``versionId`` s. This means that one dataset content overwrites the other.
            :param role_arn: The ARN of the role that grants AWS IoT Analytics permission to interact with your Amazon S3 and AWS Glue resources.
            :param glue_configuration: Configuration information for coordination with AWS Glue , a fully managed extract, transform and load (ETL) service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-s3destinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                s3_destination_configuration_property = iotanalytics.CfnDataset.S3DestinationConfigurationProperty(
                    bucket="bucket",
                    key="key",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    glue_configuration=iotanalytics.CfnDataset.GlueConfigurationProperty(
                        database_name="databaseName",
                        table_name="tableName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__42695c1832b8cae8c36043ce30de17800b72e233c2b6e6377d8eb3deede70de3)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument glue_configuration", value=glue_configuration, expected_type=type_hints["glue_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "key": key,
                "role_arn": role_arn,
            }
            if glue_configuration is not None:
                self._values["glue_configuration"] = glue_configuration

        @builtins.property
        def bucket(self) -> builtins.str:
            '''The name of the S3 bucket to which dataset contents are delivered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-s3destinationconfiguration.html#cfn-iotanalytics-dataset-s3destinationconfiguration-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''The key of the dataset contents object in an S3 bucket.

            Each object has a key that is a unique identifier. Each object has exactly one key.

            You can create a unique key with the following options:

            - Use ``!{iotanalytics:scheduleTime}`` to insert the time of a scheduled SQL query run.
            - Use ``!{iotanalytics:versionId}`` to insert a unique hash that identifies a dataset content.
            - Use ``!{iotanalytics:creationTime}`` to insert the creation time of a dataset content.

            The following example creates a unique key for a CSV file: ``dataset/mydataset/!{iotanalytics:scheduleTime}/!{iotanalytics:versionId}.csv``
            .. epigraph::

               If you don't use ``!{iotanalytics:versionId}`` to specify the key, you might get duplicate keys. For example, you might have two dataset contents with the same ``scheduleTime`` but different ``versionId`` s. This means that one dataset content overwrites the other.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-s3destinationconfiguration.html#cfn-iotanalytics-dataset-s3destinationconfiguration-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the role that grants AWS IoT Analytics permission to interact with your Amazon S3 and AWS Glue resources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-s3destinationconfiguration.html#cfn-iotanalytics-dataset-s3destinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def glue_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.GlueConfigurationProperty"]]:
            '''Configuration information for coordination with AWS Glue , a fully managed extract, transform and load (ETL) service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-s3destinationconfiguration.html#cfn-iotanalytics-dataset-s3destinationconfiguration-glueconfiguration
            '''
            result = self._values.get("glue_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.GlueConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3DestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDataset.ScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={"schedule_expression": "scheduleExpression"},
    )
    class ScheduleProperty:
        def __init__(self, *, schedule_expression: builtins.str) -> None:
            '''The schedule for when to trigger an update.

            :param schedule_expression: The expression that defines when to trigger an update. For more information, see `Schedule Expressions for Rules <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`_ in the Amazon CloudWatch documentation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-schedule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                schedule_property = iotanalytics.CfnDataset.ScheduleProperty(
                    schedule_expression="scheduleExpression"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6e00f7c2fafca878429e43d7ef3e7f43c6570a720c615402abbda3393f274b96)
                check_type(argname="argument schedule_expression", value=schedule_expression, expected_type=type_hints["schedule_expression"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "schedule_expression": schedule_expression,
            }

        @builtins.property
        def schedule_expression(self) -> builtins.str:
            '''The expression that defines when to trigger an update.

            For more information, see `Schedule Expressions for Rules <https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html>`_ in the Amazon CloudWatch documentation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-schedule.html#cfn-iotanalytics-dataset-schedule-scheduleexpression
            '''
            result = self._values.get("schedule_expression")
            assert result is not None, "Required property 'schedule_expression' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDataset.TriggerProperty",
        jsii_struct_bases=[],
        name_mapping={
            "schedule": "schedule",
            "triggering_dataset": "triggeringDataset",
        },
    )
    class TriggerProperty:
        def __init__(
            self,
            *,
            schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.ScheduleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            triggering_dataset: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.TriggeringDatasetProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The "DatasetTrigger" that specifies when the data set is automatically updated.

            :param schedule: The "Schedule" when the trigger is initiated.
            :param triggering_dataset: Information about the data set whose content generation triggers the new data set content generation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-trigger.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                trigger_property = iotanalytics.CfnDataset.TriggerProperty(
                    schedule=iotanalytics.CfnDataset.ScheduleProperty(
                        schedule_expression="scheduleExpression"
                    ),
                    triggering_dataset=iotanalytics.CfnDataset.TriggeringDatasetProperty(
                        dataset_name="datasetName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5f8d91baeba7735ed150f70716898211ad99b3281e2fb4199bfb4b2dede3f363)
                check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
                check_type(argname="argument triggering_dataset", value=triggering_dataset, expected_type=type_hints["triggering_dataset"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if schedule is not None:
                self._values["schedule"] = schedule
            if triggering_dataset is not None:
                self._values["triggering_dataset"] = triggering_dataset

        @builtins.property
        def schedule(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.ScheduleProperty"]]:
            '''The "Schedule" when the trigger is initiated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-trigger.html#cfn-iotanalytics-dataset-trigger-schedule
            '''
            result = self._values.get("schedule")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.ScheduleProperty"]], result)

        @builtins.property
        def triggering_dataset(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.TriggeringDatasetProperty"]]:
            '''Information about the data set whose content generation triggers the new data set content generation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-trigger.html#cfn-iotanalytics-dataset-trigger-triggeringdataset
            '''
            result = self._values.get("triggering_dataset")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.TriggeringDatasetProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TriggerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDataset.TriggeringDatasetProperty",
        jsii_struct_bases=[],
        name_mapping={"dataset_name": "datasetName"},
    )
    class TriggeringDatasetProperty:
        def __init__(self, *, dataset_name: builtins.str) -> None:
            '''Information about the dataset whose content generation triggers the new dataset content generation.

            :param dataset_name: The name of the data set whose content generation triggers the new data set content generation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-triggeringdataset.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                triggering_dataset_property = iotanalytics.CfnDataset.TriggeringDatasetProperty(
                    dataset_name="datasetName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5a822098e3c67a5eb69596bd59484a55a8e0ac97e0694746c6488c191c5e2eda)
                check_type(argname="argument dataset_name", value=dataset_name, expected_type=type_hints["dataset_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "dataset_name": dataset_name,
            }

        @builtins.property
        def dataset_name(self) -> builtins.str:
            '''The name of the data set whose content generation triggers the new data set content generation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-triggeringdataset.html#cfn-iotanalytics-dataset-triggeringdataset-datasetname
            '''
            result = self._values.get("dataset_name")
            assert result is not None, "Required property 'dataset_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TriggeringDatasetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDataset.VariableProperty",
        jsii_struct_bases=[],
        name_mapping={
            "variable_name": "variableName",
            "dataset_content_version_value": "datasetContentVersionValue",
            "double_value": "doubleValue",
            "output_file_uri_value": "outputFileUriValue",
            "string_value": "stringValue",
        },
    )
    class VariableProperty:
        def __init__(
            self,
            *,
            variable_name: builtins.str,
            dataset_content_version_value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.DatasetContentVersionValueProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            double_value: typing.Optional[jsii.Number] = None,
            output_file_uri_value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataset.OutputFileUriValueProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            string_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An instance of a variable to be passed to the ``containerAction`` execution.

            Each variable must have a name and a value given by one of ``stringValue`` , ``datasetContentVersionValue`` , or ``outputFileUriValue`` .

            :param variable_name: The name of the variable.
            :param dataset_content_version_value: The value of the variable as a structure that specifies a dataset content version.
            :param double_value: The value of the variable as a double (numeric).
            :param output_file_uri_value: The value of the variable as a structure that specifies an output file URI.
            :param string_value: The value of the variable as a string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                variable_property = iotanalytics.CfnDataset.VariableProperty(
                    variable_name="variableName",
                
                    # the properties below are optional
                    dataset_content_version_value=iotanalytics.CfnDataset.DatasetContentVersionValueProperty(
                        dataset_name="datasetName"
                    ),
                    double_value=123,
                    output_file_uri_value=iotanalytics.CfnDataset.OutputFileUriValueProperty(
                        file_name="fileName"
                    ),
                    string_value="stringValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2f442efcc6fc67ff4c6b32b902bffe3a1e716ab6fa19002d570fdd99768219b7)
                check_type(argname="argument variable_name", value=variable_name, expected_type=type_hints["variable_name"])
                check_type(argname="argument dataset_content_version_value", value=dataset_content_version_value, expected_type=type_hints["dataset_content_version_value"])
                check_type(argname="argument double_value", value=double_value, expected_type=type_hints["double_value"])
                check_type(argname="argument output_file_uri_value", value=output_file_uri_value, expected_type=type_hints["output_file_uri_value"])
                check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "variable_name": variable_name,
            }
            if dataset_content_version_value is not None:
                self._values["dataset_content_version_value"] = dataset_content_version_value
            if double_value is not None:
                self._values["double_value"] = double_value
            if output_file_uri_value is not None:
                self._values["output_file_uri_value"] = output_file_uri_value
            if string_value is not None:
                self._values["string_value"] = string_value

        @builtins.property
        def variable_name(self) -> builtins.str:
            '''The name of the variable.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable.html#cfn-iotanalytics-dataset-variable-variablename
            '''
            result = self._values.get("variable_name")
            assert result is not None, "Required property 'variable_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dataset_content_version_value(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.DatasetContentVersionValueProperty"]]:
            '''The value of the variable as a structure that specifies a dataset content version.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable.html#cfn-iotanalytics-dataset-variable-datasetcontentversionvalue
            '''
            result = self._values.get("dataset_content_version_value")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.DatasetContentVersionValueProperty"]], result)

        @builtins.property
        def double_value(self) -> typing.Optional[jsii.Number]:
            '''The value of the variable as a double (numeric).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable.html#cfn-iotanalytics-dataset-variable-doublevalue
            '''
            result = self._values.get("double_value")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def output_file_uri_value(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.OutputFileUriValueProperty"]]:
            '''The value of the variable as a structure that specifies an output file URI.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable.html#cfn-iotanalytics-dataset-variable-outputfileurivalue
            '''
            result = self._values.get("output_file_uri_value")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataset.OutputFileUriValueProperty"]], result)

        @builtins.property
        def string_value(self) -> typing.Optional[builtins.str]:
            '''The value of the variable as a string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-variable.html#cfn-iotanalytics-dataset-variable-stringvalue
            '''
            result = self._values.get("string_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VariableProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDataset.VersioningConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"max_versions": "maxVersions", "unlimited": "unlimited"},
    )
    class VersioningConfigurationProperty:
        def __init__(
            self,
            *,
            max_versions: typing.Optional[jsii.Number] = None,
            unlimited: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Information about the versioning of dataset contents.

            :param max_versions: How many versions of dataset contents are kept. The ``unlimited`` parameter must be ``false`` .
            :param unlimited: If true, unlimited versions of dataset contents are kept.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-versioningconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                versioning_configuration_property = iotanalytics.CfnDataset.VersioningConfigurationProperty(
                    max_versions=123,
                    unlimited=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__44ef2d0f147e3d91be95ed97931f9fe1fdbe66142e58213b3dda686e0a38729a)
                check_type(argname="argument max_versions", value=max_versions, expected_type=type_hints["max_versions"])
                check_type(argname="argument unlimited", value=unlimited, expected_type=type_hints["unlimited"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if max_versions is not None:
                self._values["max_versions"] = max_versions
            if unlimited is not None:
                self._values["unlimited"] = unlimited

        @builtins.property
        def max_versions(self) -> typing.Optional[jsii.Number]:
            '''How many versions of dataset contents are kept.

            The ``unlimited`` parameter must be ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-versioningconfiguration.html#cfn-iotanalytics-dataset-versioningconfiguration-maxversions
            '''
            result = self._values.get("max_versions")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def unlimited(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If true, unlimited versions of dataset contents are kept.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-dataset-versioningconfiguration.html#cfn-iotanalytics-dataset-versioningconfiguration-unlimited
            '''
            result = self._values.get("unlimited")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VersioningConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDatasetProps",
    jsii_struct_bases=[],
    name_mapping={
        "actions": "actions",
        "content_delivery_rules": "contentDeliveryRules",
        "dataset_name": "datasetName",
        "late_data_rules": "lateDataRules",
        "retention_period": "retentionPeriod",
        "tags": "tags",
        "triggers": "triggers",
        "versioning_configuration": "versioningConfiguration",
    },
)
class CfnDatasetProps:
    def __init__(
        self,
        *,
        actions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.ActionProperty, typing.Dict[builtins.str, typing.Any]]]]],
        content_delivery_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.DatasetContentDeliveryRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        dataset_name: typing.Optional[builtins.str] = None,
        late_data_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.LateDataRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        retention_period: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.RetentionPeriodProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        triggers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.TriggerProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        versioning_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.VersioningConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataset``.

        :param actions: The ``DatasetAction`` objects that automatically create the dataset contents.
        :param content_delivery_rules: When dataset contents are created they are delivered to destinations specified here.
        :param dataset_name: The name of the dataset.
        :param late_data_rules: A list of data rules that send notifications to CloudWatch, when data arrives late. To specify ``lateDataRules`` , the dataset must use a `DeltaTimer <https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_DeltaTime.html>`_ filter.
        :param retention_period: Optional. How long, in days, message data is kept for the dataset.
        :param tags: Metadata which can be used to manage the data set. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param triggers: The ``DatasetTrigger`` objects that specify when the dataset is automatically updated.
        :param versioning_configuration: Optional. How many versions of dataset contents are kept. If not specified or set to null, only the latest version plus the latest succeeded version (if they are different) are kept for the time period specified by the ``retentionPeriod`` parameter. For more information, see `Keeping Multiple Versions of AWS IoT Analytics datasets <https://docs.aws.amazon.com/iotanalytics/latest/userguide/getting-started.html#aws-iot-analytics-dataset-versions>`_ in the *AWS IoT Analytics User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotanalytics as iotanalytics
            
            cfn_dataset_props = iotanalytics.CfnDatasetProps(
                actions=[iotanalytics.CfnDataset.ActionProperty(
                    action_name="actionName",
            
                    # the properties below are optional
                    container_action=iotanalytics.CfnDataset.ContainerActionProperty(
                        execution_role_arn="executionRoleArn",
                        image="image",
                        resource_configuration=iotanalytics.CfnDataset.ResourceConfigurationProperty(
                            compute_type="computeType",
                            volume_size_in_gb=123
                        ),
            
                        # the properties below are optional
                        variables=[iotanalytics.CfnDataset.VariableProperty(
                            variable_name="variableName",
            
                            # the properties below are optional
                            dataset_content_version_value=iotanalytics.CfnDataset.DatasetContentVersionValueProperty(
                                dataset_name="datasetName"
                            ),
                            double_value=123,
                            output_file_uri_value=iotanalytics.CfnDataset.OutputFileUriValueProperty(
                                file_name="fileName"
                            ),
                            string_value="stringValue"
                        )]
                    ),
                    query_action=iotanalytics.CfnDataset.QueryActionProperty(
                        sql_query="sqlQuery",
            
                        # the properties below are optional
                        filters=[iotanalytics.CfnDataset.FilterProperty(
                            delta_time=iotanalytics.CfnDataset.DeltaTimeProperty(
                                offset_seconds=123,
                                time_expression="timeExpression"
                            )
                        )]
                    )
                )],
            
                # the properties below are optional
                content_delivery_rules=[iotanalytics.CfnDataset.DatasetContentDeliveryRuleProperty(
                    destination=iotanalytics.CfnDataset.DatasetContentDeliveryRuleDestinationProperty(
                        iot_events_destination_configuration=iotanalytics.CfnDataset.IotEventsDestinationConfigurationProperty(
                            input_name="inputName",
                            role_arn="roleArn"
                        ),
                        s3_destination_configuration=iotanalytics.CfnDataset.S3DestinationConfigurationProperty(
                            bucket="bucket",
                            key="key",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            glue_configuration=iotanalytics.CfnDataset.GlueConfigurationProperty(
                                database_name="databaseName",
                                table_name="tableName"
                            )
                        )
                    ),
            
                    # the properties below are optional
                    entry_name="entryName"
                )],
                dataset_name="datasetName",
                late_data_rules=[iotanalytics.CfnDataset.LateDataRuleProperty(
                    rule_configuration=iotanalytics.CfnDataset.LateDataRuleConfigurationProperty(
                        delta_time_session_window_configuration=iotanalytics.CfnDataset.DeltaTimeSessionWindowConfigurationProperty(
                            timeout_in_minutes=123
                        )
                    ),
            
                    # the properties below are optional
                    rule_name="ruleName"
                )],
                retention_period=iotanalytics.CfnDataset.RetentionPeriodProperty(
                    number_of_days=123,
                    unlimited=False
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                triggers=[iotanalytics.CfnDataset.TriggerProperty(
                    schedule=iotanalytics.CfnDataset.ScheduleProperty(
                        schedule_expression="scheduleExpression"
                    ),
                    triggering_dataset=iotanalytics.CfnDataset.TriggeringDatasetProperty(
                        dataset_name="datasetName"
                    )
                )],
                versioning_configuration=iotanalytics.CfnDataset.VersioningConfigurationProperty(
                    max_versions=123,
                    unlimited=False
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba482b4c89e3977548d923f68d372a4195ddedc9b62d05ec8d5000808561e994)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument content_delivery_rules", value=content_delivery_rules, expected_type=type_hints["content_delivery_rules"])
            check_type(argname="argument dataset_name", value=dataset_name, expected_type=type_hints["dataset_name"])
            check_type(argname="argument late_data_rules", value=late_data_rules, expected_type=type_hints["late_data_rules"])
            check_type(argname="argument retention_period", value=retention_period, expected_type=type_hints["retention_period"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument triggers", value=triggers, expected_type=type_hints["triggers"])
            check_type(argname="argument versioning_configuration", value=versioning_configuration, expected_type=type_hints["versioning_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "actions": actions,
        }
        if content_delivery_rules is not None:
            self._values["content_delivery_rules"] = content_delivery_rules
        if dataset_name is not None:
            self._values["dataset_name"] = dataset_name
        if late_data_rules is not None:
            self._values["late_data_rules"] = late_data_rules
        if retention_period is not None:
            self._values["retention_period"] = retention_period
        if tags is not None:
            self._values["tags"] = tags
        if triggers is not None:
            self._values["triggers"] = triggers
        if versioning_configuration is not None:
            self._values["versioning_configuration"] = versioning_configuration

    @builtins.property
    def actions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataset.ActionProperty]]]:
        '''The ``DatasetAction`` objects that automatically create the dataset contents.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-actions
        '''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataset.ActionProperty]]], result)

    @builtins.property
    def content_delivery_rules(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataset.DatasetContentDeliveryRuleProperty]]]]:
        '''When dataset contents are created they are delivered to destinations specified here.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-contentdeliveryrules
        '''
        result = self._values.get("content_delivery_rules")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataset.DatasetContentDeliveryRuleProperty]]]], result)

    @builtins.property
    def dataset_name(self) -> typing.Optional[builtins.str]:
        '''The name of the dataset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-datasetname
        '''
        result = self._values.get("dataset_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def late_data_rules(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataset.LateDataRuleProperty]]]]:
        '''A list of data rules that send notifications to CloudWatch, when data arrives late.

        To specify ``lateDataRules`` , the dataset must use a `DeltaTimer <https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_DeltaTime.html>`_ filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-latedatarules
        '''
        result = self._values.get("late_data_rules")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataset.LateDataRuleProperty]]]], result)

    @builtins.property
    def retention_period(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataset.RetentionPeriodProperty]]:
        '''Optional.

        How long, in days, message data is kept for the dataset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-retentionperiod
        '''
        result = self._values.get("retention_period")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataset.RetentionPeriodProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata which can be used to manage the data set.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def triggers(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataset.TriggerProperty]]]]:
        '''The ``DatasetTrigger`` objects that specify when the dataset is automatically updated.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-triggers
        '''
        result = self._values.get("triggers")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataset.TriggerProperty]]]], result)

    @builtins.property
    def versioning_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataset.VersioningConfigurationProperty]]:
        '''Optional.

        How many versions of dataset contents are kept. If not specified or set to null, only the latest version plus the latest succeeded version (if they are different) are kept for the time period specified by the ``retentionPeriod`` parameter. For more information, see `Keeping Multiple Versions of AWS IoT Analytics datasets <https://docs.aws.amazon.com/iotanalytics/latest/userguide/getting-started.html#aws-iot-analytics-dataset-versions>`_ in the *AWS IoT Analytics User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html#cfn-iotanalytics-dataset-versioningconfiguration
        '''
        result = self._values.get("versioning_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataset.VersioningConfigurationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDatasetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDatastore(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDatastore",
):
    '''AWS::IoTAnalytics::Datastore resource is a repository for messages.

    For more information, see `How to Use AWS IoT Analytics <https://docs.aws.amazon.com/iotanalytics/latest/userguide/welcome.html#aws-iot-analytics-how>`_ in the *AWS IoT Analytics User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html
    :cloudformationResource: AWS::IoTAnalytics::Datastore
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotanalytics as iotanalytics
        
        # json_configuration: Any
        # service_managed_s3: Any
        
        cfn_datastore = iotanalytics.CfnDatastore(self, "MyCfnDatastore",
            datastore_name="datastoreName",
            datastore_partitions=iotanalytics.CfnDatastore.DatastorePartitionsProperty(
                partitions=[iotanalytics.CfnDatastore.DatastorePartitionProperty(
                    partition=iotanalytics.CfnDatastore.PartitionProperty(
                        attribute_name="attributeName"
                    ),
                    timestamp_partition=iotanalytics.CfnDatastore.TimestampPartitionProperty(
                        attribute_name="attributeName",
        
                        # the properties below are optional
                        timestamp_format="timestampFormat"
                    )
                )]
            ),
            datastore_storage=iotanalytics.CfnDatastore.DatastoreStorageProperty(
                customer_managed_s3=iotanalytics.CfnDatastore.CustomerManagedS3Property(
                    bucket="bucket",
                    role_arn="roleArn",
        
                    # the properties below are optional
                    key_prefix="keyPrefix"
                ),
                iot_site_wise_multi_layer_storage=iotanalytics.CfnDatastore.IotSiteWiseMultiLayerStorageProperty(
                    customer_managed_s3_storage=iotanalytics.CfnDatastore.CustomerManagedS3StorageProperty(
                        bucket="bucket",
        
                        # the properties below are optional
                        key_prefix="keyPrefix"
                    )
                ),
                service_managed_s3=service_managed_s3
            ),
            file_format_configuration=iotanalytics.CfnDatastore.FileFormatConfigurationProperty(
                json_configuration=json_configuration,
                parquet_configuration=iotanalytics.CfnDatastore.ParquetConfigurationProperty(
                    schema_definition=iotanalytics.CfnDatastore.SchemaDefinitionProperty(
                        columns=[iotanalytics.CfnDatastore.ColumnProperty(
                            name="name",
                            type="type"
                        )]
                    )
                )
            ),
            retention_period=iotanalytics.CfnDatastore.RetentionPeriodProperty(
                number_of_days=123,
                unlimited=False
            ),
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
        datastore_name: typing.Optional[builtins.str] = None,
        datastore_partitions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDatastore.DatastorePartitionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        datastore_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDatastore.DatastoreStorageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        file_format_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDatastore.FileFormatConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        retention_period: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDatastore.RetentionPeriodProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param datastore_name: The name of the data store.
        :param datastore_partitions: Information about the partition dimensions in a data store.
        :param datastore_storage: Where data store data is stored.
        :param file_format_configuration: Contains the configuration information of file formats. AWS IoT Analytics data stores support JSON and `Parquet <https://docs.aws.amazon.com/https://parquet.apache.org/>`_ . The default file format is JSON. You can specify only one format. You can't change the file format after you create the data store.
        :param retention_period: How long, in days, message data is kept for the data store. When ``customerManagedS3`` storage is selected, this parameter is ignored.
        :param tags: Metadata which can be used to manage the data store. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80888194774a160a9eb52d698126a6fd1e7e99768082595c8f4810a89813f3c1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDatastoreProps(
            datastore_name=datastore_name,
            datastore_partitions=datastore_partitions,
            datastore_storage=datastore_storage,
            file_format_configuration=file_format_configuration,
            retention_period=retention_period,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ade56a7c5d6431a16dde38053efe2001ac1c8ab06985988a23a00267d80a5a16)
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
            type_hints = typing.get_type_hints(_typecheckingstub__94c0a67e5e4c43aa44435879b4f1b63ef3b5102e13736181e9448de1796ed206)
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
        '''
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
    @jsii.member(jsii_name="datastoreName")
    def datastore_name(self) -> typing.Optional[builtins.str]:
        '''The name of the data store.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datastoreName"))

    @datastore_name.setter
    def datastore_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__081a53e062ad7ea5c2f6ecb7ebbccac62478ecd868806928c47c7eb98ae61d0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datastoreName", value)

    @builtins.property
    @jsii.member(jsii_name="datastorePartitions")
    def datastore_partitions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.DatastorePartitionsProperty"]]:
        '''Information about the partition dimensions in a data store.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.DatastorePartitionsProperty"]], jsii.get(self, "datastorePartitions"))

    @datastore_partitions.setter
    def datastore_partitions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.DatastorePartitionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bcc26ed136adb3f4c32488bcb2844b209ec226cd795eb2c0cea62ded0053c40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datastorePartitions", value)

    @builtins.property
    @jsii.member(jsii_name="datastoreStorage")
    def datastore_storage(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.DatastoreStorageProperty"]]:
        '''Where data store data is stored.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.DatastoreStorageProperty"]], jsii.get(self, "datastoreStorage"))

    @datastore_storage.setter
    def datastore_storage(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.DatastoreStorageProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe446f198ffdaea0dc4c9d93e32d3c1aec9b88e8f422a0ce06659dba6598ae0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datastoreStorage", value)

    @builtins.property
    @jsii.member(jsii_name="fileFormatConfiguration")
    def file_format_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.FileFormatConfigurationProperty"]]:
        '''Contains the configuration information of file formats.

        AWS IoT Analytics data stores support JSON and `Parquet <https://docs.aws.amazon.com/https://parquet.apache.org/>`_ .
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.FileFormatConfigurationProperty"]], jsii.get(self, "fileFormatConfiguration"))

    @file_format_configuration.setter
    def file_format_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.FileFormatConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bc9a7886f31a213d5c1836b73e8f3e9697e0e07f52f23623adfd569fa72c125)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileFormatConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="retentionPeriod")
    def retention_period(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.RetentionPeriodProperty"]]:
        '''How long, in days, message data is kept for the data store.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.RetentionPeriodProperty"]], jsii.get(self, "retentionPeriod"))

    @retention_period.setter
    def retention_period(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.RetentionPeriodProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__032263fee34119301fc0a40c33438ae261f79f8664628d410d34905ede484924)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata which can be used to manage the data store.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09e62e46bc734f5ed26f36e04b2552fae780df1bd2f0edbb6b1492d2e5a21d03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDatastore.ColumnProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "type": "type"},
    )
    class ColumnProperty:
        def __init__(self, *, name: builtins.str, type: builtins.str) -> None:
            '''Contains information about a column that stores your data.

            :param name: The name of the column.
            :param type: The type of data. For more information about the supported data types, see `Common data types <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-common.html>`_ in the *AWS Glue Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-column.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                column_property = iotanalytics.CfnDatastore.ColumnProperty(
                    name="name",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6ae2b1794960971e3043a45488ed7248bf5111d4413a143e8d852de963f225b3)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "type": type,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the column.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-column.html#cfn-iotanalytics-datastore-column-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of data.

            For more information about the supported data types, see `Common data types <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-common.html>`_ in the *AWS Glue Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-column.html#cfn-iotanalytics-datastore-column-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ColumnProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDatastore.CustomerManagedS3Property",
        jsii_struct_bases=[],
        name_mapping={
            "bucket": "bucket",
            "role_arn": "roleArn",
            "key_prefix": "keyPrefix",
        },
    )
    class CustomerManagedS3Property:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            role_arn: builtins.str,
            key_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''S3-customer-managed;

            When you choose customer-managed storage, the ``retentionPeriod`` parameter is ignored. You can't change the choice of Amazon S3 storage after your data store is created.

            :param bucket: The name of the Amazon S3 bucket where your data is stored.
            :param role_arn: The ARN of the role that grants AWS IoT Analytics permission to interact with your Amazon S3 resources.
            :param key_prefix: (Optional) The prefix used to create the keys of the data store data objects. Each object in an Amazon S3 bucket has a key that is its unique identifier in the bucket. Each object in a bucket has exactly one key. The prefix must end with a forward slash (/).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                customer_managed_s3_property = iotanalytics.CfnDatastore.CustomerManagedS3Property(
                    bucket="bucket",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    key_prefix="keyPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f4068d1c6245c24c4ab2ad550651845d10e8e4ccaf674e9cd3b91ccf9fcb5405)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument key_prefix", value=key_prefix, expected_type=type_hints["key_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "role_arn": role_arn,
            }
            if key_prefix is not None:
                self._values["key_prefix"] = key_prefix

        @builtins.property
        def bucket(self) -> builtins.str:
            '''The name of the Amazon S3 bucket where your data is stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3.html#cfn-iotanalytics-datastore-customermanageds3-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the role that grants AWS IoT Analytics permission to interact with your Amazon S3 resources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3.html#cfn-iotanalytics-datastore-customermanageds3-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_prefix(self) -> typing.Optional[builtins.str]:
            '''(Optional) The prefix used to create the keys of the data store data objects.

            Each object in an Amazon S3 bucket has a key that is its unique identifier in the bucket. Each object in a bucket has exactly one key. The prefix must end with a forward slash (/).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3.html#cfn-iotanalytics-datastore-customermanageds3-keyprefix
            '''
            result = self._values.get("key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomerManagedS3Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDatastore.CustomerManagedS3StorageProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "key_prefix": "keyPrefix"},
    )
    class CustomerManagedS3StorageProperty:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            key_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Amazon S3 -customer-managed;

            When you choose customer-managed storage, the ``retentionPeriod`` parameter is ignored. You can't change the choice of Amazon S3 storage after your data store is created.

            :param bucket: The name of the Amazon S3 bucket where your data is stored.
            :param key_prefix: (Optional) The prefix used to create the keys of the data store data objects. Each object in an Amazon S3 bucket has a key that is its unique identifier in the bucket. Each object in a bucket has exactly one key. The prefix must end with a forward slash (/).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3storage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                customer_managed_s3_storage_property = iotanalytics.CfnDatastore.CustomerManagedS3StorageProperty(
                    bucket="bucket",
                
                    # the properties below are optional
                    key_prefix="keyPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__35524e38307a14aa06cb90fa741a954b5439d4d8f6f5e9f4f8d8ba9fe80348a6)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument key_prefix", value=key_prefix, expected_type=type_hints["key_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
            }
            if key_prefix is not None:
                self._values["key_prefix"] = key_prefix

        @builtins.property
        def bucket(self) -> builtins.str:
            '''The name of the Amazon S3 bucket where your data is stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3storage.html#cfn-iotanalytics-datastore-customermanageds3storage-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_prefix(self) -> typing.Optional[builtins.str]:
            '''(Optional) The prefix used to create the keys of the data store data objects.

            Each object in an Amazon S3 bucket has a key that is its unique identifier in the bucket. Each object in a bucket has exactly one key. The prefix must end with a forward slash (/).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-customermanageds3storage.html#cfn-iotanalytics-datastore-customermanageds3storage-keyprefix
            '''
            result = self._values.get("key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomerManagedS3StorageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDatastore.DatastorePartitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "partition": "partition",
            "timestamp_partition": "timestampPartition",
        },
    )
    class DatastorePartitionProperty:
        def __init__(
            self,
            *,
            partition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDatastore.PartitionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            timestamp_partition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDatastore.TimestampPartitionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A single dimension to partition a data store.

            The dimension must be an ``AttributePartition`` or a ``TimestampPartition`` .

            :param partition: A partition dimension defined by an attribute.
            :param timestamp_partition: A partition dimension defined by a timestamp attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorepartition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                datastore_partition_property = iotanalytics.CfnDatastore.DatastorePartitionProperty(
                    partition=iotanalytics.CfnDatastore.PartitionProperty(
                        attribute_name="attributeName"
                    ),
                    timestamp_partition=iotanalytics.CfnDatastore.TimestampPartitionProperty(
                        attribute_name="attributeName",
                
                        # the properties below are optional
                        timestamp_format="timestampFormat"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bbd39480bd26262bd30c3905cca3a0643938b5db9c601cc7a1dcc0d73fb778dd)
                check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
                check_type(argname="argument timestamp_partition", value=timestamp_partition, expected_type=type_hints["timestamp_partition"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if partition is not None:
                self._values["partition"] = partition
            if timestamp_partition is not None:
                self._values["timestamp_partition"] = timestamp_partition

        @builtins.property
        def partition(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.PartitionProperty"]]:
            '''A partition dimension defined by an attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorepartition.html#cfn-iotanalytics-datastore-datastorepartition-partition
            '''
            result = self._values.get("partition")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.PartitionProperty"]], result)

        @builtins.property
        def timestamp_partition(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.TimestampPartitionProperty"]]:
            '''A partition dimension defined by a timestamp attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorepartition.html#cfn-iotanalytics-datastore-datastorepartition-timestamppartition
            '''
            result = self._values.get("timestamp_partition")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.TimestampPartitionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatastorePartitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDatastore.DatastorePartitionsProperty",
        jsii_struct_bases=[],
        name_mapping={"partitions": "partitions"},
    )
    class DatastorePartitionsProperty:
        def __init__(
            self,
            *,
            partitions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDatastore.DatastorePartitionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Information about the partition dimensions in a data store.

            :param partitions: A list of partition dimensions in a data store.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorepartitions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                datastore_partitions_property = iotanalytics.CfnDatastore.DatastorePartitionsProperty(
                    partitions=[iotanalytics.CfnDatastore.DatastorePartitionProperty(
                        partition=iotanalytics.CfnDatastore.PartitionProperty(
                            attribute_name="attributeName"
                        ),
                        timestamp_partition=iotanalytics.CfnDatastore.TimestampPartitionProperty(
                            attribute_name="attributeName",
                
                            # the properties below are optional
                            timestamp_format="timestampFormat"
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__59a13ae3d10a02ccef29ab4c2489258358fa3aaf39021e87f7b7f0475d7924f5)
                check_type(argname="argument partitions", value=partitions, expected_type=type_hints["partitions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if partitions is not None:
                self._values["partitions"] = partitions

        @builtins.property
        def partitions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDatastore.DatastorePartitionProperty"]]]]:
            '''A list of partition dimensions in a data store.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorepartitions.html#cfn-iotanalytics-datastore-datastorepartitions-partitions
            '''
            result = self._values.get("partitions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDatastore.DatastorePartitionProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatastorePartitionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDatastore.DatastoreStorageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "customer_managed_s3": "customerManagedS3",
            "iot_site_wise_multi_layer_storage": "iotSiteWiseMultiLayerStorage",
            "service_managed_s3": "serviceManagedS3",
        },
    )
    class DatastoreStorageProperty:
        def __init__(
            self,
            *,
            customer_managed_s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDatastore.CustomerManagedS3Property", typing.Dict[builtins.str, typing.Any]]]] = None,
            iot_site_wise_multi_layer_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDatastore.IotSiteWiseMultiLayerStorageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            service_managed_s3: typing.Any = None,
        ) -> None:
            '''Where data store data is stored.

            :param customer_managed_s3: Use this to store data store data in an S3 bucket that you manage. The choice of service-managed or customer-managed S3 storage cannot be changed after creation of the data store.
            :param iot_site_wise_multi_layer_storage: Use this to store data used by AWS IoT SiteWise in an Amazon S3 bucket that you manage. You can't change the choice of Amazon S3 storage after your data store is created.
            :param service_managed_s3: Use this to store data store data in an S3 bucket managed by the AWS IoT Analytics service. The choice of service-managed or customer-managed S3 storage cannot be changed after creation of the data store.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorestorage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                # service_managed_s3: Any
                
                datastore_storage_property = iotanalytics.CfnDatastore.DatastoreStorageProperty(
                    customer_managed_s3=iotanalytics.CfnDatastore.CustomerManagedS3Property(
                        bucket="bucket",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        key_prefix="keyPrefix"
                    ),
                    iot_site_wise_multi_layer_storage=iotanalytics.CfnDatastore.IotSiteWiseMultiLayerStorageProperty(
                        customer_managed_s3_storage=iotanalytics.CfnDatastore.CustomerManagedS3StorageProperty(
                            bucket="bucket",
                
                            # the properties below are optional
                            key_prefix="keyPrefix"
                        )
                    ),
                    service_managed_s3=service_managed_s3
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5984b7f9d7ba382e2b28022cc78b28dd28173cb76fb8b5cc637be3ee56ea2c81)
                check_type(argname="argument customer_managed_s3", value=customer_managed_s3, expected_type=type_hints["customer_managed_s3"])
                check_type(argname="argument iot_site_wise_multi_layer_storage", value=iot_site_wise_multi_layer_storage, expected_type=type_hints["iot_site_wise_multi_layer_storage"])
                check_type(argname="argument service_managed_s3", value=service_managed_s3, expected_type=type_hints["service_managed_s3"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if customer_managed_s3 is not None:
                self._values["customer_managed_s3"] = customer_managed_s3
            if iot_site_wise_multi_layer_storage is not None:
                self._values["iot_site_wise_multi_layer_storage"] = iot_site_wise_multi_layer_storage
            if service_managed_s3 is not None:
                self._values["service_managed_s3"] = service_managed_s3

        @builtins.property
        def customer_managed_s3(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.CustomerManagedS3Property"]]:
            '''Use this to store data store data in an S3 bucket that you manage.

            The choice of service-managed or customer-managed S3 storage cannot be changed after creation of the data store.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorestorage.html#cfn-iotanalytics-datastore-datastorestorage-customermanageds3
            '''
            result = self._values.get("customer_managed_s3")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.CustomerManagedS3Property"]], result)

        @builtins.property
        def iot_site_wise_multi_layer_storage(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.IotSiteWiseMultiLayerStorageProperty"]]:
            '''Use this to store data used by AWS IoT SiteWise in an Amazon S3 bucket that you manage.

            You can't change the choice of Amazon S3 storage after your data store is created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorestorage.html#cfn-iotanalytics-datastore-datastorestorage-iotsitewisemultilayerstorage
            '''
            result = self._values.get("iot_site_wise_multi_layer_storage")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.IotSiteWiseMultiLayerStorageProperty"]], result)

        @builtins.property
        def service_managed_s3(self) -> typing.Any:
            '''Use this to store data store data in an S3 bucket managed by the AWS IoT Analytics service.

            The choice of service-managed or customer-managed S3 storage cannot be changed after creation of the data store.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-datastorestorage.html#cfn-iotanalytics-datastore-datastorestorage-servicemanageds3
            '''
            result = self._values.get("service_managed_s3")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatastoreStorageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDatastore.FileFormatConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "json_configuration": "jsonConfiguration",
            "parquet_configuration": "parquetConfiguration",
        },
    )
    class FileFormatConfigurationProperty:
        def __init__(
            self,
            *,
            json_configuration: typing.Any = None,
            parquet_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDatastore.ParquetConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains the configuration information of file formats. AWS IoT Analytics data stores support JSON and `Parquet <https://docs.aws.amazon.com/https://parquet.apache.org/>`_ .

            The default file format is JSON. You can specify only one format.

            You can't change the file format after you create the data store.

            :param json_configuration: Contains the configuration information of the JSON format.
            :param parquet_configuration: Contains the configuration information of the Parquet format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-fileformatconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                # json_configuration: Any
                
                file_format_configuration_property = iotanalytics.CfnDatastore.FileFormatConfigurationProperty(
                    json_configuration=json_configuration,
                    parquet_configuration=iotanalytics.CfnDatastore.ParquetConfigurationProperty(
                        schema_definition=iotanalytics.CfnDatastore.SchemaDefinitionProperty(
                            columns=[iotanalytics.CfnDatastore.ColumnProperty(
                                name="name",
                                type="type"
                            )]
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e0ed74456c35a181d6d6de607a0cba62b46dacd1b5841393ea8e579cde121ff1)
                check_type(argname="argument json_configuration", value=json_configuration, expected_type=type_hints["json_configuration"])
                check_type(argname="argument parquet_configuration", value=parquet_configuration, expected_type=type_hints["parquet_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if json_configuration is not None:
                self._values["json_configuration"] = json_configuration
            if parquet_configuration is not None:
                self._values["parquet_configuration"] = parquet_configuration

        @builtins.property
        def json_configuration(self) -> typing.Any:
            '''Contains the configuration information of the JSON format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-fileformatconfiguration.html#cfn-iotanalytics-datastore-fileformatconfiguration-jsonconfiguration
            '''
            result = self._values.get("json_configuration")
            return typing.cast(typing.Any, result)

        @builtins.property
        def parquet_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.ParquetConfigurationProperty"]]:
            '''Contains the configuration information of the Parquet format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-fileformatconfiguration.html#cfn-iotanalytics-datastore-fileformatconfiguration-parquetconfiguration
            '''
            result = self._values.get("parquet_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.ParquetConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FileFormatConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDatastore.IotSiteWiseMultiLayerStorageProperty",
        jsii_struct_bases=[],
        name_mapping={"customer_managed_s3_storage": "customerManagedS3Storage"},
    )
    class IotSiteWiseMultiLayerStorageProperty:
        def __init__(
            self,
            *,
            customer_managed_s3_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDatastore.CustomerManagedS3StorageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Stores data used by AWS IoT SiteWise in an Amazon S3 bucket that you manage.

            You can't change the choice of Amazon S3 storage after your data store is created.

            :param customer_managed_s3_storage: Stores data used by AWS IoT SiteWise in an Amazon S3 bucket that you manage.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-iotsitewisemultilayerstorage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                iot_site_wise_multi_layer_storage_property = iotanalytics.CfnDatastore.IotSiteWiseMultiLayerStorageProperty(
                    customer_managed_s3_storage=iotanalytics.CfnDatastore.CustomerManagedS3StorageProperty(
                        bucket="bucket",
                
                        # the properties below are optional
                        key_prefix="keyPrefix"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f347023ec67ebec701d0a7d67d19ead6d99d6ae0f1aa6aad2416fcce1d5e2591)
                check_type(argname="argument customer_managed_s3_storage", value=customer_managed_s3_storage, expected_type=type_hints["customer_managed_s3_storage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if customer_managed_s3_storage is not None:
                self._values["customer_managed_s3_storage"] = customer_managed_s3_storage

        @builtins.property
        def customer_managed_s3_storage(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.CustomerManagedS3StorageProperty"]]:
            '''Stores data used by AWS IoT SiteWise in an Amazon S3 bucket that you manage.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-iotsitewisemultilayerstorage.html#cfn-iotanalytics-datastore-iotsitewisemultilayerstorage-customermanageds3storage
            '''
            result = self._values.get("customer_managed_s3_storage")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.CustomerManagedS3StorageProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IotSiteWiseMultiLayerStorageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDatastore.ParquetConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"schema_definition": "schemaDefinition"},
    )
    class ParquetConfigurationProperty:
        def __init__(
            self,
            *,
            schema_definition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDatastore.SchemaDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains the configuration information of the Parquet format.

            :param schema_definition: Information needed to define a schema.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-parquetconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                parquet_configuration_property = iotanalytics.CfnDatastore.ParquetConfigurationProperty(
                    schema_definition=iotanalytics.CfnDatastore.SchemaDefinitionProperty(
                        columns=[iotanalytics.CfnDatastore.ColumnProperty(
                            name="name",
                            type="type"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dea7c4dd001f38a8f0ea6dfa412735a2dab8f5b3cae0ed5309527fad8bee321e)
                check_type(argname="argument schema_definition", value=schema_definition, expected_type=type_hints["schema_definition"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if schema_definition is not None:
                self._values["schema_definition"] = schema_definition

        @builtins.property
        def schema_definition(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.SchemaDefinitionProperty"]]:
            '''Information needed to define a schema.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-parquetconfiguration.html#cfn-iotanalytics-datastore-parquetconfiguration-schemadefinition
            '''
            result = self._values.get("schema_definition")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDatastore.SchemaDefinitionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParquetConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDatastore.PartitionProperty",
        jsii_struct_bases=[],
        name_mapping={"attribute_name": "attributeName"},
    )
    class PartitionProperty:
        def __init__(self, *, attribute_name: builtins.str) -> None:
            '''A single dimension to partition a data store.

            The dimension must be an ``AttributePartition`` or a ``TimestampPartition`` .

            :param attribute_name: The name of the attribute that defines a partition dimension.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-partition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                partition_property = iotanalytics.CfnDatastore.PartitionProperty(
                    attribute_name="attributeName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__327e41bcdc4d9e40e80bb337f397b1df7c75d836745e92ad6753e1ccc8fa6ddd)
                check_type(argname="argument attribute_name", value=attribute_name, expected_type=type_hints["attribute_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "attribute_name": attribute_name,
            }

        @builtins.property
        def attribute_name(self) -> builtins.str:
            '''The name of the attribute that defines a partition dimension.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-partition.html#cfn-iotanalytics-datastore-partition-attributename
            '''
            result = self._values.get("attribute_name")
            assert result is not None, "Required property 'attribute_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PartitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDatastore.RetentionPeriodProperty",
        jsii_struct_bases=[],
        name_mapping={"number_of_days": "numberOfDays", "unlimited": "unlimited"},
    )
    class RetentionPeriodProperty:
        def __init__(
            self,
            *,
            number_of_days: typing.Optional[jsii.Number] = None,
            unlimited: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''How long, in days, message data is kept.

            :param number_of_days: The number of days that message data is kept. The ``unlimited`` parameter must be false.
            :param unlimited: If true, message data is kept indefinitely.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-retentionperiod.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                retention_period_property = iotanalytics.CfnDatastore.RetentionPeriodProperty(
                    number_of_days=123,
                    unlimited=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a7f15bd2b6ccbd3452a9eccff4b8b3378d4efc6f30d6f60f6faed63b647a4c3c)
                check_type(argname="argument number_of_days", value=number_of_days, expected_type=type_hints["number_of_days"])
                check_type(argname="argument unlimited", value=unlimited, expected_type=type_hints["unlimited"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if number_of_days is not None:
                self._values["number_of_days"] = number_of_days
            if unlimited is not None:
                self._values["unlimited"] = unlimited

        @builtins.property
        def number_of_days(self) -> typing.Optional[jsii.Number]:
            '''The number of days that message data is kept.

            The ``unlimited`` parameter must be false.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-retentionperiod.html#cfn-iotanalytics-datastore-retentionperiod-numberofdays
            '''
            result = self._values.get("number_of_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def unlimited(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If true, message data is kept indefinitely.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-retentionperiod.html#cfn-iotanalytics-datastore-retentionperiod-unlimited
            '''
            result = self._values.get("unlimited")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RetentionPeriodProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDatastore.SchemaDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"columns": "columns"},
    )
    class SchemaDefinitionProperty:
        def __init__(
            self,
            *,
            columns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDatastore.ColumnProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Information needed to define a schema.

            :param columns: Specifies one or more columns that store your data. Each schema can have up to 100 columns. Each column can have up to 100 nested types.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-schemadefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                schema_definition_property = iotanalytics.CfnDatastore.SchemaDefinitionProperty(
                    columns=[iotanalytics.CfnDatastore.ColumnProperty(
                        name="name",
                        type="type"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f36d43c7f1f6d356e648b26afe1feb2408dae7114d15163cf3465b0a94ba58e7)
                check_type(argname="argument columns", value=columns, expected_type=type_hints["columns"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if columns is not None:
                self._values["columns"] = columns

        @builtins.property
        def columns(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDatastore.ColumnProperty"]]]]:
            '''Specifies one or more columns that store your data.

            Each schema can have up to 100 columns. Each column can have up to 100 nested types.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-schemadefinition.html#cfn-iotanalytics-datastore-schemadefinition-columns
            '''
            result = self._values.get("columns")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDatastore.ColumnProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SchemaDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDatastore.TimestampPartitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attribute_name": "attributeName",
            "timestamp_format": "timestampFormat",
        },
    )
    class TimestampPartitionProperty:
        def __init__(
            self,
            *,
            attribute_name: builtins.str,
            timestamp_format: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A partition dimension defined by a timestamp attribute.

            :param attribute_name: The attribute name of the partition defined by a timestamp.
            :param timestamp_format: The timestamp format of a partition defined by a timestamp. The default format is seconds since epoch (January 1, 1970 at midnight UTC time).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-timestamppartition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                timestamp_partition_property = iotanalytics.CfnDatastore.TimestampPartitionProperty(
                    attribute_name="attributeName",
                
                    # the properties below are optional
                    timestamp_format="timestampFormat"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6d43c9ee54cedeb8e135981f6b1b363d55973c05551571400829d3f5e2771731)
                check_type(argname="argument attribute_name", value=attribute_name, expected_type=type_hints["attribute_name"])
                check_type(argname="argument timestamp_format", value=timestamp_format, expected_type=type_hints["timestamp_format"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "attribute_name": attribute_name,
            }
            if timestamp_format is not None:
                self._values["timestamp_format"] = timestamp_format

        @builtins.property
        def attribute_name(self) -> builtins.str:
            '''The attribute name of the partition defined by a timestamp.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-timestamppartition.html#cfn-iotanalytics-datastore-timestamppartition-attributename
            '''
            result = self._values.get("attribute_name")
            assert result is not None, "Required property 'attribute_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def timestamp_format(self) -> typing.Optional[builtins.str]:
            '''The timestamp format of a partition defined by a timestamp.

            The default format is seconds since epoch (January 1, 1970 at midnight UTC time).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-datastore-timestamppartition.html#cfn-iotanalytics-datastore-timestamppartition-timestampformat
            '''
            result = self._values.get("timestamp_format")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimestampPartitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotanalytics.CfnDatastoreProps",
    jsii_struct_bases=[],
    name_mapping={
        "datastore_name": "datastoreName",
        "datastore_partitions": "datastorePartitions",
        "datastore_storage": "datastoreStorage",
        "file_format_configuration": "fileFormatConfiguration",
        "retention_period": "retentionPeriod",
        "tags": "tags",
    },
)
class CfnDatastoreProps:
    def __init__(
        self,
        *,
        datastore_name: typing.Optional[builtins.str] = None,
        datastore_partitions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatastore.DatastorePartitionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        datastore_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatastore.DatastoreStorageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        file_format_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatastore.FileFormatConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        retention_period: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatastore.RetentionPeriodProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDatastore``.

        :param datastore_name: The name of the data store.
        :param datastore_partitions: Information about the partition dimensions in a data store.
        :param datastore_storage: Where data store data is stored.
        :param file_format_configuration: Contains the configuration information of file formats. AWS IoT Analytics data stores support JSON and `Parquet <https://docs.aws.amazon.com/https://parquet.apache.org/>`_ . The default file format is JSON. You can specify only one format. You can't change the file format after you create the data store.
        :param retention_period: How long, in days, message data is kept for the data store. When ``customerManagedS3`` storage is selected, this parameter is ignored.
        :param tags: Metadata which can be used to manage the data store. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotanalytics as iotanalytics
            
            # json_configuration: Any
            # service_managed_s3: Any
            
            cfn_datastore_props = iotanalytics.CfnDatastoreProps(
                datastore_name="datastoreName",
                datastore_partitions=iotanalytics.CfnDatastore.DatastorePartitionsProperty(
                    partitions=[iotanalytics.CfnDatastore.DatastorePartitionProperty(
                        partition=iotanalytics.CfnDatastore.PartitionProperty(
                            attribute_name="attributeName"
                        ),
                        timestamp_partition=iotanalytics.CfnDatastore.TimestampPartitionProperty(
                            attribute_name="attributeName",
            
                            # the properties below are optional
                            timestamp_format="timestampFormat"
                        )
                    )]
                ),
                datastore_storage=iotanalytics.CfnDatastore.DatastoreStorageProperty(
                    customer_managed_s3=iotanalytics.CfnDatastore.CustomerManagedS3Property(
                        bucket="bucket",
                        role_arn="roleArn",
            
                        # the properties below are optional
                        key_prefix="keyPrefix"
                    ),
                    iot_site_wise_multi_layer_storage=iotanalytics.CfnDatastore.IotSiteWiseMultiLayerStorageProperty(
                        customer_managed_s3_storage=iotanalytics.CfnDatastore.CustomerManagedS3StorageProperty(
                            bucket="bucket",
            
                            # the properties below are optional
                            key_prefix="keyPrefix"
                        )
                    ),
                    service_managed_s3=service_managed_s3
                ),
                file_format_configuration=iotanalytics.CfnDatastore.FileFormatConfigurationProperty(
                    json_configuration=json_configuration,
                    parquet_configuration=iotanalytics.CfnDatastore.ParquetConfigurationProperty(
                        schema_definition=iotanalytics.CfnDatastore.SchemaDefinitionProperty(
                            columns=[iotanalytics.CfnDatastore.ColumnProperty(
                                name="name",
                                type="type"
                            )]
                        )
                    )
                ),
                retention_period=iotanalytics.CfnDatastore.RetentionPeriodProperty(
                    number_of_days=123,
                    unlimited=False
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5e07deff1542b5d76f6fbec1b51b693bafafe7f15017228354ea52b83a2737b)
            check_type(argname="argument datastore_name", value=datastore_name, expected_type=type_hints["datastore_name"])
            check_type(argname="argument datastore_partitions", value=datastore_partitions, expected_type=type_hints["datastore_partitions"])
            check_type(argname="argument datastore_storage", value=datastore_storage, expected_type=type_hints["datastore_storage"])
            check_type(argname="argument file_format_configuration", value=file_format_configuration, expected_type=type_hints["file_format_configuration"])
            check_type(argname="argument retention_period", value=retention_period, expected_type=type_hints["retention_period"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if datastore_name is not None:
            self._values["datastore_name"] = datastore_name
        if datastore_partitions is not None:
            self._values["datastore_partitions"] = datastore_partitions
        if datastore_storage is not None:
            self._values["datastore_storage"] = datastore_storage
        if file_format_configuration is not None:
            self._values["file_format_configuration"] = file_format_configuration
        if retention_period is not None:
            self._values["retention_period"] = retention_period
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def datastore_name(self) -> typing.Optional[builtins.str]:
        '''The name of the data store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html#cfn-iotanalytics-datastore-datastorename
        '''
        result = self._values.get("datastore_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def datastore_partitions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDatastore.DatastorePartitionsProperty]]:
        '''Information about the partition dimensions in a data store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html#cfn-iotanalytics-datastore-datastorepartitions
        '''
        result = self._values.get("datastore_partitions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDatastore.DatastorePartitionsProperty]], result)

    @builtins.property
    def datastore_storage(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDatastore.DatastoreStorageProperty]]:
        '''Where data store data is stored.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html#cfn-iotanalytics-datastore-datastorestorage
        '''
        result = self._values.get("datastore_storage")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDatastore.DatastoreStorageProperty]], result)

    @builtins.property
    def file_format_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDatastore.FileFormatConfigurationProperty]]:
        '''Contains the configuration information of file formats. AWS IoT Analytics data stores support JSON and `Parquet <https://docs.aws.amazon.com/https://parquet.apache.org/>`_ .

        The default file format is JSON. You can specify only one format.

        You can't change the file format after you create the data store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html#cfn-iotanalytics-datastore-fileformatconfiguration
        '''
        result = self._values.get("file_format_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDatastore.FileFormatConfigurationProperty]], result)

    @builtins.property
    def retention_period(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDatastore.RetentionPeriodProperty]]:
        '''How long, in days, message data is kept for the data store.

        When ``customerManagedS3`` storage is selected, this parameter is ignored.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html#cfn-iotanalytics-datastore-retentionperiod
        '''
        result = self._values.get("retention_period")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDatastore.RetentionPeriodProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata which can be used to manage the data store.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html#cfn-iotanalytics-datastore-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDatastoreProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnPipeline(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotanalytics.CfnPipeline",
):
    '''The AWS::IoTAnalytics::Pipeline resource consumes messages from one or more channels and allows you to process the messages before storing them in a data store.

    You must specify both a ``channel`` and a ``datastore`` activity and, optionally, as many as 23 additional activities in the ``pipelineActivities`` array. For more information, see `How to Use AWS IoT Analytics <https://docs.aws.amazon.com/iotanalytics/latest/userguide/welcome.html#aws-iot-analytics-how>`_ in the *AWS IoT Analytics User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-pipeline.html
    :cloudformationResource: AWS::IoTAnalytics::Pipeline
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotanalytics as iotanalytics
        
        cfn_pipeline = iotanalytics.CfnPipeline(self, "MyCfnPipeline",
            pipeline_activities=[iotanalytics.CfnPipeline.ActivityProperty(
                add_attributes=iotanalytics.CfnPipeline.AddAttributesProperty(
                    attributes={
                        "attributes_key": "attributes"
                    },
                    name="name",
        
                    # the properties below are optional
                    next="next"
                ),
                channel=iotanalytics.CfnPipeline.ChannelProperty(
                    channel_name="channelName",
                    name="name",
        
                    # the properties below are optional
                    next="next"
                ),
                datastore=iotanalytics.CfnPipeline.DatastoreProperty(
                    datastore_name="datastoreName",
                    name="name"
                ),
                device_registry_enrich=iotanalytics.CfnPipeline.DeviceRegistryEnrichProperty(
                    attribute="attribute",
                    name="name",
                    role_arn="roleArn",
                    thing_name="thingName",
        
                    # the properties below are optional
                    next="next"
                ),
                device_shadow_enrich=iotanalytics.CfnPipeline.DeviceShadowEnrichProperty(
                    attribute="attribute",
                    name="name",
                    role_arn="roleArn",
                    thing_name="thingName",
        
                    # the properties below are optional
                    next="next"
                ),
                filter=iotanalytics.CfnPipeline.FilterProperty(
                    filter="filter",
                    name="name",
        
                    # the properties below are optional
                    next="next"
                ),
                lambda_=iotanalytics.CfnPipeline.LambdaProperty(
                    batch_size=123,
                    lambda_name="lambdaName",
                    name="name",
        
                    # the properties below are optional
                    next="next"
                ),
                math=iotanalytics.CfnPipeline.MathProperty(
                    attribute="attribute",
                    math="math",
                    name="name",
        
                    # the properties below are optional
                    next="next"
                ),
                remove_attributes=iotanalytics.CfnPipeline.RemoveAttributesProperty(
                    attributes=["attributes"],
                    name="name",
        
                    # the properties below are optional
                    next="next"
                ),
                select_attributes=iotanalytics.CfnPipeline.SelectAttributesProperty(
                    attributes=["attributes"],
                    name="name",
        
                    # the properties below are optional
                    next="next"
                )
            )],
        
            # the properties below are optional
            pipeline_name="pipelineName",
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
        pipeline_activities: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipeline.ActivityProperty", typing.Dict[builtins.str, typing.Any]]]]],
        pipeline_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param pipeline_activities: A list of "PipelineActivity" objects. Activities perform transformations on your messages, such as removing, renaming or adding message attributes; filtering messages based on attribute values; invoking your Lambda functions on messages for advanced processing; or performing mathematical transformations to normalize device data. The list can be 2-25 *PipelineActivity* objects and must contain both a ``channel`` and a ``datastore`` activity. Each entry in the list must contain only one activity, for example: ``pipelineActivities = [ { "channel": { ... } }, { "lambda": { ... } }, ... ]``
        :param pipeline_name: The name of the pipeline.
        :param tags: Metadata which can be used to manage the pipeline. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__780e6e051f6bd102a51bd0b3de8f56cd44681953f4198d827460085558e2add9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPipelineProps(
            pipeline_activities=pipeline_activities,
            pipeline_name=pipeline_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__405496d6c191e31df7bb8a63193cea61a5bf750f573ac5a5fede36aaa0994c7c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ba374f9d6213ab4f683b1553c4a35de7e4a81680071121852d026b7cd734f359)
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
        '''
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
    @jsii.member(jsii_name="pipelineActivities")
    def pipeline_activities(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipeline.ActivityProperty"]]]:
        '''A list of "PipelineActivity" objects.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipeline.ActivityProperty"]]], jsii.get(self, "pipelineActivities"))

    @pipeline_activities.setter
    def pipeline_activities(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPipeline.ActivityProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f91482ef32b46baa85edafca306dfc279654decbb3dc3b6968fd311f70972d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pipelineActivities", value)

    @builtins.property
    @jsii.member(jsii_name="pipelineName")
    def pipeline_name(self) -> typing.Optional[builtins.str]:
        '''The name of the pipeline.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pipelineName"))

    @pipeline_name.setter
    def pipeline_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54be44f48af8d45aa4b74df14476342f70be64a61ed9cc470a1a0efa37552b10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pipelineName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata which can be used to manage the pipeline.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb2cf7a7a3f0428848c668b76beea41674b32a79ad06a43cc68538235ba32f54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnPipeline.ActivityProperty",
        jsii_struct_bases=[],
        name_mapping={
            "add_attributes": "addAttributes",
            "channel": "channel",
            "datastore": "datastore",
            "device_registry_enrich": "deviceRegistryEnrich",
            "device_shadow_enrich": "deviceShadowEnrich",
            "filter": "filter",
            "lambda_": "lambda",
            "math": "math",
            "remove_attributes": "removeAttributes",
            "select_attributes": "selectAttributes",
        },
    )
    class ActivityProperty:
        def __init__(
            self,
            *,
            add_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipeline.AddAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            channel: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipeline.ChannelProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            datastore: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipeline.DatastoreProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            device_registry_enrich: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipeline.DeviceRegistryEnrichProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            device_shadow_enrich: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipeline.DeviceShadowEnrichProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            filter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipeline.FilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            lambda_: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipeline.LambdaProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            math: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipeline.MathProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            remove_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipeline.RemoveAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            select_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipeline.SelectAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''An activity that performs a transformation on a message.

            :param add_attributes: Adds other attributes based on existing attributes in the message.
            :param channel: Determines the source of the messages to be processed.
            :param datastore: Specifies where to store the processed message data.
            :param device_registry_enrich: Adds data from the AWS IoT device registry to your message.
            :param device_shadow_enrich: Adds information from the AWS IoT Device Shadows service to a message.
            :param filter: Filters a message based on its attributes.
            :param lambda_: Runs a Lambda function to modify the message.
            :param math: Computes an arithmetic expression using the message's attributes and adds it to the message.
            :param remove_attributes: Removes attributes from a message.
            :param select_attributes: Creates a new message using only the specified attributes from the original message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                activity_property = iotanalytics.CfnPipeline.ActivityProperty(
                    add_attributes=iotanalytics.CfnPipeline.AddAttributesProperty(
                        attributes={
                            "attributes_key": "attributes"
                        },
                        name="name",
                
                        # the properties below are optional
                        next="next"
                    ),
                    channel=iotanalytics.CfnPipeline.ChannelProperty(
                        channel_name="channelName",
                        name="name",
                
                        # the properties below are optional
                        next="next"
                    ),
                    datastore=iotanalytics.CfnPipeline.DatastoreProperty(
                        datastore_name="datastoreName",
                        name="name"
                    ),
                    device_registry_enrich=iotanalytics.CfnPipeline.DeviceRegistryEnrichProperty(
                        attribute="attribute",
                        name="name",
                        role_arn="roleArn",
                        thing_name="thingName",
                
                        # the properties below are optional
                        next="next"
                    ),
                    device_shadow_enrich=iotanalytics.CfnPipeline.DeviceShadowEnrichProperty(
                        attribute="attribute",
                        name="name",
                        role_arn="roleArn",
                        thing_name="thingName",
                
                        # the properties below are optional
                        next="next"
                    ),
                    filter=iotanalytics.CfnPipeline.FilterProperty(
                        filter="filter",
                        name="name",
                
                        # the properties below are optional
                        next="next"
                    ),
                    lambda_=iotanalytics.CfnPipeline.LambdaProperty(
                        batch_size=123,
                        lambda_name="lambdaName",
                        name="name",
                
                        # the properties below are optional
                        next="next"
                    ),
                    math=iotanalytics.CfnPipeline.MathProperty(
                        attribute="attribute",
                        math="math",
                        name="name",
                
                        # the properties below are optional
                        next="next"
                    ),
                    remove_attributes=iotanalytics.CfnPipeline.RemoveAttributesProperty(
                        attributes=["attributes"],
                        name="name",
                
                        # the properties below are optional
                        next="next"
                    ),
                    select_attributes=iotanalytics.CfnPipeline.SelectAttributesProperty(
                        attributes=["attributes"],
                        name="name",
                
                        # the properties below are optional
                        next="next"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ef4301ffee8a8b9c56444ba866610802447f4507a483114152269c2d14b47821)
                check_type(argname="argument add_attributes", value=add_attributes, expected_type=type_hints["add_attributes"])
                check_type(argname="argument channel", value=channel, expected_type=type_hints["channel"])
                check_type(argname="argument datastore", value=datastore, expected_type=type_hints["datastore"])
                check_type(argname="argument device_registry_enrich", value=device_registry_enrich, expected_type=type_hints["device_registry_enrich"])
                check_type(argname="argument device_shadow_enrich", value=device_shadow_enrich, expected_type=type_hints["device_shadow_enrich"])
                check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
                check_type(argname="argument lambda_", value=lambda_, expected_type=type_hints["lambda_"])
                check_type(argname="argument math", value=math, expected_type=type_hints["math"])
                check_type(argname="argument remove_attributes", value=remove_attributes, expected_type=type_hints["remove_attributes"])
                check_type(argname="argument select_attributes", value=select_attributes, expected_type=type_hints["select_attributes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if add_attributes is not None:
                self._values["add_attributes"] = add_attributes
            if channel is not None:
                self._values["channel"] = channel
            if datastore is not None:
                self._values["datastore"] = datastore
            if device_registry_enrich is not None:
                self._values["device_registry_enrich"] = device_registry_enrich
            if device_shadow_enrich is not None:
                self._values["device_shadow_enrich"] = device_shadow_enrich
            if filter is not None:
                self._values["filter"] = filter
            if lambda_ is not None:
                self._values["lambda_"] = lambda_
            if math is not None:
                self._values["math"] = math
            if remove_attributes is not None:
                self._values["remove_attributes"] = remove_attributes
            if select_attributes is not None:
                self._values["select_attributes"] = select_attributes

        @builtins.property
        def add_attributes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.AddAttributesProperty"]]:
            '''Adds other attributes based on existing attributes in the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-addattributes
            '''
            result = self._values.get("add_attributes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.AddAttributesProperty"]], result)

        @builtins.property
        def channel(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.ChannelProperty"]]:
            '''Determines the source of the messages to be processed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-channel
            '''
            result = self._values.get("channel")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.ChannelProperty"]], result)

        @builtins.property
        def datastore(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.DatastoreProperty"]]:
            '''Specifies where to store the processed message data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-datastore
            '''
            result = self._values.get("datastore")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.DatastoreProperty"]], result)

        @builtins.property
        def device_registry_enrich(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.DeviceRegistryEnrichProperty"]]:
            '''Adds data from the AWS IoT device registry to your message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-deviceregistryenrich
            '''
            result = self._values.get("device_registry_enrich")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.DeviceRegistryEnrichProperty"]], result)

        @builtins.property
        def device_shadow_enrich(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.DeviceShadowEnrichProperty"]]:
            '''Adds information from the AWS IoT Device Shadows service to a message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-deviceshadowenrich
            '''
            result = self._values.get("device_shadow_enrich")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.DeviceShadowEnrichProperty"]], result)

        @builtins.property
        def filter(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.FilterProperty"]]:
            '''Filters a message based on its attributes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-filter
            '''
            result = self._values.get("filter")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.FilterProperty"]], result)

        @builtins.property
        def lambda_(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.LambdaProperty"]]:
            '''Runs a Lambda function to modify the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-lambda
            '''
            result = self._values.get("lambda_")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.LambdaProperty"]], result)

        @builtins.property
        def math(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.MathProperty"]]:
            '''Computes an arithmetic expression using the message's attributes and adds it to the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-math
            '''
            result = self._values.get("math")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.MathProperty"]], result)

        @builtins.property
        def remove_attributes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.RemoveAttributesProperty"]]:
            '''Removes attributes from a message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-removeattributes
            '''
            result = self._values.get("remove_attributes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.RemoveAttributesProperty"]], result)

        @builtins.property
        def select_attributes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.SelectAttributesProperty"]]:
            '''Creates a new message using only the specified attributes from the original message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-activity.html#cfn-iotanalytics-pipeline-activity-selectattributes
            '''
            result = self._values.get("select_attributes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.SelectAttributesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActivityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnPipeline.AddAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={"attributes": "attributes", "name": "name", "next": "next"},
    )
    class AddAttributesProperty:
        def __init__(
            self,
            *,
            attributes: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]],
            name: builtins.str,
            next: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An activity that adds other attributes based on existing attributes in the message.

            :param attributes: A list of 1-50 "AttributeNameMapping" objects that map an existing attribute to a new attribute. .. epigraph:: The existing attributes remain in the message, so if you want to remove the originals, use "RemoveAttributeActivity".
            :param name: The name of the 'addAttributes' activity.
            :param next: The next activity in the pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-addattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                add_attributes_property = iotanalytics.CfnPipeline.AddAttributesProperty(
                    attributes={
                        "attributes_key": "attributes"
                    },
                    name="name",
                
                    # the properties below are optional
                    next="next"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__577567edb1bcbc381086b32d827a8fa916777984a8a94532f921964c944864e3)
                check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument next", value=next, expected_type=type_hints["next"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "attributes": attributes,
                "name": name,
            }
            if next is not None:
                self._values["next"] = next

        @builtins.property
        def attributes(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]:
            '''A list of 1-50 "AttributeNameMapping" objects that map an existing attribute to a new attribute.

            .. epigraph::

               The existing attributes remain in the message, so if you want to remove the originals, use "RemoveAttributeActivity".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-addattributes.html#cfn-iotanalytics-pipeline-addattributes-attributes
            '''
            result = self._values.get("attributes")
            assert result is not None, "Required property 'attributes' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the 'addAttributes' activity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-addattributes.html#cfn-iotanalytics-pipeline-addattributes-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def next(self) -> typing.Optional[builtins.str]:
            '''The next activity in the pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-addattributes.html#cfn-iotanalytics-pipeline-addattributes-next
            '''
            result = self._values.get("next")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AddAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnPipeline.ChannelProperty",
        jsii_struct_bases=[],
        name_mapping={"channel_name": "channelName", "name": "name", "next": "next"},
    )
    class ChannelProperty:
        def __init__(
            self,
            *,
            channel_name: builtins.str,
            name: builtins.str,
            next: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Determines the source of the messages to be processed.

            :param channel_name: The name of the channel from which the messages are processed.
            :param name: The name of the 'channel' activity.
            :param next: The next activity in the pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-channel.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                channel_property = iotanalytics.CfnPipeline.ChannelProperty(
                    channel_name="channelName",
                    name="name",
                
                    # the properties below are optional
                    next="next"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__527444433b58193b6bbced07f46923ccbfa842f89d0abdfc358194e5d487ec43)
                check_type(argname="argument channel_name", value=channel_name, expected_type=type_hints["channel_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument next", value=next, expected_type=type_hints["next"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "channel_name": channel_name,
                "name": name,
            }
            if next is not None:
                self._values["next"] = next

        @builtins.property
        def channel_name(self) -> builtins.str:
            '''The name of the channel from which the messages are processed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-channel.html#cfn-iotanalytics-pipeline-channel-channelname
            '''
            result = self._values.get("channel_name")
            assert result is not None, "Required property 'channel_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the 'channel' activity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-channel.html#cfn-iotanalytics-pipeline-channel-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def next(self) -> typing.Optional[builtins.str]:
            '''The next activity in the pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-channel.html#cfn-iotanalytics-pipeline-channel-next
            '''
            result = self._values.get("next")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ChannelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnPipeline.DatastoreProperty",
        jsii_struct_bases=[],
        name_mapping={"datastore_name": "datastoreName", "name": "name"},
    )
    class DatastoreProperty:
        def __init__(self, *, datastore_name: builtins.str, name: builtins.str) -> None:
            '''The datastore activity that specifies where to store the processed data.

            :param datastore_name: The name of the data store where processed messages are stored.
            :param name: The name of the datastore activity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-datastore.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                datastore_property = iotanalytics.CfnPipeline.DatastoreProperty(
                    datastore_name="datastoreName",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3babb765a17ffb7f52df98d8cfac4d4ad731f21ae72df208b251bda410ab8786)
                check_type(argname="argument datastore_name", value=datastore_name, expected_type=type_hints["datastore_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "datastore_name": datastore_name,
                "name": name,
            }

        @builtins.property
        def datastore_name(self) -> builtins.str:
            '''The name of the data store where processed messages are stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-datastore.html#cfn-iotanalytics-pipeline-datastore-datastorename
            '''
            result = self._values.get("datastore_name")
            assert result is not None, "Required property 'datastore_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the datastore activity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-datastore.html#cfn-iotanalytics-pipeline-datastore-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatastoreProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnPipeline.DeviceRegistryEnrichProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attribute": "attribute",
            "name": "name",
            "role_arn": "roleArn",
            "thing_name": "thingName",
            "next": "next",
        },
    )
    class DeviceRegistryEnrichProperty:
        def __init__(
            self,
            *,
            attribute: builtins.str,
            name: builtins.str,
            role_arn: builtins.str,
            thing_name: builtins.str,
            next: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An activity that adds data from the AWS IoT device registry to your message.

            :param attribute: The name of the attribute that is added to the message.
            :param name: The name of the 'deviceRegistryEnrich' activity.
            :param role_arn: The ARN of the role that allows access to the device's registry information.
            :param thing_name: The name of the IoT device whose registry information is added to the message.
            :param next: The next activity in the pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceregistryenrich.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                device_registry_enrich_property = iotanalytics.CfnPipeline.DeviceRegistryEnrichProperty(
                    attribute="attribute",
                    name="name",
                    role_arn="roleArn",
                    thing_name="thingName",
                
                    # the properties below are optional
                    next="next"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b2800ea3a2b7d7d4294d7e2e6344a11b8cad32694fb315fc03efd00bc0505dc5)
                check_type(argname="argument attribute", value=attribute, expected_type=type_hints["attribute"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument thing_name", value=thing_name, expected_type=type_hints["thing_name"])
                check_type(argname="argument next", value=next, expected_type=type_hints["next"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "attribute": attribute,
                "name": name,
                "role_arn": role_arn,
                "thing_name": thing_name,
            }
            if next is not None:
                self._values["next"] = next

        @builtins.property
        def attribute(self) -> builtins.str:
            '''The name of the attribute that is added to the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceregistryenrich.html#cfn-iotanalytics-pipeline-deviceregistryenrich-attribute
            '''
            result = self._values.get("attribute")
            assert result is not None, "Required property 'attribute' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the 'deviceRegistryEnrich' activity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceregistryenrich.html#cfn-iotanalytics-pipeline-deviceregistryenrich-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the role that allows access to the device's registry information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceregistryenrich.html#cfn-iotanalytics-pipeline-deviceregistryenrich-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def thing_name(self) -> builtins.str:
            '''The name of the IoT device whose registry information is added to the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceregistryenrich.html#cfn-iotanalytics-pipeline-deviceregistryenrich-thingname
            '''
            result = self._values.get("thing_name")
            assert result is not None, "Required property 'thing_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def next(self) -> typing.Optional[builtins.str]:
            '''The next activity in the pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceregistryenrich.html#cfn-iotanalytics-pipeline-deviceregistryenrich-next
            '''
            result = self._values.get("next")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeviceRegistryEnrichProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnPipeline.DeviceShadowEnrichProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attribute": "attribute",
            "name": "name",
            "role_arn": "roleArn",
            "thing_name": "thingName",
            "next": "next",
        },
    )
    class DeviceShadowEnrichProperty:
        def __init__(
            self,
            *,
            attribute: builtins.str,
            name: builtins.str,
            role_arn: builtins.str,
            thing_name: builtins.str,
            next: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An activity that adds information from the AWS IoT Device Shadows service to a message.

            :param attribute: The name of the attribute that is added to the message.
            :param name: The name of the 'deviceShadowEnrich' activity.
            :param role_arn: The ARN of the role that allows access to the device's shadow.
            :param thing_name: The name of the IoT device whose shadow information is added to the message.
            :param next: The next activity in the pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceshadowenrich.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                device_shadow_enrich_property = iotanalytics.CfnPipeline.DeviceShadowEnrichProperty(
                    attribute="attribute",
                    name="name",
                    role_arn="roleArn",
                    thing_name="thingName",
                
                    # the properties below are optional
                    next="next"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__238547b5f82d740f9decd2daa684215e12eef3b20ceba1c57a25013623ea6912)
                check_type(argname="argument attribute", value=attribute, expected_type=type_hints["attribute"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument thing_name", value=thing_name, expected_type=type_hints["thing_name"])
                check_type(argname="argument next", value=next, expected_type=type_hints["next"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "attribute": attribute,
                "name": name,
                "role_arn": role_arn,
                "thing_name": thing_name,
            }
            if next is not None:
                self._values["next"] = next

        @builtins.property
        def attribute(self) -> builtins.str:
            '''The name of the attribute that is added to the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceshadowenrich.html#cfn-iotanalytics-pipeline-deviceshadowenrich-attribute
            '''
            result = self._values.get("attribute")
            assert result is not None, "Required property 'attribute' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the 'deviceShadowEnrich' activity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceshadowenrich.html#cfn-iotanalytics-pipeline-deviceshadowenrich-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the role that allows access to the device's shadow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceshadowenrich.html#cfn-iotanalytics-pipeline-deviceshadowenrich-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def thing_name(self) -> builtins.str:
            '''The name of the IoT device whose shadow information is added to the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceshadowenrich.html#cfn-iotanalytics-pipeline-deviceshadowenrich-thingname
            '''
            result = self._values.get("thing_name")
            assert result is not None, "Required property 'thing_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def next(self) -> typing.Optional[builtins.str]:
            '''The next activity in the pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-deviceshadowenrich.html#cfn-iotanalytics-pipeline-deviceshadowenrich-next
            '''
            result = self._values.get("next")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeviceShadowEnrichProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnPipeline.FilterProperty",
        jsii_struct_bases=[],
        name_mapping={"filter": "filter", "name": "name", "next": "next"},
    )
    class FilterProperty:
        def __init__(
            self,
            *,
            filter: builtins.str,
            name: builtins.str,
            next: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An activity that filters a message based on its attributes.

            :param filter: An expression that looks like an SQL WHERE clause that must return a Boolean value.
            :param name: The name of the 'filter' activity.
            :param next: The next activity in the pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-filter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                filter_property = iotanalytics.CfnPipeline.FilterProperty(
                    filter="filter",
                    name="name",
                
                    # the properties below are optional
                    next="next"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fce5e1ced04c8cd77e578566bbf673533674f03ccaca5a51a4e2fbf22c107f89)
                check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument next", value=next, expected_type=type_hints["next"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "filter": filter,
                "name": name,
            }
            if next is not None:
                self._values["next"] = next

        @builtins.property
        def filter(self) -> builtins.str:
            '''An expression that looks like an SQL WHERE clause that must return a Boolean value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-filter.html#cfn-iotanalytics-pipeline-filter-filter
            '''
            result = self._values.get("filter")
            assert result is not None, "Required property 'filter' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the 'filter' activity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-filter.html#cfn-iotanalytics-pipeline-filter-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def next(self) -> typing.Optional[builtins.str]:
            '''The next activity in the pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-filter.html#cfn-iotanalytics-pipeline-filter-next
            '''
            result = self._values.get("next")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnPipeline.LambdaProperty",
        jsii_struct_bases=[],
        name_mapping={
            "batch_size": "batchSize",
            "lambda_name": "lambdaName",
            "name": "name",
            "next": "next",
        },
    )
    class LambdaProperty:
        def __init__(
            self,
            *,
            batch_size: jsii.Number,
            lambda_name: builtins.str,
            name: builtins.str,
            next: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An activity that runs a Lambda function to modify the message.

            :param batch_size: The number of messages passed to the Lambda function for processing. The AWS Lambda function must be able to process all of these messages within five minutes, which is the maximum timeout duration for Lambda functions.
            :param lambda_name: The name of the Lambda function that is run on the message.
            :param name: The name of the 'lambda' activity.
            :param next: The next activity in the pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-lambda.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                lambda_property = iotanalytics.CfnPipeline.LambdaProperty(
                    batch_size=123,
                    lambda_name="lambdaName",
                    name="name",
                
                    # the properties below are optional
                    next="next"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7a41aece7bf831b1c610498ba55a2613cabc289252a5e07c031e2e862b348bdb)
                check_type(argname="argument batch_size", value=batch_size, expected_type=type_hints["batch_size"])
                check_type(argname="argument lambda_name", value=lambda_name, expected_type=type_hints["lambda_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument next", value=next, expected_type=type_hints["next"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "batch_size": batch_size,
                "lambda_name": lambda_name,
                "name": name,
            }
            if next is not None:
                self._values["next"] = next

        @builtins.property
        def batch_size(self) -> jsii.Number:
            '''The number of messages passed to the Lambda function for processing.

            The AWS Lambda function must be able to process all of these messages within five minutes, which is the maximum timeout duration for Lambda functions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-lambda.html#cfn-iotanalytics-pipeline-lambda-batchsize
            '''
            result = self._values.get("batch_size")
            assert result is not None, "Required property 'batch_size' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def lambda_name(self) -> builtins.str:
            '''The name of the Lambda function that is run on the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-lambda.html#cfn-iotanalytics-pipeline-lambda-lambdaname
            '''
            result = self._values.get("lambda_name")
            assert result is not None, "Required property 'lambda_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the 'lambda' activity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-lambda.html#cfn-iotanalytics-pipeline-lambda-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def next(self) -> typing.Optional[builtins.str]:
            '''The next activity in the pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-lambda.html#cfn-iotanalytics-pipeline-lambda-next
            '''
            result = self._values.get("next")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnPipeline.MathProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attribute": "attribute",
            "math": "math",
            "name": "name",
            "next": "next",
        },
    )
    class MathProperty:
        def __init__(
            self,
            *,
            attribute: builtins.str,
            math: builtins.str,
            name: builtins.str,
            next: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An activity that computes an arithmetic expression using the message's attributes.

            :param attribute: The name of the attribute that contains the result of the math operation.
            :param math: An expression that uses one or more existing attributes and must return an integer value.
            :param name: The name of the 'math' activity.
            :param next: The next activity in the pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-math.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                math_property = iotanalytics.CfnPipeline.MathProperty(
                    attribute="attribute",
                    math="math",
                    name="name",
                
                    # the properties below are optional
                    next="next"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__52044f730cde3bad7e4f1fe2489cebfa7f8cf5458d1dc0df0c40d654605edfbe)
                check_type(argname="argument attribute", value=attribute, expected_type=type_hints["attribute"])
                check_type(argname="argument math", value=math, expected_type=type_hints["math"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument next", value=next, expected_type=type_hints["next"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "attribute": attribute,
                "math": math,
                "name": name,
            }
            if next is not None:
                self._values["next"] = next

        @builtins.property
        def attribute(self) -> builtins.str:
            '''The name of the attribute that contains the result of the math operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-math.html#cfn-iotanalytics-pipeline-math-attribute
            '''
            result = self._values.get("attribute")
            assert result is not None, "Required property 'attribute' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def math(self) -> builtins.str:
            '''An expression that uses one or more existing attributes and must return an integer value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-math.html#cfn-iotanalytics-pipeline-math-math
            '''
            result = self._values.get("math")
            assert result is not None, "Required property 'math' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the 'math' activity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-math.html#cfn-iotanalytics-pipeline-math-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def next(self) -> typing.Optional[builtins.str]:
            '''The next activity in the pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-math.html#cfn-iotanalytics-pipeline-math-next
            '''
            result = self._values.get("next")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MathProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnPipeline.RemoveAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={"attributes": "attributes", "name": "name", "next": "next"},
    )
    class RemoveAttributesProperty:
        def __init__(
            self,
            *,
            attributes: typing.Sequence[builtins.str],
            name: builtins.str,
            next: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An activity that removes attributes from a message.

            :param attributes: A list of 1-50 attributes to remove from the message.
            :param name: The name of the 'removeAttributes' activity.
            :param next: The next activity in the pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-removeattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                remove_attributes_property = iotanalytics.CfnPipeline.RemoveAttributesProperty(
                    attributes=["attributes"],
                    name="name",
                
                    # the properties below are optional
                    next="next"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c15acf91d20002f60f78f9cf42f80d60fee07f455177f4c7632340d5238dc5d1)
                check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument next", value=next, expected_type=type_hints["next"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "attributes": attributes,
                "name": name,
            }
            if next is not None:
                self._values["next"] = next

        @builtins.property
        def attributes(self) -> typing.List[builtins.str]:
            '''A list of 1-50 attributes to remove from the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-removeattributes.html#cfn-iotanalytics-pipeline-removeattributes-attributes
            '''
            result = self._values.get("attributes")
            assert result is not None, "Required property 'attributes' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the 'removeAttributes' activity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-removeattributes.html#cfn-iotanalytics-pipeline-removeattributes-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def next(self) -> typing.Optional[builtins.str]:
            '''The next activity in the pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-removeattributes.html#cfn-iotanalytics-pipeline-removeattributes-next
            '''
            result = self._values.get("next")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RemoveAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotanalytics.CfnPipeline.SelectAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={"attributes": "attributes", "name": "name", "next": "next"},
    )
    class SelectAttributesProperty:
        def __init__(
            self,
            *,
            attributes: typing.Sequence[builtins.str],
            name: builtins.str,
            next: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Creates a new message using only the specified attributes from the original message.

            :param attributes: A list of the attributes to select from the message.
            :param name: The name of the 'selectAttributes' activity.
            :param next: The next activity in the pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-selectattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotanalytics as iotanalytics
                
                select_attributes_property = iotanalytics.CfnPipeline.SelectAttributesProperty(
                    attributes=["attributes"],
                    name="name",
                
                    # the properties below are optional
                    next="next"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__32451c3e1df1197b5950a71e851820554a3321946c3ba2be585d73c0f775527b)
                check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument next", value=next, expected_type=type_hints["next"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "attributes": attributes,
                "name": name,
            }
            if next is not None:
                self._values["next"] = next

        @builtins.property
        def attributes(self) -> typing.List[builtins.str]:
            '''A list of the attributes to select from the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-selectattributes.html#cfn-iotanalytics-pipeline-selectattributes-attributes
            '''
            result = self._values.get("attributes")
            assert result is not None, "Required property 'attributes' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the 'selectAttributes' activity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-selectattributes.html#cfn-iotanalytics-pipeline-selectattributes-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def next(self) -> typing.Optional[builtins.str]:
            '''The next activity in the pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-selectattributes.html#cfn-iotanalytics-pipeline-selectattributes-next
            '''
            result = self._values.get("next")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SelectAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotanalytics.CfnPipelineProps",
    jsii_struct_bases=[],
    name_mapping={
        "pipeline_activities": "pipelineActivities",
        "pipeline_name": "pipelineName",
        "tags": "tags",
    },
)
class CfnPipelineProps:
    def __init__(
        self,
        *,
        pipeline_activities: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipeline.ActivityProperty, typing.Dict[builtins.str, typing.Any]]]]],
        pipeline_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPipeline``.

        :param pipeline_activities: A list of "PipelineActivity" objects. Activities perform transformations on your messages, such as removing, renaming or adding message attributes; filtering messages based on attribute values; invoking your Lambda functions on messages for advanced processing; or performing mathematical transformations to normalize device data. The list can be 2-25 *PipelineActivity* objects and must contain both a ``channel`` and a ``datastore`` activity. Each entry in the list must contain only one activity, for example: ``pipelineActivities = [ { "channel": { ... } }, { "lambda": { ... } }, ... ]``
        :param pipeline_name: The name of the pipeline.
        :param tags: Metadata which can be used to manage the pipeline. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-pipeline.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotanalytics as iotanalytics
            
            cfn_pipeline_props = iotanalytics.CfnPipelineProps(
                pipeline_activities=[iotanalytics.CfnPipeline.ActivityProperty(
                    add_attributes=iotanalytics.CfnPipeline.AddAttributesProperty(
                        attributes={
                            "attributes_key": "attributes"
                        },
                        name="name",
            
                        # the properties below are optional
                        next="next"
                    ),
                    channel=iotanalytics.CfnPipeline.ChannelProperty(
                        channel_name="channelName",
                        name="name",
            
                        # the properties below are optional
                        next="next"
                    ),
                    datastore=iotanalytics.CfnPipeline.DatastoreProperty(
                        datastore_name="datastoreName",
                        name="name"
                    ),
                    device_registry_enrich=iotanalytics.CfnPipeline.DeviceRegistryEnrichProperty(
                        attribute="attribute",
                        name="name",
                        role_arn="roleArn",
                        thing_name="thingName",
            
                        # the properties below are optional
                        next="next"
                    ),
                    device_shadow_enrich=iotanalytics.CfnPipeline.DeviceShadowEnrichProperty(
                        attribute="attribute",
                        name="name",
                        role_arn="roleArn",
                        thing_name="thingName",
            
                        # the properties below are optional
                        next="next"
                    ),
                    filter=iotanalytics.CfnPipeline.FilterProperty(
                        filter="filter",
                        name="name",
            
                        # the properties below are optional
                        next="next"
                    ),
                    lambda_=iotanalytics.CfnPipeline.LambdaProperty(
                        batch_size=123,
                        lambda_name="lambdaName",
                        name="name",
            
                        # the properties below are optional
                        next="next"
                    ),
                    math=iotanalytics.CfnPipeline.MathProperty(
                        attribute="attribute",
                        math="math",
                        name="name",
            
                        # the properties below are optional
                        next="next"
                    ),
                    remove_attributes=iotanalytics.CfnPipeline.RemoveAttributesProperty(
                        attributes=["attributes"],
                        name="name",
            
                        # the properties below are optional
                        next="next"
                    ),
                    select_attributes=iotanalytics.CfnPipeline.SelectAttributesProperty(
                        attributes=["attributes"],
                        name="name",
            
                        # the properties below are optional
                        next="next"
                    )
                )],
            
                # the properties below are optional
                pipeline_name="pipelineName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f679c4a07101956552f6a581e512ccc717093dd11033f5cba9e585cec9333ef)
            check_type(argname="argument pipeline_activities", value=pipeline_activities, expected_type=type_hints["pipeline_activities"])
            check_type(argname="argument pipeline_name", value=pipeline_name, expected_type=type_hints["pipeline_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pipeline_activities": pipeline_activities,
        }
        if pipeline_name is not None:
            self._values["pipeline_name"] = pipeline_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def pipeline_activities(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPipeline.ActivityProperty]]]:
        '''A list of "PipelineActivity" objects.

        Activities perform transformations on your messages, such as removing, renaming or adding message attributes; filtering messages based on attribute values; invoking your Lambda functions on messages for advanced processing; or performing mathematical transformations to normalize device data.

        The list can be 2-25 *PipelineActivity* objects and must contain both a ``channel`` and a ``datastore`` activity. Each entry in the list must contain only one activity, for example:

        ``pipelineActivities = [ { "channel": { ... } }, { "lambda": { ... } }, ... ]``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-pipeline.html#cfn-iotanalytics-pipeline-pipelineactivities
        '''
        result = self._values.get("pipeline_activities")
        assert result is not None, "Required property 'pipeline_activities' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPipeline.ActivityProperty]]], result)

    @builtins.property
    def pipeline_name(self) -> typing.Optional[builtins.str]:
        '''The name of the pipeline.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-pipeline.html#cfn-iotanalytics-pipeline-pipelinename
        '''
        result = self._values.get("pipeline_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Metadata which can be used to manage the pipeline.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-pipeline.html#cfn-iotanalytics-pipeline-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPipelineProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnChannel",
    "CfnChannelProps",
    "CfnDataset",
    "CfnDatasetProps",
    "CfnDatastore",
    "CfnDatastoreProps",
    "CfnPipeline",
    "CfnPipelineProps",
]

publication.publish()

def _typecheckingstub__8332c208b00865f2cfdad255e86ebeabe2b2b68a70b8fa26b96ec9b8c1e25499(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    channel_name: typing.Optional[builtins.str] = None,
    channel_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.ChannelStorageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retention_period: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.RetentionPeriodProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3afdfadc9a4edd9b5c35f5d06ae9f61c5c1ebaa012686da4a923c736b3fa979b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e6a928cd907de244850e605fb376bc7dc51306fe95d12a79b27dbb27038d241(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65896b87ac00168069b3023b993de25e4b6e0d2f7062c80b2bd040584f8e7e1c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__897830b597b7f068ad39137a599c6bcc3329380b80a31c457e181b64e3c87677(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnChannel.ChannelStorageProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e6072ad5478c8c43508f65ecec006c8dfe38ec650f0a67eb9970771e8d1484e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnChannel.RetentionPeriodProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32eb80eb4a923d8935d89ce4d4e01a0cfaf3d7c894b3102ee7c33c63cf554635(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbc8b32257128c3df6a233f408369201793dc955662fe4cece76a7bdcaec3ecd(
    *,
    customer_managed_s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.CustomerManagedS3Property, typing.Dict[builtins.str, typing.Any]]]] = None,
    service_managed_s3: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44d2e287ab890d34114c77aaedf5da8bf78be529b28b900b0f298f1e6f2eca2e(
    *,
    bucket: builtins.str,
    role_arn: builtins.str,
    key_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c61da11bbb4ca5d43e4fd9639491db4447e4c3f71df13bf8e176559eab373cb2(
    *,
    number_of_days: typing.Optional[jsii.Number] = None,
    unlimited: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1389944a7a7c5ae7ccfca31343abcc6dd4bb78b250fa7c33a3787f169cd7fdb3(
    *,
    channel_name: typing.Optional[builtins.str] = None,
    channel_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.ChannelStorageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retention_period: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.RetentionPeriodProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28e622d1f32fa52fab95276ceeda7ad3576bf8992514bb441ca9b4ec4c53e656(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    actions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.ActionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    content_delivery_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.DatasetContentDeliveryRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    dataset_name: typing.Optional[builtins.str] = None,
    late_data_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.LateDataRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    retention_period: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.RetentionPeriodProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    triggers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.TriggerProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    versioning_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.VersioningConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f43abe364fcb83fda3cc5c4f98b2e4482fe72474205d310be98d8daa35ad70e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__022ee74ca256ae166d4ad18e647fce9936f9dc0446dac904fa6bfc5c57e0d328(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bea1d7db65ef2e1dd07cc6ad0511bc305600ada926a081f4afb5441eab9862f9(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataset.ActionProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1191be1b889318deb878087580e18a33f2b1eb69287f1988f9589d01097e71d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataset.DatasetContentDeliveryRuleProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e08086740a66aa7f8dc6e47ec6c22172a3100d1ca2502cf801db5c180d0a6d13(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bc1deb3c6d08c1c1ca7ffa721da938a0b604bf7e64fde45dd87c4e7478ce691(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataset.LateDataRuleProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36003a82d5901d6085a6056449c0d0dae73bc495f138ce413f2a3940ca19669c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataset.RetentionPeriodProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__201d27101e415eb7f1fb30604fdbd5f5dab782974340b049d78678175f90e844(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db66da5cbfc6b7c7e9db0e44713028b1f68bef47ecead6ba507500a1bc85c1d1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDataset.TriggerProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1446f217595acd6056460044992a066513ba69220f2ecb77d8dc7122679ac975(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataset.VersioningConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3c3351641f2ce5cf26f289df6ae1a9b894c17bc061f16ff20ea18c0dab7ba8a(
    *,
    action_name: builtins.str,
    container_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.ContainerActionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    query_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.QueryActionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6242d8a947c41a4804fe02dc984b064df367b06752dc26316c0ae4eca8f5075d(
    *,
    execution_role_arn: builtins.str,
    image: builtins.str,
    resource_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.ResourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.VariableProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fa6d9df2b2748545080f3145accff6d8b456a3f97c1e9f9a1f20b39000073b3(
    *,
    iot_events_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.IotEventsDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f19bbb35f806c8e28f81b57dec9b64e4ce3204e27bd015c548f0bbba4ed1001(
    *,
    destination: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.DatasetContentDeliveryRuleDestinationProperty, typing.Dict[builtins.str, typing.Any]]],
    entry_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9627e37a604313ddab69d513bf6df569a93f856ba451e38f6882334fb43968b8(
    *,
    dataset_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be02cd80d95071c31b45ce101d8562e196ddc6e85436afb5709305d83e344d41(
    *,
    offset_seconds: jsii.Number,
    time_expression: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb8e8f18aa3ead62f5ae202a1709d61bdf2b12ef7326a6cf4ff2263f0a7eff1a(
    *,
    timeout_in_minutes: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfd8c6d60abf268a0c3bab812403ca3b57768d51d4c8d5e8797b17c47d006a0a(
    *,
    delta_time: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.DeltaTimeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66cdd212b38725bdb16f7222a75d297d4b793a295ab37b2fc13715220449280c(
    *,
    database_name: builtins.str,
    table_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__846e71e501ac1e6310b413155464156cb586e0fd915c8ac73e9992c0c401c16a(
    *,
    input_name: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea0a5734ae5d70864971efc665d2a95b42f5f7fb3ccc748bd86497539309ed35(
    *,
    delta_time_session_window_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.DeltaTimeSessionWindowConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fa8dab9d3a3aa7ec10a97f6790a0d96684a968619f309c9c509577e2d399f1e(
    *,
    rule_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.LateDataRuleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    rule_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40ca34490c1eeedddc3e02770d487e08b263b4c1b33b1e11d3bff8beed84028f(
    *,
    file_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de5c5b0c96d44386f201894780b99dc31af0d8ffa106e6450f8d677406e216a6(
    *,
    sql_query: builtins.str,
    filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.FilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4caca4363dbddfd7d8d63d5ed7437e9806b6f864fd4ce7d7a3d9ae4d12c2026c(
    *,
    compute_type: builtins.str,
    volume_size_in_gb: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f25a34ec948131db017888ecc72a87f38ca9edc34e4f905c095fe6219d526f82(
    *,
    number_of_days: typing.Optional[jsii.Number] = None,
    unlimited: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42695c1832b8cae8c36043ce30de17800b72e233c2b6e6377d8eb3deede70de3(
    *,
    bucket: builtins.str,
    key: builtins.str,
    role_arn: builtins.str,
    glue_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.GlueConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e00f7c2fafca878429e43d7ef3e7f43c6570a720c615402abbda3393f274b96(
    *,
    schedule_expression: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f8d91baeba7735ed150f70716898211ad99b3281e2fb4199bfb4b2dede3f363(
    *,
    schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    triggering_dataset: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.TriggeringDatasetProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a822098e3c67a5eb69596bd59484a55a8e0ac97e0694746c6488c191c5e2eda(
    *,
    dataset_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f442efcc6fc67ff4c6b32b902bffe3a1e716ab6fa19002d570fdd99768219b7(
    *,
    variable_name: builtins.str,
    dataset_content_version_value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.DatasetContentVersionValueProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    double_value: typing.Optional[jsii.Number] = None,
    output_file_uri_value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.OutputFileUriValueProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    string_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44ef2d0f147e3d91be95ed97931f9fe1fdbe66142e58213b3dda686e0a38729a(
    *,
    max_versions: typing.Optional[jsii.Number] = None,
    unlimited: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba482b4c89e3977548d923f68d372a4195ddedc9b62d05ec8d5000808561e994(
    *,
    actions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.ActionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    content_delivery_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.DatasetContentDeliveryRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    dataset_name: typing.Optional[builtins.str] = None,
    late_data_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.LateDataRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    retention_period: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.RetentionPeriodProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    triggers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.TriggerProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    versioning_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataset.VersioningConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80888194774a160a9eb52d698126a6fd1e7e99768082595c8f4810a89813f3c1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    datastore_name: typing.Optional[builtins.str] = None,
    datastore_partitions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatastore.DatastorePartitionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    datastore_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatastore.DatastoreStorageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    file_format_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatastore.FileFormatConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retention_period: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatastore.RetentionPeriodProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ade56a7c5d6431a16dde38053efe2001ac1c8ab06985988a23a00267d80a5a16(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94c0a67e5e4c43aa44435879b4f1b63ef3b5102e13736181e9448de1796ed206(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__081a53e062ad7ea5c2f6ecb7ebbccac62478ecd868806928c47c7eb98ae61d0b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bcc26ed136adb3f4c32488bcb2844b209ec226cd795eb2c0cea62ded0053c40(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDatastore.DatastorePartitionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe446f198ffdaea0dc4c9d93e32d3c1aec9b88e8f422a0ce06659dba6598ae0f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDatastore.DatastoreStorageProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bc9a7886f31a213d5c1836b73e8f3e9697e0e07f52f23623adfd569fa72c125(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDatastore.FileFormatConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__032263fee34119301fc0a40c33438ae261f79f8664628d410d34905ede484924(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDatastore.RetentionPeriodProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09e62e46bc734f5ed26f36e04b2552fae780df1bd2f0edbb6b1492d2e5a21d03(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ae2b1794960971e3043a45488ed7248bf5111d4413a143e8d852de963f225b3(
    *,
    name: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4068d1c6245c24c4ab2ad550651845d10e8e4ccaf674e9cd3b91ccf9fcb5405(
    *,
    bucket: builtins.str,
    role_arn: builtins.str,
    key_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35524e38307a14aa06cb90fa741a954b5439d4d8f6f5e9f4f8d8ba9fe80348a6(
    *,
    bucket: builtins.str,
    key_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbd39480bd26262bd30c3905cca3a0643938b5db9c601cc7a1dcc0d73fb778dd(
    *,
    partition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatastore.PartitionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    timestamp_partition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatastore.TimestampPartitionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59a13ae3d10a02ccef29ab4c2489258358fa3aaf39021e87f7b7f0475d7924f5(
    *,
    partitions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatastore.DatastorePartitionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5984b7f9d7ba382e2b28022cc78b28dd28173cb76fb8b5cc637be3ee56ea2c81(
    *,
    customer_managed_s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatastore.CustomerManagedS3Property, typing.Dict[builtins.str, typing.Any]]]] = None,
    iot_site_wise_multi_layer_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatastore.IotSiteWiseMultiLayerStorageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    service_managed_s3: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0ed74456c35a181d6d6de607a0cba62b46dacd1b5841393ea8e579cde121ff1(
    *,
    json_configuration: typing.Any = None,
    parquet_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatastore.ParquetConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f347023ec67ebec701d0a7d67d19ead6d99d6ae0f1aa6aad2416fcce1d5e2591(
    *,
    customer_managed_s3_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatastore.CustomerManagedS3StorageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dea7c4dd001f38a8f0ea6dfa412735a2dab8f5b3cae0ed5309527fad8bee321e(
    *,
    schema_definition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatastore.SchemaDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__327e41bcdc4d9e40e80bb337f397b1df7c75d836745e92ad6753e1ccc8fa6ddd(
    *,
    attribute_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7f15bd2b6ccbd3452a9eccff4b8b3378d4efc6f30d6f60f6faed63b647a4c3c(
    *,
    number_of_days: typing.Optional[jsii.Number] = None,
    unlimited: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f36d43c7f1f6d356e648b26afe1feb2408dae7114d15163cf3465b0a94ba58e7(
    *,
    columns: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatastore.ColumnProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d43c9ee54cedeb8e135981f6b1b363d55973c05551571400829d3f5e2771731(
    *,
    attribute_name: builtins.str,
    timestamp_format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5e07deff1542b5d76f6fbec1b51b693bafafe7f15017228354ea52b83a2737b(
    *,
    datastore_name: typing.Optional[builtins.str] = None,
    datastore_partitions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatastore.DatastorePartitionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    datastore_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatastore.DatastoreStorageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    file_format_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatastore.FileFormatConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retention_period: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDatastore.RetentionPeriodProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__780e6e051f6bd102a51bd0b3de8f56cd44681953f4198d827460085558e2add9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    pipeline_activities: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipeline.ActivityProperty, typing.Dict[builtins.str, typing.Any]]]]],
    pipeline_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__405496d6c191e31df7bb8a63193cea61a5bf750f573ac5a5fede36aaa0994c7c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba374f9d6213ab4f683b1553c4a35de7e4a81680071121852d026b7cd734f359(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f91482ef32b46baa85edafca306dfc279654decbb3dc3b6968fd311f70972d4(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPipeline.ActivityProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54be44f48af8d45aa4b74df14476342f70be64a61ed9cc470a1a0efa37552b10(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb2cf7a7a3f0428848c668b76beea41674b32a79ad06a43cc68538235ba32f54(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef4301ffee8a8b9c56444ba866610802447f4507a483114152269c2d14b47821(
    *,
    add_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipeline.AddAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    channel: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipeline.ChannelProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    datastore: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipeline.DatastoreProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    device_registry_enrich: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipeline.DeviceRegistryEnrichProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    device_shadow_enrich: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipeline.DeviceShadowEnrichProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    filter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipeline.FilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    lambda_: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipeline.LambdaProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    math: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipeline.MathProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    remove_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipeline.RemoveAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    select_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipeline.SelectAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__577567edb1bcbc381086b32d827a8fa916777984a8a94532f921964c944864e3(
    *,
    attributes: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]],
    name: builtins.str,
    next: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__527444433b58193b6bbced07f46923ccbfa842f89d0abdfc358194e5d487ec43(
    *,
    channel_name: builtins.str,
    name: builtins.str,
    next: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3babb765a17ffb7f52df98d8cfac4d4ad731f21ae72df208b251bda410ab8786(
    *,
    datastore_name: builtins.str,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2800ea3a2b7d7d4294d7e2e6344a11b8cad32694fb315fc03efd00bc0505dc5(
    *,
    attribute: builtins.str,
    name: builtins.str,
    role_arn: builtins.str,
    thing_name: builtins.str,
    next: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__238547b5f82d740f9decd2daa684215e12eef3b20ceba1c57a25013623ea6912(
    *,
    attribute: builtins.str,
    name: builtins.str,
    role_arn: builtins.str,
    thing_name: builtins.str,
    next: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fce5e1ced04c8cd77e578566bbf673533674f03ccaca5a51a4e2fbf22c107f89(
    *,
    filter: builtins.str,
    name: builtins.str,
    next: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a41aece7bf831b1c610498ba55a2613cabc289252a5e07c031e2e862b348bdb(
    *,
    batch_size: jsii.Number,
    lambda_name: builtins.str,
    name: builtins.str,
    next: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52044f730cde3bad7e4f1fe2489cebfa7f8cf5458d1dc0df0c40d654605edfbe(
    *,
    attribute: builtins.str,
    math: builtins.str,
    name: builtins.str,
    next: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c15acf91d20002f60f78f9cf42f80d60fee07f455177f4c7632340d5238dc5d1(
    *,
    attributes: typing.Sequence[builtins.str],
    name: builtins.str,
    next: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32451c3e1df1197b5950a71e851820554a3321946c3ba2be585d73c0f775527b(
    *,
    attributes: typing.Sequence[builtins.str],
    name: builtins.str,
    next: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f679c4a07101956552f6a581e512ccc717093dd11033f5cba9e585cec9333ef(
    *,
    pipeline_activities: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipeline.ActivityProperty, typing.Dict[builtins.str, typing.Any]]]]],
    pipeline_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
