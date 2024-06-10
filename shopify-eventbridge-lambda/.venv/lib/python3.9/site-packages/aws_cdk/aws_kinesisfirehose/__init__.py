'''
# Amazon Kinesis Data Firehose Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_kinesisfirehose as kinesisfirehose
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for KinesisFirehose construct libraries](https://constructs.dev/search?q=kinesisfirehose)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::KinesisFirehose resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_KinesisFirehose.html) directly.

> An experimental construct library for this service is available in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-kinesisfirehose-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::KinesisFirehose](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_KinesisFirehose.html).

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
class CfnDeliveryStream(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream",
):
    '''The ``AWS::KinesisFirehose::DeliveryStream`` resource specifies an Amazon Kinesis Data Firehose (Kinesis Data Firehose) delivery stream that delivers real-time streaming data to an Amazon Simple Storage Service (Amazon S3), Amazon Redshift, or Amazon Elasticsearch Service (Amazon ES) destination.

    For more information, see `Creating an Amazon Kinesis Data Firehose Delivery Stream <https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html>`_ in the *Amazon Kinesis Data Firehose Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html
    :cloudformationResource: AWS::KinesisFirehose::DeliveryStream
    :exampleMetadata: infused

    Example::

        destination_bucket = s3.Bucket(self, "Bucket")
        delivery_stream_role = iam.Role(self, "Role",
            assumed_by=iam.ServicePrincipal("firehose.amazonaws.com")
        )
        
        stream = firehose.CfnDeliveryStream(self, "MyStream",
            delivery_stream_name="amazon-apigateway-delivery-stream",
            s3_destination_configuration=firehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                bucket_arn=destination_bucket.bucket_arn,
                role_arn=delivery_stream_role.role_arn
            )
        )
        
        api = apigateway.RestApi(self, "books",
            deploy_options=apigateway.StageOptions(
                access_log_destination=apigateway.FirehoseLogDestination(stream),
                access_log_format=apigateway.AccessLogFormat.json_with_standard_fields()
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        amazon_open_search_serverless_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.AmazonOpenSearchServerlessDestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        amazonopensearchservice_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        delivery_stream_encryption_configuration_input: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        delivery_stream_name: typing.Optional[builtins.str] = None,
        delivery_stream_type: typing.Optional[builtins.str] = None,
        elasticsearch_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        extended_s3_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        http_endpoint_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        kinesis_stream_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.KinesisStreamSourceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        msk_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.MSKSourceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        redshift_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.RedshiftDestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        s3_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.S3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        snowflake_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.SnowflakeDestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        splunk_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.SplunkDestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param amazon_open_search_serverless_destination_configuration: Describes the configuration of a destination in the Serverless offering for Amazon OpenSearch Service.
        :param amazonopensearchservice_destination_configuration: The destination in Amazon OpenSearch Service. You can specify only one destination.
        :param delivery_stream_encryption_configuration_input: Specifies the type and Amazon Resource Name (ARN) of the CMK to use for Server-Side Encryption (SSE).
        :param delivery_stream_name: The name of the delivery stream.
        :param delivery_stream_type: The delivery stream type. This can be one of the following values:. - ``DirectPut`` : Provider applications access the delivery stream directly. - ``KinesisStreamAsSource`` : The delivery stream uses a Kinesis data stream as a source.
        :param elasticsearch_destination_configuration: An Amazon ES destination for the delivery stream. Conditional. You must specify only one destination configuration. If you change the delivery stream destination from an Amazon ES destination to an Amazon S3 or Amazon Redshift destination, update requires `some interruptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt>`_ .
        :param extended_s3_destination_configuration: An Amazon S3 destination for the delivery stream. Conditional. You must specify only one destination configuration. If you change the delivery stream destination from an Amazon Extended S3 destination to an Amazon ES destination, update requires `some interruptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt>`_ .
        :param http_endpoint_destination_configuration: Enables configuring Kinesis Firehose to deliver data to any HTTP endpoint destination. You can specify only one destination.
        :param kinesis_stream_source_configuration: When a Kinesis stream is used as the source for the delivery stream, a `KinesisStreamSourceConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html>`_ containing the Kinesis stream ARN and the role ARN for the source stream.
        :param msk_source_configuration: The configuration for the Amazon MSK cluster to be used as the source for a delivery stream.
        :param redshift_destination_configuration: An Amazon Redshift destination for the delivery stream. Conditional. You must specify only one destination configuration. If you change the delivery stream destination from an Amazon Redshift destination to an Amazon ES destination, update requires `some interruptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt>`_ .
        :param s3_destination_configuration: The ``S3DestinationConfiguration`` property type specifies an Amazon Simple Storage Service (Amazon S3) destination to which Amazon Kinesis Data Firehose (Kinesis Data Firehose) delivers data. Conditional. You must specify only one destination configuration. If you change the delivery stream destination from an Amazon S3 destination to an Amazon ES destination, update requires `some interruptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt>`_ .
        :param snowflake_destination_configuration: Configure Snowflake destination.
        :param splunk_destination_configuration: The configuration of a destination in Splunk for the delivery stream.
        :param tags: A set of tags to assign to the delivery stream. A tag is a key-value pair that you can define and assign to AWS resources. Tags are metadata. For example, you can add friendly names and descriptions or other types of information that can help you distinguish the delivery stream. For more information about tags, see `Using Cost Allocation Tags <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`_ in the AWS Billing and Cost Management User Guide. You can specify up to 50 tags when creating a delivery stream. If you specify tags in the ``CreateDeliveryStream`` action, Amazon Data Firehose performs an additional authorization on the ``firehose:TagDeliveryStream`` action to verify if users have permissions to create tags. If you do not provide this permission, requests to create new Firehose delivery streams with IAM resource tags will fail with an ``AccessDeniedException`` such as following. *AccessDeniedException* User: arn:aws:sts::x:assumed-role/x/x is not authorized to perform: firehose:TagDeliveryStream on resource: arn:aws:firehose:us-east-1:x:deliverystream/x with an explicit deny in an identity-based policy. For an example IAM policy, see `Tag example. <https://docs.aws.amazon.com/firehose/latest/APIReference/API_CreateDeliveryStream.html#API_CreateDeliveryStream_Examples>`_
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3cd824a2680c7d043cac684bd1be9ca77e94201f1ba00785d60a50ff43c2288)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDeliveryStreamProps(
            amazon_open_search_serverless_destination_configuration=amazon_open_search_serverless_destination_configuration,
            amazonopensearchservice_destination_configuration=amazonopensearchservice_destination_configuration,
            delivery_stream_encryption_configuration_input=delivery_stream_encryption_configuration_input,
            delivery_stream_name=delivery_stream_name,
            delivery_stream_type=delivery_stream_type,
            elasticsearch_destination_configuration=elasticsearch_destination_configuration,
            extended_s3_destination_configuration=extended_s3_destination_configuration,
            http_endpoint_destination_configuration=http_endpoint_destination_configuration,
            kinesis_stream_source_configuration=kinesis_stream_source_configuration,
            msk_source_configuration=msk_source_configuration,
            redshift_destination_configuration=redshift_destination_configuration,
            s3_destination_configuration=s3_destination_configuration,
            snowflake_destination_configuration=snowflake_destination_configuration,
            splunk_destination_configuration=splunk_destination_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f6206943f45cc34824996fe47b775be3c1a09cb74450254dfa716bc71a96a69)
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
            type_hints = typing.get_type_hints(_typecheckingstub__822762453b1edc05d278fe4b56cb34de36a63cda89772b6624160f6ac406e7e7)
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
        '''The Amazon Resource Name (ARN) of the delivery stream, such as ``arn:aws:firehose:us-east-2:123456789012:deliverystream/delivery-stream-name`` .

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
    @jsii.member(jsii_name="amazonOpenSearchServerlessDestinationConfiguration")
    def amazon_open_search_serverless_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonOpenSearchServerlessDestinationConfigurationProperty"]]:
        '''Describes the configuration of a destination in the Serverless offering for Amazon OpenSearch Service.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonOpenSearchServerlessDestinationConfigurationProperty"]], jsii.get(self, "amazonOpenSearchServerlessDestinationConfiguration"))

    @amazon_open_search_serverless_destination_configuration.setter
    def amazon_open_search_serverless_destination_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonOpenSearchServerlessDestinationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9361f4405d0a8e9a0285d4b343c6420073eedc822c339d1a147f151a3b03f641)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "amazonOpenSearchServerlessDestinationConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="amazonopensearchserviceDestinationConfiguration")
    def amazonopensearchservice_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty"]]:
        '''The destination in Amazon OpenSearch Service.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty"]], jsii.get(self, "amazonopensearchserviceDestinationConfiguration"))

    @amazonopensearchservice_destination_configuration.setter
    def amazonopensearchservice_destination_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58964b8831d37cbba22a48328508a0d1fc866bb6da992a0c3f544fc6649acc5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "amazonopensearchserviceDestinationConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamEncryptionConfigurationInput")
    def delivery_stream_encryption_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty"]]:
        '''Specifies the type and Amazon Resource Name (ARN) of the CMK to use for Server-Side Encryption (SSE).'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty"]], jsii.get(self, "deliveryStreamEncryptionConfigurationInput"))

    @delivery_stream_encryption_configuration_input.setter
    def delivery_stream_encryption_configuration_input(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b541613844a306d329ee6aaf12a513672a01cea651f015810fd2ab896394415)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryStreamEncryptionConfigurationInput", value)

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamName")
    def delivery_stream_name(self) -> typing.Optional[builtins.str]:
        '''The name of the delivery stream.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryStreamName"))

    @delivery_stream_name.setter
    def delivery_stream_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d90731f57c337a34bb7290e3bb4239e949b5caeea354433c46c25998a03b39f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryStreamName", value)

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamType")
    def delivery_stream_type(self) -> typing.Optional[builtins.str]:
        '''The delivery stream type.

        This can be one of the following values:.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deliveryStreamType"))

    @delivery_stream_type.setter
    def delivery_stream_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0749b7e1cb2e266044df272e646eba4d2505c56ccb68f4ce96de186aeb83ba9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryStreamType", value)

    @builtins.property
    @jsii.member(jsii_name="elasticsearchDestinationConfiguration")
    def elasticsearch_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty"]]:
        '''An Amazon ES destination for the delivery stream.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty"]], jsii.get(self, "elasticsearchDestinationConfiguration"))

    @elasticsearch_destination_configuration.setter
    def elasticsearch_destination_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2485fd6e8467da83435abf801383e98fea4d4ae9797551e1774f2327e1b069c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticsearchDestinationConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="extendedS3DestinationConfiguration")
    def extended_s3_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty"]]:
        '''An Amazon S3 destination for the delivery stream.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty"]], jsii.get(self, "extendedS3DestinationConfiguration"))

    @extended_s3_destination_configuration.setter
    def extended_s3_destination_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b3827d67811452e6783eeef4d719d420c5534229b93597dbfafa7256a89932e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extendedS3DestinationConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="httpEndpointDestinationConfiguration")
    def http_endpoint_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty"]]:
        '''Enables configuring Kinesis Firehose to deliver data to any HTTP endpoint destination.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty"]], jsii.get(self, "httpEndpointDestinationConfiguration"))

    @http_endpoint_destination_configuration.setter
    def http_endpoint_destination_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c45396814a2f1f16d85b99c121f14ab851eda0a9f84038025d5ae44a858837a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpEndpointDestinationConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="kinesisStreamSourceConfiguration")
    def kinesis_stream_source_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.KinesisStreamSourceConfigurationProperty"]]:
        '''When a Kinesis stream is used as the source for the delivery stream, a `KinesisStreamSourceConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html>`_ containing the Kinesis stream ARN and the role ARN for the source stream.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.KinesisStreamSourceConfigurationProperty"]], jsii.get(self, "kinesisStreamSourceConfiguration"))

    @kinesis_stream_source_configuration.setter
    def kinesis_stream_source_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.KinesisStreamSourceConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__025f54a26e52ce42f679eff3aa8b95a5fee2e0e5b3aba7c4320f9900690e60b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kinesisStreamSourceConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="mskSourceConfiguration")
    def msk_source_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.MSKSourceConfigurationProperty"]]:
        '''The configuration for the Amazon MSK cluster to be used as the source for a delivery stream.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.MSKSourceConfigurationProperty"]], jsii.get(self, "mskSourceConfiguration"))

    @msk_source_configuration.setter
    def msk_source_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.MSKSourceConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d05261de796c66b290d3bf9493dedca3a4f904726566b1e0d28cd6f7e525757)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mskSourceConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="redshiftDestinationConfiguration")
    def redshift_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.RedshiftDestinationConfigurationProperty"]]:
        '''An Amazon Redshift destination for the delivery stream.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.RedshiftDestinationConfigurationProperty"]], jsii.get(self, "redshiftDestinationConfiguration"))

    @redshift_destination_configuration.setter
    def redshift_destination_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.RedshiftDestinationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9283febc90a4404b9eb41b227b6baf567d66cf4929f4f56dc67252a81e997f1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redshiftDestinationConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="s3DestinationConfiguration")
    def s3_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]]:
        '''The ``S3DestinationConfiguration`` property type specifies an Amazon Simple Storage Service (Amazon S3) destination to which Amazon Kinesis Data Firehose (Kinesis Data Firehose) delivers data.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]], jsii.get(self, "s3DestinationConfiguration"))

    @s3_destination_configuration.setter
    def s3_destination_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb8b949ac7c9700a5ef03cddf3b3be451041166fe7583faee720a903b17ffd7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3DestinationConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="snowflakeDestinationConfiguration")
    def snowflake_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SnowflakeDestinationConfigurationProperty"]]:
        '''Configure Snowflake destination.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SnowflakeDestinationConfigurationProperty"]], jsii.get(self, "snowflakeDestinationConfiguration"))

    @snowflake_destination_configuration.setter
    def snowflake_destination_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SnowflakeDestinationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4334e067c783ee048616b856f03ad5fb828c1a4c18bbdce130d9850ac2ce4034)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snowflakeDestinationConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="splunkDestinationConfiguration")
    def splunk_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SplunkDestinationConfigurationProperty"]]:
        '''The configuration of a destination in Splunk for the delivery stream.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SplunkDestinationConfigurationProperty"]], jsii.get(self, "splunkDestinationConfiguration"))

    @splunk_destination_configuration.setter
    def splunk_destination_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SplunkDestinationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1143a0f5e018d10fdc1fff0bbcada0e3653e2264078be8b5a6441f6918b95c91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "splunkDestinationConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A set of tags to assign to the delivery stream.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b611aca673873100e4f1f1366dada7f80beaecdafd39582bd00fb48881dca276)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.AmazonOpenSearchServerlessBufferingHintsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "interval_in_seconds": "intervalInSeconds",
            "size_in_m_bs": "sizeInMBs",
        },
    )
    class AmazonOpenSearchServerlessBufferingHintsProperty:
        def __init__(
            self,
            *,
            interval_in_seconds: typing.Optional[jsii.Number] = None,
            size_in_m_bs: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes the buffering to perform before delivering data to the Serverless offering for Amazon OpenSearch Service destination.

            :param interval_in_seconds: Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes).
            :param size_in_m_bs: Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5. We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessbufferinghints.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                amazon_open_search_serverless_buffering_hints_property = kinesisfirehose.CfnDeliveryStream.AmazonOpenSearchServerlessBufferingHintsProperty(
                    interval_in_seconds=123,
                    size_in_mBs=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__73b3806edee327ffa718f826cdd3f2971c613586675003f856582bd7f9f0990b)
                check_type(argname="argument interval_in_seconds", value=interval_in_seconds, expected_type=type_hints["interval_in_seconds"])
                check_type(argname="argument size_in_m_bs", value=size_in_m_bs, expected_type=type_hints["size_in_m_bs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if interval_in_seconds is not None:
                self._values["interval_in_seconds"] = interval_in_seconds
            if size_in_m_bs is not None:
                self._values["size_in_m_bs"] = size_in_m_bs

        @builtins.property
        def interval_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination.

            The default value is 300 (5 minutes).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessbufferinghints.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessbufferinghints-intervalinseconds
            '''
            result = self._values.get("interval_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def size_in_m_bs(self) -> typing.Optional[jsii.Number]:
            '''Buffer incoming data to the specified size, in MBs, before delivering it to the destination.

            The default value is 5.

            We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessbufferinghints.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessbufferinghints-sizeinmbs
            '''
            result = self._values.get("size_in_m_bs")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmazonOpenSearchServerlessBufferingHintsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.AmazonOpenSearchServerlessDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "index_name": "indexName",
            "role_arn": "roleArn",
            "s3_configuration": "s3Configuration",
            "buffering_hints": "bufferingHints",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "collection_endpoint": "collectionEndpoint",
            "processing_configuration": "processingConfiguration",
            "retry_options": "retryOptions",
            "s3_backup_mode": "s3BackupMode",
            "vpc_configuration": "vpcConfiguration",
        },
    )
    class AmazonOpenSearchServerlessDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            index_name: builtins.str,
            role_arn: builtins.str,
            s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.S3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.AmazonOpenSearchServerlessBufferingHintsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.CloudWatchLoggingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            collection_endpoint: typing.Optional[builtins.str] = None,
            processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ProcessingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.AmazonOpenSearchServerlessRetryOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_backup_mode: typing.Optional[builtins.str] = None,
            vpc_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.VpcConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes the configuration of a destination in the Serverless offering for Amazon OpenSearch Service.

            :param index_name: The Serverless offering for Amazon OpenSearch Service index name.
            :param role_arn: The Amazon Resource Name (ARN) of the IAM role to be assumed by Firehose for calling the Serverless offering for Amazon OpenSearch Service Configuration API and for indexing documents.
            :param s3_configuration: 
            :param buffering_hints: The buffering options. If no value is specified, the default values for AmazonopensearchserviceBufferingHints are used.
            :param cloud_watch_logging_options: 
            :param collection_endpoint: The endpoint to use when communicating with the collection in the Serverless offering for Amazon OpenSearch Service.
            :param processing_configuration: 
            :param retry_options: The retry behavior in case Firehose is unable to deliver documents to the Serverless offering for Amazon OpenSearch Service. The default value is 300 (5 minutes).
            :param s3_backup_mode: Defines how documents should be delivered to Amazon S3. When it is set to FailedDocumentsOnly, Firehose writes any documents that could not be indexed to the configured Amazon S3 destination, with AmazonOpenSearchService-failed/ appended to the key prefix. When set to AllDocuments, Firehose delivers all incoming records to Amazon S3, and also writes failed documents with AmazonOpenSearchService-failed/ appended to the prefix.
            :param vpc_configuration: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                amazon_open_search_serverless_destination_configuration_property = kinesisfirehose.CfnDeliveryStream.AmazonOpenSearchServerlessDestinationConfigurationProperty(
                    index_name="indexName",
                    role_arn="roleArn",
                    s3_configuration=kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                        bucket_arn="bucketArn",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                            interval_in_seconds=123,
                            size_in_mBs=123
                        ),
                        cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                            enabled=False,
                            log_group_name="logGroupName",
                            log_stream_name="logStreamName"
                        ),
                        compression_format="compressionFormat",
                        encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                            kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                                awskms_key_arn="awskmsKeyArn"
                            ),
                            no_encryption_config="noEncryptionConfig"
                        ),
                        error_output_prefix="errorOutputPrefix",
                        prefix="prefix"
                    ),
                
                    # the properties below are optional
                    buffering_hints=kinesisfirehose.CfnDeliveryStream.AmazonOpenSearchServerlessBufferingHintsProperty(
                        interval_in_seconds=123,
                        size_in_mBs=123
                    ),
                    cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                        enabled=False,
                        log_group_name="logGroupName",
                        log_stream_name="logStreamName"
                    ),
                    collection_endpoint="collectionEndpoint",
                    processing_configuration=kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty(
                        enabled=False,
                        processors=[kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                            type="type",
                
                            # the properties below are optional
                            parameters=[kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                                parameter_name="parameterName",
                                parameter_value="parameterValue"
                            )]
                        )]
                    ),
                    retry_options=kinesisfirehose.CfnDeliveryStream.AmazonOpenSearchServerlessRetryOptionsProperty(
                        duration_in_seconds=123
                    ),
                    s3_backup_mode="s3BackupMode",
                    vpc_configuration=kinesisfirehose.CfnDeliveryStream.VpcConfigurationProperty(
                        role_arn="roleArn",
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c09d95c569c785593bec028509479a3c62ff0333544fe7fb6ea165082930dcf0)
                check_type(argname="argument index_name", value=index_name, expected_type=type_hints["index_name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument s3_configuration", value=s3_configuration, expected_type=type_hints["s3_configuration"])
                check_type(argname="argument buffering_hints", value=buffering_hints, expected_type=type_hints["buffering_hints"])
                check_type(argname="argument cloud_watch_logging_options", value=cloud_watch_logging_options, expected_type=type_hints["cloud_watch_logging_options"])
                check_type(argname="argument collection_endpoint", value=collection_endpoint, expected_type=type_hints["collection_endpoint"])
                check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
                check_type(argname="argument retry_options", value=retry_options, expected_type=type_hints["retry_options"])
                check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
                check_type(argname="argument vpc_configuration", value=vpc_configuration, expected_type=type_hints["vpc_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "index_name": index_name,
                "role_arn": role_arn,
                "s3_configuration": s3_configuration,
            }
            if buffering_hints is not None:
                self._values["buffering_hints"] = buffering_hints
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if collection_endpoint is not None:
                self._values["collection_endpoint"] = collection_endpoint
            if processing_configuration is not None:
                self._values["processing_configuration"] = processing_configuration
            if retry_options is not None:
                self._values["retry_options"] = retry_options
            if s3_backup_mode is not None:
                self._values["s3_backup_mode"] = s3_backup_mode
            if vpc_configuration is not None:
                self._values["vpc_configuration"] = vpc_configuration

        @builtins.property
        def index_name(self) -> builtins.str:
            '''The Serverless offering for Amazon OpenSearch Service index name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-indexname
            '''
            result = self._values.get("index_name")
            assert result is not None, "Required property 'index_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the IAM role to be assumed by Firehose for calling the Serverless offering for Amazon OpenSearch Service Configuration API and for indexing documents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-s3configuration
            '''
            result = self._values.get("s3_configuration")
            assert result is not None, "Required property 's3_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"], result)

        @builtins.property
        def buffering_hints(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonOpenSearchServerlessBufferingHintsProperty"]]:
            '''The buffering options.

            If no value is specified, the default values for AmazonopensearchserviceBufferingHints are used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-bufferinghints
            '''
            result = self._values.get("buffering_hints")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonOpenSearchServerlessBufferingHintsProperty"]], result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def collection_endpoint(self) -> typing.Optional[builtins.str]:
            '''The endpoint to use when communicating with the collection in the Serverless offering for Amazon OpenSearch Service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-collectionendpoint
            '''
            result = self._values.get("collection_endpoint")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def processing_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-processingconfiguration
            '''
            result = self._values.get("processing_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]], result)

        @builtins.property
        def retry_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonOpenSearchServerlessRetryOptionsProperty"]]:
            '''The retry behavior in case Firehose is unable to deliver documents to the Serverless offering for Amazon OpenSearch Service.

            The default value is 300 (5 minutes).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-retryoptions
            '''
            result = self._values.get("retry_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonOpenSearchServerlessRetryOptionsProperty"]], result)

        @builtins.property
        def s3_backup_mode(self) -> typing.Optional[builtins.str]:
            '''Defines how documents should be delivered to Amazon S3.

            When it is set to FailedDocumentsOnly, Firehose writes any documents that could not be indexed to the configured Amazon S3 destination, with AmazonOpenSearchService-failed/ appended to the key prefix. When set to AllDocuments, Firehose delivers all incoming records to Amazon S3, and also writes failed documents with AmazonOpenSearchService-failed/ appended to the prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-s3backupmode
            '''
            result = self._values.get("s3_backup_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.VpcConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration-vpcconfiguration
            '''
            result = self._values.get("vpc_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.VpcConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmazonOpenSearchServerlessDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.AmazonOpenSearchServerlessRetryOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"duration_in_seconds": "durationInSeconds"},
    )
    class AmazonOpenSearchServerlessRetryOptionsProperty:
        def __init__(
            self,
            *,
            duration_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Configures retry behavior in case Firehose is unable to deliver documents to the Serverless offering for Amazon OpenSearch Service.

            :param duration_in_seconds: After an initial failure to deliver to the Serverless offering for Amazon OpenSearch Service, the total amount of time during which Firehose retries delivery (including the first attempt). After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessretryoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                amazon_open_search_serverless_retry_options_property = kinesisfirehose.CfnDeliveryStream.AmazonOpenSearchServerlessRetryOptionsProperty(
                    duration_in_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__753f83f6d86f1797776bc00b3eb90cc19e80bd47ed33370727e5209255714a3b)
                check_type(argname="argument duration_in_seconds", value=duration_in_seconds, expected_type=type_hints["duration_in_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if duration_in_seconds is not None:
                self._values["duration_in_seconds"] = duration_in_seconds

        @builtins.property
        def duration_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''After an initial failure to deliver to the Serverless offering for Amazon OpenSearch Service, the total amount of time during which Firehose retries delivery (including the first attempt).

            After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserverlessretryoptions.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessretryoptions-durationinseconds
            '''
            result = self._values.get("duration_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmazonOpenSearchServerlessRetryOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.AmazonopensearchserviceBufferingHintsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "interval_in_seconds": "intervalInSeconds",
            "size_in_m_bs": "sizeInMBs",
        },
    )
    class AmazonopensearchserviceBufferingHintsProperty:
        def __init__(
            self,
            *,
            interval_in_seconds: typing.Optional[jsii.Number] = None,
            size_in_m_bs: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes the buffering to perform before delivering data to the Amazon OpenSearch Service destination.

            :param interval_in_seconds: Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes).
            :param size_in_m_bs: Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5. We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                amazonopensearchservice_buffering_hints_property = kinesisfirehose.CfnDeliveryStream.AmazonopensearchserviceBufferingHintsProperty(
                    interval_in_seconds=123,
                    size_in_mBs=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4bc008db5e34e3ef0ac28740f5aa52a90ec2c2ec0ebeb06a2e361e737f34b840)
                check_type(argname="argument interval_in_seconds", value=interval_in_seconds, expected_type=type_hints["interval_in_seconds"])
                check_type(argname="argument size_in_m_bs", value=size_in_m_bs, expected_type=type_hints["size_in_m_bs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if interval_in_seconds is not None:
                self._values["interval_in_seconds"] = interval_in_seconds
            if size_in_m_bs is not None:
                self._values["size_in_m_bs"] = size_in_m_bs

        @builtins.property
        def interval_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination.

            The default value is 300 (5 minutes).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints-intervalinseconds
            '''
            result = self._values.get("interval_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def size_in_m_bs(self) -> typing.Optional[jsii.Number]:
            '''Buffer incoming data to the specified size, in MBs, before delivering it to the destination.

            The default value is 5. We recommend setting this parameter to a value greater than the amount of data you typically ingest into the delivery stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicebufferinghints-sizeinmbs
            '''
            result = self._values.get("size_in_m_bs")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmazonopensearchserviceBufferingHintsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "index_name": "indexName",
            "role_arn": "roleArn",
            "s3_configuration": "s3Configuration",
            "buffering_hints": "bufferingHints",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "cluster_endpoint": "clusterEndpoint",
            "document_id_options": "documentIdOptions",
            "domain_arn": "domainArn",
            "index_rotation_period": "indexRotationPeriod",
            "processing_configuration": "processingConfiguration",
            "retry_options": "retryOptions",
            "s3_backup_mode": "s3BackupMode",
            "type_name": "typeName",
            "vpc_configuration": "vpcConfiguration",
        },
    )
    class AmazonopensearchserviceDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            index_name: builtins.str,
            role_arn: builtins.str,
            s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.S3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.AmazonopensearchserviceBufferingHintsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.CloudWatchLoggingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cluster_endpoint: typing.Optional[builtins.str] = None,
            document_id_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.DocumentIdOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            domain_arn: typing.Optional[builtins.str] = None,
            index_rotation_period: typing.Optional[builtins.str] = None,
            processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ProcessingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.AmazonopensearchserviceRetryOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_backup_mode: typing.Optional[builtins.str] = None,
            type_name: typing.Optional[builtins.str] = None,
            vpc_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.VpcConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes the configuration of a destination in Amazon OpenSearch Service.

            :param index_name: The Amazon OpenSearch Service index name.
            :param role_arn: The Amazon Resource Name (ARN) of the IAM role to be assumed by Kinesis Data Firehose for calling the Amazon OpenSearch Service Configuration API and for indexing documents.
            :param s3_configuration: Describes the configuration of a destination in Amazon S3.
            :param buffering_hints: The buffering options. If no value is specified, the default values for AmazonopensearchserviceBufferingHints are used.
            :param cloud_watch_logging_options: Describes the Amazon CloudWatch logging options for your delivery stream.
            :param cluster_endpoint: The endpoint to use when communicating with the cluster. Specify either this ClusterEndpoint or the DomainARN field.
            :param document_id_options: Indicates the method for setting up document ID. The supported methods are Firehose generated document ID and OpenSearch Service generated document ID.
            :param domain_arn: The ARN of the Amazon OpenSearch Service domain.
            :param index_rotation_period: The Amazon OpenSearch Service index rotation period. Index rotation appends a timestamp to the IndexName to facilitate the expiration of old data.
            :param processing_configuration: Describes a data processing configuration.
            :param retry_options: The retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon OpenSearch Service. The default value is 300 (5 minutes).
            :param s3_backup_mode: Defines how documents should be delivered to Amazon S3.
            :param type_name: The Amazon OpenSearch Service type name.
            :param vpc_configuration: The details of the VPC of the Amazon OpenSearch Service destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                amazonopensearchservice_destination_configuration_property = kinesisfirehose.CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty(
                    index_name="indexName",
                    role_arn="roleArn",
                    s3_configuration=kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                        bucket_arn="bucketArn",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                            interval_in_seconds=123,
                            size_in_mBs=123
                        ),
                        cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                            enabled=False,
                            log_group_name="logGroupName",
                            log_stream_name="logStreamName"
                        ),
                        compression_format="compressionFormat",
                        encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                            kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                                awskms_key_arn="awskmsKeyArn"
                            ),
                            no_encryption_config="noEncryptionConfig"
                        ),
                        error_output_prefix="errorOutputPrefix",
                        prefix="prefix"
                    ),
                
                    # the properties below are optional
                    buffering_hints=kinesisfirehose.CfnDeliveryStream.AmazonopensearchserviceBufferingHintsProperty(
                        interval_in_seconds=123,
                        size_in_mBs=123
                    ),
                    cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                        enabled=False,
                        log_group_name="logGroupName",
                        log_stream_name="logStreamName"
                    ),
                    cluster_endpoint="clusterEndpoint",
                    document_id_options=kinesisfirehose.CfnDeliveryStream.DocumentIdOptionsProperty(
                        default_document_id_format="defaultDocumentIdFormat"
                    ),
                    domain_arn="domainArn",
                    index_rotation_period="indexRotationPeriod",
                    processing_configuration=kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty(
                        enabled=False,
                        processors=[kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                            type="type",
                
                            # the properties below are optional
                            parameters=[kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                                parameter_name="parameterName",
                                parameter_value="parameterValue"
                            )]
                        )]
                    ),
                    retry_options=kinesisfirehose.CfnDeliveryStream.AmazonopensearchserviceRetryOptionsProperty(
                        duration_in_seconds=123
                    ),
                    s3_backup_mode="s3BackupMode",
                    type_name="typeName",
                    vpc_configuration=kinesisfirehose.CfnDeliveryStream.VpcConfigurationProperty(
                        role_arn="roleArn",
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fd4e3bfe32a6bde0a79abfda5de58ef25a59c29217c39eadcd363cb781608bca)
                check_type(argname="argument index_name", value=index_name, expected_type=type_hints["index_name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument s3_configuration", value=s3_configuration, expected_type=type_hints["s3_configuration"])
                check_type(argname="argument buffering_hints", value=buffering_hints, expected_type=type_hints["buffering_hints"])
                check_type(argname="argument cloud_watch_logging_options", value=cloud_watch_logging_options, expected_type=type_hints["cloud_watch_logging_options"])
                check_type(argname="argument cluster_endpoint", value=cluster_endpoint, expected_type=type_hints["cluster_endpoint"])
                check_type(argname="argument document_id_options", value=document_id_options, expected_type=type_hints["document_id_options"])
                check_type(argname="argument domain_arn", value=domain_arn, expected_type=type_hints["domain_arn"])
                check_type(argname="argument index_rotation_period", value=index_rotation_period, expected_type=type_hints["index_rotation_period"])
                check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
                check_type(argname="argument retry_options", value=retry_options, expected_type=type_hints["retry_options"])
                check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
                check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
                check_type(argname="argument vpc_configuration", value=vpc_configuration, expected_type=type_hints["vpc_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "index_name": index_name,
                "role_arn": role_arn,
                "s3_configuration": s3_configuration,
            }
            if buffering_hints is not None:
                self._values["buffering_hints"] = buffering_hints
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if cluster_endpoint is not None:
                self._values["cluster_endpoint"] = cluster_endpoint
            if document_id_options is not None:
                self._values["document_id_options"] = document_id_options
            if domain_arn is not None:
                self._values["domain_arn"] = domain_arn
            if index_rotation_period is not None:
                self._values["index_rotation_period"] = index_rotation_period
            if processing_configuration is not None:
                self._values["processing_configuration"] = processing_configuration
            if retry_options is not None:
                self._values["retry_options"] = retry_options
            if s3_backup_mode is not None:
                self._values["s3_backup_mode"] = s3_backup_mode
            if type_name is not None:
                self._values["type_name"] = type_name
            if vpc_configuration is not None:
                self._values["vpc_configuration"] = vpc_configuration

        @builtins.property
        def index_name(self) -> builtins.str:
            '''The Amazon OpenSearch Service index name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-indexname
            '''
            result = self._values.get("index_name")
            assert result is not None, "Required property 'index_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the IAM role to be assumed by Kinesis Data Firehose for calling the Amazon OpenSearch Service Configuration API and for indexing documents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]:
            '''Describes the configuration of a destination in Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-s3configuration
            '''
            result = self._values.get("s3_configuration")
            assert result is not None, "Required property 's3_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"], result)

        @builtins.property
        def buffering_hints(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonopensearchserviceBufferingHintsProperty"]]:
            '''The buffering options.

            If no value is specified, the default values for AmazonopensearchserviceBufferingHints are used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-bufferinghints
            '''
            result = self._values.get("buffering_hints")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonopensearchserviceBufferingHintsProperty"]], result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''Describes the Amazon CloudWatch logging options for your delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def cluster_endpoint(self) -> typing.Optional[builtins.str]:
            '''The endpoint to use when communicating with the cluster.

            Specify either this ClusterEndpoint or the DomainARN field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-clusterendpoint
            '''
            result = self._values.get("cluster_endpoint")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def document_id_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DocumentIdOptionsProperty"]]:
            '''Indicates the method for setting up document ID.

            The supported methods are Firehose generated document ID and OpenSearch Service generated document ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-documentidoptions
            '''
            result = self._values.get("document_id_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DocumentIdOptionsProperty"]], result)

        @builtins.property
        def domain_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the Amazon OpenSearch Service domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-domainarn
            '''
            result = self._values.get("domain_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def index_rotation_period(self) -> typing.Optional[builtins.str]:
            '''The Amazon OpenSearch Service index rotation period.

            Index rotation appends a timestamp to the IndexName to facilitate the expiration of old data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-indexrotationperiod
            '''
            result = self._values.get("index_rotation_period")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def processing_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]]:
            '''Describes a data processing configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-processingconfiguration
            '''
            result = self._values.get("processing_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]], result)

        @builtins.property
        def retry_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonopensearchserviceRetryOptionsProperty"]]:
            '''The retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon OpenSearch Service.

            The default value is 300 (5 minutes).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-retryoptions
            '''
            result = self._values.get("retry_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AmazonopensearchserviceRetryOptionsProperty"]], result)

        @builtins.property
        def s3_backup_mode(self) -> typing.Optional[builtins.str]:
            '''Defines how documents should be delivered to Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-s3backupmode
            '''
            result = self._values.get("s3_backup_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type_name(self) -> typing.Optional[builtins.str]:
            '''The Amazon OpenSearch Service type name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-typename
            '''
            result = self._values.get("type_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.VpcConfigurationProperty"]]:
            '''The details of the VPC of the Amazon OpenSearch Service destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration-vpcconfiguration
            '''
            result = self._values.get("vpc_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.VpcConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmazonopensearchserviceDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.AmazonopensearchserviceRetryOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"duration_in_seconds": "durationInSeconds"},
    )
    class AmazonopensearchserviceRetryOptionsProperty:
        def __init__(
            self,
            *,
            duration_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Configures retry behavior in case Kinesis Data Firehose is unable to deliver documents to Amazon OpenSearch Service.

            :param duration_in_seconds: After an initial failure to deliver to Amazon OpenSearch Service, the total amount of time during which Kinesis Data Firehose retries delivery (including the first attempt). After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserviceretryoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                amazonopensearchservice_retry_options_property = kinesisfirehose.CfnDeliveryStream.AmazonopensearchserviceRetryOptionsProperty(
                    duration_in_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e3a6adce37d15471d3dfb2f014a8d32c640e5a4f535c6da724e3b743675a04cb)
                check_type(argname="argument duration_in_seconds", value=duration_in_seconds, expected_type=type_hints["duration_in_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if duration_in_seconds is not None:
                self._values["duration_in_seconds"] = duration_in_seconds

        @builtins.property
        def duration_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''After an initial failure to deliver to Amazon OpenSearch Service, the total amount of time during which Kinesis Data Firehose retries delivery (including the first attempt).

            After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-amazonopensearchserviceretryoptions.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserviceretryoptions-durationinseconds
            '''
            result = self._values.get("duration_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmazonopensearchserviceRetryOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.AuthenticationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"connectivity": "connectivity", "role_arn": "roleArn"},
    )
    class AuthenticationConfigurationProperty:
        def __init__(
            self,
            *,
            connectivity: builtins.str,
            role_arn: builtins.str,
        ) -> None:
            '''The authentication configuration of the Amazon MSK cluster.

            :param connectivity: The type of connectivity used to access the Amazon MSK cluster.
            :param role_arn: The ARN of the role used to access the Amazon MSK cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-authenticationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                authentication_configuration_property = kinesisfirehose.CfnDeliveryStream.AuthenticationConfigurationProperty(
                    connectivity="connectivity",
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__68e16a68225e493cf684cc2bfb151ded05293f2e7b47087f4a97398a1bfeaeb0)
                check_type(argname="argument connectivity", value=connectivity, expected_type=type_hints["connectivity"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "connectivity": connectivity,
                "role_arn": role_arn,
            }

        @builtins.property
        def connectivity(self) -> builtins.str:
            '''The type of connectivity used to access the Amazon MSK cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-authenticationconfiguration.html#cfn-kinesisfirehose-deliverystream-authenticationconfiguration-connectivity
            '''
            result = self._values.get("connectivity")
            assert result is not None, "Required property 'connectivity' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the role used to access the Amazon MSK cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-authenticationconfiguration.html#cfn-kinesisfirehose-deliverystream-authenticationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthenticationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "interval_in_seconds": "intervalInSeconds",
            "size_in_m_bs": "sizeInMBs",
        },
    )
    class BufferingHintsProperty:
        def __init__(
            self,
            *,
            interval_in_seconds: typing.Optional[jsii.Number] = None,
            size_in_m_bs: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The ``BufferingHints`` property type specifies how Amazon Kinesis Data Firehose (Kinesis Data Firehose) buffers incoming data before delivering it to the destination.

            The first buffer condition that is satisfied triggers Kinesis Data Firehose to deliver the data.

            :param interval_in_seconds: The length of time, in seconds, that Kinesis Data Firehose buffers incoming data before delivering it to the destination. For valid values, see the ``IntervalInSeconds`` content for the `BufferingHints <https://docs.aws.amazon.com/firehose/latest/APIReference/API_BufferingHints.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .
            :param size_in_m_bs: The size of the buffer, in MBs, that Kinesis Data Firehose uses for incoming data before delivering it to the destination. For valid values, see the ``SizeInMBs`` content for the `BufferingHints <https://docs.aws.amazon.com/firehose/latest/APIReference/API_BufferingHints.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-bufferinghints.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                buffering_hints_property = kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                    interval_in_seconds=123,
                    size_in_mBs=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c672d0753e4b959e46f98cc809bc2380cd7be551cc9bab6f1b7baa1d203a6f7d)
                check_type(argname="argument interval_in_seconds", value=interval_in_seconds, expected_type=type_hints["interval_in_seconds"])
                check_type(argname="argument size_in_m_bs", value=size_in_m_bs, expected_type=type_hints["size_in_m_bs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if interval_in_seconds is not None:
                self._values["interval_in_seconds"] = interval_in_seconds
            if size_in_m_bs is not None:
                self._values["size_in_m_bs"] = size_in_m_bs

        @builtins.property
        def interval_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The length of time, in seconds, that Kinesis Data Firehose buffers incoming data before delivering it to the destination.

            For valid values, see the ``IntervalInSeconds`` content for the `BufferingHints <https://docs.aws.amazon.com/firehose/latest/APIReference/API_BufferingHints.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-bufferinghints.html#cfn-kinesisfirehose-deliverystream-bufferinghints-intervalinseconds
            '''
            result = self._values.get("interval_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def size_in_m_bs(self) -> typing.Optional[jsii.Number]:
            '''The size of the buffer, in MBs, that Kinesis Data Firehose uses for incoming data before delivering it to the destination.

            For valid values, see the ``SizeInMBs`` content for the `BufferingHints <https://docs.aws.amazon.com/firehose/latest/APIReference/API_BufferingHints.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-bufferinghints.html#cfn-kinesisfirehose-deliverystream-bufferinghints-sizeinmbs
            '''
            result = self._values.get("size_in_m_bs")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BufferingHintsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "log_group_name": "logGroupName",
            "log_stream_name": "logStreamName",
        },
    )
    class CloudWatchLoggingOptionsProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            log_group_name: typing.Optional[builtins.str] = None,
            log_stream_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``CloudWatchLoggingOptions`` property type specifies Amazon CloudWatch Logs (CloudWatch Logs) logging options that Amazon Kinesis Data Firehose (Kinesis Data Firehose) uses for the delivery stream.

            :param enabled: Indicates whether CloudWatch Logs logging is enabled.
            :param log_group_name: The name of the CloudWatch Logs log group that contains the log stream that Kinesis Data Firehose will use. Conditional. If you enable logging, you must specify this property.
            :param log_stream_name: The name of the CloudWatch Logs log stream that Kinesis Data Firehose uses to send logs about data delivery. Conditional. If you enable logging, you must specify this property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                cloud_watch_logging_options_property = kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                    enabled=False,
                    log_group_name="logGroupName",
                    log_stream_name="logStreamName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0992b1c8af7fd8e057904e94d1f683be6233929613125517587cd51de86aa4b5)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
                check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if log_group_name is not None:
                self._values["log_group_name"] = log_group_name
            if log_stream_name is not None:
                self._values["log_stream_name"] = log_stream_name

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether CloudWatch Logs logging is enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.html#cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def log_group_name(self) -> typing.Optional[builtins.str]:
            '''The name of the CloudWatch Logs log group that contains the log stream that Kinesis Data Firehose will use.

            Conditional. If you enable logging, you must specify this property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.html#cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-loggroupname
            '''
            result = self._values.get("log_group_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def log_stream_name(self) -> typing.Optional[builtins.str]:
            '''The name of the CloudWatch Logs log stream that Kinesis Data Firehose uses to send logs about data delivery.

            Conditional. If you enable logging, you must specify this property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-cloudwatchloggingoptions.html#cfn-kinesisfirehose-deliverystream-cloudwatchloggingoptions-logstreamname
            '''
            result = self._values.get("log_stream_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLoggingOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.CopyCommandProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_table_name": "dataTableName",
            "copy_options": "copyOptions",
            "data_table_columns": "dataTableColumns",
        },
    )
    class CopyCommandProperty:
        def __init__(
            self,
            *,
            data_table_name: builtins.str,
            copy_options: typing.Optional[builtins.str] = None,
            data_table_columns: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``CopyCommand`` property type configures the Amazon Redshift ``COPY`` command that Amazon Kinesis Data Firehose (Kinesis Data Firehose) uses to load data into an Amazon Redshift cluster from an Amazon S3 bucket.

            :param data_table_name: The name of the target table. The table must already exist in the database.
            :param copy_options: Parameters to use with the Amazon Redshift ``COPY`` command. For examples, see the ``CopyOptions`` content for the `CopyCommand <https://docs.aws.amazon.com/firehose/latest/APIReference/API_CopyCommand.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .
            :param data_table_columns: A comma-separated list of column names.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-copycommand.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                copy_command_property = kinesisfirehose.CfnDeliveryStream.CopyCommandProperty(
                    data_table_name="dataTableName",
                
                    # the properties below are optional
                    copy_options="copyOptions",
                    data_table_columns="dataTableColumns"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3ed6eb88a63ca5e75a449863a292b3dcd0cbfcd3127e73f575819aaf579cc41f)
                check_type(argname="argument data_table_name", value=data_table_name, expected_type=type_hints["data_table_name"])
                check_type(argname="argument copy_options", value=copy_options, expected_type=type_hints["copy_options"])
                check_type(argname="argument data_table_columns", value=data_table_columns, expected_type=type_hints["data_table_columns"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "data_table_name": data_table_name,
            }
            if copy_options is not None:
                self._values["copy_options"] = copy_options
            if data_table_columns is not None:
                self._values["data_table_columns"] = data_table_columns

        @builtins.property
        def data_table_name(self) -> builtins.str:
            '''The name of the target table.

            The table must already exist in the database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-copycommand.html#cfn-kinesisfirehose-deliverystream-copycommand-datatablename
            '''
            result = self._values.get("data_table_name")
            assert result is not None, "Required property 'data_table_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def copy_options(self) -> typing.Optional[builtins.str]:
            '''Parameters to use with the Amazon Redshift ``COPY`` command.

            For examples, see the ``CopyOptions`` content for the `CopyCommand <https://docs.aws.amazon.com/firehose/latest/APIReference/API_CopyCommand.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-copycommand.html#cfn-kinesisfirehose-deliverystream-copycommand-copyoptions
            '''
            result = self._values.get("copy_options")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_table_columns(self) -> typing.Optional[builtins.str]:
            '''A comma-separated list of column names.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-copycommand.html#cfn-kinesisfirehose-deliverystream-copycommand-datatablecolumns
            '''
            result = self._values.get("data_table_columns")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CopyCommandProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.DataFormatConversionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "input_format_configuration": "inputFormatConfiguration",
            "output_format_configuration": "outputFormatConfiguration",
            "schema_configuration": "schemaConfiguration",
        },
    )
    class DataFormatConversionConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            input_format_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.InputFormatConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            output_format_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.OutputFormatConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            schema_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.SchemaConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies that you want Kinesis Data Firehose to convert data from the JSON format to the Parquet or ORC format before writing it to Amazon S3.

            Kinesis Data Firehose uses the serializer and deserializer that you specify, in addition to the column information from the AWS Glue table, to deserialize your input data from JSON and then serialize it to the Parquet or ORC format. For more information, see `Kinesis Data Firehose Record Format Conversion <https://docs.aws.amazon.com/firehose/latest/dev/record-format-conversion.html>`_ .

            :param enabled: Defaults to ``true`` . Set it to ``false`` if you want to disable format conversion while preserving the configuration details.
            :param input_format_configuration: Specifies the deserializer that you want Firehose to use to convert the format of your data from JSON. This parameter is required if ``Enabled`` is set to true.
            :param output_format_configuration: Specifies the serializer that you want Firehose to use to convert the format of your data to the Parquet or ORC format. This parameter is required if ``Enabled`` is set to true.
            :param schema_configuration: Specifies the AWS Glue Data Catalog table that contains the column information. This parameter is required if ``Enabled`` is set to true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                data_format_conversion_configuration_property = kinesisfirehose.CfnDeliveryStream.DataFormatConversionConfigurationProperty(
                    enabled=False,
                    input_format_configuration=kinesisfirehose.CfnDeliveryStream.InputFormatConfigurationProperty(
                        deserializer=kinesisfirehose.CfnDeliveryStream.DeserializerProperty(
                            hive_json_ser_de=kinesisfirehose.CfnDeliveryStream.HiveJsonSerDeProperty(
                                timestamp_formats=["timestampFormats"]
                            ),
                            open_xJson_ser_de=kinesisfirehose.CfnDeliveryStream.OpenXJsonSerDeProperty(
                                case_insensitive=False,
                                column_to_json_key_mappings={
                                    "column_to_json_key_mappings_key": "columnToJsonKeyMappings"
                                },
                                convert_dots_in_json_keys_to_underscores=False
                            )
                        )
                    ),
                    output_format_configuration=kinesisfirehose.CfnDeliveryStream.OutputFormatConfigurationProperty(
                        serializer=kinesisfirehose.CfnDeliveryStream.SerializerProperty(
                            orc_ser_de=kinesisfirehose.CfnDeliveryStream.OrcSerDeProperty(
                                block_size_bytes=123,
                                bloom_filter_columns=["bloomFilterColumns"],
                                bloom_filter_false_positive_probability=123,
                                compression="compression",
                                dictionary_key_threshold=123,
                                enable_padding=False,
                                format_version="formatVersion",
                                padding_tolerance=123,
                                row_index_stride=123,
                                stripe_size_bytes=123
                            ),
                            parquet_ser_de=kinesisfirehose.CfnDeliveryStream.ParquetSerDeProperty(
                                block_size_bytes=123,
                                compression="compression",
                                enable_dictionary_compression=False,
                                max_padding_bytes=123,
                                page_size_bytes=123,
                                writer_version="writerVersion"
                            )
                        )
                    ),
                    schema_configuration=kinesisfirehose.CfnDeliveryStream.SchemaConfigurationProperty(
                        catalog_id="catalogId",
                        database_name="databaseName",
                        region="region",
                        role_arn="roleArn",
                        table_name="tableName",
                        version_id="versionId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d2fd0a4fb437e036bd2436bcfd397fa35f08aba48c5a25c4aac36dedb0d37e42)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument input_format_configuration", value=input_format_configuration, expected_type=type_hints["input_format_configuration"])
                check_type(argname="argument output_format_configuration", value=output_format_configuration, expected_type=type_hints["output_format_configuration"])
                check_type(argname="argument schema_configuration", value=schema_configuration, expected_type=type_hints["schema_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if input_format_configuration is not None:
                self._values["input_format_configuration"] = input_format_configuration
            if output_format_configuration is not None:
                self._values["output_format_configuration"] = output_format_configuration
            if schema_configuration is not None:
                self._values["schema_configuration"] = schema_configuration

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Defaults to ``true`` .

            Set it to ``false`` if you want to disable format conversion while preserving the configuration details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html#cfn-kinesisfirehose-deliverystream-dataformatconversionconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def input_format_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.InputFormatConfigurationProperty"]]:
            '''Specifies the deserializer that you want Firehose to use to convert the format of your data from JSON.

            This parameter is required if ``Enabled`` is set to true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html#cfn-kinesisfirehose-deliverystream-dataformatconversionconfiguration-inputformatconfiguration
            '''
            result = self._values.get("input_format_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.InputFormatConfigurationProperty"]], result)

        @builtins.property
        def output_format_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.OutputFormatConfigurationProperty"]]:
            '''Specifies the serializer that you want Firehose to use to convert the format of your data to the Parquet or ORC format.

            This parameter is required if ``Enabled`` is set to true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html#cfn-kinesisfirehose-deliverystream-dataformatconversionconfiguration-outputformatconfiguration
            '''
            result = self._values.get("output_format_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.OutputFormatConfigurationProperty"]], result)

        @builtins.property
        def schema_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SchemaConfigurationProperty"]]:
            '''Specifies the AWS Glue Data Catalog table that contains the column information.

            This parameter is required if ``Enabled`` is set to true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dataformatconversionconfiguration.html#cfn-kinesisfirehose-deliverystream-dataformatconversionconfiguration-schemaconfiguration
            '''
            result = self._values.get("schema_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SchemaConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataFormatConversionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={"key_type": "keyType", "key_arn": "keyArn"},
    )
    class DeliveryStreamEncryptionConfigurationInputProperty:
        def __init__(
            self,
            *,
            key_type: builtins.str,
            key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the type and Amazon Resource Name (ARN) of the CMK to use for Server-Side Encryption (SSE).

            :param key_type: Indicates the type of customer master key (CMK) to use for encryption. The default setting is ``AWS_OWNED_CMK`` . For more information about CMKs, see `Customer Master Keys (CMKs) <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys>`_ . You can use a CMK of type CUSTOMER_MANAGED_CMK to encrypt up to 500 delivery streams. .. epigraph:: To encrypt your delivery stream, use symmetric CMKs. Kinesis Data Firehose doesn't support asymmetric CMKs. For information about symmetric and asymmetric CMKs, see `About Symmetric and Asymmetric CMKs <https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-concepts.html>`_ in the AWS Key Management Service developer guide.
            :param key_arn: If you set ``KeyType`` to ``CUSTOMER_MANAGED_CMK`` , you must specify the Amazon Resource Name (ARN) of the CMK. If you set ``KeyType`` to ``AWS _OWNED_CMK`` , Firehose uses a service-account CMK.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                delivery_stream_encryption_configuration_input_property = kinesisfirehose.CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty(
                    key_type="keyType",
                
                    # the properties below are optional
                    key_arn="keyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a51e3602fa39b19119cb43ff1945ccb136f7909bb7d76a42abc9195cb0d725a3)
                check_type(argname="argument key_type", value=key_type, expected_type=type_hints["key_type"])
                check_type(argname="argument key_arn", value=key_arn, expected_type=type_hints["key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key_type": key_type,
            }
            if key_arn is not None:
                self._values["key_arn"] = key_arn

        @builtins.property
        def key_type(self) -> builtins.str:
            '''Indicates the type of customer master key (CMK) to use for encryption.

            The default setting is ``AWS_OWNED_CMK`` . For more information about CMKs, see `Customer Master Keys (CMKs) <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys>`_ .

            You can use a CMK of type CUSTOMER_MANAGED_CMK to encrypt up to 500 delivery streams.
            .. epigraph::

               To encrypt your delivery stream, use symmetric CMKs. Kinesis Data Firehose doesn't support asymmetric CMKs. For information about symmetric and asymmetric CMKs, see `About Symmetric and Asymmetric CMKs <https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-concepts.html>`_ in the AWS Key Management Service developer guide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput.html#cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput-keytype
            '''
            result = self._values.get("key_type")
            assert result is not None, "Required property 'key_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_arn(self) -> typing.Optional[builtins.str]:
            '''If you set ``KeyType`` to ``CUSTOMER_MANAGED_CMK`` , you must specify the Amazon Resource Name (ARN) of the CMK.

            If you set ``KeyType`` to ``AWS _OWNED_CMK`` , Firehose uses a service-account CMK.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput.html#cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput-keyarn
            '''
            result = self._values.get("key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeliveryStreamEncryptionConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.DeserializerProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hive_json_ser_de": "hiveJsonSerDe",
            "open_x_json_ser_de": "openXJsonSerDe",
        },
    )
    class DeserializerProperty:
        def __init__(
            self,
            *,
            hive_json_ser_de: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.HiveJsonSerDeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            open_x_json_ser_de: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.OpenXJsonSerDeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The deserializer you want Kinesis Data Firehose to use for converting the input data from JSON.

            Kinesis Data Firehose then serializes the data to its final format using the ``Serializer`` . Kinesis Data Firehose supports two types of deserializers: the `Apache Hive JSON SerDe <https://docs.aws.amazon.com/https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL#LanguageManualDDL-JSON>`_ and the `OpenX JSON SerDe <https://docs.aws.amazon.com/https://github.com/rcongiu/Hive-JSON-Serde>`_ .

            :param hive_json_ser_de: The native Hive / HCatalog JsonSerDe. Used by Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the OpenX SerDe.
            :param open_x_json_ser_de: The OpenX SerDe. Used by Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the native Hive / HCatalog JsonSerDe.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deserializer.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                deserializer_property = kinesisfirehose.CfnDeliveryStream.DeserializerProperty(
                    hive_json_ser_de=kinesisfirehose.CfnDeliveryStream.HiveJsonSerDeProperty(
                        timestamp_formats=["timestampFormats"]
                    ),
                    open_xJson_ser_de=kinesisfirehose.CfnDeliveryStream.OpenXJsonSerDeProperty(
                        case_insensitive=False,
                        column_to_json_key_mappings={
                            "column_to_json_key_mappings_key": "columnToJsonKeyMappings"
                        },
                        convert_dots_in_json_keys_to_underscores=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__42c1d0a7a47a7fb87bd171a324b5d6ec1a60f675aa066d295f3a321445b0d566)
                check_type(argname="argument hive_json_ser_de", value=hive_json_ser_de, expected_type=type_hints["hive_json_ser_de"])
                check_type(argname="argument open_x_json_ser_de", value=open_x_json_ser_de, expected_type=type_hints["open_x_json_ser_de"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if hive_json_ser_de is not None:
                self._values["hive_json_ser_de"] = hive_json_ser_de
            if open_x_json_ser_de is not None:
                self._values["open_x_json_ser_de"] = open_x_json_ser_de

        @builtins.property
        def hive_json_ser_de(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.HiveJsonSerDeProperty"]]:
            '''The native Hive / HCatalog JsonSerDe.

            Used by Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the OpenX SerDe.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deserializer.html#cfn-kinesisfirehose-deliverystream-deserializer-hivejsonserde
            '''
            result = self._values.get("hive_json_ser_de")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.HiveJsonSerDeProperty"]], result)

        @builtins.property
        def open_x_json_ser_de(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.OpenXJsonSerDeProperty"]]:
            '''The OpenX SerDe.

            Used by Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the native Hive / HCatalog JsonSerDe.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-deserializer.html#cfn-kinesisfirehose-deliverystream-deserializer-openxjsonserde
            '''
            result = self._values.get("open_x_json_ser_de")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.OpenXJsonSerDeProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeserializerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.DocumentIdOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"default_document_id_format": "defaultDocumentIdFormat"},
    )
    class DocumentIdOptionsProperty:
        def __init__(self, *, default_document_id_format: builtins.str) -> None:
            '''Indicates the method for setting up document ID.

            The supported methods are Firehose generated document ID and OpenSearch Service generated document ID.

            :param default_document_id_format: When the ``FIREHOSE_DEFAULT`` option is chosen, Firehose generates a unique document ID for each record based on a unique internal identifier. The generated document ID is stable across multiple delivery attempts, which helps prevent the same record from being indexed multiple times with different document IDs. When the ``NO_DOCUMENT_ID`` option is chosen, Firehose does not include any document IDs in the requests it sends to the Amazon OpenSearch Service. This causes the Amazon OpenSearch Service domain to generate document IDs. In case of multiple delivery attempts, this may cause the same record to be indexed more than once with different document IDs. This option enables write-heavy operations, such as the ingestion of logs and observability data, to consume less resources in the Amazon OpenSearch Service domain, resulting in improved performance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-documentidoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                document_id_options_property = kinesisfirehose.CfnDeliveryStream.DocumentIdOptionsProperty(
                    default_document_id_format="defaultDocumentIdFormat"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d76edd5ad2b58b9b0bbc3359143f6d89ce784d7ac50b34881cf657d8016bcec4)
                check_type(argname="argument default_document_id_format", value=default_document_id_format, expected_type=type_hints["default_document_id_format"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "default_document_id_format": default_document_id_format,
            }

        @builtins.property
        def default_document_id_format(self) -> builtins.str:
            '''When the ``FIREHOSE_DEFAULT`` option is chosen, Firehose generates a unique document ID for each record based on a unique internal identifier.

            The generated document ID is stable across multiple delivery attempts, which helps prevent the same record from being indexed multiple times with different document IDs.

            When the ``NO_DOCUMENT_ID`` option is chosen, Firehose does not include any document IDs in the requests it sends to the Amazon OpenSearch Service. This causes the Amazon OpenSearch Service domain to generate document IDs. In case of multiple delivery attempts, this may cause the same record to be indexed more than once with different document IDs. This option enables write-heavy operations, such as the ingestion of logs and observability data, to consume less resources in the Amazon OpenSearch Service domain, resulting in improved performance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-documentidoptions.html#cfn-kinesisfirehose-deliverystream-documentidoptions-defaultdocumentidformat
            '''
            result = self._values.get("default_document_id_format")
            assert result is not None, "Required property 'default_document_id_format' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocumentIdOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.DynamicPartitioningConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "retry_options": "retryOptions"},
    )
    class DynamicPartitioningConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.RetryOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The ``DynamicPartitioningConfiguration`` property type specifies the configuration of the dynamic partitioning mechanism that creates targeted data sets from the streaming data by partitioning it based on partition keys.

            :param enabled: Specifies whether dynamic partitioning is enabled for this Kinesis Data Firehose delivery stream.
            :param retry_options: Specifies the retry behavior in case Kinesis Data Firehose is unable to deliver data to an Amazon S3 prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                dynamic_partitioning_configuration_property = kinesisfirehose.CfnDeliveryStream.DynamicPartitioningConfigurationProperty(
                    enabled=False,
                    retry_options=kinesisfirehose.CfnDeliveryStream.RetryOptionsProperty(
                        duration_in_seconds=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9cc891db4fb4eb3331e62299f82fedd4776288b7686ae851e51bfb6e44e55a52)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument retry_options", value=retry_options, expected_type=type_hints["retry_options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if retry_options is not None:
                self._values["retry_options"] = retry_options

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether dynamic partitioning is enabled for this Kinesis Data Firehose delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration.html#cfn-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def retry_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.RetryOptionsProperty"]]:
            '''Specifies the retry behavior in case Kinesis Data Firehose is unable to deliver data to an Amazon S3 prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration.html#cfn-kinesisfirehose-deliverystream-dynamicpartitioningconfiguration-retryoptions
            '''
            result = self._values.get("retry_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.RetryOptionsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynamicPartitioningConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.ElasticsearchBufferingHintsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "interval_in_seconds": "intervalInSeconds",
            "size_in_m_bs": "sizeInMBs",
        },
    )
    class ElasticsearchBufferingHintsProperty:
        def __init__(
            self,
            *,
            interval_in_seconds: typing.Optional[jsii.Number] = None,
            size_in_m_bs: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The ``ElasticsearchBufferingHints`` property type specifies how Amazon Kinesis Data Firehose (Kinesis Data Firehose) buffers incoming data while delivering it to the destination.

            The first buffer condition that is satisfied triggers Kinesis Data Firehose to deliver the data.

            ElasticsearchBufferingHints is the property type for the ``BufferingHints`` property of the `Amazon Kinesis Data Firehose DeliveryStream ElasticsearchDestinationConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html>`_ property type.

            :param interval_in_seconds: The length of time, in seconds, that Kinesis Data Firehose buffers incoming data before delivering it to the destination. For valid values, see the ``IntervalInSeconds`` content for the `BufferingHints <https://docs.aws.amazon.com/firehose/latest/APIReference/API_BufferingHints.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .
            :param size_in_m_bs: The size of the buffer, in MBs, that Kinesis Data Firehose uses for incoming data before delivering it to the destination. For valid values, see the ``SizeInMBs`` content for the `BufferingHints <https://docs.aws.amazon.com/firehose/latest/APIReference/API_BufferingHints.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchbufferinghints.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                elasticsearch_buffering_hints_property = kinesisfirehose.CfnDeliveryStream.ElasticsearchBufferingHintsProperty(
                    interval_in_seconds=123,
                    size_in_mBs=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__081c1ee4107d2560ed72dcc369fb8bd5cb51575be94b287e3e1d199e78950677)
                check_type(argname="argument interval_in_seconds", value=interval_in_seconds, expected_type=type_hints["interval_in_seconds"])
                check_type(argname="argument size_in_m_bs", value=size_in_m_bs, expected_type=type_hints["size_in_m_bs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if interval_in_seconds is not None:
                self._values["interval_in_seconds"] = interval_in_seconds
            if size_in_m_bs is not None:
                self._values["size_in_m_bs"] = size_in_m_bs

        @builtins.property
        def interval_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The length of time, in seconds, that Kinesis Data Firehose buffers incoming data before delivering it to the destination.

            For valid values, see the ``IntervalInSeconds`` content for the `BufferingHints <https://docs.aws.amazon.com/firehose/latest/APIReference/API_BufferingHints.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchbufferinghints.html#cfn-kinesisfirehose-deliverystream-elasticsearchbufferinghints-intervalinseconds
            '''
            result = self._values.get("interval_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def size_in_m_bs(self) -> typing.Optional[jsii.Number]:
            '''The size of the buffer, in MBs, that Kinesis Data Firehose uses for incoming data before delivering it to the destination.

            For valid values, see the ``SizeInMBs`` content for the `BufferingHints <https://docs.aws.amazon.com/firehose/latest/APIReference/API_BufferingHints.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchbufferinghints.html#cfn-kinesisfirehose-deliverystream-elasticsearchbufferinghints-sizeinmbs
            '''
            result = self._values.get("size_in_m_bs")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ElasticsearchBufferingHintsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "index_name": "indexName",
            "role_arn": "roleArn",
            "s3_configuration": "s3Configuration",
            "buffering_hints": "bufferingHints",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "cluster_endpoint": "clusterEndpoint",
            "document_id_options": "documentIdOptions",
            "domain_arn": "domainArn",
            "index_rotation_period": "indexRotationPeriod",
            "processing_configuration": "processingConfiguration",
            "retry_options": "retryOptions",
            "s3_backup_mode": "s3BackupMode",
            "type_name": "typeName",
            "vpc_configuration": "vpcConfiguration",
        },
    )
    class ElasticsearchDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            index_name: builtins.str,
            role_arn: builtins.str,
            s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.S3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ElasticsearchBufferingHintsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.CloudWatchLoggingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cluster_endpoint: typing.Optional[builtins.str] = None,
            document_id_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.DocumentIdOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            domain_arn: typing.Optional[builtins.str] = None,
            index_rotation_period: typing.Optional[builtins.str] = None,
            processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ProcessingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ElasticsearchRetryOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_backup_mode: typing.Optional[builtins.str] = None,
            type_name: typing.Optional[builtins.str] = None,
            vpc_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.VpcConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The ``ElasticsearchDestinationConfiguration`` property type specifies an Amazon Elasticsearch Service (Amazon ES) domain that Amazon Kinesis Data Firehose (Kinesis Data Firehose) delivers data to.

            :param index_name: The name of the Elasticsearch index to which Kinesis Data Firehose adds data for indexing.
            :param role_arn: The Amazon Resource Name (ARN) of the IAM role to be assumed by Kinesis Data Firehose for calling the Amazon ES Configuration API and for indexing documents. For more information, see `Controlling Access with Amazon Kinesis Data Firehose <https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html>`_ .
            :param s3_configuration: The S3 bucket where Kinesis Data Firehose backs up incoming data.
            :param buffering_hints: Configures how Kinesis Data Firehose buffers incoming data while delivering it to the Amazon ES domain.
            :param cloud_watch_logging_options: The Amazon CloudWatch Logs logging options for the delivery stream.
            :param cluster_endpoint: The endpoint to use when communicating with the cluster. Specify either this ``ClusterEndpoint`` or the ``DomainARN`` field.
            :param document_id_options: Indicates the method for setting up document ID. The supported methods are Firehose generated document ID and OpenSearch Service generated document ID.
            :param domain_arn: The ARN of the Amazon ES domain. The IAM role must have permissions for ``DescribeElasticsearchDomain`` , ``DescribeElasticsearchDomains`` , and ``DescribeElasticsearchDomainConfig`` after assuming the role specified in *RoleARN* . Specify either ``ClusterEndpoint`` or ``DomainARN`` .
            :param index_rotation_period: The frequency of Elasticsearch index rotation. If you enable index rotation, Kinesis Data Firehose appends a portion of the UTC arrival timestamp to the specified index name, and rotates the appended timestamp accordingly. For more information, see `Index Rotation for the Amazon ES Destination <https://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#es-index-rotation>`_ in the *Amazon Kinesis Data Firehose Developer Guide* .
            :param processing_configuration: The data processing configuration for the Kinesis Data Firehose delivery stream.
            :param retry_options: The retry behavior when Kinesis Data Firehose is unable to deliver data to Amazon ES.
            :param s3_backup_mode: The condition under which Kinesis Data Firehose delivers data to Amazon Simple Storage Service (Amazon S3). You can send Amazon S3 all documents (all data) or only the documents that Kinesis Data Firehose could not deliver to the Amazon ES destination. For more information and valid values, see the ``S3BackupMode`` content for the `ElasticsearchDestinationConfiguration <https://docs.aws.amazon.com/firehose/latest/APIReference/API_ElasticsearchDestinationConfiguration.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .
            :param type_name: The Elasticsearch type name that Amazon ES adds to documents when indexing data.
            :param vpc_configuration: The details of the VPC of the Amazon ES destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                elasticsearch_destination_configuration_property = kinesisfirehose.CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty(
                    index_name="indexName",
                    role_arn="roleArn",
                    s3_configuration=kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                        bucket_arn="bucketArn",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                            interval_in_seconds=123,
                            size_in_mBs=123
                        ),
                        cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                            enabled=False,
                            log_group_name="logGroupName",
                            log_stream_name="logStreamName"
                        ),
                        compression_format="compressionFormat",
                        encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                            kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                                awskms_key_arn="awskmsKeyArn"
                            ),
                            no_encryption_config="noEncryptionConfig"
                        ),
                        error_output_prefix="errorOutputPrefix",
                        prefix="prefix"
                    ),
                
                    # the properties below are optional
                    buffering_hints=kinesisfirehose.CfnDeliveryStream.ElasticsearchBufferingHintsProperty(
                        interval_in_seconds=123,
                        size_in_mBs=123
                    ),
                    cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                        enabled=False,
                        log_group_name="logGroupName",
                        log_stream_name="logStreamName"
                    ),
                    cluster_endpoint="clusterEndpoint",
                    document_id_options=kinesisfirehose.CfnDeliveryStream.DocumentIdOptionsProperty(
                        default_document_id_format="defaultDocumentIdFormat"
                    ),
                    domain_arn="domainArn",
                    index_rotation_period="indexRotationPeriod",
                    processing_configuration=kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty(
                        enabled=False,
                        processors=[kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                            type="type",
                
                            # the properties below are optional
                            parameters=[kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                                parameter_name="parameterName",
                                parameter_value="parameterValue"
                            )]
                        )]
                    ),
                    retry_options=kinesisfirehose.CfnDeliveryStream.ElasticsearchRetryOptionsProperty(
                        duration_in_seconds=123
                    ),
                    s3_backup_mode="s3BackupMode",
                    type_name="typeName",
                    vpc_configuration=kinesisfirehose.CfnDeliveryStream.VpcConfigurationProperty(
                        role_arn="roleArn",
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__029a33c003279860929256e859d4ba1b8707f3f6569f11613c5f08ef467fe6d6)
                check_type(argname="argument index_name", value=index_name, expected_type=type_hints["index_name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument s3_configuration", value=s3_configuration, expected_type=type_hints["s3_configuration"])
                check_type(argname="argument buffering_hints", value=buffering_hints, expected_type=type_hints["buffering_hints"])
                check_type(argname="argument cloud_watch_logging_options", value=cloud_watch_logging_options, expected_type=type_hints["cloud_watch_logging_options"])
                check_type(argname="argument cluster_endpoint", value=cluster_endpoint, expected_type=type_hints["cluster_endpoint"])
                check_type(argname="argument document_id_options", value=document_id_options, expected_type=type_hints["document_id_options"])
                check_type(argname="argument domain_arn", value=domain_arn, expected_type=type_hints["domain_arn"])
                check_type(argname="argument index_rotation_period", value=index_rotation_period, expected_type=type_hints["index_rotation_period"])
                check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
                check_type(argname="argument retry_options", value=retry_options, expected_type=type_hints["retry_options"])
                check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
                check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
                check_type(argname="argument vpc_configuration", value=vpc_configuration, expected_type=type_hints["vpc_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "index_name": index_name,
                "role_arn": role_arn,
                "s3_configuration": s3_configuration,
            }
            if buffering_hints is not None:
                self._values["buffering_hints"] = buffering_hints
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if cluster_endpoint is not None:
                self._values["cluster_endpoint"] = cluster_endpoint
            if document_id_options is not None:
                self._values["document_id_options"] = document_id_options
            if domain_arn is not None:
                self._values["domain_arn"] = domain_arn
            if index_rotation_period is not None:
                self._values["index_rotation_period"] = index_rotation_period
            if processing_configuration is not None:
                self._values["processing_configuration"] = processing_configuration
            if retry_options is not None:
                self._values["retry_options"] = retry_options
            if s3_backup_mode is not None:
                self._values["s3_backup_mode"] = s3_backup_mode
            if type_name is not None:
                self._values["type_name"] = type_name
            if vpc_configuration is not None:
                self._values["vpc_configuration"] = vpc_configuration

        @builtins.property
        def index_name(self) -> builtins.str:
            '''The name of the Elasticsearch index to which Kinesis Data Firehose adds data for indexing.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-indexname
            '''
            result = self._values.get("index_name")
            assert result is not None, "Required property 'index_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the IAM role to be assumed by Kinesis Data Firehose for calling the Amazon ES Configuration API and for indexing documents.

            For more information, see `Controlling Access with Amazon Kinesis Data Firehose <https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]:
            '''The S3 bucket where Kinesis Data Firehose backs up incoming data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-s3configuration
            '''
            result = self._values.get("s3_configuration")
            assert result is not None, "Required property 's3_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"], result)

        @builtins.property
        def buffering_hints(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ElasticsearchBufferingHintsProperty"]]:
            '''Configures how Kinesis Data Firehose buffers incoming data while delivering it to the Amazon ES domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-bufferinghints
            '''
            result = self._values.get("buffering_hints")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ElasticsearchBufferingHintsProperty"]], result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''The Amazon CloudWatch Logs logging options for the delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def cluster_endpoint(self) -> typing.Optional[builtins.str]:
            '''The endpoint to use when communicating with the cluster.

            Specify either this ``ClusterEndpoint`` or the ``DomainARN`` field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-clusterendpoint
            '''
            result = self._values.get("cluster_endpoint")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def document_id_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DocumentIdOptionsProperty"]]:
            '''Indicates the method for setting up document ID.

            The supported methods are Firehose generated document ID and OpenSearch Service generated document ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-documentidoptions
            '''
            result = self._values.get("document_id_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DocumentIdOptionsProperty"]], result)

        @builtins.property
        def domain_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the Amazon ES domain.

            The IAM role must have permissions for ``DescribeElasticsearchDomain`` , ``DescribeElasticsearchDomains`` , and ``DescribeElasticsearchDomainConfig`` after assuming the role specified in *RoleARN* .

            Specify either ``ClusterEndpoint`` or ``DomainARN`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-domainarn
            '''
            result = self._values.get("domain_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def index_rotation_period(self) -> typing.Optional[builtins.str]:
            '''The frequency of Elasticsearch index rotation.

            If you enable index rotation, Kinesis Data Firehose appends a portion of the UTC arrival timestamp to the specified index name, and rotates the appended timestamp accordingly. For more information, see `Index Rotation for the Amazon ES Destination <https://docs.aws.amazon.com/firehose/latest/dev/basic-deliver.html#es-index-rotation>`_ in the *Amazon Kinesis Data Firehose Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-indexrotationperiod
            '''
            result = self._values.get("index_rotation_period")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def processing_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]]:
            '''The data processing configuration for the Kinesis Data Firehose delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-processingconfiguration
            '''
            result = self._values.get("processing_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]], result)

        @builtins.property
        def retry_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ElasticsearchRetryOptionsProperty"]]:
            '''The retry behavior when Kinesis Data Firehose is unable to deliver data to Amazon ES.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-retryoptions
            '''
            result = self._values.get("retry_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ElasticsearchRetryOptionsProperty"]], result)

        @builtins.property
        def s3_backup_mode(self) -> typing.Optional[builtins.str]:
            '''The condition under which Kinesis Data Firehose delivers data to Amazon Simple Storage Service (Amazon S3).

            You can send Amazon S3 all documents (all data) or only the documents that Kinesis Data Firehose could not deliver to the Amazon ES destination. For more information and valid values, see the ``S3BackupMode`` content for the `ElasticsearchDestinationConfiguration <https://docs.aws.amazon.com/firehose/latest/APIReference/API_ElasticsearchDestinationConfiguration.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-s3backupmode
            '''
            result = self._values.get("s3_backup_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type_name(self) -> typing.Optional[builtins.str]:
            '''The Elasticsearch type name that Amazon ES adds to documents when indexing data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-typename
            '''
            result = self._values.get("type_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.VpcConfigurationProperty"]]:
            '''The details of the VPC of the Amazon ES destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration-vpcconfiguration
            '''
            result = self._values.get("vpc_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.VpcConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ElasticsearchDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.ElasticsearchRetryOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"duration_in_seconds": "durationInSeconds"},
    )
    class ElasticsearchRetryOptionsProperty:
        def __init__(
            self,
            *,
            duration_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The ``ElasticsearchRetryOptions`` property type configures the retry behavior for when Amazon Kinesis Data Firehose (Kinesis Data Firehose) can't deliver data to Amazon Elasticsearch Service (Amazon ES).

            :param duration_in_seconds: After an initial failure to deliver to Amazon ES, the total amount of time during which Kinesis Data Firehose re-attempts delivery (including the first attempt). If Kinesis Data Firehose can't deliver the data within the specified time, it writes the data to the backup S3 bucket. For valid values, see the ``DurationInSeconds`` content for the `ElasticsearchRetryOptions <https://docs.aws.amazon.com/firehose/latest/APIReference/API_ElasticsearchRetryOptions.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchretryoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                elasticsearch_retry_options_property = kinesisfirehose.CfnDeliveryStream.ElasticsearchRetryOptionsProperty(
                    duration_in_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2556301b4eb1fbc8924ad4d41633add09219c34215bad4251ecd9506fbd5f4f1)
                check_type(argname="argument duration_in_seconds", value=duration_in_seconds, expected_type=type_hints["duration_in_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if duration_in_seconds is not None:
                self._values["duration_in_seconds"] = duration_in_seconds

        @builtins.property
        def duration_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''After an initial failure to deliver to Amazon ES, the total amount of time during which Kinesis Data Firehose re-attempts delivery (including the first attempt).

            If Kinesis Data Firehose can't deliver the data within the specified time, it writes the data to the backup S3 bucket. For valid values, see the ``DurationInSeconds`` content for the `ElasticsearchRetryOptions <https://docs.aws.amazon.com/firehose/latest/APIReference/API_ElasticsearchRetryOptions.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-elasticsearchretryoptions.html#cfn-kinesisfirehose-deliverystream-elasticsearchretryoptions-durationinseconds
            '''
            result = self._values.get("duration_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ElasticsearchRetryOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "kms_encryption_config": "kmsEncryptionConfig",
            "no_encryption_config": "noEncryptionConfig",
        },
    )
    class EncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            kms_encryption_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.KMSEncryptionConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            no_encryption_config: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``EncryptionConfiguration`` property type specifies the encryption settings that Amazon Kinesis Data Firehose (Kinesis Data Firehose) uses when delivering data to Amazon Simple Storage Service (Amazon S3).

            :param kms_encryption_config: The AWS Key Management Service ( AWS KMS) encryption key that Amazon S3 uses to encrypt your data.
            :param no_encryption_config: Disables encryption. For valid values, see the ``NoEncryptionConfig`` content for the `EncryptionConfiguration <https://docs.aws.amazon.com/firehose/latest/APIReference/API_EncryptionConfiguration.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-encryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                encryption_configuration_property = kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                    kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                        awskms_key_arn="awskmsKeyArn"
                    ),
                    no_encryption_config="noEncryptionConfig"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4416718c6f0bcd460ac15d8467b60189a1b6ff006003483c5095802962acb534)
                check_type(argname="argument kms_encryption_config", value=kms_encryption_config, expected_type=type_hints["kms_encryption_config"])
                check_type(argname="argument no_encryption_config", value=no_encryption_config, expected_type=type_hints["no_encryption_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if kms_encryption_config is not None:
                self._values["kms_encryption_config"] = kms_encryption_config
            if no_encryption_config is not None:
                self._values["no_encryption_config"] = no_encryption_config

        @builtins.property
        def kms_encryption_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.KMSEncryptionConfigProperty"]]:
            '''The AWS Key Management Service ( AWS KMS) encryption key that Amazon S3 uses to encrypt your data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-encryptionconfiguration.html#cfn-kinesisfirehose-deliverystream-encryptionconfiguration-kmsencryptionconfig
            '''
            result = self._values.get("kms_encryption_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.KMSEncryptionConfigProperty"]], result)

        @builtins.property
        def no_encryption_config(self) -> typing.Optional[builtins.str]:
            '''Disables encryption.

            For valid values, see the ``NoEncryptionConfig`` content for the `EncryptionConfiguration <https://docs.aws.amazon.com/firehose/latest/APIReference/API_EncryptionConfiguration.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-encryptionconfiguration.html#cfn-kinesisfirehose-deliverystream-encryptionconfiguration-noencryptionconfig
            '''
            result = self._values.get("no_encryption_config")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_arn": "bucketArn",
            "role_arn": "roleArn",
            "buffering_hints": "bufferingHints",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "compression_format": "compressionFormat",
            "custom_time_zone": "customTimeZone",
            "data_format_conversion_configuration": "dataFormatConversionConfiguration",
            "dynamic_partitioning_configuration": "dynamicPartitioningConfiguration",
            "encryption_configuration": "encryptionConfiguration",
            "error_output_prefix": "errorOutputPrefix",
            "file_extension": "fileExtension",
            "prefix": "prefix",
            "processing_configuration": "processingConfiguration",
            "s3_backup_configuration": "s3BackupConfiguration",
            "s3_backup_mode": "s3BackupMode",
        },
    )
    class ExtendedS3DestinationConfigurationProperty:
        def __init__(
            self,
            *,
            bucket_arn: builtins.str,
            role_arn: builtins.str,
            buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.BufferingHintsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.CloudWatchLoggingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            compression_format: typing.Optional[builtins.str] = None,
            custom_time_zone: typing.Optional[builtins.str] = None,
            data_format_conversion_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.DataFormatConversionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            dynamic_partitioning_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.DynamicPartitioningConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            error_output_prefix: typing.Optional[builtins.str] = None,
            file_extension: typing.Optional[builtins.str] = None,
            prefix: typing.Optional[builtins.str] = None,
            processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ProcessingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_backup_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.S3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_backup_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``ExtendedS3DestinationConfiguration`` property type configures an Amazon S3 destination for an Amazon Kinesis Data Firehose delivery stream.

            :param bucket_arn: The Amazon Resource Name (ARN) of the Amazon S3 bucket. For constraints, see `ExtendedS3DestinationConfiguration <https://docs.aws.amazon.com/firehose/latest/APIReference/API_ExtendedS3DestinationConfiguration.html>`_ in the *Amazon Kinesis Data Firehose API Reference* .
            :param role_arn: The Amazon Resource Name (ARN) of the AWS credentials. For constraints, see `ExtendedS3DestinationConfiguration <https://docs.aws.amazon.com/firehose/latest/APIReference/API_ExtendedS3DestinationConfiguration.html>`_ in the *Amazon Kinesis Data Firehose API Reference* .
            :param buffering_hints: The buffering option.
            :param cloud_watch_logging_options: The Amazon CloudWatch logging options for your delivery stream.
            :param compression_format: The compression format. If no value is specified, the default is ``UNCOMPRESSED`` .
            :param custom_time_zone: The time zone you prefer. UTC is the default.
            :param data_format_conversion_configuration: The serializer, deserializer, and schema for converting data from the JSON format to the Parquet or ORC format before writing it to Amazon S3.
            :param dynamic_partitioning_configuration: The configuration of the dynamic partitioning mechanism that creates targeted data sets from the streaming data by partitioning it based on partition keys.
            :param encryption_configuration: The encryption configuration for the Kinesis Data Firehose delivery stream. The default value is ``NoEncryption`` .
            :param error_output_prefix: A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see `Custom Prefixes for Amazon S3 Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`_ .
            :param file_extension: Specify a file extension. It will override the default file extension
            :param prefix: The ``YYYY/MM/DD/HH`` time format prefix is automatically used for delivered Amazon S3 files. For more information, see `ExtendedS3DestinationConfiguration <https://docs.aws.amazon.com/firehose/latest/APIReference/API_ExtendedS3DestinationConfiguration.html>`_ in the *Amazon Kinesis Data Firehose API Reference* .
            :param processing_configuration: The data processing configuration for the Kinesis Data Firehose delivery stream.
            :param s3_backup_configuration: The configuration for backup in Amazon S3.
            :param s3_backup_mode: The Amazon S3 backup mode. After you create a delivery stream, you can update it to enable Amazon S3 backup if it is disabled. If backup is enabled, you can't update the delivery stream to disable it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                extended_s3_destination_configuration_property = kinesisfirehose.CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty(
                    bucket_arn="bucketArn",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                        interval_in_seconds=123,
                        size_in_mBs=123
                    ),
                    cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                        enabled=False,
                        log_group_name="logGroupName",
                        log_stream_name="logStreamName"
                    ),
                    compression_format="compressionFormat",
                    custom_time_zone="customTimeZone",
                    data_format_conversion_configuration=kinesisfirehose.CfnDeliveryStream.DataFormatConversionConfigurationProperty(
                        enabled=False,
                        input_format_configuration=kinesisfirehose.CfnDeliveryStream.InputFormatConfigurationProperty(
                            deserializer=kinesisfirehose.CfnDeliveryStream.DeserializerProperty(
                                hive_json_ser_de=kinesisfirehose.CfnDeliveryStream.HiveJsonSerDeProperty(
                                    timestamp_formats=["timestampFormats"]
                                ),
                                open_xJson_ser_de=kinesisfirehose.CfnDeliveryStream.OpenXJsonSerDeProperty(
                                    case_insensitive=False,
                                    column_to_json_key_mappings={
                                        "column_to_json_key_mappings_key": "columnToJsonKeyMappings"
                                    },
                                    convert_dots_in_json_keys_to_underscores=False
                                )
                            )
                        ),
                        output_format_configuration=kinesisfirehose.CfnDeliveryStream.OutputFormatConfigurationProperty(
                            serializer=kinesisfirehose.CfnDeliveryStream.SerializerProperty(
                                orc_ser_de=kinesisfirehose.CfnDeliveryStream.OrcSerDeProperty(
                                    block_size_bytes=123,
                                    bloom_filter_columns=["bloomFilterColumns"],
                                    bloom_filter_false_positive_probability=123,
                                    compression="compression",
                                    dictionary_key_threshold=123,
                                    enable_padding=False,
                                    format_version="formatVersion",
                                    padding_tolerance=123,
                                    row_index_stride=123,
                                    stripe_size_bytes=123
                                ),
                                parquet_ser_de=kinesisfirehose.CfnDeliveryStream.ParquetSerDeProperty(
                                    block_size_bytes=123,
                                    compression="compression",
                                    enable_dictionary_compression=False,
                                    max_padding_bytes=123,
                                    page_size_bytes=123,
                                    writer_version="writerVersion"
                                )
                            )
                        ),
                        schema_configuration=kinesisfirehose.CfnDeliveryStream.SchemaConfigurationProperty(
                            catalog_id="catalogId",
                            database_name="databaseName",
                            region="region",
                            role_arn="roleArn",
                            table_name="tableName",
                            version_id="versionId"
                        )
                    ),
                    dynamic_partitioning_configuration=kinesisfirehose.CfnDeliveryStream.DynamicPartitioningConfigurationProperty(
                        enabled=False,
                        retry_options=kinesisfirehose.CfnDeliveryStream.RetryOptionsProperty(
                            duration_in_seconds=123
                        )
                    ),
                    encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                        kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                            awskms_key_arn="awskmsKeyArn"
                        ),
                        no_encryption_config="noEncryptionConfig"
                    ),
                    error_output_prefix="errorOutputPrefix",
                    file_extension="fileExtension",
                    prefix="prefix",
                    processing_configuration=kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty(
                        enabled=False,
                        processors=[kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                            type="type",
                
                            # the properties below are optional
                            parameters=[kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                                parameter_name="parameterName",
                                parameter_value="parameterValue"
                            )]
                        )]
                    ),
                    s3_backup_configuration=kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                        bucket_arn="bucketArn",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                            interval_in_seconds=123,
                            size_in_mBs=123
                        ),
                        cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                            enabled=False,
                            log_group_name="logGroupName",
                            log_stream_name="logStreamName"
                        ),
                        compression_format="compressionFormat",
                        encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                            kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                                awskms_key_arn="awskmsKeyArn"
                            ),
                            no_encryption_config="noEncryptionConfig"
                        ),
                        error_output_prefix="errorOutputPrefix",
                        prefix="prefix"
                    ),
                    s3_backup_mode="s3BackupMode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7faa411782bea929613482f29819c6479d5ad2f4416ea558d510fb9fd71eaa95)
                check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument buffering_hints", value=buffering_hints, expected_type=type_hints["buffering_hints"])
                check_type(argname="argument cloud_watch_logging_options", value=cloud_watch_logging_options, expected_type=type_hints["cloud_watch_logging_options"])
                check_type(argname="argument compression_format", value=compression_format, expected_type=type_hints["compression_format"])
                check_type(argname="argument custom_time_zone", value=custom_time_zone, expected_type=type_hints["custom_time_zone"])
                check_type(argname="argument data_format_conversion_configuration", value=data_format_conversion_configuration, expected_type=type_hints["data_format_conversion_configuration"])
                check_type(argname="argument dynamic_partitioning_configuration", value=dynamic_partitioning_configuration, expected_type=type_hints["dynamic_partitioning_configuration"])
                check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
                check_type(argname="argument error_output_prefix", value=error_output_prefix, expected_type=type_hints["error_output_prefix"])
                check_type(argname="argument file_extension", value=file_extension, expected_type=type_hints["file_extension"])
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
                check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
                check_type(argname="argument s3_backup_configuration", value=s3_backup_configuration, expected_type=type_hints["s3_backup_configuration"])
                check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_arn": bucket_arn,
                "role_arn": role_arn,
            }
            if buffering_hints is not None:
                self._values["buffering_hints"] = buffering_hints
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if compression_format is not None:
                self._values["compression_format"] = compression_format
            if custom_time_zone is not None:
                self._values["custom_time_zone"] = custom_time_zone
            if data_format_conversion_configuration is not None:
                self._values["data_format_conversion_configuration"] = data_format_conversion_configuration
            if dynamic_partitioning_configuration is not None:
                self._values["dynamic_partitioning_configuration"] = dynamic_partitioning_configuration
            if encryption_configuration is not None:
                self._values["encryption_configuration"] = encryption_configuration
            if error_output_prefix is not None:
                self._values["error_output_prefix"] = error_output_prefix
            if file_extension is not None:
                self._values["file_extension"] = file_extension
            if prefix is not None:
                self._values["prefix"] = prefix
            if processing_configuration is not None:
                self._values["processing_configuration"] = processing_configuration
            if s3_backup_configuration is not None:
                self._values["s3_backup_configuration"] = s3_backup_configuration
            if s3_backup_mode is not None:
                self._values["s3_backup_mode"] = s3_backup_mode

        @builtins.property
        def bucket_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Amazon S3 bucket.

            For constraints, see `ExtendedS3DestinationConfiguration <https://docs.aws.amazon.com/firehose/latest/APIReference/API_ExtendedS3DestinationConfiguration.html>`_ in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-bucketarn
            '''
            result = self._values.get("bucket_arn")
            assert result is not None, "Required property 'bucket_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the AWS credentials.

            For constraints, see `ExtendedS3DestinationConfiguration <https://docs.aws.amazon.com/firehose/latest/APIReference/API_ExtendedS3DestinationConfiguration.html>`_ in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def buffering_hints(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.BufferingHintsProperty"]]:
            '''The buffering option.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-bufferinghints
            '''
            result = self._values.get("buffering_hints")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.BufferingHintsProperty"]], result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''The Amazon CloudWatch logging options for your delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def compression_format(self) -> typing.Optional[builtins.str]:
            '''The compression format.

            If no value is specified, the default is ``UNCOMPRESSED`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-compressionformat
            '''
            result = self._values.get("compression_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def custom_time_zone(self) -> typing.Optional[builtins.str]:
            '''The time zone you prefer.

            UTC is the default.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-customtimezone
            '''
            result = self._values.get("custom_time_zone")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_format_conversion_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DataFormatConversionConfigurationProperty"]]:
            '''The serializer, deserializer, and schema for converting data from the JSON format to the Parquet or ORC format before writing it to Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-dataformatconversionconfiguration
            '''
            result = self._values.get("data_format_conversion_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DataFormatConversionConfigurationProperty"]], result)

        @builtins.property
        def dynamic_partitioning_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DynamicPartitioningConfigurationProperty"]]:
            '''The configuration of the dynamic partitioning mechanism that creates targeted data sets from the streaming data by partitioning it based on partition keys.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-dynamicpartitioningconfiguration
            '''
            result = self._values.get("dynamic_partitioning_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DynamicPartitioningConfigurationProperty"]], result)

        @builtins.property
        def encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.EncryptionConfigurationProperty"]]:
            '''The encryption configuration for the Kinesis Data Firehose delivery stream.

            The default value is ``NoEncryption`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-encryptionconfiguration
            '''
            result = self._values.get("encryption_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.EncryptionConfigurationProperty"]], result)

        @builtins.property
        def error_output_prefix(self) -> typing.Optional[builtins.str]:
            '''A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3.

            This prefix appears immediately following the bucket name. For information about how to specify this prefix, see `Custom Prefixes for Amazon S3 Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-erroroutputprefix
            '''
            result = self._values.get("error_output_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def file_extension(self) -> typing.Optional[builtins.str]:
            '''Specify a file extension.

            It will override the default file extension

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-fileextension
            '''
            result = self._values.get("file_extension")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''The ``YYYY/MM/DD/HH`` time format prefix is automatically used for delivered Amazon S3 files.

            For more information, see `ExtendedS3DestinationConfiguration <https://docs.aws.amazon.com/firehose/latest/APIReference/API_ExtendedS3DestinationConfiguration.html>`_ in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def processing_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]]:
            '''The data processing configuration for the Kinesis Data Firehose delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-processingconfiguration
            '''
            result = self._values.get("processing_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]], result)

        @builtins.property
        def s3_backup_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]]:
            '''The configuration for backup in Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-s3backupconfiguration
            '''
            result = self._values.get("s3_backup_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]], result)

        @builtins.property
        def s3_backup_mode(self) -> typing.Optional[builtins.str]:
            '''The Amazon S3 backup mode.

            After you create a delivery stream, you can update it to enable Amazon S3 backup if it is disabled. If backup is enabled, you can't update the delivery stream to disable it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-extendeds3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration-s3backupmode
            '''
            result = self._values.get("s3_backup_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExtendedS3DestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.HiveJsonSerDeProperty",
        jsii_struct_bases=[],
        name_mapping={"timestamp_formats": "timestampFormats"},
    )
    class HiveJsonSerDeProperty:
        def __init__(
            self,
            *,
            timestamp_formats: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The native Hive / HCatalog JsonSerDe.

            Used by Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the OpenX SerDe.

            :param timestamp_formats: Indicates how you want Firehose to parse the date and timestamps that may be present in your input data JSON. To specify these format strings, follow the pattern syntax of JodaTime's DateTimeFormat format strings. For more information, see `Class DateTimeFormat <https://docs.aws.amazon.com/https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html>`_ . You can also use the special value ``millis`` to parse timestamps in epoch milliseconds. If you don't specify a format, Firehose uses ``java.sql.Timestamp::valueOf`` by default.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-hivejsonserde.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                hive_json_ser_de_property = kinesisfirehose.CfnDeliveryStream.HiveJsonSerDeProperty(
                    timestamp_formats=["timestampFormats"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f8aed0e38a71aaf287d17202c1a15e108a76c336307d62f78aaec9e6482a117f)
                check_type(argname="argument timestamp_formats", value=timestamp_formats, expected_type=type_hints["timestamp_formats"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if timestamp_formats is not None:
                self._values["timestamp_formats"] = timestamp_formats

        @builtins.property
        def timestamp_formats(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Indicates how you want Firehose to parse the date and timestamps that may be present in your input data JSON.

            To specify these format strings, follow the pattern syntax of JodaTime's DateTimeFormat format strings. For more information, see `Class DateTimeFormat <https://docs.aws.amazon.com/https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html>`_ . You can also use the special value ``millis`` to parse timestamps in epoch milliseconds. If you don't specify a format, Firehose uses ``java.sql.Timestamp::valueOf`` by default.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-hivejsonserde.html#cfn-kinesisfirehose-deliverystream-hivejsonserde-timestampformats
            '''
            result = self._values.get("timestamp_formats")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HiveJsonSerDeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.HttpEndpointCommonAttributeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attribute_name": "attributeName",
            "attribute_value": "attributeValue",
        },
    )
    class HttpEndpointCommonAttributeProperty:
        def __init__(
            self,
            *,
            attribute_name: builtins.str,
            attribute_value: builtins.str,
        ) -> None:
            '''Describes the metadata that's delivered to the specified HTTP endpoint destination.

            Kinesis Firehose supports any custom HTTP endpoint or HTTP endpoints owned by supported third-party service providers, including Datadog, MongoDB, and New Relic.

            :param attribute_name: The name of the HTTP endpoint common attribute.
            :param attribute_value: The value of the HTTP endpoint common attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointcommonattribute.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                http_endpoint_common_attribute_property = kinesisfirehose.CfnDeliveryStream.HttpEndpointCommonAttributeProperty(
                    attribute_name="attributeName",
                    attribute_value="attributeValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4d04b9e64bbadb832ca77b64870e79e2910eb18ecbaf3d42b7d1c1b17fb3c160)
                check_type(argname="argument attribute_name", value=attribute_name, expected_type=type_hints["attribute_name"])
                check_type(argname="argument attribute_value", value=attribute_value, expected_type=type_hints["attribute_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "attribute_name": attribute_name,
                "attribute_value": attribute_value,
            }

        @builtins.property
        def attribute_name(self) -> builtins.str:
            '''The name of the HTTP endpoint common attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointcommonattribute.html#cfn-kinesisfirehose-deliverystream-httpendpointcommonattribute-attributename
            '''
            result = self._values.get("attribute_name")
            assert result is not None, "Required property 'attribute_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def attribute_value(self) -> builtins.str:
            '''The value of the HTTP endpoint common attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointcommonattribute.html#cfn-kinesisfirehose-deliverystream-httpendpointcommonattribute-attributevalue
            '''
            result = self._values.get("attribute_value")
            assert result is not None, "Required property 'attribute_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpEndpointCommonAttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.HttpEndpointConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"url": "url", "access_key": "accessKey", "name": "name"},
    )
    class HttpEndpointConfigurationProperty:
        def __init__(
            self,
            *,
            url: builtins.str,
            access_key: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the configuration of the HTTP endpoint to which Kinesis Firehose delivers data.

            Kinesis Firehose supports any custom HTTP endpoint or HTTP endpoints owned by supported third-party service providers, including Datadog, MongoDB, and New Relic.

            :param url: The URL of the HTTP endpoint selected as the destination.
            :param access_key: The access key required for Kinesis Firehose to authenticate with the HTTP endpoint selected as the destination.
            :param name: The name of the HTTP endpoint selected as the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                http_endpoint_configuration_property = kinesisfirehose.CfnDeliveryStream.HttpEndpointConfigurationProperty(
                    url="url",
                
                    # the properties below are optional
                    access_key="accessKey",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b0aeaa2e754e3362456fea60de1849d85d4913483f2324b0f89480dc7822dd8c)
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
                check_type(argname="argument access_key", value=access_key, expected_type=type_hints["access_key"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "url": url,
            }
            if access_key is not None:
                self._values["access_key"] = access_key
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def url(self) -> builtins.str:
            '''The URL of the HTTP endpoint selected as the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-url
            '''
            result = self._values.get("url")
            assert result is not None, "Required property 'url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def access_key(self) -> typing.Optional[builtins.str]:
            '''The access key required for Kinesis Firehose to authenticate with the HTTP endpoint selected as the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-accesskey
            '''
            result = self._values.get("access_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the HTTP endpoint selected as the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointconfiguration-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpEndpointConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_configuration": "endpointConfiguration",
            "s3_configuration": "s3Configuration",
            "buffering_hints": "bufferingHints",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "processing_configuration": "processingConfiguration",
            "request_configuration": "requestConfiguration",
            "retry_options": "retryOptions",
            "role_arn": "roleArn",
            "s3_backup_mode": "s3BackupMode",
        },
    )
    class HttpEndpointDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            endpoint_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.HttpEndpointConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.S3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.BufferingHintsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.CloudWatchLoggingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ProcessingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            request_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.HttpEndpointRequestConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.RetryOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            role_arn: typing.Optional[builtins.str] = None,
            s3_backup_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the configuration of the HTTP endpoint destination.

            Kinesis Firehose supports any custom HTTP endpoint or HTTP endpoints owned by supported third-party service providers, including Datadog, MongoDB, and New Relic.

            :param endpoint_configuration: The configuration of the HTTP endpoint selected as the destination.
            :param s3_configuration: Describes the configuration of a destination in Amazon S3.
            :param buffering_hints: The buffering options that can be used before data is delivered to the specified destination. Kinesis Data Firehose treats these options as hints, and it might choose to use more optimal values. The SizeInMBs and IntervalInSeconds parameters are optional. However, if you specify a value for one of them, you must also provide a value for the other.
            :param cloud_watch_logging_options: Describes the Amazon CloudWatch logging options for your delivery stream.
            :param processing_configuration: Describes the data processing configuration.
            :param request_configuration: The configuration of the request sent to the HTTP endpoint specified as the destination.
            :param retry_options: Describes the retry behavior in case Kinesis Data Firehose is unable to deliver data to the specified HTTP endpoint destination, or if it doesn't receive a valid acknowledgment of receipt from the specified HTTP endpoint destination.
            :param role_arn: Kinesis Data Firehose uses this IAM role for all the permissions that the delivery stream needs.
            :param s3_backup_mode: Describes the S3 bucket backup options for the data that Kinesis Data Firehose delivers to the HTTP endpoint destination. You can back up all documents (AllData) or only the documents that Kinesis Data Firehose could not deliver to the specified HTTP endpoint destination (FailedDataOnly).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                http_endpoint_destination_configuration_property = kinesisfirehose.CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty(
                    endpoint_configuration=kinesisfirehose.CfnDeliveryStream.HttpEndpointConfigurationProperty(
                        url="url",
                
                        # the properties below are optional
                        access_key="accessKey",
                        name="name"
                    ),
                    s3_configuration=kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                        bucket_arn="bucketArn",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                            interval_in_seconds=123,
                            size_in_mBs=123
                        ),
                        cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                            enabled=False,
                            log_group_name="logGroupName",
                            log_stream_name="logStreamName"
                        ),
                        compression_format="compressionFormat",
                        encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                            kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                                awskms_key_arn="awskmsKeyArn"
                            ),
                            no_encryption_config="noEncryptionConfig"
                        ),
                        error_output_prefix="errorOutputPrefix",
                        prefix="prefix"
                    ),
                
                    # the properties below are optional
                    buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                        interval_in_seconds=123,
                        size_in_mBs=123
                    ),
                    cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                        enabled=False,
                        log_group_name="logGroupName",
                        log_stream_name="logStreamName"
                    ),
                    processing_configuration=kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty(
                        enabled=False,
                        processors=[kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                            type="type",
                
                            # the properties below are optional
                            parameters=[kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                                parameter_name="parameterName",
                                parameter_value="parameterValue"
                            )]
                        )]
                    ),
                    request_configuration=kinesisfirehose.CfnDeliveryStream.HttpEndpointRequestConfigurationProperty(
                        common_attributes=[kinesisfirehose.CfnDeliveryStream.HttpEndpointCommonAttributeProperty(
                            attribute_name="attributeName",
                            attribute_value="attributeValue"
                        )],
                        content_encoding="contentEncoding"
                    ),
                    retry_options=kinesisfirehose.CfnDeliveryStream.RetryOptionsProperty(
                        duration_in_seconds=123
                    ),
                    role_arn="roleArn",
                    s3_backup_mode="s3BackupMode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6e8b3a25c8aa6cb1c905473fb8dd18a708e794918ae12a9a622993603b96ab8a)
                check_type(argname="argument endpoint_configuration", value=endpoint_configuration, expected_type=type_hints["endpoint_configuration"])
                check_type(argname="argument s3_configuration", value=s3_configuration, expected_type=type_hints["s3_configuration"])
                check_type(argname="argument buffering_hints", value=buffering_hints, expected_type=type_hints["buffering_hints"])
                check_type(argname="argument cloud_watch_logging_options", value=cloud_watch_logging_options, expected_type=type_hints["cloud_watch_logging_options"])
                check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
                check_type(argname="argument request_configuration", value=request_configuration, expected_type=type_hints["request_configuration"])
                check_type(argname="argument retry_options", value=retry_options, expected_type=type_hints["retry_options"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "endpoint_configuration": endpoint_configuration,
                "s3_configuration": s3_configuration,
            }
            if buffering_hints is not None:
                self._values["buffering_hints"] = buffering_hints
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if processing_configuration is not None:
                self._values["processing_configuration"] = processing_configuration
            if request_configuration is not None:
                self._values["request_configuration"] = request_configuration
            if retry_options is not None:
                self._values["retry_options"] = retry_options
            if role_arn is not None:
                self._values["role_arn"] = role_arn
            if s3_backup_mode is not None:
                self._values["s3_backup_mode"] = s3_backup_mode

        @builtins.property
        def endpoint_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.HttpEndpointConfigurationProperty"]:
            '''The configuration of the HTTP endpoint selected as the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-endpointconfiguration
            '''
            result = self._values.get("endpoint_configuration")
            assert result is not None, "Required property 'endpoint_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.HttpEndpointConfigurationProperty"], result)

        @builtins.property
        def s3_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]:
            '''Describes the configuration of a destination in Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-s3configuration
            '''
            result = self._values.get("s3_configuration")
            assert result is not None, "Required property 's3_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"], result)

        @builtins.property
        def buffering_hints(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.BufferingHintsProperty"]]:
            '''The buffering options that can be used before data is delivered to the specified destination.

            Kinesis Data Firehose treats these options as hints, and it might choose to use more optimal values. The SizeInMBs and IntervalInSeconds parameters are optional. However, if you specify a value for one of them, you must also provide a value for the other.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-bufferinghints
            '''
            result = self._values.get("buffering_hints")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.BufferingHintsProperty"]], result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''Describes the Amazon CloudWatch logging options for your delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def processing_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]]:
            '''Describes the data processing configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-processingconfiguration
            '''
            result = self._values.get("processing_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]], result)

        @builtins.property
        def request_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.HttpEndpointRequestConfigurationProperty"]]:
            '''The configuration of the request sent to the HTTP endpoint specified as the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-requestconfiguration
            '''
            result = self._values.get("request_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.HttpEndpointRequestConfigurationProperty"]], result)

        @builtins.property
        def retry_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.RetryOptionsProperty"]]:
            '''Describes the retry behavior in case Kinesis Data Firehose is unable to deliver data to the specified HTTP endpoint destination, or if it doesn't receive a valid acknowledgment of receipt from the specified HTTP endpoint destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-retryoptions
            '''
            result = self._values.get("retry_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.RetryOptionsProperty"]], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''Kinesis Data Firehose uses this IAM role for all the permissions that the delivery stream needs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_backup_mode(self) -> typing.Optional[builtins.str]:
            '''Describes the S3 bucket backup options for the data that Kinesis Data Firehose delivers to the HTTP endpoint destination.

            You can back up all documents (AllData) or only the documents that Kinesis Data Firehose could not deliver to the specified HTTP endpoint destination (FailedDataOnly).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration-s3backupmode
            '''
            result = self._values.get("s3_backup_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpEndpointDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.HttpEndpointRequestConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "common_attributes": "commonAttributes",
            "content_encoding": "contentEncoding",
        },
    )
    class HttpEndpointRequestConfigurationProperty:
        def __init__(
            self,
            *,
            common_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.HttpEndpointCommonAttributeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            content_encoding: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration of the HTTP endpoint request.

            Kinesis Firehose supports any custom HTTP endpoint or HTTP endpoints owned by supported third-party service providers, including Datadog, MongoDB, and New Relic.

            :param common_attributes: Describes the metadata sent to the HTTP endpoint destination.
            :param content_encoding: Kinesis Data Firehose uses the content encoding to compress the body of a request before sending the request to the destination. For more information, see Content-Encoding in MDN Web Docs, the official Mozilla documentation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointrequestconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                http_endpoint_request_configuration_property = kinesisfirehose.CfnDeliveryStream.HttpEndpointRequestConfigurationProperty(
                    common_attributes=[kinesisfirehose.CfnDeliveryStream.HttpEndpointCommonAttributeProperty(
                        attribute_name="attributeName",
                        attribute_value="attributeValue"
                    )],
                    content_encoding="contentEncoding"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4a9efa4d9f485d918f70adc5823c0a1caf4894264ec785a00d5ef0879e3c1177)
                check_type(argname="argument common_attributes", value=common_attributes, expected_type=type_hints["common_attributes"])
                check_type(argname="argument content_encoding", value=content_encoding, expected_type=type_hints["content_encoding"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if common_attributes is not None:
                self._values["common_attributes"] = common_attributes
            if content_encoding is not None:
                self._values["content_encoding"] = content_encoding

        @builtins.property
        def common_attributes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.HttpEndpointCommonAttributeProperty"]]]]:
            '''Describes the metadata sent to the HTTP endpoint destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointrequestconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointrequestconfiguration-commonattributes
            '''
            result = self._values.get("common_attributes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.HttpEndpointCommonAttributeProperty"]]]], result)

        @builtins.property
        def content_encoding(self) -> typing.Optional[builtins.str]:
            '''Kinesis Data Firehose uses the content encoding to compress the body of a request before sending the request to the destination.

            For more information, see Content-Encoding in MDN Web Docs, the official Mozilla documentation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-httpendpointrequestconfiguration.html#cfn-kinesisfirehose-deliverystream-httpendpointrequestconfiguration-contentencoding
            '''
            result = self._values.get("content_encoding")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpEndpointRequestConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.InputFormatConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"deserializer": "deserializer"},
    )
    class InputFormatConfigurationProperty:
        def __init__(
            self,
            *,
            deserializer: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.DeserializerProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the deserializer you want to use to convert the format of the input data.

            This parameter is required if ``Enabled`` is set to true.

            :param deserializer: Specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or the OpenX JSON SerDe. If both are non-null, the server rejects the request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-inputformatconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                input_format_configuration_property = kinesisfirehose.CfnDeliveryStream.InputFormatConfigurationProperty(
                    deserializer=kinesisfirehose.CfnDeliveryStream.DeserializerProperty(
                        hive_json_ser_de=kinesisfirehose.CfnDeliveryStream.HiveJsonSerDeProperty(
                            timestamp_formats=["timestampFormats"]
                        ),
                        open_xJson_ser_de=kinesisfirehose.CfnDeliveryStream.OpenXJsonSerDeProperty(
                            case_insensitive=False,
                            column_to_json_key_mappings={
                                "column_to_json_key_mappings_key": "columnToJsonKeyMappings"
                            },
                            convert_dots_in_json_keys_to_underscores=False
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dce5223aa97132391790e172c7c143f8a4c8df67b3b09df48eb0b1dff486468b)
                check_type(argname="argument deserializer", value=deserializer, expected_type=type_hints["deserializer"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if deserializer is not None:
                self._values["deserializer"] = deserializer

        @builtins.property
        def deserializer(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DeserializerProperty"]]:
            '''Specifies which deserializer to use.

            You can choose either the Apache Hive JSON SerDe or the OpenX JSON SerDe. If both are non-null, the server rejects the request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-inputformatconfiguration.html#cfn-kinesisfirehose-deliverystream-inputformatconfiguration-deserializer
            '''
            result = self._values.get("deserializer")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.DeserializerProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputFormatConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"awskms_key_arn": "awskmsKeyArn"},
    )
    class KMSEncryptionConfigProperty:
        def __init__(self, *, awskms_key_arn: builtins.str) -> None:
            '''The ``KMSEncryptionConfig`` property type specifies the AWS Key Management Service ( AWS KMS) encryption key that Amazon Simple Storage Service (Amazon S3) uses to encrypt data delivered by the Amazon Kinesis Data Firehose (Kinesis Data Firehose) stream.

            :param awskms_key_arn: The Amazon Resource Name (ARN) of the AWS KMS encryption key that Amazon S3 uses to encrypt data delivered by the Kinesis Data Firehose stream. The key must belong to the same region as the destination S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kmsencryptionconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                k_mSEncryption_config_property = kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                    awskms_key_arn="awskmsKeyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ca085a464bc9440602c605444adda1cec3d2059da145bca43dd610fba2e9a8be)
                check_type(argname="argument awskms_key_arn", value=awskms_key_arn, expected_type=type_hints["awskms_key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "awskms_key_arn": awskms_key_arn,
            }

        @builtins.property
        def awskms_key_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the AWS KMS encryption key that Amazon S3 uses to encrypt data delivered by the Kinesis Data Firehose stream.

            The key must belong to the same region as the destination S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kmsencryptionconfig.html#cfn-kinesisfirehose-deliverystream-kmsencryptionconfig-awskmskeyarn
            '''
            result = self._values.get("awskms_key_arn")
            assert result is not None, "Required property 'awskms_key_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KMSEncryptionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.KinesisStreamSourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kinesis_stream_arn": "kinesisStreamArn", "role_arn": "roleArn"},
    )
    class KinesisStreamSourceConfigurationProperty:
        def __init__(
            self,
            *,
            kinesis_stream_arn: builtins.str,
            role_arn: builtins.str,
        ) -> None:
            '''The ``KinesisStreamSourceConfiguration`` property type specifies the stream and role Amazon Resource Names (ARNs) for a Kinesis stream used as the source for a delivery stream.

            :param kinesis_stream_arn: The ARN of the source Kinesis data stream.
            :param role_arn: The ARN of the role that provides access to the source Kinesis data stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                kinesis_stream_source_configuration_property = kinesisfirehose.CfnDeliveryStream.KinesisStreamSourceConfigurationProperty(
                    kinesis_stream_arn="kinesisStreamArn",
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7ae1be427fa992bcfd551dc79aa5bba9af3c552f1661c763a814eb22ecd5dff7)
                check_type(argname="argument kinesis_stream_arn", value=kinesis_stream_arn, expected_type=type_hints["kinesis_stream_arn"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "kinesis_stream_arn": kinesis_stream_arn,
                "role_arn": role_arn,
            }

        @builtins.property
        def kinesis_stream_arn(self) -> builtins.str:
            '''The ARN of the source Kinesis data stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html#cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration-kinesisstreamarn
            '''
            result = self._values.get("kinesis_stream_arn")
            assert result is not None, "Required property 'kinesis_stream_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the role that provides access to the source Kinesis data stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html#cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisStreamSourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.MSKSourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authentication_configuration": "authenticationConfiguration",
            "msk_cluster_arn": "mskClusterArn",
            "topic_name": "topicName",
        },
    )
    class MSKSourceConfigurationProperty:
        def __init__(
            self,
            *,
            authentication_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.AuthenticationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            msk_cluster_arn: builtins.str,
            topic_name: builtins.str,
        ) -> None:
            '''The configuration for the Amazon MSK cluster to be used as the source for a delivery stream.

            :param authentication_configuration: The authentication configuration of the Amazon MSK cluster.
            :param msk_cluster_arn: The ARN of the Amazon MSK cluster.
            :param topic_name: The topic name within the Amazon MSK cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-msksourceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                m_sKSource_configuration_property = kinesisfirehose.CfnDeliveryStream.MSKSourceConfigurationProperty(
                    authentication_configuration=kinesisfirehose.CfnDeliveryStream.AuthenticationConfigurationProperty(
                        connectivity="connectivity",
                        role_arn="roleArn"
                    ),
                    msk_cluster_arn="mskClusterArn",
                    topic_name="topicName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7b2563c2a3f195e01ffbb501ca4b7d501c1fb934c35f08b019e248300a348473)
                check_type(argname="argument authentication_configuration", value=authentication_configuration, expected_type=type_hints["authentication_configuration"])
                check_type(argname="argument msk_cluster_arn", value=msk_cluster_arn, expected_type=type_hints["msk_cluster_arn"])
                check_type(argname="argument topic_name", value=topic_name, expected_type=type_hints["topic_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "authentication_configuration": authentication_configuration,
                "msk_cluster_arn": msk_cluster_arn,
                "topic_name": topic_name,
            }

        @builtins.property
        def authentication_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AuthenticationConfigurationProperty"]:
            '''The authentication configuration of the Amazon MSK cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-msksourceconfiguration.html#cfn-kinesisfirehose-deliverystream-msksourceconfiguration-authenticationconfiguration
            '''
            result = self._values.get("authentication_configuration")
            assert result is not None, "Required property 'authentication_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.AuthenticationConfigurationProperty"], result)

        @builtins.property
        def msk_cluster_arn(self) -> builtins.str:
            '''The ARN of the Amazon MSK cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-msksourceconfiguration.html#cfn-kinesisfirehose-deliverystream-msksourceconfiguration-mskclusterarn
            '''
            result = self._values.get("msk_cluster_arn")
            assert result is not None, "Required property 'msk_cluster_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def topic_name(self) -> builtins.str:
            '''The topic name within the Amazon MSK cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-msksourceconfiguration.html#cfn-kinesisfirehose-deliverystream-msksourceconfiguration-topicname
            '''
            result = self._values.get("topic_name")
            assert result is not None, "Required property 'topic_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MSKSourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.OpenXJsonSerDeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "case_insensitive": "caseInsensitive",
            "column_to_json_key_mappings": "columnToJsonKeyMappings",
            "convert_dots_in_json_keys_to_underscores": "convertDotsInJsonKeysToUnderscores",
        },
    )
    class OpenXJsonSerDeProperty:
        def __init__(
            self,
            *,
            case_insensitive: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            column_to_json_key_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            convert_dots_in_json_keys_to_underscores: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The OpenX SerDe.

            Used by Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the native Hive / HCatalog JsonSerDe.

            :param case_insensitive: When set to ``true`` , which is the default, Firehose converts JSON keys to lowercase before deserializing them.
            :param column_to_json_key_mappings: Maps column names to JSON keys that aren't identical to the column names. This is useful when the JSON contains keys that are Hive keywords. For example, ``timestamp`` is a Hive keyword. If you have a JSON key named ``timestamp`` , set this parameter to ``{"ts": "timestamp"}`` to map this key to a column named ``ts`` .
            :param convert_dots_in_json_keys_to_underscores: When set to ``true`` , specifies that the names of the keys include dots and that you want Firehose to replace them with underscores. This is useful because Apache Hive does not allow dots in column names. For example, if the JSON contains a key whose name is "a.b", you can define the column name to be "a_b" when using this option. The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-openxjsonserde.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                open_xJson_ser_de_property = kinesisfirehose.CfnDeliveryStream.OpenXJsonSerDeProperty(
                    case_insensitive=False,
                    column_to_json_key_mappings={
                        "column_to_json_key_mappings_key": "columnToJsonKeyMappings"
                    },
                    convert_dots_in_json_keys_to_underscores=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__65dc173b1d3e5c449c2f9ee9f1727428f35f33407e71da72ecdc48c19f3fb78c)
                check_type(argname="argument case_insensitive", value=case_insensitive, expected_type=type_hints["case_insensitive"])
                check_type(argname="argument column_to_json_key_mappings", value=column_to_json_key_mappings, expected_type=type_hints["column_to_json_key_mappings"])
                check_type(argname="argument convert_dots_in_json_keys_to_underscores", value=convert_dots_in_json_keys_to_underscores, expected_type=type_hints["convert_dots_in_json_keys_to_underscores"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if case_insensitive is not None:
                self._values["case_insensitive"] = case_insensitive
            if column_to_json_key_mappings is not None:
                self._values["column_to_json_key_mappings"] = column_to_json_key_mappings
            if convert_dots_in_json_keys_to_underscores is not None:
                self._values["convert_dots_in_json_keys_to_underscores"] = convert_dots_in_json_keys_to_underscores

        @builtins.property
        def case_insensitive(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When set to ``true`` , which is the default, Firehose converts JSON keys to lowercase before deserializing them.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-openxjsonserde.html#cfn-kinesisfirehose-deliverystream-openxjsonserde-caseinsensitive
            '''
            result = self._values.get("case_insensitive")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def column_to_json_key_mappings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''Maps column names to JSON keys that aren't identical to the column names.

            This is useful when the JSON contains keys that are Hive keywords. For example, ``timestamp`` is a Hive keyword. If you have a JSON key named ``timestamp`` , set this parameter to ``{"ts": "timestamp"}`` to map this key to a column named ``ts`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-openxjsonserde.html#cfn-kinesisfirehose-deliverystream-openxjsonserde-columntojsonkeymappings
            '''
            result = self._values.get("column_to_json_key_mappings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def convert_dots_in_json_keys_to_underscores(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When set to ``true`` , specifies that the names of the keys include dots and that you want Firehose to replace them with underscores.

            This is useful because Apache Hive does not allow dots in column names. For example, if the JSON contains a key whose name is "a.b", you can define the column name to be "a_b" when using this option.

            The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-openxjsonserde.html#cfn-kinesisfirehose-deliverystream-openxjsonserde-convertdotsinjsonkeystounderscores
            '''
            result = self._values.get("convert_dots_in_json_keys_to_underscores")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OpenXJsonSerDeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.OrcSerDeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "block_size_bytes": "blockSizeBytes",
            "bloom_filter_columns": "bloomFilterColumns",
            "bloom_filter_false_positive_probability": "bloomFilterFalsePositiveProbability",
            "compression": "compression",
            "dictionary_key_threshold": "dictionaryKeyThreshold",
            "enable_padding": "enablePadding",
            "format_version": "formatVersion",
            "padding_tolerance": "paddingTolerance",
            "row_index_stride": "rowIndexStride",
            "stripe_size_bytes": "stripeSizeBytes",
        },
    )
    class OrcSerDeProperty:
        def __init__(
            self,
            *,
            block_size_bytes: typing.Optional[jsii.Number] = None,
            bloom_filter_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
            bloom_filter_false_positive_probability: typing.Optional[jsii.Number] = None,
            compression: typing.Optional[builtins.str] = None,
            dictionary_key_threshold: typing.Optional[jsii.Number] = None,
            enable_padding: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            format_version: typing.Optional[builtins.str] = None,
            padding_tolerance: typing.Optional[jsii.Number] = None,
            row_index_stride: typing.Optional[jsii.Number] = None,
            stripe_size_bytes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''A serializer to use for converting data to the ORC format before storing it in Amazon S3.

            For more information, see `Apache ORC <https://docs.aws.amazon.com/https://orc.apache.org/docs/>`_ .

            :param block_size_bytes: The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Firehose uses this value for padding calculations.
            :param bloom_filter_columns: The column names for which you want Firehose to create bloom filters. The default is ``null`` .
            :param bloom_filter_false_positive_probability: The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.
            :param compression: The compression code to use over data blocks. The default is ``SNAPPY`` .
            :param dictionary_key_threshold: Represents the fraction of the total number of non-null rows. To turn off dictionary encoding, set this fraction to a number that is less than the number of distinct keys in a dictionary. To always use dictionary encoding, set this threshold to 1.
            :param enable_padding: Set this to ``true`` to indicate that you want stripes to be padded to the HDFS block boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is ``false`` .
            :param format_version: The version of the file to write. The possible values are ``V0_11`` and ``V0_12`` . The default is ``V0_12`` .
            :param padding_tolerance: A number between 0 and 1 that defines the tolerance for block padding as a decimal fraction of stripe size. The default value is 0.05, which means 5 percent of stripe size. For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256 MiB block. In such a case, if the available size within the block is more than 3.2 MiB, a new, smaller stripe is inserted to fit within that space. This ensures that no stripe crosses block boundaries and causes remote reads within a node-local task. Kinesis Data Firehose ignores this parameter when ``EnablePadding`` is ``false`` .
            :param row_index_stride: The number of rows between index entries. The default is 10,000 and the minimum is 1,000.
            :param stripe_size_bytes: The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                orc_ser_de_property = kinesisfirehose.CfnDeliveryStream.OrcSerDeProperty(
                    block_size_bytes=123,
                    bloom_filter_columns=["bloomFilterColumns"],
                    bloom_filter_false_positive_probability=123,
                    compression="compression",
                    dictionary_key_threshold=123,
                    enable_padding=False,
                    format_version="formatVersion",
                    padding_tolerance=123,
                    row_index_stride=123,
                    stripe_size_bytes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8a6f3732f1d1f7da40207abc3f87e65bccadac8f31c2f54e16aa9b9d2132fd6e)
                check_type(argname="argument block_size_bytes", value=block_size_bytes, expected_type=type_hints["block_size_bytes"])
                check_type(argname="argument bloom_filter_columns", value=bloom_filter_columns, expected_type=type_hints["bloom_filter_columns"])
                check_type(argname="argument bloom_filter_false_positive_probability", value=bloom_filter_false_positive_probability, expected_type=type_hints["bloom_filter_false_positive_probability"])
                check_type(argname="argument compression", value=compression, expected_type=type_hints["compression"])
                check_type(argname="argument dictionary_key_threshold", value=dictionary_key_threshold, expected_type=type_hints["dictionary_key_threshold"])
                check_type(argname="argument enable_padding", value=enable_padding, expected_type=type_hints["enable_padding"])
                check_type(argname="argument format_version", value=format_version, expected_type=type_hints["format_version"])
                check_type(argname="argument padding_tolerance", value=padding_tolerance, expected_type=type_hints["padding_tolerance"])
                check_type(argname="argument row_index_stride", value=row_index_stride, expected_type=type_hints["row_index_stride"])
                check_type(argname="argument stripe_size_bytes", value=stripe_size_bytes, expected_type=type_hints["stripe_size_bytes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if block_size_bytes is not None:
                self._values["block_size_bytes"] = block_size_bytes
            if bloom_filter_columns is not None:
                self._values["bloom_filter_columns"] = bloom_filter_columns
            if bloom_filter_false_positive_probability is not None:
                self._values["bloom_filter_false_positive_probability"] = bloom_filter_false_positive_probability
            if compression is not None:
                self._values["compression"] = compression
            if dictionary_key_threshold is not None:
                self._values["dictionary_key_threshold"] = dictionary_key_threshold
            if enable_padding is not None:
                self._values["enable_padding"] = enable_padding
            if format_version is not None:
                self._values["format_version"] = format_version
            if padding_tolerance is not None:
                self._values["padding_tolerance"] = padding_tolerance
            if row_index_stride is not None:
                self._values["row_index_stride"] = row_index_stride
            if stripe_size_bytes is not None:
                self._values["stripe_size_bytes"] = stripe_size_bytes

        @builtins.property
        def block_size_bytes(self) -> typing.Optional[jsii.Number]:
            '''The Hadoop Distributed File System (HDFS) block size.

            This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Firehose uses this value for padding calculations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-blocksizebytes
            '''
            result = self._values.get("block_size_bytes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def bloom_filter_columns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The column names for which you want Firehose to create bloom filters.

            The default is ``null`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-bloomfiltercolumns
            '''
            result = self._values.get("bloom_filter_columns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def bloom_filter_false_positive_probability(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''The Bloom filter false positive probability (FPP).

            The lower the FPP, the bigger the Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-bloomfilterfalsepositiveprobability
            '''
            result = self._values.get("bloom_filter_false_positive_probability")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def compression(self) -> typing.Optional[builtins.str]:
            '''The compression code to use over data blocks.

            The default is ``SNAPPY`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-compression
            '''
            result = self._values.get("compression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dictionary_key_threshold(self) -> typing.Optional[jsii.Number]:
            '''Represents the fraction of the total number of non-null rows.

            To turn off dictionary encoding, set this fraction to a number that is less than the number of distinct keys in a dictionary. To always use dictionary encoding, set this threshold to 1.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-dictionarykeythreshold
            '''
            result = self._values.get("dictionary_key_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def enable_padding(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set this to ``true`` to indicate that you want stripes to be padded to the HDFS block boundaries.

            This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-enablepadding
            '''
            result = self._values.get("enable_padding")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def format_version(self) -> typing.Optional[builtins.str]:
            '''The version of the file to write.

            The possible values are ``V0_11`` and ``V0_12`` . The default is ``V0_12`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-formatversion
            '''
            result = self._values.get("format_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def padding_tolerance(self) -> typing.Optional[jsii.Number]:
            '''A number between 0 and 1 that defines the tolerance for block padding as a decimal fraction of stripe size.

            The default value is 0.05, which means 5 percent of stripe size.

            For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256 MiB block. In such a case, if the available size within the block is more than 3.2 MiB, a new, smaller stripe is inserted to fit within that space. This ensures that no stripe crosses block boundaries and causes remote reads within a node-local task.

            Kinesis Data Firehose ignores this parameter when ``EnablePadding`` is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-paddingtolerance
            '''
            result = self._values.get("padding_tolerance")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def row_index_stride(self) -> typing.Optional[jsii.Number]:
            '''The number of rows between index entries.

            The default is 10,000 and the minimum is 1,000.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-rowindexstride
            '''
            result = self._values.get("row_index_stride")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def stripe_size_bytes(self) -> typing.Optional[jsii.Number]:
            '''The number of bytes in each stripe.

            The default is 64 MiB and the minimum is 8 MiB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-orcserde.html#cfn-kinesisfirehose-deliverystream-orcserde-stripesizebytes
            '''
            result = self._values.get("stripe_size_bytes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OrcSerDeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.OutputFormatConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"serializer": "serializer"},
    )
    class OutputFormatConfigurationProperty:
        def __init__(
            self,
            *,
            serializer: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.SerializerProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the serializer that you want Firehose to use to convert the format of your data before it writes it to Amazon S3.

            This parameter is required if ``Enabled`` is set to true.

            :param serializer: Specifies which serializer to use. You can choose either the ORC SerDe or the Parquet SerDe. If both are non-null, the server rejects the request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-outputformatconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                output_format_configuration_property = kinesisfirehose.CfnDeliveryStream.OutputFormatConfigurationProperty(
                    serializer=kinesisfirehose.CfnDeliveryStream.SerializerProperty(
                        orc_ser_de=kinesisfirehose.CfnDeliveryStream.OrcSerDeProperty(
                            block_size_bytes=123,
                            bloom_filter_columns=["bloomFilterColumns"],
                            bloom_filter_false_positive_probability=123,
                            compression="compression",
                            dictionary_key_threshold=123,
                            enable_padding=False,
                            format_version="formatVersion",
                            padding_tolerance=123,
                            row_index_stride=123,
                            stripe_size_bytes=123
                        ),
                        parquet_ser_de=kinesisfirehose.CfnDeliveryStream.ParquetSerDeProperty(
                            block_size_bytes=123,
                            compression="compression",
                            enable_dictionary_compression=False,
                            max_padding_bytes=123,
                            page_size_bytes=123,
                            writer_version="writerVersion"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3fcba637de22c6790633f7c4fdbfafe0f3cf2fcd07e8753fb333222a3b7916c2)
                check_type(argname="argument serializer", value=serializer, expected_type=type_hints["serializer"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if serializer is not None:
                self._values["serializer"] = serializer

        @builtins.property
        def serializer(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SerializerProperty"]]:
            '''Specifies which serializer to use.

            You can choose either the ORC SerDe or the Parquet SerDe. If both are non-null, the server rejects the request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-outputformatconfiguration.html#cfn-kinesisfirehose-deliverystream-outputformatconfiguration-serializer
            '''
            result = self._values.get("serializer")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SerializerProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputFormatConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.ParquetSerDeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "block_size_bytes": "blockSizeBytes",
            "compression": "compression",
            "enable_dictionary_compression": "enableDictionaryCompression",
            "max_padding_bytes": "maxPaddingBytes",
            "page_size_bytes": "pageSizeBytes",
            "writer_version": "writerVersion",
        },
    )
    class ParquetSerDeProperty:
        def __init__(
            self,
            *,
            block_size_bytes: typing.Optional[jsii.Number] = None,
            compression: typing.Optional[builtins.str] = None,
            enable_dictionary_compression: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            max_padding_bytes: typing.Optional[jsii.Number] = None,
            page_size_bytes: typing.Optional[jsii.Number] = None,
            writer_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A serializer to use for converting data to the Parquet format before storing it in Amazon S3.

            For more information, see `Apache Parquet <https://docs.aws.amazon.com/https://parquet.apache.org/docs/>`_ .

            :param block_size_bytes: The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Firehose uses this value for padding calculations.
            :param compression: The compression code to use over data blocks. The possible values are ``UNCOMPRESSED`` , ``SNAPPY`` , and ``GZIP`` , with the default being ``SNAPPY`` . Use ``SNAPPY`` for higher decompression speed. Use ``GZIP`` if the compression ratio is more important than speed.
            :param enable_dictionary_compression: Indicates whether to enable dictionary compression.
            :param max_padding_bytes: The maximum amount of padding to apply. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 0.
            :param page_size_bytes: The Parquet page size. Column chunks are divided into pages. A page is conceptually an indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB and the default is 1 MiB.
            :param writer_version: Indicates the version of row format to output. The possible values are ``V1`` and ``V2`` . The default is ``V1`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                parquet_ser_de_property = kinesisfirehose.CfnDeliveryStream.ParquetSerDeProperty(
                    block_size_bytes=123,
                    compression="compression",
                    enable_dictionary_compression=False,
                    max_padding_bytes=123,
                    page_size_bytes=123,
                    writer_version="writerVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d5e42046b59e857630ade1e52237b3f99ec5d3fcea0cff6ee85255354c8bc1a9)
                check_type(argname="argument block_size_bytes", value=block_size_bytes, expected_type=type_hints["block_size_bytes"])
                check_type(argname="argument compression", value=compression, expected_type=type_hints["compression"])
                check_type(argname="argument enable_dictionary_compression", value=enable_dictionary_compression, expected_type=type_hints["enable_dictionary_compression"])
                check_type(argname="argument max_padding_bytes", value=max_padding_bytes, expected_type=type_hints["max_padding_bytes"])
                check_type(argname="argument page_size_bytes", value=page_size_bytes, expected_type=type_hints["page_size_bytes"])
                check_type(argname="argument writer_version", value=writer_version, expected_type=type_hints["writer_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if block_size_bytes is not None:
                self._values["block_size_bytes"] = block_size_bytes
            if compression is not None:
                self._values["compression"] = compression
            if enable_dictionary_compression is not None:
                self._values["enable_dictionary_compression"] = enable_dictionary_compression
            if max_padding_bytes is not None:
                self._values["max_padding_bytes"] = max_padding_bytes
            if page_size_bytes is not None:
                self._values["page_size_bytes"] = page_size_bytes
            if writer_version is not None:
                self._values["writer_version"] = writer_version

        @builtins.property
        def block_size_bytes(self) -> typing.Optional[jsii.Number]:
            '''The Hadoop Distributed File System (HDFS) block size.

            This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Firehose uses this value for padding calculations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-blocksizebytes
            '''
            result = self._values.get("block_size_bytes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def compression(self) -> typing.Optional[builtins.str]:
            '''The compression code to use over data blocks.

            The possible values are ``UNCOMPRESSED`` , ``SNAPPY`` , and ``GZIP`` , with the default being ``SNAPPY`` . Use ``SNAPPY`` for higher decompression speed. Use ``GZIP`` if the compression ratio is more important than speed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-compression
            '''
            result = self._values.get("compression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enable_dictionary_compression(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether to enable dictionary compression.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-enabledictionarycompression
            '''
            result = self._values.get("enable_dictionary_compression")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def max_padding_bytes(self) -> typing.Optional[jsii.Number]:
            '''The maximum amount of padding to apply.

            This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 0.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-maxpaddingbytes
            '''
            result = self._values.get("max_padding_bytes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def page_size_bytes(self) -> typing.Optional[jsii.Number]:
            '''The Parquet page size.

            Column chunks are divided into pages. A page is conceptually an indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB and the default is 1 MiB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-pagesizebytes
            '''
            result = self._values.get("page_size_bytes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def writer_version(self) -> typing.Optional[builtins.str]:
            '''Indicates the version of row format to output.

            The possible values are ``V1`` and ``V2`` . The default is ``V1`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-parquetserde.html#cfn-kinesisfirehose-deliverystream-parquetserde-writerversion
            '''
            result = self._values.get("writer_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParquetSerDeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "processors": "processors"},
    )
    class ProcessingConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            processors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ProcessorProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The ``ProcessingConfiguration`` property configures data processing for an Amazon Kinesis Data Firehose delivery stream.

            :param enabled: Indicates whether data processing is enabled (true) or disabled (false).
            :param processors: The data processors.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                processing_configuration_property = kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty(
                    enabled=False,
                    processors=[kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                        type="type",
                
                        # the properties below are optional
                        parameters=[kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                            parameter_name="parameterName",
                            parameter_value="parameterValue"
                        )]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__47d08fb3fe02427fce54795dba1288ad02d1fec20884867948eae460f986d43d)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument processors", value=processors, expected_type=type_hints["processors"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if processors is not None:
                self._values["processors"] = processors

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether data processing is enabled (true) or disabled (false).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processingconfiguration.html#cfn-kinesisfirehose-deliverystream-processingconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def processors(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessorProperty"]]]]:
            '''The data processors.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processingconfiguration.html#cfn-kinesisfirehose-deliverystream-processingconfiguration-processors
            '''
            result = self._values.get("processors")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessorProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProcessingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "parameter_name": "parameterName",
            "parameter_value": "parameterValue",
        },
    )
    class ProcessorParameterProperty:
        def __init__(
            self,
            *,
            parameter_name: builtins.str,
            parameter_value: builtins.str,
        ) -> None:
            '''The ``ProcessorParameter`` property specifies a processor parameter in a data processor for an Amazon Kinesis Data Firehose delivery stream.

            :param parameter_name: The name of the parameter. Currently the following default values are supported: 3 for ``NumberOfRetries`` and 60 for the ``BufferIntervalInSeconds`` . The ``BufferSizeInMBs`` ranges between 0.2 MB and up to 3MB. The default buffering hint is 1MB for all destinations, except Splunk. For Splunk, the default buffering hint is 256 KB.
            :param parameter_value: The parameter value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processorparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                processor_parameter_property = kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                    parameter_name="parameterName",
                    parameter_value="parameterValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__29244e412176b0b05c7328e22087c12ec9670a06bdeda2a69994a31022941e39)
                check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
                check_type(argname="argument parameter_value", value=parameter_value, expected_type=type_hints["parameter_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "parameter_name": parameter_name,
                "parameter_value": parameter_value,
            }

        @builtins.property
        def parameter_name(self) -> builtins.str:
            '''The name of the parameter.

            Currently the following default values are supported: 3 for ``NumberOfRetries`` and 60 for the ``BufferIntervalInSeconds`` . The ``BufferSizeInMBs`` ranges between 0.2 MB and up to 3MB. The default buffering hint is 1MB for all destinations, except Splunk. For Splunk, the default buffering hint is 256 KB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processorparameter.html#cfn-kinesisfirehose-deliverystream-processorparameter-parametername
            '''
            result = self._values.get("parameter_name")
            assert result is not None, "Required property 'parameter_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameter_value(self) -> builtins.str:
            '''The parameter value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processorparameter.html#cfn-kinesisfirehose-deliverystream-processorparameter-parametervalue
            '''
            result = self._values.get("parameter_value")
            assert result is not None, "Required property 'parameter_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProcessorParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.ProcessorProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "parameters": "parameters"},
    )
    class ProcessorProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ProcessorParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The ``Processor`` property specifies a data processor for an Amazon Kinesis Data Firehose delivery stream.

            :param type: The type of processor. Valid values: ``Lambda`` .
            :param parameters: The processor parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                processor_property = kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                    type="type",
                
                    # the properties below are optional
                    parameters=[kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                        parameter_name="parameterName",
                        parameter_value="parameterValue"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__69c6d7cb07c53f27959cf35e3f4436c85b60c102a9d091138cad44aec29a7fc3)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if parameters is not None:
                self._values["parameters"] = parameters

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of processor.

            Valid values: ``Lambda`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processor.html#cfn-kinesisfirehose-deliverystream-processor-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessorParameterProperty"]]]]:
            '''The processor parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-processor.html#cfn-kinesisfirehose-deliverystream-processor-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessorParameterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProcessorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.RedshiftDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cluster_jdbcurl": "clusterJdbcurl",
            "copy_command": "copyCommand",
            "password": "password",
            "role_arn": "roleArn",
            "s3_configuration": "s3Configuration",
            "username": "username",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "processing_configuration": "processingConfiguration",
            "retry_options": "retryOptions",
            "s3_backup_configuration": "s3BackupConfiguration",
            "s3_backup_mode": "s3BackupMode",
        },
    )
    class RedshiftDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            cluster_jdbcurl: builtins.str,
            copy_command: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.CopyCommandProperty", typing.Dict[builtins.str, typing.Any]]],
            password: builtins.str,
            role_arn: builtins.str,
            s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.S3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            username: builtins.str,
            cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.CloudWatchLoggingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ProcessingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.RedshiftRetryOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_backup_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.S3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_backup_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``RedshiftDestinationConfiguration`` property type specifies an Amazon Redshift cluster to which Amazon Kinesis Data Firehose (Kinesis Data Firehose) delivers data.

            :param cluster_jdbcurl: The connection string that Kinesis Data Firehose uses to connect to the Amazon Redshift cluster.
            :param copy_command: Configures the Amazon Redshift ``COPY`` command that Kinesis Data Firehose uses to load data into the cluster from the Amazon S3 bucket.
            :param password: The password for the Amazon Redshift user that you specified in the ``Username`` property.
            :param role_arn: The ARN of the AWS Identity and Access Management (IAM) role that grants Kinesis Data Firehose access to your Amazon S3 bucket and AWS KMS (if you enable data encryption). For more information, see `Grant Kinesis Data Firehose Access to an Amazon Redshift Destination <https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#using-iam-rs>`_ in the *Amazon Kinesis Data Firehose Developer Guide* .
            :param s3_configuration: The S3 bucket where Kinesis Data Firehose first delivers data. After the data is in the bucket, Kinesis Data Firehose uses the ``COPY`` command to load the data into the Amazon Redshift cluster. For the Amazon S3 bucket's compression format, don't specify ``SNAPPY`` or ``ZIP`` because the Amazon Redshift ``COPY`` command doesn't support them.
            :param username: The Amazon Redshift user that has permission to access the Amazon Redshift cluster. This user must have ``INSERT`` privileges for copying data from the Amazon S3 bucket to the cluster.
            :param cloud_watch_logging_options: The CloudWatch logging options for your delivery stream.
            :param processing_configuration: The data processing configuration for the Kinesis Data Firehose delivery stream.
            :param retry_options: The retry behavior in case Firehose is unable to deliver documents to Amazon Redshift. Default value is 3600 (60 minutes).
            :param s3_backup_configuration: The configuration for backup in Amazon S3.
            :param s3_backup_mode: The Amazon S3 backup mode. After you create a delivery stream, you can update it to enable Amazon S3 backup if it is disabled. If backup is enabled, you can't update the delivery stream to disable it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                redshift_destination_configuration_property = kinesisfirehose.CfnDeliveryStream.RedshiftDestinationConfigurationProperty(
                    cluster_jdbcurl="clusterJdbcurl",
                    copy_command=kinesisfirehose.CfnDeliveryStream.CopyCommandProperty(
                        data_table_name="dataTableName",
                
                        # the properties below are optional
                        copy_options="copyOptions",
                        data_table_columns="dataTableColumns"
                    ),
                    password="password",
                    role_arn="roleArn",
                    s3_configuration=kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                        bucket_arn="bucketArn",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                            interval_in_seconds=123,
                            size_in_mBs=123
                        ),
                        cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                            enabled=False,
                            log_group_name="logGroupName",
                            log_stream_name="logStreamName"
                        ),
                        compression_format="compressionFormat",
                        encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                            kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                                awskms_key_arn="awskmsKeyArn"
                            ),
                            no_encryption_config="noEncryptionConfig"
                        ),
                        error_output_prefix="errorOutputPrefix",
                        prefix="prefix"
                    ),
                    username="username",
                
                    # the properties below are optional
                    cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                        enabled=False,
                        log_group_name="logGroupName",
                        log_stream_name="logStreamName"
                    ),
                    processing_configuration=kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty(
                        enabled=False,
                        processors=[kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                            type="type",
                
                            # the properties below are optional
                            parameters=[kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                                parameter_name="parameterName",
                                parameter_value="parameterValue"
                            )]
                        )]
                    ),
                    retry_options=kinesisfirehose.CfnDeliveryStream.RedshiftRetryOptionsProperty(
                        duration_in_seconds=123
                    ),
                    s3_backup_configuration=kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                        bucket_arn="bucketArn",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                            interval_in_seconds=123,
                            size_in_mBs=123
                        ),
                        cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                            enabled=False,
                            log_group_name="logGroupName",
                            log_stream_name="logStreamName"
                        ),
                        compression_format="compressionFormat",
                        encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                            kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                                awskms_key_arn="awskmsKeyArn"
                            ),
                            no_encryption_config="noEncryptionConfig"
                        ),
                        error_output_prefix="errorOutputPrefix",
                        prefix="prefix"
                    ),
                    s3_backup_mode="s3BackupMode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a05dc5298788a3b9496bc2e383242a0570183c6703c04af2c5e991292f2c58fa)
                check_type(argname="argument cluster_jdbcurl", value=cluster_jdbcurl, expected_type=type_hints["cluster_jdbcurl"])
                check_type(argname="argument copy_command", value=copy_command, expected_type=type_hints["copy_command"])
                check_type(argname="argument password", value=password, expected_type=type_hints["password"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument s3_configuration", value=s3_configuration, expected_type=type_hints["s3_configuration"])
                check_type(argname="argument username", value=username, expected_type=type_hints["username"])
                check_type(argname="argument cloud_watch_logging_options", value=cloud_watch_logging_options, expected_type=type_hints["cloud_watch_logging_options"])
                check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
                check_type(argname="argument retry_options", value=retry_options, expected_type=type_hints["retry_options"])
                check_type(argname="argument s3_backup_configuration", value=s3_backup_configuration, expected_type=type_hints["s3_backup_configuration"])
                check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cluster_jdbcurl": cluster_jdbcurl,
                "copy_command": copy_command,
                "password": password,
                "role_arn": role_arn,
                "s3_configuration": s3_configuration,
                "username": username,
            }
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if processing_configuration is not None:
                self._values["processing_configuration"] = processing_configuration
            if retry_options is not None:
                self._values["retry_options"] = retry_options
            if s3_backup_configuration is not None:
                self._values["s3_backup_configuration"] = s3_backup_configuration
            if s3_backup_mode is not None:
                self._values["s3_backup_mode"] = s3_backup_mode

        @builtins.property
        def cluster_jdbcurl(self) -> builtins.str:
            '''The connection string that Kinesis Data Firehose uses to connect to the Amazon Redshift cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-clusterjdbcurl
            '''
            result = self._values.get("cluster_jdbcurl")
            assert result is not None, "Required property 'cluster_jdbcurl' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def copy_command(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CopyCommandProperty"]:
            '''Configures the Amazon Redshift ``COPY`` command that Kinesis Data Firehose uses to load data into the cluster from the Amazon S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-copycommand
            '''
            result = self._values.get("copy_command")
            assert result is not None, "Required property 'copy_command' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CopyCommandProperty"], result)

        @builtins.property
        def password(self) -> builtins.str:
            '''The password for the Amazon Redshift user that you specified in the ``Username`` property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-password
            '''
            result = self._values.get("password")
            assert result is not None, "Required property 'password' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the AWS Identity and Access Management (IAM) role that grants Kinesis Data Firehose access to your Amazon S3 bucket and AWS KMS (if you enable data encryption).

            For more information, see `Grant Kinesis Data Firehose Access to an Amazon Redshift Destination <https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#using-iam-rs>`_ in the *Amazon Kinesis Data Firehose Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]:
            '''The S3 bucket where Kinesis Data Firehose first delivers data.

            After the data is in the bucket, Kinesis Data Firehose uses the ``COPY`` command to load the data into the Amazon Redshift cluster. For the Amazon S3 bucket's compression format, don't specify ``SNAPPY`` or ``ZIP`` because the Amazon Redshift ``COPY`` command doesn't support them.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-s3configuration
            '''
            result = self._values.get("s3_configuration")
            assert result is not None, "Required property 's3_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"], result)

        @builtins.property
        def username(self) -> builtins.str:
            '''The Amazon Redshift user that has permission to access the Amazon Redshift cluster.

            This user must have ``INSERT`` privileges for copying data from the Amazon S3 bucket to the cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-username
            '''
            result = self._values.get("username")
            assert result is not None, "Required property 'username' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''The CloudWatch logging options for your delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def processing_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]]:
            '''The data processing configuration for the Kinesis Data Firehose delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-processingconfiguration
            '''
            result = self._values.get("processing_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]], result)

        @builtins.property
        def retry_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.RedshiftRetryOptionsProperty"]]:
            '''The retry behavior in case Firehose is unable to deliver documents to Amazon Redshift.

            Default value is 3600 (60 minutes).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-retryoptions
            '''
            result = self._values.get("retry_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.RedshiftRetryOptionsProperty"]], result)

        @builtins.property
        def s3_backup_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]]:
            '''The configuration for backup in Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-s3backupconfiguration
            '''
            result = self._values.get("s3_backup_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]], result)

        @builtins.property
        def s3_backup_mode(self) -> typing.Optional[builtins.str]:
            '''The Amazon S3 backup mode.

            After you create a delivery stream, you can update it to enable Amazon S3 backup if it is disabled. If backup is enabled, you can't update the delivery stream to disable it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration-s3backupmode
            '''
            result = self._values.get("s3_backup_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.RedshiftRetryOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"duration_in_seconds": "durationInSeconds"},
    )
    class RedshiftRetryOptionsProperty:
        def __init__(
            self,
            *,
            duration_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Configures retry behavior in case Firehose is unable to deliver documents to Amazon Redshift.

            :param duration_in_seconds: The length of time during which Firehose retries delivery after a failure, starting from the initial request and including the first attempt. The default value is 3600 seconds (60 minutes). Firehose does not retry if the value of ``DurationInSeconds`` is 0 (zero) or if the first delivery attempt takes longer than the current value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftretryoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                redshift_retry_options_property = kinesisfirehose.CfnDeliveryStream.RedshiftRetryOptionsProperty(
                    duration_in_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d0656ad0d58c235ec01fb44e9e595a95164029cf26c86a1e17d49b3de0807568)
                check_type(argname="argument duration_in_seconds", value=duration_in_seconds, expected_type=type_hints["duration_in_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if duration_in_seconds is not None:
                self._values["duration_in_seconds"] = duration_in_seconds

        @builtins.property
        def duration_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The length of time during which Firehose retries delivery after a failure, starting from the initial request and including the first attempt.

            The default value is 3600 seconds (60 minutes). Firehose does not retry if the value of ``DurationInSeconds`` is 0 (zero) or if the first delivery attempt takes longer than the current value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-redshiftretryoptions.html#cfn-kinesisfirehose-deliverystream-redshiftretryoptions-durationinseconds
            '''
            result = self._values.get("duration_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftRetryOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.RetryOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"duration_in_seconds": "durationInSeconds"},
    )
    class RetryOptionsProperty:
        def __init__(
            self,
            *,
            duration_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes the retry behavior in case Kinesis Data Firehose is unable to deliver data to the specified HTTP endpoint destination, or if it doesn't receive a valid acknowledgment of receipt from the specified HTTP endpoint destination.

            Kinesis Firehose supports any custom HTTP endpoint or HTTP endpoints owned by supported third-party service providers, including Datadog, MongoDB, and New Relic.

            :param duration_in_seconds: The total amount of time that Kinesis Data Firehose spends on retries. This duration starts after the initial attempt to send data to the custom destination via HTTPS endpoint fails. It doesn't include the periods during which Kinesis Data Firehose waits for acknowledgment from the specified destination after each attempt.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-retryoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                retry_options_property = kinesisfirehose.CfnDeliveryStream.RetryOptionsProperty(
                    duration_in_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9f65ebaf68fad95eebbec4bb62ddc86711c9f922e5243b0ef218440713a1dbf3)
                check_type(argname="argument duration_in_seconds", value=duration_in_seconds, expected_type=type_hints["duration_in_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if duration_in_seconds is not None:
                self._values["duration_in_seconds"] = duration_in_seconds

        @builtins.property
        def duration_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The total amount of time that Kinesis Data Firehose spends on retries.

            This duration starts after the initial attempt to send data to the custom destination via HTTPS endpoint fails. It doesn't include the periods during which Kinesis Data Firehose waits for acknowledgment from the specified destination after each attempt.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-retryoptions.html#cfn-kinesisfirehose-deliverystream-retryoptions-durationinseconds
            '''
            result = self._values.get("duration_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RetryOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_arn": "bucketArn",
            "role_arn": "roleArn",
            "buffering_hints": "bufferingHints",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "compression_format": "compressionFormat",
            "encryption_configuration": "encryptionConfiguration",
            "error_output_prefix": "errorOutputPrefix",
            "prefix": "prefix",
        },
    )
    class S3DestinationConfigurationProperty:
        def __init__(
            self,
            *,
            bucket_arn: builtins.str,
            role_arn: builtins.str,
            buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.BufferingHintsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.CloudWatchLoggingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            compression_format: typing.Optional[builtins.str] = None,
            encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            error_output_prefix: typing.Optional[builtins.str] = None,
            prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``S3DestinationConfiguration`` property type specifies an Amazon Simple Storage Service (Amazon S3) destination to which Amazon Kinesis Data Firehose (Kinesis Data Firehose) delivers data.

            :param bucket_arn: The Amazon Resource Name (ARN) of the Amazon S3 bucket to send data to.
            :param role_arn: The ARN of an AWS Identity and Access Management (IAM) role that grants Kinesis Data Firehose access to your Amazon S3 bucket and AWS KMS (if you enable data encryption). For more information, see `Grant Kinesis Data Firehose Access to an Amazon S3 Destination <https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#using-iam-s3>`_ in the *Amazon Kinesis Data Firehose Developer Guide* .
            :param buffering_hints: Configures how Kinesis Data Firehose buffers incoming data while delivering it to the Amazon S3 bucket.
            :param cloud_watch_logging_options: The CloudWatch logging options for your delivery stream.
            :param compression_format: The type of compression that Kinesis Data Firehose uses to compress the data that it delivers to the Amazon S3 bucket. For valid values, see the ``CompressionFormat`` content for the `S3DestinationConfiguration <https://docs.aws.amazon.com/firehose/latest/APIReference/API_S3DestinationConfiguration.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .
            :param encryption_configuration: Configures Amazon Simple Storage Service (Amazon S3) server-side encryption. Kinesis Data Firehose uses AWS Key Management Service ( AWS KMS) to encrypt the data that it delivers to your Amazon S3 bucket.
            :param error_output_prefix: A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see `Custom Prefixes for Amazon S3 Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`_ .
            :param prefix: A prefix that Kinesis Data Firehose adds to the files that it delivers to the Amazon S3 bucket. The prefix helps you identify the files that Kinesis Data Firehose delivered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                s3_destination_configuration_property = kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                    bucket_arn="bucketArn",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                        interval_in_seconds=123,
                        size_in_mBs=123
                    ),
                    cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                        enabled=False,
                        log_group_name="logGroupName",
                        log_stream_name="logStreamName"
                    ),
                    compression_format="compressionFormat",
                    encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                        kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                            awskms_key_arn="awskmsKeyArn"
                        ),
                        no_encryption_config="noEncryptionConfig"
                    ),
                    error_output_prefix="errorOutputPrefix",
                    prefix="prefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8569fcc15b3b4467365ecb9c23c43fe8704a4b9efea3337dfd60994daf97d928)
                check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument buffering_hints", value=buffering_hints, expected_type=type_hints["buffering_hints"])
                check_type(argname="argument cloud_watch_logging_options", value=cloud_watch_logging_options, expected_type=type_hints["cloud_watch_logging_options"])
                check_type(argname="argument compression_format", value=compression_format, expected_type=type_hints["compression_format"])
                check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
                check_type(argname="argument error_output_prefix", value=error_output_prefix, expected_type=type_hints["error_output_prefix"])
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_arn": bucket_arn,
                "role_arn": role_arn,
            }
            if buffering_hints is not None:
                self._values["buffering_hints"] = buffering_hints
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if compression_format is not None:
                self._values["compression_format"] = compression_format
            if encryption_configuration is not None:
                self._values["encryption_configuration"] = encryption_configuration
            if error_output_prefix is not None:
                self._values["error_output_prefix"] = error_output_prefix
            if prefix is not None:
                self._values["prefix"] = prefix

        @builtins.property
        def bucket_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Amazon S3 bucket to send data to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-bucketarn
            '''
            result = self._values.get("bucket_arn")
            assert result is not None, "Required property 'bucket_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of an AWS Identity and Access Management (IAM) role that grants Kinesis Data Firehose access to your Amazon S3 bucket and AWS KMS (if you enable data encryption).

            For more information, see `Grant Kinesis Data Firehose Access to an Amazon S3 Destination <https://docs.aws.amazon.com/firehose/latest/dev/controlling-access.html#using-iam-s3>`_ in the *Amazon Kinesis Data Firehose Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def buffering_hints(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.BufferingHintsProperty"]]:
            '''Configures how Kinesis Data Firehose buffers incoming data while delivering it to the Amazon S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-bufferinghints
            '''
            result = self._values.get("buffering_hints")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.BufferingHintsProperty"]], result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''The CloudWatch logging options for your delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def compression_format(self) -> typing.Optional[builtins.str]:
            '''The type of compression that Kinesis Data Firehose uses to compress the data that it delivers to the Amazon S3 bucket.

            For valid values, see the ``CompressionFormat`` content for the `S3DestinationConfiguration <https://docs.aws.amazon.com/firehose/latest/APIReference/API_S3DestinationConfiguration.html>`_ data type in the *Amazon Kinesis Data Firehose API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-compressionformat
            '''
            result = self._values.get("compression_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.EncryptionConfigurationProperty"]]:
            '''Configures Amazon Simple Storage Service (Amazon S3) server-side encryption.

            Kinesis Data Firehose uses AWS Key Management Service ( AWS KMS) to encrypt the data that it delivers to your Amazon S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-encryptionconfiguration
            '''
            result = self._values.get("encryption_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.EncryptionConfigurationProperty"]], result)

        @builtins.property
        def error_output_prefix(self) -> typing.Optional[builtins.str]:
            '''A prefix that Kinesis Data Firehose evaluates and adds to failed records before writing them to S3.

            This prefix appears immediately following the bucket name. For information about how to specify this prefix, see `Custom Prefixes for Amazon S3 Objects <https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-erroroutputprefix
            '''
            result = self._values.get("error_output_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''A prefix that Kinesis Data Firehose adds to the files that it delivers to the Amazon S3 bucket.

            The prefix helps you identify the files that Kinesis Data Firehose delivered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-s3destinationconfiguration.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3DestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.SchemaConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "catalog_id": "catalogId",
            "database_name": "databaseName",
            "region": "region",
            "role_arn": "roleArn",
            "table_name": "tableName",
            "version_id": "versionId",
        },
    )
    class SchemaConfigurationProperty:
        def __init__(
            self,
            *,
            catalog_id: typing.Optional[builtins.str] = None,
            database_name: typing.Optional[builtins.str] = None,
            region: typing.Optional[builtins.str] = None,
            role_arn: typing.Optional[builtins.str] = None,
            table_name: typing.Optional[builtins.str] = None,
            version_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the schema to which you want Firehose to configure your data before it writes it to Amazon S3.

            This parameter is required if ``Enabled`` is set to true.

            :param catalog_id: The ID of the AWS Glue Data Catalog. If you don't supply this, the AWS account ID is used by default.
            :param database_name: Specifies the name of the AWS Glue database that contains the schema for the output data. .. epigraph:: If the ``SchemaConfiguration`` request parameter is used as part of invoking the ``CreateDeliveryStream`` API, then the ``DatabaseName`` property is required and its value must be specified.
            :param region: If you don't specify an AWS Region, the default is the current Region.
            :param role_arn: The role that Firehose can use to access AWS Glue. This role must be in the same account you use for Firehose. Cross-account roles aren't allowed. .. epigraph:: If the ``SchemaConfiguration`` request parameter is used as part of invoking the ``CreateDeliveryStream`` API, then the ``RoleARN`` property is required and its value must be specified.
            :param table_name: Specifies the AWS Glue table that contains the column information that constitutes your data schema. .. epigraph:: If the ``SchemaConfiguration`` request parameter is used as part of invoking the ``CreateDeliveryStream`` API, then the ``TableName`` property is required and its value must be specified.
            :param version_id: Specifies the table version for the output data schema. If you don't specify this version ID, or if you set it to ``LATEST`` , Firehose uses the most recent version. This means that any updates to the table are automatically picked up.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                schema_configuration_property = kinesisfirehose.CfnDeliveryStream.SchemaConfigurationProperty(
                    catalog_id="catalogId",
                    database_name="databaseName",
                    region="region",
                    role_arn="roleArn",
                    table_name="tableName",
                    version_id="versionId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c1389c57283b687c62069951b51187332947eeb24f5fcb8781af71c2b3e5d657)
                check_type(argname="argument catalog_id", value=catalog_id, expected_type=type_hints["catalog_id"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
                check_type(argname="argument version_id", value=version_id, expected_type=type_hints["version_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if catalog_id is not None:
                self._values["catalog_id"] = catalog_id
            if database_name is not None:
                self._values["database_name"] = database_name
            if region is not None:
                self._values["region"] = region
            if role_arn is not None:
                self._values["role_arn"] = role_arn
            if table_name is not None:
                self._values["table_name"] = table_name
            if version_id is not None:
                self._values["version_id"] = version_id

        @builtins.property
        def catalog_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the AWS Glue Data Catalog.

            If you don't supply this, the AWS account ID is used by default.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-catalogid
            '''
            result = self._values.get("catalog_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''Specifies the name of the AWS Glue database that contains the schema for the output data.

            .. epigraph::

               If the ``SchemaConfiguration`` request parameter is used as part of invoking the ``CreateDeliveryStream`` API, then the ``DatabaseName`` property is required and its value must be specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def region(self) -> typing.Optional[builtins.str]:
            '''If you don't specify an AWS Region, the default is the current Region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-region
            '''
            result = self._values.get("region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''The role that Firehose can use to access AWS Glue.

            This role must be in the same account you use for Firehose. Cross-account roles aren't allowed.
            .. epigraph::

               If the ``SchemaConfiguration`` request parameter is used as part of invoking the ``CreateDeliveryStream`` API, then the ``RoleARN`` property is required and its value must be specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def table_name(self) -> typing.Optional[builtins.str]:
            '''Specifies the AWS Glue table that contains the column information that constitutes your data schema.

            .. epigraph::

               If the ``SchemaConfiguration`` request parameter is used as part of invoking the ``CreateDeliveryStream`` API, then the ``TableName`` property is required and its value must be specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-tablename
            '''
            result = self._values.get("table_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version_id(self) -> typing.Optional[builtins.str]:
            '''Specifies the table version for the output data schema.

            If you don't specify this version ID, or if you set it to ``LATEST`` , Firehose uses the most recent version. This means that any updates to the table are automatically picked up.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-schemaconfiguration.html#cfn-kinesisfirehose-deliverystream-schemaconfiguration-versionid
            '''
            result = self._values.get("version_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SchemaConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.SerializerProperty",
        jsii_struct_bases=[],
        name_mapping={"orc_ser_de": "orcSerDe", "parquet_ser_de": "parquetSerDe"},
    )
    class SerializerProperty:
        def __init__(
            self,
            *,
            orc_ser_de: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.OrcSerDeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            parquet_ser_de: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ParquetSerDeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The serializer that you want Firehose to use to convert data to the target format before writing it to Amazon S3.

            Firehose supports two types of serializers: the `ORC SerDe <https://docs.aws.amazon.com/https://hive.apache.org/javadocs/r1.2.2/api/org/apache/hadoop/hive/ql/io/orc/OrcSerde.html>`_ and the `Parquet SerDe <https://docs.aws.amazon.com/https://hive.apache.org/javadocs/r1.2.2/api/org/apache/hadoop/hive/ql/io/parquet/serde/ParquetHiveSerDe.html>`_ .

            :param orc_ser_de: A serializer to use for converting data to the ORC format before storing it in Amazon S3. For more information, see `Apache ORC <https://docs.aws.amazon.com/https://orc.apache.org/docs/>`_ .
            :param parquet_ser_de: A serializer to use for converting data to the Parquet format before storing it in Amazon S3. For more information, see `Apache Parquet <https://docs.aws.amazon.com/https://parquet.apache.org/documentation/latest/>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-serializer.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                serializer_property = kinesisfirehose.CfnDeliveryStream.SerializerProperty(
                    orc_ser_de=kinesisfirehose.CfnDeliveryStream.OrcSerDeProperty(
                        block_size_bytes=123,
                        bloom_filter_columns=["bloomFilterColumns"],
                        bloom_filter_false_positive_probability=123,
                        compression="compression",
                        dictionary_key_threshold=123,
                        enable_padding=False,
                        format_version="formatVersion",
                        padding_tolerance=123,
                        row_index_stride=123,
                        stripe_size_bytes=123
                    ),
                    parquet_ser_de=kinesisfirehose.CfnDeliveryStream.ParquetSerDeProperty(
                        block_size_bytes=123,
                        compression="compression",
                        enable_dictionary_compression=False,
                        max_padding_bytes=123,
                        page_size_bytes=123,
                        writer_version="writerVersion"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__706925197a1b663cd9be8234e85ce2780b58d7bf71737c801e0c393104407464)
                check_type(argname="argument orc_ser_de", value=orc_ser_de, expected_type=type_hints["orc_ser_de"])
                check_type(argname="argument parquet_ser_de", value=parquet_ser_de, expected_type=type_hints["parquet_ser_de"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if orc_ser_de is not None:
                self._values["orc_ser_de"] = orc_ser_de
            if parquet_ser_de is not None:
                self._values["parquet_ser_de"] = parquet_ser_de

        @builtins.property
        def orc_ser_de(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.OrcSerDeProperty"]]:
            '''A serializer to use for converting data to the ORC format before storing it in Amazon S3.

            For more information, see `Apache ORC <https://docs.aws.amazon.com/https://orc.apache.org/docs/>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-serializer.html#cfn-kinesisfirehose-deliverystream-serializer-orcserde
            '''
            result = self._values.get("orc_ser_de")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.OrcSerDeProperty"]], result)

        @builtins.property
        def parquet_ser_de(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ParquetSerDeProperty"]]:
            '''A serializer to use for converting data to the Parquet format before storing it in Amazon S3.

            For more information, see `Apache Parquet <https://docs.aws.amazon.com/https://parquet.apache.org/documentation/latest/>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-serializer.html#cfn-kinesisfirehose-deliverystream-serializer-parquetserde
            '''
            result = self._values.get("parquet_ser_de")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ParquetSerDeProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SerializerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.SnowflakeDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_url": "accountUrl",
            "database": "database",
            "private_key": "privateKey",
            "role_arn": "roleArn",
            "s3_configuration": "s3Configuration",
            "schema": "schema",
            "table": "table",
            "user": "user",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "content_column_name": "contentColumnName",
            "data_loading_option": "dataLoadingOption",
            "key_passphrase": "keyPassphrase",
            "meta_data_column_name": "metaDataColumnName",
            "processing_configuration": "processingConfiguration",
            "retry_options": "retryOptions",
            "s3_backup_mode": "s3BackupMode",
            "snowflake_role_configuration": "snowflakeRoleConfiguration",
            "snowflake_vpc_configuration": "snowflakeVpcConfiguration",
        },
    )
    class SnowflakeDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            account_url: builtins.str,
            database: builtins.str,
            private_key: builtins.str,
            role_arn: builtins.str,
            s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.S3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            schema: builtins.str,
            table: builtins.str,
            user: builtins.str,
            cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.CloudWatchLoggingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            content_column_name: typing.Optional[builtins.str] = None,
            data_loading_option: typing.Optional[builtins.str] = None,
            key_passphrase: typing.Optional[builtins.str] = None,
            meta_data_column_name: typing.Optional[builtins.str] = None,
            processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ProcessingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.SnowflakeRetryOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_backup_mode: typing.Optional[builtins.str] = None,
            snowflake_role_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.SnowflakeRoleConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            snowflake_vpc_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.SnowflakeVpcConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configure Snowflake destination.

            :param account_url: URL for accessing your Snowflake account. This URL must include your `account identifier <https://docs.aws.amazon.com/https://docs.snowflake.com/en/user-guide/admin-account-identifier>`_ . Note that the protocol (https://) and port number are optional.
            :param database: All data in Snowflake is maintained in databases.
            :param private_key: The private key used to encrypt your Snowflake client. For information, see `Using Key Pair Authentication & Key Rotation <https://docs.aws.amazon.com/https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-configuration#using-key-pair-authentication-key-rotation>`_ .
            :param role_arn: The Amazon Resource Name (ARN) of the Snowflake role.
            :param s3_configuration: 
            :param schema: Each database consists of one or more schemas, which are logical groupings of database objects, such as tables and views.
            :param table: All data in Snowflake is stored in database tables, logically structured as collections of columns and rows.
            :param user: User login name for the Snowflake account.
            :param cloud_watch_logging_options: 
            :param content_column_name: The name of the record content column.
            :param data_loading_option: Choose to load JSON keys mapped to table column names or choose to split the JSON payload where content is mapped to a record content column and source metadata is mapped to a record metadata column.
            :param key_passphrase: Passphrase to decrypt the private key when the key is encrypted. For information, see `Using Key Pair Authentication & Key Rotation <https://docs.aws.amazon.com/https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-configuration#using-key-pair-authentication-key-rotation>`_ .
            :param meta_data_column_name: The name of the record metadata column.
            :param processing_configuration: 
            :param retry_options: The time period where Firehose will retry sending data to the chosen HTTP endpoint.
            :param s3_backup_mode: Choose an S3 backup mode.
            :param snowflake_role_configuration: Optionally configure a Snowflake role. Otherwise the default user role will be used.
            :param snowflake_vpc_configuration: The VPCE ID for Firehose to privately connect with Snowflake. The ID format is com.amazonaws.vpce.[region].vpce-svc-<[id]>. For more information, see `Amazon PrivateLink & Snowflake <https://docs.aws.amazon.com/https://docs.snowflake.com/en/user-guide/admin-security-privatelink>`_

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                snowflake_destination_configuration_property = kinesisfirehose.CfnDeliveryStream.SnowflakeDestinationConfigurationProperty(
                    account_url="accountUrl",
                    database="database",
                    private_key="privateKey",
                    role_arn="roleArn",
                    s3_configuration=kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                        bucket_arn="bucketArn",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                            interval_in_seconds=123,
                            size_in_mBs=123
                        ),
                        cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                            enabled=False,
                            log_group_name="logGroupName",
                            log_stream_name="logStreamName"
                        ),
                        compression_format="compressionFormat",
                        encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                            kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                                awskms_key_arn="awskmsKeyArn"
                            ),
                            no_encryption_config="noEncryptionConfig"
                        ),
                        error_output_prefix="errorOutputPrefix",
                        prefix="prefix"
                    ),
                    schema="schema",
                    table="table",
                    user="user",
                
                    # the properties below are optional
                    cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                        enabled=False,
                        log_group_name="logGroupName",
                        log_stream_name="logStreamName"
                    ),
                    content_column_name="contentColumnName",
                    data_loading_option="dataLoadingOption",
                    key_passphrase="keyPassphrase",
                    meta_data_column_name="metaDataColumnName",
                    processing_configuration=kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty(
                        enabled=False,
                        processors=[kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                            type="type",
                
                            # the properties below are optional
                            parameters=[kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                                parameter_name="parameterName",
                                parameter_value="parameterValue"
                            )]
                        )]
                    ),
                    retry_options=kinesisfirehose.CfnDeliveryStream.SnowflakeRetryOptionsProperty(
                        duration_in_seconds=123
                    ),
                    s3_backup_mode="s3BackupMode",
                    snowflake_role_configuration=kinesisfirehose.CfnDeliveryStream.SnowflakeRoleConfigurationProperty(
                        enabled=False,
                        snowflake_role="snowflakeRole"
                    ),
                    snowflake_vpc_configuration=kinesisfirehose.CfnDeliveryStream.SnowflakeVpcConfigurationProperty(
                        private_link_vpce_id="privateLinkVpceId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9743b3910a7f4b6edd05f7d4a76aa45c5a9f674a473fcf4c8c046e1d8d64cb53)
                check_type(argname="argument account_url", value=account_url, expected_type=type_hints["account_url"])
                check_type(argname="argument database", value=database, expected_type=type_hints["database"])
                check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument s3_configuration", value=s3_configuration, expected_type=type_hints["s3_configuration"])
                check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
                check_type(argname="argument table", value=table, expected_type=type_hints["table"])
                check_type(argname="argument user", value=user, expected_type=type_hints["user"])
                check_type(argname="argument cloud_watch_logging_options", value=cloud_watch_logging_options, expected_type=type_hints["cloud_watch_logging_options"])
                check_type(argname="argument content_column_name", value=content_column_name, expected_type=type_hints["content_column_name"])
                check_type(argname="argument data_loading_option", value=data_loading_option, expected_type=type_hints["data_loading_option"])
                check_type(argname="argument key_passphrase", value=key_passphrase, expected_type=type_hints["key_passphrase"])
                check_type(argname="argument meta_data_column_name", value=meta_data_column_name, expected_type=type_hints["meta_data_column_name"])
                check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
                check_type(argname="argument retry_options", value=retry_options, expected_type=type_hints["retry_options"])
                check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
                check_type(argname="argument snowflake_role_configuration", value=snowflake_role_configuration, expected_type=type_hints["snowflake_role_configuration"])
                check_type(argname="argument snowflake_vpc_configuration", value=snowflake_vpc_configuration, expected_type=type_hints["snowflake_vpc_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "account_url": account_url,
                "database": database,
                "private_key": private_key,
                "role_arn": role_arn,
                "s3_configuration": s3_configuration,
                "schema": schema,
                "table": table,
                "user": user,
            }
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if content_column_name is not None:
                self._values["content_column_name"] = content_column_name
            if data_loading_option is not None:
                self._values["data_loading_option"] = data_loading_option
            if key_passphrase is not None:
                self._values["key_passphrase"] = key_passphrase
            if meta_data_column_name is not None:
                self._values["meta_data_column_name"] = meta_data_column_name
            if processing_configuration is not None:
                self._values["processing_configuration"] = processing_configuration
            if retry_options is not None:
                self._values["retry_options"] = retry_options
            if s3_backup_mode is not None:
                self._values["s3_backup_mode"] = s3_backup_mode
            if snowflake_role_configuration is not None:
                self._values["snowflake_role_configuration"] = snowflake_role_configuration
            if snowflake_vpc_configuration is not None:
                self._values["snowflake_vpc_configuration"] = snowflake_vpc_configuration

        @builtins.property
        def account_url(self) -> builtins.str:
            '''URL for accessing your Snowflake account.

            This URL must include your `account identifier <https://docs.aws.amazon.com/https://docs.snowflake.com/en/user-guide/admin-account-identifier>`_ . Note that the protocol (https://) and port number are optional.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-accounturl
            '''
            result = self._values.get("account_url")
            assert result is not None, "Required property 'account_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def database(self) -> builtins.str:
            '''All data in Snowflake is maintained in databases.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-database
            '''
            result = self._values.get("database")
            assert result is not None, "Required property 'database' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def private_key(self) -> builtins.str:
            '''The private key used to encrypt your Snowflake client.

            For information, see `Using Key Pair Authentication & Key Rotation <https://docs.aws.amazon.com/https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-configuration#using-key-pair-authentication-key-rotation>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-privatekey
            '''
            result = self._values.get("private_key")
            assert result is not None, "Required property 'private_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Snowflake role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-s3configuration
            '''
            result = self._values.get("s3_configuration")
            assert result is not None, "Required property 's3_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"], result)

        @builtins.property
        def schema(self) -> builtins.str:
            '''Each database consists of one or more schemas, which are logical groupings of database objects, such as tables and views.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-schema
            '''
            result = self._values.get("schema")
            assert result is not None, "Required property 'schema' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table(self) -> builtins.str:
            '''All data in Snowflake is stored in database tables, logically structured as collections of columns and rows.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-table
            '''
            result = self._values.get("table")
            assert result is not None, "Required property 'table' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def user(self) -> builtins.str:
            '''User login name for the Snowflake account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-user
            '''
            result = self._values.get("user")
            assert result is not None, "Required property 'user' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def content_column_name(self) -> typing.Optional[builtins.str]:
            '''The name of the record content column.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-contentcolumnname
            '''
            result = self._values.get("content_column_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_loading_option(self) -> typing.Optional[builtins.str]:
            '''Choose to load JSON keys mapped to table column names or choose to split the JSON payload where content is mapped to a record content column and source metadata is mapped to a record metadata column.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-dataloadingoption
            '''
            result = self._values.get("data_loading_option")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key_passphrase(self) -> typing.Optional[builtins.str]:
            '''Passphrase to decrypt the private key when the key is encrypted.

            For information, see `Using Key Pair Authentication & Key Rotation <https://docs.aws.amazon.com/https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-configuration#using-key-pair-authentication-key-rotation>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-keypassphrase
            '''
            result = self._values.get("key_passphrase")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def meta_data_column_name(self) -> typing.Optional[builtins.str]:
            '''The name of the record metadata column.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-metadatacolumnname
            '''
            result = self._values.get("meta_data_column_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def processing_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-processingconfiguration
            '''
            result = self._values.get("processing_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]], result)

        @builtins.property
        def retry_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SnowflakeRetryOptionsProperty"]]:
            '''The time period where Firehose will retry sending data to the chosen HTTP endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-retryoptions
            '''
            result = self._values.get("retry_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SnowflakeRetryOptionsProperty"]], result)

        @builtins.property
        def s3_backup_mode(self) -> typing.Optional[builtins.str]:
            '''Choose an S3 backup mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-s3backupmode
            '''
            result = self._values.get("s3_backup_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def snowflake_role_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SnowflakeRoleConfigurationProperty"]]:
            '''Optionally configure a Snowflake role.

            Otherwise the default user role will be used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-snowflakeroleconfiguration
            '''
            result = self._values.get("snowflake_role_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SnowflakeRoleConfigurationProperty"]], result)

        @builtins.property
        def snowflake_vpc_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SnowflakeVpcConfigurationProperty"]]:
            '''The VPCE ID for Firehose to privately connect with Snowflake.

            The ID format is com.amazonaws.vpce.[region].vpce-svc-<[id]>. For more information, see `Amazon PrivateLink & Snowflake <https://docs.aws.amazon.com/https://docs.snowflake.com/en/user-guide/admin-security-privatelink>`_

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakedestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration-snowflakevpcconfiguration
            '''
            result = self._values.get("snowflake_vpc_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SnowflakeVpcConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnowflakeDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.SnowflakeRetryOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"duration_in_seconds": "durationInSeconds"},
    )
    class SnowflakeRetryOptionsProperty:
        def __init__(
            self,
            *,
            duration_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Specify how long Firehose retries sending data to the New Relic HTTP endpoint.

            After sending data, Firehose first waits for an acknowledgment from the HTTP endpoint. If an error occurs or the acknowledgment doesn’t arrive within the acknowledgment timeout period, Firehose starts the retry duration counter. It keeps retrying until the retry duration expires. After that, Firehose considers it a data delivery failure and backs up the data to your Amazon S3 bucket. Every time that Firehose sends data to the HTTP endpoint (either the initial attempt or a retry), it restarts the acknowledgement timeout counter and waits for an acknowledgement from the HTTP endpoint. Even if the retry duration expires, Firehose still waits for the acknowledgment until it receives it or the acknowledgement timeout period is reached. If the acknowledgment times out, Firehose determines whether there's time left in the retry counter. If there is time left, it retries again and repeats the logic until it receives an acknowledgment or determines that the retry time has expired. If you don't want Firehose to retry sending data, set this value to 0.

            :param duration_in_seconds: the time period where Firehose will retry sending data to the chosen HTTP endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakeretryoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                snowflake_retry_options_property = kinesisfirehose.CfnDeliveryStream.SnowflakeRetryOptionsProperty(
                    duration_in_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b7d919c23da3109305810f31f91a7020b20f997fbd66a87a4b4dfe122efff981)
                check_type(argname="argument duration_in_seconds", value=duration_in_seconds, expected_type=type_hints["duration_in_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if duration_in_seconds is not None:
                self._values["duration_in_seconds"] = duration_in_seconds

        @builtins.property
        def duration_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''the time period where Firehose will retry sending data to the chosen HTTP endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakeretryoptions.html#cfn-kinesisfirehose-deliverystream-snowflakeretryoptions-durationinseconds
            '''
            result = self._values.get("duration_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnowflakeRetryOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.SnowflakeRoleConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "snowflake_role": "snowflakeRole"},
    )
    class SnowflakeRoleConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            snowflake_role: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Optionally configure a Snowflake role.

            Otherwise the default user role will be used.

            :param enabled: Enable Snowflake role.
            :param snowflake_role: The Snowflake role you wish to configure.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakeroleconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                snowflake_role_configuration_property = kinesisfirehose.CfnDeliveryStream.SnowflakeRoleConfigurationProperty(
                    enabled=False,
                    snowflake_role="snowflakeRole"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__867673ab46f448fd1867f3b74172d4939969188f736abc7f1c5c26682419368b)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument snowflake_role", value=snowflake_role, expected_type=type_hints["snowflake_role"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if snowflake_role is not None:
                self._values["snowflake_role"] = snowflake_role

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Enable Snowflake role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakeroleconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakeroleconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def snowflake_role(self) -> typing.Optional[builtins.str]:
            '''The Snowflake role you wish to configure.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakeroleconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakeroleconfiguration-snowflakerole
            '''
            result = self._values.get("snowflake_role")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnowflakeRoleConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.SnowflakeVpcConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"private_link_vpce_id": "privateLinkVpceId"},
    )
    class SnowflakeVpcConfigurationProperty:
        def __init__(self, *, private_link_vpce_id: builtins.str) -> None:
            '''Configure a Snowflake VPC.

            :param private_link_vpce_id: The VPCE ID for Firehose to privately connect with Snowflake. The ID format is com.amazonaws.vpce.[region].vpce-svc-<[id]>. For more information, see `Amazon PrivateLink & Snowflake <https://docs.aws.amazon.com/https://docs.snowflake.com/en/user-guide/admin-security-privatelink>`_

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakevpcconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                snowflake_vpc_configuration_property = kinesisfirehose.CfnDeliveryStream.SnowflakeVpcConfigurationProperty(
                    private_link_vpce_id="privateLinkVpceId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a5715c831de8e3fe729e9e76213a2b933810f642d09eb653534a3d23054acf0d)
                check_type(argname="argument private_link_vpce_id", value=private_link_vpce_id, expected_type=type_hints["private_link_vpce_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "private_link_vpce_id": private_link_vpce_id,
            }

        @builtins.property
        def private_link_vpce_id(self) -> builtins.str:
            '''The VPCE ID for Firehose to privately connect with Snowflake.

            The ID format is com.amazonaws.vpce.[region].vpce-svc-<[id]>. For more information, see `Amazon PrivateLink & Snowflake <https://docs.aws.amazon.com/https://docs.snowflake.com/en/user-guide/admin-security-privatelink>`_

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-snowflakevpcconfiguration.html#cfn-kinesisfirehose-deliverystream-snowflakevpcconfiguration-privatelinkvpceid
            '''
            result = self._values.get("private_link_vpce_id")
            assert result is not None, "Required property 'private_link_vpce_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnowflakeVpcConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.SplunkBufferingHintsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "interval_in_seconds": "intervalInSeconds",
            "size_in_m_bs": "sizeInMBs",
        },
    )
    class SplunkBufferingHintsProperty:
        def __init__(
            self,
            *,
            interval_in_seconds: typing.Optional[jsii.Number] = None,
            size_in_m_bs: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The buffering options.

            If no value is specified, the default values for Splunk are used.

            :param interval_in_seconds: Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 60 (1 minute).
            :param size_in_m_bs: Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkbufferinghints.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                splunk_buffering_hints_property = kinesisfirehose.CfnDeliveryStream.SplunkBufferingHintsProperty(
                    interval_in_seconds=123,
                    size_in_mBs=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__60823c61f8aea3242c07551788af8f338bff46b6299ee9aa1d0ff6112c454ecc)
                check_type(argname="argument interval_in_seconds", value=interval_in_seconds, expected_type=type_hints["interval_in_seconds"])
                check_type(argname="argument size_in_m_bs", value=size_in_m_bs, expected_type=type_hints["size_in_m_bs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if interval_in_seconds is not None:
                self._values["interval_in_seconds"] = interval_in_seconds
            if size_in_m_bs is not None:
                self._values["size_in_m_bs"] = size_in_m_bs

        @builtins.property
        def interval_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination.

            The default value is 60 (1 minute).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkbufferinghints.html#cfn-kinesisfirehose-deliverystream-splunkbufferinghints-intervalinseconds
            '''
            result = self._values.get("interval_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def size_in_m_bs(self) -> typing.Optional[jsii.Number]:
            '''Buffer incoming data to the specified size, in MBs, before delivering it to the destination.

            The default value is 5.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkbufferinghints.html#cfn-kinesisfirehose-deliverystream-splunkbufferinghints-sizeinmbs
            '''
            result = self._values.get("size_in_m_bs")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SplunkBufferingHintsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.SplunkDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hec_endpoint": "hecEndpoint",
            "hec_endpoint_type": "hecEndpointType",
            "hec_token": "hecToken",
            "s3_configuration": "s3Configuration",
            "buffering_hints": "bufferingHints",
            "cloud_watch_logging_options": "cloudWatchLoggingOptions",
            "hec_acknowledgment_timeout_in_seconds": "hecAcknowledgmentTimeoutInSeconds",
            "processing_configuration": "processingConfiguration",
            "retry_options": "retryOptions",
            "s3_backup_mode": "s3BackupMode",
        },
    )
    class SplunkDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            hec_endpoint: builtins.str,
            hec_endpoint_type: builtins.str,
            hec_token: builtins.str,
            s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.S3DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.SplunkBufferingHintsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.CloudWatchLoggingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            hec_acknowledgment_timeout_in_seconds: typing.Optional[jsii.Number] = None,
            processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.ProcessingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeliveryStream.SplunkRetryOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_backup_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``SplunkDestinationConfiguration`` property type specifies the configuration of a destination in Splunk for a Kinesis Data Firehose delivery stream.

            :param hec_endpoint: The HTTP Event Collector (HEC) endpoint to which Firehose sends your data.
            :param hec_endpoint_type: This type can be either ``Raw`` or ``Event`` .
            :param hec_token: This is a GUID that you obtain from your Splunk cluster when you create a new HEC endpoint.
            :param s3_configuration: The configuration for the backup Amazon S3 location.
            :param buffering_hints: The buffering options. If no value is specified, the default values for Splunk are used.
            :param cloud_watch_logging_options: The Amazon CloudWatch logging options for your delivery stream.
            :param hec_acknowledgment_timeout_in_seconds: The amount of time that Firehose waits to receive an acknowledgment from Splunk after it sends it data. At the end of the timeout period, Firehose either tries to send the data again or considers it an error, based on your retry settings.
            :param processing_configuration: The data processing configuration.
            :param retry_options: The retry behavior in case Firehose is unable to deliver data to Splunk, or if it doesn't receive an acknowledgment of receipt from Splunk.
            :param s3_backup_mode: Defines how documents should be delivered to Amazon S3. When set to ``FailedEventsOnly`` , Firehose writes any data that could not be indexed to the configured Amazon S3 destination. When set to ``AllEvents`` , Firehose delivers all incoming records to Amazon S3, and also writes failed documents to Amazon S3. The default value is ``FailedEventsOnly`` . You can update this backup mode from ``FailedEventsOnly`` to ``AllEvents`` . You can't update it from ``AllEvents`` to ``FailedEventsOnly`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                splunk_destination_configuration_property = kinesisfirehose.CfnDeliveryStream.SplunkDestinationConfigurationProperty(
                    hec_endpoint="hecEndpoint",
                    hec_endpoint_type="hecEndpointType",
                    hec_token="hecToken",
                    s3_configuration=kinesisfirehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                        bucket_arn="bucketArn",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        buffering_hints=kinesisfirehose.CfnDeliveryStream.BufferingHintsProperty(
                            interval_in_seconds=123,
                            size_in_mBs=123
                        ),
                        cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                            enabled=False,
                            log_group_name="logGroupName",
                            log_stream_name="logStreamName"
                        ),
                        compression_format="compressionFormat",
                        encryption_configuration=kinesisfirehose.CfnDeliveryStream.EncryptionConfigurationProperty(
                            kms_encryption_config=kinesisfirehose.CfnDeliveryStream.KMSEncryptionConfigProperty(
                                awskms_key_arn="awskmsKeyArn"
                            ),
                            no_encryption_config="noEncryptionConfig"
                        ),
                        error_output_prefix="errorOutputPrefix",
                        prefix="prefix"
                    ),
                
                    # the properties below are optional
                    buffering_hints=kinesisfirehose.CfnDeliveryStream.SplunkBufferingHintsProperty(
                        interval_in_seconds=123,
                        size_in_mBs=123
                    ),
                    cloud_watch_logging_options=kinesisfirehose.CfnDeliveryStream.CloudWatchLoggingOptionsProperty(
                        enabled=False,
                        log_group_name="logGroupName",
                        log_stream_name="logStreamName"
                    ),
                    hec_acknowledgment_timeout_in_seconds=123,
                    processing_configuration=kinesisfirehose.CfnDeliveryStream.ProcessingConfigurationProperty(
                        enabled=False,
                        processors=[kinesisfirehose.CfnDeliveryStream.ProcessorProperty(
                            type="type",
                
                            # the properties below are optional
                            parameters=[kinesisfirehose.CfnDeliveryStream.ProcessorParameterProperty(
                                parameter_name="parameterName",
                                parameter_value="parameterValue"
                            )]
                        )]
                    ),
                    retry_options=kinesisfirehose.CfnDeliveryStream.SplunkRetryOptionsProperty(
                        duration_in_seconds=123
                    ),
                    s3_backup_mode="s3BackupMode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__be9923ea7818bcdc567ae6e06b529c44c6a3c42b59af06768977f4c55fdd20a6)
                check_type(argname="argument hec_endpoint", value=hec_endpoint, expected_type=type_hints["hec_endpoint"])
                check_type(argname="argument hec_endpoint_type", value=hec_endpoint_type, expected_type=type_hints["hec_endpoint_type"])
                check_type(argname="argument hec_token", value=hec_token, expected_type=type_hints["hec_token"])
                check_type(argname="argument s3_configuration", value=s3_configuration, expected_type=type_hints["s3_configuration"])
                check_type(argname="argument buffering_hints", value=buffering_hints, expected_type=type_hints["buffering_hints"])
                check_type(argname="argument cloud_watch_logging_options", value=cloud_watch_logging_options, expected_type=type_hints["cloud_watch_logging_options"])
                check_type(argname="argument hec_acknowledgment_timeout_in_seconds", value=hec_acknowledgment_timeout_in_seconds, expected_type=type_hints["hec_acknowledgment_timeout_in_seconds"])
                check_type(argname="argument processing_configuration", value=processing_configuration, expected_type=type_hints["processing_configuration"])
                check_type(argname="argument retry_options", value=retry_options, expected_type=type_hints["retry_options"])
                check_type(argname="argument s3_backup_mode", value=s3_backup_mode, expected_type=type_hints["s3_backup_mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "hec_endpoint": hec_endpoint,
                "hec_endpoint_type": hec_endpoint_type,
                "hec_token": hec_token,
                "s3_configuration": s3_configuration,
            }
            if buffering_hints is not None:
                self._values["buffering_hints"] = buffering_hints
            if cloud_watch_logging_options is not None:
                self._values["cloud_watch_logging_options"] = cloud_watch_logging_options
            if hec_acknowledgment_timeout_in_seconds is not None:
                self._values["hec_acknowledgment_timeout_in_seconds"] = hec_acknowledgment_timeout_in_seconds
            if processing_configuration is not None:
                self._values["processing_configuration"] = processing_configuration
            if retry_options is not None:
                self._values["retry_options"] = retry_options
            if s3_backup_mode is not None:
                self._values["s3_backup_mode"] = s3_backup_mode

        @builtins.property
        def hec_endpoint(self) -> builtins.str:
            '''The HTTP Event Collector (HEC) endpoint to which Firehose sends your data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-hecendpoint
            '''
            result = self._values.get("hec_endpoint")
            assert result is not None, "Required property 'hec_endpoint' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def hec_endpoint_type(self) -> builtins.str:
            '''This type can be either ``Raw`` or ``Event`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-hecendpointtype
            '''
            result = self._values.get("hec_endpoint_type")
            assert result is not None, "Required property 'hec_endpoint_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def hec_token(self) -> builtins.str:
            '''This is a GUID that you obtain from your Splunk cluster when you create a new HEC endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-hectoken
            '''
            result = self._values.get("hec_token")
            assert result is not None, "Required property 'hec_token' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"]:
            '''The configuration for the backup Amazon S3 location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-s3configuration
            '''
            result = self._values.get("s3_configuration")
            assert result is not None, "Required property 's3_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.S3DestinationConfigurationProperty"], result)

        @builtins.property
        def buffering_hints(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SplunkBufferingHintsProperty"]]:
            '''The buffering options.

            If no value is specified, the default values for Splunk are used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-bufferinghints
            '''
            result = self._values.get("buffering_hints")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SplunkBufferingHintsProperty"]], result)

        @builtins.property
        def cloud_watch_logging_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]]:
            '''The Amazon CloudWatch logging options for your delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-cloudwatchloggingoptions
            '''
            result = self._values.get("cloud_watch_logging_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.CloudWatchLoggingOptionsProperty"]], result)

        @builtins.property
        def hec_acknowledgment_timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The amount of time that Firehose waits to receive an acknowledgment from Splunk after it sends it data.

            At the end of the timeout period, Firehose either tries to send the data again or considers it an error, based on your retry settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-hecacknowledgmenttimeoutinseconds
            '''
            result = self._values.get("hec_acknowledgment_timeout_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def processing_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]]:
            '''The data processing configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-processingconfiguration
            '''
            result = self._values.get("processing_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.ProcessingConfigurationProperty"]], result)

        @builtins.property
        def retry_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SplunkRetryOptionsProperty"]]:
            '''The retry behavior in case Firehose is unable to deliver data to Splunk, or if it doesn't receive an acknowledgment of receipt from Splunk.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-retryoptions
            '''
            result = self._values.get("retry_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeliveryStream.SplunkRetryOptionsProperty"]], result)

        @builtins.property
        def s3_backup_mode(self) -> typing.Optional[builtins.str]:
            '''Defines how documents should be delivered to Amazon S3.

            When set to ``FailedEventsOnly`` , Firehose writes any data that could not be indexed to the configured Amazon S3 destination. When set to ``AllEvents`` , Firehose delivers all incoming records to Amazon S3, and also writes failed documents to Amazon S3. The default value is ``FailedEventsOnly`` .

            You can update this backup mode from ``FailedEventsOnly`` to ``AllEvents`` . You can't update it from ``AllEvents`` to ``FailedEventsOnly`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkdestinationconfiguration.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration-s3backupmode
            '''
            result = self._values.get("s3_backup_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SplunkDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.SplunkRetryOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"duration_in_seconds": "durationInSeconds"},
    )
    class SplunkRetryOptionsProperty:
        def __init__(
            self,
            *,
            duration_in_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The ``SplunkRetryOptions`` property type specifies retry behavior in case Kinesis Data Firehose is unable to deliver documents to Splunk or if it doesn't receive an acknowledgment from Splunk.

            :param duration_in_seconds: The total amount of time that Firehose spends on retries. This duration starts after the initial attempt to send data to Splunk fails. It doesn't include the periods during which Firehose waits for acknowledgment from Splunk after each attempt.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkretryoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                splunk_retry_options_property = kinesisfirehose.CfnDeliveryStream.SplunkRetryOptionsProperty(
                    duration_in_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5c5cbe7244c68f12454d07974a4cae50f1d208afdbc3a96f1e2ada11e37fc412)
                check_type(argname="argument duration_in_seconds", value=duration_in_seconds, expected_type=type_hints["duration_in_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if duration_in_seconds is not None:
                self._values["duration_in_seconds"] = duration_in_seconds

        @builtins.property
        def duration_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''The total amount of time that Firehose spends on retries.

            This duration starts after the initial attempt to send data to Splunk fails. It doesn't include the periods during which Firehose waits for acknowledgment from Splunk after each attempt.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-splunkretryoptions.html#cfn-kinesisfirehose-deliverystream-splunkretryoptions-durationinseconds
            '''
            result = self._values.get("duration_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SplunkRetryOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.VpcConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class VpcConfigurationProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            security_group_ids: typing.Sequence[builtins.str],
            subnet_ids: typing.Sequence[builtins.str],
        ) -> None:
            '''The details of the VPC of the Amazon ES destination.

            :param role_arn: The ARN of the IAM role that you want the delivery stream to use to create endpoints in the destination VPC. You can use your existing Kinesis Data Firehose delivery role or you can specify a new role. In either case, make sure that the role trusts the Kinesis Data Firehose service principal and that it grants the following permissions: - ``ec2:DescribeVpcs`` - ``ec2:DescribeVpcAttribute`` - ``ec2:DescribeSubnets`` - ``ec2:DescribeSecurityGroups`` - ``ec2:DescribeNetworkInterfaces`` - ``ec2:CreateNetworkInterface`` - ``ec2:CreateNetworkInterfacePermission`` - ``ec2:DeleteNetworkInterface`` If you revoke these permissions after you create the delivery stream, Kinesis Data Firehose can't scale out by creating more ENIs when necessary. You might therefore see a degradation in performance.
            :param security_group_ids: The IDs of the security groups that you want Kinesis Data Firehose to use when it creates ENIs in the VPC of the Amazon ES destination. You can use the same security group that the Amazon ES domain uses or different ones. If you specify different security groups here, ensure that they allow outbound HTTPS traffic to the Amazon ES domain's security group. Also ensure that the Amazon ES domain's security group allows HTTPS traffic from the security groups specified here. If you use the same security group for both your delivery stream and the Amazon ES domain, make sure the security group inbound rule allows HTTPS traffic.
            :param subnet_ids: The IDs of the subnets that Kinesis Data Firehose uses to create ENIs in the VPC of the Amazon ES destination. Make sure that the routing tables and inbound and outbound rules allow traffic to flow from the subnets whose IDs are specified here to the subnets that have the destination Amazon ES endpoints. Kinesis Data Firehose creates at least one ENI in each of the subnets that are specified here. Do not delete or modify these ENIs. The number of ENIs that Kinesis Data Firehose creates in the subnets specified here scales up and down automatically based on throughput. To enable Kinesis Data Firehose to scale up the number of ENIs to match throughput, ensure that you have sufficient quota. To help you calculate the quota you need, assume that Kinesis Data Firehose can create up to three ENIs for this delivery stream for each of the subnets specified here.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-vpcconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisfirehose as kinesisfirehose
                
                vpc_configuration_property = kinesisfirehose.CfnDeliveryStream.VpcConfigurationProperty(
                    role_arn="roleArn",
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3ecd7f59955db0312a31e14fafedff3746c1d169b6a24f2985f6a096a09db25a)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
                "security_group_ids": security_group_ids,
                "subnet_ids": subnet_ids,
            }

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the IAM role that you want the delivery stream to use to create endpoints in the destination VPC.

            You can use your existing Kinesis Data Firehose delivery role or you can specify a new role. In either case, make sure that the role trusts the Kinesis Data Firehose service principal and that it grants the following permissions:

            - ``ec2:DescribeVpcs``
            - ``ec2:DescribeVpcAttribute``
            - ``ec2:DescribeSubnets``
            - ``ec2:DescribeSecurityGroups``
            - ``ec2:DescribeNetworkInterfaces``
            - ``ec2:CreateNetworkInterface``
            - ``ec2:CreateNetworkInterfacePermission``
            - ``ec2:DeleteNetworkInterface``

            If you revoke these permissions after you create the delivery stream, Kinesis Data Firehose can't scale out by creating more ENIs when necessary. You might therefore see a degradation in performance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-vpcconfiguration.html#cfn-kinesisfirehose-deliverystream-vpcconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''The IDs of the security groups that you want Kinesis Data Firehose to use when it creates ENIs in the VPC of the Amazon ES destination.

            You can use the same security group that the Amazon ES domain uses or different ones. If you specify different security groups here, ensure that they allow outbound HTTPS traffic to the Amazon ES domain's security group. Also ensure that the Amazon ES domain's security group allows HTTPS traffic from the security groups specified here. If you use the same security group for both your delivery stream and the Amazon ES domain, make sure the security group inbound rule allows HTTPS traffic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-vpcconfiguration.html#cfn-kinesisfirehose-deliverystream-vpcconfiguration-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''The IDs of the subnets that Kinesis Data Firehose uses to create ENIs in the VPC of the Amazon ES destination.

            Make sure that the routing tables and inbound and outbound rules allow traffic to flow from the subnets whose IDs are specified here to the subnets that have the destination Amazon ES endpoints. Kinesis Data Firehose creates at least one ENI in each of the subnets that are specified here. Do not delete or modify these ENIs.

            The number of ENIs that Kinesis Data Firehose creates in the subnets specified here scales up and down automatically based on throughput. To enable Kinesis Data Firehose to scale up the number of ENIs to match throughput, ensure that you have sufficient quota. To help you calculate the quota you need, assume that Kinesis Data Firehose can create up to three ENIs for this delivery stream for each of the subnets specified here.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-vpcconfiguration.html#cfn-kinesisfirehose-deliverystream-vpcconfiguration-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
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
    jsii_type="aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStreamProps",
    jsii_struct_bases=[],
    name_mapping={
        "amazon_open_search_serverless_destination_configuration": "amazonOpenSearchServerlessDestinationConfiguration",
        "amazonopensearchservice_destination_configuration": "amazonopensearchserviceDestinationConfiguration",
        "delivery_stream_encryption_configuration_input": "deliveryStreamEncryptionConfigurationInput",
        "delivery_stream_name": "deliveryStreamName",
        "delivery_stream_type": "deliveryStreamType",
        "elasticsearch_destination_configuration": "elasticsearchDestinationConfiguration",
        "extended_s3_destination_configuration": "extendedS3DestinationConfiguration",
        "http_endpoint_destination_configuration": "httpEndpointDestinationConfiguration",
        "kinesis_stream_source_configuration": "kinesisStreamSourceConfiguration",
        "msk_source_configuration": "mskSourceConfiguration",
        "redshift_destination_configuration": "redshiftDestinationConfiguration",
        "s3_destination_configuration": "s3DestinationConfiguration",
        "snowflake_destination_configuration": "snowflakeDestinationConfiguration",
        "splunk_destination_configuration": "splunkDestinationConfiguration",
        "tags": "tags",
    },
)
class CfnDeliveryStreamProps:
    def __init__(
        self,
        *,
        amazon_open_search_serverless_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.AmazonOpenSearchServerlessDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        amazonopensearchservice_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        delivery_stream_encryption_configuration_input: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        delivery_stream_name: typing.Optional[builtins.str] = None,
        delivery_stream_type: typing.Optional[builtins.str] = None,
        elasticsearch_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        extended_s3_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        http_endpoint_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        kinesis_stream_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.KinesisStreamSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        msk_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.MSKSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        redshift_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.RedshiftDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        s3_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        snowflake_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SnowflakeDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        splunk_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SplunkDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDeliveryStream``.

        :param amazon_open_search_serverless_destination_configuration: Describes the configuration of a destination in the Serverless offering for Amazon OpenSearch Service.
        :param amazonopensearchservice_destination_configuration: The destination in Amazon OpenSearch Service. You can specify only one destination.
        :param delivery_stream_encryption_configuration_input: Specifies the type and Amazon Resource Name (ARN) of the CMK to use for Server-Side Encryption (SSE).
        :param delivery_stream_name: The name of the delivery stream.
        :param delivery_stream_type: The delivery stream type. This can be one of the following values:. - ``DirectPut`` : Provider applications access the delivery stream directly. - ``KinesisStreamAsSource`` : The delivery stream uses a Kinesis data stream as a source.
        :param elasticsearch_destination_configuration: An Amazon ES destination for the delivery stream. Conditional. You must specify only one destination configuration. If you change the delivery stream destination from an Amazon ES destination to an Amazon S3 or Amazon Redshift destination, update requires `some interruptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt>`_ .
        :param extended_s3_destination_configuration: An Amazon S3 destination for the delivery stream. Conditional. You must specify only one destination configuration. If you change the delivery stream destination from an Amazon Extended S3 destination to an Amazon ES destination, update requires `some interruptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt>`_ .
        :param http_endpoint_destination_configuration: Enables configuring Kinesis Firehose to deliver data to any HTTP endpoint destination. You can specify only one destination.
        :param kinesis_stream_source_configuration: When a Kinesis stream is used as the source for the delivery stream, a `KinesisStreamSourceConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html>`_ containing the Kinesis stream ARN and the role ARN for the source stream.
        :param msk_source_configuration: The configuration for the Amazon MSK cluster to be used as the source for a delivery stream.
        :param redshift_destination_configuration: An Amazon Redshift destination for the delivery stream. Conditional. You must specify only one destination configuration. If you change the delivery stream destination from an Amazon Redshift destination to an Amazon ES destination, update requires `some interruptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt>`_ .
        :param s3_destination_configuration: The ``S3DestinationConfiguration`` property type specifies an Amazon Simple Storage Service (Amazon S3) destination to which Amazon Kinesis Data Firehose (Kinesis Data Firehose) delivers data. Conditional. You must specify only one destination configuration. If you change the delivery stream destination from an Amazon S3 destination to an Amazon ES destination, update requires `some interruptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt>`_ .
        :param snowflake_destination_configuration: Configure Snowflake destination.
        :param splunk_destination_configuration: The configuration of a destination in Splunk for the delivery stream.
        :param tags: A set of tags to assign to the delivery stream. A tag is a key-value pair that you can define and assign to AWS resources. Tags are metadata. For example, you can add friendly names and descriptions or other types of information that can help you distinguish the delivery stream. For more information about tags, see `Using Cost Allocation Tags <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`_ in the AWS Billing and Cost Management User Guide. You can specify up to 50 tags when creating a delivery stream. If you specify tags in the ``CreateDeliveryStream`` action, Amazon Data Firehose performs an additional authorization on the ``firehose:TagDeliveryStream`` action to verify if users have permissions to create tags. If you do not provide this permission, requests to create new Firehose delivery streams with IAM resource tags will fail with an ``AccessDeniedException`` such as following. *AccessDeniedException* User: arn:aws:sts::x:assumed-role/x/x is not authorized to perform: firehose:TagDeliveryStream on resource: arn:aws:firehose:us-east-1:x:deliverystream/x with an explicit deny in an identity-based policy. For an example IAM policy, see `Tag example. <https://docs.aws.amazon.com/firehose/latest/APIReference/API_CreateDeliveryStream.html#API_CreateDeliveryStream_Examples>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html
        :exampleMetadata: infused

        Example::

            destination_bucket = s3.Bucket(self, "Bucket")
            delivery_stream_role = iam.Role(self, "Role",
                assumed_by=iam.ServicePrincipal("firehose.amazonaws.com")
            )
            
            stream = firehose.CfnDeliveryStream(self, "MyStream",
                delivery_stream_name="amazon-apigateway-delivery-stream",
                s3_destination_configuration=firehose.CfnDeliveryStream.S3DestinationConfigurationProperty(
                    bucket_arn=destination_bucket.bucket_arn,
                    role_arn=delivery_stream_role.role_arn
                )
            )
            
            api = apigateway.RestApi(self, "books",
                deploy_options=apigateway.StageOptions(
                    access_log_destination=apigateway.FirehoseLogDestination(stream),
                    access_log_format=apigateway.AccessLogFormat.json_with_standard_fields()
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f4e310bf0ff2c76f9c126ea4431fb25b9b53c8ba7e0c0eacc1c934debd05a95)
            check_type(argname="argument amazon_open_search_serverless_destination_configuration", value=amazon_open_search_serverless_destination_configuration, expected_type=type_hints["amazon_open_search_serverless_destination_configuration"])
            check_type(argname="argument amazonopensearchservice_destination_configuration", value=amazonopensearchservice_destination_configuration, expected_type=type_hints["amazonopensearchservice_destination_configuration"])
            check_type(argname="argument delivery_stream_encryption_configuration_input", value=delivery_stream_encryption_configuration_input, expected_type=type_hints["delivery_stream_encryption_configuration_input"])
            check_type(argname="argument delivery_stream_name", value=delivery_stream_name, expected_type=type_hints["delivery_stream_name"])
            check_type(argname="argument delivery_stream_type", value=delivery_stream_type, expected_type=type_hints["delivery_stream_type"])
            check_type(argname="argument elasticsearch_destination_configuration", value=elasticsearch_destination_configuration, expected_type=type_hints["elasticsearch_destination_configuration"])
            check_type(argname="argument extended_s3_destination_configuration", value=extended_s3_destination_configuration, expected_type=type_hints["extended_s3_destination_configuration"])
            check_type(argname="argument http_endpoint_destination_configuration", value=http_endpoint_destination_configuration, expected_type=type_hints["http_endpoint_destination_configuration"])
            check_type(argname="argument kinesis_stream_source_configuration", value=kinesis_stream_source_configuration, expected_type=type_hints["kinesis_stream_source_configuration"])
            check_type(argname="argument msk_source_configuration", value=msk_source_configuration, expected_type=type_hints["msk_source_configuration"])
            check_type(argname="argument redshift_destination_configuration", value=redshift_destination_configuration, expected_type=type_hints["redshift_destination_configuration"])
            check_type(argname="argument s3_destination_configuration", value=s3_destination_configuration, expected_type=type_hints["s3_destination_configuration"])
            check_type(argname="argument snowflake_destination_configuration", value=snowflake_destination_configuration, expected_type=type_hints["snowflake_destination_configuration"])
            check_type(argname="argument splunk_destination_configuration", value=splunk_destination_configuration, expected_type=type_hints["splunk_destination_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if amazon_open_search_serverless_destination_configuration is not None:
            self._values["amazon_open_search_serverless_destination_configuration"] = amazon_open_search_serverless_destination_configuration
        if amazonopensearchservice_destination_configuration is not None:
            self._values["amazonopensearchservice_destination_configuration"] = amazonopensearchservice_destination_configuration
        if delivery_stream_encryption_configuration_input is not None:
            self._values["delivery_stream_encryption_configuration_input"] = delivery_stream_encryption_configuration_input
        if delivery_stream_name is not None:
            self._values["delivery_stream_name"] = delivery_stream_name
        if delivery_stream_type is not None:
            self._values["delivery_stream_type"] = delivery_stream_type
        if elasticsearch_destination_configuration is not None:
            self._values["elasticsearch_destination_configuration"] = elasticsearch_destination_configuration
        if extended_s3_destination_configuration is not None:
            self._values["extended_s3_destination_configuration"] = extended_s3_destination_configuration
        if http_endpoint_destination_configuration is not None:
            self._values["http_endpoint_destination_configuration"] = http_endpoint_destination_configuration
        if kinesis_stream_source_configuration is not None:
            self._values["kinesis_stream_source_configuration"] = kinesis_stream_source_configuration
        if msk_source_configuration is not None:
            self._values["msk_source_configuration"] = msk_source_configuration
        if redshift_destination_configuration is not None:
            self._values["redshift_destination_configuration"] = redshift_destination_configuration
        if s3_destination_configuration is not None:
            self._values["s3_destination_configuration"] = s3_destination_configuration
        if snowflake_destination_configuration is not None:
            self._values["snowflake_destination_configuration"] = snowflake_destination_configuration
        if splunk_destination_configuration is not None:
            self._values["splunk_destination_configuration"] = splunk_destination_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def amazon_open_search_serverless_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.AmazonOpenSearchServerlessDestinationConfigurationProperty]]:
        '''Describes the configuration of a destination in the Serverless offering for Amazon OpenSearch Service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-amazonopensearchserverlessdestinationconfiguration
        '''
        result = self._values.get("amazon_open_search_serverless_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.AmazonOpenSearchServerlessDestinationConfigurationProperty]], result)

    @builtins.property
    def amazonopensearchservice_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty]]:
        '''The destination in Amazon OpenSearch Service.

        You can specify only one destination.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-amazonopensearchservicedestinationconfiguration
        '''
        result = self._values.get("amazonopensearchservice_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty]], result)

    @builtins.property
    def delivery_stream_encryption_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty]]:
        '''Specifies the type and Amazon Resource Name (ARN) of the CMK to use for Server-Side Encryption (SSE).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-deliverystreamencryptionconfigurationinput
        '''
        result = self._values.get("delivery_stream_encryption_configuration_input")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty]], result)

    @builtins.property
    def delivery_stream_name(self) -> typing.Optional[builtins.str]:
        '''The name of the delivery stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-deliverystreamname
        '''
        result = self._values.get("delivery_stream_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delivery_stream_type(self) -> typing.Optional[builtins.str]:
        '''The delivery stream type. This can be one of the following values:.

        - ``DirectPut`` : Provider applications access the delivery stream directly.
        - ``KinesisStreamAsSource`` : The delivery stream uses a Kinesis data stream as a source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-deliverystreamtype
        '''
        result = self._values.get("delivery_stream_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def elasticsearch_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty]]:
        '''An Amazon ES destination for the delivery stream.

        Conditional. You must specify only one destination configuration.

        If you change the delivery stream destination from an Amazon ES destination to an Amazon S3 or Amazon Redshift destination, update requires `some interruptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-elasticsearchdestinationconfiguration
        '''
        result = self._values.get("elasticsearch_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty]], result)

    @builtins.property
    def extended_s3_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty]]:
        '''An Amazon S3 destination for the delivery stream.

        Conditional. You must specify only one destination configuration.

        If you change the delivery stream destination from an Amazon Extended S3 destination to an Amazon ES destination, update requires `some interruptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-extendeds3destinationconfiguration
        '''
        result = self._values.get("extended_s3_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty]], result)

    @builtins.property
    def http_endpoint_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty]]:
        '''Enables configuring Kinesis Firehose to deliver data to any HTTP endpoint destination.

        You can specify only one destination.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-httpendpointdestinationconfiguration
        '''
        result = self._values.get("http_endpoint_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty]], result)

    @builtins.property
    def kinesis_stream_source_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.KinesisStreamSourceConfigurationProperty]]:
        '''When a Kinesis stream is used as the source for the delivery stream, a `KinesisStreamSourceConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration.html>`_ containing the Kinesis stream ARN and the role ARN for the source stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-kinesisstreamsourceconfiguration
        '''
        result = self._values.get("kinesis_stream_source_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.KinesisStreamSourceConfigurationProperty]], result)

    @builtins.property
    def msk_source_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.MSKSourceConfigurationProperty]]:
        '''The configuration for the Amazon MSK cluster to be used as the source for a delivery stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-msksourceconfiguration
        '''
        result = self._values.get("msk_source_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.MSKSourceConfigurationProperty]], result)

    @builtins.property
    def redshift_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.RedshiftDestinationConfigurationProperty]]:
        '''An Amazon Redshift destination for the delivery stream.

        Conditional. You must specify only one destination configuration.

        If you change the delivery stream destination from an Amazon Redshift destination to an Amazon ES destination, update requires `some interruptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-redshiftdestinationconfiguration
        '''
        result = self._values.get("redshift_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.RedshiftDestinationConfigurationProperty]], result)

    @builtins.property
    def s3_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.S3DestinationConfigurationProperty]]:
        '''The ``S3DestinationConfiguration`` property type specifies an Amazon Simple Storage Service (Amazon S3) destination to which Amazon Kinesis Data Firehose (Kinesis Data Firehose) delivers data.

        Conditional. You must specify only one destination configuration.

        If you change the delivery stream destination from an Amazon S3 destination to an Amazon ES destination, update requires `some interruptions <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-s3destinationconfiguration
        '''
        result = self._values.get("s3_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.S3DestinationConfigurationProperty]], result)

    @builtins.property
    def snowflake_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.SnowflakeDestinationConfigurationProperty]]:
        '''Configure Snowflake destination.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-snowflakedestinationconfiguration
        '''
        result = self._values.get("snowflake_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.SnowflakeDestinationConfigurationProperty]], result)

    @builtins.property
    def splunk_destination_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.SplunkDestinationConfigurationProperty]]:
        '''The configuration of a destination in Splunk for the delivery stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-splunkdestinationconfiguration
        '''
        result = self._values.get("splunk_destination_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.SplunkDestinationConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A set of tags to assign to the delivery stream.

        A tag is a key-value pair that you can define and assign to AWS resources. Tags are metadata. For example, you can add friendly names and descriptions or other types of information that can help you distinguish the delivery stream. For more information about tags, see `Using Cost Allocation Tags <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`_ in the AWS Billing and Cost Management User Guide.

        You can specify up to 50 tags when creating a delivery stream.

        If you specify tags in the ``CreateDeliveryStream`` action, Amazon Data Firehose performs an additional authorization on the ``firehose:TagDeliveryStream`` action to verify if users have permissions to create tags. If you do not provide this permission, requests to create new Firehose delivery streams with IAM resource tags will fail with an ``AccessDeniedException`` such as following.

        *AccessDeniedException*

        User: arn:aws:sts::x:assumed-role/x/x is not authorized to perform: firehose:TagDeliveryStream on resource: arn:aws:firehose:us-east-1:x:deliverystream/x with an explicit deny in an identity-based policy.

        For an example IAM policy, see `Tag example. <https://docs.aws.amazon.com/firehose/latest/APIReference/API_CreateDeliveryStream.html#API_CreateDeliveryStream_Examples>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html#cfn-kinesisfirehose-deliverystream-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeliveryStreamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDeliveryStream",
    "CfnDeliveryStreamProps",
]

publication.publish()

def _typecheckingstub__b3cd824a2680c7d043cac684bd1be9ca77e94201f1ba00785d60a50ff43c2288(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    amazon_open_search_serverless_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.AmazonOpenSearchServerlessDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    amazonopensearchservice_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    delivery_stream_encryption_configuration_input: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    delivery_stream_name: typing.Optional[builtins.str] = None,
    delivery_stream_type: typing.Optional[builtins.str] = None,
    elasticsearch_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    extended_s3_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    http_endpoint_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kinesis_stream_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.KinesisStreamSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    msk_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.MSKSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    redshift_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.RedshiftDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    snowflake_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SnowflakeDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    splunk_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SplunkDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f6206943f45cc34824996fe47b775be3c1a09cb74450254dfa716bc71a96a69(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__822762453b1edc05d278fe4b56cb34de36a63cda89772b6624160f6ac406e7e7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9361f4405d0a8e9a0285d4b343c6420073eedc822c339d1a147f151a3b03f641(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.AmazonOpenSearchServerlessDestinationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58964b8831d37cbba22a48328508a0d1fc866bb6da992a0c3f544fc6649acc5a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b541613844a306d329ee6aaf12a513672a01cea651f015810fd2ab896394415(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d90731f57c337a34bb7290e3bb4239e949b5caeea354433c46c25998a03b39f6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0749b7e1cb2e266044df272e646eba4d2505c56ccb68f4ce96de186aeb83ba9b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2485fd6e8467da83435abf801383e98fea4d4ae9797551e1774f2327e1b069c5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b3827d67811452e6783eeef4d719d420c5534229b93597dbfafa7256a89932e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c45396814a2f1f16d85b99c121f14ab851eda0a9f84038025d5ae44a858837a1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__025f54a26e52ce42f679eff3aa8b95a5fee2e0e5b3aba7c4320f9900690e60b9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.KinesisStreamSourceConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d05261de796c66b290d3bf9493dedca3a4f904726566b1e0d28cd6f7e525757(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.MSKSourceConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9283febc90a4404b9eb41b227b6baf567d66cf4929f4f56dc67252a81e997f1f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.RedshiftDestinationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb8b949ac7c9700a5ef03cddf3b3be451041166fe7583faee720a903b17ffd7c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.S3DestinationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4334e067c783ee048616b856f03ad5fb828c1a4c18bbdce130d9850ac2ce4034(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.SnowflakeDestinationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1143a0f5e018d10fdc1fff0bbcada0e3653e2264078be8b5a6441f6918b95c91(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeliveryStream.SplunkDestinationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b611aca673873100e4f1f1366dada7f80beaecdafd39582bd00fb48881dca276(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73b3806edee327ffa718f826cdd3f2971c613586675003f856582bd7f9f0990b(
    *,
    interval_in_seconds: typing.Optional[jsii.Number] = None,
    size_in_m_bs: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c09d95c569c785593bec028509479a3c62ff0333544fe7fb6ea165082930dcf0(
    *,
    index_name: builtins.str,
    role_arn: builtins.str,
    s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.AmazonOpenSearchServerlessBufferingHintsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.CloudWatchLoggingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    collection_endpoint: typing.Optional[builtins.str] = None,
    processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ProcessingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.AmazonOpenSearchServerlessRetryOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_backup_mode: typing.Optional[builtins.str] = None,
    vpc_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.VpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__753f83f6d86f1797776bc00b3eb90cc19e80bd47ed33370727e5209255714a3b(
    *,
    duration_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bc008db5e34e3ef0ac28740f5aa52a90ec2c2ec0ebeb06a2e361e737f34b840(
    *,
    interval_in_seconds: typing.Optional[jsii.Number] = None,
    size_in_m_bs: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd4e3bfe32a6bde0a79abfda5de58ef25a59c29217c39eadcd363cb781608bca(
    *,
    index_name: builtins.str,
    role_arn: builtins.str,
    s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.AmazonopensearchserviceBufferingHintsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.CloudWatchLoggingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cluster_endpoint: typing.Optional[builtins.str] = None,
    document_id_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DocumentIdOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    domain_arn: typing.Optional[builtins.str] = None,
    index_rotation_period: typing.Optional[builtins.str] = None,
    processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ProcessingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.AmazonopensearchserviceRetryOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_backup_mode: typing.Optional[builtins.str] = None,
    type_name: typing.Optional[builtins.str] = None,
    vpc_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.VpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3a6adce37d15471d3dfb2f014a8d32c640e5a4f535c6da724e3b743675a04cb(
    *,
    duration_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68e16a68225e493cf684cc2bfb151ded05293f2e7b47087f4a97398a1bfeaeb0(
    *,
    connectivity: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c672d0753e4b959e46f98cc809bc2380cd7be551cc9bab6f1b7baa1d203a6f7d(
    *,
    interval_in_seconds: typing.Optional[jsii.Number] = None,
    size_in_m_bs: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0992b1c8af7fd8e057904e94d1f683be6233929613125517587cd51de86aa4b5(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    log_group_name: typing.Optional[builtins.str] = None,
    log_stream_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ed6eb88a63ca5e75a449863a292b3dcd0cbfcd3127e73f575819aaf579cc41f(
    *,
    data_table_name: builtins.str,
    copy_options: typing.Optional[builtins.str] = None,
    data_table_columns: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2fd0a4fb437e036bd2436bcfd397fa35f08aba48c5a25c4aac36dedb0d37e42(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    input_format_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.InputFormatConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    output_format_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.OutputFormatConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    schema_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SchemaConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a51e3602fa39b19119cb43ff1945ccb136f7909bb7d76a42abc9195cb0d725a3(
    *,
    key_type: builtins.str,
    key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42c1d0a7a47a7fb87bd171a324b5d6ec1a60f675aa066d295f3a321445b0d566(
    *,
    hive_json_ser_de: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.HiveJsonSerDeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    open_x_json_ser_de: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.OpenXJsonSerDeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d76edd5ad2b58b9b0bbc3359143f6d89ce784d7ac50b34881cf657d8016bcec4(
    *,
    default_document_id_format: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cc891db4fb4eb3331e62299f82fedd4776288b7686ae851e51bfb6e44e55a52(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.RetryOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__081c1ee4107d2560ed72dcc369fb8bd5cb51575be94b287e3e1d199e78950677(
    *,
    interval_in_seconds: typing.Optional[jsii.Number] = None,
    size_in_m_bs: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__029a33c003279860929256e859d4ba1b8707f3f6569f11613c5f08ef467fe6d6(
    *,
    index_name: builtins.str,
    role_arn: builtins.str,
    s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ElasticsearchBufferingHintsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.CloudWatchLoggingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cluster_endpoint: typing.Optional[builtins.str] = None,
    document_id_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DocumentIdOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    domain_arn: typing.Optional[builtins.str] = None,
    index_rotation_period: typing.Optional[builtins.str] = None,
    processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ProcessingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ElasticsearchRetryOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_backup_mode: typing.Optional[builtins.str] = None,
    type_name: typing.Optional[builtins.str] = None,
    vpc_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.VpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2556301b4eb1fbc8924ad4d41633add09219c34215bad4251ecd9506fbd5f4f1(
    *,
    duration_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4416718c6f0bcd460ac15d8467b60189a1b6ff006003483c5095802962acb534(
    *,
    kms_encryption_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.KMSEncryptionConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    no_encryption_config: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7faa411782bea929613482f29819c6479d5ad2f4416ea558d510fb9fd71eaa95(
    *,
    bucket_arn: builtins.str,
    role_arn: builtins.str,
    buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.BufferingHintsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.CloudWatchLoggingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    compression_format: typing.Optional[builtins.str] = None,
    custom_time_zone: typing.Optional[builtins.str] = None,
    data_format_conversion_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DataFormatConversionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dynamic_partitioning_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DynamicPartitioningConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    error_output_prefix: typing.Optional[builtins.str] = None,
    file_extension: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
    processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ProcessingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_backup_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_backup_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8aed0e38a71aaf287d17202c1a15e108a76c336307d62f78aaec9e6482a117f(
    *,
    timestamp_formats: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d04b9e64bbadb832ca77b64870e79e2910eb18ecbaf3d42b7d1c1b17fb3c160(
    *,
    attribute_name: builtins.str,
    attribute_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0aeaa2e754e3362456fea60de1849d85d4913483f2324b0f89480dc7822dd8c(
    *,
    url: builtins.str,
    access_key: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e8b3a25c8aa6cb1c905473fb8dd18a708e794918ae12a9a622993603b96ab8a(
    *,
    endpoint_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.HttpEndpointConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.BufferingHintsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.CloudWatchLoggingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ProcessingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    request_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.HttpEndpointRequestConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.RetryOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    role_arn: typing.Optional[builtins.str] = None,
    s3_backup_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a9efa4d9f485d918f70adc5823c0a1caf4894264ec785a00d5ef0879e3c1177(
    *,
    common_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.HttpEndpointCommonAttributeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    content_encoding: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dce5223aa97132391790e172c7c143f8a4c8df67b3b09df48eb0b1dff486468b(
    *,
    deserializer: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DeserializerProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca085a464bc9440602c605444adda1cec3d2059da145bca43dd610fba2e9a8be(
    *,
    awskms_key_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ae1be427fa992bcfd551dc79aa5bba9af3c552f1661c763a814eb22ecd5dff7(
    *,
    kinesis_stream_arn: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b2563c2a3f195e01ffbb501ca4b7d501c1fb934c35f08b019e248300a348473(
    *,
    authentication_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.AuthenticationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    msk_cluster_arn: builtins.str,
    topic_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65dc173b1d3e5c449c2f9ee9f1727428f35f33407e71da72ecdc48c19f3fb78c(
    *,
    case_insensitive: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    column_to_json_key_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    convert_dots_in_json_keys_to_underscores: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a6f3732f1d1f7da40207abc3f87e65bccadac8f31c2f54e16aa9b9d2132fd6e(
    *,
    block_size_bytes: typing.Optional[jsii.Number] = None,
    bloom_filter_columns: typing.Optional[typing.Sequence[builtins.str]] = None,
    bloom_filter_false_positive_probability: typing.Optional[jsii.Number] = None,
    compression: typing.Optional[builtins.str] = None,
    dictionary_key_threshold: typing.Optional[jsii.Number] = None,
    enable_padding: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    format_version: typing.Optional[builtins.str] = None,
    padding_tolerance: typing.Optional[jsii.Number] = None,
    row_index_stride: typing.Optional[jsii.Number] = None,
    stripe_size_bytes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fcba637de22c6790633f7c4fdbfafe0f3cf2fcd07e8753fb333222a3b7916c2(
    *,
    serializer: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SerializerProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5e42046b59e857630ade1e52237b3f99ec5d3fcea0cff6ee85255354c8bc1a9(
    *,
    block_size_bytes: typing.Optional[jsii.Number] = None,
    compression: typing.Optional[builtins.str] = None,
    enable_dictionary_compression: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    max_padding_bytes: typing.Optional[jsii.Number] = None,
    page_size_bytes: typing.Optional[jsii.Number] = None,
    writer_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47d08fb3fe02427fce54795dba1288ad02d1fec20884867948eae460f986d43d(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    processors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ProcessorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29244e412176b0b05c7328e22087c12ec9670a06bdeda2a69994a31022941e39(
    *,
    parameter_name: builtins.str,
    parameter_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69c6d7cb07c53f27959cf35e3f4436c85b60c102a9d091138cad44aec29a7fc3(
    *,
    type: builtins.str,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ProcessorParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a05dc5298788a3b9496bc2e383242a0570183c6703c04af2c5e991292f2c58fa(
    *,
    cluster_jdbcurl: builtins.str,
    copy_command: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.CopyCommandProperty, typing.Dict[builtins.str, typing.Any]]],
    password: builtins.str,
    role_arn: builtins.str,
    s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    username: builtins.str,
    cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.CloudWatchLoggingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ProcessingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.RedshiftRetryOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_backup_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_backup_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0656ad0d58c235ec01fb44e9e595a95164029cf26c86a1e17d49b3de0807568(
    *,
    duration_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f65ebaf68fad95eebbec4bb62ddc86711c9f922e5243b0ef218440713a1dbf3(
    *,
    duration_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8569fcc15b3b4467365ecb9c23c43fe8704a4b9efea3337dfd60994daf97d928(
    *,
    bucket_arn: builtins.str,
    role_arn: builtins.str,
    buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.BufferingHintsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.CloudWatchLoggingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    compression_format: typing.Optional[builtins.str] = None,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    error_output_prefix: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1389c57283b687c62069951b51187332947eeb24f5fcb8781af71c2b3e5d657(
    *,
    catalog_id: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    table_name: typing.Optional[builtins.str] = None,
    version_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__706925197a1b663cd9be8234e85ce2780b58d7bf71737c801e0c393104407464(
    *,
    orc_ser_de: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.OrcSerDeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    parquet_ser_de: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ParquetSerDeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9743b3910a7f4b6edd05f7d4a76aa45c5a9f674a473fcf4c8c046e1d8d64cb53(
    *,
    account_url: builtins.str,
    database: builtins.str,
    private_key: builtins.str,
    role_arn: builtins.str,
    s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    schema: builtins.str,
    table: builtins.str,
    user: builtins.str,
    cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.CloudWatchLoggingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    content_column_name: typing.Optional[builtins.str] = None,
    data_loading_option: typing.Optional[builtins.str] = None,
    key_passphrase: typing.Optional[builtins.str] = None,
    meta_data_column_name: typing.Optional[builtins.str] = None,
    processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ProcessingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SnowflakeRetryOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_backup_mode: typing.Optional[builtins.str] = None,
    snowflake_role_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SnowflakeRoleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    snowflake_vpc_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SnowflakeVpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7d919c23da3109305810f31f91a7020b20f997fbd66a87a4b4dfe122efff981(
    *,
    duration_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__867673ab46f448fd1867f3b74172d4939969188f736abc7f1c5c26682419368b(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    snowflake_role: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5715c831de8e3fe729e9e76213a2b933810f642d09eb653534a3d23054acf0d(
    *,
    private_link_vpce_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60823c61f8aea3242c07551788af8f338bff46b6299ee9aa1d0ff6112c454ecc(
    *,
    interval_in_seconds: typing.Optional[jsii.Number] = None,
    size_in_m_bs: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be9923ea7818bcdc567ae6e06b529c44c6a3c42b59af06768977f4c55fdd20a6(
    *,
    hec_endpoint: builtins.str,
    hec_endpoint_type: builtins.str,
    hec_token: builtins.str,
    s3_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    buffering_hints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SplunkBufferingHintsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cloud_watch_logging_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.CloudWatchLoggingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    hec_acknowledgment_timeout_in_seconds: typing.Optional[jsii.Number] = None,
    processing_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ProcessingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retry_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SplunkRetryOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_backup_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c5cbe7244c68f12454d07974a4cae50f1d208afdbc3a96f1e2ada11e37fc412(
    *,
    duration_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ecd7f59955db0312a31e14fafedff3746c1d169b6a24f2985f6a096a09db25a(
    *,
    role_arn: builtins.str,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_ids: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f4e310bf0ff2c76f9c126ea4431fb25b9b53c8ba7e0c0eacc1c934debd05a95(
    *,
    amazon_open_search_serverless_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.AmazonOpenSearchServerlessDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    amazonopensearchservice_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.AmazonopensearchserviceDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    delivery_stream_encryption_configuration_input: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.DeliveryStreamEncryptionConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    delivery_stream_name: typing.Optional[builtins.str] = None,
    delivery_stream_type: typing.Optional[builtins.str] = None,
    elasticsearch_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ElasticsearchDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    extended_s3_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.ExtendedS3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    http_endpoint_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.HttpEndpointDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kinesis_stream_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.KinesisStreamSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    msk_source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.MSKSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    redshift_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.RedshiftDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.S3DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    snowflake_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SnowflakeDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    splunk_destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeliveryStream.SplunkDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
