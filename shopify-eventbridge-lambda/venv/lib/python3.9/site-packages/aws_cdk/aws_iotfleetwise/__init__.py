'''
# AWS::IoTFleetWise Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_iotfleetwise as iotfleetwise
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for IoTFleetWise construct libraries](https://constructs.dev/search?q=iotfleetwise)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::IoTFleetWise resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTFleetWise.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::IoTFleetWise](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_IoTFleetWise.html).

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
class CfnCampaign(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnCampaign",
):
    '''Creates an orchestration of data collection rules.

    The AWS IoT FleetWise Edge Agent software running in vehicles uses campaigns to decide how to collect and transfer data to the cloud. You create campaigns in the cloud. After you or your team approve campaigns, AWS IoT FleetWise automatically deploys them to vehicles.

    For more information, see `Collect and transfer data with campaigns <https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/campaigns.html>`_ in the *AWS IoT FleetWise Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html
    :cloudformationResource: AWS::IoTFleetWise::Campaign
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotfleetwise as iotfleetwise
        
        cfn_campaign = iotfleetwise.CfnCampaign(self, "MyCfnCampaign",
            action="action",
            collection_scheme=iotfleetwise.CfnCampaign.CollectionSchemeProperty(
                condition_based_collection_scheme=iotfleetwise.CfnCampaign.ConditionBasedCollectionSchemeProperty(
                    expression="expression",
        
                    # the properties below are optional
                    condition_language_version=123,
                    minimum_trigger_interval_ms=123,
                    trigger_mode="triggerMode"
                ),
                time_based_collection_scheme=iotfleetwise.CfnCampaign.TimeBasedCollectionSchemeProperty(
                    period_ms=123
                )
            ),
            name="name",
            signal_catalog_arn="signalCatalogArn",
            target_arn="targetArn",
        
            # the properties below are optional
            compression="compression",
            data_destination_configs=[iotfleetwise.CfnCampaign.DataDestinationConfigProperty(
                s3_config=iotfleetwise.CfnCampaign.S3ConfigProperty(
                    bucket_arn="bucketArn",
        
                    # the properties below are optional
                    data_format="dataFormat",
                    prefix="prefix",
                    storage_compression_format="storageCompressionFormat"
                ),
                timestream_config=iotfleetwise.CfnCampaign.TimestreamConfigProperty(
                    execution_role_arn="executionRoleArn",
                    timestream_table_arn="timestreamTableArn"
                )
            )],
            data_extra_dimensions=["dataExtraDimensions"],
            description="description",
            diagnostics_mode="diagnosticsMode",
            expiry_time="expiryTime",
            post_trigger_collection_duration=123,
            priority=123,
            signals_to_collect=[iotfleetwise.CfnCampaign.SignalInformationProperty(
                name="name",
        
                # the properties below are optional
                max_sample_count=123,
                minimum_sampling_interval_ms=123
            )],
            spooling_mode="spoolingMode",
            start_time="startTime",
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
        action: builtins.str,
        collection_scheme: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.CollectionSchemeProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        signal_catalog_arn: builtins.str,
        target_arn: builtins.str,
        compression: typing.Optional[builtins.str] = None,
        data_destination_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.DataDestinationConfigProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        data_extra_dimensions: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        diagnostics_mode: typing.Optional[builtins.str] = None,
        expiry_time: typing.Optional[builtins.str] = None,
        post_trigger_collection_duration: typing.Optional[jsii.Number] = None,
        priority: typing.Optional[jsii.Number] = None,
        signals_to_collect: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.SignalInformationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        spooling_mode: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param action: Specifies how to update a campaign. The action can be one of the following:. - ``APPROVE`` - To approve delivering a data collection scheme to vehicles. - ``SUSPEND`` - To suspend collecting signal data. The campaign is deleted from vehicles and all vehicles in the suspended campaign will stop sending data. - ``RESUME`` - To reactivate the ``SUSPEND`` campaign. The campaign is redeployed to all vehicles and the vehicles will resume sending data. - ``UPDATE`` - To update a campaign.
        :param collection_scheme: The data collection scheme associated with the campaign. You can specify a scheme that collects data based on time or an event.
        :param name: The name of a campaign.
        :param signal_catalog_arn: The Amazon Resource Name (ARN) of the signal catalog associated with the campaign.
        :param target_arn: The Amazon Resource Name (ARN) of a vehicle or fleet to which the campaign is deployed.
        :param compression: (Optional) Whether to compress signals before transmitting data to AWS IoT FleetWise . If you don't want to compress the signals, use ``OFF`` . If it's not specified, ``SNAPPY`` is used. Default: ``SNAPPY`` Default: - "OFF"
        :param data_destination_configs: (Optional) The destination where the campaign sends data. You can choose to send data to be stored in Amazon S3 or Amazon Timestream . Amazon S3 optimizes the cost of data storage and provides additional mechanisms to use vehicle data, such as data lakes, centralized data storage, data processing pipelines, and analytics. AWS IoT FleetWise supports at-least-once file delivery to S3. Your vehicle data is stored on multiple AWS IoT FleetWise servers for redundancy and high availability. You can use Amazon Timestream to access and analyze time series data, and Timestream to query vehicle data so that you can identify trends and patterns.
        :param data_extra_dimensions: (Optional) A list of vehicle attributes to associate with a campaign. Enrich the data with specified vehicle attributes. For example, add ``make`` and ``model`` to the campaign, and AWS IoT FleetWise will associate the data with those attributes as dimensions in Amazon Timestream . You can then query the data against ``make`` and ``model`` . Default: An empty array
        :param description: (Optional) The description of the campaign.
        :param diagnostics_mode: (Optional) Option for a vehicle to send diagnostic trouble codes to AWS IoT FleetWise . If you want to send diagnostic trouble codes, use ``SEND_ACTIVE_DTCS`` . If it's not specified, ``OFF`` is used. Default: ``OFF`` Default: - "OFF"
        :param expiry_time: (Optional) The time the campaign expires, in seconds since epoch (January 1, 1970 at midnight UTC time). Vehicle data isn't collected after the campaign expires. Default: 253402214400 (December 31, 9999, 00:00:00 UTC) Default: - "253402214400"
        :param post_trigger_collection_duration: (Optional) How long (in milliseconds) to collect raw data after a triggering event initiates the collection. If it's not specified, ``0`` is used. Default: ``0`` Default: - 0
        :param priority: (Optional) A number indicating the priority of one campaign over another campaign for a certain vehicle or fleet. A campaign with the lowest value is deployed to vehicles before any other campaigns. If it's not specified, ``0`` is used. Default: ``0`` Default: - 0
        :param signals_to_collect: (Optional) A list of information about signals to collect.
        :param spooling_mode: (Optional) Whether to store collected data after a vehicle lost a connection with the cloud. After a connection is re-established, the data is automatically forwarded to AWS IoT FleetWise . If you want to store collected data when a vehicle loses connection with the cloud, use ``TO_DISK`` . If it's not specified, ``OFF`` is used. Default: ``OFF`` Default: - "OFF"
        :param start_time: (Optional) The time, in milliseconds, to deliver a campaign after it was approved. If it's not specified, ``0`` is used. Default: ``0`` Default: - "0"
        :param tags: (Optional) Metadata that can be used to manage the campaign.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7abc45d2046b48ec3bc5807ec2826a784930a5009b41b194dd6e4bed2413f8d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCampaignProps(
            action=action,
            collection_scheme=collection_scheme,
            name=name,
            signal_catalog_arn=signal_catalog_arn,
            target_arn=target_arn,
            compression=compression,
            data_destination_configs=data_destination_configs,
            data_extra_dimensions=data_extra_dimensions,
            description=description,
            diagnostics_mode=diagnostics_mode,
            expiry_time=expiry_time,
            post_trigger_collection_duration=post_trigger_collection_duration,
            priority=priority,
            signals_to_collect=signals_to_collect,
            spooling_mode=spooling_mode,
            start_time=start_time,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09fbf1d259fb24b3ffc81851949fdbc1abbaa3df7fef9d0031938dd5b723205f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__89d4f6e55fdf4b8418716e773b2a62dc1763b8a2553490a7567e2cfe6f27d77f)
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
        '''The Amazon Resource Name (ARN) of the campaign.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The time the campaign was created in seconds since epoch (January 1, 1970 at midnight UTC time).

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModificationTime")
    def attr_last_modification_time(self) -> builtins.str:
        '''The last time the campaign was modified.

        :cloudformationAttribute: LastModificationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModificationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The state of the campaign.

        The status can be one of: ``CREATING`` , ``WAITING_FOR_APPROVAL`` , ``RUNNING`` , and ``SUSPENDED`` .

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

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
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        '''Specifies how to update a campaign.

        The action can be one of the following:.
        '''
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66dafa89e69b8562346040c56213280b8861d04a6b73911f5471941f58e3d463)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="collectionScheme")
    def collection_scheme(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnCampaign.CollectionSchemeProperty"]:
        '''The data collection scheme associated with the campaign.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCampaign.CollectionSchemeProperty"], jsii.get(self, "collectionScheme"))

    @collection_scheme.setter
    def collection_scheme(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnCampaign.CollectionSchemeProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__868a9ff35e32583e37d3c029fdca22ea031055a38c7dd0dcbfa1f30846ee551d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collectionScheme", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of a campaign.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61dfb8819034de21f19e0466ab15e542f6b7270be82092cfffb60970bbc9708b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="signalCatalogArn")
    def signal_catalog_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the signal catalog associated with the campaign.'''
        return typing.cast(builtins.str, jsii.get(self, "signalCatalogArn"))

    @signal_catalog_arn.setter
    def signal_catalog_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5a5ce376850a7a86f93938b2f133fca5cc48d27769ddbdcaf2291ab00d48bac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signalCatalogArn", value)

    @builtins.property
    @jsii.member(jsii_name="targetArn")
    def target_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of a vehicle or fleet to which the campaign is deployed.'''
        return typing.cast(builtins.str, jsii.get(self, "targetArn"))

    @target_arn.setter
    def target_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6154b7ad20e73a4e23143d3707a09d050bbb1092b307bc8e0145589083575f5a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetArn", value)

    @builtins.property
    @jsii.member(jsii_name="compression")
    def compression(self) -> typing.Optional[builtins.str]:
        '''(Optional) Whether to compress signals before transmitting data to AWS IoT FleetWise .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compression"))

    @compression.setter
    def compression(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17ec1dfb29d11e0d55dc84fc23937babfb2d1e33fdf8192c23c4130716fa6a02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compression", value)

    @builtins.property
    @jsii.member(jsii_name="dataDestinationConfigs")
    def data_destination_configs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCampaign.DataDestinationConfigProperty"]]]]:
        '''(Optional) The destination where the campaign sends data.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCampaign.DataDestinationConfigProperty"]]]], jsii.get(self, "dataDestinationConfigs"))

    @data_destination_configs.setter
    def data_destination_configs(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCampaign.DataDestinationConfigProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82921435d923d6321ee61688fc07b3aa8e4790a3f86fff3b232ba9bb71993646)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataDestinationConfigs", value)

    @builtins.property
    @jsii.member(jsii_name="dataExtraDimensions")
    def data_extra_dimensions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(Optional) A list of vehicle attributes to associate with a campaign.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dataExtraDimensions"))

    @data_extra_dimensions.setter
    def data_extra_dimensions(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d948dada7b0177410b9932e42eb5ef3a76fe3c3274594fb0b3ffa49ded440324)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataExtraDimensions", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(Optional) The description of the campaign.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24bd4808a24c1ef5c17e4550fe902693202fc86dca7d97ddddcd994c722276bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="diagnosticsMode")
    def diagnostics_mode(self) -> typing.Optional[builtins.str]:
        '''(Optional) Option for a vehicle to send diagnostic trouble codes to AWS IoT FleetWise .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diagnosticsMode"))

    @diagnostics_mode.setter
    def diagnostics_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e28d99e6bd56db5b97b272b04aeb5c1af8103d1b8b0080fe05d1a5f2fb149e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diagnosticsMode", value)

    @builtins.property
    @jsii.member(jsii_name="expiryTime")
    def expiry_time(self) -> typing.Optional[builtins.str]:
        '''(Optional) The time the campaign expires, in seconds since epoch (January 1, 1970 at midnight UTC time).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expiryTime"))

    @expiry_time.setter
    def expiry_time(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11cce95e76c12143123da5bc8c755592e90256d2ed3e61b6cd5a6d839e9318e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expiryTime", value)

    @builtins.property
    @jsii.member(jsii_name="postTriggerCollectionDuration")
    def post_trigger_collection_duration(self) -> typing.Optional[jsii.Number]:
        '''(Optional) How long (in milliseconds) to collect raw data after a triggering event initiates the collection.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "postTriggerCollectionDuration"))

    @post_trigger_collection_duration.setter
    def post_trigger_collection_duration(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__660bebd5ebd77dcec64e7fcb6fd086f3ce7252832c2b9967a58fbda5d5fe6bd2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postTriggerCollectionDuration", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> typing.Optional[jsii.Number]:
        '''(Optional) A number indicating the priority of one campaign over another campaign for a certain vehicle or fleet.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7eceb1aaf4de04c54d69e423a5e6de547b2e207a605050b36deefed0ccc4c9b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="signalsToCollect")
    def signals_to_collect(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCampaign.SignalInformationProperty"]]]]:
        '''(Optional) A list of information about signals to collect.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCampaign.SignalInformationProperty"]]]], jsii.get(self, "signalsToCollect"))

    @signals_to_collect.setter
    def signals_to_collect(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCampaign.SignalInformationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49e9a686748dfc74bfa8ee7c7e9c87ccd64dc236b6b72144f22cebb87065a3d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signalsToCollect", value)

    @builtins.property
    @jsii.member(jsii_name="spoolingMode")
    def spooling_mode(self) -> typing.Optional[builtins.str]:
        '''(Optional) Whether to store collected data after a vehicle lost a connection with the cloud.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "spoolingMode"))

    @spooling_mode.setter
    def spooling_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2470f955a4e2089dd25722e38734a0e9fffc60420def257c19a15c6db378b523)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "spoolingMode", value)

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> typing.Optional[builtins.str]:
        '''(Optional) The time, in milliseconds, to deliver a campaign after it was approved.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startTime"))

    @start_time.setter
    def start_time(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67bb9c23f09e7b35b9a93baa91bd26954a931e9dac0ecfa4b472a8de197849a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startTime", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''(Optional) Metadata that can be used to manage the campaign.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3493674fad7a8f212642ff0171f2ddf22e133359a2aee9ae22d9b3da5be4a8b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnCampaign.CollectionSchemeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "condition_based_collection_scheme": "conditionBasedCollectionScheme",
            "time_based_collection_scheme": "timeBasedCollectionScheme",
        },
    )
    class CollectionSchemeProperty:
        def __init__(
            self,
            *,
            condition_based_collection_scheme: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.ConditionBasedCollectionSchemeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            time_based_collection_scheme: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.TimeBasedCollectionSchemeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies what data to collect and how often or when to collect it.

            :param condition_based_collection_scheme: (Optional) Information about a collection scheme that uses a simple logical expression to recognize what data to collect.
            :param time_based_collection_scheme: (Optional) Information about a collection scheme that uses a time period to decide how often to collect data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-collectionscheme.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                collection_scheme_property = iotfleetwise.CfnCampaign.CollectionSchemeProperty(
                    condition_based_collection_scheme=iotfleetwise.CfnCampaign.ConditionBasedCollectionSchemeProperty(
                        expression="expression",
                
                        # the properties below are optional
                        condition_language_version=123,
                        minimum_trigger_interval_ms=123,
                        trigger_mode="triggerMode"
                    ),
                    time_based_collection_scheme=iotfleetwise.CfnCampaign.TimeBasedCollectionSchemeProperty(
                        period_ms=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1d2862e457404e83c11e21830d9ccb15c52f442305bb2db0a1ebf80b0de3877a)
                check_type(argname="argument condition_based_collection_scheme", value=condition_based_collection_scheme, expected_type=type_hints["condition_based_collection_scheme"])
                check_type(argname="argument time_based_collection_scheme", value=time_based_collection_scheme, expected_type=type_hints["time_based_collection_scheme"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if condition_based_collection_scheme is not None:
                self._values["condition_based_collection_scheme"] = condition_based_collection_scheme
            if time_based_collection_scheme is not None:
                self._values["time_based_collection_scheme"] = time_based_collection_scheme

        @builtins.property
        def condition_based_collection_scheme(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.ConditionBasedCollectionSchemeProperty"]]:
            '''(Optional) Information about a collection scheme that uses a simple logical expression to recognize what data to collect.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-collectionscheme.html#cfn-iotfleetwise-campaign-collectionscheme-conditionbasedcollectionscheme
            '''
            result = self._values.get("condition_based_collection_scheme")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.ConditionBasedCollectionSchemeProperty"]], result)

        @builtins.property
        def time_based_collection_scheme(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TimeBasedCollectionSchemeProperty"]]:
            '''(Optional) Information about a collection scheme that uses a time period to decide how often to collect data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-collectionscheme.html#cfn-iotfleetwise-campaign-collectionscheme-timebasedcollectionscheme
            '''
            result = self._values.get("time_based_collection_scheme")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TimeBasedCollectionSchemeProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CollectionSchemeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnCampaign.ConditionBasedCollectionSchemeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "expression": "expression",
            "condition_language_version": "conditionLanguageVersion",
            "minimum_trigger_interval_ms": "minimumTriggerIntervalMs",
            "trigger_mode": "triggerMode",
        },
    )
    class ConditionBasedCollectionSchemeProperty:
        def __init__(
            self,
            *,
            expression: builtins.str,
            condition_language_version: typing.Optional[jsii.Number] = None,
            minimum_trigger_interval_ms: typing.Optional[jsii.Number] = None,
            trigger_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about a collection scheme that uses a simple logical expression to recognize what data to collect.

            :param expression: The logical expression used to recognize what data to collect. For example, ``$variable.Vehicle.OutsideAirTemperature >= 105.0`` .
            :param condition_language_version: (Optional) Specifies the version of the conditional expression language.
            :param minimum_trigger_interval_ms: (Optional) The minimum duration of time between two triggering events to collect data, in milliseconds. .. epigraph:: If a signal changes often, you might want to collect data at a slower rate.
            :param trigger_mode: (Optional) Whether to collect data for all triggering events ( ``ALWAYS`` ). Specify ( ``RISING_EDGE`` ), or specify only when the condition first evaluates to false. For example, triggering on "AirbagDeployed"; Users aren't interested on triggering when the airbag is already exploded; they only care about the change from not deployed => deployed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-conditionbasedcollectionscheme.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                condition_based_collection_scheme_property = iotfleetwise.CfnCampaign.ConditionBasedCollectionSchemeProperty(
                    expression="expression",
                
                    # the properties below are optional
                    condition_language_version=123,
                    minimum_trigger_interval_ms=123,
                    trigger_mode="triggerMode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dd3351de9470a98f13f006dd95deedef6c30dbfc08cdfe7bde2b9d950d547615)
                check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
                check_type(argname="argument condition_language_version", value=condition_language_version, expected_type=type_hints["condition_language_version"])
                check_type(argname="argument minimum_trigger_interval_ms", value=minimum_trigger_interval_ms, expected_type=type_hints["minimum_trigger_interval_ms"])
                check_type(argname="argument trigger_mode", value=trigger_mode, expected_type=type_hints["trigger_mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "expression": expression,
            }
            if condition_language_version is not None:
                self._values["condition_language_version"] = condition_language_version
            if minimum_trigger_interval_ms is not None:
                self._values["minimum_trigger_interval_ms"] = minimum_trigger_interval_ms
            if trigger_mode is not None:
                self._values["trigger_mode"] = trigger_mode

        @builtins.property
        def expression(self) -> builtins.str:
            '''The logical expression used to recognize what data to collect.

            For example, ``$variable.Vehicle.OutsideAirTemperature >= 105.0`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-conditionbasedcollectionscheme.html#cfn-iotfleetwise-campaign-conditionbasedcollectionscheme-expression
            '''
            result = self._values.get("expression")
            assert result is not None, "Required property 'expression' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def condition_language_version(self) -> typing.Optional[jsii.Number]:
            '''(Optional) Specifies the version of the conditional expression language.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-conditionbasedcollectionscheme.html#cfn-iotfleetwise-campaign-conditionbasedcollectionscheme-conditionlanguageversion
            '''
            result = self._values.get("condition_language_version")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def minimum_trigger_interval_ms(self) -> typing.Optional[jsii.Number]:
            '''(Optional) The minimum duration of time between two triggering events to collect data, in milliseconds.

            .. epigraph::

               If a signal changes often, you might want to collect data at a slower rate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-conditionbasedcollectionscheme.html#cfn-iotfleetwise-campaign-conditionbasedcollectionscheme-minimumtriggerintervalms
            '''
            result = self._values.get("minimum_trigger_interval_ms")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def trigger_mode(self) -> typing.Optional[builtins.str]:
            '''(Optional) Whether to collect data for all triggering events ( ``ALWAYS`` ).

            Specify ( ``RISING_EDGE`` ), or specify only when the condition first evaluates to false. For example, triggering on "AirbagDeployed"; Users aren't interested on triggering when the airbag is already exploded; they only care about the change from not deployed => deployed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-conditionbasedcollectionscheme.html#cfn-iotfleetwise-campaign-conditionbasedcollectionscheme-triggermode
            '''
            result = self._values.get("trigger_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConditionBasedCollectionSchemeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnCampaign.DataDestinationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "s3_config": "s3Config",
            "timestream_config": "timestreamConfig",
        },
    )
    class DataDestinationConfigProperty:
        def __init__(
            self,
            *,
            s3_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.S3ConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            timestream_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCampaign.TimestreamConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The destination where the AWS IoT FleetWise campaign sends data.

            You can send data to be stored in Amazon S3 or Amazon Timestream .

            :param s3_config: (Optional) The Amazon S3 bucket where the AWS IoT FleetWise campaign sends data.
            :param timestream_config: (Optional) The Amazon Timestream table where the campaign sends data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-datadestinationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                data_destination_config_property = iotfleetwise.CfnCampaign.DataDestinationConfigProperty(
                    s3_config=iotfleetwise.CfnCampaign.S3ConfigProperty(
                        bucket_arn="bucketArn",
                
                        # the properties below are optional
                        data_format="dataFormat",
                        prefix="prefix",
                        storage_compression_format="storageCompressionFormat"
                    ),
                    timestream_config=iotfleetwise.CfnCampaign.TimestreamConfigProperty(
                        execution_role_arn="executionRoleArn",
                        timestream_table_arn="timestreamTableArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a76d3ecac8a3286ba64142d7bb2621dd82495be58438bdb339be1559bb8129f3)
                check_type(argname="argument s3_config", value=s3_config, expected_type=type_hints["s3_config"])
                check_type(argname="argument timestream_config", value=timestream_config, expected_type=type_hints["timestream_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if s3_config is not None:
                self._values["s3_config"] = s3_config
            if timestream_config is not None:
                self._values["timestream_config"] = timestream_config

        @builtins.property
        def s3_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.S3ConfigProperty"]]:
            '''(Optional) The Amazon S3 bucket where the AWS IoT FleetWise campaign sends data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-datadestinationconfig.html#cfn-iotfleetwise-campaign-datadestinationconfig-s3config
            '''
            result = self._values.get("s3_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.S3ConfigProperty"]], result)

        @builtins.property
        def timestream_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TimestreamConfigProperty"]]:
            '''(Optional) The Amazon Timestream table where the campaign sends data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-datadestinationconfig.html#cfn-iotfleetwise-campaign-datadestinationconfig-timestreamconfig
            '''
            result = self._values.get("timestream_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCampaign.TimestreamConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataDestinationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnCampaign.S3ConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_arn": "bucketArn",
            "data_format": "dataFormat",
            "prefix": "prefix",
            "storage_compression_format": "storageCompressionFormat",
        },
    )
    class S3ConfigProperty:
        def __init__(
            self,
            *,
            bucket_arn: builtins.str,
            data_format: typing.Optional[builtins.str] = None,
            prefix: typing.Optional[builtins.str] = None,
            storage_compression_format: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The Amazon S3 bucket where the AWS IoT FleetWise campaign sends data.

            Amazon S3 is an object storage service that stores data as objects within buckets. For more information, see `Creating, configuring, and working with Amazon S3 buckets <https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html>`_ in the *Amazon Simple Storage Service User Guide* .

            :param bucket_arn: The Amazon Resource Name (ARN) of the Amazon S3 bucket.
            :param data_format: (Optional) Specify the format that files are saved in the Amazon S3 bucket. You can save files in an Apache Parquet or JSON format. - Parquet - Store data in a columnar storage file format. Parquet is optimal for fast data retrieval and can reduce costs. This option is selected by default. - JSON - Store data in a standard text-based JSON file format.
            :param prefix: (Optional) Enter an S3 bucket prefix. The prefix is the string of characters after the bucket name and before the object name. You can use the prefix to organize data stored in Amazon S3 buckets. For more information, see `Organizing objects using prefixes <https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html>`_ in the *Amazon Simple Storage Service User Guide* . By default, AWS IoT FleetWise sets the prefix ``processed-data/year=YY/month=MM/date=DD/hour=HH/`` (in UTC) to data it delivers to Amazon S3 . You can enter a prefix to append it to this default prefix. For example, if you enter the prefix ``vehicles`` , the prefix will be ``vehicles/processed-data/year=YY/month=MM/date=DD/hour=HH/`` .
            :param storage_compression_format: (Optional) By default, stored data is compressed as a .gzip file. Compressed files have a reduced file size, which can optimize the cost of data storage.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-s3config.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                s3_config_property = iotfleetwise.CfnCampaign.S3ConfigProperty(
                    bucket_arn="bucketArn",
                
                    # the properties below are optional
                    data_format="dataFormat",
                    prefix="prefix",
                    storage_compression_format="storageCompressionFormat"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cb82e0c92a9fdd48764ec7ba91d5dabd16d19776d63621d9b09fba43e604eb8a)
                check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
                check_type(argname="argument data_format", value=data_format, expected_type=type_hints["data_format"])
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
                check_type(argname="argument storage_compression_format", value=storage_compression_format, expected_type=type_hints["storage_compression_format"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_arn": bucket_arn,
            }
            if data_format is not None:
                self._values["data_format"] = data_format
            if prefix is not None:
                self._values["prefix"] = prefix
            if storage_compression_format is not None:
                self._values["storage_compression_format"] = storage_compression_format

        @builtins.property
        def bucket_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Amazon S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-s3config.html#cfn-iotfleetwise-campaign-s3config-bucketarn
            '''
            result = self._values.get("bucket_arn")
            assert result is not None, "Required property 'bucket_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def data_format(self) -> typing.Optional[builtins.str]:
            '''(Optional) Specify the format that files are saved in the Amazon S3 bucket.

            You can save files in an Apache Parquet or JSON format.

            - Parquet - Store data in a columnar storage file format. Parquet is optimal for fast data retrieval and can reduce costs. This option is selected by default.
            - JSON - Store data in a standard text-based JSON file format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-s3config.html#cfn-iotfleetwise-campaign-s3config-dataformat
            '''
            result = self._values.get("data_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prefix(self) -> typing.Optional[builtins.str]:
            '''(Optional) Enter an S3 bucket prefix.

            The prefix is the string of characters after the bucket name and before the object name. You can use the prefix to organize data stored in Amazon S3 buckets. For more information, see `Organizing objects using prefixes <https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html>`_ in the *Amazon Simple Storage Service User Guide* .

            By default, AWS IoT FleetWise sets the prefix ``processed-data/year=YY/month=MM/date=DD/hour=HH/`` (in UTC) to data it delivers to Amazon S3 . You can enter a prefix to append it to this default prefix. For example, if you enter the prefix ``vehicles`` , the prefix will be ``vehicles/processed-data/year=YY/month=MM/date=DD/hour=HH/`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-s3config.html#cfn-iotfleetwise-campaign-s3config-prefix
            '''
            result = self._values.get("prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def storage_compression_format(self) -> typing.Optional[builtins.str]:
            '''(Optional) By default, stored data is compressed as a .gzip file. Compressed files have a reduced file size, which can optimize the cost of data storage.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-s3config.html#cfn-iotfleetwise-campaign-s3config-storagecompressionformat
            '''
            result = self._values.get("storage_compression_format")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3ConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnCampaign.SignalInformationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "max_sample_count": "maxSampleCount",
            "minimum_sampling_interval_ms": "minimumSamplingIntervalMs",
        },
    )
    class SignalInformationProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            max_sample_count: typing.Optional[jsii.Number] = None,
            minimum_sampling_interval_ms: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Information about a signal.

            :param name: The name of the signal.
            :param max_sample_count: (Optional) The maximum number of samples to collect.
            :param minimum_sampling_interval_ms: (Optional) The minimum duration of time (in milliseconds) between two triggering events to collect data. .. epigraph:: If a signal changes often, you might want to collect data at a slower rate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-signalinformation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                signal_information_property = iotfleetwise.CfnCampaign.SignalInformationProperty(
                    name="name",
                
                    # the properties below are optional
                    max_sample_count=123,
                    minimum_sampling_interval_ms=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__53d5027f8c4da8a26f3f9cf9e5ab42f41c46c70820c567f2c340ad26784c6997)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument max_sample_count", value=max_sample_count, expected_type=type_hints["max_sample_count"])
                check_type(argname="argument minimum_sampling_interval_ms", value=minimum_sampling_interval_ms, expected_type=type_hints["minimum_sampling_interval_ms"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if max_sample_count is not None:
                self._values["max_sample_count"] = max_sample_count
            if minimum_sampling_interval_ms is not None:
                self._values["minimum_sampling_interval_ms"] = minimum_sampling_interval_ms

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the signal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-signalinformation.html#cfn-iotfleetwise-campaign-signalinformation-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def max_sample_count(self) -> typing.Optional[jsii.Number]:
            '''(Optional) The maximum number of samples to collect.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-signalinformation.html#cfn-iotfleetwise-campaign-signalinformation-maxsamplecount
            '''
            result = self._values.get("max_sample_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def minimum_sampling_interval_ms(self) -> typing.Optional[jsii.Number]:
            '''(Optional) The minimum duration of time (in milliseconds) between two triggering events to collect data.

            .. epigraph::

               If a signal changes often, you might want to collect data at a slower rate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-signalinformation.html#cfn-iotfleetwise-campaign-signalinformation-minimumsamplingintervalms
            '''
            result = self._values.get("minimum_sampling_interval_ms")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SignalInformationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnCampaign.TimeBasedCollectionSchemeProperty",
        jsii_struct_bases=[],
        name_mapping={"period_ms": "periodMs"},
    )
    class TimeBasedCollectionSchemeProperty:
        def __init__(self, *, period_ms: jsii.Number) -> None:
            '''Information about a collection scheme that uses a time period to decide how often to collect data.

            :param period_ms: The time period (in milliseconds) to decide how often to collect data. For example, if the time period is ``60000`` , the Edge Agent software collects data once every minute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-timebasedcollectionscheme.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                time_based_collection_scheme_property = iotfleetwise.CfnCampaign.TimeBasedCollectionSchemeProperty(
                    period_ms=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7bffeabbd9e812e2b77c405369e410069d9bd5d47737b57d4b23d11433d93329)
                check_type(argname="argument period_ms", value=period_ms, expected_type=type_hints["period_ms"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "period_ms": period_ms,
            }

        @builtins.property
        def period_ms(self) -> jsii.Number:
            '''The time period (in milliseconds) to decide how often to collect data.

            For example, if the time period is ``60000`` , the Edge Agent software collects data once every minute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-timebasedcollectionscheme.html#cfn-iotfleetwise-campaign-timebasedcollectionscheme-periodms
            '''
            result = self._values.get("period_ms")
            assert result is not None, "Required property 'period_ms' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimeBasedCollectionSchemeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnCampaign.TimestreamConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "execution_role_arn": "executionRoleArn",
            "timestream_table_arn": "timestreamTableArn",
        },
    )
    class TimestreamConfigProperty:
        def __init__(
            self,
            *,
            execution_role_arn: builtins.str,
            timestream_table_arn: builtins.str,
        ) -> None:
            '''The Amazon Timestream table where the AWS IoT FleetWise campaign sends data.

            Timestream stores and organizes data to optimize query processing time and to reduce storage costs. For more information, see `Data modeling <https://docs.aws.amazon.com/timestream/latest/developerguide/data-modeling.html>`_ in the *Amazon Timestream Developer Guide* .

            :param execution_role_arn: The Amazon Resource Name (ARN) of the task execution role that grants AWS IoT FleetWise permission to deliver data to the Amazon Timestream table.
            :param timestream_table_arn: The Amazon Resource Name (ARN) of the Amazon Timestream table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-timestreamconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                timestream_config_property = iotfleetwise.CfnCampaign.TimestreamConfigProperty(
                    execution_role_arn="executionRoleArn",
                    timestream_table_arn="timestreamTableArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5788ae222c7e21aaed8bd9dbed72cfbc09a7c423d494e8aa4ae9d7a226350700)
                check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
                check_type(argname="argument timestream_table_arn", value=timestream_table_arn, expected_type=type_hints["timestream_table_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "execution_role_arn": execution_role_arn,
                "timestream_table_arn": timestream_table_arn,
            }

        @builtins.property
        def execution_role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the task execution role that grants AWS IoT FleetWise permission to deliver data to the Amazon Timestream table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-timestreamconfig.html#cfn-iotfleetwise-campaign-timestreamconfig-executionrolearn
            '''
            result = self._values.get("execution_role_arn")
            assert result is not None, "Required property 'execution_role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def timestream_table_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Amazon Timestream table.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-campaign-timestreamconfig.html#cfn-iotfleetwise-campaign-timestreamconfig-timestreamtablearn
            '''
            result = self._values.get("timestream_table_arn")
            assert result is not None, "Required property 'timestream_table_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimestreamConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnCampaignProps",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "collection_scheme": "collectionScheme",
        "name": "name",
        "signal_catalog_arn": "signalCatalogArn",
        "target_arn": "targetArn",
        "compression": "compression",
        "data_destination_configs": "dataDestinationConfigs",
        "data_extra_dimensions": "dataExtraDimensions",
        "description": "description",
        "diagnostics_mode": "diagnosticsMode",
        "expiry_time": "expiryTime",
        "post_trigger_collection_duration": "postTriggerCollectionDuration",
        "priority": "priority",
        "signals_to_collect": "signalsToCollect",
        "spooling_mode": "spoolingMode",
        "start_time": "startTime",
        "tags": "tags",
    },
)
class CfnCampaignProps:
    def __init__(
        self,
        *,
        action: builtins.str,
        collection_scheme: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.CollectionSchemeProperty, typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        signal_catalog_arn: builtins.str,
        target_arn: builtins.str,
        compression: typing.Optional[builtins.str] = None,
        data_destination_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.DataDestinationConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        data_extra_dimensions: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        diagnostics_mode: typing.Optional[builtins.str] = None,
        expiry_time: typing.Optional[builtins.str] = None,
        post_trigger_collection_duration: typing.Optional[jsii.Number] = None,
        priority: typing.Optional[jsii.Number] = None,
        signals_to_collect: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.SignalInformationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        spooling_mode: typing.Optional[builtins.str] = None,
        start_time: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCampaign``.

        :param action: Specifies how to update a campaign. The action can be one of the following:. - ``APPROVE`` - To approve delivering a data collection scheme to vehicles. - ``SUSPEND`` - To suspend collecting signal data. The campaign is deleted from vehicles and all vehicles in the suspended campaign will stop sending data. - ``RESUME`` - To reactivate the ``SUSPEND`` campaign. The campaign is redeployed to all vehicles and the vehicles will resume sending data. - ``UPDATE`` - To update a campaign.
        :param collection_scheme: The data collection scheme associated with the campaign. You can specify a scheme that collects data based on time or an event.
        :param name: The name of a campaign.
        :param signal_catalog_arn: The Amazon Resource Name (ARN) of the signal catalog associated with the campaign.
        :param target_arn: The Amazon Resource Name (ARN) of a vehicle or fleet to which the campaign is deployed.
        :param compression: (Optional) Whether to compress signals before transmitting data to AWS IoT FleetWise . If you don't want to compress the signals, use ``OFF`` . If it's not specified, ``SNAPPY`` is used. Default: ``SNAPPY`` Default: - "OFF"
        :param data_destination_configs: (Optional) The destination where the campaign sends data. You can choose to send data to be stored in Amazon S3 or Amazon Timestream . Amazon S3 optimizes the cost of data storage and provides additional mechanisms to use vehicle data, such as data lakes, centralized data storage, data processing pipelines, and analytics. AWS IoT FleetWise supports at-least-once file delivery to S3. Your vehicle data is stored on multiple AWS IoT FleetWise servers for redundancy and high availability. You can use Amazon Timestream to access and analyze time series data, and Timestream to query vehicle data so that you can identify trends and patterns.
        :param data_extra_dimensions: (Optional) A list of vehicle attributes to associate with a campaign. Enrich the data with specified vehicle attributes. For example, add ``make`` and ``model`` to the campaign, and AWS IoT FleetWise will associate the data with those attributes as dimensions in Amazon Timestream . You can then query the data against ``make`` and ``model`` . Default: An empty array
        :param description: (Optional) The description of the campaign.
        :param diagnostics_mode: (Optional) Option for a vehicle to send diagnostic trouble codes to AWS IoT FleetWise . If you want to send diagnostic trouble codes, use ``SEND_ACTIVE_DTCS`` . If it's not specified, ``OFF`` is used. Default: ``OFF`` Default: - "OFF"
        :param expiry_time: (Optional) The time the campaign expires, in seconds since epoch (January 1, 1970 at midnight UTC time). Vehicle data isn't collected after the campaign expires. Default: 253402214400 (December 31, 9999, 00:00:00 UTC) Default: - "253402214400"
        :param post_trigger_collection_duration: (Optional) How long (in milliseconds) to collect raw data after a triggering event initiates the collection. If it's not specified, ``0`` is used. Default: ``0`` Default: - 0
        :param priority: (Optional) A number indicating the priority of one campaign over another campaign for a certain vehicle or fleet. A campaign with the lowest value is deployed to vehicles before any other campaigns. If it's not specified, ``0`` is used. Default: ``0`` Default: - 0
        :param signals_to_collect: (Optional) A list of information about signals to collect.
        :param spooling_mode: (Optional) Whether to store collected data after a vehicle lost a connection with the cloud. After a connection is re-established, the data is automatically forwarded to AWS IoT FleetWise . If you want to store collected data when a vehicle loses connection with the cloud, use ``TO_DISK`` . If it's not specified, ``OFF`` is used. Default: ``OFF`` Default: - "OFF"
        :param start_time: (Optional) The time, in milliseconds, to deliver a campaign after it was approved. If it's not specified, ``0`` is used. Default: ``0`` Default: - "0"
        :param tags: (Optional) Metadata that can be used to manage the campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotfleetwise as iotfleetwise
            
            cfn_campaign_props = iotfleetwise.CfnCampaignProps(
                action="action",
                collection_scheme=iotfleetwise.CfnCampaign.CollectionSchemeProperty(
                    condition_based_collection_scheme=iotfleetwise.CfnCampaign.ConditionBasedCollectionSchemeProperty(
                        expression="expression",
            
                        # the properties below are optional
                        condition_language_version=123,
                        minimum_trigger_interval_ms=123,
                        trigger_mode="triggerMode"
                    ),
                    time_based_collection_scheme=iotfleetwise.CfnCampaign.TimeBasedCollectionSchemeProperty(
                        period_ms=123
                    )
                ),
                name="name",
                signal_catalog_arn="signalCatalogArn",
                target_arn="targetArn",
            
                # the properties below are optional
                compression="compression",
                data_destination_configs=[iotfleetwise.CfnCampaign.DataDestinationConfigProperty(
                    s3_config=iotfleetwise.CfnCampaign.S3ConfigProperty(
                        bucket_arn="bucketArn",
            
                        # the properties below are optional
                        data_format="dataFormat",
                        prefix="prefix",
                        storage_compression_format="storageCompressionFormat"
                    ),
                    timestream_config=iotfleetwise.CfnCampaign.TimestreamConfigProperty(
                        execution_role_arn="executionRoleArn",
                        timestream_table_arn="timestreamTableArn"
                    )
                )],
                data_extra_dimensions=["dataExtraDimensions"],
                description="description",
                diagnostics_mode="diagnosticsMode",
                expiry_time="expiryTime",
                post_trigger_collection_duration=123,
                priority=123,
                signals_to_collect=[iotfleetwise.CfnCampaign.SignalInformationProperty(
                    name="name",
            
                    # the properties below are optional
                    max_sample_count=123,
                    minimum_sampling_interval_ms=123
                )],
                spooling_mode="spoolingMode",
                start_time="startTime",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54c45792d3f0c102d3358acf678401b9616a7fee4b70882083776c5f9635cf71)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument collection_scheme", value=collection_scheme, expected_type=type_hints["collection_scheme"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument signal_catalog_arn", value=signal_catalog_arn, expected_type=type_hints["signal_catalog_arn"])
            check_type(argname="argument target_arn", value=target_arn, expected_type=type_hints["target_arn"])
            check_type(argname="argument compression", value=compression, expected_type=type_hints["compression"])
            check_type(argname="argument data_destination_configs", value=data_destination_configs, expected_type=type_hints["data_destination_configs"])
            check_type(argname="argument data_extra_dimensions", value=data_extra_dimensions, expected_type=type_hints["data_extra_dimensions"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument diagnostics_mode", value=diagnostics_mode, expected_type=type_hints["diagnostics_mode"])
            check_type(argname="argument expiry_time", value=expiry_time, expected_type=type_hints["expiry_time"])
            check_type(argname="argument post_trigger_collection_duration", value=post_trigger_collection_duration, expected_type=type_hints["post_trigger_collection_duration"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument signals_to_collect", value=signals_to_collect, expected_type=type_hints["signals_to_collect"])
            check_type(argname="argument spooling_mode", value=spooling_mode, expected_type=type_hints["spooling_mode"])
            check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "collection_scheme": collection_scheme,
            "name": name,
            "signal_catalog_arn": signal_catalog_arn,
            "target_arn": target_arn,
        }
        if compression is not None:
            self._values["compression"] = compression
        if data_destination_configs is not None:
            self._values["data_destination_configs"] = data_destination_configs
        if data_extra_dimensions is not None:
            self._values["data_extra_dimensions"] = data_extra_dimensions
        if description is not None:
            self._values["description"] = description
        if diagnostics_mode is not None:
            self._values["diagnostics_mode"] = diagnostics_mode
        if expiry_time is not None:
            self._values["expiry_time"] = expiry_time
        if post_trigger_collection_duration is not None:
            self._values["post_trigger_collection_duration"] = post_trigger_collection_duration
        if priority is not None:
            self._values["priority"] = priority
        if signals_to_collect is not None:
            self._values["signals_to_collect"] = signals_to_collect
        if spooling_mode is not None:
            self._values["spooling_mode"] = spooling_mode
        if start_time is not None:
            self._values["start_time"] = start_time
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def action(self) -> builtins.str:
        '''Specifies how to update a campaign. The action can be one of the following:.

        - ``APPROVE`` - To approve delivering a data collection scheme to vehicles.
        - ``SUSPEND`` - To suspend collecting signal data. The campaign is deleted from vehicles and all vehicles in the suspended campaign will stop sending data.
        - ``RESUME`` - To reactivate the ``SUSPEND`` campaign. The campaign is redeployed to all vehicles and the vehicles will resume sending data.
        - ``UPDATE`` - To update a campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-action
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def collection_scheme(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnCampaign.CollectionSchemeProperty]:
        '''The data collection scheme associated with the campaign.

        You can specify a scheme that collects data based on time or an event.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-collectionscheme
        '''
        result = self._values.get("collection_scheme")
        assert result is not None, "Required property 'collection_scheme' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnCampaign.CollectionSchemeProperty], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of a campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signal_catalog_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the signal catalog associated with the campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-signalcatalogarn
        '''
        result = self._values.get("signal_catalog_arn")
        assert result is not None, "Required property 'signal_catalog_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of a vehicle or fleet to which the campaign is deployed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-targetarn
        '''
        result = self._values.get("target_arn")
        assert result is not None, "Required property 'target_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def compression(self) -> typing.Optional[builtins.str]:
        '''(Optional) Whether to compress signals before transmitting data to AWS IoT FleetWise .

        If you don't want to compress the signals, use ``OFF`` . If it's not specified, ``SNAPPY`` is used.

        Default: ``SNAPPY``

        :default: - "OFF"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-compression
        '''
        result = self._values.get("compression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_destination_configs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCampaign.DataDestinationConfigProperty]]]]:
        '''(Optional) The destination where the campaign sends data.

        You can choose to send data to be stored in Amazon S3 or Amazon Timestream .

        Amazon S3 optimizes the cost of data storage and provides additional mechanisms to use vehicle data, such as data lakes, centralized data storage, data processing pipelines, and analytics. AWS IoT FleetWise supports at-least-once file delivery to S3. Your vehicle data is stored on multiple AWS IoT FleetWise servers for redundancy and high availability.

        You can use Amazon Timestream to access and analyze time series data, and Timestream to query vehicle data so that you can identify trends and patterns.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-datadestinationconfigs
        '''
        result = self._values.get("data_destination_configs")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCampaign.DataDestinationConfigProperty]]]], result)

    @builtins.property
    def data_extra_dimensions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(Optional) A list of vehicle attributes to associate with a campaign.

        Enrich the data with specified vehicle attributes. For example, add ``make`` and ``model`` to the campaign, and AWS IoT FleetWise will associate the data with those attributes as dimensions in Amazon Timestream . You can then query the data against ``make`` and ``model`` .

        Default: An empty array

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-dataextradimensions
        '''
        result = self._values.get("data_extra_dimensions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(Optional) The description of the campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def diagnostics_mode(self) -> typing.Optional[builtins.str]:
        '''(Optional) Option for a vehicle to send diagnostic trouble codes to AWS IoT FleetWise .

        If you want to send diagnostic trouble codes, use ``SEND_ACTIVE_DTCS`` . If it's not specified, ``OFF`` is used.

        Default: ``OFF``

        :default: - "OFF"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-diagnosticsmode
        '''
        result = self._values.get("diagnostics_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expiry_time(self) -> typing.Optional[builtins.str]:
        '''(Optional) The time the campaign expires, in seconds since epoch (January 1, 1970 at midnight UTC time).

        Vehicle data isn't collected after the campaign expires.

        Default: 253402214400 (December 31, 9999, 00:00:00 UTC)

        :default: - "253402214400"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-expirytime
        '''
        result = self._values.get("expiry_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def post_trigger_collection_duration(self) -> typing.Optional[jsii.Number]:
        '''(Optional) How long (in milliseconds) to collect raw data after a triggering event initiates the collection.

        If it's not specified, ``0`` is used.

        Default: ``0``

        :default: - 0

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-posttriggercollectionduration
        '''
        result = self._values.get("post_trigger_collection_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''(Optional) A number indicating the priority of one campaign over another campaign for a certain vehicle or fleet.

        A campaign with the lowest value is deployed to vehicles before any other campaigns. If it's not specified, ``0`` is used.

        Default: ``0``

        :default: - 0

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-priority
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def signals_to_collect(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCampaign.SignalInformationProperty]]]]:
        '''(Optional) A list of information about signals to collect.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-signalstocollect
        '''
        result = self._values.get("signals_to_collect")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCampaign.SignalInformationProperty]]]], result)

    @builtins.property
    def spooling_mode(self) -> typing.Optional[builtins.str]:
        '''(Optional) Whether to store collected data after a vehicle lost a connection with the cloud.

        After a connection is re-established, the data is automatically forwarded to AWS IoT FleetWise . If you want to store collected data when a vehicle loses connection with the cloud, use ``TO_DISK`` . If it's not specified, ``OFF`` is used.

        Default: ``OFF``

        :default: - "OFF"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-spoolingmode
        '''
        result = self._values.get("spooling_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_time(self) -> typing.Optional[builtins.str]:
        '''(Optional) The time, in milliseconds, to deliver a campaign after it was approved.

        If it's not specified, ``0`` is used.

        Default: ``0``

        :default: - "0"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-starttime
        '''
        result = self._values.get("start_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''(Optional) Metadata that can be used to manage the campaign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-campaign.html#cfn-iotfleetwise-campaign-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCampaignProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDecoderManifest(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnDecoderManifest",
):
    '''Creates the decoder manifest associated with a model manifest. To create a decoder manifest, the following must be true:.

    - Every signal decoder has a unique name.
    - Each signal decoder is associated with a network interface.
    - Each network interface has a unique ID.
    - The signal decoders are specified in the model manifest.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html
    :cloudformationResource: AWS::IoTFleetWise::DecoderManifest
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotfleetwise as iotfleetwise
        
        cfn_decoder_manifest = iotfleetwise.CfnDecoderManifest(self, "MyCfnDecoderManifest",
            model_manifest_arn="modelManifestArn",
            name="name",
        
            # the properties below are optional
            description="description",
            network_interfaces=[iotfleetwise.CfnDecoderManifest.NetworkInterfacesItemsProperty(
                interface_id="interfaceId",
                type="type",
        
                # the properties below are optional
                can_interface=iotfleetwise.CfnDecoderManifest.CanInterfaceProperty(
                    name="name",
        
                    # the properties below are optional
                    protocol_name="protocolName",
                    protocol_version="protocolVersion"
                ),
                obd_interface=iotfleetwise.CfnDecoderManifest.ObdInterfaceProperty(
                    name="name",
                    request_message_id="requestMessageId",
        
                    # the properties below are optional
                    dtc_request_interval_seconds="dtcRequestIntervalSeconds",
                    has_transmission_ecu="hasTransmissionEcu",
                    obd_standard="obdStandard",
                    pid_request_interval_seconds="pidRequestIntervalSeconds",
                    use_extended_ids="useExtendedIds"
                )
            )],
            signal_decoders=[iotfleetwise.CfnDecoderManifest.SignalDecodersItemsProperty(
                fully_qualified_name="fullyQualifiedName",
                interface_id="interfaceId",
                type="type",
        
                # the properties below are optional
                can_signal=iotfleetwise.CfnDecoderManifest.CanSignalProperty(
                    factor="factor",
                    is_big_endian="isBigEndian",
                    is_signed="isSigned",
                    length="length",
                    message_id="messageId",
                    offset="offset",
                    start_bit="startBit",
        
                    # the properties below are optional
                    name="name"
                ),
                obd_signal=iotfleetwise.CfnDecoderManifest.ObdSignalProperty(
                    byte_length="byteLength",
                    offset="offset",
                    pid="pid",
                    pid_response_length="pidResponseLength",
                    scaling="scaling",
                    service_mode="serviceMode",
                    start_byte="startByte",
        
                    # the properties below are optional
                    bit_mask_length="bitMaskLength",
                    bit_right_shift="bitRightShift"
                )
            )],
            status="status",
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
        model_manifest_arn: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        network_interfaces: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDecoderManifest.NetworkInterfacesItemsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        signal_decoders: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDecoderManifest.SignalDecodersItemsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param model_manifest_arn: The Amazon Resource Name (ARN) of a vehicle model (model manifest) associated with the decoder manifest.
        :param name: The name of the decoder manifest.
        :param description: (Optional) A brief description of the decoder manifest.
        :param network_interfaces: (Optional) A list of information about available network interfaces.
        :param signal_decoders: (Optional) A list of information about signal decoders.
        :param status: (Optional) The state of the decoder manifest. If the status is ``ACTIVE`` , the decoder manifest can't be edited. If the status is marked ``DRAFT`` , you can edit the decoder manifest. Default: - "DRAFT"
        :param tags: (Optional) Metadata that can be used to manage the decoder manifest.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd0d8efce6baca0fa606fb0cf95bebcdeda196fcde2fb7e18542334332eb8ba4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDecoderManifestProps(
            model_manifest_arn=model_manifest_arn,
            name=name,
            description=description,
            network_interfaces=network_interfaces,
            signal_decoders=signal_decoders,
            status=status,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7c1f4e3cc81a06a60eef4d178a3aaf54f7c99cca4a0481a51c50d560d76ba09)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d12e1e0a1684404c74ecc86ed4ae33ffdac8b3611db04d45a6a46ef55c87bbbe)
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
        '''The Amazon Resource Name (ARN) of the decoder manifest.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The time the decoder manifest was created in seconds since epoch (January 1, 1970 at midnight UTC time).

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModificationTime")
    def attr_last_modification_time(self) -> builtins.str:
        '''The time the decoder manifest was last updated in seconds since epoch (January 1, 1970 at midnight UTC time).

        :cloudformationAttribute: LastModificationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModificationTime"))

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
    @jsii.member(jsii_name="modelManifestArn")
    def model_manifest_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of a vehicle model (model manifest) associated with the decoder manifest.'''
        return typing.cast(builtins.str, jsii.get(self, "modelManifestArn"))

    @model_manifest_arn.setter
    def model_manifest_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b8f77dd16bf3c88bd7f097b2327803bb360213ddb0b320722348c6a1b99afce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelManifestArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the decoder manifest.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a5a43cce0da85f8ef5934babccfc93088317c19ae303a38ae3adc573ad6c633)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(Optional) A brief description of the decoder manifest.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1e4501ad7312a6dac9b29817aed239a25a724386677541e036223da190a2d9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="networkInterfaces")
    def network_interfaces(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDecoderManifest.NetworkInterfacesItemsProperty"]]]]:
        '''(Optional) A list of information about available network interfaces.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDecoderManifest.NetworkInterfacesItemsProperty"]]]], jsii.get(self, "networkInterfaces"))

    @network_interfaces.setter
    def network_interfaces(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDecoderManifest.NetworkInterfacesItemsProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4059f7868b58b43acd642cd2537b59a16c939681bb626ef560a6efbc8d7cda5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkInterfaces", value)

    @builtins.property
    @jsii.member(jsii_name="signalDecoders")
    def signal_decoders(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDecoderManifest.SignalDecodersItemsProperty"]]]]:
        '''(Optional) A list of information about signal decoders.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDecoderManifest.SignalDecodersItemsProperty"]]]], jsii.get(self, "signalDecoders"))

    @signal_decoders.setter
    def signal_decoders(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDecoderManifest.SignalDecodersItemsProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32a124503ae0a9be522e3691aef89b61eb023aea0d8b57342dcef4a708073af0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signalDecoders", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''(Optional) The state of the decoder manifest.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8428ef9254e1885dc4fbe7c358202136e77b7b7c68b9e9b92c6016edfca9ad8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''(Optional) Metadata that can be used to manage the decoder manifest.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7589d4cace83e702bf125b3cef9c6977200de03aea448dca5adc0790c282933)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnDecoderManifest.CanInterfaceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "protocol_name": "protocolName",
            "protocol_version": "protocolVersion",
        },
    )
    class CanInterfaceProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            protocol_name: typing.Optional[builtins.str] = None,
            protocol_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A single controller area network (CAN) device interface.

            :param name: The unique name of the interface.
            :param protocol_name: (Optional) The name of the communication protocol for the interface.
            :param protocol_version: (Optional) The version of the communication protocol for the interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-caninterface.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                can_interface_property = iotfleetwise.CfnDecoderManifest.CanInterfaceProperty(
                    name="name",
                
                    # the properties below are optional
                    protocol_name="protocolName",
                    protocol_version="protocolVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f41ef25a35e6c8526ccaa9ecc87becb68ccffe031fd1ae9c650719807164dc68)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument protocol_name", value=protocol_name, expected_type=type_hints["protocol_name"])
                check_type(argname="argument protocol_version", value=protocol_version, expected_type=type_hints["protocol_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if protocol_name is not None:
                self._values["protocol_name"] = protocol_name
            if protocol_version is not None:
                self._values["protocol_version"] = protocol_version

        @builtins.property
        def name(self) -> builtins.str:
            '''The unique name of the interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-caninterface.html#cfn-iotfleetwise-decodermanifest-caninterface-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def protocol_name(self) -> typing.Optional[builtins.str]:
            '''(Optional) The name of the communication protocol for the interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-caninterface.html#cfn-iotfleetwise-decodermanifest-caninterface-protocolname
            '''
            result = self._values.get("protocol_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def protocol_version(self) -> typing.Optional[builtins.str]:
            '''(Optional) The version of the communication protocol for the interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-caninterface.html#cfn-iotfleetwise-decodermanifest-caninterface-protocolversion
            '''
            result = self._values.get("protocol_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CanInterfaceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnDecoderManifest.CanNetworkInterfaceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "can_interface": "canInterface",
            "interface_id": "interfaceId",
            "type": "type",
        },
    )
    class CanNetworkInterfaceProperty:
        def __init__(
            self,
            *,
            can_interface: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDecoderManifest.CanInterfaceProperty", typing.Dict[builtins.str, typing.Any]]],
            interface_id: builtins.str,
            type: builtins.str,
        ) -> None:
            '''Represents a node and its specifications in an in-vehicle communication network.

            All signal decoders must be associated with a network node.

            To return this information about all the network interfaces specified in a decoder manifest, use the `ListDecoderManifestNetworkInterfaces <https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListDecoderManifestNetworkInterfaces.html>`_ in the *AWS IoT FleetWise API Reference* .

            :param can_interface: Information about a network interface specified by the Controller Area Network (CAN) protocol.
            :param interface_id: The ID of the network interface.
            :param type: The network protocol for the vehicle. For example, ``CAN_SIGNAL`` specifies a protocol that defines how data is communicated between electronic control units (ECUs). ``OBD_SIGNAL`` specifies a protocol that defines how self-diagnostic data is communicated between ECUs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cannetworkinterface.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                can_network_interface_property = iotfleetwise.CfnDecoderManifest.CanNetworkInterfaceProperty(
                    can_interface=iotfleetwise.CfnDecoderManifest.CanInterfaceProperty(
                        name="name",
                
                        # the properties below are optional
                        protocol_name="protocolName",
                        protocol_version="protocolVersion"
                    ),
                    interface_id="interfaceId",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b1254441c18c12325ded72e4eeb9b3d36d94b7f5b9ff298529a028d2b2d735a3)
                check_type(argname="argument can_interface", value=can_interface, expected_type=type_hints["can_interface"])
                check_type(argname="argument interface_id", value=interface_id, expected_type=type_hints["interface_id"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "can_interface": can_interface,
                "interface_id": interface_id,
                "type": type,
            }

        @builtins.property
        def can_interface(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDecoderManifest.CanInterfaceProperty"]:
            '''Information about a network interface specified by the Controller Area Network (CAN) protocol.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cannetworkinterface.html#cfn-iotfleetwise-decodermanifest-cannetworkinterface-caninterface
            '''
            result = self._values.get("can_interface")
            assert result is not None, "Required property 'can_interface' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDecoderManifest.CanInterfaceProperty"], result)

        @builtins.property
        def interface_id(self) -> builtins.str:
            '''The ID of the network interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cannetworkinterface.html#cfn-iotfleetwise-decodermanifest-cannetworkinterface-interfaceid
            '''
            result = self._values.get("interface_id")
            assert result is not None, "Required property 'interface_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The network protocol for the vehicle.

            For example, ``CAN_SIGNAL`` specifies a protocol that defines how data is communicated between electronic control units (ECUs). ``OBD_SIGNAL`` specifies a protocol that defines how self-diagnostic data is communicated between ECUs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cannetworkinterface.html#cfn-iotfleetwise-decodermanifest-cannetworkinterface-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CanNetworkInterfaceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnDecoderManifest.CanSignalDecoderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "can_signal": "canSignal",
            "fully_qualified_name": "fullyQualifiedName",
            "interface_id": "interfaceId",
            "type": "type",
        },
    )
    class CanSignalDecoderProperty:
        def __init__(
            self,
            *,
            can_signal: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDecoderManifest.CanSignalProperty", typing.Dict[builtins.str, typing.Any]]],
            fully_qualified_name: builtins.str,
            interface_id: builtins.str,
            type: builtins.str,
        ) -> None:
            '''Information about signal decoder using the Controller Area Network (CAN) protocol.

            :param can_signal: Information about a single controller area network (CAN) signal and the messages it receives and transmits.
            :param fully_qualified_name: The fully qualified name of a signal decoder as defined in a vehicle model.
            :param interface_id: The ID of a network interface that specifies what network protocol a vehicle follows.
            :param type: The network protocol for the vehicle. For example, ``CAN_SIGNAL`` specifies a protocol that defines how data is communicated between electronic control units (ECUs). ``OBD_SIGNAL`` specifies a protocol that defines how self-diagnostic data is communicated between ECUs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignaldecoder.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                can_signal_decoder_property = iotfleetwise.CfnDecoderManifest.CanSignalDecoderProperty(
                    can_signal=iotfleetwise.CfnDecoderManifest.CanSignalProperty(
                        factor="factor",
                        is_big_endian="isBigEndian",
                        is_signed="isSigned",
                        length="length",
                        message_id="messageId",
                        offset="offset",
                        start_bit="startBit",
                
                        # the properties below are optional
                        name="name"
                    ),
                    fully_qualified_name="fullyQualifiedName",
                    interface_id="interfaceId",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a43ee038ead545f634e09871c712c71b73d4a94505498eb010ce592d21e11b3a)
                check_type(argname="argument can_signal", value=can_signal, expected_type=type_hints["can_signal"])
                check_type(argname="argument fully_qualified_name", value=fully_qualified_name, expected_type=type_hints["fully_qualified_name"])
                check_type(argname="argument interface_id", value=interface_id, expected_type=type_hints["interface_id"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "can_signal": can_signal,
                "fully_qualified_name": fully_qualified_name,
                "interface_id": interface_id,
                "type": type,
            }

        @builtins.property
        def can_signal(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDecoderManifest.CanSignalProperty"]:
            '''Information about a single controller area network (CAN) signal and the messages it receives and transmits.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignaldecoder.html#cfn-iotfleetwise-decodermanifest-cansignaldecoder-cansignal
            '''
            result = self._values.get("can_signal")
            assert result is not None, "Required property 'can_signal' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDecoderManifest.CanSignalProperty"], result)

        @builtins.property
        def fully_qualified_name(self) -> builtins.str:
            '''The fully qualified name of a signal decoder as defined in a vehicle model.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignaldecoder.html#cfn-iotfleetwise-decodermanifest-cansignaldecoder-fullyqualifiedname
            '''
            result = self._values.get("fully_qualified_name")
            assert result is not None, "Required property 'fully_qualified_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def interface_id(self) -> builtins.str:
            '''The ID of a network interface that specifies what network protocol a vehicle follows.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignaldecoder.html#cfn-iotfleetwise-decodermanifest-cansignaldecoder-interfaceid
            '''
            result = self._values.get("interface_id")
            assert result is not None, "Required property 'interface_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The network protocol for the vehicle.

            For example, ``CAN_SIGNAL`` specifies a protocol that defines how data is communicated between electronic control units (ECUs). ``OBD_SIGNAL`` specifies a protocol that defines how self-diagnostic data is communicated between ECUs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignaldecoder.html#cfn-iotfleetwise-decodermanifest-cansignaldecoder-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CanSignalDecoderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnDecoderManifest.CanSignalProperty",
        jsii_struct_bases=[],
        name_mapping={
            "factor": "factor",
            "is_big_endian": "isBigEndian",
            "is_signed": "isSigned",
            "length": "length",
            "message_id": "messageId",
            "offset": "offset",
            "start_bit": "startBit",
            "name": "name",
        },
    )
    class CanSignalProperty:
        def __init__(
            self,
            *,
            factor: builtins.str,
            is_big_endian: builtins.str,
            is_signed: builtins.str,
            length: builtins.str,
            message_id: builtins.str,
            offset: builtins.str,
            start_bit: builtins.str,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''(Optional) Information about a single controller area network (CAN) signal and the messages it receives and transmits.

            :param factor: A multiplier used to decode the CAN message.
            :param is_big_endian: Whether the byte ordering of a CAN message is big-endian.
            :param is_signed: Whether the message data is specified as a signed value.
            :param length: How many bytes of data are in the message.
            :param message_id: The ID of the message.
            :param offset: The offset used to calculate the signal value. Combined with factor, the calculation is ``value = raw_value * factor + offset`` .
            :param start_bit: Indicates the beginning of the CAN message.
            :param name: (Optional) The name of the signal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                can_signal_property = iotfleetwise.CfnDecoderManifest.CanSignalProperty(
                    factor="factor",
                    is_big_endian="isBigEndian",
                    is_signed="isSigned",
                    length="length",
                    message_id="messageId",
                    offset="offset",
                    start_bit="startBit",
                
                    # the properties below are optional
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d1fdd86137a92797754860d3b8da115496d862a2f95c8e39c08a70fdf76855c4)
                check_type(argname="argument factor", value=factor, expected_type=type_hints["factor"])
                check_type(argname="argument is_big_endian", value=is_big_endian, expected_type=type_hints["is_big_endian"])
                check_type(argname="argument is_signed", value=is_signed, expected_type=type_hints["is_signed"])
                check_type(argname="argument length", value=length, expected_type=type_hints["length"])
                check_type(argname="argument message_id", value=message_id, expected_type=type_hints["message_id"])
                check_type(argname="argument offset", value=offset, expected_type=type_hints["offset"])
                check_type(argname="argument start_bit", value=start_bit, expected_type=type_hints["start_bit"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "factor": factor,
                "is_big_endian": is_big_endian,
                "is_signed": is_signed,
                "length": length,
                "message_id": message_id,
                "offset": offset,
                "start_bit": start_bit,
            }
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def factor(self) -> builtins.str:
            '''A multiplier used to decode the CAN message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-factor
            '''
            result = self._values.get("factor")
            assert result is not None, "Required property 'factor' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def is_big_endian(self) -> builtins.str:
            '''Whether the byte ordering of a CAN message is big-endian.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-isbigendian
            '''
            result = self._values.get("is_big_endian")
            assert result is not None, "Required property 'is_big_endian' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def is_signed(self) -> builtins.str:
            '''Whether the message data is specified as a signed value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-issigned
            '''
            result = self._values.get("is_signed")
            assert result is not None, "Required property 'is_signed' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def length(self) -> builtins.str:
            '''How many bytes of data are in the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-length
            '''
            result = self._values.get("length")
            assert result is not None, "Required property 'length' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def message_id(self) -> builtins.str:
            '''The ID of the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-messageid
            '''
            result = self._values.get("message_id")
            assert result is not None, "Required property 'message_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def offset(self) -> builtins.str:
            '''The offset used to calculate the signal value.

            Combined with factor, the calculation is ``value = raw_value * factor + offset`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-offset
            '''
            result = self._values.get("offset")
            assert result is not None, "Required property 'offset' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def start_bit(self) -> builtins.str:
            '''Indicates the beginning of the CAN message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-startbit
            '''
            result = self._values.get("start_bit")
            assert result is not None, "Required property 'start_bit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''(Optional) The name of the signal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-cansignal.html#cfn-iotfleetwise-decodermanifest-cansignal-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CanSignalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnDecoderManifest.NetworkInterfacesItemsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "interface_id": "interfaceId",
            "type": "type",
            "can_interface": "canInterface",
            "obd_interface": "obdInterface",
        },
    )
    class NetworkInterfacesItemsProperty:
        def __init__(
            self,
            *,
            interface_id: builtins.str,
            type: builtins.str,
            can_interface: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDecoderManifest.CanInterfaceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            obd_interface: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDecoderManifest.ObdInterfaceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''(Optional) A list of information about available network interfaces.

            :param interface_id: 
            :param type: 
            :param can_interface: 
            :param obd_interface: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-networkinterfacesitems.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                network_interfaces_items_property = iotfleetwise.CfnDecoderManifest.NetworkInterfacesItemsProperty(
                    interface_id="interfaceId",
                    type="type",
                
                    # the properties below are optional
                    can_interface=iotfleetwise.CfnDecoderManifest.CanInterfaceProperty(
                        name="name",
                
                        # the properties below are optional
                        protocol_name="protocolName",
                        protocol_version="protocolVersion"
                    ),
                    obd_interface=iotfleetwise.CfnDecoderManifest.ObdInterfaceProperty(
                        name="name",
                        request_message_id="requestMessageId",
                
                        # the properties below are optional
                        dtc_request_interval_seconds="dtcRequestIntervalSeconds",
                        has_transmission_ecu="hasTransmissionEcu",
                        obd_standard="obdStandard",
                        pid_request_interval_seconds="pidRequestIntervalSeconds",
                        use_extended_ids="useExtendedIds"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__763a8a9c006b5f64d4a07d45a9f83b3a4b0be692630292c6e33fd7f6c09a4c07)
                check_type(argname="argument interface_id", value=interface_id, expected_type=type_hints["interface_id"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument can_interface", value=can_interface, expected_type=type_hints["can_interface"])
                check_type(argname="argument obd_interface", value=obd_interface, expected_type=type_hints["obd_interface"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "interface_id": interface_id,
                "type": type,
            }
            if can_interface is not None:
                self._values["can_interface"] = can_interface
            if obd_interface is not None:
                self._values["obd_interface"] = obd_interface

        @builtins.property
        def interface_id(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-networkinterfacesitems.html#cfn-iotfleetwise-decodermanifest-networkinterfacesitems-interfaceid
            '''
            result = self._values.get("interface_id")
            assert result is not None, "Required property 'interface_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-networkinterfacesitems.html#cfn-iotfleetwise-decodermanifest-networkinterfacesitems-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def can_interface(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDecoderManifest.CanInterfaceProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-networkinterfacesitems.html#cfn-iotfleetwise-decodermanifest-networkinterfacesitems-caninterface
            '''
            result = self._values.get("can_interface")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDecoderManifest.CanInterfaceProperty"]], result)

        @builtins.property
        def obd_interface(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDecoderManifest.ObdInterfaceProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-networkinterfacesitems.html#cfn-iotfleetwise-decodermanifest-networkinterfacesitems-obdinterface
            '''
            result = self._values.get("obd_interface")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDecoderManifest.ObdInterfaceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkInterfacesItemsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnDecoderManifest.ObdInterfaceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "request_message_id": "requestMessageId",
            "dtc_request_interval_seconds": "dtcRequestIntervalSeconds",
            "has_transmission_ecu": "hasTransmissionEcu",
            "obd_standard": "obdStandard",
            "pid_request_interval_seconds": "pidRequestIntervalSeconds",
            "use_extended_ids": "useExtendedIds",
        },
    )
    class ObdInterfaceProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            request_message_id: builtins.str,
            dtc_request_interval_seconds: typing.Optional[builtins.str] = None,
            has_transmission_ecu: typing.Optional[builtins.str] = None,
            obd_standard: typing.Optional[builtins.str] = None,
            pid_request_interval_seconds: typing.Optional[builtins.str] = None,
            use_extended_ids: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A network interface that specifies the On-board diagnostic (OBD) II network protocol.

            :param name: The name of the interface.
            :param request_message_id: The ID of the message requesting vehicle data.
            :param dtc_request_interval_seconds: (Optional) The maximum number message requests per diagnostic trouble code per second.
            :param has_transmission_ecu: (Optional) Whether the vehicle has a transmission control module (TCM).
            :param obd_standard: (Optional) The standard OBD II PID.
            :param pid_request_interval_seconds: (Optional) The maximum number message requests per second.
            :param use_extended_ids: (Optional) Whether to use extended IDs in the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                obd_interface_property = iotfleetwise.CfnDecoderManifest.ObdInterfaceProperty(
                    name="name",
                    request_message_id="requestMessageId",
                
                    # the properties below are optional
                    dtc_request_interval_seconds="dtcRequestIntervalSeconds",
                    has_transmission_ecu="hasTransmissionEcu",
                    obd_standard="obdStandard",
                    pid_request_interval_seconds="pidRequestIntervalSeconds",
                    use_extended_ids="useExtendedIds"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__619deb4a5a81c6ae8bcb58cd0d96a9beddd6b7ac867f4e945e1bd4668fc25b17)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument request_message_id", value=request_message_id, expected_type=type_hints["request_message_id"])
                check_type(argname="argument dtc_request_interval_seconds", value=dtc_request_interval_seconds, expected_type=type_hints["dtc_request_interval_seconds"])
                check_type(argname="argument has_transmission_ecu", value=has_transmission_ecu, expected_type=type_hints["has_transmission_ecu"])
                check_type(argname="argument obd_standard", value=obd_standard, expected_type=type_hints["obd_standard"])
                check_type(argname="argument pid_request_interval_seconds", value=pid_request_interval_seconds, expected_type=type_hints["pid_request_interval_seconds"])
                check_type(argname="argument use_extended_ids", value=use_extended_ids, expected_type=type_hints["use_extended_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "request_message_id": request_message_id,
            }
            if dtc_request_interval_seconds is not None:
                self._values["dtc_request_interval_seconds"] = dtc_request_interval_seconds
            if has_transmission_ecu is not None:
                self._values["has_transmission_ecu"] = has_transmission_ecu
            if obd_standard is not None:
                self._values["obd_standard"] = obd_standard
            if pid_request_interval_seconds is not None:
                self._values["pid_request_interval_seconds"] = pid_request_interval_seconds
            if use_extended_ids is not None:
                self._values["use_extended_ids"] = use_extended_ids

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def request_message_id(self) -> builtins.str:
            '''The ID of the message requesting vehicle data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-requestmessageid
            '''
            result = self._values.get("request_message_id")
            assert result is not None, "Required property 'request_message_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dtc_request_interval_seconds(self) -> typing.Optional[builtins.str]:
            '''(Optional) The maximum number message requests per diagnostic trouble code per second.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-dtcrequestintervalseconds
            '''
            result = self._values.get("dtc_request_interval_seconds")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def has_transmission_ecu(self) -> typing.Optional[builtins.str]:
            '''(Optional) Whether the vehicle has a transmission control module (TCM).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-hastransmissionecu
            '''
            result = self._values.get("has_transmission_ecu")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def obd_standard(self) -> typing.Optional[builtins.str]:
            '''(Optional) The standard OBD II PID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-obdstandard
            '''
            result = self._values.get("obd_standard")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def pid_request_interval_seconds(self) -> typing.Optional[builtins.str]:
            '''(Optional) The maximum number message requests per second.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-pidrequestintervalseconds
            '''
            result = self._values.get("pid_request_interval_seconds")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def use_extended_ids(self) -> typing.Optional[builtins.str]:
            '''(Optional) Whether to use extended IDs in the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdinterface.html#cfn-iotfleetwise-decodermanifest-obdinterface-useextendedids
            '''
            result = self._values.get("use_extended_ids")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ObdInterfaceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnDecoderManifest.ObdNetworkInterfaceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "interface_id": "interfaceId",
            "obd_interface": "obdInterface",
            "type": "type",
        },
    )
    class ObdNetworkInterfaceProperty:
        def __init__(
            self,
            *,
            interface_id: builtins.str,
            obd_interface: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDecoderManifest.ObdInterfaceProperty", typing.Dict[builtins.str, typing.Any]]],
            type: builtins.str,
        ) -> None:
            '''Information about a network interface specified by the On-board diagnostic (OBD) II protocol.

            :param interface_id: The ID of the network interface.
            :param obd_interface: (Optional) Information about a network interface specified by the On-board diagnostic (OBD) II protocol.
            :param type: The network protocol for the vehicle. For example, ``CAN_SIGNAL`` specifies a protocol that defines how data is communicated between electronic control units (ECUs). ``OBD_SIGNAL`` specifies a protocol that defines how self-diagnostic data is communicated between ECUs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdnetworkinterface.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                obd_network_interface_property = iotfleetwise.CfnDecoderManifest.ObdNetworkInterfaceProperty(
                    interface_id="interfaceId",
                    obd_interface=iotfleetwise.CfnDecoderManifest.ObdInterfaceProperty(
                        name="name",
                        request_message_id="requestMessageId",
                
                        # the properties below are optional
                        dtc_request_interval_seconds="dtcRequestIntervalSeconds",
                        has_transmission_ecu="hasTransmissionEcu",
                        obd_standard="obdStandard",
                        pid_request_interval_seconds="pidRequestIntervalSeconds",
                        use_extended_ids="useExtendedIds"
                    ),
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c45c63503d1f718c56dd74e773036e65da8f350e05d1468a20136ad9ee6cfaf7)
                check_type(argname="argument interface_id", value=interface_id, expected_type=type_hints["interface_id"])
                check_type(argname="argument obd_interface", value=obd_interface, expected_type=type_hints["obd_interface"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "interface_id": interface_id,
                "obd_interface": obd_interface,
                "type": type,
            }

        @builtins.property
        def interface_id(self) -> builtins.str:
            '''The ID of the network interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdnetworkinterface.html#cfn-iotfleetwise-decodermanifest-obdnetworkinterface-interfaceid
            '''
            result = self._values.get("interface_id")
            assert result is not None, "Required property 'interface_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def obd_interface(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDecoderManifest.ObdInterfaceProperty"]:
            '''(Optional) Information about a network interface specified by the On-board diagnostic (OBD) II protocol.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdnetworkinterface.html#cfn-iotfleetwise-decodermanifest-obdnetworkinterface-obdinterface
            '''
            result = self._values.get("obd_interface")
            assert result is not None, "Required property 'obd_interface' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDecoderManifest.ObdInterfaceProperty"], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The network protocol for the vehicle.

            For example, ``CAN_SIGNAL`` specifies a protocol that defines how data is communicated between electronic control units (ECUs). ``OBD_SIGNAL`` specifies a protocol that defines how self-diagnostic data is communicated between ECUs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdnetworkinterface.html#cfn-iotfleetwise-decodermanifest-obdnetworkinterface-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ObdNetworkInterfaceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnDecoderManifest.ObdSignalDecoderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "fully_qualified_name": "fullyQualifiedName",
            "interface_id": "interfaceId",
            "obd_signal": "obdSignal",
            "type": "type",
        },
    )
    class ObdSignalDecoderProperty:
        def __init__(
            self,
            *,
            fully_qualified_name: builtins.str,
            interface_id: builtins.str,
            obd_signal: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDecoderManifest.ObdSignalProperty", typing.Dict[builtins.str, typing.Any]]],
            type: builtins.str,
        ) -> None:
            '''A list of information about signal decoders.

            :param fully_qualified_name: 
            :param interface_id: 
            :param obd_signal: Information about signal messages using the on-board diagnostics (OBD) II protocol in a vehicle.
            :param type: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignaldecoder.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                obd_signal_decoder_property = iotfleetwise.CfnDecoderManifest.ObdSignalDecoderProperty(
                    fully_qualified_name="fullyQualifiedName",
                    interface_id="interfaceId",
                    obd_signal=iotfleetwise.CfnDecoderManifest.ObdSignalProperty(
                        byte_length="byteLength",
                        offset="offset",
                        pid="pid",
                        pid_response_length="pidResponseLength",
                        scaling="scaling",
                        service_mode="serviceMode",
                        start_byte="startByte",
                
                        # the properties below are optional
                        bit_mask_length="bitMaskLength",
                        bit_right_shift="bitRightShift"
                    ),
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5b66ad96f7c649fd06e9447c0e2e4b23db06a0053d635376375d3d5fcf7fc8e7)
                check_type(argname="argument fully_qualified_name", value=fully_qualified_name, expected_type=type_hints["fully_qualified_name"])
                check_type(argname="argument interface_id", value=interface_id, expected_type=type_hints["interface_id"])
                check_type(argname="argument obd_signal", value=obd_signal, expected_type=type_hints["obd_signal"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "fully_qualified_name": fully_qualified_name,
                "interface_id": interface_id,
                "obd_signal": obd_signal,
                "type": type,
            }

        @builtins.property
        def fully_qualified_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignaldecoder.html#cfn-iotfleetwise-decodermanifest-obdsignaldecoder-fullyqualifiedname
            '''
            result = self._values.get("fully_qualified_name")
            assert result is not None, "Required property 'fully_qualified_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def interface_id(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignaldecoder.html#cfn-iotfleetwise-decodermanifest-obdsignaldecoder-interfaceid
            '''
            result = self._values.get("interface_id")
            assert result is not None, "Required property 'interface_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def obd_signal(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDecoderManifest.ObdSignalProperty"]:
            '''Information about signal messages using the on-board diagnostics (OBD) II protocol in a vehicle.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignaldecoder.html#cfn-iotfleetwise-decodermanifest-obdsignaldecoder-obdsignal
            '''
            result = self._values.get("obd_signal")
            assert result is not None, "Required property 'obd_signal' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDecoderManifest.ObdSignalProperty"], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignaldecoder.html#cfn-iotfleetwise-decodermanifest-obdsignaldecoder-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ObdSignalDecoderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnDecoderManifest.ObdSignalProperty",
        jsii_struct_bases=[],
        name_mapping={
            "byte_length": "byteLength",
            "offset": "offset",
            "pid": "pid",
            "pid_response_length": "pidResponseLength",
            "scaling": "scaling",
            "service_mode": "serviceMode",
            "start_byte": "startByte",
            "bit_mask_length": "bitMaskLength",
            "bit_right_shift": "bitRightShift",
        },
    )
    class ObdSignalProperty:
        def __init__(
            self,
            *,
            byte_length: builtins.str,
            offset: builtins.str,
            pid: builtins.str,
            pid_response_length: builtins.str,
            scaling: builtins.str,
            service_mode: builtins.str,
            start_byte: builtins.str,
            bit_mask_length: typing.Optional[builtins.str] = None,
            bit_right_shift: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about signal messages using the on-board diagnostics (OBD) II protocol in a vehicle.

            :param byte_length: The length of a message.
            :param offset: The offset used to calculate the signal value. Combined with scaling, the calculation is ``value = raw_value * scaling + offset`` .
            :param pid: The diagnostic code used to request data from a vehicle for this signal.
            :param pid_response_length: The length of the requested data.
            :param scaling: A multiplier used to decode the message.
            :param service_mode: The mode of operation (diagnostic service) in a message.
            :param start_byte: Indicates the beginning of the message.
            :param bit_mask_length: (Optional) The number of bits to mask in a message.
            :param bit_right_shift: (Optional) The number of positions to shift bits in the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                obd_signal_property = iotfleetwise.CfnDecoderManifest.ObdSignalProperty(
                    byte_length="byteLength",
                    offset="offset",
                    pid="pid",
                    pid_response_length="pidResponseLength",
                    scaling="scaling",
                    service_mode="serviceMode",
                    start_byte="startByte",
                
                    # the properties below are optional
                    bit_mask_length="bitMaskLength",
                    bit_right_shift="bitRightShift"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ccb776ce607aa563ef4bc105956ab186267e45066ee492c162a4555709004e4b)
                check_type(argname="argument byte_length", value=byte_length, expected_type=type_hints["byte_length"])
                check_type(argname="argument offset", value=offset, expected_type=type_hints["offset"])
                check_type(argname="argument pid", value=pid, expected_type=type_hints["pid"])
                check_type(argname="argument pid_response_length", value=pid_response_length, expected_type=type_hints["pid_response_length"])
                check_type(argname="argument scaling", value=scaling, expected_type=type_hints["scaling"])
                check_type(argname="argument service_mode", value=service_mode, expected_type=type_hints["service_mode"])
                check_type(argname="argument start_byte", value=start_byte, expected_type=type_hints["start_byte"])
                check_type(argname="argument bit_mask_length", value=bit_mask_length, expected_type=type_hints["bit_mask_length"])
                check_type(argname="argument bit_right_shift", value=bit_right_shift, expected_type=type_hints["bit_right_shift"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "byte_length": byte_length,
                "offset": offset,
                "pid": pid,
                "pid_response_length": pid_response_length,
                "scaling": scaling,
                "service_mode": service_mode,
                "start_byte": start_byte,
            }
            if bit_mask_length is not None:
                self._values["bit_mask_length"] = bit_mask_length
            if bit_right_shift is not None:
                self._values["bit_right_shift"] = bit_right_shift

        @builtins.property
        def byte_length(self) -> builtins.str:
            '''The length of a message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-bytelength
            '''
            result = self._values.get("byte_length")
            assert result is not None, "Required property 'byte_length' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def offset(self) -> builtins.str:
            '''The offset used to calculate the signal value.

            Combined with scaling, the calculation is ``value = raw_value * scaling + offset`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-offset
            '''
            result = self._values.get("offset")
            assert result is not None, "Required property 'offset' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def pid(self) -> builtins.str:
            '''The diagnostic code used to request data from a vehicle for this signal.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-pid
            '''
            result = self._values.get("pid")
            assert result is not None, "Required property 'pid' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def pid_response_length(self) -> builtins.str:
            '''The length of the requested data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-pidresponselength
            '''
            result = self._values.get("pid_response_length")
            assert result is not None, "Required property 'pid_response_length' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def scaling(self) -> builtins.str:
            '''A multiplier used to decode the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-scaling
            '''
            result = self._values.get("scaling")
            assert result is not None, "Required property 'scaling' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def service_mode(self) -> builtins.str:
            '''The mode of operation (diagnostic service) in a message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-servicemode
            '''
            result = self._values.get("service_mode")
            assert result is not None, "Required property 'service_mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def start_byte(self) -> builtins.str:
            '''Indicates the beginning of the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-startbyte
            '''
            result = self._values.get("start_byte")
            assert result is not None, "Required property 'start_byte' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bit_mask_length(self) -> typing.Optional[builtins.str]:
            '''(Optional) The number of bits to mask in a message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-bitmasklength
            '''
            result = self._values.get("bit_mask_length")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bit_right_shift(self) -> typing.Optional[builtins.str]:
            '''(Optional) The number of positions to shift bits in the message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-obdsignal.html#cfn-iotfleetwise-decodermanifest-obdsignal-bitrightshift
            '''
            result = self._values.get("bit_right_shift")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ObdSignalProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnDecoderManifest.SignalDecodersItemsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "fully_qualified_name": "fullyQualifiedName",
            "interface_id": "interfaceId",
            "type": "type",
            "can_signal": "canSignal",
            "obd_signal": "obdSignal",
        },
    )
    class SignalDecodersItemsProperty:
        def __init__(
            self,
            *,
            fully_qualified_name: builtins.str,
            interface_id: builtins.str,
            type: builtins.str,
            can_signal: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDecoderManifest.CanSignalProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            obd_signal: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDecoderManifest.ObdSignalProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Information about a signal decoder.

            :param fully_qualified_name: 
            :param interface_id: 
            :param type: 
            :param can_signal: 
            :param obd_signal: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-signaldecodersitems.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                signal_decoders_items_property = iotfleetwise.CfnDecoderManifest.SignalDecodersItemsProperty(
                    fully_qualified_name="fullyQualifiedName",
                    interface_id="interfaceId",
                    type="type",
                
                    # the properties below are optional
                    can_signal=iotfleetwise.CfnDecoderManifest.CanSignalProperty(
                        factor="factor",
                        is_big_endian="isBigEndian",
                        is_signed="isSigned",
                        length="length",
                        message_id="messageId",
                        offset="offset",
                        start_bit="startBit",
                
                        # the properties below are optional
                        name="name"
                    ),
                    obd_signal=iotfleetwise.CfnDecoderManifest.ObdSignalProperty(
                        byte_length="byteLength",
                        offset="offset",
                        pid="pid",
                        pid_response_length="pidResponseLength",
                        scaling="scaling",
                        service_mode="serviceMode",
                        start_byte="startByte",
                
                        # the properties below are optional
                        bit_mask_length="bitMaskLength",
                        bit_right_shift="bitRightShift"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5832121c7c16050419993147c157e7f5739fca1dc1afba25d1f52da2d4bd75fb)
                check_type(argname="argument fully_qualified_name", value=fully_qualified_name, expected_type=type_hints["fully_qualified_name"])
                check_type(argname="argument interface_id", value=interface_id, expected_type=type_hints["interface_id"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument can_signal", value=can_signal, expected_type=type_hints["can_signal"])
                check_type(argname="argument obd_signal", value=obd_signal, expected_type=type_hints["obd_signal"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "fully_qualified_name": fully_qualified_name,
                "interface_id": interface_id,
                "type": type,
            }
            if can_signal is not None:
                self._values["can_signal"] = can_signal
            if obd_signal is not None:
                self._values["obd_signal"] = obd_signal

        @builtins.property
        def fully_qualified_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-signaldecodersitems.html#cfn-iotfleetwise-decodermanifest-signaldecodersitems-fullyqualifiedname
            '''
            result = self._values.get("fully_qualified_name")
            assert result is not None, "Required property 'fully_qualified_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def interface_id(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-signaldecodersitems.html#cfn-iotfleetwise-decodermanifest-signaldecodersitems-interfaceid
            '''
            result = self._values.get("interface_id")
            assert result is not None, "Required property 'interface_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-signaldecodersitems.html#cfn-iotfleetwise-decodermanifest-signaldecodersitems-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def can_signal(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDecoderManifest.CanSignalProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-signaldecodersitems.html#cfn-iotfleetwise-decodermanifest-signaldecodersitems-cansignal
            '''
            result = self._values.get("can_signal")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDecoderManifest.CanSignalProperty"]], result)

        @builtins.property
        def obd_signal(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDecoderManifest.ObdSignalProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-decodermanifest-signaldecodersitems.html#cfn-iotfleetwise-decodermanifest-signaldecodersitems-obdsignal
            '''
            result = self._values.get("obd_signal")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDecoderManifest.ObdSignalProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SignalDecodersItemsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnDecoderManifestProps",
    jsii_struct_bases=[],
    name_mapping={
        "model_manifest_arn": "modelManifestArn",
        "name": "name",
        "description": "description",
        "network_interfaces": "networkInterfaces",
        "signal_decoders": "signalDecoders",
        "status": "status",
        "tags": "tags",
    },
)
class CfnDecoderManifestProps:
    def __init__(
        self,
        *,
        model_manifest_arn: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        network_interfaces: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDecoderManifest.NetworkInterfacesItemsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        signal_decoders: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDecoderManifest.SignalDecodersItemsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDecoderManifest``.

        :param model_manifest_arn: The Amazon Resource Name (ARN) of a vehicle model (model manifest) associated with the decoder manifest.
        :param name: The name of the decoder manifest.
        :param description: (Optional) A brief description of the decoder manifest.
        :param network_interfaces: (Optional) A list of information about available network interfaces.
        :param signal_decoders: (Optional) A list of information about signal decoders.
        :param status: (Optional) The state of the decoder manifest. If the status is ``ACTIVE`` , the decoder manifest can't be edited. If the status is marked ``DRAFT`` , you can edit the decoder manifest. Default: - "DRAFT"
        :param tags: (Optional) Metadata that can be used to manage the decoder manifest.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotfleetwise as iotfleetwise
            
            cfn_decoder_manifest_props = iotfleetwise.CfnDecoderManifestProps(
                model_manifest_arn="modelManifestArn",
                name="name",
            
                # the properties below are optional
                description="description",
                network_interfaces=[iotfleetwise.CfnDecoderManifest.NetworkInterfacesItemsProperty(
                    interface_id="interfaceId",
                    type="type",
            
                    # the properties below are optional
                    can_interface=iotfleetwise.CfnDecoderManifest.CanInterfaceProperty(
                        name="name",
            
                        # the properties below are optional
                        protocol_name="protocolName",
                        protocol_version="protocolVersion"
                    ),
                    obd_interface=iotfleetwise.CfnDecoderManifest.ObdInterfaceProperty(
                        name="name",
                        request_message_id="requestMessageId",
            
                        # the properties below are optional
                        dtc_request_interval_seconds="dtcRequestIntervalSeconds",
                        has_transmission_ecu="hasTransmissionEcu",
                        obd_standard="obdStandard",
                        pid_request_interval_seconds="pidRequestIntervalSeconds",
                        use_extended_ids="useExtendedIds"
                    )
                )],
                signal_decoders=[iotfleetwise.CfnDecoderManifest.SignalDecodersItemsProperty(
                    fully_qualified_name="fullyQualifiedName",
                    interface_id="interfaceId",
                    type="type",
            
                    # the properties below are optional
                    can_signal=iotfleetwise.CfnDecoderManifest.CanSignalProperty(
                        factor="factor",
                        is_big_endian="isBigEndian",
                        is_signed="isSigned",
                        length="length",
                        message_id="messageId",
                        offset="offset",
                        start_bit="startBit",
            
                        # the properties below are optional
                        name="name"
                    ),
                    obd_signal=iotfleetwise.CfnDecoderManifest.ObdSignalProperty(
                        byte_length="byteLength",
                        offset="offset",
                        pid="pid",
                        pid_response_length="pidResponseLength",
                        scaling="scaling",
                        service_mode="serviceMode",
                        start_byte="startByte",
            
                        # the properties below are optional
                        bit_mask_length="bitMaskLength",
                        bit_right_shift="bitRightShift"
                    )
                )],
                status="status",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1be5cfb3ca0441a2fdb0856303c08c4449592f7472588f5c0659c42af4d89e2c)
            check_type(argname="argument model_manifest_arn", value=model_manifest_arn, expected_type=type_hints["model_manifest_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument network_interfaces", value=network_interfaces, expected_type=type_hints["network_interfaces"])
            check_type(argname="argument signal_decoders", value=signal_decoders, expected_type=type_hints["signal_decoders"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "model_manifest_arn": model_manifest_arn,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if network_interfaces is not None:
            self._values["network_interfaces"] = network_interfaces
        if signal_decoders is not None:
            self._values["signal_decoders"] = signal_decoders
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def model_manifest_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of a vehicle model (model manifest) associated with the decoder manifest.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-modelmanifestarn
        '''
        result = self._values.get("model_manifest_arn")
        assert result is not None, "Required property 'model_manifest_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the decoder manifest.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(Optional) A brief description of the decoder manifest.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_interfaces(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDecoderManifest.NetworkInterfacesItemsProperty]]]]:
        '''(Optional) A list of information about available network interfaces.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-networkinterfaces
        '''
        result = self._values.get("network_interfaces")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDecoderManifest.NetworkInterfacesItemsProperty]]]], result)

    @builtins.property
    def signal_decoders(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDecoderManifest.SignalDecodersItemsProperty]]]]:
        '''(Optional) A list of information about signal decoders.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-signaldecoders
        '''
        result = self._values.get("signal_decoders")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDecoderManifest.SignalDecodersItemsProperty]]]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''(Optional) The state of the decoder manifest.

        If the status is ``ACTIVE`` , the decoder manifest can't be edited. If the status is marked ``DRAFT`` , you can edit the decoder manifest.

        :default: - "DRAFT"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''(Optional) Metadata that can be used to manage the decoder manifest.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-decodermanifest.html#cfn-iotfleetwise-decodermanifest-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDecoderManifestProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnFleet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnFleet",
):
    '''Creates a fleet that represents a group of vehicles.

    .. epigraph::

       You must create both a signal catalog and vehicles before you can create a fleet.

    For more information, see `Fleets <https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleets.html>`_ in the *AWS IoT FleetWise Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html
    :cloudformationResource: AWS::IoTFleetWise::Fleet
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotfleetwise as iotfleetwise
        
        cfn_fleet = iotfleetwise.CfnFleet(self, "MyCfnFleet",
            id="id",
            signal_catalog_arn="signalCatalogArn",
        
            # the properties below are optional
            description="description",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        id: builtins.str,
        signal_catalog_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id_: Construct identifier for this resource (unique in its scope).
        :param id: The unique ID of the fleet.
        :param signal_catalog_arn: The ARN of the signal catalog associated with the fleet.
        :param description: (Optional) A brief description of the fleet.
        :param tags: (Optional) Metadata that can be used to manage the fleet.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be2399a288ba3f0fe4eba6c31d42082d31eac165febede18736a759d92f2120d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        props = CfnFleetProps(
            id=id,
            signal_catalog_arn=signal_catalog_arn,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id_, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b66a25ffe3875464ec35ff63e6d6335f63f5bd966c356414cfa0ec840225eedd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__19ef6ad0585e294dae29b4c919f9fbf11b89c72deadd5a5cda8a56f1433235a8)
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
        '''The Amazon Resource Name (ARN) of the created fleet.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The time the fleet was created in seconds since epoch (January 1, 1970 at midnight UTC time).

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModificationTime")
    def attr_last_modification_time(self) -> builtins.str:
        '''The time the fleet was last updated, in seconds since epoch (January 1, 1970 at midnight UTC time).

        :cloudformationAttribute: LastModificationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModificationTime"))

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
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''The unique ID of the fleet.'''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__521c3cdc3b4991a92beb684d8c8af88ceab73dcbd34d08d120663c9c7f94d059)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="signalCatalogArn")
    def signal_catalog_arn(self) -> builtins.str:
        '''The ARN of the signal catalog associated with the fleet.'''
        return typing.cast(builtins.str, jsii.get(self, "signalCatalogArn"))

    @signal_catalog_arn.setter
    def signal_catalog_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eec1aed040f26806fdbfee937ccf8c8b0ccb036bc460096cfbb5b04da65cccca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signalCatalogArn", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(Optional) A brief description of the fleet.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47625bcd41335399a9f769fa64574c2375f2937ed4511d09a3984dbd0abef447)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''(Optional) Metadata that can be used to manage the fleet.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b778328780cd48e8666cfdebbdaa84f93e4dd8ae56fc24f3ac40fb8baa31791)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnFleetProps",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "signal_catalog_arn": "signalCatalogArn",
        "description": "description",
        "tags": "tags",
    },
)
class CfnFleetProps:
    def __init__(
        self,
        *,
        id: builtins.str,
        signal_catalog_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFleet``.

        :param id: The unique ID of the fleet.
        :param signal_catalog_arn: The ARN of the signal catalog associated with the fleet.
        :param description: (Optional) A brief description of the fleet.
        :param tags: (Optional) Metadata that can be used to manage the fleet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotfleetwise as iotfleetwise
            
            cfn_fleet_props = iotfleetwise.CfnFleetProps(
                id="id",
                signal_catalog_arn="signalCatalogArn",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06c4343c5d692e914e7c2c900c5e4f0c5bed9b41e2c90ff1efc672ba0974c3d8)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument signal_catalog_arn", value=signal_catalog_arn, expected_type=type_hints["signal_catalog_arn"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
            "signal_catalog_arn": signal_catalog_arn,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def id(self) -> builtins.str:
        '''The unique ID of the fleet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html#cfn-iotfleetwise-fleet-id
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signal_catalog_arn(self) -> builtins.str:
        '''The ARN of the signal catalog associated with the fleet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html#cfn-iotfleetwise-fleet-signalcatalogarn
        '''
        result = self._values.get("signal_catalog_arn")
        assert result is not None, "Required property 'signal_catalog_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(Optional) A brief description of the fleet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html#cfn-iotfleetwise-fleet-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''(Optional) Metadata that can be used to manage the fleet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-fleet.html#cfn-iotfleetwise-fleet-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFleetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnModelManifest(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnModelManifest",
):
    '''Creates a vehicle model (model manifest) that specifies signals (attributes, branches, sensors, and actuators).

    For more information, see `Vehicle models <https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/vehicle-models.html>`_ in the *AWS IoT FleetWise Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html
    :cloudformationResource: AWS::IoTFleetWise::ModelManifest
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotfleetwise as iotfleetwise
        
        cfn_model_manifest = iotfleetwise.CfnModelManifest(self, "MyCfnModelManifest",
            name="name",
            signal_catalog_arn="signalCatalogArn",
        
            # the properties below are optional
            description="description",
            nodes=["nodes"],
            status="status",
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
        name: builtins.str,
        signal_catalog_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        nodes: typing.Optional[typing.Sequence[builtins.str]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the vehicle model.
        :param signal_catalog_arn: The Amazon Resource Name (ARN) of the signal catalog associated with the vehicle model.
        :param description: (Optional) A brief description of the vehicle model.
        :param nodes: (Optional) A list of nodes, which are a general abstraction of signals.
        :param status: (Optional) The state of the vehicle model. If the status is ``ACTIVE`` , the vehicle model can't be edited. If the status is ``DRAFT`` , you can edit the vehicle model. Default: - "DRAFT"
        :param tags: (Optional) Metadata that can be used to manage the vehicle model.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f0e03fe14f53de97f2e7071c7f10132492e794782f840695921dc42cd286a81)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnModelManifestProps(
            name=name,
            signal_catalog_arn=signal_catalog_arn,
            description=description,
            nodes=nodes,
            status=status,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26ab7dc28e60a5682365801d22047c22eca01f42fd1ecbb3b9b379fa832ee14c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c6a3d382e4e768e4426411dff74ffd0bcaba33058efbe3e880fae9c7ace6d5d3)
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
        '''The Amazon Resource Name (ARN) of the vehicle model.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The time the vehicle model was created, in seconds since epoch (January 1, 1970 at midnight UTC time).

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModificationTime")
    def attr_last_modification_time(self) -> builtins.str:
        '''The time the vehicle model was last updated, in seconds since epoch (January 1, 1970 at midnight UTC time).

        :cloudformationAttribute: LastModificationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModificationTime"))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the vehicle model.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf56f12f94bd9c70533145a1dbb473b412b33dff8bc3791a2bcad34f29302b8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="signalCatalogArn")
    def signal_catalog_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the signal catalog associated with the vehicle model.'''
        return typing.cast(builtins.str, jsii.get(self, "signalCatalogArn"))

    @signal_catalog_arn.setter
    def signal_catalog_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9c26dfed7e5cc0b2e5105665abac1ffd59d367b056759c9e21642fa1214969e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signalCatalogArn", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(Optional) A brief description of the vehicle model.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d266113c8b366f668b05115f1bddeefd3b243d1c8fd8eecc3c143d130167d11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="nodes")
    def nodes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(Optional) A list of nodes, which are a general abstraction of signals.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "nodes"))

    @nodes.setter
    def nodes(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f0af1e0b1687e8bdbdeec73691f1b3cac6582b744e41041b611118e281c9134)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodes", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''(Optional) The state of the vehicle model.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f57f8c832da7ae938e0025bdef8ca3f24978b35cafd09be0c6bc21a8ee3329a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''(Optional) Metadata that can be used to manage the vehicle model.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0971ec828be6bb2e46ba031c824132b8b86c7ad424636cd3dd01983d63fc1adc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnModelManifestProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "signal_catalog_arn": "signalCatalogArn",
        "description": "description",
        "nodes": "nodes",
        "status": "status",
        "tags": "tags",
    },
)
class CfnModelManifestProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        signal_catalog_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        nodes: typing.Optional[typing.Sequence[builtins.str]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnModelManifest``.

        :param name: The name of the vehicle model.
        :param signal_catalog_arn: The Amazon Resource Name (ARN) of the signal catalog associated with the vehicle model.
        :param description: (Optional) A brief description of the vehicle model.
        :param nodes: (Optional) A list of nodes, which are a general abstraction of signals.
        :param status: (Optional) The state of the vehicle model. If the status is ``ACTIVE`` , the vehicle model can't be edited. If the status is ``DRAFT`` , you can edit the vehicle model. Default: - "DRAFT"
        :param tags: (Optional) Metadata that can be used to manage the vehicle model.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotfleetwise as iotfleetwise
            
            cfn_model_manifest_props = iotfleetwise.CfnModelManifestProps(
                name="name",
                signal_catalog_arn="signalCatalogArn",
            
                # the properties below are optional
                description="description",
                nodes=["nodes"],
                status="status",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1235282929965217b607172340e97ee502a13c24469f00158a042c2a92786260)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument signal_catalog_arn", value=signal_catalog_arn, expected_type=type_hints["signal_catalog_arn"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument nodes", value=nodes, expected_type=type_hints["nodes"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "signal_catalog_arn": signal_catalog_arn,
        }
        if description is not None:
            self._values["description"] = description
        if nodes is not None:
            self._values["nodes"] = nodes
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the vehicle model.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signal_catalog_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the signal catalog associated with the vehicle model.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-signalcatalogarn
        '''
        result = self._values.get("signal_catalog_arn")
        assert result is not None, "Required property 'signal_catalog_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(Optional) A brief description of the vehicle model.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nodes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(Optional) A list of nodes, which are a general abstraction of signals.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-nodes
        '''
        result = self._values.get("nodes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''(Optional) The state of the vehicle model.

        If the status is ``ACTIVE`` , the vehicle model can't be edited. If the status is ``DRAFT`` , you can edit the vehicle model.

        :default: - "DRAFT"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''(Optional) Metadata that can be used to manage the vehicle model.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-modelmanifest.html#cfn-iotfleetwise-modelmanifest-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModelManifestProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnSignalCatalog(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnSignalCatalog",
):
    '''Creates a collection of standardized signals that can be reused to create vehicle models.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html
    :cloudformationResource: AWS::IoTFleetWise::SignalCatalog
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotfleetwise as iotfleetwise
        
        cfn_signal_catalog = iotfleetwise.CfnSignalCatalog(self, "MyCfnSignalCatalog",
            description="description",
            name="name",
            node_counts=iotfleetwise.CfnSignalCatalog.NodeCountsProperty(
                total_actuators=123,
                total_attributes=123,
                total_branches=123,
                total_nodes=123,
                total_sensors=123
            ),
            nodes=[iotfleetwise.CfnSignalCatalog.NodeProperty(
                actuator=iotfleetwise.CfnSignalCatalog.ActuatorProperty(
                    data_type="dataType",
                    fully_qualified_name="fullyQualifiedName",
        
                    # the properties below are optional
                    allowed_values=["allowedValues"],
                    assigned_value="assignedValue",
                    description="description",
                    max=123,
                    min=123,
                    unit="unit"
                ),
                attribute=iotfleetwise.CfnSignalCatalog.AttributeProperty(
                    data_type="dataType",
                    fully_qualified_name="fullyQualifiedName",
        
                    # the properties below are optional
                    allowed_values=["allowedValues"],
                    assigned_value="assignedValue",
                    default_value="defaultValue",
                    description="description",
                    max=123,
                    min=123,
                    unit="unit"
                ),
                branch=iotfleetwise.CfnSignalCatalog.BranchProperty(
                    fully_qualified_name="fullyQualifiedName",
        
                    # the properties below are optional
                    description="description"
                ),
                sensor=iotfleetwise.CfnSignalCatalog.SensorProperty(
                    data_type="dataType",
                    fully_qualified_name="fullyQualifiedName",
        
                    # the properties below are optional
                    allowed_values=["allowedValues"],
                    description="description",
                    max=123,
                    min=123,
                    unit="unit"
                )
            )],
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
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        node_counts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSignalCatalog.NodeCountsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        nodes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSignalCatalog.NodeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param description: (Optional) A brief description of the signal catalog.
        :param name: (Optional) The name of the signal catalog.
        :param node_counts: (Optional) Information about the number of nodes and node types in a vehicle network.
        :param nodes: (Optional) A list of information about nodes, which are a general abstraction of signals.
        :param tags: (Optional) Metadata that can be used to manage the signal catalog.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00a926b4b26fd9efc933b63c5d4e497e8bfeceb8f4fb16790d18152e0fd2e282)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSignalCatalogProps(
            description=description,
            name=name,
            node_counts=node_counts,
            nodes=nodes,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d1771c8f83cb9b124255f0cb877c396f7dc19033885dac73e197f274702fe58)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3c1bc0963e13c138e8b1a9d56f8dfaba2b1c3f856cd9d0bc996158b2c5b704bb)
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
        '''The Amazon Resource Name (ARN) of the signal catalog.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The time the signal catalog was created in seconds since epoch (January 1, 1970 at midnight UTC time).

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModificationTime")
    def attr_last_modification_time(self) -> builtins.str:
        '''The time the signal catalog was last updated in seconds since epoch (January 1, 1970 at midnight UTC time).

        :cloudformationAttribute: LastModificationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModificationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrNodeCountsTotalActuators")
    def attr_node_counts_total_actuators(self) -> _IResolvable_da3f097b:
        '''The total number of nodes in a vehicle network that represent actuators.

        :cloudformationAttribute: NodeCounts.TotalActuators
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrNodeCountsTotalActuators"))

    @builtins.property
    @jsii.member(jsii_name="attrNodeCountsTotalAttributes")
    def attr_node_counts_total_attributes(self) -> _IResolvable_da3f097b:
        '''The total number of nodes in a vehicle network that represent attributes.

        :cloudformationAttribute: NodeCounts.TotalAttributes
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrNodeCountsTotalAttributes"))

    @builtins.property
    @jsii.member(jsii_name="attrNodeCountsTotalBranches")
    def attr_node_counts_total_branches(self) -> _IResolvable_da3f097b:
        '''The total number of nodes in a vehicle network that represent branches.

        :cloudformationAttribute: NodeCounts.TotalBranches
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrNodeCountsTotalBranches"))

    @builtins.property
    @jsii.member(jsii_name="attrNodeCountsTotalNodes")
    def attr_node_counts_total_nodes(self) -> _IResolvable_da3f097b:
        '''The total number of nodes in a vehicle network.

        :cloudformationAttribute: NodeCounts.TotalNodes
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrNodeCountsTotalNodes"))

    @builtins.property
    @jsii.member(jsii_name="attrNodeCountsTotalSensors")
    def attr_node_counts_total_sensors(self) -> _IResolvable_da3f097b:
        '''The total number of nodes in a vehicle network that represent sensors.

        :cloudformationAttribute: NodeCounts.TotalSensors
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrNodeCountsTotalSensors"))

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
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''(Optional) A brief description of the signal catalog.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f426284778d609b7de7cea520eccf5230e025cc40e766b3f3f0a9b3c536bfe4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''(Optional) The name of the signal catalog.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1be488894dded62944d72e0b078393e92b8c846e12e5682732e5b292abdf03c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nodeCounts")
    def node_counts(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSignalCatalog.NodeCountsProperty"]]:
        '''(Optional) Information about the number of nodes and node types in a vehicle network.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSignalCatalog.NodeCountsProperty"]], jsii.get(self, "nodeCounts"))

    @node_counts.setter
    def node_counts(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSignalCatalog.NodeCountsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f8c5daca018b1e857e68a1c38c2d8c8ad48c3e10d76e27f1b88db531cc7800d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeCounts", value)

    @builtins.property
    @jsii.member(jsii_name="nodes")
    def nodes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSignalCatalog.NodeProperty"]]]]:
        '''(Optional) A list of information about nodes, which are a general abstraction of signals.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSignalCatalog.NodeProperty"]]]], jsii.get(self, "nodes"))

    @nodes.setter
    def nodes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSignalCatalog.NodeProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__017bfa378203e76812e9cd13928c4c7498a8ed198568cb4d309d165dee01a3b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodes", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''(Optional) Metadata that can be used to manage the signal catalog.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da7834679bb5499c36909d22cd0d467aafe0c8ddde54a7ee3e9dda5f794b7bbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnSignalCatalog.ActuatorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_type": "dataType",
            "fully_qualified_name": "fullyQualifiedName",
            "allowed_values": "allowedValues",
            "assigned_value": "assignedValue",
            "description": "description",
            "max": "max",
            "min": "min",
            "unit": "unit",
        },
    )
    class ActuatorProperty:
        def __init__(
            self,
            *,
            data_type: builtins.str,
            fully_qualified_name: builtins.str,
            allowed_values: typing.Optional[typing.Sequence[builtins.str]] = None,
            assigned_value: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            max: typing.Optional[jsii.Number] = None,
            min: typing.Optional[jsii.Number] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A signal that represents a vehicle device such as the engine, heater, and door locks.

            Data from an actuator reports the state of a certain vehicle device.
            .. epigraph::

               Updating actuator data can change the state of a device. For example, you can turn on or off the heater by updating its actuator data.

            :param data_type: The specified data type of the actuator.
            :param fully_qualified_name: The fully qualified name of the actuator. For example, the fully qualified name of an actuator might be ``Vehicle.Front.Left.Door.Lock`` .
            :param allowed_values: (Optional) A list of possible values an actuator can take.
            :param assigned_value: (Optional) A specified value for the actuator.
            :param description: (Optional) A brief description of the actuator.
            :param max: (Optional) The specified possible maximum value of an actuator.
            :param min: (Optional) The specified possible minimum value of an actuator.
            :param unit: (Optional) The scientific unit for the actuator.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                actuator_property = iotfleetwise.CfnSignalCatalog.ActuatorProperty(
                    data_type="dataType",
                    fully_qualified_name="fullyQualifiedName",
                
                    # the properties below are optional
                    allowed_values=["allowedValues"],
                    assigned_value="assignedValue",
                    description="description",
                    max=123,
                    min=123,
                    unit="unit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3692c9418e6188deb5e6f1b10c8f51484f74857c2b24c543b0730826f0e8014c)
                check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
                check_type(argname="argument fully_qualified_name", value=fully_qualified_name, expected_type=type_hints["fully_qualified_name"])
                check_type(argname="argument allowed_values", value=allowed_values, expected_type=type_hints["allowed_values"])
                check_type(argname="argument assigned_value", value=assigned_value, expected_type=type_hints["assigned_value"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument max", value=max, expected_type=type_hints["max"])
                check_type(argname="argument min", value=min, expected_type=type_hints["min"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "data_type": data_type,
                "fully_qualified_name": fully_qualified_name,
            }
            if allowed_values is not None:
                self._values["allowed_values"] = allowed_values
            if assigned_value is not None:
                self._values["assigned_value"] = assigned_value
            if description is not None:
                self._values["description"] = description
            if max is not None:
                self._values["max"] = max
            if min is not None:
                self._values["min"] = min
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def data_type(self) -> builtins.str:
            '''The specified data type of the actuator.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-datatype
            '''
            result = self._values.get("data_type")
            assert result is not None, "Required property 'data_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def fully_qualified_name(self) -> builtins.str:
            '''The fully qualified name of the actuator.

            For example, the fully qualified name of an actuator might be ``Vehicle.Front.Left.Door.Lock`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-fullyqualifiedname
            '''
            result = self._values.get("fully_qualified_name")
            assert result is not None, "Required property 'fully_qualified_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def allowed_values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''(Optional) A list of possible values an actuator can take.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-allowedvalues
            '''
            result = self._values.get("allowed_values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def assigned_value(self) -> typing.Optional[builtins.str]:
            '''(Optional) A specified value for the actuator.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-assignedvalue
            '''
            result = self._values.get("assigned_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''(Optional) A brief description of the actuator.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max(self) -> typing.Optional[jsii.Number]:
            '''(Optional) The specified possible maximum value of an actuator.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-max
            '''
            result = self._values.get("max")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min(self) -> typing.Optional[jsii.Number]:
            '''(Optional) The specified possible minimum value of an actuator.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-min
            '''
            result = self._values.get("min")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''(Optional) The scientific unit for the actuator.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-actuator.html#cfn-iotfleetwise-signalcatalog-actuator-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActuatorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnSignalCatalog.AttributeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_type": "dataType",
            "fully_qualified_name": "fullyQualifiedName",
            "allowed_values": "allowedValues",
            "assigned_value": "assignedValue",
            "default_value": "defaultValue",
            "description": "description",
            "max": "max",
            "min": "min",
            "unit": "unit",
        },
    )
    class AttributeProperty:
        def __init__(
            self,
            *,
            data_type: builtins.str,
            fully_qualified_name: builtins.str,
            allowed_values: typing.Optional[typing.Sequence[builtins.str]] = None,
            assigned_value: typing.Optional[builtins.str] = None,
            default_value: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            max: typing.Optional[jsii.Number] = None,
            min: typing.Optional[jsii.Number] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A signal that represents static information about the vehicle, such as engine type or manufacturing date.

            :param data_type: The specified data type of the attribute.
            :param fully_qualified_name: The fully qualified name of the attribute. For example, the fully qualified name of an attribute might be ``Vehicle.Body.Engine.Type`` .
            :param allowed_values: (Optional) A list of possible values an attribute can be assigned.
            :param assigned_value: (Optional) A specified value for the attribute.
            :param default_value: (Optional) The default value of the attribute.
            :param description: (Optional) A brief description of the attribute.
            :param max: (Optional) The specified possible maximum value of the attribute.
            :param min: (Optional) The specified possible minimum value of the attribute.
            :param unit: (Optional) The scientific unit for the attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                attribute_property = iotfleetwise.CfnSignalCatalog.AttributeProperty(
                    data_type="dataType",
                    fully_qualified_name="fullyQualifiedName",
                
                    # the properties below are optional
                    allowed_values=["allowedValues"],
                    assigned_value="assignedValue",
                    default_value="defaultValue",
                    description="description",
                    max=123,
                    min=123,
                    unit="unit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__34812da89e0890988b83a21707bc72187e1251886f85c8d31c8bad4f51a5ad5d)
                check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
                check_type(argname="argument fully_qualified_name", value=fully_qualified_name, expected_type=type_hints["fully_qualified_name"])
                check_type(argname="argument allowed_values", value=allowed_values, expected_type=type_hints["allowed_values"])
                check_type(argname="argument assigned_value", value=assigned_value, expected_type=type_hints["assigned_value"])
                check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument max", value=max, expected_type=type_hints["max"])
                check_type(argname="argument min", value=min, expected_type=type_hints["min"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "data_type": data_type,
                "fully_qualified_name": fully_qualified_name,
            }
            if allowed_values is not None:
                self._values["allowed_values"] = allowed_values
            if assigned_value is not None:
                self._values["assigned_value"] = assigned_value
            if default_value is not None:
                self._values["default_value"] = default_value
            if description is not None:
                self._values["description"] = description
            if max is not None:
                self._values["max"] = max
            if min is not None:
                self._values["min"] = min
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def data_type(self) -> builtins.str:
            '''The specified data type of the attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-datatype
            '''
            result = self._values.get("data_type")
            assert result is not None, "Required property 'data_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def fully_qualified_name(self) -> builtins.str:
            '''The fully qualified name of the attribute.

            For example, the fully qualified name of an attribute might be ``Vehicle.Body.Engine.Type`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-fullyqualifiedname
            '''
            result = self._values.get("fully_qualified_name")
            assert result is not None, "Required property 'fully_qualified_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def allowed_values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''(Optional) A list of possible values an attribute can be assigned.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-allowedvalues
            '''
            result = self._values.get("allowed_values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def assigned_value(self) -> typing.Optional[builtins.str]:
            '''(Optional) A specified value for the attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-assignedvalue
            '''
            result = self._values.get("assigned_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def default_value(self) -> typing.Optional[builtins.str]:
            '''(Optional) The default value of the attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-defaultvalue
            '''
            result = self._values.get("default_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''(Optional) A brief description of the attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max(self) -> typing.Optional[jsii.Number]:
            '''(Optional) The specified possible maximum value of the attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-max
            '''
            result = self._values.get("max")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min(self) -> typing.Optional[jsii.Number]:
            '''(Optional) The specified possible minimum value of the attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-min
            '''
            result = self._values.get("min")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''(Optional) The scientific unit for the attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-attribute.html#cfn-iotfleetwise-signalcatalog-attribute-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnSignalCatalog.BranchProperty",
        jsii_struct_bases=[],
        name_mapping={
            "fully_qualified_name": "fullyQualifiedName",
            "description": "description",
        },
    )
    class BranchProperty:
        def __init__(
            self,
            *,
            fully_qualified_name: builtins.str,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A group of signals that are defined in a hierarchical structure.

            :param fully_qualified_name: The fully qualified name of the branch. For example, the fully qualified name of a branch might be ``Vehicle.Body.Engine`` .
            :param description: (Optional) A brief description of the branch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-branch.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                branch_property = iotfleetwise.CfnSignalCatalog.BranchProperty(
                    fully_qualified_name="fullyQualifiedName",
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__10c551cff70ab7e9a7ade619807100cf531ce4f17b5ade4cfc711a7110032c76)
                check_type(argname="argument fully_qualified_name", value=fully_qualified_name, expected_type=type_hints["fully_qualified_name"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "fully_qualified_name": fully_qualified_name,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def fully_qualified_name(self) -> builtins.str:
            '''The fully qualified name of the branch.

            For example, the fully qualified name of a branch might be ``Vehicle.Body.Engine`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-branch.html#cfn-iotfleetwise-signalcatalog-branch-fullyqualifiedname
            '''
            result = self._values.get("fully_qualified_name")
            assert result is not None, "Required property 'fully_qualified_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''(Optional) A brief description of the branch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-branch.html#cfn-iotfleetwise-signalcatalog-branch-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BranchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnSignalCatalog.NodeCountsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "total_actuators": "totalActuators",
            "total_attributes": "totalAttributes",
            "total_branches": "totalBranches",
            "total_nodes": "totalNodes",
            "total_sensors": "totalSensors",
        },
    )
    class NodeCountsProperty:
        def __init__(
            self,
            *,
            total_actuators: typing.Optional[jsii.Number] = None,
            total_attributes: typing.Optional[jsii.Number] = None,
            total_branches: typing.Optional[jsii.Number] = None,
            total_nodes: typing.Optional[jsii.Number] = None,
            total_sensors: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Information about the number of nodes and node types in a vehicle network.

            :param total_actuators: (Optional) The total number of nodes in a vehicle network that represent actuators.
            :param total_attributes: (Optional) The total number of nodes in a vehicle network that represent attributes.
            :param total_branches: (Optional) The total number of nodes in a vehicle network that represent branches.
            :param total_nodes: (Optional) The total number of nodes in a vehicle network.
            :param total_sensors: (Optional) The total number of nodes in a vehicle network that represent sensors.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                node_counts_property = iotfleetwise.CfnSignalCatalog.NodeCountsProperty(
                    total_actuators=123,
                    total_attributes=123,
                    total_branches=123,
                    total_nodes=123,
                    total_sensors=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e0ecad1dc29fa151da6ab7009debe26c40391783260739fb2c93faa85a3ff88d)
                check_type(argname="argument total_actuators", value=total_actuators, expected_type=type_hints["total_actuators"])
                check_type(argname="argument total_attributes", value=total_attributes, expected_type=type_hints["total_attributes"])
                check_type(argname="argument total_branches", value=total_branches, expected_type=type_hints["total_branches"])
                check_type(argname="argument total_nodes", value=total_nodes, expected_type=type_hints["total_nodes"])
                check_type(argname="argument total_sensors", value=total_sensors, expected_type=type_hints["total_sensors"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if total_actuators is not None:
                self._values["total_actuators"] = total_actuators
            if total_attributes is not None:
                self._values["total_attributes"] = total_attributes
            if total_branches is not None:
                self._values["total_branches"] = total_branches
            if total_nodes is not None:
                self._values["total_nodes"] = total_nodes
            if total_sensors is not None:
                self._values["total_sensors"] = total_sensors

        @builtins.property
        def total_actuators(self) -> typing.Optional[jsii.Number]:
            '''(Optional) The total number of nodes in a vehicle network that represent actuators.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html#cfn-iotfleetwise-signalcatalog-nodecounts-totalactuators
            '''
            result = self._values.get("total_actuators")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def total_attributes(self) -> typing.Optional[jsii.Number]:
            '''(Optional) The total number of nodes in a vehicle network that represent attributes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html#cfn-iotfleetwise-signalcatalog-nodecounts-totalattributes
            '''
            result = self._values.get("total_attributes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def total_branches(self) -> typing.Optional[jsii.Number]:
            '''(Optional) The total number of nodes in a vehicle network that represent branches.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html#cfn-iotfleetwise-signalcatalog-nodecounts-totalbranches
            '''
            result = self._values.get("total_branches")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def total_nodes(self) -> typing.Optional[jsii.Number]:
            '''(Optional) The total number of nodes in a vehicle network.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html#cfn-iotfleetwise-signalcatalog-nodecounts-totalnodes
            '''
            result = self._values.get("total_nodes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def total_sensors(self) -> typing.Optional[jsii.Number]:
            '''(Optional) The total number of nodes in a vehicle network that represent sensors.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-nodecounts.html#cfn-iotfleetwise-signalcatalog-nodecounts-totalsensors
            '''
            result = self._values.get("total_sensors")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NodeCountsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnSignalCatalog.NodeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "actuator": "actuator",
            "attribute": "attribute",
            "branch": "branch",
            "sensor": "sensor",
        },
    )
    class NodeProperty:
        def __init__(
            self,
            *,
            actuator: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSignalCatalog.ActuatorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            attribute: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSignalCatalog.AttributeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            branch: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSignalCatalog.BranchProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sensor: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSignalCatalog.SensorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A general abstraction of a signal.

            A node can be specified as an actuator, attribute, branch, or sensor.

            :param actuator: (Optional) Information about a node specified as an actuator. .. epigraph:: An actuator is a digital representation of a vehicle device.
            :param attribute: (Optional) Information about a node specified as an attribute. .. epigraph:: An attribute represents static information about a vehicle.
            :param branch: (Optional) Information about a node specified as a branch. .. epigraph:: A group of signals that are defined in a hierarchical structure.
            :param sensor: (Optional) An input component that reports the environmental condition of a vehicle. .. epigraph:: You can collect data about fluid levels, temperatures, vibrations, or battery voltage from sensors.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-node.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                node_property = iotfleetwise.CfnSignalCatalog.NodeProperty(
                    actuator=iotfleetwise.CfnSignalCatalog.ActuatorProperty(
                        data_type="dataType",
                        fully_qualified_name="fullyQualifiedName",
                
                        # the properties below are optional
                        allowed_values=["allowedValues"],
                        assigned_value="assignedValue",
                        description="description",
                        max=123,
                        min=123,
                        unit="unit"
                    ),
                    attribute=iotfleetwise.CfnSignalCatalog.AttributeProperty(
                        data_type="dataType",
                        fully_qualified_name="fullyQualifiedName",
                
                        # the properties below are optional
                        allowed_values=["allowedValues"],
                        assigned_value="assignedValue",
                        default_value="defaultValue",
                        description="description",
                        max=123,
                        min=123,
                        unit="unit"
                    ),
                    branch=iotfleetwise.CfnSignalCatalog.BranchProperty(
                        fully_qualified_name="fullyQualifiedName",
                
                        # the properties below are optional
                        description="description"
                    ),
                    sensor=iotfleetwise.CfnSignalCatalog.SensorProperty(
                        data_type="dataType",
                        fully_qualified_name="fullyQualifiedName",
                
                        # the properties below are optional
                        allowed_values=["allowedValues"],
                        description="description",
                        max=123,
                        min=123,
                        unit="unit"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3f7b644285514f42793054887b78a595b6a6dc6b59e3a153fd29b94fb12c45e0)
                check_type(argname="argument actuator", value=actuator, expected_type=type_hints["actuator"])
                check_type(argname="argument attribute", value=attribute, expected_type=type_hints["attribute"])
                check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
                check_type(argname="argument sensor", value=sensor, expected_type=type_hints["sensor"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if actuator is not None:
                self._values["actuator"] = actuator
            if attribute is not None:
                self._values["attribute"] = attribute
            if branch is not None:
                self._values["branch"] = branch
            if sensor is not None:
                self._values["sensor"] = sensor

        @builtins.property
        def actuator(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSignalCatalog.ActuatorProperty"]]:
            '''(Optional) Information about a node specified as an actuator.

            .. epigraph::

               An actuator is a digital representation of a vehicle device.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-node.html#cfn-iotfleetwise-signalcatalog-node-actuator
            '''
            result = self._values.get("actuator")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSignalCatalog.ActuatorProperty"]], result)

        @builtins.property
        def attribute(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSignalCatalog.AttributeProperty"]]:
            '''(Optional) Information about a node specified as an attribute.

            .. epigraph::

               An attribute represents static information about a vehicle.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-node.html#cfn-iotfleetwise-signalcatalog-node-attribute
            '''
            result = self._values.get("attribute")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSignalCatalog.AttributeProperty"]], result)

        @builtins.property
        def branch(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSignalCatalog.BranchProperty"]]:
            '''(Optional) Information about a node specified as a branch.

            .. epigraph::

               A group of signals that are defined in a hierarchical structure.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-node.html#cfn-iotfleetwise-signalcatalog-node-branch
            '''
            result = self._values.get("branch")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSignalCatalog.BranchProperty"]], result)

        @builtins.property
        def sensor(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSignalCatalog.SensorProperty"]]:
            '''(Optional) An input component that reports the environmental condition of a vehicle.

            .. epigraph::

               You can collect data about fluid levels, temperatures, vibrations, or battery voltage from sensors.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-node.html#cfn-iotfleetwise-signalcatalog-node-sensor
            '''
            result = self._values.get("sensor")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSignalCatalog.SensorProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NodeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnSignalCatalog.SensorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_type": "dataType",
            "fully_qualified_name": "fullyQualifiedName",
            "allowed_values": "allowedValues",
            "description": "description",
            "max": "max",
            "min": "min",
            "unit": "unit",
        },
    )
    class SensorProperty:
        def __init__(
            self,
            *,
            data_type: builtins.str,
            fully_qualified_name: builtins.str,
            allowed_values: typing.Optional[typing.Sequence[builtins.str]] = None,
            description: typing.Optional[builtins.str] = None,
            max: typing.Optional[jsii.Number] = None,
            min: typing.Optional[jsii.Number] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An input component that reports the environmental condition of a vehicle.

            .. epigraph::

               You can collect data about fluid levels, temperatures, vibrations, or battery voltage from sensors.

            :param data_type: The specified data type of the sensor.
            :param fully_qualified_name: The fully qualified name of the sensor. For example, the fully qualified name of a sensor might be ``Vehicle.Body.Engine.Battery`` .
            :param allowed_values: (Optional) A list of possible values a sensor can take.
            :param description: (Optional) A brief description of a sensor.
            :param max: (Optional) The specified possible maximum value of the sensor.
            :param min: (Optional) The specified possible minimum value of the sensor.
            :param unit: (Optional) The scientific unit of measurement for data collected by the sensor.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_iotfleetwise as iotfleetwise
                
                sensor_property = iotfleetwise.CfnSignalCatalog.SensorProperty(
                    data_type="dataType",
                    fully_qualified_name="fullyQualifiedName",
                
                    # the properties below are optional
                    allowed_values=["allowedValues"],
                    description="description",
                    max=123,
                    min=123,
                    unit="unit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__94596961b895ad256763fda2e339ce98264b2f53e8048d34957d691a584debcf)
                check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
                check_type(argname="argument fully_qualified_name", value=fully_qualified_name, expected_type=type_hints["fully_qualified_name"])
                check_type(argname="argument allowed_values", value=allowed_values, expected_type=type_hints["allowed_values"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument max", value=max, expected_type=type_hints["max"])
                check_type(argname="argument min", value=min, expected_type=type_hints["min"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "data_type": data_type,
                "fully_qualified_name": fully_qualified_name,
            }
            if allowed_values is not None:
                self._values["allowed_values"] = allowed_values
            if description is not None:
                self._values["description"] = description
            if max is not None:
                self._values["max"] = max
            if min is not None:
                self._values["min"] = min
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def data_type(self) -> builtins.str:
            '''The specified data type of the sensor.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-datatype
            '''
            result = self._values.get("data_type")
            assert result is not None, "Required property 'data_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def fully_qualified_name(self) -> builtins.str:
            '''The fully qualified name of the sensor.

            For example, the fully qualified name of a sensor might be ``Vehicle.Body.Engine.Battery`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-fullyqualifiedname
            '''
            result = self._values.get("fully_qualified_name")
            assert result is not None, "Required property 'fully_qualified_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def allowed_values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''(Optional) A list of possible values a sensor can take.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-allowedvalues
            '''
            result = self._values.get("allowed_values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''(Optional) A brief description of a sensor.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max(self) -> typing.Optional[jsii.Number]:
            '''(Optional) The specified possible maximum value of the sensor.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-max
            '''
            result = self._values.get("max")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min(self) -> typing.Optional[jsii.Number]:
            '''(Optional) The specified possible minimum value of the sensor.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-min
            '''
            result = self._values.get("min")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''(Optional) The scientific unit of measurement for data collected by the sensor.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotfleetwise-signalcatalog-sensor.html#cfn-iotfleetwise-signalcatalog-sensor-unit
            '''
            result = self._values.get("unit")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SensorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnSignalCatalogProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "name": "name",
        "node_counts": "nodeCounts",
        "nodes": "nodes",
        "tags": "tags",
    },
)
class CfnSignalCatalogProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        node_counts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSignalCatalog.NodeCountsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        nodes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSignalCatalog.NodeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSignalCatalog``.

        :param description: (Optional) A brief description of the signal catalog.
        :param name: (Optional) The name of the signal catalog.
        :param node_counts: (Optional) Information about the number of nodes and node types in a vehicle network.
        :param nodes: (Optional) A list of information about nodes, which are a general abstraction of signals.
        :param tags: (Optional) Metadata that can be used to manage the signal catalog.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotfleetwise as iotfleetwise
            
            cfn_signal_catalog_props = iotfleetwise.CfnSignalCatalogProps(
                description="description",
                name="name",
                node_counts=iotfleetwise.CfnSignalCatalog.NodeCountsProperty(
                    total_actuators=123,
                    total_attributes=123,
                    total_branches=123,
                    total_nodes=123,
                    total_sensors=123
                ),
                nodes=[iotfleetwise.CfnSignalCatalog.NodeProperty(
                    actuator=iotfleetwise.CfnSignalCatalog.ActuatorProperty(
                        data_type="dataType",
                        fully_qualified_name="fullyQualifiedName",
            
                        # the properties below are optional
                        allowed_values=["allowedValues"],
                        assigned_value="assignedValue",
                        description="description",
                        max=123,
                        min=123,
                        unit="unit"
                    ),
                    attribute=iotfleetwise.CfnSignalCatalog.AttributeProperty(
                        data_type="dataType",
                        fully_qualified_name="fullyQualifiedName",
            
                        # the properties below are optional
                        allowed_values=["allowedValues"],
                        assigned_value="assignedValue",
                        default_value="defaultValue",
                        description="description",
                        max=123,
                        min=123,
                        unit="unit"
                    ),
                    branch=iotfleetwise.CfnSignalCatalog.BranchProperty(
                        fully_qualified_name="fullyQualifiedName",
            
                        # the properties below are optional
                        description="description"
                    ),
                    sensor=iotfleetwise.CfnSignalCatalog.SensorProperty(
                        data_type="dataType",
                        fully_qualified_name="fullyQualifiedName",
            
                        # the properties below are optional
                        allowed_values=["allowedValues"],
                        description="description",
                        max=123,
                        min=123,
                        unit="unit"
                    )
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bd41091fa8f71325a3bfb8a9da99b2637a4ed068a31b5c7427bae2097ba03dd)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument node_counts", value=node_counts, expected_type=type_hints["node_counts"])
            check_type(argname="argument nodes", value=nodes, expected_type=type_hints["nodes"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if node_counts is not None:
            self._values["node_counts"] = node_counts
        if nodes is not None:
            self._values["nodes"] = nodes
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(Optional) A brief description of the signal catalog.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(Optional) The name of the signal catalog.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_counts(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSignalCatalog.NodeCountsProperty]]:
        '''(Optional) Information about the number of nodes and node types in a vehicle network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-nodecounts
        '''
        result = self._values.get("node_counts")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSignalCatalog.NodeCountsProperty]], result)

    @builtins.property
    def nodes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSignalCatalog.NodeProperty]]]]:
        '''(Optional) A list of information about nodes, which are a general abstraction of signals.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-nodes
        '''
        result = self._values.get("nodes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSignalCatalog.NodeProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''(Optional) Metadata that can be used to manage the signal catalog.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-signalcatalog.html#cfn-iotfleetwise-signalcatalog-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSignalCatalogProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnVehicle(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnVehicle",
):
    '''Creates a vehicle, which is an instance of a vehicle model (model manifest).

    Vehicles created from the same vehicle model consist of the same signals inherited from the vehicle model.
    .. epigraph::

       If you have an existing AWS IoT thing, you can use AWS IoT FleetWise to create a vehicle and collect data from your thing.

    For more information, see `Create a vehicle (console) <https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/create-vehicle-console.html>`_ in the *AWS IoT FleetWise Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html
    :cloudformationResource: AWS::IoTFleetWise::Vehicle
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iotfleetwise as iotfleetwise
        
        cfn_vehicle = iotfleetwise.CfnVehicle(self, "MyCfnVehicle",
            decoder_manifest_arn="decoderManifestArn",
            model_manifest_arn="modelManifestArn",
            name="name",
        
            # the properties below are optional
            association_behavior="associationBehavior",
            attributes={
                "attributes_key": "attributes"
            },
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
        decoder_manifest_arn: builtins.str,
        model_manifest_arn: builtins.str,
        name: builtins.str,
        association_behavior: typing.Optional[builtins.str] = None,
        attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param decoder_manifest_arn: The Amazon Resource Name (ARN) of a decoder manifest associated with the vehicle to create.
        :param model_manifest_arn: The Amazon Resource Name (ARN) of the vehicle model (model manifest) to create the vehicle from.
        :param name: The unique ID of the vehicle.
        :param association_behavior: (Optional) An option to create a new AWS IoT thing when creating a vehicle, or to validate an existing thing as a vehicle.
        :param attributes: (Optional) Static information about a vehicle in a key-value pair. For example: ``"engine Type"`` : ``"v6"``
        :param tags: (Optional) Metadata which can be used to manage the vehicle.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7269c48709f71a558e1053c22bd1ef391024711944714eff09133981d39ff54)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVehicleProps(
            decoder_manifest_arn=decoder_manifest_arn,
            model_manifest_arn=model_manifest_arn,
            name=name,
            association_behavior=association_behavior,
            attributes=attributes,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9b760c35be3bf4d0675af37ba807d0a1697ff44f4ca74c19616752539cb068e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__95af86f45386152805565188e4a1543fd1b5baf694bb584c01d1362547cffb8a)
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
        '''The Amazon Resource Name (ARN) of the vehicle.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The time the vehicle was created in seconds since epoch (January 1, 1970 at midnight UTC time).

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModificationTime")
    def attr_last_modification_time(self) -> builtins.str:
        '''The time the vehicle was last updated in seconds since epoch (January 1, 1970 at midnight UTC time).

        :cloudformationAttribute: LastModificationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModificationTime"))

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
    @jsii.member(jsii_name="decoderManifestArn")
    def decoder_manifest_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of a decoder manifest associated with the vehicle to create.'''
        return typing.cast(builtins.str, jsii.get(self, "decoderManifestArn"))

    @decoder_manifest_arn.setter
    def decoder_manifest_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07dfd0df1edc272a1b88da28d8fb52906df9f9da3594e4adc19e6bed64630a13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "decoderManifestArn", value)

    @builtins.property
    @jsii.member(jsii_name="modelManifestArn")
    def model_manifest_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the vehicle model (model manifest) to create the vehicle from.'''
        return typing.cast(builtins.str, jsii.get(self, "modelManifestArn"))

    @model_manifest_arn.setter
    def model_manifest_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44d29d9f9e6bcafa63b7a5a0e813e2a6bc9bf4dce13cba6bf0c8f3674cb8ab42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelManifestArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The unique ID of the vehicle.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4505759fcded180f5aeb7d85f70fe4449363a0030d04d86046e82cc83a56ab92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="associationBehavior")
    def association_behavior(self) -> typing.Optional[builtins.str]:
        '''(Optional) An option to create a new AWS IoT thing when creating a vehicle, or to validate an existing thing as a vehicle.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "associationBehavior"))

    @association_behavior.setter
    def association_behavior(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58744563e98ef419016bcbd09088b8ed734d062980dbe0b3fa2e4ff0fe8f722d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associationBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''(Optional) Static information about a vehicle in a key-value pair.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "attributes"))

    @attributes.setter
    def attributes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58c16f565864833e1b877bedd4f136bed80dfb02ea2ee4627d0b77770775cf1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributes", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''(Optional) Metadata which can be used to manage the vehicle.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__289b2e31ff1b98481910d4cc38b6e283cbc14d5b0abe0266ffe3aff2d0287c48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_iotfleetwise.CfnVehicleProps",
    jsii_struct_bases=[],
    name_mapping={
        "decoder_manifest_arn": "decoderManifestArn",
        "model_manifest_arn": "modelManifestArn",
        "name": "name",
        "association_behavior": "associationBehavior",
        "attributes": "attributes",
        "tags": "tags",
    },
)
class CfnVehicleProps:
    def __init__(
        self,
        *,
        decoder_manifest_arn: builtins.str,
        model_manifest_arn: builtins.str,
        name: builtins.str,
        association_behavior: typing.Optional[builtins.str] = None,
        attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnVehicle``.

        :param decoder_manifest_arn: The Amazon Resource Name (ARN) of a decoder manifest associated with the vehicle to create.
        :param model_manifest_arn: The Amazon Resource Name (ARN) of the vehicle model (model manifest) to create the vehicle from.
        :param name: The unique ID of the vehicle.
        :param association_behavior: (Optional) An option to create a new AWS IoT thing when creating a vehicle, or to validate an existing thing as a vehicle.
        :param attributes: (Optional) Static information about a vehicle in a key-value pair. For example: ``"engine Type"`` : ``"v6"``
        :param tags: (Optional) Metadata which can be used to manage the vehicle.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iotfleetwise as iotfleetwise
            
            cfn_vehicle_props = iotfleetwise.CfnVehicleProps(
                decoder_manifest_arn="decoderManifestArn",
                model_manifest_arn="modelManifestArn",
                name="name",
            
                # the properties below are optional
                association_behavior="associationBehavior",
                attributes={
                    "attributes_key": "attributes"
                },
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24066091b85e61810110bf13ed6c1606f4b16a2637a0ea85ffb516d58b89a826)
            check_type(argname="argument decoder_manifest_arn", value=decoder_manifest_arn, expected_type=type_hints["decoder_manifest_arn"])
            check_type(argname="argument model_manifest_arn", value=model_manifest_arn, expected_type=type_hints["model_manifest_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument association_behavior", value=association_behavior, expected_type=type_hints["association_behavior"])
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "decoder_manifest_arn": decoder_manifest_arn,
            "model_manifest_arn": model_manifest_arn,
            "name": name,
        }
        if association_behavior is not None:
            self._values["association_behavior"] = association_behavior
        if attributes is not None:
            self._values["attributes"] = attributes
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def decoder_manifest_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of a decoder manifest associated with the vehicle to create.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-decodermanifestarn
        '''
        result = self._values.get("decoder_manifest_arn")
        assert result is not None, "Required property 'decoder_manifest_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def model_manifest_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the vehicle model (model manifest) to create the vehicle from.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-modelmanifestarn
        '''
        result = self._values.get("model_manifest_arn")
        assert result is not None, "Required property 'model_manifest_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The unique ID of the vehicle.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def association_behavior(self) -> typing.Optional[builtins.str]:
        '''(Optional) An option to create a new AWS IoT thing when creating a vehicle, or to validate an existing thing as a vehicle.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-associationbehavior
        '''
        result = self._values.get("association_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''(Optional) Static information about a vehicle in a key-value pair.

        For example: ``"engine Type"`` : ``"v6"``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-attributes
        '''
        result = self._values.get("attributes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''(Optional) Metadata which can be used to manage the vehicle.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotfleetwise-vehicle.html#cfn-iotfleetwise-vehicle-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVehicleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCampaign",
    "CfnCampaignProps",
    "CfnDecoderManifest",
    "CfnDecoderManifestProps",
    "CfnFleet",
    "CfnFleetProps",
    "CfnModelManifest",
    "CfnModelManifestProps",
    "CfnSignalCatalog",
    "CfnSignalCatalogProps",
    "CfnVehicle",
    "CfnVehicleProps",
]

publication.publish()

def _typecheckingstub__f7abc45d2046b48ec3bc5807ec2826a784930a5009b41b194dd6e4bed2413f8d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    action: builtins.str,
    collection_scheme: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.CollectionSchemeProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    signal_catalog_arn: builtins.str,
    target_arn: builtins.str,
    compression: typing.Optional[builtins.str] = None,
    data_destination_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.DataDestinationConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    data_extra_dimensions: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    diagnostics_mode: typing.Optional[builtins.str] = None,
    expiry_time: typing.Optional[builtins.str] = None,
    post_trigger_collection_duration: typing.Optional[jsii.Number] = None,
    priority: typing.Optional[jsii.Number] = None,
    signals_to_collect: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.SignalInformationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    spooling_mode: typing.Optional[builtins.str] = None,
    start_time: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09fbf1d259fb24b3ffc81851949fdbc1abbaa3df7fef9d0031938dd5b723205f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89d4f6e55fdf4b8418716e773b2a62dc1763b8a2553490a7567e2cfe6f27d77f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66dafa89e69b8562346040c56213280b8861d04a6b73911f5471941f58e3d463(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__868a9ff35e32583e37d3c029fdca22ea031055a38c7dd0dcbfa1f30846ee551d(
    value: typing.Union[_IResolvable_da3f097b, CfnCampaign.CollectionSchemeProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61dfb8819034de21f19e0466ab15e542f6b7270be82092cfffb60970bbc9708b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5a5ce376850a7a86f93938b2f133fca5cc48d27769ddbdcaf2291ab00d48bac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6154b7ad20e73a4e23143d3707a09d050bbb1092b307bc8e0145589083575f5a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17ec1dfb29d11e0d55dc84fc23937babfb2d1e33fdf8192c23c4130716fa6a02(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82921435d923d6321ee61688fc07b3aa8e4790a3f86fff3b232ba9bb71993646(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCampaign.DataDestinationConfigProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d948dada7b0177410b9932e42eb5ef3a76fe3c3274594fb0b3ffa49ded440324(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24bd4808a24c1ef5c17e4550fe902693202fc86dca7d97ddddcd994c722276bf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e28d99e6bd56db5b97b272b04aeb5c1af8103d1b8b0080fe05d1a5f2fb149e2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11cce95e76c12143123da5bc8c755592e90256d2ed3e61b6cd5a6d839e9318e9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__660bebd5ebd77dcec64e7fcb6fd086f3ce7252832c2b9967a58fbda5d5fe6bd2(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7eceb1aaf4de04c54d69e423a5e6de547b2e207a605050b36deefed0ccc4c9b8(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49e9a686748dfc74bfa8ee7c7e9c87ccd64dc236b6b72144f22cebb87065a3d7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCampaign.SignalInformationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2470f955a4e2089dd25722e38734a0e9fffc60420def257c19a15c6db378b523(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67bb9c23f09e7b35b9a93baa91bd26954a931e9dac0ecfa4b472a8de197849a7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3493674fad7a8f212642ff0171f2ddf22e133359a2aee9ae22d9b3da5be4a8b6(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d2862e457404e83c11e21830d9ccb15c52f442305bb2db0a1ebf80b0de3877a(
    *,
    condition_based_collection_scheme: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.ConditionBasedCollectionSchemeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    time_based_collection_scheme: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.TimeBasedCollectionSchemeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd3351de9470a98f13f006dd95deedef6c30dbfc08cdfe7bde2b9d950d547615(
    *,
    expression: builtins.str,
    condition_language_version: typing.Optional[jsii.Number] = None,
    minimum_trigger_interval_ms: typing.Optional[jsii.Number] = None,
    trigger_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a76d3ecac8a3286ba64142d7bb2621dd82495be58438bdb339be1559bb8129f3(
    *,
    s3_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.S3ConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    timestream_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.TimestreamConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb82e0c92a9fdd48764ec7ba91d5dabd16d19776d63621d9b09fba43e604eb8a(
    *,
    bucket_arn: builtins.str,
    data_format: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
    storage_compression_format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53d5027f8c4da8a26f3f9cf9e5ab42f41c46c70820c567f2c340ad26784c6997(
    *,
    name: builtins.str,
    max_sample_count: typing.Optional[jsii.Number] = None,
    minimum_sampling_interval_ms: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bffeabbd9e812e2b77c405369e410069d9bd5d47737b57d4b23d11433d93329(
    *,
    period_ms: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5788ae222c7e21aaed8bd9dbed72cfbc09a7c423d494e8aa4ae9d7a226350700(
    *,
    execution_role_arn: builtins.str,
    timestream_table_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54c45792d3f0c102d3358acf678401b9616a7fee4b70882083776c5f9635cf71(
    *,
    action: builtins.str,
    collection_scheme: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.CollectionSchemeProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    signal_catalog_arn: builtins.str,
    target_arn: builtins.str,
    compression: typing.Optional[builtins.str] = None,
    data_destination_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.DataDestinationConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    data_extra_dimensions: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    diagnostics_mode: typing.Optional[builtins.str] = None,
    expiry_time: typing.Optional[builtins.str] = None,
    post_trigger_collection_duration: typing.Optional[jsii.Number] = None,
    priority: typing.Optional[jsii.Number] = None,
    signals_to_collect: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCampaign.SignalInformationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    spooling_mode: typing.Optional[builtins.str] = None,
    start_time: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd0d8efce6baca0fa606fb0cf95bebcdeda196fcde2fb7e18542334332eb8ba4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    model_manifest_arn: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    network_interfaces: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDecoderManifest.NetworkInterfacesItemsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    signal_decoders: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDecoderManifest.SignalDecodersItemsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7c1f4e3cc81a06a60eef4d178a3aaf54f7c99cca4a0481a51c50d560d76ba09(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d12e1e0a1684404c74ecc86ed4ae33ffdac8b3611db04d45a6a46ef55c87bbbe(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b8f77dd16bf3c88bd7f097b2327803bb360213ddb0b320722348c6a1b99afce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a5a43cce0da85f8ef5934babccfc93088317c19ae303a38ae3adc573ad6c633(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1e4501ad7312a6dac9b29817aed239a25a724386677541e036223da190a2d9b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4059f7868b58b43acd642cd2537b59a16c939681bb626ef560a6efbc8d7cda5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDecoderManifest.NetworkInterfacesItemsProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32a124503ae0a9be522e3691aef89b61eb023aea0d8b57342dcef4a708073af0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDecoderManifest.SignalDecodersItemsProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8428ef9254e1885dc4fbe7c358202136e77b7b7c68b9e9b92c6016edfca9ad8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7589d4cace83e702bf125b3cef9c6977200de03aea448dca5adc0790c282933(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f41ef25a35e6c8526ccaa9ecc87becb68ccffe031fd1ae9c650719807164dc68(
    *,
    name: builtins.str,
    protocol_name: typing.Optional[builtins.str] = None,
    protocol_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1254441c18c12325ded72e4eeb9b3d36d94b7f5b9ff298529a028d2b2d735a3(
    *,
    can_interface: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDecoderManifest.CanInterfaceProperty, typing.Dict[builtins.str, typing.Any]]],
    interface_id: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a43ee038ead545f634e09871c712c71b73d4a94505498eb010ce592d21e11b3a(
    *,
    can_signal: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDecoderManifest.CanSignalProperty, typing.Dict[builtins.str, typing.Any]]],
    fully_qualified_name: builtins.str,
    interface_id: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1fdd86137a92797754860d3b8da115496d862a2f95c8e39c08a70fdf76855c4(
    *,
    factor: builtins.str,
    is_big_endian: builtins.str,
    is_signed: builtins.str,
    length: builtins.str,
    message_id: builtins.str,
    offset: builtins.str,
    start_bit: builtins.str,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__763a8a9c006b5f64d4a07d45a9f83b3a4b0be692630292c6e33fd7f6c09a4c07(
    *,
    interface_id: builtins.str,
    type: builtins.str,
    can_interface: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDecoderManifest.CanInterfaceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    obd_interface: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDecoderManifest.ObdInterfaceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__619deb4a5a81c6ae8bcb58cd0d96a9beddd6b7ac867f4e945e1bd4668fc25b17(
    *,
    name: builtins.str,
    request_message_id: builtins.str,
    dtc_request_interval_seconds: typing.Optional[builtins.str] = None,
    has_transmission_ecu: typing.Optional[builtins.str] = None,
    obd_standard: typing.Optional[builtins.str] = None,
    pid_request_interval_seconds: typing.Optional[builtins.str] = None,
    use_extended_ids: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c45c63503d1f718c56dd74e773036e65da8f350e05d1468a20136ad9ee6cfaf7(
    *,
    interface_id: builtins.str,
    obd_interface: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDecoderManifest.ObdInterfaceProperty, typing.Dict[builtins.str, typing.Any]]],
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b66ad96f7c649fd06e9447c0e2e4b23db06a0053d635376375d3d5fcf7fc8e7(
    *,
    fully_qualified_name: builtins.str,
    interface_id: builtins.str,
    obd_signal: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDecoderManifest.ObdSignalProperty, typing.Dict[builtins.str, typing.Any]]],
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccb776ce607aa563ef4bc105956ab186267e45066ee492c162a4555709004e4b(
    *,
    byte_length: builtins.str,
    offset: builtins.str,
    pid: builtins.str,
    pid_response_length: builtins.str,
    scaling: builtins.str,
    service_mode: builtins.str,
    start_byte: builtins.str,
    bit_mask_length: typing.Optional[builtins.str] = None,
    bit_right_shift: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5832121c7c16050419993147c157e7f5739fca1dc1afba25d1f52da2d4bd75fb(
    *,
    fully_qualified_name: builtins.str,
    interface_id: builtins.str,
    type: builtins.str,
    can_signal: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDecoderManifest.CanSignalProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    obd_signal: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDecoderManifest.ObdSignalProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1be5cfb3ca0441a2fdb0856303c08c4449592f7472588f5c0659c42af4d89e2c(
    *,
    model_manifest_arn: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    network_interfaces: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDecoderManifest.NetworkInterfacesItemsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    signal_decoders: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDecoderManifest.SignalDecodersItemsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be2399a288ba3f0fe4eba6c31d42082d31eac165febede18736a759d92f2120d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    id: builtins.str,
    signal_catalog_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b66a25ffe3875464ec35ff63e6d6335f63f5bd966c356414cfa0ec840225eedd(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19ef6ad0585e294dae29b4c919f9fbf11b89c72deadd5a5cda8a56f1433235a8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__521c3cdc3b4991a92beb684d8c8af88ceab73dcbd34d08d120663c9c7f94d059(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eec1aed040f26806fdbfee937ccf8c8b0ccb036bc460096cfbb5b04da65cccca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47625bcd41335399a9f769fa64574c2375f2937ed4511d09a3984dbd0abef447(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b778328780cd48e8666cfdebbdaa84f93e4dd8ae56fc24f3ac40fb8baa31791(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06c4343c5d692e914e7c2c900c5e4f0c5bed9b41e2c90ff1efc672ba0974c3d8(
    *,
    id: builtins.str,
    signal_catalog_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f0e03fe14f53de97f2e7071c7f10132492e794782f840695921dc42cd286a81(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    signal_catalog_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    nodes: typing.Optional[typing.Sequence[builtins.str]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26ab7dc28e60a5682365801d22047c22eca01f42fd1ecbb3b9b379fa832ee14c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6a3d382e4e768e4426411dff74ffd0bcaba33058efbe3e880fae9c7ace6d5d3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf56f12f94bd9c70533145a1dbb473b412b33dff8bc3791a2bcad34f29302b8d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9c26dfed7e5cc0b2e5105665abac1ffd59d367b056759c9e21642fa1214969e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d266113c8b366f668b05115f1bddeefd3b243d1c8fd8eecc3c143d130167d11(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f0af1e0b1687e8bdbdeec73691f1b3cac6582b744e41041b611118e281c9134(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f57f8c832da7ae938e0025bdef8ca3f24978b35cafd09be0c6bc21a8ee3329a9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0971ec828be6bb2e46ba031c824132b8b86c7ad424636cd3dd01983d63fc1adc(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1235282929965217b607172340e97ee502a13c24469f00158a042c2a92786260(
    *,
    name: builtins.str,
    signal_catalog_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    nodes: typing.Optional[typing.Sequence[builtins.str]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00a926b4b26fd9efc933b63c5d4e497e8bfeceb8f4fb16790d18152e0fd2e282(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    node_counts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSignalCatalog.NodeCountsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    nodes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSignalCatalog.NodeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d1771c8f83cb9b124255f0cb877c396f7dc19033885dac73e197f274702fe58(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c1bc0963e13c138e8b1a9d56f8dfaba2b1c3f856cd9d0bc996158b2c5b704bb(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f426284778d609b7de7cea520eccf5230e025cc40e766b3f3f0a9b3c536bfe4a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1be488894dded62944d72e0b078393e92b8c846e12e5682732e5b292abdf03c1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f8c5daca018b1e857e68a1c38c2d8c8ad48c3e10d76e27f1b88db531cc7800d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSignalCatalog.NodeCountsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__017bfa378203e76812e9cd13928c4c7498a8ed198568cb4d309d165dee01a3b3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSignalCatalog.NodeProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da7834679bb5499c36909d22cd0d467aafe0c8ddde54a7ee3e9dda5f794b7bbb(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3692c9418e6188deb5e6f1b10c8f51484f74857c2b24c543b0730826f0e8014c(
    *,
    data_type: builtins.str,
    fully_qualified_name: builtins.str,
    allowed_values: typing.Optional[typing.Sequence[builtins.str]] = None,
    assigned_value: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    max: typing.Optional[jsii.Number] = None,
    min: typing.Optional[jsii.Number] = None,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34812da89e0890988b83a21707bc72187e1251886f85c8d31c8bad4f51a5ad5d(
    *,
    data_type: builtins.str,
    fully_qualified_name: builtins.str,
    allowed_values: typing.Optional[typing.Sequence[builtins.str]] = None,
    assigned_value: typing.Optional[builtins.str] = None,
    default_value: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    max: typing.Optional[jsii.Number] = None,
    min: typing.Optional[jsii.Number] = None,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10c551cff70ab7e9a7ade619807100cf531ce4f17b5ade4cfc711a7110032c76(
    *,
    fully_qualified_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0ecad1dc29fa151da6ab7009debe26c40391783260739fb2c93faa85a3ff88d(
    *,
    total_actuators: typing.Optional[jsii.Number] = None,
    total_attributes: typing.Optional[jsii.Number] = None,
    total_branches: typing.Optional[jsii.Number] = None,
    total_nodes: typing.Optional[jsii.Number] = None,
    total_sensors: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f7b644285514f42793054887b78a595b6a6dc6b59e3a153fd29b94fb12c45e0(
    *,
    actuator: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSignalCatalog.ActuatorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    attribute: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSignalCatalog.AttributeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    branch: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSignalCatalog.BranchProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sensor: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSignalCatalog.SensorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94596961b895ad256763fda2e339ce98264b2f53e8048d34957d691a584debcf(
    *,
    data_type: builtins.str,
    fully_qualified_name: builtins.str,
    allowed_values: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    max: typing.Optional[jsii.Number] = None,
    min: typing.Optional[jsii.Number] = None,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bd41091fa8f71325a3bfb8a9da99b2637a4ed068a31b5c7427bae2097ba03dd(
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    node_counts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSignalCatalog.NodeCountsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    nodes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSignalCatalog.NodeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7269c48709f71a558e1053c22bd1ef391024711944714eff09133981d39ff54(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    decoder_manifest_arn: builtins.str,
    model_manifest_arn: builtins.str,
    name: builtins.str,
    association_behavior: typing.Optional[builtins.str] = None,
    attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9b760c35be3bf4d0675af37ba807d0a1697ff44f4ca74c19616752539cb068e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95af86f45386152805565188e4a1543fd1b5baf694bb584c01d1362547cffb8a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07dfd0df1edc272a1b88da28d8fb52906df9f9da3594e4adc19e6bed64630a13(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44d29d9f9e6bcafa63b7a5a0e813e2a6bc9bf4dce13cba6bf0c8f3674cb8ab42(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4505759fcded180f5aeb7d85f70fe4449363a0030d04d86046e82cc83a56ab92(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58744563e98ef419016bcbd09088b8ed734d062980dbe0b3fa2e4ff0fe8f722d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58c16f565864833e1b877bedd4f136bed80dfb02ea2ee4627d0b77770775cf1c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__289b2e31ff1b98481910d4cc38b6e283cbc14d5b0abe0266ffe3aff2d0287c48(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24066091b85e61810110bf13ed6c1606f4b16a2637a0ea85ffb516d58b89a826(
    *,
    decoder_manifest_arn: builtins.str,
    model_manifest_arn: builtins.str,
    name: builtins.str,
    association_behavior: typing.Optional[builtins.str] = None,
    attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
