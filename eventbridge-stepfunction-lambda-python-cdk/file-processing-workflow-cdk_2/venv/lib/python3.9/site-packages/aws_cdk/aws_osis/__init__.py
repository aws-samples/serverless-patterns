'''
# AWS::OSIS Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_osis as osis
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for OSIS construct libraries](https://constructs.dev/search?q=osis)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::OSIS resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_OSIS.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::OSIS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_OSIS.html).

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
class CfnPipeline(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_osis.CfnPipeline",
):
    '''The AWS::OSIS::Pipeline resource creates an Amazon OpenSearch Ingestion pipeline.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-osis-pipeline.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_osis as osis
        
        cfn_pipeline = osis.CfnPipeline(self, "MyCfnPipeline",
            max_units=123,
            min_units=123,
            pipeline_configuration_body="pipelineConfigurationBody",
            pipeline_name="pipelineName",
        
            # the properties below are optional
            log_publishing_options=osis.CfnPipeline.LogPublishingOptionsProperty(
                cloud_watch_log_destination=osis.CfnPipeline.CloudWatchLogDestinationProperty(
                    log_group="logGroup"
                ),
                is_logging_enabled=False
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpc_options=osis.CfnPipeline.VpcOptionsProperty(
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"]
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        max_units: jsii.Number,
        min_units: jsii.Number,
        pipeline_configuration_body: builtins.str,
        pipeline_name: builtins.str,
        log_publishing_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipeline.LogPublishingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipeline.VpcOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param max_units: The maximum pipeline capacity, in Ingestion Compute Units (ICUs).
        :param min_units: The minimum pipeline capacity, in Ingestion Compute Units (ICUs).
        :param pipeline_configuration_body: The Data Prepper pipeline configuration in YAML format.
        :param pipeline_name: The name of the pipeline.
        :param log_publishing_options: Key-value pairs that represent log publishing settings.
        :param tags: List of tags to add to the pipeline upon creation.
        :param vpc_options: Options that specify the subnets and security groups for an OpenSearch Ingestion VPC endpoint.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7720fc023720b487ee160161639df896ae055ed55f72c575e20e1b949736cfc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPipelineProps(
            max_units=max_units,
            min_units=min_units,
            pipeline_configuration_body=pipeline_configuration_body,
            pipeline_name=pipeline_name,
            log_publishing_options=log_publishing_options,
            tags=tags,
            vpc_options=vpc_options,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__239688f63c3486bc7f913474ee165697d7de6b5a8fc4adb504c14084f0bc0802)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a29ed8d3685ccad7a1a2ef94cb456f09af90c9888cf236a0c4923af8bdc422d6)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrIngestEndpointUrls")
    def attr_ingest_endpoint_urls(self) -> typing.List[builtins.str]:
        '''A list of the ingestion endpoints for the pipeline that you can send data to.

        Currently, only a single ingestion endpoint is supported for a pipeline. For example, ``my-pipeline-123456789012.us-east-1.osis.amazonaws.com`` .

        :cloudformationAttribute: IngestEndpointUrls
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrIngestEndpointUrls"))

    @builtins.property
    @jsii.member(jsii_name="attrPipelineArn")
    def attr_pipeline_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the pipeline.

        :cloudformationAttribute: PipelineArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPipelineArn"))

    @builtins.property
    @jsii.member(jsii_name="attrVpcEndpoints")
    def attr_vpc_endpoints(self) -> _IResolvable_da3f097b:
        '''The VPC interface endpoints that have access to the pipeline.

        :cloudformationAttribute: VpcEndpoints
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrVpcEndpoints"))

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
    @jsii.member(jsii_name="maxUnits")
    def max_units(self) -> jsii.Number:
        '''The maximum pipeline capacity, in Ingestion Compute Units (ICUs).'''
        return typing.cast(jsii.Number, jsii.get(self, "maxUnits"))

    @max_units.setter
    def max_units(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de251ed9641bf7b73f2296bee3997159873d7b43cf745dd7982f4ea6c583447b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxUnits", value)

    @builtins.property
    @jsii.member(jsii_name="minUnits")
    def min_units(self) -> jsii.Number:
        '''The minimum pipeline capacity, in Ingestion Compute Units (ICUs).'''
        return typing.cast(jsii.Number, jsii.get(self, "minUnits"))

    @min_units.setter
    def min_units(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a46158b7e5e312849491a71a3f8706d5845a9ab85c459d431fc07c45bbbc853)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minUnits", value)

    @builtins.property
    @jsii.member(jsii_name="pipelineConfigurationBody")
    def pipeline_configuration_body(self) -> builtins.str:
        '''The Data Prepper pipeline configuration in YAML format.'''
        return typing.cast(builtins.str, jsii.get(self, "pipelineConfigurationBody"))

    @pipeline_configuration_body.setter
    def pipeline_configuration_body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79ac63ad0c86be582b61b422db8412494c998fc04aa18a7a6c754c9656d29a6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pipelineConfigurationBody", value)

    @builtins.property
    @jsii.member(jsii_name="pipelineName")
    def pipeline_name(self) -> builtins.str:
        '''The name of the pipeline.'''
        return typing.cast(builtins.str, jsii.get(self, "pipelineName"))

    @pipeline_name.setter
    def pipeline_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df2123f129ac4fe1db88c161dd3e50f0d376738b19f6e3bef4fbe6a506140b50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pipelineName", value)

    @builtins.property
    @jsii.member(jsii_name="logPublishingOptions")
    def log_publishing_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.LogPublishingOptionsProperty"]]:
        '''Key-value pairs that represent log publishing settings.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.LogPublishingOptionsProperty"]], jsii.get(self, "logPublishingOptions"))

    @log_publishing_options.setter
    def log_publishing_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.LogPublishingOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b44b1fb090de1c3a97c62326f13cf12ff45ba873b47547be0cd3ea8680ef42e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logPublishingOptions", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''List of tags to add to the pipeline upon creation.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__678a542f1777226f3ecd76ae89117b1cbf99c7a46ef4c26f32370792db69c5ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="vpcOptions")
    def vpc_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.VpcOptionsProperty"]]:
        '''Options that specify the subnets and security groups for an OpenSearch Ingestion VPC endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.VpcOptionsProperty"]], jsii.get(self, "vpcOptions"))

    @vpc_options.setter
    def vpc_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.VpcOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fba41b395dc1c970e9d0aa14a6a1ab0253934baf83b04037847520ae16e9833c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcOptions", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_osis.CfnPipeline.CloudWatchLogDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group": "logGroup"},
    )
    class CloudWatchLogDestinationProperty:
        def __init__(self, *, log_group: typing.Optional[builtins.str] = None) -> None:
            '''The destination for OpenSearch Ingestion logs sent to Amazon CloudWatch.

            :param log_group: The name of the CloudWatch Logs group to send pipeline logs to. You can specify an existing log group or create a new one. For example, ``/aws/OpenSearchService/IngestionService/my-pipeline`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-osis-pipeline-cloudwatchlogdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_osis as osis
                
                cloud_watch_log_destination_property = osis.CfnPipeline.CloudWatchLogDestinationProperty(
                    log_group="logGroup"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c01b8e66d5b6049eed2691204d06b883fc5ba0ecb3ef2a6ff58958057fa34ad9)
                check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_group is not None:
                self._values["log_group"] = log_group

        @builtins.property
        def log_group(self) -> typing.Optional[builtins.str]:
            '''The name of the CloudWatch Logs group to send pipeline logs to.

            You can specify an existing log group or create a new one. For example, ``/aws/OpenSearchService/IngestionService/my-pipeline`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-osis-pipeline-cloudwatchlogdestination.html#cfn-osis-pipeline-cloudwatchlogdestination-loggroup
            '''
            result = self._values.get("log_group")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLogDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_osis.CfnPipeline.LogPublishingOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_log_destination": "cloudWatchLogDestination",
            "is_logging_enabled": "isLoggingEnabled",
        },
    )
    class LogPublishingOptionsProperty:
        def __init__(
            self,
            *,
            cloud_watch_log_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipeline.CloudWatchLogDestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            is_logging_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Container for the values required to configure logging for the pipeline.

            If you don't specify these values, OpenSearch Ingestion will not publish logs from your application to CloudWatch Logs.

            :param cloud_watch_log_destination: The destination for OpenSearch Ingestion logs sent to Amazon CloudWatch Logs. This parameter is required if ``IsLoggingEnabled`` is set to ``true`` .
            :param is_logging_enabled: Whether logs should be published.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-osis-pipeline-logpublishingoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_osis as osis
                
                log_publishing_options_property = osis.CfnPipeline.LogPublishingOptionsProperty(
                    cloud_watch_log_destination=osis.CfnPipeline.CloudWatchLogDestinationProperty(
                        log_group="logGroup"
                    ),
                    is_logging_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c2a4597a1154076637de8b0314d4ccfd1e5283d50069d827a0d01e2cc420bc7b)
                check_type(argname="argument cloud_watch_log_destination", value=cloud_watch_log_destination, expected_type=type_hints["cloud_watch_log_destination"])
                check_type(argname="argument is_logging_enabled", value=is_logging_enabled, expected_type=type_hints["is_logging_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloud_watch_log_destination is not None:
                self._values["cloud_watch_log_destination"] = cloud_watch_log_destination
            if is_logging_enabled is not None:
                self._values["is_logging_enabled"] = is_logging_enabled

        @builtins.property
        def cloud_watch_log_destination(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.CloudWatchLogDestinationProperty"]]:
            '''The destination for OpenSearch Ingestion logs sent to Amazon CloudWatch Logs.

            This parameter is required if ``IsLoggingEnabled`` is set to ``true`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-osis-pipeline-logpublishingoptions.html#cfn-osis-pipeline-logpublishingoptions-cloudwatchlogdestination
            '''
            result = self._values.get("cloud_watch_log_destination")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.CloudWatchLogDestinationProperty"]], result)

        @builtins.property
        def is_logging_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether logs should be published.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-osis-pipeline-logpublishingoptions.html#cfn-osis-pipeline-logpublishingoptions-isloggingenabled
            '''
            result = self._values.get("is_logging_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogPublishingOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_osis.CfnPipeline.VpcEndpointProperty",
        jsii_struct_bases=[],
        name_mapping={
            "vpc_endpoint_id": "vpcEndpointId",
            "vpc_id": "vpcId",
            "vpc_options": "vpcOptions",
        },
    )
    class VpcEndpointProperty:
        def __init__(
            self,
            *,
            vpc_endpoint_id: typing.Optional[builtins.str] = None,
            vpc_id: typing.Optional[builtins.str] = None,
            vpc_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPipeline.VpcOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''An OpenSearch Ingestion-managed VPC endpoint that will access one or more pipelines.

            :param vpc_endpoint_id: The unique identifier of the endpoint.
            :param vpc_id: The ID for your VPC. AWS PrivateLink generates this value when you create a VPC.
            :param vpc_options: Information about the VPC, including associated subnets and security groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-osis-pipeline-vpcendpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_osis as osis
                
                vpc_endpoint_property = osis.CfnPipeline.VpcEndpointProperty(
                    vpc_endpoint_id="vpcEndpointId",
                    vpc_id="vpcId",
                    vpc_options=osis.CfnPipeline.VpcOptionsProperty(
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8d38e6cb9cbcb864c898af5877a119ef843fc9588abfbe68a92321cf3eeaf341)
                check_type(argname="argument vpc_endpoint_id", value=vpc_endpoint_id, expected_type=type_hints["vpc_endpoint_id"])
                check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
                check_type(argname="argument vpc_options", value=vpc_options, expected_type=type_hints["vpc_options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if vpc_endpoint_id is not None:
                self._values["vpc_endpoint_id"] = vpc_endpoint_id
            if vpc_id is not None:
                self._values["vpc_id"] = vpc_id
            if vpc_options is not None:
                self._values["vpc_options"] = vpc_options

        @builtins.property
        def vpc_endpoint_id(self) -> typing.Optional[builtins.str]:
            '''The unique identifier of the endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-osis-pipeline-vpcendpoint.html#cfn-osis-pipeline-vpcendpoint-vpcendpointid
            '''
            result = self._values.get("vpc_endpoint_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_id(self) -> typing.Optional[builtins.str]:
            '''The ID for your VPC.

            AWS PrivateLink generates this value when you create a VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-osis-pipeline-vpcendpoint.html#cfn-osis-pipeline-vpcendpoint-vpcid
            '''
            result = self._values.get("vpc_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.VpcOptionsProperty"]]:
            '''Information about the VPC, including associated subnets and security groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-osis-pipeline-vpcendpoint.html#cfn-osis-pipeline-vpcendpoint-vpcoptions
            '''
            result = self._values.get("vpc_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPipeline.VpcOptionsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcEndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_osis.CfnPipeline.VpcOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class VpcOptionsProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Options that specify the subnets and security groups for an OpenSearch Ingestion VPC endpoint.

            :param security_group_ids: A list of security groups associated with the VPC endpoint.
            :param subnet_ids: A list of subnet IDs associated with the VPC endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-osis-pipeline-vpcoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_osis as osis
                
                vpc_options_property = osis.CfnPipeline.VpcOptionsProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d6c7fc6663c9baefdd81f02e0e69deb4e81a8e210a00a4346752ffa95aa926ac)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if subnet_ids is not None:
                self._values["subnet_ids"] = subnet_ids

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of security groups associated with the VPC endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-osis-pipeline-vpcoptions.html#cfn-osis-pipeline-vpcoptions-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of subnet IDs associated with the VPC endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-osis-pipeline-vpcoptions.html#cfn-osis-pipeline-vpcoptions-subnetids
            '''
            result = self._values.get("subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_osis.CfnPipelineProps",
    jsii_struct_bases=[],
    name_mapping={
        "max_units": "maxUnits",
        "min_units": "minUnits",
        "pipeline_configuration_body": "pipelineConfigurationBody",
        "pipeline_name": "pipelineName",
        "log_publishing_options": "logPublishingOptions",
        "tags": "tags",
        "vpc_options": "vpcOptions",
    },
)
class CfnPipelineProps:
    def __init__(
        self,
        *,
        max_units: jsii.Number,
        min_units: jsii.Number,
        pipeline_configuration_body: builtins.str,
        pipeline_name: builtins.str,
        log_publishing_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipeline.LogPublishingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipeline.VpcOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPipeline``.

        :param max_units: The maximum pipeline capacity, in Ingestion Compute Units (ICUs).
        :param min_units: The minimum pipeline capacity, in Ingestion Compute Units (ICUs).
        :param pipeline_configuration_body: The Data Prepper pipeline configuration in YAML format.
        :param pipeline_name: The name of the pipeline.
        :param log_publishing_options: Key-value pairs that represent log publishing settings.
        :param tags: List of tags to add to the pipeline upon creation.
        :param vpc_options: Options that specify the subnets and security groups for an OpenSearch Ingestion VPC endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-osis-pipeline.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_osis as osis
            
            cfn_pipeline_props = osis.CfnPipelineProps(
                max_units=123,
                min_units=123,
                pipeline_configuration_body="pipelineConfigurationBody",
                pipeline_name="pipelineName",
            
                # the properties below are optional
                log_publishing_options=osis.CfnPipeline.LogPublishingOptionsProperty(
                    cloud_watch_log_destination=osis.CfnPipeline.CloudWatchLogDestinationProperty(
                        log_group="logGroup"
                    ),
                    is_logging_enabled=False
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpc_options=osis.CfnPipeline.VpcOptionsProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5ae24cae502e48ff4f681bebbc941bf569bb00330722c27b6a689ced8f28145)
            check_type(argname="argument max_units", value=max_units, expected_type=type_hints["max_units"])
            check_type(argname="argument min_units", value=min_units, expected_type=type_hints["min_units"])
            check_type(argname="argument pipeline_configuration_body", value=pipeline_configuration_body, expected_type=type_hints["pipeline_configuration_body"])
            check_type(argname="argument pipeline_name", value=pipeline_name, expected_type=type_hints["pipeline_name"])
            check_type(argname="argument log_publishing_options", value=log_publishing_options, expected_type=type_hints["log_publishing_options"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc_options", value=vpc_options, expected_type=type_hints["vpc_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "max_units": max_units,
            "min_units": min_units,
            "pipeline_configuration_body": pipeline_configuration_body,
            "pipeline_name": pipeline_name,
        }
        if log_publishing_options is not None:
            self._values["log_publishing_options"] = log_publishing_options
        if tags is not None:
            self._values["tags"] = tags
        if vpc_options is not None:
            self._values["vpc_options"] = vpc_options

    @builtins.property
    def max_units(self) -> jsii.Number:
        '''The maximum pipeline capacity, in Ingestion Compute Units (ICUs).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-osis-pipeline.html#cfn-osis-pipeline-maxunits
        '''
        result = self._values.get("max_units")
        assert result is not None, "Required property 'max_units' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min_units(self) -> jsii.Number:
        '''The minimum pipeline capacity, in Ingestion Compute Units (ICUs).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-osis-pipeline.html#cfn-osis-pipeline-minunits
        '''
        result = self._values.get("min_units")
        assert result is not None, "Required property 'min_units' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def pipeline_configuration_body(self) -> builtins.str:
        '''The Data Prepper pipeline configuration in YAML format.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-osis-pipeline.html#cfn-osis-pipeline-pipelineconfigurationbody
        '''
        result = self._values.get("pipeline_configuration_body")
        assert result is not None, "Required property 'pipeline_configuration_body' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pipeline_name(self) -> builtins.str:
        '''The name of the pipeline.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-osis-pipeline.html#cfn-osis-pipeline-pipelinename
        '''
        result = self._values.get("pipeline_name")
        assert result is not None, "Required property 'pipeline_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_publishing_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPipeline.LogPublishingOptionsProperty]]:
        '''Key-value pairs that represent log publishing settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-osis-pipeline.html#cfn-osis-pipeline-logpublishingoptions
        '''
        result = self._values.get("log_publishing_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPipeline.LogPublishingOptionsProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''List of tags to add to the pipeline upon creation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-osis-pipeline.html#cfn-osis-pipeline-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def vpc_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPipeline.VpcOptionsProperty]]:
        '''Options that specify the subnets and security groups for an OpenSearch Ingestion VPC endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-osis-pipeline.html#cfn-osis-pipeline-vpcoptions
        '''
        result = self._values.get("vpc_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPipeline.VpcOptionsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPipelineProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnPipeline",
    "CfnPipelineProps",
]

publication.publish()

def _typecheckingstub__f7720fc023720b487ee160161639df896ae055ed55f72c575e20e1b949736cfc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    max_units: jsii.Number,
    min_units: jsii.Number,
    pipeline_configuration_body: builtins.str,
    pipeline_name: builtins.str,
    log_publishing_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipeline.LogPublishingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipeline.VpcOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__239688f63c3486bc7f913474ee165697d7de6b5a8fc4adb504c14084f0bc0802(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a29ed8d3685ccad7a1a2ef94cb456f09af90c9888cf236a0c4923af8bdc422d6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de251ed9641bf7b73f2296bee3997159873d7b43cf745dd7982f4ea6c583447b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a46158b7e5e312849491a71a3f8706d5845a9ab85c459d431fc07c45bbbc853(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79ac63ad0c86be582b61b422db8412494c998fc04aa18a7a6c754c9656d29a6f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df2123f129ac4fe1db88c161dd3e50f0d376738b19f6e3bef4fbe6a506140b50(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b44b1fb090de1c3a97c62326f13cf12ff45ba873b47547be0cd3ea8680ef42e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPipeline.LogPublishingOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__678a542f1777226f3ecd76ae89117b1cbf99c7a46ef4c26f32370792db69c5ad(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fba41b395dc1c970e9d0aa14a6a1ab0253934baf83b04037847520ae16e9833c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPipeline.VpcOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c01b8e66d5b6049eed2691204d06b883fc5ba0ecb3ef2a6ff58958057fa34ad9(
    *,
    log_group: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2a4597a1154076637de8b0314d4ccfd1e5283d50069d827a0d01e2cc420bc7b(
    *,
    cloud_watch_log_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipeline.CloudWatchLogDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    is_logging_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d38e6cb9cbcb864c898af5877a119ef843fc9588abfbe68a92321cf3eeaf341(
    *,
    vpc_endpoint_id: typing.Optional[builtins.str] = None,
    vpc_id: typing.Optional[builtins.str] = None,
    vpc_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipeline.VpcOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6c7fc6663c9baefdd81f02e0e69deb4e81a8e210a00a4346752ffa95aa926ac(
    *,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5ae24cae502e48ff4f681bebbc941bf569bb00330722c27b6a689ced8f28145(
    *,
    max_units: jsii.Number,
    min_units: jsii.Number,
    pipeline_configuration_body: builtins.str,
    pipeline_name: builtins.str,
    log_publishing_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipeline.LogPublishingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPipeline.VpcOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
