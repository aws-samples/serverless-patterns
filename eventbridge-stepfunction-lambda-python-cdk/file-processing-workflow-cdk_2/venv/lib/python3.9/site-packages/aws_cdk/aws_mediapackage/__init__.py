'''
# AWS::MediaPackage Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_mediapackage as mediapackage
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for MediaPackage construct libraries](https://constructs.dev/search?q=mediapackage)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::MediaPackage resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MediaPackage.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::MediaPackage](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MediaPackage.html).

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
class CfnAsset(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediapackage.CfnAsset",
):
    '''Creates an asset to ingest VOD content.

    After it's created, the asset starts ingesting content and generates playback URLs for the packaging configurations associated with it. When ingest is complete, downstream devices use the appropriate URL to request VOD content from AWS Elemental MediaPackage .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediapackage as mediapackage
        
        cfn_asset = mediapackage.CfnAsset(self, "MyCfnAsset",
            id="id",
            packaging_group_id="packagingGroupId",
            source_arn="sourceArn",
            source_role_arn="sourceRoleArn",
        
            # the properties below are optional
            egress_endpoints=[mediapackage.CfnAsset.EgressEndpointProperty(
                packaging_configuration_id="packagingConfigurationId",
                url="url"
            )],
            resource_id="resourceId",
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
        packaging_group_id: builtins.str,
        source_arn: builtins.str,
        source_role_arn: builtins.str,
        egress_endpoints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAsset.EgressEndpointProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        resource_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id_: Construct identifier for this resource (unique in its scope).
        :param id: Unique identifier that you assign to the asset.
        :param packaging_group_id: The ID of the packaging group associated with this asset.
        :param source_arn: The ARN for the source content in Amazon S3.
        :param source_role_arn: The ARN for the IAM role that provides AWS Elemental MediaPackage access to the Amazon S3 bucket where the source content is stored. Valid format: arn:aws:iam::{accountID}:role/{name}
        :param egress_endpoints: List of playback endpoints that are available for this asset.
        :param resource_id: Unique identifier for this asset, as it's configured in the key provider service.
        :param tags: The tags to assign to the asset.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f18cc60b1c4089a35fd436a7258b422078f0fecc32d062615b3434a45a2e2b39)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        props = CfnAssetProps(
            id=id,
            packaging_group_id=packaging_group_id,
            source_arn=source_arn,
            source_role_arn=source_role_arn,
            egress_endpoints=egress_endpoints,
            resource_id=resource_id,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id_, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2a76b75b5e09e9a8d97792dff99a5272eed0a3f4557a4181b2b56b77f0cdcef)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b4389b9d5dd5c3d310e064eeab7db8ef228e477e34d2335664ab83fd39985040)
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
        '''The Amazon Resource Name (ARN) for the asset.

        You can get this from the response to any request to the asset.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The date and time that the asset was initially submitted for ingest.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

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
        '''Unique identifier that you assign to the asset.'''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35b6682ae346664a086b9dff0d456af04d28c65a084cf0ae564d117116459491)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="packagingGroupId")
    def packaging_group_id(self) -> builtins.str:
        '''The ID of the packaging group associated with this asset.'''
        return typing.cast(builtins.str, jsii.get(self, "packagingGroupId"))

    @packaging_group_id.setter
    def packaging_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35d95ecd9b726f976edf6a9d1f766835ad6631faef33a2d12b96d6c8d6638d03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "packagingGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="sourceArn")
    def source_arn(self) -> builtins.str:
        '''The ARN for the source content in Amazon S3.'''
        return typing.cast(builtins.str, jsii.get(self, "sourceArn"))

    @source_arn.setter
    def source_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72d3df8af23896f6f5ef3194ec3ed4bbfbb982faf70463969c7c34164fee8ed5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="sourceRoleArn")
    def source_role_arn(self) -> builtins.str:
        '''The ARN for the IAM role that provides AWS Elemental MediaPackage access to the Amazon S3 bucket where the source content is stored.'''
        return typing.cast(builtins.str, jsii.get(self, "sourceRoleArn"))

    @source_role_arn.setter
    def source_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41f7b135121a8ac650206952f41f006f691f4d3be4e73e76fa6bef7576e8f9fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="egressEndpoints")
    def egress_endpoints(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAsset.EgressEndpointProperty"]]]]:
        '''List of playback endpoints that are available for this asset.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAsset.EgressEndpointProperty"]]]], jsii.get(self, "egressEndpoints"))

    @egress_endpoints.setter
    def egress_endpoints(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnAsset.EgressEndpointProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a644764b4a43d734fea1bf555feb1c097efc7cf3b30ba898c866f73a019f663e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "egressEndpoints", value)

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> typing.Optional[builtins.str]:
        '''Unique identifier for this asset, as it's configured in the key provider service.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceId"))

    @resource_id.setter
    def resource_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcd0264c72c6ead9699a93d8126ea230415f8b868e98b4a5a1c59fc224a6321b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceId", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to assign to the asset.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40009e0bd275773b97adc81d95be811402372bc85c522f243c45a58fa3a41f3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnAsset.EgressEndpointProperty",
        jsii_struct_bases=[],
        name_mapping={
            "packaging_configuration_id": "packagingConfigurationId",
            "url": "url",
        },
    )
    class EgressEndpointProperty:
        def __init__(
            self,
            *,
            packaging_configuration_id: builtins.str,
            url: builtins.str,
        ) -> None:
            '''The playback endpoint for a packaging configuration on an asset.

            :param packaging_configuration_id: The ID of a packaging configuration that's applied to this asset.
            :param url: The URL that's used to request content from this endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-asset-egressendpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                egress_endpoint_property = mediapackage.CfnAsset.EgressEndpointProperty(
                    packaging_configuration_id="packagingConfigurationId",
                    url="url"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7d2fee4640b24dddffbfcd26c914f32e00de4b0cf2345061ed96cb652a4b4abb)
                check_type(argname="argument packaging_configuration_id", value=packaging_configuration_id, expected_type=type_hints["packaging_configuration_id"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "packaging_configuration_id": packaging_configuration_id,
                "url": url,
            }

        @builtins.property
        def packaging_configuration_id(self) -> builtins.str:
            '''The ID of a packaging configuration that's applied to this asset.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-asset-egressendpoint.html#cfn-mediapackage-asset-egressendpoint-packagingconfigurationid
            '''
            result = self._values.get("packaging_configuration_id")
            assert result is not None, "Required property 'packaging_configuration_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def url(self) -> builtins.str:
            '''The URL that's used to request content from this endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-asset-egressendpoint.html#cfn-mediapackage-asset-egressendpoint-url
            '''
            result = self._values.get("url")
            assert result is not None, "Required property 'url' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EgressEndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediapackage.CfnAssetProps",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "packaging_group_id": "packagingGroupId",
        "source_arn": "sourceArn",
        "source_role_arn": "sourceRoleArn",
        "egress_endpoints": "egressEndpoints",
        "resource_id": "resourceId",
        "tags": "tags",
    },
)
class CfnAssetProps:
    def __init__(
        self,
        *,
        id: builtins.str,
        packaging_group_id: builtins.str,
        source_arn: builtins.str,
        source_role_arn: builtins.str,
        egress_endpoints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAsset.EgressEndpointProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        resource_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAsset``.

        :param id: Unique identifier that you assign to the asset.
        :param packaging_group_id: The ID of the packaging group associated with this asset.
        :param source_arn: The ARN for the source content in Amazon S3.
        :param source_role_arn: The ARN for the IAM role that provides AWS Elemental MediaPackage access to the Amazon S3 bucket where the source content is stored. Valid format: arn:aws:iam::{accountID}:role/{name}
        :param egress_endpoints: List of playback endpoints that are available for this asset.
        :param resource_id: Unique identifier for this asset, as it's configured in the key provider service.
        :param tags: The tags to assign to the asset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediapackage as mediapackage
            
            cfn_asset_props = mediapackage.CfnAssetProps(
                id="id",
                packaging_group_id="packagingGroupId",
                source_arn="sourceArn",
                source_role_arn="sourceRoleArn",
            
                # the properties below are optional
                egress_endpoints=[mediapackage.CfnAsset.EgressEndpointProperty(
                    packaging_configuration_id="packagingConfigurationId",
                    url="url"
                )],
                resource_id="resourceId",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75a0b1d34d977af6555f35f8e5de3877b3368ef3ca4c39da943111a6f5840b01)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument packaging_group_id", value=packaging_group_id, expected_type=type_hints["packaging_group_id"])
            check_type(argname="argument source_arn", value=source_arn, expected_type=type_hints["source_arn"])
            check_type(argname="argument source_role_arn", value=source_role_arn, expected_type=type_hints["source_role_arn"])
            check_type(argname="argument egress_endpoints", value=egress_endpoints, expected_type=type_hints["egress_endpoints"])
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
            "packaging_group_id": packaging_group_id,
            "source_arn": source_arn,
            "source_role_arn": source_role_arn,
        }
        if egress_endpoints is not None:
            self._values["egress_endpoints"] = egress_endpoints
        if resource_id is not None:
            self._values["resource_id"] = resource_id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def id(self) -> builtins.str:
        '''Unique identifier that you assign to the asset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-id
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def packaging_group_id(self) -> builtins.str:
        '''The ID of the packaging group associated with this asset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-packaginggroupid
        '''
        result = self._values.get("packaging_group_id")
        assert result is not None, "Required property 'packaging_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_arn(self) -> builtins.str:
        '''The ARN for the source content in Amazon S3.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-sourcearn
        '''
        result = self._values.get("source_arn")
        assert result is not None, "Required property 'source_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_role_arn(self) -> builtins.str:
        '''The ARN for the IAM role that provides AWS Elemental MediaPackage access to the Amazon S3 bucket where the source content is stored.

        Valid format: arn:aws:iam::{accountID}:role/{name}

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-sourcerolearn
        '''
        result = self._values.get("source_role_arn")
        assert result is not None, "Required property 'source_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def egress_endpoints(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAsset.EgressEndpointProperty]]]]:
        '''List of playback endpoints that are available for this asset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-egressendpoints
        '''
        result = self._values.get("egress_endpoints")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAsset.EgressEndpointProperty]]]], result)

    @builtins.property
    def resource_id(self) -> typing.Optional[builtins.str]:
        '''Unique identifier for this asset, as it's configured in the key provider service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-resourceid
        '''
        result = self._values.get("resource_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to assign to the asset.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-asset.html#cfn-mediapackage-asset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnChannel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediapackage.CfnChannel",
):
    '''Creates a channel to receive content.

    After it's created, a channel provides static input URLs. These URLs remain the same throughout the lifetime of the channel, regardless of any failures or upgrades that might occur. Use these URLs to configure the outputs of your upstream encoder.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediapackage as mediapackage
        
        cfn_channel = mediapackage.CfnChannel(self, "MyCfnChannel",
            id="id",
        
            # the properties below are optional
            description="description",
            egress_access_logs=mediapackage.CfnChannel.LogConfigurationProperty(
                log_group_name="logGroupName"
            ),
            hls_ingest=mediapackage.CfnChannel.HlsIngestProperty(
                ingest_endpoints=[mediapackage.CfnChannel.IngestEndpointProperty(
                    id="id",
                    password="password",
                    url="url",
                    username="username"
                )]
            ),
            ingress_access_logs=mediapackage.CfnChannel.LogConfigurationProperty(
                log_group_name="logGroupName"
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
        id_: builtins.str,
        *,
        id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        egress_access_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnChannel.LogConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        hls_ingest: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnChannel.HlsIngestProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ingress_access_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnChannel.LogConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id_: Construct identifier for this resource (unique in its scope).
        :param id: Unique identifier that you assign to the channel.
        :param description: Any descriptive information that you want to add to the channel for future identification purposes.
        :param egress_access_logs: Configures egress access logs.
        :param hls_ingest: The input URL where the source stream should be sent.
        :param ingress_access_logs: Configures ingress access logs.
        :param tags: The tags to assign to the channel.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__affeaf26cf4f8ef0e55a6096e7b94b296b27d02db77d19dbc77989422463b5f7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        props = CfnChannelProps(
            id=id,
            description=description,
            egress_access_logs=egress_access_logs,
            hls_ingest=hls_ingest,
            ingress_access_logs=ingress_access_logs,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id_, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a46a52d6dc51e43bc3260e55b89bbcfdda168c349ea724ce787a0fa6b5f0c0ae)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e92fe8ab8981412f0b93b05f876df2c0ea41b1e4cc736a04a5a927181c9c3611)
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
        '''The channel's unique system-generated resource name, based on the AWS record.

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
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''Unique identifier that you assign to the channel.'''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dfbfa5e60b31deabc06dac96485918d2f795cb0d3241ec09ac091e73b80a1a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Any descriptive information that you want to add to the channel for future identification purposes.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b5c758b0bb9f06dee32e08926740d41a3cce1b111f1626fa66ea6f82115cc16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="egressAccessLogs")
    def egress_access_logs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.LogConfigurationProperty"]]:
        '''Configures egress access logs.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.LogConfigurationProperty"]], jsii.get(self, "egressAccessLogs"))

    @egress_access_logs.setter
    def egress_access_logs(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.LogConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bf5b93815da3604606437071a85affcc9f8a576213172d6442244006725709c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "egressAccessLogs", value)

    @builtins.property
    @jsii.member(jsii_name="hlsIngest")
    def hls_ingest(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.HlsIngestProperty"]]:
        '''The input URL where the source stream should be sent.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.HlsIngestProperty"]], jsii.get(self, "hlsIngest"))

    @hls_ingest.setter
    def hls_ingest(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.HlsIngestProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd06c14ed9d8edf5f5e20f5cc9d6e0f82ce9226bf2682de8368e9134dfb2ecca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hlsIngest", value)

    @builtins.property
    @jsii.member(jsii_name="ingressAccessLogs")
    def ingress_access_logs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.LogConfigurationProperty"]]:
        '''Configures ingress access logs.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.LogConfigurationProperty"]], jsii.get(self, "ingressAccessLogs"))

    @ingress_access_logs.setter
    def ingress_access_logs(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnChannel.LogConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1eba56f28a4c29c9f6a1b3e1b6fce471204f7c3704ad8b8bfc70d8eea07dc4d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingressAccessLogs", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to assign to the channel.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffcf834ef6a826c28d9aa0d38721dbed5c74dbc38ca930c45f097c244fe6987c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnChannel.HlsIngestProperty",
        jsii_struct_bases=[],
        name_mapping={"ingest_endpoints": "ingestEndpoints"},
    )
    class HlsIngestProperty:
        def __init__(
            self,
            *,
            ingest_endpoints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnChannel.IngestEndpointProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''HLS ingest configuration.

            :param ingest_endpoints: The input URL where the source stream should be sent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-hlsingest.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                hls_ingest_property = mediapackage.CfnChannel.HlsIngestProperty(
                    ingest_endpoints=[mediapackage.CfnChannel.IngestEndpointProperty(
                        id="id",
                        password="password",
                        url="url",
                        username="username"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d8879f1cc6590d96234de60e9c45cd369821bc7c5aed33b342acff35c1254cac)
                check_type(argname="argument ingest_endpoints", value=ingest_endpoints, expected_type=type_hints["ingest_endpoints"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ingest_endpoints is not None:
                self._values["ingest_endpoints"] = ingest_endpoints

        @builtins.property
        def ingest_endpoints(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnChannel.IngestEndpointProperty"]]]]:
            '''The input URL where the source stream should be sent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-hlsingest.html#cfn-mediapackage-channel-hlsingest-ingestendpoints
            '''
            result = self._values.get("ingest_endpoints")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnChannel.IngestEndpointProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsIngestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnChannel.IngestEndpointProperty",
        jsii_struct_bases=[],
        name_mapping={
            "id": "id",
            "password": "password",
            "url": "url",
            "username": "username",
        },
    )
    class IngestEndpointProperty:
        def __init__(
            self,
            *,
            id: builtins.str,
            password: builtins.str,
            url: builtins.str,
            username: builtins.str,
        ) -> None:
            '''An endpoint for ingesting source content for a channel.

            :param id: The endpoint identifier.
            :param password: The system-generated password for WebDAV input authentication.
            :param url: The input URL where the source stream should be sent.
            :param username: The system-generated username for WebDAV input authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-ingestendpoint.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                ingest_endpoint_property = mediapackage.CfnChannel.IngestEndpointProperty(
                    id="id",
                    password="password",
                    url="url",
                    username="username"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4a0b9e94f252eb78a349be10dd707d652377ae6ccf636f5f08b2754b2de7260e)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument password", value=password, expected_type=type_hints["password"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
                check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
                "password": password,
                "url": url,
                "username": username,
            }

        @builtins.property
        def id(self) -> builtins.str:
            '''The endpoint identifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-ingestendpoint.html#cfn-mediapackage-channel-ingestendpoint-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def password(self) -> builtins.str:
            '''The system-generated password for WebDAV input authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-ingestendpoint.html#cfn-mediapackage-channel-ingestendpoint-password
            '''
            result = self._values.get("password")
            assert result is not None, "Required property 'password' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def url(self) -> builtins.str:
            '''The input URL where the source stream should be sent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-ingestendpoint.html#cfn-mediapackage-channel-ingestendpoint-url
            '''
            result = self._values.get("url")
            assert result is not None, "Required property 'url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def username(self) -> builtins.str:
            '''The system-generated username for WebDAV input authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-ingestendpoint.html#cfn-mediapackage-channel-ingestendpoint-username
            '''
            result = self._values.get("username")
            assert result is not None, "Required property 'username' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IngestEndpointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnChannel.LogConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_name": "logGroupName"},
    )
    class LogConfigurationProperty:
        def __init__(
            self,
            *,
            log_group_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The access log configuration parameters for your channel.

            :param log_group_name: Sets a custom Amazon CloudWatch log group name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-logconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                log_configuration_property = mediapackage.CfnChannel.LogConfigurationProperty(
                    log_group_name="logGroupName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5285b3c3196f5f3515543929d1ccf061692d47e8617d4ea53715cd2b0e00f85e)
                check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_group_name is not None:
                self._values["log_group_name"] = log_group_name

        @builtins.property
        def log_group_name(self) -> typing.Optional[builtins.str]:
            '''Sets a custom Amazon CloudWatch log group name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-channel-logconfiguration.html#cfn-mediapackage-channel-logconfiguration-loggroupname
            '''
            result = self._values.get("log_group_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediapackage.CfnChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "description": "description",
        "egress_access_logs": "egressAccessLogs",
        "hls_ingest": "hlsIngest",
        "ingress_access_logs": "ingressAccessLogs",
        "tags": "tags",
    },
)
class CfnChannelProps:
    def __init__(
        self,
        *,
        id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        egress_access_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.LogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        hls_ingest: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.HlsIngestProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        ingress_access_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.LogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnChannel``.

        :param id: Unique identifier that you assign to the channel.
        :param description: Any descriptive information that you want to add to the channel for future identification purposes.
        :param egress_access_logs: Configures egress access logs.
        :param hls_ingest: The input URL where the source stream should be sent.
        :param ingress_access_logs: Configures ingress access logs.
        :param tags: The tags to assign to the channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediapackage as mediapackage
            
            cfn_channel_props = mediapackage.CfnChannelProps(
                id="id",
            
                # the properties below are optional
                description="description",
                egress_access_logs=mediapackage.CfnChannel.LogConfigurationProperty(
                    log_group_name="logGroupName"
                ),
                hls_ingest=mediapackage.CfnChannel.HlsIngestProperty(
                    ingest_endpoints=[mediapackage.CfnChannel.IngestEndpointProperty(
                        id="id",
                        password="password",
                        url="url",
                        username="username"
                    )]
                ),
                ingress_access_logs=mediapackage.CfnChannel.LogConfigurationProperty(
                    log_group_name="logGroupName"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6608d4c68a49ca8e028b5d1d7da6506d3d11de3ed14a5a1bfcc17f851ffd06a5)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument egress_access_logs", value=egress_access_logs, expected_type=type_hints["egress_access_logs"])
            check_type(argname="argument hls_ingest", value=hls_ingest, expected_type=type_hints["hls_ingest"])
            check_type(argname="argument ingress_access_logs", value=ingress_access_logs, expected_type=type_hints["ingress_access_logs"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
        }
        if description is not None:
            self._values["description"] = description
        if egress_access_logs is not None:
            self._values["egress_access_logs"] = egress_access_logs
        if hls_ingest is not None:
            self._values["hls_ingest"] = hls_ingest
        if ingress_access_logs is not None:
            self._values["ingress_access_logs"] = ingress_access_logs
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def id(self) -> builtins.str:
        '''Unique identifier that you assign to the channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-id
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Any descriptive information that you want to add to the channel for future identification purposes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def egress_access_logs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnChannel.LogConfigurationProperty]]:
        '''Configures egress access logs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-egressaccesslogs
        '''
        result = self._values.get("egress_access_logs")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnChannel.LogConfigurationProperty]], result)

    @builtins.property
    def hls_ingest(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnChannel.HlsIngestProperty]]:
        '''The input URL where the source stream should be sent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-hlsingest
        '''
        result = self._values.get("hls_ingest")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnChannel.HlsIngestProperty]], result)

    @builtins.property
    def ingress_access_logs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnChannel.LogConfigurationProperty]]:
        '''Configures ingress access logs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-ingressaccesslogs
        '''
        result = self._values.get("ingress_access_logs")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnChannel.LogConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to assign to the channel.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html#cfn-mediapackage-channel-tags
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
class CfnOriginEndpoint(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediapackage.CfnOriginEndpoint",
):
    '''Create an endpoint on an AWS Elemental MediaPackage channel.

    An endpoint represents a single delivery point of a channel, and defines content output handling through various components, such as packaging protocols, DRM and encryption integration, and more.

    After it's created, an endpoint provides a fixed public URL. This URL remains the same throughout the lifetime of the endpoint, regardless of any failures or upgrades that might occur. Integrate the URL with a downstream CDN (such as Amazon CloudFront) or playback device.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediapackage as mediapackage
        
        cfn_origin_endpoint = mediapackage.CfnOriginEndpoint(self, "MyCfnOriginEndpoint",
            channel_id="channelId",
            id="id",
        
            # the properties below are optional
            authorization=mediapackage.CfnOriginEndpoint.AuthorizationProperty(
                cdn_identifier_secret="cdnIdentifierSecret",
                secrets_role_arn="secretsRoleArn"
            ),
            cmaf_package=mediapackage.CfnOriginEndpoint.CmafPackageProperty(
                encryption=mediapackage.CfnOriginEndpoint.CmafEncryptionProperty(
                    speke_key_provider=mediapackage.CfnOriginEndpoint.SpekeKeyProviderProperty(
                        resource_id="resourceId",
                        role_arn="roleArn",
                        system_ids=["systemIds"],
                        url="url",
        
                        # the properties below are optional
                        certificate_arn="certificateArn",
                        encryption_contract_configuration=mediapackage.CfnOriginEndpoint.EncryptionContractConfigurationProperty(
                            preset_speke20_audio="presetSpeke20Audio",
                            preset_speke20_video="presetSpeke20Video"
                        )
                    ),
        
                    # the properties below are optional
                    constant_initialization_vector="constantInitializationVector",
                    encryption_method="encryptionMethod",
                    key_rotation_interval_seconds=123
                ),
                hls_manifests=[mediapackage.CfnOriginEndpoint.HlsManifestProperty(
                    id="id",
        
                    # the properties below are optional
                    ad_markers="adMarkers",
                    ads_on_delivery_restrictions="adsOnDeliveryRestrictions",
                    ad_triggers=["adTriggers"],
                    include_iframe_only_stream=False,
                    manifest_name="manifestName",
                    playlist_type="playlistType",
                    playlist_window_seconds=123,
                    program_date_time_interval_seconds=123,
                    url="url"
                )],
                segment_duration_seconds=123,
                segment_prefix="segmentPrefix",
                stream_selection=mediapackage.CfnOriginEndpoint.StreamSelectionProperty(
                    max_video_bits_per_second=123,
                    min_video_bits_per_second=123,
                    stream_order="streamOrder"
                )
            ),
            dash_package=mediapackage.CfnOriginEndpoint.DashPackageProperty(
                ads_on_delivery_restrictions="adsOnDeliveryRestrictions",
                ad_triggers=["adTriggers"],
                encryption=mediapackage.CfnOriginEndpoint.DashEncryptionProperty(
                    speke_key_provider=mediapackage.CfnOriginEndpoint.SpekeKeyProviderProperty(
                        resource_id="resourceId",
                        role_arn="roleArn",
                        system_ids=["systemIds"],
                        url="url",
        
                        # the properties below are optional
                        certificate_arn="certificateArn",
                        encryption_contract_configuration=mediapackage.CfnOriginEndpoint.EncryptionContractConfigurationProperty(
                            preset_speke20_audio="presetSpeke20Audio",
                            preset_speke20_video="presetSpeke20Video"
                        )
                    ),
        
                    # the properties below are optional
                    key_rotation_interval_seconds=123
                ),
                include_iframe_only_stream=False,
                manifest_layout="manifestLayout",
                manifest_window_seconds=123,
                min_buffer_time_seconds=123,
                min_update_period_seconds=123,
                period_triggers=["periodTriggers"],
                profile="profile",
                segment_duration_seconds=123,
                segment_template_format="segmentTemplateFormat",
                stream_selection=mediapackage.CfnOriginEndpoint.StreamSelectionProperty(
                    max_video_bits_per_second=123,
                    min_video_bits_per_second=123,
                    stream_order="streamOrder"
                ),
                suggested_presentation_delay_seconds=123,
                utc_timing="utcTiming",
                utc_timing_uri="utcTimingUri"
            ),
            description="description",
            hls_package=mediapackage.CfnOriginEndpoint.HlsPackageProperty(
                ad_markers="adMarkers",
                ads_on_delivery_restrictions="adsOnDeliveryRestrictions",
                ad_triggers=["adTriggers"],
                encryption=mediapackage.CfnOriginEndpoint.HlsEncryptionProperty(
                    speke_key_provider=mediapackage.CfnOriginEndpoint.SpekeKeyProviderProperty(
                        resource_id="resourceId",
                        role_arn="roleArn",
                        system_ids=["systemIds"],
                        url="url",
        
                        # the properties below are optional
                        certificate_arn="certificateArn",
                        encryption_contract_configuration=mediapackage.CfnOriginEndpoint.EncryptionContractConfigurationProperty(
                            preset_speke20_audio="presetSpeke20Audio",
                            preset_speke20_video="presetSpeke20Video"
                        )
                    ),
        
                    # the properties below are optional
                    constant_initialization_vector="constantInitializationVector",
                    encryption_method="encryptionMethod",
                    key_rotation_interval_seconds=123,
                    repeat_ext_xKey=False
                ),
                include_dvb_subtitles=False,
                include_iframe_only_stream=False,
                playlist_type="playlistType",
                playlist_window_seconds=123,
                program_date_time_interval_seconds=123,
                segment_duration_seconds=123,
                stream_selection=mediapackage.CfnOriginEndpoint.StreamSelectionProperty(
                    max_video_bits_per_second=123,
                    min_video_bits_per_second=123,
                    stream_order="streamOrder"
                ),
                use_audio_rendition_group=False
            ),
            manifest_name="manifestName",
            mss_package=mediapackage.CfnOriginEndpoint.MssPackageProperty(
                encryption=mediapackage.CfnOriginEndpoint.MssEncryptionProperty(
                    speke_key_provider=mediapackage.CfnOriginEndpoint.SpekeKeyProviderProperty(
                        resource_id="resourceId",
                        role_arn="roleArn",
                        system_ids=["systemIds"],
                        url="url",
        
                        # the properties below are optional
                        certificate_arn="certificateArn",
                        encryption_contract_configuration=mediapackage.CfnOriginEndpoint.EncryptionContractConfigurationProperty(
                            preset_speke20_audio="presetSpeke20Audio",
                            preset_speke20_video="presetSpeke20Video"
                        )
                    )
                ),
                manifest_window_seconds=123,
                segment_duration_seconds=123,
                stream_selection=mediapackage.CfnOriginEndpoint.StreamSelectionProperty(
                    max_video_bits_per_second=123,
                    min_video_bits_per_second=123,
                    stream_order="streamOrder"
                )
            ),
            origination="origination",
            startover_window_seconds=123,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            time_delay_seconds=123,
            whitelist=["whitelist"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        channel_id: builtins.str,
        id: builtins.str,
        authorization: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.AuthorizationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        cmaf_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.CmafPackageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        dash_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.DashPackageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        hls_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.HlsPackageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        manifest_name: typing.Optional[builtins.str] = None,
        mss_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.MssPackageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        origination: typing.Optional[builtins.str] = None,
        startover_window_seconds: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        time_delay_seconds: typing.Optional[jsii.Number] = None,
        whitelist: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id_: Construct identifier for this resource (unique in its scope).
        :param channel_id: The ID of the channel associated with this endpoint.
        :param id: The manifest ID is required and must be unique within the OriginEndpoint. The ID can't be changed after the endpoint is created.
        :param authorization: Parameters for CDN authorization.
        :param cmaf_package: Parameters for Common Media Application Format (CMAF) packaging.
        :param dash_package: Parameters for DASH packaging.
        :param description: Any descriptive information that you want to add to the endpoint for future identification purposes.
        :param hls_package: Parameters for Apple HLS packaging.
        :param manifest_name: A short string that's appended to the end of the endpoint URL to create a unique path to this endpoint.
        :param mss_package: Parameters for Microsoft Smooth Streaming packaging.
        :param origination: Controls video origination from this endpoint. Valid values: - ``ALLOW`` - enables this endpoint to serve content to requesting devices. - ``DENY`` - prevents this endpoint from serving content. Denying origination is helpful for harvesting live-to-VOD assets. For more information about harvesting and origination, see `Live-to-VOD Requirements <https://docs.aws.amazon.com/mediapackage/latest/ug/ltov-reqmts.html>`_ .
        :param startover_window_seconds: Maximum duration (seconds) of content to retain for startover playback. Omit this attribute or enter ``0`` to indicate that startover playback is disabled for this endpoint.
        :param tags: The tags to assign to the endpoint.
        :param time_delay_seconds: Minimum duration (seconds) of delay to enforce on the playback of live content. Omit this attribute or enter ``0`` to indicate that there is no time delay in effect for this endpoint.
        :param whitelist: The IP addresses that can access this endpoint.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01f85bb3acbb258c87305e632e7d154966949216428ef553b6c3235e01417aa8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        props = CfnOriginEndpointProps(
            channel_id=channel_id,
            id=id,
            authorization=authorization,
            cmaf_package=cmaf_package,
            dash_package=dash_package,
            description=description,
            hls_package=hls_package,
            manifest_name=manifest_name,
            mss_package=mss_package,
            origination=origination,
            startover_window_seconds=startover_window_seconds,
            tags=tags,
            time_delay_seconds=time_delay_seconds,
            whitelist=whitelist,
        )

        jsii.create(self.__class__, self, [scope, id_, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3478aec9c15e91156fc03894a528b9f2055b88884d84bcb16fa53310f28c4cf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f55a0e1543c341d60565427fa11f8fd24cd6bd09fe56ce62c8e50d2a9a3b8535)
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
        '''The endpoint's unique system-generated resource name, based on the AWS record.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrUrl")
    def attr_url(self) -> builtins.str:
        '''URL for the key provider’s key retrieval API endpoint.

        Must start with https://.

        :cloudformationAttribute: Url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUrl"))

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
    @jsii.member(jsii_name="channelId")
    def channel_id(self) -> builtins.str:
        '''The ID of the channel associated with this endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "channelId"))

    @channel_id.setter
    def channel_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be0b35a7d39f22a922e6d2806701c97a79583ed4cd380349683d0ae31a09565e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channelId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''The manifest ID is required and must be unique within the OriginEndpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99a06c257b6797d9aae3bd64d6eeb55571af3841b86e1ad7d2980726f85a9dc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="authorization")
    def authorization(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.AuthorizationProperty"]]:
        '''Parameters for CDN authorization.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.AuthorizationProperty"]], jsii.get(self, "authorization"))

    @authorization.setter
    def authorization(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.AuthorizationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__156ab3ebea5a8eacd612f1583257bbe7850d21712c1c3dcd5447fd36f76d3ba2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorization", value)

    @builtins.property
    @jsii.member(jsii_name="cmafPackage")
    def cmaf_package(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.CmafPackageProperty"]]:
        '''Parameters for Common Media Application Format (CMAF) packaging.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.CmafPackageProperty"]], jsii.get(self, "cmafPackage"))

    @cmaf_package.setter
    def cmaf_package(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.CmafPackageProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25473ff4d9f0fbc872a9885f718995cbcc6ad16528e432dfbadeb748e4129584)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cmafPackage", value)

    @builtins.property
    @jsii.member(jsii_name="dashPackage")
    def dash_package(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.DashPackageProperty"]]:
        '''Parameters for DASH packaging.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.DashPackageProperty"]], jsii.get(self, "dashPackage"))

    @dash_package.setter
    def dash_package(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.DashPackageProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0c2c45ab2e510dd522ccbc5accd0905f0fc2d460bf6760ffc34e1a0ce8652f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dashPackage", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Any descriptive information that you want to add to the endpoint for future identification purposes.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12d8129533cd4dccc4d114bda308471faa5a22dd061a8c8efe51e6bbe12d5a51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="hlsPackage")
    def hls_package(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.HlsPackageProperty"]]:
        '''Parameters for Apple HLS packaging.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.HlsPackageProperty"]], jsii.get(self, "hlsPackage"))

    @hls_package.setter
    def hls_package(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.HlsPackageProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65497669bad52e91563221a8604146d8b2b151a2211a913fabce3fd05beb01df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hlsPackage", value)

    @builtins.property
    @jsii.member(jsii_name="manifestName")
    def manifest_name(self) -> typing.Optional[builtins.str]:
        '''A short string that's appended to the end of the endpoint URL to create a unique path to this endpoint.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "manifestName"))

    @manifest_name.setter
    def manifest_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee8a6384d559f558cfc96a8adbf44f42b4b89ad14cf509a9bb35857f61b20531)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manifestName", value)

    @builtins.property
    @jsii.member(jsii_name="mssPackage")
    def mss_package(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.MssPackageProperty"]]:
        '''Parameters for Microsoft Smooth Streaming packaging.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.MssPackageProperty"]], jsii.get(self, "mssPackage"))

    @mss_package.setter
    def mss_package(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.MssPackageProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5b207fa4f25365ce14c50d90586150f16e19390170ef5cbd3169b1037eace1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mssPackage", value)

    @builtins.property
    @jsii.member(jsii_name="origination")
    def origination(self) -> typing.Optional[builtins.str]:
        '''Controls video origination from this endpoint.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "origination"))

    @origination.setter
    def origination(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7d8c8b852ebe894d61bc71a445d8ac7e24da974818f025c346a33de8083a9b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "origination", value)

    @builtins.property
    @jsii.member(jsii_name="startoverWindowSeconds")
    def startover_window_seconds(self) -> typing.Optional[jsii.Number]:
        '''Maximum duration (seconds) of content to retain for startover playback.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startoverWindowSeconds"))

    @startover_window_seconds.setter
    def startover_window_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c528046b9214a04549830faf062051f7418fc9517ba9c6c4a5e6dd283f7850b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startoverWindowSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to assign to the endpoint.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61e0125a3a7672d5a1bf2f0e24eb93f48b6dd949a3c5d94bda3997afcde3e15a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="timeDelaySeconds")
    def time_delay_seconds(self) -> typing.Optional[jsii.Number]:
        '''Minimum duration (seconds) of delay to enforce on the playback of live content.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeDelaySeconds"))

    @time_delay_seconds.setter
    def time_delay_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af85b805197b1d411c4fd747d0ac4e2468574569f1fdb2926834a94c4da3c0f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeDelaySeconds", value)

    @builtins.property
    @jsii.member(jsii_name="whitelist")
    def whitelist(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The IP addresses that can access this endpoint.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "whitelist"))

    @whitelist.setter
    def whitelist(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cabc2520080e09c3795d546475e7a04bb502f05de10623e2eaf44596dffcf971)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "whitelist", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnOriginEndpoint.AuthorizationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cdn_identifier_secret": "cdnIdentifierSecret",
            "secrets_role_arn": "secretsRoleArn",
        },
    )
    class AuthorizationProperty:
        def __init__(
            self,
            *,
            cdn_identifier_secret: builtins.str,
            secrets_role_arn: builtins.str,
        ) -> None:
            '''Parameters for enabling CDN authorization on the endpoint.

            :param cdn_identifier_secret: The Amazon Resource Name (ARN) for the secret in AWS Secrets Manager that your Content Delivery Network (CDN) uses for authorization to access your endpoint.
            :param secrets_role_arn: The Amazon Resource Name (ARN) for the IAM role that allows AWS Elemental MediaPackage to communicate with AWS Secrets Manager .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-authorization.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                authorization_property = mediapackage.CfnOriginEndpoint.AuthorizationProperty(
                    cdn_identifier_secret="cdnIdentifierSecret",
                    secrets_role_arn="secretsRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d25e4ac516c5e88a584ad88a9eff22ac7db2bb6285c6ee8d81d5ec6d823bf9ef)
                check_type(argname="argument cdn_identifier_secret", value=cdn_identifier_secret, expected_type=type_hints["cdn_identifier_secret"])
                check_type(argname="argument secrets_role_arn", value=secrets_role_arn, expected_type=type_hints["secrets_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cdn_identifier_secret": cdn_identifier_secret,
                "secrets_role_arn": secrets_role_arn,
            }

        @builtins.property
        def cdn_identifier_secret(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) for the secret in AWS Secrets Manager that your Content Delivery Network (CDN) uses for authorization to access your endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-authorization.html#cfn-mediapackage-originendpoint-authorization-cdnidentifiersecret
            '''
            result = self._values.get("cdn_identifier_secret")
            assert result is not None, "Required property 'cdn_identifier_secret' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secrets_role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) for the IAM role that allows AWS Elemental MediaPackage to communicate with AWS Secrets Manager .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-authorization.html#cfn-mediapackage-originendpoint-authorization-secretsrolearn
            '''
            result = self._values.get("secrets_role_arn")
            assert result is not None, "Required property 'secrets_role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthorizationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnOriginEndpoint.CmafEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "speke_key_provider": "spekeKeyProvider",
            "constant_initialization_vector": "constantInitializationVector",
            "encryption_method": "encryptionMethod",
            "key_rotation_interval_seconds": "keyRotationIntervalSeconds",
        },
    )
    class CmafEncryptionProperty:
        def __init__(
            self,
            *,
            speke_key_provider: typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.SpekeKeyProviderProperty", typing.Dict[builtins.str, typing.Any]]],
            constant_initialization_vector: typing.Optional[builtins.str] = None,
            encryption_method: typing.Optional[builtins.str] = None,
            key_rotation_interval_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Holds encryption information so that access to the content can be controlled by a DRM solution.

            :param speke_key_provider: Parameters for the SPEKE key provider.
            :param constant_initialization_vector: An optional 128-bit, 16-byte hex value represented by a 32-character string, used in conjunction with the key for encrypting blocks. If you don't specify a value, then AWS Elemental MediaPackage creates the constant initialization vector (IV).
            :param encryption_method: The encryption method to use.
            :param key_rotation_interval_seconds: Number of seconds before AWS Elemental MediaPackage rotates to a new key. By default, rotation is set to 60 seconds. Set to ``0`` to disable key rotation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafencryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                cmaf_encryption_property = mediapackage.CfnOriginEndpoint.CmafEncryptionProperty(
                    speke_key_provider=mediapackage.CfnOriginEndpoint.SpekeKeyProviderProperty(
                        resource_id="resourceId",
                        role_arn="roleArn",
                        system_ids=["systemIds"],
                        url="url",
                
                        # the properties below are optional
                        certificate_arn="certificateArn",
                        encryption_contract_configuration=mediapackage.CfnOriginEndpoint.EncryptionContractConfigurationProperty(
                            preset_speke20_audio="presetSpeke20Audio",
                            preset_speke20_video="presetSpeke20Video"
                        )
                    ),
                
                    # the properties below are optional
                    constant_initialization_vector="constantInitializationVector",
                    encryption_method="encryptionMethod",
                    key_rotation_interval_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__665a104be1b3a19db35ae8236df5a37f409cede911767d94187e4c949dd198e9)
                check_type(argname="argument speke_key_provider", value=speke_key_provider, expected_type=type_hints["speke_key_provider"])
                check_type(argname="argument constant_initialization_vector", value=constant_initialization_vector, expected_type=type_hints["constant_initialization_vector"])
                check_type(argname="argument encryption_method", value=encryption_method, expected_type=type_hints["encryption_method"])
                check_type(argname="argument key_rotation_interval_seconds", value=key_rotation_interval_seconds, expected_type=type_hints["key_rotation_interval_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "speke_key_provider": speke_key_provider,
            }
            if constant_initialization_vector is not None:
                self._values["constant_initialization_vector"] = constant_initialization_vector
            if encryption_method is not None:
                self._values["encryption_method"] = encryption_method
            if key_rotation_interval_seconds is not None:
                self._values["key_rotation_interval_seconds"] = key_rotation_interval_seconds

        @builtins.property
        def speke_key_provider(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.SpekeKeyProviderProperty"]:
            '''Parameters for the SPEKE key provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafencryption.html#cfn-mediapackage-originendpoint-cmafencryption-spekekeyprovider
            '''
            result = self._values.get("speke_key_provider")
            assert result is not None, "Required property 'speke_key_provider' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.SpekeKeyProviderProperty"], result)

        @builtins.property
        def constant_initialization_vector(self) -> typing.Optional[builtins.str]:
            '''An optional 128-bit, 16-byte hex value represented by a 32-character string, used in conjunction with the key for encrypting blocks.

            If you don't specify a value, then AWS Elemental MediaPackage creates the constant initialization vector (IV).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafencryption.html#cfn-mediapackage-originendpoint-cmafencryption-constantinitializationvector
            '''
            result = self._values.get("constant_initialization_vector")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def encryption_method(self) -> typing.Optional[builtins.str]:
            '''The encryption method to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafencryption.html#cfn-mediapackage-originendpoint-cmafencryption-encryptionmethod
            '''
            result = self._values.get("encryption_method")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key_rotation_interval_seconds(self) -> typing.Optional[jsii.Number]:
            '''Number of seconds before AWS Elemental MediaPackage rotates to a new key.

            By default, rotation is set to 60 seconds. Set to ``0`` to disable key rotation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafencryption.html#cfn-mediapackage-originendpoint-cmafencryption-keyrotationintervalseconds
            '''
            result = self._values.get("key_rotation_interval_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CmafEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnOriginEndpoint.CmafPackageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption": "encryption",
            "hls_manifests": "hlsManifests",
            "segment_duration_seconds": "segmentDurationSeconds",
            "segment_prefix": "segmentPrefix",
            "stream_selection": "streamSelection",
        },
    )
    class CmafPackageProperty:
        def __init__(
            self,
            *,
            encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.CmafEncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            hls_manifests: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.HlsManifestProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            segment_duration_seconds: typing.Optional[jsii.Number] = None,
            segment_prefix: typing.Optional[builtins.str] = None,
            stream_selection: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.StreamSelectionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Parameters for Common Media Application Format (CMAF) packaging.

            :param encryption: Parameters for encrypting content.
            :param hls_manifests: A list of HLS manifest configurations that are available from this endpoint.
            :param segment_duration_seconds: Duration (in seconds) of each segment. Actual segments are rounded to the nearest multiple of the source segment duration.
            :param segment_prefix: An optional custom string that is prepended to the name of each segment. If not specified, the segment prefix defaults to the ChannelId.
            :param stream_selection: Limitations for outputs from the endpoint, based on the video bitrate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                cmaf_package_property = mediapackage.CfnOriginEndpoint.CmafPackageProperty(
                    encryption=mediapackage.CfnOriginEndpoint.CmafEncryptionProperty(
                        speke_key_provider=mediapackage.CfnOriginEndpoint.SpekeKeyProviderProperty(
                            resource_id="resourceId",
                            role_arn="roleArn",
                            system_ids=["systemIds"],
                            url="url",
                
                            # the properties below are optional
                            certificate_arn="certificateArn",
                            encryption_contract_configuration=mediapackage.CfnOriginEndpoint.EncryptionContractConfigurationProperty(
                                preset_speke20_audio="presetSpeke20Audio",
                                preset_speke20_video="presetSpeke20Video"
                            )
                        ),
                
                        # the properties below are optional
                        constant_initialization_vector="constantInitializationVector",
                        encryption_method="encryptionMethod",
                        key_rotation_interval_seconds=123
                    ),
                    hls_manifests=[mediapackage.CfnOriginEndpoint.HlsManifestProperty(
                        id="id",
                
                        # the properties below are optional
                        ad_markers="adMarkers",
                        ads_on_delivery_restrictions="adsOnDeliveryRestrictions",
                        ad_triggers=["adTriggers"],
                        include_iframe_only_stream=False,
                        manifest_name="manifestName",
                        playlist_type="playlistType",
                        playlist_window_seconds=123,
                        program_date_time_interval_seconds=123,
                        url="url"
                    )],
                    segment_duration_seconds=123,
                    segment_prefix="segmentPrefix",
                    stream_selection=mediapackage.CfnOriginEndpoint.StreamSelectionProperty(
                        max_video_bits_per_second=123,
                        min_video_bits_per_second=123,
                        stream_order="streamOrder"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a2d9ac49bc2a414f54d7fa4069dc81be30a81c60a1a099ba1f19e415e6295078)
                check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
                check_type(argname="argument hls_manifests", value=hls_manifests, expected_type=type_hints["hls_manifests"])
                check_type(argname="argument segment_duration_seconds", value=segment_duration_seconds, expected_type=type_hints["segment_duration_seconds"])
                check_type(argname="argument segment_prefix", value=segment_prefix, expected_type=type_hints["segment_prefix"])
                check_type(argname="argument stream_selection", value=stream_selection, expected_type=type_hints["stream_selection"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if encryption is not None:
                self._values["encryption"] = encryption
            if hls_manifests is not None:
                self._values["hls_manifests"] = hls_manifests
            if segment_duration_seconds is not None:
                self._values["segment_duration_seconds"] = segment_duration_seconds
            if segment_prefix is not None:
                self._values["segment_prefix"] = segment_prefix
            if stream_selection is not None:
                self._values["stream_selection"] = stream_selection

        @builtins.property
        def encryption(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.CmafEncryptionProperty"]]:
            '''Parameters for encrypting content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html#cfn-mediapackage-originendpoint-cmafpackage-encryption
            '''
            result = self._values.get("encryption")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.CmafEncryptionProperty"]], result)

        @builtins.property
        def hls_manifests(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.HlsManifestProperty"]]]]:
            '''A list of HLS manifest configurations that are available from this endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html#cfn-mediapackage-originendpoint-cmafpackage-hlsmanifests
            '''
            result = self._values.get("hls_manifests")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.HlsManifestProperty"]]]], result)

        @builtins.property
        def segment_duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''Duration (in seconds) of each segment.

            Actual segments are rounded to the nearest multiple of the source segment duration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html#cfn-mediapackage-originendpoint-cmafpackage-segmentdurationseconds
            '''
            result = self._values.get("segment_duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def segment_prefix(self) -> typing.Optional[builtins.str]:
            '''An optional custom string that is prepended to the name of each segment.

            If not specified, the segment prefix defaults to the ChannelId.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html#cfn-mediapackage-originendpoint-cmafpackage-segmentprefix
            '''
            result = self._values.get("segment_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def stream_selection(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.StreamSelectionProperty"]]:
            '''Limitations for outputs from the endpoint, based on the video bitrate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-cmafpackage.html#cfn-mediapackage-originendpoint-cmafpackage-streamselection
            '''
            result = self._values.get("stream_selection")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.StreamSelectionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CmafPackageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnOriginEndpoint.DashEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "speke_key_provider": "spekeKeyProvider",
            "key_rotation_interval_seconds": "keyRotationIntervalSeconds",
        },
    )
    class DashEncryptionProperty:
        def __init__(
            self,
            *,
            speke_key_provider: typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.SpekeKeyProviderProperty", typing.Dict[builtins.str, typing.Any]]],
            key_rotation_interval_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Holds encryption information so that access to the content can be controlled by a DRM solution.

            :param speke_key_provider: Parameters for the SPEKE key provider.
            :param key_rotation_interval_seconds: Number of seconds before AWS Elemental MediaPackage rotates to a new key. By default, rotation is set to 60 seconds. Set to ``0`` to disable key rotation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashencryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                dash_encryption_property = mediapackage.CfnOriginEndpoint.DashEncryptionProperty(
                    speke_key_provider=mediapackage.CfnOriginEndpoint.SpekeKeyProviderProperty(
                        resource_id="resourceId",
                        role_arn="roleArn",
                        system_ids=["systemIds"],
                        url="url",
                
                        # the properties below are optional
                        certificate_arn="certificateArn",
                        encryption_contract_configuration=mediapackage.CfnOriginEndpoint.EncryptionContractConfigurationProperty(
                            preset_speke20_audio="presetSpeke20Audio",
                            preset_speke20_video="presetSpeke20Video"
                        )
                    ),
                
                    # the properties below are optional
                    key_rotation_interval_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2f56c756b424a8b673433bbd23b0af6d3a73ae1da9d39c6467efe26215ce4980)
                check_type(argname="argument speke_key_provider", value=speke_key_provider, expected_type=type_hints["speke_key_provider"])
                check_type(argname="argument key_rotation_interval_seconds", value=key_rotation_interval_seconds, expected_type=type_hints["key_rotation_interval_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "speke_key_provider": speke_key_provider,
            }
            if key_rotation_interval_seconds is not None:
                self._values["key_rotation_interval_seconds"] = key_rotation_interval_seconds

        @builtins.property
        def speke_key_provider(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.SpekeKeyProviderProperty"]:
            '''Parameters for the SPEKE key provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashencryption.html#cfn-mediapackage-originendpoint-dashencryption-spekekeyprovider
            '''
            result = self._values.get("speke_key_provider")
            assert result is not None, "Required property 'speke_key_provider' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.SpekeKeyProviderProperty"], result)

        @builtins.property
        def key_rotation_interval_seconds(self) -> typing.Optional[jsii.Number]:
            '''Number of seconds before AWS Elemental MediaPackage rotates to a new key.

            By default, rotation is set to 60 seconds. Set to ``0`` to disable key rotation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashencryption.html#cfn-mediapackage-originendpoint-dashencryption-keyrotationintervalseconds
            '''
            result = self._values.get("key_rotation_interval_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnOriginEndpoint.DashPackageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ads_on_delivery_restrictions": "adsOnDeliveryRestrictions",
            "ad_triggers": "adTriggers",
            "encryption": "encryption",
            "include_iframe_only_stream": "includeIframeOnlyStream",
            "manifest_layout": "manifestLayout",
            "manifest_window_seconds": "manifestWindowSeconds",
            "min_buffer_time_seconds": "minBufferTimeSeconds",
            "min_update_period_seconds": "minUpdatePeriodSeconds",
            "period_triggers": "periodTriggers",
            "profile": "profile",
            "segment_duration_seconds": "segmentDurationSeconds",
            "segment_template_format": "segmentTemplateFormat",
            "stream_selection": "streamSelection",
            "suggested_presentation_delay_seconds": "suggestedPresentationDelaySeconds",
            "utc_timing": "utcTiming",
            "utc_timing_uri": "utcTimingUri",
        },
    )
    class DashPackageProperty:
        def __init__(
            self,
            *,
            ads_on_delivery_restrictions: typing.Optional[builtins.str] = None,
            ad_triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
            encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.DashEncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            include_iframe_only_stream: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            manifest_layout: typing.Optional[builtins.str] = None,
            manifest_window_seconds: typing.Optional[jsii.Number] = None,
            min_buffer_time_seconds: typing.Optional[jsii.Number] = None,
            min_update_period_seconds: typing.Optional[jsii.Number] = None,
            period_triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
            profile: typing.Optional[builtins.str] = None,
            segment_duration_seconds: typing.Optional[jsii.Number] = None,
            segment_template_format: typing.Optional[builtins.str] = None,
            stream_selection: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.StreamSelectionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            suggested_presentation_delay_seconds: typing.Optional[jsii.Number] = None,
            utc_timing: typing.Optional[builtins.str] = None,
            utc_timing_uri: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Parameters for DASH packaging.

            :param ads_on_delivery_restrictions: The flags on SCTE-35 segmentation descriptors that have to be present for AWS Elemental MediaPackage to insert ad markers in the output manifest. For information about SCTE-35 in AWS Elemental MediaPackage , see `SCTE-35 Message Options in AWS Elemental MediaPackage <https://docs.aws.amazon.com/mediapackage/latest/ug/scte.html>`_ .
            :param ad_triggers: Specifies the SCTE-35 message types that AWS Elemental MediaPackage treats as ad markers in the output manifest. Valid values: - ``BREAK`` - ``DISTRIBUTOR_ADVERTISEMENT`` - ``DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY`` . - ``DISTRIBUTOR_PLACEMENT_OPPORTUNITY`` . - ``PROVIDER_ADVERTISEMENT`` . - ``PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY`` . - ``PROVIDER_PLACEMENT_OPPORTUNITY`` . - ``SPLICE_INSERT`` .
            :param encryption: Parameters for encrypting content.
            :param include_iframe_only_stream: This applies only to stream sets with a single video track. When true, the stream set includes an additional I-frame trick-play only stream, along with the other tracks. If false, this extra stream is not included.
            :param manifest_layout: Determines the position of some tags in the manifest. Valid values: - ``FULL`` - Elements like ``SegmentTemplate`` and ``ContentProtection`` are included in each ``Representation`` . - ``COMPACT`` - Duplicate elements are combined and presented at the ``AdaptationSet`` level.
            :param manifest_window_seconds: Time window (in seconds) contained in each manifest.
            :param min_buffer_time_seconds: Minimum amount of content (measured in seconds) that a player must keep available in the buffer.
            :param min_update_period_seconds: Minimum amount of time (in seconds) that the player should wait before requesting updates to the manifest.
            :param period_triggers: Controls whether AWS Elemental MediaPackage produces single-period or multi-period DASH manifests. For more information about periods, see `Multi-period DASH in AWS Elemental MediaPackage <https://docs.aws.amazon.com/mediapackage/latest/ug/multi-period.html>`_ . Valid values: - ``ADS`` - AWS Elemental MediaPackage will produce multi-period DASH manifests. Periods are created based on the SCTE-35 ad markers present in the input manifest. - *No value* - AWS Elemental MediaPackage will produce single-period DASH manifests. This is the default setting.
            :param profile: The DASH profile for the output. Valid values: - ``NONE`` - The output doesn't use a DASH profile. - ``HBBTV_1_5`` - The output is compliant with HbbTV v1.5. - ``DVB_DASH_2014`` - The output is compliant with DVB-DASH 2014.
            :param segment_duration_seconds: Duration (in seconds) of each fragment. Actual fragments are rounded to the nearest multiple of the source fragment duration.
            :param segment_template_format: Determines the type of variable used in the ``media`` URL of the ``SegmentTemplate`` tag in the manifest. Also specifies if segment timeline information is included in ``SegmentTimeline`` or ``SegmentTemplate`` . Valid values: - ``NUMBER_WITH_TIMELINE`` - The ``$Number$`` variable is used in the ``media`` URL. The value of this variable is the sequential number of the segment. A full ``SegmentTimeline`` object is presented in each ``SegmentTemplate`` . - ``NUMBER_WITH_DURATION`` - The ``$Number$`` variable is used in the ``media`` URL and a ``duration`` attribute is added to the segment template. The ``SegmentTimeline`` object is removed from the representation. - ``TIME_WITH_TIMELINE`` - The ``$Time$`` variable is used in the ``media`` URL. The value of this variable is the timestamp of when the segment starts. A full ``SegmentTimeline`` object is presented in each ``SegmentTemplate`` .
            :param stream_selection: Limitations for outputs from the endpoint, based on the video bitrate.
            :param suggested_presentation_delay_seconds: Amount of time (in seconds) that the player should be from the live point at the end of the manifest.
            :param utc_timing: Determines the type of UTC timing included in the DASH Media Presentation Description (MPD).
            :param utc_timing_uri: Specifies the value attribute of the UTC timing field when utcTiming is set to HTTP-ISO or HTTP-HEAD.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                dash_package_property = mediapackage.CfnOriginEndpoint.DashPackageProperty(
                    ads_on_delivery_restrictions="adsOnDeliveryRestrictions",
                    ad_triggers=["adTriggers"],
                    encryption=mediapackage.CfnOriginEndpoint.DashEncryptionProperty(
                        speke_key_provider=mediapackage.CfnOriginEndpoint.SpekeKeyProviderProperty(
                            resource_id="resourceId",
                            role_arn="roleArn",
                            system_ids=["systemIds"],
                            url="url",
                
                            # the properties below are optional
                            certificate_arn="certificateArn",
                            encryption_contract_configuration=mediapackage.CfnOriginEndpoint.EncryptionContractConfigurationProperty(
                                preset_speke20_audio="presetSpeke20Audio",
                                preset_speke20_video="presetSpeke20Video"
                            )
                        ),
                
                        # the properties below are optional
                        key_rotation_interval_seconds=123
                    ),
                    include_iframe_only_stream=False,
                    manifest_layout="manifestLayout",
                    manifest_window_seconds=123,
                    min_buffer_time_seconds=123,
                    min_update_period_seconds=123,
                    period_triggers=["periodTriggers"],
                    profile="profile",
                    segment_duration_seconds=123,
                    segment_template_format="segmentTemplateFormat",
                    stream_selection=mediapackage.CfnOriginEndpoint.StreamSelectionProperty(
                        max_video_bits_per_second=123,
                        min_video_bits_per_second=123,
                        stream_order="streamOrder"
                    ),
                    suggested_presentation_delay_seconds=123,
                    utc_timing="utcTiming",
                    utc_timing_uri="utcTimingUri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8c4696e5d92d7a873900820a774868b04c3d76cad65c252fb49a13d1cdfc76fb)
                check_type(argname="argument ads_on_delivery_restrictions", value=ads_on_delivery_restrictions, expected_type=type_hints["ads_on_delivery_restrictions"])
                check_type(argname="argument ad_triggers", value=ad_triggers, expected_type=type_hints["ad_triggers"])
                check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
                check_type(argname="argument include_iframe_only_stream", value=include_iframe_only_stream, expected_type=type_hints["include_iframe_only_stream"])
                check_type(argname="argument manifest_layout", value=manifest_layout, expected_type=type_hints["manifest_layout"])
                check_type(argname="argument manifest_window_seconds", value=manifest_window_seconds, expected_type=type_hints["manifest_window_seconds"])
                check_type(argname="argument min_buffer_time_seconds", value=min_buffer_time_seconds, expected_type=type_hints["min_buffer_time_seconds"])
                check_type(argname="argument min_update_period_seconds", value=min_update_period_seconds, expected_type=type_hints["min_update_period_seconds"])
                check_type(argname="argument period_triggers", value=period_triggers, expected_type=type_hints["period_triggers"])
                check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
                check_type(argname="argument segment_duration_seconds", value=segment_duration_seconds, expected_type=type_hints["segment_duration_seconds"])
                check_type(argname="argument segment_template_format", value=segment_template_format, expected_type=type_hints["segment_template_format"])
                check_type(argname="argument stream_selection", value=stream_selection, expected_type=type_hints["stream_selection"])
                check_type(argname="argument suggested_presentation_delay_seconds", value=suggested_presentation_delay_seconds, expected_type=type_hints["suggested_presentation_delay_seconds"])
                check_type(argname="argument utc_timing", value=utc_timing, expected_type=type_hints["utc_timing"])
                check_type(argname="argument utc_timing_uri", value=utc_timing_uri, expected_type=type_hints["utc_timing_uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ads_on_delivery_restrictions is not None:
                self._values["ads_on_delivery_restrictions"] = ads_on_delivery_restrictions
            if ad_triggers is not None:
                self._values["ad_triggers"] = ad_triggers
            if encryption is not None:
                self._values["encryption"] = encryption
            if include_iframe_only_stream is not None:
                self._values["include_iframe_only_stream"] = include_iframe_only_stream
            if manifest_layout is not None:
                self._values["manifest_layout"] = manifest_layout
            if manifest_window_seconds is not None:
                self._values["manifest_window_seconds"] = manifest_window_seconds
            if min_buffer_time_seconds is not None:
                self._values["min_buffer_time_seconds"] = min_buffer_time_seconds
            if min_update_period_seconds is not None:
                self._values["min_update_period_seconds"] = min_update_period_seconds
            if period_triggers is not None:
                self._values["period_triggers"] = period_triggers
            if profile is not None:
                self._values["profile"] = profile
            if segment_duration_seconds is not None:
                self._values["segment_duration_seconds"] = segment_duration_seconds
            if segment_template_format is not None:
                self._values["segment_template_format"] = segment_template_format
            if stream_selection is not None:
                self._values["stream_selection"] = stream_selection
            if suggested_presentation_delay_seconds is not None:
                self._values["suggested_presentation_delay_seconds"] = suggested_presentation_delay_seconds
            if utc_timing is not None:
                self._values["utc_timing"] = utc_timing
            if utc_timing_uri is not None:
                self._values["utc_timing_uri"] = utc_timing_uri

        @builtins.property
        def ads_on_delivery_restrictions(self) -> typing.Optional[builtins.str]:
            '''The flags on SCTE-35 segmentation descriptors that have to be present for AWS Elemental MediaPackage to insert ad markers in the output manifest.

            For information about SCTE-35 in AWS Elemental MediaPackage , see `SCTE-35 Message Options in AWS Elemental MediaPackage <https://docs.aws.amazon.com/mediapackage/latest/ug/scte.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-adsondeliveryrestrictions
            '''
            result = self._values.get("ads_on_delivery_restrictions")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ad_triggers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Specifies the SCTE-35 message types that AWS Elemental MediaPackage treats as ad markers in the output manifest.

            Valid values:

            - ``BREAK``
            - ``DISTRIBUTOR_ADVERTISEMENT``
            - ``DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY`` .
            - ``DISTRIBUTOR_PLACEMENT_OPPORTUNITY`` .
            - ``PROVIDER_ADVERTISEMENT`` .
            - ``PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY`` .
            - ``PROVIDER_PLACEMENT_OPPORTUNITY`` .
            - ``SPLICE_INSERT`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-adtriggers
            '''
            result = self._values.get("ad_triggers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def encryption(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.DashEncryptionProperty"]]:
            '''Parameters for encrypting content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-encryption
            '''
            result = self._values.get("encryption")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.DashEncryptionProperty"]], result)

        @builtins.property
        def include_iframe_only_stream(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''This applies only to stream sets with a single video track.

            When true, the stream set includes an additional I-frame trick-play only stream, along with the other tracks. If false, this extra stream is not included.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-includeiframeonlystream
            '''
            result = self._values.get("include_iframe_only_stream")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def manifest_layout(self) -> typing.Optional[builtins.str]:
            '''Determines the position of some tags in the manifest.

            Valid values:

            - ``FULL`` - Elements like ``SegmentTemplate`` and ``ContentProtection`` are included in each ``Representation`` .
            - ``COMPACT`` - Duplicate elements are combined and presented at the ``AdaptationSet`` level.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-manifestlayout
            '''
            result = self._values.get("manifest_layout")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def manifest_window_seconds(self) -> typing.Optional[jsii.Number]:
            '''Time window (in seconds) contained in each manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-manifestwindowseconds
            '''
            result = self._values.get("manifest_window_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min_buffer_time_seconds(self) -> typing.Optional[jsii.Number]:
            '''Minimum amount of content (measured in seconds) that a player must keep available in the buffer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-minbuffertimeseconds
            '''
            result = self._values.get("min_buffer_time_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min_update_period_seconds(self) -> typing.Optional[jsii.Number]:
            '''Minimum amount of time (in seconds) that the player should wait before requesting updates to the manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-minupdateperiodseconds
            '''
            result = self._values.get("min_update_period_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def period_triggers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Controls whether AWS Elemental MediaPackage produces single-period or multi-period DASH manifests.

            For more information about periods, see `Multi-period DASH in AWS Elemental MediaPackage <https://docs.aws.amazon.com/mediapackage/latest/ug/multi-period.html>`_ .

            Valid values:

            - ``ADS`` - AWS Elemental MediaPackage will produce multi-period DASH manifests. Periods are created based on the SCTE-35 ad markers present in the input manifest.
            - *No value* - AWS Elemental MediaPackage will produce single-period DASH manifests. This is the default setting.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-periodtriggers
            '''
            result = self._values.get("period_triggers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def profile(self) -> typing.Optional[builtins.str]:
            '''The DASH profile for the output.

            Valid values:

            - ``NONE`` - The output doesn't use a DASH profile.
            - ``HBBTV_1_5`` - The output is compliant with HbbTV v1.5.
            - ``DVB_DASH_2014`` - The output is compliant with DVB-DASH 2014.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-profile
            '''
            result = self._values.get("profile")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def segment_duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''Duration (in seconds) of each fragment.

            Actual fragments are rounded to the nearest multiple of the source fragment duration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-segmentdurationseconds
            '''
            result = self._values.get("segment_duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def segment_template_format(self) -> typing.Optional[builtins.str]:
            '''Determines the type of variable used in the ``media`` URL of the ``SegmentTemplate`` tag in the manifest.

            Also specifies if segment timeline information is included in ``SegmentTimeline`` or ``SegmentTemplate`` .

            Valid values:

            - ``NUMBER_WITH_TIMELINE`` - The ``$Number$`` variable is used in the ``media`` URL. The value of this variable is the sequential number of the segment. A full ``SegmentTimeline`` object is presented in each ``SegmentTemplate`` .
            - ``NUMBER_WITH_DURATION`` - The ``$Number$`` variable is used in the ``media`` URL and a ``duration`` attribute is added to the segment template. The ``SegmentTimeline`` object is removed from the representation.
            - ``TIME_WITH_TIMELINE`` - The ``$Time$`` variable is used in the ``media`` URL. The value of this variable is the timestamp of when the segment starts. A full ``SegmentTimeline`` object is presented in each ``SegmentTemplate`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-segmenttemplateformat
            '''
            result = self._values.get("segment_template_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def stream_selection(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.StreamSelectionProperty"]]:
            '''Limitations for outputs from the endpoint, based on the video bitrate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-streamselection
            '''
            result = self._values.get("stream_selection")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.StreamSelectionProperty"]], result)

        @builtins.property
        def suggested_presentation_delay_seconds(self) -> typing.Optional[jsii.Number]:
            '''Amount of time (in seconds) that the player should be from the live point at the end of the manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-suggestedpresentationdelayseconds
            '''
            result = self._values.get("suggested_presentation_delay_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def utc_timing(self) -> typing.Optional[builtins.str]:
            '''Determines the type of UTC timing included in the DASH Media Presentation Description (MPD).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-utctiming
            '''
            result = self._values.get("utc_timing")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def utc_timing_uri(self) -> typing.Optional[builtins.str]:
            '''Specifies the value attribute of the UTC timing field when utcTiming is set to HTTP-ISO or HTTP-HEAD.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-dashpackage.html#cfn-mediapackage-originendpoint-dashpackage-utctiminguri
            '''
            result = self._values.get("utc_timing_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashPackageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnOriginEndpoint.EncryptionContractConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "preset_speke20_audio": "presetSpeke20Audio",
            "preset_speke20_video": "presetSpeke20Video",
        },
    )
    class EncryptionContractConfigurationProperty:
        def __init__(
            self,
            *,
            preset_speke20_audio: builtins.str,
            preset_speke20_video: builtins.str,
        ) -> None:
            '''Use ``encryptionContractConfiguration`` to configure one or more content encryption keys for your endpoints that use SPEKE Version 2.0. The encryption contract defines the content keys used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use. For more information about these presets, see `SPEKE Version 2.0 Presets <https://docs.aws.amazon.com/mediapackage/latest/ug/drm-content-speke-v2-presets.html>`_ .

            Note the following considerations when using ``encryptionContractConfiguration`` :

            - You can use ``encryptionContractConfiguration`` for DASH endpoints that use SPEKE Version 2.0. SPEKE Version 2.0 relies on the CPIX Version 2.3 specification.
            - You cannot combine an ``UNENCRYPTED`` preset with ``UNENCRYPTED`` or ``SHARED`` presets across ``presetSpeke20Audio`` and ``presetSpeke20Video`` .
            - When you use a ``SHARED`` preset, you must use it for both ``presetSpeke20Audio`` and ``presetSpeke20Video`` .

            :param preset_speke20_audio: A collection of audio encryption presets.
            :param preset_speke20_video: A collection of video encryption presets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-encryptioncontractconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                encryption_contract_configuration_property = mediapackage.CfnOriginEndpoint.EncryptionContractConfigurationProperty(
                    preset_speke20_audio="presetSpeke20Audio",
                    preset_speke20_video="presetSpeke20Video"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d004a027349401a62ecd9b769e520b22a332cbc1fd4ecea898450bbbac2f6f40)
                check_type(argname="argument preset_speke20_audio", value=preset_speke20_audio, expected_type=type_hints["preset_speke20_audio"])
                check_type(argname="argument preset_speke20_video", value=preset_speke20_video, expected_type=type_hints["preset_speke20_video"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "preset_speke20_audio": preset_speke20_audio,
                "preset_speke20_video": preset_speke20_video,
            }

        @builtins.property
        def preset_speke20_audio(self) -> builtins.str:
            '''A collection of audio encryption presets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-encryptioncontractconfiguration.html#cfn-mediapackage-originendpoint-encryptioncontractconfiguration-presetspeke20audio
            '''
            result = self._values.get("preset_speke20_audio")
            assert result is not None, "Required property 'preset_speke20_audio' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def preset_speke20_video(self) -> builtins.str:
            '''A collection of video encryption presets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-encryptioncontractconfiguration.html#cfn-mediapackage-originendpoint-encryptioncontractconfiguration-presetspeke20video
            '''
            result = self._values.get("preset_speke20_video")
            assert result is not None, "Required property 'preset_speke20_video' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionContractConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnOriginEndpoint.HlsEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "speke_key_provider": "spekeKeyProvider",
            "constant_initialization_vector": "constantInitializationVector",
            "encryption_method": "encryptionMethod",
            "key_rotation_interval_seconds": "keyRotationIntervalSeconds",
            "repeat_ext_x_key": "repeatExtXKey",
        },
    )
    class HlsEncryptionProperty:
        def __init__(
            self,
            *,
            speke_key_provider: typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.SpekeKeyProviderProperty", typing.Dict[builtins.str, typing.Any]]],
            constant_initialization_vector: typing.Optional[builtins.str] = None,
            encryption_method: typing.Optional[builtins.str] = None,
            key_rotation_interval_seconds: typing.Optional[jsii.Number] = None,
            repeat_ext_x_key: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Holds encryption information so that access to the content can be controlled by a DRM solution.

            :param speke_key_provider: Parameters for the SPEKE key provider.
            :param constant_initialization_vector: A 128-bit, 16-byte hex value represented by a 32-character string, used with the key for encrypting blocks.
            :param encryption_method: HLS encryption type.
            :param key_rotation_interval_seconds: Number of seconds before AWS Elemental MediaPackage rotates to a new key. By default, rotation is set to 60 seconds. Set to ``0`` to disable key rotation.
            :param repeat_ext_x_key: Repeat the ``EXT-X-KEY`` directive for every media segment. This might result in an increase in client requests to the DRM server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                hls_encryption_property = mediapackage.CfnOriginEndpoint.HlsEncryptionProperty(
                    speke_key_provider=mediapackage.CfnOriginEndpoint.SpekeKeyProviderProperty(
                        resource_id="resourceId",
                        role_arn="roleArn",
                        system_ids=["systemIds"],
                        url="url",
                
                        # the properties below are optional
                        certificate_arn="certificateArn",
                        encryption_contract_configuration=mediapackage.CfnOriginEndpoint.EncryptionContractConfigurationProperty(
                            preset_speke20_audio="presetSpeke20Audio",
                            preset_speke20_video="presetSpeke20Video"
                        )
                    ),
                
                    # the properties below are optional
                    constant_initialization_vector="constantInitializationVector",
                    encryption_method="encryptionMethod",
                    key_rotation_interval_seconds=123,
                    repeat_ext_xKey=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2bb2230c09575c8cdc63eb8385b3b1ed5b43e8bd3bdc0da5be4202670b0dfa68)
                check_type(argname="argument speke_key_provider", value=speke_key_provider, expected_type=type_hints["speke_key_provider"])
                check_type(argname="argument constant_initialization_vector", value=constant_initialization_vector, expected_type=type_hints["constant_initialization_vector"])
                check_type(argname="argument encryption_method", value=encryption_method, expected_type=type_hints["encryption_method"])
                check_type(argname="argument key_rotation_interval_seconds", value=key_rotation_interval_seconds, expected_type=type_hints["key_rotation_interval_seconds"])
                check_type(argname="argument repeat_ext_x_key", value=repeat_ext_x_key, expected_type=type_hints["repeat_ext_x_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "speke_key_provider": speke_key_provider,
            }
            if constant_initialization_vector is not None:
                self._values["constant_initialization_vector"] = constant_initialization_vector
            if encryption_method is not None:
                self._values["encryption_method"] = encryption_method
            if key_rotation_interval_seconds is not None:
                self._values["key_rotation_interval_seconds"] = key_rotation_interval_seconds
            if repeat_ext_x_key is not None:
                self._values["repeat_ext_x_key"] = repeat_ext_x_key

        @builtins.property
        def speke_key_provider(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.SpekeKeyProviderProperty"]:
            '''Parameters for the SPEKE key provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-spekekeyprovider
            '''
            result = self._values.get("speke_key_provider")
            assert result is not None, "Required property 'speke_key_provider' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.SpekeKeyProviderProperty"], result)

        @builtins.property
        def constant_initialization_vector(self) -> typing.Optional[builtins.str]:
            '''A 128-bit, 16-byte hex value represented by a 32-character string, used with the key for encrypting blocks.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-constantinitializationvector
            '''
            result = self._values.get("constant_initialization_vector")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def encryption_method(self) -> typing.Optional[builtins.str]:
            '''HLS encryption type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-encryptionmethod
            '''
            result = self._values.get("encryption_method")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key_rotation_interval_seconds(self) -> typing.Optional[jsii.Number]:
            '''Number of seconds before AWS Elemental MediaPackage rotates to a new key.

            By default, rotation is set to 60 seconds. Set to ``0`` to disable key rotation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-keyrotationintervalseconds
            '''
            result = self._values.get("key_rotation_interval_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def repeat_ext_x_key(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Repeat the ``EXT-X-KEY`` directive for every media segment.

            This might result in an increase in client requests to the DRM server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsencryption.html#cfn-mediapackage-originendpoint-hlsencryption-repeatextxkey
            '''
            result = self._values.get("repeat_ext_x_key")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnOriginEndpoint.HlsManifestProperty",
        jsii_struct_bases=[],
        name_mapping={
            "id": "id",
            "ad_markers": "adMarkers",
            "ads_on_delivery_restrictions": "adsOnDeliveryRestrictions",
            "ad_triggers": "adTriggers",
            "include_iframe_only_stream": "includeIframeOnlyStream",
            "manifest_name": "manifestName",
            "playlist_type": "playlistType",
            "playlist_window_seconds": "playlistWindowSeconds",
            "program_date_time_interval_seconds": "programDateTimeIntervalSeconds",
            "url": "url",
        },
    )
    class HlsManifestProperty:
        def __init__(
            self,
            *,
            id: builtins.str,
            ad_markers: typing.Optional[builtins.str] = None,
            ads_on_delivery_restrictions: typing.Optional[builtins.str] = None,
            ad_triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
            include_iframe_only_stream: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            manifest_name: typing.Optional[builtins.str] = None,
            playlist_type: typing.Optional[builtins.str] = None,
            playlist_window_seconds: typing.Optional[jsii.Number] = None,
            program_date_time_interval_seconds: typing.Optional[jsii.Number] = None,
            url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An HTTP Live Streaming (HLS) manifest configuration on a CMAF endpoint.

            :param id: The manifest ID is required and must be unique within the OriginEndpoint. The ID can't be changed after the endpoint is created.
            :param ad_markers: Controls how ad markers are included in the packaged endpoint. Valid values: - ``NONE`` - Omits all SCTE-35 ad markers from the output. - ``PASSTHROUGH`` - Creates a copy in the output of the SCTE-35 ad markers (comments) taken directly from the input manifest. - ``SCTE35_ENHANCED`` - Generates ad markers and blackout tags in the output based on the SCTE-35 messages from the input manifest.
            :param ads_on_delivery_restrictions: The flags on SCTE-35 segmentation descriptors that have to be present for AWS Elemental MediaPackage to insert ad markers in the output manifest. For information about SCTE-35 in AWS Elemental MediaPackage , see `SCTE-35 Message Options in AWS Elemental MediaPackage <https://docs.aws.amazon.com/mediapackage/latest/ug/scte.html>`_ .
            :param ad_triggers: Specifies the SCTE-35 message types that AWS Elemental MediaPackage treats as ad markers in the output manifest. Valid values: - ``BREAK`` - ``DISTRIBUTOR_ADVERTISEMENT`` - ``DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY`` - ``DISTRIBUTOR_PLACEMENT_OPPORTUNITY`` - ``PROVIDER_ADVERTISEMENT`` - ``PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY`` - ``PROVIDER_PLACEMENT_OPPORTUNITY`` - ``SPLICE_INSERT``
            :param include_iframe_only_stream: Applies to stream sets with a single video track only. When true, the stream set includes an additional I-frame only stream, along with the other tracks. If false, this extra stream is not included.
            :param manifest_name: A short string that's appended to the end of the endpoint URL to create a unique path to this endpoint. The manifestName on the HLSManifest object overrides the manifestName that you provided on the originEndpoint object.
            :param playlist_type: When specified as either ``event`` or ``vod`` , a corresponding ``EXT-X-PLAYLIST-TYPE`` entry is included in the media playlist. Indicates if the playlist is live-to-VOD content.
            :param playlist_window_seconds: Time window (in seconds) contained in each parent manifest.
            :param program_date_time_interval_seconds: Inserts ``EXT-X-PROGRAM-DATE-TIME`` tags in the output manifest at the interval that you specify. Additionally, ID3Timed metadata messages are generated every 5 seconds starting when the content was ingested. Irrespective of this parameter, if any ID3Timed metadata is in the HLS input, it is passed through to the HLS output. Omit this attribute or enter ``0`` to indicate that the ``EXT-X-PROGRAM-DATE-TIME`` tags are not included in the manifest.
            :param url: The URL that's used to request this manifest from this endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                hls_manifest_property = mediapackage.CfnOriginEndpoint.HlsManifestProperty(
                    id="id",
                
                    # the properties below are optional
                    ad_markers="adMarkers",
                    ads_on_delivery_restrictions="adsOnDeliveryRestrictions",
                    ad_triggers=["adTriggers"],
                    include_iframe_only_stream=False,
                    manifest_name="manifestName",
                    playlist_type="playlistType",
                    playlist_window_seconds=123,
                    program_date_time_interval_seconds=123,
                    url="url"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4367b7a88cd2fce8b4e47599c1f36f00f1184af4a9a26f40d6b422a374b0ea08)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument ad_markers", value=ad_markers, expected_type=type_hints["ad_markers"])
                check_type(argname="argument ads_on_delivery_restrictions", value=ads_on_delivery_restrictions, expected_type=type_hints["ads_on_delivery_restrictions"])
                check_type(argname="argument ad_triggers", value=ad_triggers, expected_type=type_hints["ad_triggers"])
                check_type(argname="argument include_iframe_only_stream", value=include_iframe_only_stream, expected_type=type_hints["include_iframe_only_stream"])
                check_type(argname="argument manifest_name", value=manifest_name, expected_type=type_hints["manifest_name"])
                check_type(argname="argument playlist_type", value=playlist_type, expected_type=type_hints["playlist_type"])
                check_type(argname="argument playlist_window_seconds", value=playlist_window_seconds, expected_type=type_hints["playlist_window_seconds"])
                check_type(argname="argument program_date_time_interval_seconds", value=program_date_time_interval_seconds, expected_type=type_hints["program_date_time_interval_seconds"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
            }
            if ad_markers is not None:
                self._values["ad_markers"] = ad_markers
            if ads_on_delivery_restrictions is not None:
                self._values["ads_on_delivery_restrictions"] = ads_on_delivery_restrictions
            if ad_triggers is not None:
                self._values["ad_triggers"] = ad_triggers
            if include_iframe_only_stream is not None:
                self._values["include_iframe_only_stream"] = include_iframe_only_stream
            if manifest_name is not None:
                self._values["manifest_name"] = manifest_name
            if playlist_type is not None:
                self._values["playlist_type"] = playlist_type
            if playlist_window_seconds is not None:
                self._values["playlist_window_seconds"] = playlist_window_seconds
            if program_date_time_interval_seconds is not None:
                self._values["program_date_time_interval_seconds"] = program_date_time_interval_seconds
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def id(self) -> builtins.str:
            '''The manifest ID is required and must be unique within the OriginEndpoint.

            The ID can't be changed after the endpoint is created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def ad_markers(self) -> typing.Optional[builtins.str]:
            '''Controls how ad markers are included in the packaged endpoint.

            Valid values:

            - ``NONE`` - Omits all SCTE-35 ad markers from the output.
            - ``PASSTHROUGH`` - Creates a copy in the output of the SCTE-35 ad markers (comments) taken directly from the input manifest.
            - ``SCTE35_ENHANCED`` - Generates ad markers and blackout tags in the output based on the SCTE-35 messages from the input manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-admarkers
            '''
            result = self._values.get("ad_markers")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ads_on_delivery_restrictions(self) -> typing.Optional[builtins.str]:
            '''The flags on SCTE-35 segmentation descriptors that have to be present for AWS Elemental MediaPackage to insert ad markers in the output manifest.

            For information about SCTE-35 in AWS Elemental MediaPackage , see `SCTE-35 Message Options in AWS Elemental MediaPackage <https://docs.aws.amazon.com/mediapackage/latest/ug/scte.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-adsondeliveryrestrictions
            '''
            result = self._values.get("ads_on_delivery_restrictions")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ad_triggers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Specifies the SCTE-35 message types that AWS Elemental MediaPackage treats as ad markers in the output manifest.

            Valid values:

            - ``BREAK``
            - ``DISTRIBUTOR_ADVERTISEMENT``
            - ``DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY``
            - ``DISTRIBUTOR_PLACEMENT_OPPORTUNITY``
            - ``PROVIDER_ADVERTISEMENT``
            - ``PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY``
            - ``PROVIDER_PLACEMENT_OPPORTUNITY``
            - ``SPLICE_INSERT``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-adtriggers
            '''
            result = self._values.get("ad_triggers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def include_iframe_only_stream(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Applies to stream sets with a single video track only.

            When true, the stream set includes an additional I-frame only stream, along with the other tracks. If false, this extra stream is not included.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-includeiframeonlystream
            '''
            result = self._values.get("include_iframe_only_stream")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def manifest_name(self) -> typing.Optional[builtins.str]:
            '''A short string that's appended to the end of the endpoint URL to create a unique path to this endpoint.

            The manifestName on the HLSManifest object overrides the manifestName that you provided on the originEndpoint object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-manifestname
            '''
            result = self._values.get("manifest_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def playlist_type(self) -> typing.Optional[builtins.str]:
            '''When specified as either ``event`` or ``vod`` , a corresponding ``EXT-X-PLAYLIST-TYPE`` entry is included in the media playlist.

            Indicates if the playlist is live-to-VOD content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-playlisttype
            '''
            result = self._values.get("playlist_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def playlist_window_seconds(self) -> typing.Optional[jsii.Number]:
            '''Time window (in seconds) contained in each parent manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-playlistwindowseconds
            '''
            result = self._values.get("playlist_window_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def program_date_time_interval_seconds(self) -> typing.Optional[jsii.Number]:
            '''Inserts ``EXT-X-PROGRAM-DATE-TIME`` tags in the output manifest at the interval that you specify.

            Additionally, ID3Timed metadata messages are generated every 5 seconds starting when the content was ingested.

            Irrespective of this parameter, if any ID3Timed metadata is in the HLS input, it is passed through to the HLS output.

            Omit this attribute or enter ``0`` to indicate that the ``EXT-X-PROGRAM-DATE-TIME`` tags are not included in the manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-programdatetimeintervalseconds
            '''
            result = self._values.get("program_date_time_interval_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''The URL that's used to request this manifest from this endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlsmanifest.html#cfn-mediapackage-originendpoint-hlsmanifest-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsManifestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnOriginEndpoint.HlsPackageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ad_markers": "adMarkers",
            "ads_on_delivery_restrictions": "adsOnDeliveryRestrictions",
            "ad_triggers": "adTriggers",
            "encryption": "encryption",
            "include_dvb_subtitles": "includeDvbSubtitles",
            "include_iframe_only_stream": "includeIframeOnlyStream",
            "playlist_type": "playlistType",
            "playlist_window_seconds": "playlistWindowSeconds",
            "program_date_time_interval_seconds": "programDateTimeIntervalSeconds",
            "segment_duration_seconds": "segmentDurationSeconds",
            "stream_selection": "streamSelection",
            "use_audio_rendition_group": "useAudioRenditionGroup",
        },
    )
    class HlsPackageProperty:
        def __init__(
            self,
            *,
            ad_markers: typing.Optional[builtins.str] = None,
            ads_on_delivery_restrictions: typing.Optional[builtins.str] = None,
            ad_triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
            encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.HlsEncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            include_dvb_subtitles: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_iframe_only_stream: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            playlist_type: typing.Optional[builtins.str] = None,
            playlist_window_seconds: typing.Optional[jsii.Number] = None,
            program_date_time_interval_seconds: typing.Optional[jsii.Number] = None,
            segment_duration_seconds: typing.Optional[jsii.Number] = None,
            stream_selection: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.StreamSelectionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            use_audio_rendition_group: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Parameters for Apple HLS packaging.

            :param ad_markers: Controls how ad markers are included in the packaged endpoint. Valid values: - ``NONE`` - Omits all SCTE-35 ad markers from the output. - ``PASSTHROUGH`` - Creates a copy in the output of the SCTE-35 ad markers (comments) taken directly from the input manifest. - ``SCTE35_ENHANCED`` - Generates ad markers and blackout tags in the output based on the SCTE-35 messages from the input manifest.
            :param ads_on_delivery_restrictions: The flags on SCTE-35 segmentation descriptors that have to be present for AWS Elemental MediaPackage to insert ad markers in the output manifest. For information about SCTE-35 in AWS Elemental MediaPackage , see `SCTE-35 Message Options in AWS Elemental MediaPackage <https://docs.aws.amazon.com/mediapackage/latest/ug/scte.html>`_ .
            :param ad_triggers: Specifies the SCTE-35 message types that AWS Elemental MediaPackage treats as ad markers in the output manifest. Valid values: - ``BREAK`` - ``DISTRIBUTOR_ADVERTISEMENT`` - ``DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY`` - ``DISTRIBUTOR_PLACEMENT_OPPORTUNITY`` - ``PROVIDER_ADVERTISEMENT`` - ``PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY`` - ``PROVIDER_PLACEMENT_OPPORTUNITY`` - ``SPLICE_INSERT``
            :param encryption: Parameters for encrypting content.
            :param include_dvb_subtitles: When enabled, MediaPackage passes through digital video broadcasting (DVB) subtitles into the output.
            :param include_iframe_only_stream: Only applies to stream sets with a single video track. When true, the stream set includes an additional I-frame only stream, along with the other tracks. If false, this extra stream is not included.
            :param playlist_type: When specified as either ``event`` or ``vod`` , a corresponding ``EXT-X-PLAYLIST-TYPE`` entry is included in the media playlist. Indicates if the playlist is live-to-VOD content.
            :param playlist_window_seconds: Time window (in seconds) contained in each parent manifest.
            :param program_date_time_interval_seconds: Inserts ``EXT-X-PROGRAM-DATE-TIME`` tags in the output manifest at the interval that you specify. Additionally, ID3Timed metadata messages are generated every 5 seconds starting when the content was ingested. Irrespective of this parameter, if any ID3Timed metadata is in the HLS input, it is passed through to the HLS output. Omit this attribute or enter ``0`` to indicate that the ``EXT-X-PROGRAM-DATE-TIME`` tags are not included in the manifest.
            :param segment_duration_seconds: Duration (in seconds) of each fragment. Actual fragments are rounded to the nearest multiple of the source fragment duration.
            :param stream_selection: Limitations for outputs from the endpoint, based on the video bitrate.
            :param use_audio_rendition_group: When true, AWS Elemental MediaPackage bundles all audio tracks in a rendition group. All other tracks in the stream can be used with any audio rendition from the group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                hls_package_property = mediapackage.CfnOriginEndpoint.HlsPackageProperty(
                    ad_markers="adMarkers",
                    ads_on_delivery_restrictions="adsOnDeliveryRestrictions",
                    ad_triggers=["adTriggers"],
                    encryption=mediapackage.CfnOriginEndpoint.HlsEncryptionProperty(
                        speke_key_provider=mediapackage.CfnOriginEndpoint.SpekeKeyProviderProperty(
                            resource_id="resourceId",
                            role_arn="roleArn",
                            system_ids=["systemIds"],
                            url="url",
                
                            # the properties below are optional
                            certificate_arn="certificateArn",
                            encryption_contract_configuration=mediapackage.CfnOriginEndpoint.EncryptionContractConfigurationProperty(
                                preset_speke20_audio="presetSpeke20Audio",
                                preset_speke20_video="presetSpeke20Video"
                            )
                        ),
                
                        # the properties below are optional
                        constant_initialization_vector="constantInitializationVector",
                        encryption_method="encryptionMethod",
                        key_rotation_interval_seconds=123,
                        repeat_ext_xKey=False
                    ),
                    include_dvb_subtitles=False,
                    include_iframe_only_stream=False,
                    playlist_type="playlistType",
                    playlist_window_seconds=123,
                    program_date_time_interval_seconds=123,
                    segment_duration_seconds=123,
                    stream_selection=mediapackage.CfnOriginEndpoint.StreamSelectionProperty(
                        max_video_bits_per_second=123,
                        min_video_bits_per_second=123,
                        stream_order="streamOrder"
                    ),
                    use_audio_rendition_group=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__87f398a1f56dd5a78638b6c90bb8102a40772d7c15d100576989267626013d86)
                check_type(argname="argument ad_markers", value=ad_markers, expected_type=type_hints["ad_markers"])
                check_type(argname="argument ads_on_delivery_restrictions", value=ads_on_delivery_restrictions, expected_type=type_hints["ads_on_delivery_restrictions"])
                check_type(argname="argument ad_triggers", value=ad_triggers, expected_type=type_hints["ad_triggers"])
                check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
                check_type(argname="argument include_dvb_subtitles", value=include_dvb_subtitles, expected_type=type_hints["include_dvb_subtitles"])
                check_type(argname="argument include_iframe_only_stream", value=include_iframe_only_stream, expected_type=type_hints["include_iframe_only_stream"])
                check_type(argname="argument playlist_type", value=playlist_type, expected_type=type_hints["playlist_type"])
                check_type(argname="argument playlist_window_seconds", value=playlist_window_seconds, expected_type=type_hints["playlist_window_seconds"])
                check_type(argname="argument program_date_time_interval_seconds", value=program_date_time_interval_seconds, expected_type=type_hints["program_date_time_interval_seconds"])
                check_type(argname="argument segment_duration_seconds", value=segment_duration_seconds, expected_type=type_hints["segment_duration_seconds"])
                check_type(argname="argument stream_selection", value=stream_selection, expected_type=type_hints["stream_selection"])
                check_type(argname="argument use_audio_rendition_group", value=use_audio_rendition_group, expected_type=type_hints["use_audio_rendition_group"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ad_markers is not None:
                self._values["ad_markers"] = ad_markers
            if ads_on_delivery_restrictions is not None:
                self._values["ads_on_delivery_restrictions"] = ads_on_delivery_restrictions
            if ad_triggers is not None:
                self._values["ad_triggers"] = ad_triggers
            if encryption is not None:
                self._values["encryption"] = encryption
            if include_dvb_subtitles is not None:
                self._values["include_dvb_subtitles"] = include_dvb_subtitles
            if include_iframe_only_stream is not None:
                self._values["include_iframe_only_stream"] = include_iframe_only_stream
            if playlist_type is not None:
                self._values["playlist_type"] = playlist_type
            if playlist_window_seconds is not None:
                self._values["playlist_window_seconds"] = playlist_window_seconds
            if program_date_time_interval_seconds is not None:
                self._values["program_date_time_interval_seconds"] = program_date_time_interval_seconds
            if segment_duration_seconds is not None:
                self._values["segment_duration_seconds"] = segment_duration_seconds
            if stream_selection is not None:
                self._values["stream_selection"] = stream_selection
            if use_audio_rendition_group is not None:
                self._values["use_audio_rendition_group"] = use_audio_rendition_group

        @builtins.property
        def ad_markers(self) -> typing.Optional[builtins.str]:
            '''Controls how ad markers are included in the packaged endpoint.

            Valid values:

            - ``NONE`` - Omits all SCTE-35 ad markers from the output.
            - ``PASSTHROUGH`` - Creates a copy in the output of the SCTE-35 ad markers (comments) taken directly from the input manifest.
            - ``SCTE35_ENHANCED`` - Generates ad markers and blackout tags in the output based on the SCTE-35 messages from the input manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-admarkers
            '''
            result = self._values.get("ad_markers")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ads_on_delivery_restrictions(self) -> typing.Optional[builtins.str]:
            '''The flags on SCTE-35 segmentation descriptors that have to be present for AWS Elemental MediaPackage to insert ad markers in the output manifest.

            For information about SCTE-35 in AWS Elemental MediaPackage , see `SCTE-35 Message Options in AWS Elemental MediaPackage <https://docs.aws.amazon.com/mediapackage/latest/ug/scte.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-adsondeliveryrestrictions
            '''
            result = self._values.get("ads_on_delivery_restrictions")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ad_triggers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Specifies the SCTE-35 message types that AWS Elemental MediaPackage treats as ad markers in the output manifest.

            Valid values:

            - ``BREAK``
            - ``DISTRIBUTOR_ADVERTISEMENT``
            - ``DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY``
            - ``DISTRIBUTOR_PLACEMENT_OPPORTUNITY``
            - ``PROVIDER_ADVERTISEMENT``
            - ``PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY``
            - ``PROVIDER_PLACEMENT_OPPORTUNITY``
            - ``SPLICE_INSERT``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-adtriggers
            '''
            result = self._values.get("ad_triggers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def encryption(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.HlsEncryptionProperty"]]:
            '''Parameters for encrypting content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-encryption
            '''
            result = self._values.get("encryption")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.HlsEncryptionProperty"]], result)

        @builtins.property
        def include_dvb_subtitles(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When enabled, MediaPackage passes through digital video broadcasting (DVB) subtitles into the output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-includedvbsubtitles
            '''
            result = self._values.get("include_dvb_subtitles")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_iframe_only_stream(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Only applies to stream sets with a single video track.

            When true, the stream set includes an additional I-frame only stream, along with the other tracks. If false, this extra stream is not included.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-includeiframeonlystream
            '''
            result = self._values.get("include_iframe_only_stream")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def playlist_type(self) -> typing.Optional[builtins.str]:
            '''When specified as either ``event`` or ``vod`` , a corresponding ``EXT-X-PLAYLIST-TYPE`` entry is included in the media playlist.

            Indicates if the playlist is live-to-VOD content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-playlisttype
            '''
            result = self._values.get("playlist_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def playlist_window_seconds(self) -> typing.Optional[jsii.Number]:
            '''Time window (in seconds) contained in each parent manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-playlistwindowseconds
            '''
            result = self._values.get("playlist_window_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def program_date_time_interval_seconds(self) -> typing.Optional[jsii.Number]:
            '''Inserts ``EXT-X-PROGRAM-DATE-TIME`` tags in the output manifest at the interval that you specify.

            Additionally, ID3Timed metadata messages are generated every 5 seconds starting when the content was ingested.

            Irrespective of this parameter, if any ID3Timed metadata is in the HLS input, it is passed through to the HLS output.

            Omit this attribute or enter ``0`` to indicate that the ``EXT-X-PROGRAM-DATE-TIME`` tags are not included in the manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-programdatetimeintervalseconds
            '''
            result = self._values.get("program_date_time_interval_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def segment_duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''Duration (in seconds) of each fragment.

            Actual fragments are rounded to the nearest multiple of the source fragment duration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-segmentdurationseconds
            '''
            result = self._values.get("segment_duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def stream_selection(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.StreamSelectionProperty"]]:
            '''Limitations for outputs from the endpoint, based on the video bitrate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-streamselection
            '''
            result = self._values.get("stream_selection")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.StreamSelectionProperty"]], result)

        @builtins.property
        def use_audio_rendition_group(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When true, AWS Elemental MediaPackage bundles all audio tracks in a rendition group.

            All other tracks in the stream can be used with any audio rendition from the group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-hlspackage.html#cfn-mediapackage-originendpoint-hlspackage-useaudiorenditiongroup
            '''
            result = self._values.get("use_audio_rendition_group")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsPackageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnOriginEndpoint.MssEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={"speke_key_provider": "spekeKeyProvider"},
    )
    class MssEncryptionProperty:
        def __init__(
            self,
            *,
            speke_key_provider: typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.SpekeKeyProviderProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Holds encryption information so that access to the content can be controlled by a DRM solution.

            :param speke_key_provider: Parameters for the SPEKE key provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-mssencryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                mss_encryption_property = mediapackage.CfnOriginEndpoint.MssEncryptionProperty(
                    speke_key_provider=mediapackage.CfnOriginEndpoint.SpekeKeyProviderProperty(
                        resource_id="resourceId",
                        role_arn="roleArn",
                        system_ids=["systemIds"],
                        url="url",
                
                        # the properties below are optional
                        certificate_arn="certificateArn",
                        encryption_contract_configuration=mediapackage.CfnOriginEndpoint.EncryptionContractConfigurationProperty(
                            preset_speke20_audio="presetSpeke20Audio",
                            preset_speke20_video="presetSpeke20Video"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1e810041b25aa758d918a63335aaf66c8260882c17a1f14a0c6024a377e47581)
                check_type(argname="argument speke_key_provider", value=speke_key_provider, expected_type=type_hints["speke_key_provider"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "speke_key_provider": speke_key_provider,
            }

        @builtins.property
        def speke_key_provider(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.SpekeKeyProviderProperty"]:
            '''Parameters for the SPEKE key provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-mssencryption.html#cfn-mediapackage-originendpoint-mssencryption-spekekeyprovider
            '''
            result = self._values.get("speke_key_provider")
            assert result is not None, "Required property 'speke_key_provider' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.SpekeKeyProviderProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MssEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnOriginEndpoint.MssPackageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption": "encryption",
            "manifest_window_seconds": "manifestWindowSeconds",
            "segment_duration_seconds": "segmentDurationSeconds",
            "stream_selection": "streamSelection",
        },
    )
    class MssPackageProperty:
        def __init__(
            self,
            *,
            encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.MssEncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            manifest_window_seconds: typing.Optional[jsii.Number] = None,
            segment_duration_seconds: typing.Optional[jsii.Number] = None,
            stream_selection: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.StreamSelectionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Parameters for Microsoft Smooth Streaming packaging.

            :param encryption: Parameters for encrypting content.
            :param manifest_window_seconds: Time window (in seconds) contained in each manifest.
            :param segment_duration_seconds: Duration (in seconds) of each fragment. Actual fragments are rounded to the nearest multiple of the source fragment duration.
            :param stream_selection: Limitations for outputs from the endpoint, based on the video bitrate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-msspackage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                mss_package_property = mediapackage.CfnOriginEndpoint.MssPackageProperty(
                    encryption=mediapackage.CfnOriginEndpoint.MssEncryptionProperty(
                        speke_key_provider=mediapackage.CfnOriginEndpoint.SpekeKeyProviderProperty(
                            resource_id="resourceId",
                            role_arn="roleArn",
                            system_ids=["systemIds"],
                            url="url",
                
                            # the properties below are optional
                            certificate_arn="certificateArn",
                            encryption_contract_configuration=mediapackage.CfnOriginEndpoint.EncryptionContractConfigurationProperty(
                                preset_speke20_audio="presetSpeke20Audio",
                                preset_speke20_video="presetSpeke20Video"
                            )
                        )
                    ),
                    manifest_window_seconds=123,
                    segment_duration_seconds=123,
                    stream_selection=mediapackage.CfnOriginEndpoint.StreamSelectionProperty(
                        max_video_bits_per_second=123,
                        min_video_bits_per_second=123,
                        stream_order="streamOrder"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c969b579bc64ba1fc64cf397aae32417cbae6217efb342f5ca4de656126a4773)
                check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
                check_type(argname="argument manifest_window_seconds", value=manifest_window_seconds, expected_type=type_hints["manifest_window_seconds"])
                check_type(argname="argument segment_duration_seconds", value=segment_duration_seconds, expected_type=type_hints["segment_duration_seconds"])
                check_type(argname="argument stream_selection", value=stream_selection, expected_type=type_hints["stream_selection"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if encryption is not None:
                self._values["encryption"] = encryption
            if manifest_window_seconds is not None:
                self._values["manifest_window_seconds"] = manifest_window_seconds
            if segment_duration_seconds is not None:
                self._values["segment_duration_seconds"] = segment_duration_seconds
            if stream_selection is not None:
                self._values["stream_selection"] = stream_selection

        @builtins.property
        def encryption(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.MssEncryptionProperty"]]:
            '''Parameters for encrypting content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-msspackage.html#cfn-mediapackage-originendpoint-msspackage-encryption
            '''
            result = self._values.get("encryption")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.MssEncryptionProperty"]], result)

        @builtins.property
        def manifest_window_seconds(self) -> typing.Optional[jsii.Number]:
            '''Time window (in seconds) contained in each manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-msspackage.html#cfn-mediapackage-originendpoint-msspackage-manifestwindowseconds
            '''
            result = self._values.get("manifest_window_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def segment_duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''Duration (in seconds) of each fragment.

            Actual fragments are rounded to the nearest multiple of the source fragment duration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-msspackage.html#cfn-mediapackage-originendpoint-msspackage-segmentdurationseconds
            '''
            result = self._values.get("segment_duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def stream_selection(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.StreamSelectionProperty"]]:
            '''Limitations for outputs from the endpoint, based on the video bitrate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-msspackage.html#cfn-mediapackage-originendpoint-msspackage-streamselection
            '''
            result = self._values.get("stream_selection")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.StreamSelectionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MssPackageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnOriginEndpoint.SpekeKeyProviderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "resource_id": "resourceId",
            "role_arn": "roleArn",
            "system_ids": "systemIds",
            "url": "url",
            "certificate_arn": "certificateArn",
            "encryption_contract_configuration": "encryptionContractConfiguration",
        },
    )
    class SpekeKeyProviderProperty:
        def __init__(
            self,
            *,
            resource_id: builtins.str,
            role_arn: builtins.str,
            system_ids: typing.Sequence[builtins.str],
            url: builtins.str,
            certificate_arn: typing.Optional[builtins.str] = None,
            encryption_contract_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnOriginEndpoint.EncryptionContractConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Key provider settings for DRM.

            :param resource_id: Unique identifier for this endpoint, as it is configured in the key provider service.
            :param role_arn: The ARN for the IAM role that's granted by the key provider to provide access to the key provider API. This role must have a trust policy that allows AWS Elemental MediaPackage to assume the role, and it must have a sufficient permissions policy to allow access to the specific key retrieval URL. Valid format: arn:aws:iam::{accountID}:role/{name}
            :param system_ids: List of unique identifiers for the DRM systems to use, as defined in the CPIX specification.
            :param url: URL for the key provider’s key retrieval API endpoint. Must start with https://.
            :param certificate_arn: The Amazon Resource Name (ARN) for the certificate that you imported to AWS Certificate Manager to add content key encryption to this endpoint. For this feature to work, your DRM key provider must support content key encryption.
            :param encryption_contract_configuration: Use ``encryptionContractConfiguration`` to configure one or more content encryption keys for your endpoints that use SPEKE Version 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                speke_key_provider_property = mediapackage.CfnOriginEndpoint.SpekeKeyProviderProperty(
                    resource_id="resourceId",
                    role_arn="roleArn",
                    system_ids=["systemIds"],
                    url="url",
                
                    # the properties below are optional
                    certificate_arn="certificateArn",
                    encryption_contract_configuration=mediapackage.CfnOriginEndpoint.EncryptionContractConfigurationProperty(
                        preset_speke20_audio="presetSpeke20Audio",
                        preset_speke20_video="presetSpeke20Video"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__31902760039319c8326b4b548986fbad0bbd400bebcf315b1f06706a4fe40f37)
                check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument system_ids", value=system_ids, expected_type=type_hints["system_ids"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
                check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
                check_type(argname="argument encryption_contract_configuration", value=encryption_contract_configuration, expected_type=type_hints["encryption_contract_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_id": resource_id,
                "role_arn": role_arn,
                "system_ids": system_ids,
                "url": url,
            }
            if certificate_arn is not None:
                self._values["certificate_arn"] = certificate_arn
            if encryption_contract_configuration is not None:
                self._values["encryption_contract_configuration"] = encryption_contract_configuration

        @builtins.property
        def resource_id(self) -> builtins.str:
            '''Unique identifier for this endpoint, as it is configured in the key provider service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-resourceid
            '''
            result = self._values.get("resource_id")
            assert result is not None, "Required property 'resource_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN for the IAM role that's granted by the key provider to provide access to the key provider API.

            This role must have a trust policy that allows AWS Elemental MediaPackage to assume the role, and it must have a sufficient permissions policy to allow access to the specific key retrieval URL. Valid format: arn:aws:iam::{accountID}:role/{name}

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def system_ids(self) -> typing.List[builtins.str]:
            '''List of unique identifiers for the DRM systems to use, as defined in the CPIX specification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-systemids
            '''
            result = self._values.get("system_ids")
            assert result is not None, "Required property 'system_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def url(self) -> builtins.str:
            '''URL for the key provider’s key retrieval API endpoint.

            Must start with https://.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-url
            '''
            result = self._values.get("url")
            assert result is not None, "Required property 'url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def certificate_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) for the certificate that you imported to AWS Certificate Manager to add content key encryption to this endpoint.

            For this feature to work, your DRM key provider must support content key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-certificatearn
            '''
            result = self._values.get("certificate_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def encryption_contract_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.EncryptionContractConfigurationProperty"]]:
            '''Use ``encryptionContractConfiguration`` to configure one or more content encryption keys for your endpoints that use SPEKE Version 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-spekekeyprovider.html#cfn-mediapackage-originendpoint-spekekeyprovider-encryptioncontractconfiguration
            '''
            result = self._values.get("encryption_contract_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnOriginEndpoint.EncryptionContractConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SpekeKeyProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnOriginEndpoint.StreamSelectionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_video_bits_per_second": "maxVideoBitsPerSecond",
            "min_video_bits_per_second": "minVideoBitsPerSecond",
            "stream_order": "streamOrder",
        },
    )
    class StreamSelectionProperty:
        def __init__(
            self,
            *,
            max_video_bits_per_second: typing.Optional[jsii.Number] = None,
            min_video_bits_per_second: typing.Optional[jsii.Number] = None,
            stream_order: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Limitations for outputs from the endpoint, based on the video bitrate.

            :param max_video_bits_per_second: The upper limit of the bitrates that this endpoint serves. If the video track exceeds this threshold, then AWS Elemental MediaPackage excludes it from output. If you don't specify a value, it defaults to 2147483647 bits per second.
            :param min_video_bits_per_second: The lower limit of the bitrates that this endpoint serves. If the video track is below this threshold, then AWS Elemental MediaPackage excludes it from output. If you don't specify a value, it defaults to 0 bits per second.
            :param stream_order: Order in which the different video bitrates are presented to the player. Valid values: ``ORIGINAL`` , ``VIDEO_BITRATE_ASCENDING`` , ``VIDEO_BITRATE_DESCENDING`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-streamselection.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                stream_selection_property = mediapackage.CfnOriginEndpoint.StreamSelectionProperty(
                    max_video_bits_per_second=123,
                    min_video_bits_per_second=123,
                    stream_order="streamOrder"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4150b724a2d6d3b325b7f3b3e1bb909d659fb82d5ec1b7008d487cfc1e271e2f)
                check_type(argname="argument max_video_bits_per_second", value=max_video_bits_per_second, expected_type=type_hints["max_video_bits_per_second"])
                check_type(argname="argument min_video_bits_per_second", value=min_video_bits_per_second, expected_type=type_hints["min_video_bits_per_second"])
                check_type(argname="argument stream_order", value=stream_order, expected_type=type_hints["stream_order"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if max_video_bits_per_second is not None:
                self._values["max_video_bits_per_second"] = max_video_bits_per_second
            if min_video_bits_per_second is not None:
                self._values["min_video_bits_per_second"] = min_video_bits_per_second
            if stream_order is not None:
                self._values["stream_order"] = stream_order

        @builtins.property
        def max_video_bits_per_second(self) -> typing.Optional[jsii.Number]:
            '''The upper limit of the bitrates that this endpoint serves.

            If the video track exceeds this threshold, then AWS Elemental MediaPackage excludes it from output. If you don't specify a value, it defaults to 2147483647 bits per second.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-streamselection.html#cfn-mediapackage-originendpoint-streamselection-maxvideobitspersecond
            '''
            result = self._values.get("max_video_bits_per_second")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min_video_bits_per_second(self) -> typing.Optional[jsii.Number]:
            '''The lower limit of the bitrates that this endpoint serves.

            If the video track is below this threshold, then AWS Elemental MediaPackage excludes it from output. If you don't specify a value, it defaults to 0 bits per second.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-streamselection.html#cfn-mediapackage-originendpoint-streamselection-minvideobitspersecond
            '''
            result = self._values.get("min_video_bits_per_second")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def stream_order(self) -> typing.Optional[builtins.str]:
            '''Order in which the different video bitrates are presented to the player.

            Valid values: ``ORIGINAL`` , ``VIDEO_BITRATE_ASCENDING`` , ``VIDEO_BITRATE_DESCENDING`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-originendpoint-streamselection.html#cfn-mediapackage-originendpoint-streamselection-streamorder
            '''
            result = self._values.get("stream_order")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StreamSelectionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediapackage.CfnOriginEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "channel_id": "channelId",
        "id": "id",
        "authorization": "authorization",
        "cmaf_package": "cmafPackage",
        "dash_package": "dashPackage",
        "description": "description",
        "hls_package": "hlsPackage",
        "manifest_name": "manifestName",
        "mss_package": "mssPackage",
        "origination": "origination",
        "startover_window_seconds": "startoverWindowSeconds",
        "tags": "tags",
        "time_delay_seconds": "timeDelaySeconds",
        "whitelist": "whitelist",
    },
)
class CfnOriginEndpointProps:
    def __init__(
        self,
        *,
        channel_id: builtins.str,
        id: builtins.str,
        authorization: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.AuthorizationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        cmaf_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.CmafPackageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        dash_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.DashPackageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        hls_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.HlsPackageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        manifest_name: typing.Optional[builtins.str] = None,
        mss_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.MssPackageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        origination: typing.Optional[builtins.str] = None,
        startover_window_seconds: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        time_delay_seconds: typing.Optional[jsii.Number] = None,
        whitelist: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnOriginEndpoint``.

        :param channel_id: The ID of the channel associated with this endpoint.
        :param id: The manifest ID is required and must be unique within the OriginEndpoint. The ID can't be changed after the endpoint is created.
        :param authorization: Parameters for CDN authorization.
        :param cmaf_package: Parameters for Common Media Application Format (CMAF) packaging.
        :param dash_package: Parameters for DASH packaging.
        :param description: Any descriptive information that you want to add to the endpoint for future identification purposes.
        :param hls_package: Parameters for Apple HLS packaging.
        :param manifest_name: A short string that's appended to the end of the endpoint URL to create a unique path to this endpoint.
        :param mss_package: Parameters for Microsoft Smooth Streaming packaging.
        :param origination: Controls video origination from this endpoint. Valid values: - ``ALLOW`` - enables this endpoint to serve content to requesting devices. - ``DENY`` - prevents this endpoint from serving content. Denying origination is helpful for harvesting live-to-VOD assets. For more information about harvesting and origination, see `Live-to-VOD Requirements <https://docs.aws.amazon.com/mediapackage/latest/ug/ltov-reqmts.html>`_ .
        :param startover_window_seconds: Maximum duration (seconds) of content to retain for startover playback. Omit this attribute or enter ``0`` to indicate that startover playback is disabled for this endpoint.
        :param tags: The tags to assign to the endpoint.
        :param time_delay_seconds: Minimum duration (seconds) of delay to enforce on the playback of live content. Omit this attribute or enter ``0`` to indicate that there is no time delay in effect for this endpoint.
        :param whitelist: The IP addresses that can access this endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediapackage as mediapackage
            
            cfn_origin_endpoint_props = mediapackage.CfnOriginEndpointProps(
                channel_id="channelId",
                id="id",
            
                # the properties below are optional
                authorization=mediapackage.CfnOriginEndpoint.AuthorizationProperty(
                    cdn_identifier_secret="cdnIdentifierSecret",
                    secrets_role_arn="secretsRoleArn"
                ),
                cmaf_package=mediapackage.CfnOriginEndpoint.CmafPackageProperty(
                    encryption=mediapackage.CfnOriginEndpoint.CmafEncryptionProperty(
                        speke_key_provider=mediapackage.CfnOriginEndpoint.SpekeKeyProviderProperty(
                            resource_id="resourceId",
                            role_arn="roleArn",
                            system_ids=["systemIds"],
                            url="url",
            
                            # the properties below are optional
                            certificate_arn="certificateArn",
                            encryption_contract_configuration=mediapackage.CfnOriginEndpoint.EncryptionContractConfigurationProperty(
                                preset_speke20_audio="presetSpeke20Audio",
                                preset_speke20_video="presetSpeke20Video"
                            )
                        ),
            
                        # the properties below are optional
                        constant_initialization_vector="constantInitializationVector",
                        encryption_method="encryptionMethod",
                        key_rotation_interval_seconds=123
                    ),
                    hls_manifests=[mediapackage.CfnOriginEndpoint.HlsManifestProperty(
                        id="id",
            
                        # the properties below are optional
                        ad_markers="adMarkers",
                        ads_on_delivery_restrictions="adsOnDeliveryRestrictions",
                        ad_triggers=["adTriggers"],
                        include_iframe_only_stream=False,
                        manifest_name="manifestName",
                        playlist_type="playlistType",
                        playlist_window_seconds=123,
                        program_date_time_interval_seconds=123,
                        url="url"
                    )],
                    segment_duration_seconds=123,
                    segment_prefix="segmentPrefix",
                    stream_selection=mediapackage.CfnOriginEndpoint.StreamSelectionProperty(
                        max_video_bits_per_second=123,
                        min_video_bits_per_second=123,
                        stream_order="streamOrder"
                    )
                ),
                dash_package=mediapackage.CfnOriginEndpoint.DashPackageProperty(
                    ads_on_delivery_restrictions="adsOnDeliveryRestrictions",
                    ad_triggers=["adTriggers"],
                    encryption=mediapackage.CfnOriginEndpoint.DashEncryptionProperty(
                        speke_key_provider=mediapackage.CfnOriginEndpoint.SpekeKeyProviderProperty(
                            resource_id="resourceId",
                            role_arn="roleArn",
                            system_ids=["systemIds"],
                            url="url",
            
                            # the properties below are optional
                            certificate_arn="certificateArn",
                            encryption_contract_configuration=mediapackage.CfnOriginEndpoint.EncryptionContractConfigurationProperty(
                                preset_speke20_audio="presetSpeke20Audio",
                                preset_speke20_video="presetSpeke20Video"
                            )
                        ),
            
                        # the properties below are optional
                        key_rotation_interval_seconds=123
                    ),
                    include_iframe_only_stream=False,
                    manifest_layout="manifestLayout",
                    manifest_window_seconds=123,
                    min_buffer_time_seconds=123,
                    min_update_period_seconds=123,
                    period_triggers=["periodTriggers"],
                    profile="profile",
                    segment_duration_seconds=123,
                    segment_template_format="segmentTemplateFormat",
                    stream_selection=mediapackage.CfnOriginEndpoint.StreamSelectionProperty(
                        max_video_bits_per_second=123,
                        min_video_bits_per_second=123,
                        stream_order="streamOrder"
                    ),
                    suggested_presentation_delay_seconds=123,
                    utc_timing="utcTiming",
                    utc_timing_uri="utcTimingUri"
                ),
                description="description",
                hls_package=mediapackage.CfnOriginEndpoint.HlsPackageProperty(
                    ad_markers="adMarkers",
                    ads_on_delivery_restrictions="adsOnDeliveryRestrictions",
                    ad_triggers=["adTriggers"],
                    encryption=mediapackage.CfnOriginEndpoint.HlsEncryptionProperty(
                        speke_key_provider=mediapackage.CfnOriginEndpoint.SpekeKeyProviderProperty(
                            resource_id="resourceId",
                            role_arn="roleArn",
                            system_ids=["systemIds"],
                            url="url",
            
                            # the properties below are optional
                            certificate_arn="certificateArn",
                            encryption_contract_configuration=mediapackage.CfnOriginEndpoint.EncryptionContractConfigurationProperty(
                                preset_speke20_audio="presetSpeke20Audio",
                                preset_speke20_video="presetSpeke20Video"
                            )
                        ),
            
                        # the properties below are optional
                        constant_initialization_vector="constantInitializationVector",
                        encryption_method="encryptionMethod",
                        key_rotation_interval_seconds=123,
                        repeat_ext_xKey=False
                    ),
                    include_dvb_subtitles=False,
                    include_iframe_only_stream=False,
                    playlist_type="playlistType",
                    playlist_window_seconds=123,
                    program_date_time_interval_seconds=123,
                    segment_duration_seconds=123,
                    stream_selection=mediapackage.CfnOriginEndpoint.StreamSelectionProperty(
                        max_video_bits_per_second=123,
                        min_video_bits_per_second=123,
                        stream_order="streamOrder"
                    ),
                    use_audio_rendition_group=False
                ),
                manifest_name="manifestName",
                mss_package=mediapackage.CfnOriginEndpoint.MssPackageProperty(
                    encryption=mediapackage.CfnOriginEndpoint.MssEncryptionProperty(
                        speke_key_provider=mediapackage.CfnOriginEndpoint.SpekeKeyProviderProperty(
                            resource_id="resourceId",
                            role_arn="roleArn",
                            system_ids=["systemIds"],
                            url="url",
            
                            # the properties below are optional
                            certificate_arn="certificateArn",
                            encryption_contract_configuration=mediapackage.CfnOriginEndpoint.EncryptionContractConfigurationProperty(
                                preset_speke20_audio="presetSpeke20Audio",
                                preset_speke20_video="presetSpeke20Video"
                            )
                        )
                    ),
                    manifest_window_seconds=123,
                    segment_duration_seconds=123,
                    stream_selection=mediapackage.CfnOriginEndpoint.StreamSelectionProperty(
                        max_video_bits_per_second=123,
                        min_video_bits_per_second=123,
                        stream_order="streamOrder"
                    )
                ),
                origination="origination",
                startover_window_seconds=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                time_delay_seconds=123,
                whitelist=["whitelist"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a638c7220ef09ddd89f3e4ec10fad1f2325778760d9246eae3b5eeddb860f07)
            check_type(argname="argument channel_id", value=channel_id, expected_type=type_hints["channel_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument authorization", value=authorization, expected_type=type_hints["authorization"])
            check_type(argname="argument cmaf_package", value=cmaf_package, expected_type=type_hints["cmaf_package"])
            check_type(argname="argument dash_package", value=dash_package, expected_type=type_hints["dash_package"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument hls_package", value=hls_package, expected_type=type_hints["hls_package"])
            check_type(argname="argument manifest_name", value=manifest_name, expected_type=type_hints["manifest_name"])
            check_type(argname="argument mss_package", value=mss_package, expected_type=type_hints["mss_package"])
            check_type(argname="argument origination", value=origination, expected_type=type_hints["origination"])
            check_type(argname="argument startover_window_seconds", value=startover_window_seconds, expected_type=type_hints["startover_window_seconds"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument time_delay_seconds", value=time_delay_seconds, expected_type=type_hints["time_delay_seconds"])
            check_type(argname="argument whitelist", value=whitelist, expected_type=type_hints["whitelist"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_id": channel_id,
            "id": id,
        }
        if authorization is not None:
            self._values["authorization"] = authorization
        if cmaf_package is not None:
            self._values["cmaf_package"] = cmaf_package
        if dash_package is not None:
            self._values["dash_package"] = dash_package
        if description is not None:
            self._values["description"] = description
        if hls_package is not None:
            self._values["hls_package"] = hls_package
        if manifest_name is not None:
            self._values["manifest_name"] = manifest_name
        if mss_package is not None:
            self._values["mss_package"] = mss_package
        if origination is not None:
            self._values["origination"] = origination
        if startover_window_seconds is not None:
            self._values["startover_window_seconds"] = startover_window_seconds
        if tags is not None:
            self._values["tags"] = tags
        if time_delay_seconds is not None:
            self._values["time_delay_seconds"] = time_delay_seconds
        if whitelist is not None:
            self._values["whitelist"] = whitelist

    @builtins.property
    def channel_id(self) -> builtins.str:
        '''The ID of the channel associated with this endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-channelid
        '''
        result = self._values.get("channel_id")
        assert result is not None, "Required property 'channel_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> builtins.str:
        '''The manifest ID is required and must be unique within the OriginEndpoint.

        The ID can't be changed after the endpoint is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-id
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorization(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.AuthorizationProperty]]:
        '''Parameters for CDN authorization.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-authorization
        '''
        result = self._values.get("authorization")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.AuthorizationProperty]], result)

    @builtins.property
    def cmaf_package(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.CmafPackageProperty]]:
        '''Parameters for Common Media Application Format (CMAF) packaging.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-cmafpackage
        '''
        result = self._values.get("cmaf_package")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.CmafPackageProperty]], result)

    @builtins.property
    def dash_package(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.DashPackageProperty]]:
        '''Parameters for DASH packaging.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-dashpackage
        '''
        result = self._values.get("dash_package")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.DashPackageProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Any descriptive information that you want to add to the endpoint for future identification purposes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hls_package(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.HlsPackageProperty]]:
        '''Parameters for Apple HLS packaging.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-hlspackage
        '''
        result = self._values.get("hls_package")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.HlsPackageProperty]], result)

    @builtins.property
    def manifest_name(self) -> typing.Optional[builtins.str]:
        '''A short string that's appended to the end of the endpoint URL to create a unique path to this endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-manifestname
        '''
        result = self._values.get("manifest_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mss_package(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.MssPackageProperty]]:
        '''Parameters for Microsoft Smooth Streaming packaging.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-msspackage
        '''
        result = self._values.get("mss_package")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.MssPackageProperty]], result)

    @builtins.property
    def origination(self) -> typing.Optional[builtins.str]:
        '''Controls video origination from this endpoint.

        Valid values:

        - ``ALLOW`` - enables this endpoint to serve content to requesting devices.
        - ``DENY`` - prevents this endpoint from serving content. Denying origination is helpful for harvesting live-to-VOD assets. For more information about harvesting and origination, see `Live-to-VOD Requirements <https://docs.aws.amazon.com/mediapackage/latest/ug/ltov-reqmts.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-origination
        '''
        result = self._values.get("origination")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def startover_window_seconds(self) -> typing.Optional[jsii.Number]:
        '''Maximum duration (seconds) of content to retain for startover playback.

        Omit this attribute or enter ``0`` to indicate that startover playback is disabled for this endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-startoverwindowseconds
        '''
        result = self._values.get("startover_window_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to assign to the endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def time_delay_seconds(self) -> typing.Optional[jsii.Number]:
        '''Minimum duration (seconds) of delay to enforce on the playback of live content.

        Omit this attribute or enter ``0`` to indicate that there is no time delay in effect for this endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-timedelayseconds
        '''
        result = self._values.get("time_delay_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def whitelist(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The IP addresses that can access this endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-originendpoint.html#cfn-mediapackage-originendpoint-whitelist
        '''
        result = self._values.get("whitelist")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOriginEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnPackagingConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediapackage.CfnPackagingConfiguration",
):
    '''Creates a packaging configuration in a packaging group.

    The packaging configuration represents a single delivery point for an asset. It determines the format and setting for the egressing content. Specify only one package format per configuration, such as ``HlsPackage`` .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediapackage as mediapackage
        
        cfn_packaging_configuration = mediapackage.CfnPackagingConfiguration(self, "MyCfnPackagingConfiguration",
            id="id",
            packaging_group_id="packagingGroupId",
        
            # the properties below are optional
            cmaf_package=mediapackage.CfnPackagingConfiguration.CmafPackageProperty(
                hls_manifests=[mediapackage.CfnPackagingConfiguration.HlsManifestProperty(
                    ad_markers="adMarkers",
                    include_iframe_only_stream=False,
                    manifest_name="manifestName",
                    program_date_time_interval_seconds=123,
                    repeat_ext_xKey=False,
                    stream_selection=mediapackage.CfnPackagingConfiguration.StreamSelectionProperty(
                        max_video_bits_per_second=123,
                        min_video_bits_per_second=123,
                        stream_order="streamOrder"
                    )
                )],
        
                # the properties below are optional
                encryption=mediapackage.CfnPackagingConfiguration.CmafEncryptionProperty(
                    speke_key_provider=mediapackage.CfnPackagingConfiguration.SpekeKeyProviderProperty(
                        role_arn="roleArn",
                        system_ids=["systemIds"],
                        url="url",
        
                        # the properties below are optional
                        encryption_contract_configuration=mediapackage.CfnPackagingConfiguration.EncryptionContractConfigurationProperty(
                            preset_speke20_audio="presetSpeke20Audio",
                            preset_speke20_video="presetSpeke20Video"
                        )
                    )
                ),
                include_encoder_configuration_in_segments=False,
                segment_duration_seconds=123
            ),
            dash_package=mediapackage.CfnPackagingConfiguration.DashPackageProperty(
                dash_manifests=[mediapackage.CfnPackagingConfiguration.DashManifestProperty(
                    manifest_layout="manifestLayout",
                    manifest_name="manifestName",
                    min_buffer_time_seconds=123,
                    profile="profile",
                    scte_markers_source="scteMarkersSource",
                    stream_selection=mediapackage.CfnPackagingConfiguration.StreamSelectionProperty(
                        max_video_bits_per_second=123,
                        min_video_bits_per_second=123,
                        stream_order="streamOrder"
                    )
                )],
        
                # the properties below are optional
                encryption=mediapackage.CfnPackagingConfiguration.DashEncryptionProperty(
                    speke_key_provider=mediapackage.CfnPackagingConfiguration.SpekeKeyProviderProperty(
                        role_arn="roleArn",
                        system_ids=["systemIds"],
                        url="url",
        
                        # the properties below are optional
                        encryption_contract_configuration=mediapackage.CfnPackagingConfiguration.EncryptionContractConfigurationProperty(
                            preset_speke20_audio="presetSpeke20Audio",
                            preset_speke20_video="presetSpeke20Video"
                        )
                    )
                ),
                include_encoder_configuration_in_segments=False,
                include_iframe_only_stream=False,
                period_triggers=["periodTriggers"],
                segment_duration_seconds=123,
                segment_template_format="segmentTemplateFormat"
            ),
            hls_package=mediapackage.CfnPackagingConfiguration.HlsPackageProperty(
                hls_manifests=[mediapackage.CfnPackagingConfiguration.HlsManifestProperty(
                    ad_markers="adMarkers",
                    include_iframe_only_stream=False,
                    manifest_name="manifestName",
                    program_date_time_interval_seconds=123,
                    repeat_ext_xKey=False,
                    stream_selection=mediapackage.CfnPackagingConfiguration.StreamSelectionProperty(
                        max_video_bits_per_second=123,
                        min_video_bits_per_second=123,
                        stream_order="streamOrder"
                    )
                )],
        
                # the properties below are optional
                encryption=mediapackage.CfnPackagingConfiguration.HlsEncryptionProperty(
                    speke_key_provider=mediapackage.CfnPackagingConfiguration.SpekeKeyProviderProperty(
                        role_arn="roleArn",
                        system_ids=["systemIds"],
                        url="url",
        
                        # the properties below are optional
                        encryption_contract_configuration=mediapackage.CfnPackagingConfiguration.EncryptionContractConfigurationProperty(
                            preset_speke20_audio="presetSpeke20Audio",
                            preset_speke20_video="presetSpeke20Video"
                        )
                    ),
        
                    # the properties below are optional
                    constant_initialization_vector="constantInitializationVector",
                    encryption_method="encryptionMethod"
                ),
                include_dvb_subtitles=False,
                segment_duration_seconds=123,
                use_audio_rendition_group=False
            ),
            mss_package=mediapackage.CfnPackagingConfiguration.MssPackageProperty(
                mss_manifests=[mediapackage.CfnPackagingConfiguration.MssManifestProperty(
                    manifest_name="manifestName",
                    stream_selection=mediapackage.CfnPackagingConfiguration.StreamSelectionProperty(
                        max_video_bits_per_second=123,
                        min_video_bits_per_second=123,
                        stream_order="streamOrder"
                    )
                )],
        
                # the properties below are optional
                encryption=mediapackage.CfnPackagingConfiguration.MssEncryptionProperty(
                    speke_key_provider=mediapackage.CfnPackagingConfiguration.SpekeKeyProviderProperty(
                        role_arn="roleArn",
                        system_ids=["systemIds"],
                        url="url",
        
                        # the properties below are optional
                        encryption_contract_configuration=mediapackage.CfnPackagingConfiguration.EncryptionContractConfigurationProperty(
                            preset_speke20_audio="presetSpeke20Audio",
                            preset_speke20_video="presetSpeke20Video"
                        )
                    )
                ),
                segment_duration_seconds=123
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
        id_: builtins.str,
        *,
        id: builtins.str,
        packaging_group_id: builtins.str,
        cmaf_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackagingConfiguration.CmafPackageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        dash_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackagingConfiguration.DashPackageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        hls_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackagingConfiguration.HlsPackageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        mss_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackagingConfiguration.MssPackageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id_: Construct identifier for this resource (unique in its scope).
        :param id: Unique identifier that you assign to the packaging configuration.
        :param packaging_group_id: The ID of the packaging group associated with this packaging configuration.
        :param cmaf_package: Parameters for CMAF packaging.
        :param dash_package: Parameters for DASH-ISO packaging.
        :param hls_package: Parameters for Apple HLS packaging.
        :param mss_package: Parameters for Microsoft Smooth Streaming packaging.
        :param tags: The tags to assign to the packaging configuration.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__832773f8276f2faf0375005ff4da2278882f295916abd90cfb3e88d27eae60a2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        props = CfnPackagingConfigurationProps(
            id=id,
            packaging_group_id=packaging_group_id,
            cmaf_package=cmaf_package,
            dash_package=dash_package,
            hls_package=hls_package,
            mss_package=mss_package,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id_, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7ec79234b846ccf4526d21383984a066ad27bec0c2e18914091e7914cd114d5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3d9c55f0f743c67ba5f7aa4a3cd9e62904c8332212ea90f623849c6606305faf)
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
        '''The Amazon Resource Name (ARN) for the packaging configuration.

        You can get this from the response to any request to the packaging configuration.

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
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''Unique identifier that you assign to the packaging configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ccd7097ed4dd1ba043d8d7c9253de38870b8dbd6a68978af0352c0722f1d408)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="packagingGroupId")
    def packaging_group_id(self) -> builtins.str:
        '''The ID of the packaging group associated with this packaging configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "packagingGroupId"))

    @packaging_group_id.setter
    def packaging_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af2d37d8a33d032c8adfec86f32ed79504eb5a23c3a492af26657f35f9c92c25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "packagingGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="cmafPackage")
    def cmaf_package(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.CmafPackageProperty"]]:
        '''Parameters for CMAF packaging.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.CmafPackageProperty"]], jsii.get(self, "cmafPackage"))

    @cmaf_package.setter
    def cmaf_package(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.CmafPackageProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__399ba5c2786cade2c25cb41b1be97be2455fdf5dfbae120613c3942b2fca070b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cmafPackage", value)

    @builtins.property
    @jsii.member(jsii_name="dashPackage")
    def dash_package(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.DashPackageProperty"]]:
        '''Parameters for DASH-ISO packaging.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.DashPackageProperty"]], jsii.get(self, "dashPackage"))

    @dash_package.setter
    def dash_package(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.DashPackageProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d5ed5948330815ccf88262bb614ff3bfcfee39a50c798ef93f31fd435b0cb0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dashPackage", value)

    @builtins.property
    @jsii.member(jsii_name="hlsPackage")
    def hls_package(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.HlsPackageProperty"]]:
        '''Parameters for Apple HLS packaging.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.HlsPackageProperty"]], jsii.get(self, "hlsPackage"))

    @hls_package.setter
    def hls_package(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.HlsPackageProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d206943acdbd5b0d12e1841cff1d1941ed07fb9970ebf2c082e7e5128cc3bfd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hlsPackage", value)

    @builtins.property
    @jsii.member(jsii_name="mssPackage")
    def mss_package(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.MssPackageProperty"]]:
        '''Parameters for Microsoft Smooth Streaming packaging.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.MssPackageProperty"]], jsii.get(self, "mssPackage"))

    @mss_package.setter
    def mss_package(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.MssPackageProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7861bbe260077025f4e33fb0ae4337195d16c1ee61d7047a4a9952ab287f760)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mssPackage", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to assign to the packaging configuration.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b76635d4a00dd9342ff2aee3d299dfc0b57f29c37ac4af92f1dcc355e82475a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnPackagingConfiguration.CmafEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={"speke_key_provider": "spekeKeyProvider"},
    )
    class CmafEncryptionProperty:
        def __init__(
            self,
            *,
            speke_key_provider: typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackagingConfiguration.SpekeKeyProviderProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Holds encryption information so that access to the content can be controlled by a DRM solution.

            :param speke_key_provider: Parameters for the SPEKE key provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafencryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                cmaf_encryption_property = mediapackage.CfnPackagingConfiguration.CmafEncryptionProperty(
                    speke_key_provider=mediapackage.CfnPackagingConfiguration.SpekeKeyProviderProperty(
                        role_arn="roleArn",
                        system_ids=["systemIds"],
                        url="url",
                
                        # the properties below are optional
                        encryption_contract_configuration=mediapackage.CfnPackagingConfiguration.EncryptionContractConfigurationProperty(
                            preset_speke20_audio="presetSpeke20Audio",
                            preset_speke20_video="presetSpeke20Video"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c9524f29fa700d32f03cb88bcaf888d88fd8f7cf49d65982f907421d51bf1e5b)
                check_type(argname="argument speke_key_provider", value=speke_key_provider, expected_type=type_hints["speke_key_provider"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "speke_key_provider": speke_key_provider,
            }

        @builtins.property
        def speke_key_provider(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.SpekeKeyProviderProperty"]:
            '''Parameters for the SPEKE key provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafencryption.html#cfn-mediapackage-packagingconfiguration-cmafencryption-spekekeyprovider
            '''
            result = self._values.get("speke_key_provider")
            assert result is not None, "Required property 'speke_key_provider' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.SpekeKeyProviderProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CmafEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnPackagingConfiguration.CmafPackageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hls_manifests": "hlsManifests",
            "encryption": "encryption",
            "include_encoder_configuration_in_segments": "includeEncoderConfigurationInSegments",
            "segment_duration_seconds": "segmentDurationSeconds",
        },
    )
    class CmafPackageProperty:
        def __init__(
            self,
            *,
            hls_manifests: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackagingConfiguration.HlsManifestProperty", typing.Dict[builtins.str, typing.Any]]]]],
            encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackagingConfiguration.CmafEncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            include_encoder_configuration_in_segments: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            segment_duration_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Parameters for a packaging configuration that uses Common Media Application Format (CMAF) packaging.

            :param hls_manifests: A list of HLS manifest configurations that are available from this endpoint.
            :param encryption: Parameters for encrypting content.
            :param include_encoder_configuration_in_segments: When includeEncoderConfigurationInSegments is set to true, AWS Elemental MediaPackage places your encoder's Sequence Parameter Set (SPS), Picture Parameter Set (PPS), and Video Parameter Set (VPS) metadata in every video segment instead of in the init fragment. This lets you use different SPS/PPS/VPS settings for your assets during content playback.
            :param segment_duration_seconds: Duration (in seconds) of each segment. Actual segments are rounded to the nearest multiple of the source fragment duration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                cmaf_package_property = mediapackage.CfnPackagingConfiguration.CmafPackageProperty(
                    hls_manifests=[mediapackage.CfnPackagingConfiguration.HlsManifestProperty(
                        ad_markers="adMarkers",
                        include_iframe_only_stream=False,
                        manifest_name="manifestName",
                        program_date_time_interval_seconds=123,
                        repeat_ext_xKey=False,
                        stream_selection=mediapackage.CfnPackagingConfiguration.StreamSelectionProperty(
                            max_video_bits_per_second=123,
                            min_video_bits_per_second=123,
                            stream_order="streamOrder"
                        )
                    )],
                
                    # the properties below are optional
                    encryption=mediapackage.CfnPackagingConfiguration.CmafEncryptionProperty(
                        speke_key_provider=mediapackage.CfnPackagingConfiguration.SpekeKeyProviderProperty(
                            role_arn="roleArn",
                            system_ids=["systemIds"],
                            url="url",
                
                            # the properties below are optional
                            encryption_contract_configuration=mediapackage.CfnPackagingConfiguration.EncryptionContractConfigurationProperty(
                                preset_speke20_audio="presetSpeke20Audio",
                                preset_speke20_video="presetSpeke20Video"
                            )
                        )
                    ),
                    include_encoder_configuration_in_segments=False,
                    segment_duration_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3c702574616d01dedc86e0ed18adf341d64a65dc25d07e27989cf1a7627cdc3f)
                check_type(argname="argument hls_manifests", value=hls_manifests, expected_type=type_hints["hls_manifests"])
                check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
                check_type(argname="argument include_encoder_configuration_in_segments", value=include_encoder_configuration_in_segments, expected_type=type_hints["include_encoder_configuration_in_segments"])
                check_type(argname="argument segment_duration_seconds", value=segment_duration_seconds, expected_type=type_hints["segment_duration_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "hls_manifests": hls_manifests,
            }
            if encryption is not None:
                self._values["encryption"] = encryption
            if include_encoder_configuration_in_segments is not None:
                self._values["include_encoder_configuration_in_segments"] = include_encoder_configuration_in_segments
            if segment_duration_seconds is not None:
                self._values["segment_duration_seconds"] = segment_duration_seconds

        @builtins.property
        def hls_manifests(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.HlsManifestProperty"]]]:
            '''A list of HLS manifest configurations that are available from this endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html#cfn-mediapackage-packagingconfiguration-cmafpackage-hlsmanifests
            '''
            result = self._values.get("hls_manifests")
            assert result is not None, "Required property 'hls_manifests' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.HlsManifestProperty"]]], result)

        @builtins.property
        def encryption(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.CmafEncryptionProperty"]]:
            '''Parameters for encrypting content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html#cfn-mediapackage-packagingconfiguration-cmafpackage-encryption
            '''
            result = self._values.get("encryption")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.CmafEncryptionProperty"]], result)

        @builtins.property
        def include_encoder_configuration_in_segments(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When includeEncoderConfigurationInSegments is set to true, AWS Elemental MediaPackage places your encoder's Sequence Parameter Set (SPS), Picture Parameter Set (PPS), and Video Parameter Set (VPS) metadata in every video segment instead of in the init fragment.

            This lets you use different SPS/PPS/VPS settings for your assets during content playback.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html#cfn-mediapackage-packagingconfiguration-cmafpackage-includeencoderconfigurationinsegments
            '''
            result = self._values.get("include_encoder_configuration_in_segments")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def segment_duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''Duration (in seconds) of each segment.

            Actual segments are rounded to the nearest multiple of the source fragment duration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-cmafpackage.html#cfn-mediapackage-packagingconfiguration-cmafpackage-segmentdurationseconds
            '''
            result = self._values.get("segment_duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CmafPackageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnPackagingConfiguration.DashEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={"speke_key_provider": "spekeKeyProvider"},
    )
    class DashEncryptionProperty:
        def __init__(
            self,
            *,
            speke_key_provider: typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackagingConfiguration.SpekeKeyProviderProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Holds encryption information so that access to the content can be controlled by a DRM solution.

            :param speke_key_provider: Parameters for the SPEKE key provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashencryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                dash_encryption_property = mediapackage.CfnPackagingConfiguration.DashEncryptionProperty(
                    speke_key_provider=mediapackage.CfnPackagingConfiguration.SpekeKeyProviderProperty(
                        role_arn="roleArn",
                        system_ids=["systemIds"],
                        url="url",
                
                        # the properties below are optional
                        encryption_contract_configuration=mediapackage.CfnPackagingConfiguration.EncryptionContractConfigurationProperty(
                            preset_speke20_audio="presetSpeke20Audio",
                            preset_speke20_video="presetSpeke20Video"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ed10aaf0f578003dd8303a56dd49c8e049f64afd412a966e5158993e671c9449)
                check_type(argname="argument speke_key_provider", value=speke_key_provider, expected_type=type_hints["speke_key_provider"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "speke_key_provider": speke_key_provider,
            }

        @builtins.property
        def speke_key_provider(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.SpekeKeyProviderProperty"]:
            '''Parameters for the SPEKE key provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashencryption.html#cfn-mediapackage-packagingconfiguration-dashencryption-spekekeyprovider
            '''
            result = self._values.get("speke_key_provider")
            assert result is not None, "Required property 'speke_key_provider' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.SpekeKeyProviderProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnPackagingConfiguration.DashManifestProperty",
        jsii_struct_bases=[],
        name_mapping={
            "manifest_layout": "manifestLayout",
            "manifest_name": "manifestName",
            "min_buffer_time_seconds": "minBufferTimeSeconds",
            "profile": "profile",
            "scte_markers_source": "scteMarkersSource",
            "stream_selection": "streamSelection",
        },
    )
    class DashManifestProperty:
        def __init__(
            self,
            *,
            manifest_layout: typing.Optional[builtins.str] = None,
            manifest_name: typing.Optional[builtins.str] = None,
            min_buffer_time_seconds: typing.Optional[jsii.Number] = None,
            profile: typing.Optional[builtins.str] = None,
            scte_markers_source: typing.Optional[builtins.str] = None,
            stream_selection: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackagingConfiguration.StreamSelectionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Parameters for a DASH manifest.

            :param manifest_layout: Determines the position of some tags in the Media Presentation Description (MPD). When set to ``FULL`` , elements like ``SegmentTemplate`` and ``ContentProtection`` are included in each ``Representation`` . When set to ``COMPACT`` , duplicate elements are combined and presented at the AdaptationSet level.
            :param manifest_name: A short string that's appended to the end of the endpoint URL to create a unique path to this packaging configuration.
            :param min_buffer_time_seconds: Minimum amount of content (measured in seconds) that a player must keep available in the buffer.
            :param profile: The DASH profile type. When set to ``HBBTV_1_5`` , the content is compliant with HbbTV 1.5.
            :param scte_markers_source: The source of scte markers used. Value description: - ``SEGMENTS`` - The scte markers are sourced from the segments of the ingested content. - ``MANIFEST`` - the scte markers are sourced from the manifest of the ingested content. The MANIFEST value is compatible with source HLS playlists using the SCTE-35 Enhanced syntax ( ``EXT-OATCLS-SCTE35`` tags). SCTE-35 Elemental and SCTE-35 Daterange syntaxes are not supported with this option.
            :param stream_selection: Limitations for outputs from the endpoint, based on the video bitrate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                dash_manifest_property = mediapackage.CfnPackagingConfiguration.DashManifestProperty(
                    manifest_layout="manifestLayout",
                    manifest_name="manifestName",
                    min_buffer_time_seconds=123,
                    profile="profile",
                    scte_markers_source="scteMarkersSource",
                    stream_selection=mediapackage.CfnPackagingConfiguration.StreamSelectionProperty(
                        max_video_bits_per_second=123,
                        min_video_bits_per_second=123,
                        stream_order="streamOrder"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8d63cccb6b1149c27c25ba78c9e135dc5dc3329c0074867c06f2202b77fd09e7)
                check_type(argname="argument manifest_layout", value=manifest_layout, expected_type=type_hints["manifest_layout"])
                check_type(argname="argument manifest_name", value=manifest_name, expected_type=type_hints["manifest_name"])
                check_type(argname="argument min_buffer_time_seconds", value=min_buffer_time_seconds, expected_type=type_hints["min_buffer_time_seconds"])
                check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
                check_type(argname="argument scte_markers_source", value=scte_markers_source, expected_type=type_hints["scte_markers_source"])
                check_type(argname="argument stream_selection", value=stream_selection, expected_type=type_hints["stream_selection"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if manifest_layout is not None:
                self._values["manifest_layout"] = manifest_layout
            if manifest_name is not None:
                self._values["manifest_name"] = manifest_name
            if min_buffer_time_seconds is not None:
                self._values["min_buffer_time_seconds"] = min_buffer_time_seconds
            if profile is not None:
                self._values["profile"] = profile
            if scte_markers_source is not None:
                self._values["scte_markers_source"] = scte_markers_source
            if stream_selection is not None:
                self._values["stream_selection"] = stream_selection

        @builtins.property
        def manifest_layout(self) -> typing.Optional[builtins.str]:
            '''Determines the position of some tags in the Media Presentation Description (MPD).

            When set to ``FULL`` , elements like ``SegmentTemplate`` and ``ContentProtection`` are included in each ``Representation`` . When set to ``COMPACT`` , duplicate elements are combined and presented at the AdaptationSet level.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-manifestlayout
            '''
            result = self._values.get("manifest_layout")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def manifest_name(self) -> typing.Optional[builtins.str]:
            '''A short string that's appended to the end of the endpoint URL to create a unique path to this packaging configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-manifestname
            '''
            result = self._values.get("manifest_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def min_buffer_time_seconds(self) -> typing.Optional[jsii.Number]:
            '''Minimum amount of content (measured in seconds) that a player must keep available in the buffer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-minbuffertimeseconds
            '''
            result = self._values.get("min_buffer_time_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def profile(self) -> typing.Optional[builtins.str]:
            '''The DASH profile type.

            When set to ``HBBTV_1_5`` , the content is compliant with HbbTV 1.5.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-profile
            '''
            result = self._values.get("profile")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def scte_markers_source(self) -> typing.Optional[builtins.str]:
            '''The source of scte markers used.

            Value description:

            - ``SEGMENTS`` - The scte markers are sourced from the segments of the ingested content.
            - ``MANIFEST`` - the scte markers are sourced from the manifest of the ingested content. The MANIFEST value is compatible with source HLS playlists using the SCTE-35 Enhanced syntax ( ``EXT-OATCLS-SCTE35`` tags). SCTE-35 Elemental and SCTE-35 Daterange syntaxes are not supported with this option.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-sctemarkerssource
            '''
            result = self._values.get("scte_markers_source")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def stream_selection(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.StreamSelectionProperty"]]:
            '''Limitations for outputs from the endpoint, based on the video bitrate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashmanifest.html#cfn-mediapackage-packagingconfiguration-dashmanifest-streamselection
            '''
            result = self._values.get("stream_selection")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.StreamSelectionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashManifestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnPackagingConfiguration.DashPackageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dash_manifests": "dashManifests",
            "encryption": "encryption",
            "include_encoder_configuration_in_segments": "includeEncoderConfigurationInSegments",
            "include_iframe_only_stream": "includeIframeOnlyStream",
            "period_triggers": "periodTriggers",
            "segment_duration_seconds": "segmentDurationSeconds",
            "segment_template_format": "segmentTemplateFormat",
        },
    )
    class DashPackageProperty:
        def __init__(
            self,
            *,
            dash_manifests: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackagingConfiguration.DashManifestProperty", typing.Dict[builtins.str, typing.Any]]]]],
            encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackagingConfiguration.DashEncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            include_encoder_configuration_in_segments: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_iframe_only_stream: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            period_triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
            segment_duration_seconds: typing.Optional[jsii.Number] = None,
            segment_template_format: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Parameters for a packaging configuration that uses Dynamic Adaptive Streaming over HTTP (DASH) packaging.

            :param dash_manifests: A list of DASH manifest configurations that are available from this endpoint.
            :param encryption: Parameters for encrypting content.
            :param include_encoder_configuration_in_segments: When includeEncoderConfigurationInSegments is set to true, AWS Elemental MediaPackage places your encoder's Sequence Parameter Set (SPS), Picture Parameter Set (PPS), and Video Parameter Set (VPS) metadata in every video segment instead of in the init fragment. This lets you use different SPS/PPS/VPS settings for your assets during content playback.
            :param include_iframe_only_stream: This applies only to stream sets with a single video track. When true, the stream set includes an additional I-frame trick-play only stream, along with the other tracks. If false, this extra stream is not included.
            :param period_triggers: Controls whether AWS Elemental MediaPackage produces single-period or multi-period DASH manifests. For more information about periods, see `Multi-period DASH in AWS Elemental MediaPackage <https://docs.aws.amazon.com/mediapackage/latest/ug/multi-period.html>`_ . Valid values: - ``ADS`` - AWS Elemental MediaPackage will produce multi-period DASH manifests. Periods are created based on the SCTE-35 ad markers present in the input manifest. - *No value* - AWS Elemental MediaPackage will produce single-period DASH manifests. This is the default setting.
            :param segment_duration_seconds: Duration (in seconds) of each fragment. Actual fragments are rounded to the nearest multiple of the source segment duration.
            :param segment_template_format: Determines the type of SegmentTemplate included in the Media Presentation Description (MPD). When set to ``NUMBER_WITH_TIMELINE`` , a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to ``TIME_WITH_TIMELINE`` , a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to ``NUMBER_WITH_DURATION`` , only a duration is included in each SegmentTemplate, with $Number$ media URLs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                dash_package_property = mediapackage.CfnPackagingConfiguration.DashPackageProperty(
                    dash_manifests=[mediapackage.CfnPackagingConfiguration.DashManifestProperty(
                        manifest_layout="manifestLayout",
                        manifest_name="manifestName",
                        min_buffer_time_seconds=123,
                        profile="profile",
                        scte_markers_source="scteMarkersSource",
                        stream_selection=mediapackage.CfnPackagingConfiguration.StreamSelectionProperty(
                            max_video_bits_per_second=123,
                            min_video_bits_per_second=123,
                            stream_order="streamOrder"
                        )
                    )],
                
                    # the properties below are optional
                    encryption=mediapackage.CfnPackagingConfiguration.DashEncryptionProperty(
                        speke_key_provider=mediapackage.CfnPackagingConfiguration.SpekeKeyProviderProperty(
                            role_arn="roleArn",
                            system_ids=["systemIds"],
                            url="url",
                
                            # the properties below are optional
                            encryption_contract_configuration=mediapackage.CfnPackagingConfiguration.EncryptionContractConfigurationProperty(
                                preset_speke20_audio="presetSpeke20Audio",
                                preset_speke20_video="presetSpeke20Video"
                            )
                        )
                    ),
                    include_encoder_configuration_in_segments=False,
                    include_iframe_only_stream=False,
                    period_triggers=["periodTriggers"],
                    segment_duration_seconds=123,
                    segment_template_format="segmentTemplateFormat"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__422b40df588f5b400b121c9d8c5b629c038a8d7a2749bbfff023fbfcd76cc148)
                check_type(argname="argument dash_manifests", value=dash_manifests, expected_type=type_hints["dash_manifests"])
                check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
                check_type(argname="argument include_encoder_configuration_in_segments", value=include_encoder_configuration_in_segments, expected_type=type_hints["include_encoder_configuration_in_segments"])
                check_type(argname="argument include_iframe_only_stream", value=include_iframe_only_stream, expected_type=type_hints["include_iframe_only_stream"])
                check_type(argname="argument period_triggers", value=period_triggers, expected_type=type_hints["period_triggers"])
                check_type(argname="argument segment_duration_seconds", value=segment_duration_seconds, expected_type=type_hints["segment_duration_seconds"])
                check_type(argname="argument segment_template_format", value=segment_template_format, expected_type=type_hints["segment_template_format"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "dash_manifests": dash_manifests,
            }
            if encryption is not None:
                self._values["encryption"] = encryption
            if include_encoder_configuration_in_segments is not None:
                self._values["include_encoder_configuration_in_segments"] = include_encoder_configuration_in_segments
            if include_iframe_only_stream is not None:
                self._values["include_iframe_only_stream"] = include_iframe_only_stream
            if period_triggers is not None:
                self._values["period_triggers"] = period_triggers
            if segment_duration_seconds is not None:
                self._values["segment_duration_seconds"] = segment_duration_seconds
            if segment_template_format is not None:
                self._values["segment_template_format"] = segment_template_format

        @builtins.property
        def dash_manifests(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.DashManifestProperty"]]]:
            '''A list of DASH manifest configurations that are available from this endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-dashmanifests
            '''
            result = self._values.get("dash_manifests")
            assert result is not None, "Required property 'dash_manifests' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.DashManifestProperty"]]], result)

        @builtins.property
        def encryption(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.DashEncryptionProperty"]]:
            '''Parameters for encrypting content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-encryption
            '''
            result = self._values.get("encryption")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.DashEncryptionProperty"]], result)

        @builtins.property
        def include_encoder_configuration_in_segments(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When includeEncoderConfigurationInSegments is set to true, AWS Elemental MediaPackage places your encoder's Sequence Parameter Set (SPS), Picture Parameter Set (PPS), and Video Parameter Set (VPS) metadata in every video segment instead of in the init fragment.

            This lets you use different SPS/PPS/VPS settings for your assets during content playback.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-includeencoderconfigurationinsegments
            '''
            result = self._values.get("include_encoder_configuration_in_segments")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_iframe_only_stream(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''This applies only to stream sets with a single video track.

            When true, the stream set includes an additional I-frame trick-play only stream, along with the other tracks. If false, this extra stream is not included.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-includeiframeonlystream
            '''
            result = self._values.get("include_iframe_only_stream")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def period_triggers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Controls whether AWS Elemental MediaPackage produces single-period or multi-period DASH manifests.

            For more information about periods, see `Multi-period DASH in AWS Elemental MediaPackage <https://docs.aws.amazon.com/mediapackage/latest/ug/multi-period.html>`_ .

            Valid values:

            - ``ADS`` - AWS Elemental MediaPackage will produce multi-period DASH manifests. Periods are created based on the SCTE-35 ad markers present in the input manifest.
            - *No value* - AWS Elemental MediaPackage will produce single-period DASH manifests. This is the default setting.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-periodtriggers
            '''
            result = self._values.get("period_triggers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def segment_duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''Duration (in seconds) of each fragment.

            Actual fragments are rounded to the nearest multiple of the source segment duration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-segmentdurationseconds
            '''
            result = self._values.get("segment_duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def segment_template_format(self) -> typing.Optional[builtins.str]:
            '''Determines the type of SegmentTemplate included in the Media Presentation Description (MPD).

            When set to ``NUMBER_WITH_TIMELINE`` , a full timeline is presented in each SegmentTemplate, with $Number$ media URLs. When set to ``TIME_WITH_TIMELINE`` , a full timeline is presented in each SegmentTemplate, with $Time$ media URLs. When set to ``NUMBER_WITH_DURATION`` , only a duration is included in each SegmentTemplate, with $Number$ media URLs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-dashpackage.html#cfn-mediapackage-packagingconfiguration-dashpackage-segmenttemplateformat
            '''
            result = self._values.get("segment_template_format")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashPackageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnPackagingConfiguration.EncryptionContractConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "preset_speke20_audio": "presetSpeke20Audio",
            "preset_speke20_video": "presetSpeke20Video",
        },
    )
    class EncryptionContractConfigurationProperty:
        def __init__(
            self,
            *,
            preset_speke20_audio: builtins.str,
            preset_speke20_video: builtins.str,
        ) -> None:
            '''Use ``encryptionContractConfiguration`` to configure one or more content encryption keys for your endpoints that use SPEKE Version 2.0. The encryption contract defines the content keys used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use. For more information about these presets, see `SPEKE Version 2.0 Presets <https://docs.aws.amazon.com/mediapackage/latest/ug/drm-content-speke-v2-presets.html>`_ .

            Note the following considerations when using ``encryptionContractConfiguration`` :

            - You can use ``encryptionContractConfiguration`` for DASH endpoints that use SPEKE Version 2.0. SPEKE Version 2.0 relies on the CPIX Version 2.3 specification.
            - You cannot combine an ``UNENCRYPTED`` preset with ``UNENCRYPTED`` or ``SHARED`` presets across ``presetSpeke20Audio`` and ``presetSpeke20Video`` .
            - When you use a ``SHARED`` preset, you must use it for both ``presetSpeke20Audio`` and ``presetSpeke20Video`` .

            :param preset_speke20_audio: A collection of audio encryption presets. Value description: - ``PRESET-AUDIO-1`` - Use one content key to encrypt all of the audio tracks in your stream. - ``PRESET-AUDIO-2`` - Use one content key to encrypt all of the stereo audio tracks and one content key to encrypt all of the multichannel audio tracks. - ``PRESET-AUDIO-3`` - Use one content key to encrypt all of the stereo audio tracks, one content key to encrypt all of the multichannel audio tracks with 3 to 6 channels, and one content key to encrypt all of the multichannel audio tracks with more than 6 channels. - ``SHARED`` - Use the same content key for all of the audio and video tracks in your stream. - ``UNENCRYPTED`` - Don't encrypt any of the audio tracks in your stream.
            :param preset_speke20_video: A collection of video encryption presets. Value description: - ``PRESET-VIDEO-1`` - Use one content key to encrypt all of the video tracks in your stream. - ``PRESET-VIDEO-2`` - Use one content key to encrypt all of the SD video tracks and one content key for all HD and higher resolutions video tracks. - ``PRESET-VIDEO-3`` - Use one content key to encrypt all of the SD video tracks, one content key for HD video tracks and one content key for all UHD video tracks. - ``PRESET-VIDEO-4`` - Use one content key to encrypt all of the SD video tracks, one content key for HD video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks. - ``PRESET-VIDEO-5`` - Use one content key to encrypt all of the SD video tracks, one content key for HD1 video tracks, one content key for HD2 video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks. - ``PRESET-VIDEO-6`` - Use one content key to encrypt all of the SD video tracks, one content key for HD1 video tracks, one content key for HD2 video tracks and one content key for all UHD video tracks. - ``PRESET-VIDEO-7`` - Use one content key to encrypt all of the SD+HD1 video tracks, one content key for HD2 video tracks and one content key for all UHD video tracks. - ``PRESET-VIDEO-8`` - Use one content key to encrypt all of the SD+HD1 video tracks, one content key for HD2 video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks. - ``SHARED`` - Use the same content key for all of the video and audio tracks in your stream. - ``UNENCRYPTED`` - Don't encrypt any of the video tracks in your stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-encryptioncontractconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                encryption_contract_configuration_property = mediapackage.CfnPackagingConfiguration.EncryptionContractConfigurationProperty(
                    preset_speke20_audio="presetSpeke20Audio",
                    preset_speke20_video="presetSpeke20Video"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ad4a42ef0d5a0f06be0bfc9686a1d03d8c6adffc71b0b1fd88167f62d2451ff2)
                check_type(argname="argument preset_speke20_audio", value=preset_speke20_audio, expected_type=type_hints["preset_speke20_audio"])
                check_type(argname="argument preset_speke20_video", value=preset_speke20_video, expected_type=type_hints["preset_speke20_video"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "preset_speke20_audio": preset_speke20_audio,
                "preset_speke20_video": preset_speke20_video,
            }

        @builtins.property
        def preset_speke20_audio(self) -> builtins.str:
            '''A collection of audio encryption presets.

            Value description:

            - ``PRESET-AUDIO-1`` - Use one content key to encrypt all of the audio tracks in your stream.
            - ``PRESET-AUDIO-2`` - Use one content key to encrypt all of the stereo audio tracks and one content key to encrypt all of the multichannel audio tracks.
            - ``PRESET-AUDIO-3`` - Use one content key to encrypt all of the stereo audio tracks, one content key to encrypt all of the multichannel audio tracks with 3 to 6 channels, and one content key to encrypt all of the multichannel audio tracks with more than 6 channels.
            - ``SHARED`` - Use the same content key for all of the audio and video tracks in your stream.
            - ``UNENCRYPTED`` - Don't encrypt any of the audio tracks in your stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-encryptioncontractconfiguration.html#cfn-mediapackage-packagingconfiguration-encryptioncontractconfiguration-presetspeke20audio
            '''
            result = self._values.get("preset_speke20_audio")
            assert result is not None, "Required property 'preset_speke20_audio' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def preset_speke20_video(self) -> builtins.str:
            '''A collection of video encryption presets.

            Value description:

            - ``PRESET-VIDEO-1`` - Use one content key to encrypt all of the video tracks in your stream.
            - ``PRESET-VIDEO-2`` - Use one content key to encrypt all of the SD video tracks and one content key for all HD and higher resolutions video tracks.
            - ``PRESET-VIDEO-3`` - Use one content key to encrypt all of the SD video tracks, one content key for HD video tracks and one content key for all UHD video tracks.
            - ``PRESET-VIDEO-4`` - Use one content key to encrypt all of the SD video tracks, one content key for HD video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks.
            - ``PRESET-VIDEO-5`` - Use one content key to encrypt all of the SD video tracks, one content key for HD1 video tracks, one content key for HD2 video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks.
            - ``PRESET-VIDEO-6`` - Use one content key to encrypt all of the SD video tracks, one content key for HD1 video tracks, one content key for HD2 video tracks and one content key for all UHD video tracks.
            - ``PRESET-VIDEO-7`` - Use one content key to encrypt all of the SD+HD1 video tracks, one content key for HD2 video tracks and one content key for all UHD video tracks.
            - ``PRESET-VIDEO-8`` - Use one content key to encrypt all of the SD+HD1 video tracks, one content key for HD2 video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks.
            - ``SHARED`` - Use the same content key for all of the video and audio tracks in your stream.
            - ``UNENCRYPTED`` - Don't encrypt any of the video tracks in your stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-encryptioncontractconfiguration.html#cfn-mediapackage-packagingconfiguration-encryptioncontractconfiguration-presetspeke20video
            '''
            result = self._values.get("preset_speke20_video")
            assert result is not None, "Required property 'preset_speke20_video' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionContractConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnPackagingConfiguration.HlsEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "speke_key_provider": "spekeKeyProvider",
            "constant_initialization_vector": "constantInitializationVector",
            "encryption_method": "encryptionMethod",
        },
    )
    class HlsEncryptionProperty:
        def __init__(
            self,
            *,
            speke_key_provider: typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackagingConfiguration.SpekeKeyProviderProperty", typing.Dict[builtins.str, typing.Any]]],
            constant_initialization_vector: typing.Optional[builtins.str] = None,
            encryption_method: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Holds encryption information so that access to the content can be controlled by a DRM solution.

            :param speke_key_provider: Parameters for the SPEKE key provider.
            :param constant_initialization_vector: A 128-bit, 16-byte hex value represented by a 32-character string, used with the key for encrypting blocks. If you don't specify a constant initialization vector (IV), AWS Elemental MediaPackage periodically rotates the IV.
            :param encryption_method: HLS encryption type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsencryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                hls_encryption_property = mediapackage.CfnPackagingConfiguration.HlsEncryptionProperty(
                    speke_key_provider=mediapackage.CfnPackagingConfiguration.SpekeKeyProviderProperty(
                        role_arn="roleArn",
                        system_ids=["systemIds"],
                        url="url",
                
                        # the properties below are optional
                        encryption_contract_configuration=mediapackage.CfnPackagingConfiguration.EncryptionContractConfigurationProperty(
                            preset_speke20_audio="presetSpeke20Audio",
                            preset_speke20_video="presetSpeke20Video"
                        )
                    ),
                
                    # the properties below are optional
                    constant_initialization_vector="constantInitializationVector",
                    encryption_method="encryptionMethod"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a91a602f74cb33fb7d0bcad3ff19da0b98578a86eaffaca958e54308803fb660)
                check_type(argname="argument speke_key_provider", value=speke_key_provider, expected_type=type_hints["speke_key_provider"])
                check_type(argname="argument constant_initialization_vector", value=constant_initialization_vector, expected_type=type_hints["constant_initialization_vector"])
                check_type(argname="argument encryption_method", value=encryption_method, expected_type=type_hints["encryption_method"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "speke_key_provider": speke_key_provider,
            }
            if constant_initialization_vector is not None:
                self._values["constant_initialization_vector"] = constant_initialization_vector
            if encryption_method is not None:
                self._values["encryption_method"] = encryption_method

        @builtins.property
        def speke_key_provider(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.SpekeKeyProviderProperty"]:
            '''Parameters for the SPEKE key provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsencryption.html#cfn-mediapackage-packagingconfiguration-hlsencryption-spekekeyprovider
            '''
            result = self._values.get("speke_key_provider")
            assert result is not None, "Required property 'speke_key_provider' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.SpekeKeyProviderProperty"], result)

        @builtins.property
        def constant_initialization_vector(self) -> typing.Optional[builtins.str]:
            '''A 128-bit, 16-byte hex value represented by a 32-character string, used with the key for encrypting blocks.

            If you don't specify a constant initialization vector (IV), AWS Elemental MediaPackage periodically rotates the IV.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsencryption.html#cfn-mediapackage-packagingconfiguration-hlsencryption-constantinitializationvector
            '''
            result = self._values.get("constant_initialization_vector")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def encryption_method(self) -> typing.Optional[builtins.str]:
            '''HLS encryption type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsencryption.html#cfn-mediapackage-packagingconfiguration-hlsencryption-encryptionmethod
            '''
            result = self._values.get("encryption_method")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnPackagingConfiguration.HlsManifestProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ad_markers": "adMarkers",
            "include_iframe_only_stream": "includeIframeOnlyStream",
            "manifest_name": "manifestName",
            "program_date_time_interval_seconds": "programDateTimeIntervalSeconds",
            "repeat_ext_x_key": "repeatExtXKey",
            "stream_selection": "streamSelection",
        },
    )
    class HlsManifestProperty:
        def __init__(
            self,
            *,
            ad_markers: typing.Optional[builtins.str] = None,
            include_iframe_only_stream: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            manifest_name: typing.Optional[builtins.str] = None,
            program_date_time_interval_seconds: typing.Optional[jsii.Number] = None,
            repeat_ext_x_key: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            stream_selection: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackagingConfiguration.StreamSelectionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Parameters for an HLS manifest.

            :param ad_markers: This setting controls ad markers in the packaged content. Valid values: - ``NONE`` - Omits all SCTE-35 ad markers from the output. - ``PASSTHROUGH`` - Creates a copy in the output of the SCTE-35 ad markers (comments) taken directly from the input manifest. - ``SCTE35_ENHANCED`` - Generates ad markers and blackout tags in the output based on the SCTE-35 messages from the input manifest.
            :param include_iframe_only_stream: Applies to stream sets with a single video track only. When enabled, the output includes an additional I-frame only stream, along with the other tracks.
            :param manifest_name: A short string that's appended to the end of the endpoint URL to create a unique path to this packaging configuration.
            :param program_date_time_interval_seconds: Inserts ``EXT-X-PROGRAM-DATE-TIME`` tags in the output manifest at the interval that you specify. Additionally, ID3Timed metadata messages are generated every 5 seconds starting when the content was ingested. Irrespective of this parameter, if any ID3Timed metadata is in the HLS input, it is passed through to the HLS output. Omit this attribute or enter ``0`` to indicate that the ``EXT-X-PROGRAM-DATE-TIME`` tags are not included in the manifest.
            :param repeat_ext_x_key: Repeat the ``EXT-X-KEY`` directive for every media segment. This might result in an increase in client requests to the DRM server.
            :param stream_selection: Video bitrate limitations for outputs from this packaging configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                hls_manifest_property = mediapackage.CfnPackagingConfiguration.HlsManifestProperty(
                    ad_markers="adMarkers",
                    include_iframe_only_stream=False,
                    manifest_name="manifestName",
                    program_date_time_interval_seconds=123,
                    repeat_ext_xKey=False,
                    stream_selection=mediapackage.CfnPackagingConfiguration.StreamSelectionProperty(
                        max_video_bits_per_second=123,
                        min_video_bits_per_second=123,
                        stream_order="streamOrder"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__be2ad1e6428cd7b0f61ba8027ea006d43951e79835a6ecdb9f55ffefade062e3)
                check_type(argname="argument ad_markers", value=ad_markers, expected_type=type_hints["ad_markers"])
                check_type(argname="argument include_iframe_only_stream", value=include_iframe_only_stream, expected_type=type_hints["include_iframe_only_stream"])
                check_type(argname="argument manifest_name", value=manifest_name, expected_type=type_hints["manifest_name"])
                check_type(argname="argument program_date_time_interval_seconds", value=program_date_time_interval_seconds, expected_type=type_hints["program_date_time_interval_seconds"])
                check_type(argname="argument repeat_ext_x_key", value=repeat_ext_x_key, expected_type=type_hints["repeat_ext_x_key"])
                check_type(argname="argument stream_selection", value=stream_selection, expected_type=type_hints["stream_selection"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ad_markers is not None:
                self._values["ad_markers"] = ad_markers
            if include_iframe_only_stream is not None:
                self._values["include_iframe_only_stream"] = include_iframe_only_stream
            if manifest_name is not None:
                self._values["manifest_name"] = manifest_name
            if program_date_time_interval_seconds is not None:
                self._values["program_date_time_interval_seconds"] = program_date_time_interval_seconds
            if repeat_ext_x_key is not None:
                self._values["repeat_ext_x_key"] = repeat_ext_x_key
            if stream_selection is not None:
                self._values["stream_selection"] = stream_selection

        @builtins.property
        def ad_markers(self) -> typing.Optional[builtins.str]:
            '''This setting controls ad markers in the packaged content.

            Valid values:

            - ``NONE`` - Omits all SCTE-35 ad markers from the output.
            - ``PASSTHROUGH`` - Creates a copy in the output of the SCTE-35 ad markers (comments) taken directly from the input manifest.
            - ``SCTE35_ENHANCED`` - Generates ad markers and blackout tags in the output based on the SCTE-35 messages from the input manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-admarkers
            '''
            result = self._values.get("ad_markers")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def include_iframe_only_stream(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Applies to stream sets with a single video track only.

            When enabled, the output includes an additional I-frame only stream, along with the other tracks.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-includeiframeonlystream
            '''
            result = self._values.get("include_iframe_only_stream")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def manifest_name(self) -> typing.Optional[builtins.str]:
            '''A short string that's appended to the end of the endpoint URL to create a unique path to this packaging configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-manifestname
            '''
            result = self._values.get("manifest_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def program_date_time_interval_seconds(self) -> typing.Optional[jsii.Number]:
            '''Inserts ``EXT-X-PROGRAM-DATE-TIME`` tags in the output manifest at the interval that you specify.

            Additionally, ID3Timed metadata messages are generated every 5 seconds starting when the content was ingested.

            Irrespective of this parameter, if any ID3Timed metadata is in the HLS input, it is passed through to the HLS output.

            Omit this attribute or enter ``0`` to indicate that the ``EXT-X-PROGRAM-DATE-TIME`` tags are not included in the manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-programdatetimeintervalseconds
            '''
            result = self._values.get("program_date_time_interval_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def repeat_ext_x_key(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Repeat the ``EXT-X-KEY`` directive for every media segment.

            This might result in an increase in client requests to the DRM server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-repeatextxkey
            '''
            result = self._values.get("repeat_ext_x_key")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def stream_selection(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.StreamSelectionProperty"]]:
            '''Video bitrate limitations for outputs from this packaging configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlsmanifest.html#cfn-mediapackage-packagingconfiguration-hlsmanifest-streamselection
            '''
            result = self._values.get("stream_selection")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.StreamSelectionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsManifestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnPackagingConfiguration.HlsPackageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "hls_manifests": "hlsManifests",
            "encryption": "encryption",
            "include_dvb_subtitles": "includeDvbSubtitles",
            "segment_duration_seconds": "segmentDurationSeconds",
            "use_audio_rendition_group": "useAudioRenditionGroup",
        },
    )
    class HlsPackageProperty:
        def __init__(
            self,
            *,
            hls_manifests: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackagingConfiguration.HlsManifestProperty", typing.Dict[builtins.str, typing.Any]]]]],
            encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackagingConfiguration.HlsEncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            include_dvb_subtitles: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            segment_duration_seconds: typing.Optional[jsii.Number] = None,
            use_audio_rendition_group: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Parameters for a packaging configuration that uses HTTP Live Streaming (HLS) packaging.

            :param hls_manifests: A list of HLS manifest configurations that are available from this endpoint.
            :param encryption: Parameters for encrypting content.
            :param include_dvb_subtitles: When enabled, MediaPackage passes through digital video broadcasting (DVB) subtitles into the output.
            :param segment_duration_seconds: Duration (in seconds) of each fragment. Actual fragments are rounded to the nearest multiple of the source fragment duration.
            :param use_audio_rendition_group: When true, AWS Elemental MediaPackage bundles all audio tracks in a rendition group. All other tracks in the stream can be used with any audio rendition from the group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                hls_package_property = mediapackage.CfnPackagingConfiguration.HlsPackageProperty(
                    hls_manifests=[mediapackage.CfnPackagingConfiguration.HlsManifestProperty(
                        ad_markers="adMarkers",
                        include_iframe_only_stream=False,
                        manifest_name="manifestName",
                        program_date_time_interval_seconds=123,
                        repeat_ext_xKey=False,
                        stream_selection=mediapackage.CfnPackagingConfiguration.StreamSelectionProperty(
                            max_video_bits_per_second=123,
                            min_video_bits_per_second=123,
                            stream_order="streamOrder"
                        )
                    )],
                
                    # the properties below are optional
                    encryption=mediapackage.CfnPackagingConfiguration.HlsEncryptionProperty(
                        speke_key_provider=mediapackage.CfnPackagingConfiguration.SpekeKeyProviderProperty(
                            role_arn="roleArn",
                            system_ids=["systemIds"],
                            url="url",
                
                            # the properties below are optional
                            encryption_contract_configuration=mediapackage.CfnPackagingConfiguration.EncryptionContractConfigurationProperty(
                                preset_speke20_audio="presetSpeke20Audio",
                                preset_speke20_video="presetSpeke20Video"
                            )
                        ),
                
                        # the properties below are optional
                        constant_initialization_vector="constantInitializationVector",
                        encryption_method="encryptionMethod"
                    ),
                    include_dvb_subtitles=False,
                    segment_duration_seconds=123,
                    use_audio_rendition_group=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a5032d80be495792bc2559665437cf537429fe8f9454a4b44eb2b9dbf595fe5c)
                check_type(argname="argument hls_manifests", value=hls_manifests, expected_type=type_hints["hls_manifests"])
                check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
                check_type(argname="argument include_dvb_subtitles", value=include_dvb_subtitles, expected_type=type_hints["include_dvb_subtitles"])
                check_type(argname="argument segment_duration_seconds", value=segment_duration_seconds, expected_type=type_hints["segment_duration_seconds"])
                check_type(argname="argument use_audio_rendition_group", value=use_audio_rendition_group, expected_type=type_hints["use_audio_rendition_group"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "hls_manifests": hls_manifests,
            }
            if encryption is not None:
                self._values["encryption"] = encryption
            if include_dvb_subtitles is not None:
                self._values["include_dvb_subtitles"] = include_dvb_subtitles
            if segment_duration_seconds is not None:
                self._values["segment_duration_seconds"] = segment_duration_seconds
            if use_audio_rendition_group is not None:
                self._values["use_audio_rendition_group"] = use_audio_rendition_group

        @builtins.property
        def hls_manifests(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.HlsManifestProperty"]]]:
            '''A list of HLS manifest configurations that are available from this endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-hlsmanifests
            '''
            result = self._values.get("hls_manifests")
            assert result is not None, "Required property 'hls_manifests' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.HlsManifestProperty"]]], result)

        @builtins.property
        def encryption(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.HlsEncryptionProperty"]]:
            '''Parameters for encrypting content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-encryption
            '''
            result = self._values.get("encryption")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.HlsEncryptionProperty"]], result)

        @builtins.property
        def include_dvb_subtitles(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When enabled, MediaPackage passes through digital video broadcasting (DVB) subtitles into the output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-includedvbsubtitles
            '''
            result = self._values.get("include_dvb_subtitles")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def segment_duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''Duration (in seconds) of each fragment.

            Actual fragments are rounded to the nearest multiple of the source fragment duration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-segmentdurationseconds
            '''
            result = self._values.get("segment_duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def use_audio_rendition_group(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When true, AWS Elemental MediaPackage bundles all audio tracks in a rendition group.

            All other tracks in the stream can be used with any audio rendition from the group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-hlspackage.html#cfn-mediapackage-packagingconfiguration-hlspackage-useaudiorenditiongroup
            '''
            result = self._values.get("use_audio_rendition_group")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HlsPackageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnPackagingConfiguration.MssEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={"speke_key_provider": "spekeKeyProvider"},
    )
    class MssEncryptionProperty:
        def __init__(
            self,
            *,
            speke_key_provider: typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackagingConfiguration.SpekeKeyProviderProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Holds encryption information so that access to the content can be controlled by a DRM solution.

            :param speke_key_provider: Parameters for the SPEKE key provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssencryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                mss_encryption_property = mediapackage.CfnPackagingConfiguration.MssEncryptionProperty(
                    speke_key_provider=mediapackage.CfnPackagingConfiguration.SpekeKeyProviderProperty(
                        role_arn="roleArn",
                        system_ids=["systemIds"],
                        url="url",
                
                        # the properties below are optional
                        encryption_contract_configuration=mediapackage.CfnPackagingConfiguration.EncryptionContractConfigurationProperty(
                            preset_speke20_audio="presetSpeke20Audio",
                            preset_speke20_video="presetSpeke20Video"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fb108459b8bd360f0e55c35c750eea25c073892cc7dc2872d2902d86a40730a9)
                check_type(argname="argument speke_key_provider", value=speke_key_provider, expected_type=type_hints["speke_key_provider"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "speke_key_provider": speke_key_provider,
            }

        @builtins.property
        def speke_key_provider(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.SpekeKeyProviderProperty"]:
            '''Parameters for the SPEKE key provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssencryption.html#cfn-mediapackage-packagingconfiguration-mssencryption-spekekeyprovider
            '''
            result = self._values.get("speke_key_provider")
            assert result is not None, "Required property 'speke_key_provider' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.SpekeKeyProviderProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MssEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnPackagingConfiguration.MssManifestProperty",
        jsii_struct_bases=[],
        name_mapping={
            "manifest_name": "manifestName",
            "stream_selection": "streamSelection",
        },
    )
    class MssManifestProperty:
        def __init__(
            self,
            *,
            manifest_name: typing.Optional[builtins.str] = None,
            stream_selection: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackagingConfiguration.StreamSelectionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Parameters for a Microsoft Smooth manifest.

            :param manifest_name: A short string that's appended to the end of the endpoint URL to create a unique path to this packaging configuration.
            :param stream_selection: Video bitrate limitations for outputs from this packaging configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssmanifest.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                mss_manifest_property = mediapackage.CfnPackagingConfiguration.MssManifestProperty(
                    manifest_name="manifestName",
                    stream_selection=mediapackage.CfnPackagingConfiguration.StreamSelectionProperty(
                        max_video_bits_per_second=123,
                        min_video_bits_per_second=123,
                        stream_order="streamOrder"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cb6c646ceb48085b7a63cfa957ddc2e42178d58c426a068a46acc6f6cddd297f)
                check_type(argname="argument manifest_name", value=manifest_name, expected_type=type_hints["manifest_name"])
                check_type(argname="argument stream_selection", value=stream_selection, expected_type=type_hints["stream_selection"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if manifest_name is not None:
                self._values["manifest_name"] = manifest_name
            if stream_selection is not None:
                self._values["stream_selection"] = stream_selection

        @builtins.property
        def manifest_name(self) -> typing.Optional[builtins.str]:
            '''A short string that's appended to the end of the endpoint URL to create a unique path to this packaging configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssmanifest.html#cfn-mediapackage-packagingconfiguration-mssmanifest-manifestname
            '''
            result = self._values.get("manifest_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def stream_selection(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.StreamSelectionProperty"]]:
            '''Video bitrate limitations for outputs from this packaging configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-mssmanifest.html#cfn-mediapackage-packagingconfiguration-mssmanifest-streamselection
            '''
            result = self._values.get("stream_selection")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.StreamSelectionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MssManifestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnPackagingConfiguration.MssPackageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "mss_manifests": "mssManifests",
            "encryption": "encryption",
            "segment_duration_seconds": "segmentDurationSeconds",
        },
    )
    class MssPackageProperty:
        def __init__(
            self,
            *,
            mss_manifests: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackagingConfiguration.MssManifestProperty", typing.Dict[builtins.str, typing.Any]]]]],
            encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackagingConfiguration.MssEncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            segment_duration_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Parameters for a packaging configuration that uses Microsoft Smooth Streaming (MSS) packaging.

            :param mss_manifests: A list of Microsoft Smooth manifest configurations that are available from this endpoint.
            :param encryption: Parameters for encrypting content.
            :param segment_duration_seconds: Duration (in seconds) of each fragment. Actual fragments are rounded to the nearest multiple of the source fragment duration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-msspackage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                mss_package_property = mediapackage.CfnPackagingConfiguration.MssPackageProperty(
                    mss_manifests=[mediapackage.CfnPackagingConfiguration.MssManifestProperty(
                        manifest_name="manifestName",
                        stream_selection=mediapackage.CfnPackagingConfiguration.StreamSelectionProperty(
                            max_video_bits_per_second=123,
                            min_video_bits_per_second=123,
                            stream_order="streamOrder"
                        )
                    )],
                
                    # the properties below are optional
                    encryption=mediapackage.CfnPackagingConfiguration.MssEncryptionProperty(
                        speke_key_provider=mediapackage.CfnPackagingConfiguration.SpekeKeyProviderProperty(
                            role_arn="roleArn",
                            system_ids=["systemIds"],
                            url="url",
                
                            # the properties below are optional
                            encryption_contract_configuration=mediapackage.CfnPackagingConfiguration.EncryptionContractConfigurationProperty(
                                preset_speke20_audio="presetSpeke20Audio",
                                preset_speke20_video="presetSpeke20Video"
                            )
                        )
                    ),
                    segment_duration_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__596bd770b476d92d874770e06c5d3f83482d9ae3598af8013af7e947277aabb9)
                check_type(argname="argument mss_manifests", value=mss_manifests, expected_type=type_hints["mss_manifests"])
                check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
                check_type(argname="argument segment_duration_seconds", value=segment_duration_seconds, expected_type=type_hints["segment_duration_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "mss_manifests": mss_manifests,
            }
            if encryption is not None:
                self._values["encryption"] = encryption
            if segment_duration_seconds is not None:
                self._values["segment_duration_seconds"] = segment_duration_seconds

        @builtins.property
        def mss_manifests(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.MssManifestProperty"]]]:
            '''A list of Microsoft Smooth manifest configurations that are available from this endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-msspackage.html#cfn-mediapackage-packagingconfiguration-msspackage-mssmanifests
            '''
            result = self._values.get("mss_manifests")
            assert result is not None, "Required property 'mss_manifests' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.MssManifestProperty"]]], result)

        @builtins.property
        def encryption(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.MssEncryptionProperty"]]:
            '''Parameters for encrypting content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-msspackage.html#cfn-mediapackage-packagingconfiguration-msspackage-encryption
            '''
            result = self._values.get("encryption")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.MssEncryptionProperty"]], result)

        @builtins.property
        def segment_duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''Duration (in seconds) of each fragment.

            Actual fragments are rounded to the nearest multiple of the source fragment duration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-msspackage.html#cfn-mediapackage-packagingconfiguration-msspackage-segmentdurationseconds
            '''
            result = self._values.get("segment_duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MssPackageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnPackagingConfiguration.SpekeKeyProviderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "system_ids": "systemIds",
            "url": "url",
            "encryption_contract_configuration": "encryptionContractConfiguration",
        },
    )
    class SpekeKeyProviderProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            system_ids: typing.Sequence[builtins.str],
            url: builtins.str,
            encryption_contract_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackagingConfiguration.EncryptionContractConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A configuration for accessing an external Secure Packager and Encoder Key Exchange (SPEKE) service that provides encryption keys.

            :param role_arn: The ARN for the IAM role that's granted by the key provider to provide access to the key provider API. Valid format: arn:aws:iam::{accountID}:role/{name}
            :param system_ids: List of unique identifiers for the DRM systems to use, as defined in the CPIX specification.
            :param url: URL for the key provider's key retrieval API endpoint. Must start with https://.
            :param encryption_contract_configuration: Use ``encryptionContractConfiguration`` to configure one or more content encryption keys for your endpoints that use SPEKE Version 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-spekekeyprovider.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                speke_key_provider_property = mediapackage.CfnPackagingConfiguration.SpekeKeyProviderProperty(
                    role_arn="roleArn",
                    system_ids=["systemIds"],
                    url="url",
                
                    # the properties below are optional
                    encryption_contract_configuration=mediapackage.CfnPackagingConfiguration.EncryptionContractConfigurationProperty(
                        preset_speke20_audio="presetSpeke20Audio",
                        preset_speke20_video="presetSpeke20Video"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b6ba84253e87d787b38627704703d459abb9b442b892a848c98fdde4b3cf420f)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument system_ids", value=system_ids, expected_type=type_hints["system_ids"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
                check_type(argname="argument encryption_contract_configuration", value=encryption_contract_configuration, expected_type=type_hints["encryption_contract_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
                "system_ids": system_ids,
                "url": url,
            }
            if encryption_contract_configuration is not None:
                self._values["encryption_contract_configuration"] = encryption_contract_configuration

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN for the IAM role that's granted by the key provider to provide access to the key provider API.

            Valid format: arn:aws:iam::{accountID}:role/{name}

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-spekekeyprovider.html#cfn-mediapackage-packagingconfiguration-spekekeyprovider-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def system_ids(self) -> typing.List[builtins.str]:
            '''List of unique identifiers for the DRM systems to use, as defined in the CPIX specification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-spekekeyprovider.html#cfn-mediapackage-packagingconfiguration-spekekeyprovider-systemids
            '''
            result = self._values.get("system_ids")
            assert result is not None, "Required property 'system_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def url(self) -> builtins.str:
            '''URL for the key provider's key retrieval API endpoint.

            Must start with https://.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-spekekeyprovider.html#cfn-mediapackage-packagingconfiguration-spekekeyprovider-url
            '''
            result = self._values.get("url")
            assert result is not None, "Required property 'url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def encryption_contract_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.EncryptionContractConfigurationProperty"]]:
            '''Use ``encryptionContractConfiguration`` to configure one or more content encryption keys for your endpoints that use SPEKE Version 2.0. The encryption contract defines which content keys are used to encrypt the audio and video tracks in your stream. To configure the encryption contract, specify which audio and video encryption presets to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-spekekeyprovider.html#cfn-mediapackage-packagingconfiguration-spekekeyprovider-encryptioncontractconfiguration
            '''
            result = self._values.get("encryption_contract_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingConfiguration.EncryptionContractConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SpekeKeyProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnPackagingConfiguration.StreamSelectionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_video_bits_per_second": "maxVideoBitsPerSecond",
            "min_video_bits_per_second": "minVideoBitsPerSecond",
            "stream_order": "streamOrder",
        },
    )
    class StreamSelectionProperty:
        def __init__(
            self,
            *,
            max_video_bits_per_second: typing.Optional[jsii.Number] = None,
            min_video_bits_per_second: typing.Optional[jsii.Number] = None,
            stream_order: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Limitations for outputs from the endpoint, based on the video bitrate.

            :param max_video_bits_per_second: The upper limit of the bitrates that this endpoint serves. If the video track exceeds this threshold, then AWS Elemental MediaPackage excludes it from output. If you don't specify a value, it defaults to 2147483647 bits per second.
            :param min_video_bits_per_second: The lower limit of the bitrates that this endpoint serves. If the video track is below this threshold, then AWS Elemental MediaPackage excludes it from output. If you don't specify a value, it defaults to 0 bits per second.
            :param stream_order: Order in which the different video bitrates are presented to the player. Valid values: ``ORIGINAL`` , ``VIDEO_BITRATE_ASCENDING`` , ``VIDEO_BITRATE_DESCENDING`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-streamselection.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                stream_selection_property = mediapackage.CfnPackagingConfiguration.StreamSelectionProperty(
                    max_video_bits_per_second=123,
                    min_video_bits_per_second=123,
                    stream_order="streamOrder"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8b8f0e52cfccc1ebe0e2ad93d90f039baf326c3a9c8662423b9760f12f1e8e7e)
                check_type(argname="argument max_video_bits_per_second", value=max_video_bits_per_second, expected_type=type_hints["max_video_bits_per_second"])
                check_type(argname="argument min_video_bits_per_second", value=min_video_bits_per_second, expected_type=type_hints["min_video_bits_per_second"])
                check_type(argname="argument stream_order", value=stream_order, expected_type=type_hints["stream_order"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if max_video_bits_per_second is not None:
                self._values["max_video_bits_per_second"] = max_video_bits_per_second
            if min_video_bits_per_second is not None:
                self._values["min_video_bits_per_second"] = min_video_bits_per_second
            if stream_order is not None:
                self._values["stream_order"] = stream_order

        @builtins.property
        def max_video_bits_per_second(self) -> typing.Optional[jsii.Number]:
            '''The upper limit of the bitrates that this endpoint serves.

            If the video track exceeds this threshold, then AWS Elemental MediaPackage excludes it from output. If you don't specify a value, it defaults to 2147483647 bits per second.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-streamselection.html#cfn-mediapackage-packagingconfiguration-streamselection-maxvideobitspersecond
            '''
            result = self._values.get("max_video_bits_per_second")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min_video_bits_per_second(self) -> typing.Optional[jsii.Number]:
            '''The lower limit of the bitrates that this endpoint serves.

            If the video track is below this threshold, then AWS Elemental MediaPackage excludes it from output. If you don't specify a value, it defaults to 0 bits per second.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-streamselection.html#cfn-mediapackage-packagingconfiguration-streamselection-minvideobitspersecond
            '''
            result = self._values.get("min_video_bits_per_second")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def stream_order(self) -> typing.Optional[builtins.str]:
            '''Order in which the different video bitrates are presented to the player.

            Valid values: ``ORIGINAL`` , ``VIDEO_BITRATE_ASCENDING`` , ``VIDEO_BITRATE_DESCENDING`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packagingconfiguration-streamselection.html#cfn-mediapackage-packagingconfiguration-streamselection-streamorder
            '''
            result = self._values.get("stream_order")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StreamSelectionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediapackage.CfnPackagingConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "packaging_group_id": "packagingGroupId",
        "cmaf_package": "cmafPackage",
        "dash_package": "dashPackage",
        "hls_package": "hlsPackage",
        "mss_package": "mssPackage",
        "tags": "tags",
    },
)
class CfnPackagingConfigurationProps:
    def __init__(
        self,
        *,
        id: builtins.str,
        packaging_group_id: builtins.str,
        cmaf_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.CmafPackageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        dash_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.DashPackageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        hls_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.HlsPackageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        mss_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.MssPackageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPackagingConfiguration``.

        :param id: Unique identifier that you assign to the packaging configuration.
        :param packaging_group_id: The ID of the packaging group associated with this packaging configuration.
        :param cmaf_package: Parameters for CMAF packaging.
        :param dash_package: Parameters for DASH-ISO packaging.
        :param hls_package: Parameters for Apple HLS packaging.
        :param mss_package: Parameters for Microsoft Smooth Streaming packaging.
        :param tags: The tags to assign to the packaging configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediapackage as mediapackage
            
            cfn_packaging_configuration_props = mediapackage.CfnPackagingConfigurationProps(
                id="id",
                packaging_group_id="packagingGroupId",
            
                # the properties below are optional
                cmaf_package=mediapackage.CfnPackagingConfiguration.CmafPackageProperty(
                    hls_manifests=[mediapackage.CfnPackagingConfiguration.HlsManifestProperty(
                        ad_markers="adMarkers",
                        include_iframe_only_stream=False,
                        manifest_name="manifestName",
                        program_date_time_interval_seconds=123,
                        repeat_ext_xKey=False,
                        stream_selection=mediapackage.CfnPackagingConfiguration.StreamSelectionProperty(
                            max_video_bits_per_second=123,
                            min_video_bits_per_second=123,
                            stream_order="streamOrder"
                        )
                    )],
            
                    # the properties below are optional
                    encryption=mediapackage.CfnPackagingConfiguration.CmafEncryptionProperty(
                        speke_key_provider=mediapackage.CfnPackagingConfiguration.SpekeKeyProviderProperty(
                            role_arn="roleArn",
                            system_ids=["systemIds"],
                            url="url",
            
                            # the properties below are optional
                            encryption_contract_configuration=mediapackage.CfnPackagingConfiguration.EncryptionContractConfigurationProperty(
                                preset_speke20_audio="presetSpeke20Audio",
                                preset_speke20_video="presetSpeke20Video"
                            )
                        )
                    ),
                    include_encoder_configuration_in_segments=False,
                    segment_duration_seconds=123
                ),
                dash_package=mediapackage.CfnPackagingConfiguration.DashPackageProperty(
                    dash_manifests=[mediapackage.CfnPackagingConfiguration.DashManifestProperty(
                        manifest_layout="manifestLayout",
                        manifest_name="manifestName",
                        min_buffer_time_seconds=123,
                        profile="profile",
                        scte_markers_source="scteMarkersSource",
                        stream_selection=mediapackage.CfnPackagingConfiguration.StreamSelectionProperty(
                            max_video_bits_per_second=123,
                            min_video_bits_per_second=123,
                            stream_order="streamOrder"
                        )
                    )],
            
                    # the properties below are optional
                    encryption=mediapackage.CfnPackagingConfiguration.DashEncryptionProperty(
                        speke_key_provider=mediapackage.CfnPackagingConfiguration.SpekeKeyProviderProperty(
                            role_arn="roleArn",
                            system_ids=["systemIds"],
                            url="url",
            
                            # the properties below are optional
                            encryption_contract_configuration=mediapackage.CfnPackagingConfiguration.EncryptionContractConfigurationProperty(
                                preset_speke20_audio="presetSpeke20Audio",
                                preset_speke20_video="presetSpeke20Video"
                            )
                        )
                    ),
                    include_encoder_configuration_in_segments=False,
                    include_iframe_only_stream=False,
                    period_triggers=["periodTriggers"],
                    segment_duration_seconds=123,
                    segment_template_format="segmentTemplateFormat"
                ),
                hls_package=mediapackage.CfnPackagingConfiguration.HlsPackageProperty(
                    hls_manifests=[mediapackage.CfnPackagingConfiguration.HlsManifestProperty(
                        ad_markers="adMarkers",
                        include_iframe_only_stream=False,
                        manifest_name="manifestName",
                        program_date_time_interval_seconds=123,
                        repeat_ext_xKey=False,
                        stream_selection=mediapackage.CfnPackagingConfiguration.StreamSelectionProperty(
                            max_video_bits_per_second=123,
                            min_video_bits_per_second=123,
                            stream_order="streamOrder"
                        )
                    )],
            
                    # the properties below are optional
                    encryption=mediapackage.CfnPackagingConfiguration.HlsEncryptionProperty(
                        speke_key_provider=mediapackage.CfnPackagingConfiguration.SpekeKeyProviderProperty(
                            role_arn="roleArn",
                            system_ids=["systemIds"],
                            url="url",
            
                            # the properties below are optional
                            encryption_contract_configuration=mediapackage.CfnPackagingConfiguration.EncryptionContractConfigurationProperty(
                                preset_speke20_audio="presetSpeke20Audio",
                                preset_speke20_video="presetSpeke20Video"
                            )
                        ),
            
                        # the properties below are optional
                        constant_initialization_vector="constantInitializationVector",
                        encryption_method="encryptionMethod"
                    ),
                    include_dvb_subtitles=False,
                    segment_duration_seconds=123,
                    use_audio_rendition_group=False
                ),
                mss_package=mediapackage.CfnPackagingConfiguration.MssPackageProperty(
                    mss_manifests=[mediapackage.CfnPackagingConfiguration.MssManifestProperty(
                        manifest_name="manifestName",
                        stream_selection=mediapackage.CfnPackagingConfiguration.StreamSelectionProperty(
                            max_video_bits_per_second=123,
                            min_video_bits_per_second=123,
                            stream_order="streamOrder"
                        )
                    )],
            
                    # the properties below are optional
                    encryption=mediapackage.CfnPackagingConfiguration.MssEncryptionProperty(
                        speke_key_provider=mediapackage.CfnPackagingConfiguration.SpekeKeyProviderProperty(
                            role_arn="roleArn",
                            system_ids=["systemIds"],
                            url="url",
            
                            # the properties below are optional
                            encryption_contract_configuration=mediapackage.CfnPackagingConfiguration.EncryptionContractConfigurationProperty(
                                preset_speke20_audio="presetSpeke20Audio",
                                preset_speke20_video="presetSpeke20Video"
                            )
                        )
                    ),
                    segment_duration_seconds=123
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c18c6cdf8ce44ba79abb7799a3f07a9a73c17f6607c07f5bc7d6c847a36c9051)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument packaging_group_id", value=packaging_group_id, expected_type=type_hints["packaging_group_id"])
            check_type(argname="argument cmaf_package", value=cmaf_package, expected_type=type_hints["cmaf_package"])
            check_type(argname="argument dash_package", value=dash_package, expected_type=type_hints["dash_package"])
            check_type(argname="argument hls_package", value=hls_package, expected_type=type_hints["hls_package"])
            check_type(argname="argument mss_package", value=mss_package, expected_type=type_hints["mss_package"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
            "packaging_group_id": packaging_group_id,
        }
        if cmaf_package is not None:
            self._values["cmaf_package"] = cmaf_package
        if dash_package is not None:
            self._values["dash_package"] = dash_package
        if hls_package is not None:
            self._values["hls_package"] = hls_package
        if mss_package is not None:
            self._values["mss_package"] = mss_package
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def id(self) -> builtins.str:
        '''Unique identifier that you assign to the packaging configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-id
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def packaging_group_id(self) -> builtins.str:
        '''The ID of the packaging group associated with this packaging configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-packaginggroupid
        '''
        result = self._values.get("packaging_group_id")
        assert result is not None, "Required property 'packaging_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cmaf_package(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPackagingConfiguration.CmafPackageProperty]]:
        '''Parameters for CMAF packaging.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-cmafpackage
        '''
        result = self._values.get("cmaf_package")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPackagingConfiguration.CmafPackageProperty]], result)

    @builtins.property
    def dash_package(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPackagingConfiguration.DashPackageProperty]]:
        '''Parameters for DASH-ISO packaging.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-dashpackage
        '''
        result = self._values.get("dash_package")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPackagingConfiguration.DashPackageProperty]], result)

    @builtins.property
    def hls_package(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPackagingConfiguration.HlsPackageProperty]]:
        '''Parameters for Apple HLS packaging.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-hlspackage
        '''
        result = self._values.get("hls_package")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPackagingConfiguration.HlsPackageProperty]], result)

    @builtins.property
    def mss_package(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPackagingConfiguration.MssPackageProperty]]:
        '''Parameters for Microsoft Smooth Streaming packaging.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-msspackage
        '''
        result = self._values.get("mss_package")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPackagingConfiguration.MssPackageProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to assign to the packaging configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packagingconfiguration.html#cfn-mediapackage-packagingconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPackagingConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnPackagingGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediapackage.CfnPackagingGroup",
):
    '''Creates a packaging group.

    The packaging group holds one or more packaging configurations. When you create an asset, you specify the packaging group associated with the asset. The asset has playback endpoints for each packaging configuration within the group.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediapackage as mediapackage
        
        cfn_packaging_group = mediapackage.CfnPackagingGroup(self, "MyCfnPackagingGroup",
            id="id",
        
            # the properties below are optional
            authorization=mediapackage.CfnPackagingGroup.AuthorizationProperty(
                cdn_identifier_secret="cdnIdentifierSecret",
                secrets_role_arn="secretsRoleArn"
            ),
            egress_access_logs=mediapackage.CfnPackagingGroup.LogConfigurationProperty(
                log_group_name="logGroupName"
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
        id_: builtins.str,
        *,
        id: builtins.str,
        authorization: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackagingGroup.AuthorizationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        egress_access_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackagingGroup.LogConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id_: Construct identifier for this resource (unique in its scope).
        :param id: Unique identifier that you assign to the packaging group.
        :param authorization: Parameters for CDN authorization.
        :param egress_access_logs: The configuration parameters for egress access logging.
        :param tags: The tags to assign to the packaging group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbd1b59c1bc28934f2358b37570be82b032aa4ccdab40560578195b02efe423b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        props = CfnPackagingGroupProps(
            id=id,
            authorization=authorization,
            egress_access_logs=egress_access_logs,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id_, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__607d136c67f456d025fdf14d7dc1e0a69aff157c4c5eeff267508fa2ae54dc75)
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
            type_hints = typing.get_type_hints(_typecheckingstub__47694a446a5f733392635957d4aa0f98d743244185f6d99b37a7b03e69143ff9)
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
        '''The Amazon Resource Name (ARN) for the packaging group.

        You can get this from the response to any request to the packaging group.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainName")
    def attr_domain_name(self) -> builtins.str:
        '''The URL for the assets in the PackagingGroup.

        :cloudformationAttribute: DomainName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainName"))

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
        '''Unique identifier that you assign to the packaging group.'''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c11025591571c1f0afc6d388f54590a0ff4a8b3888c2d0fd58c4dbcd91281aa1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="authorization")
    def authorization(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingGroup.AuthorizationProperty"]]:
        '''Parameters for CDN authorization.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingGroup.AuthorizationProperty"]], jsii.get(self, "authorization"))

    @authorization.setter
    def authorization(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingGroup.AuthorizationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c8371f8b34356b36eff32cf2cbea4d3f14fcd556b4ab0bd7f5dd7bd2ea117d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorization", value)

    @builtins.property
    @jsii.member(jsii_name="egressAccessLogs")
    def egress_access_logs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingGroup.LogConfigurationProperty"]]:
        '''The configuration parameters for egress access logging.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingGroup.LogConfigurationProperty"]], jsii.get(self, "egressAccessLogs"))

    @egress_access_logs.setter
    def egress_access_logs(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackagingGroup.LogConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b41c84687cbb3318b0cf57c76ee83dd7efbb0ccf04883a441e2999922e95d713)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "egressAccessLogs", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to assign to the packaging group.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5205179917b0f19bc336c90cf83e4b7b624469516be6573083daea59caa9f3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnPackagingGroup.AuthorizationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cdn_identifier_secret": "cdnIdentifierSecret",
            "secrets_role_arn": "secretsRoleArn",
        },
    )
    class AuthorizationProperty:
        def __init__(
            self,
            *,
            cdn_identifier_secret: builtins.str,
            secrets_role_arn: builtins.str,
        ) -> None:
            '''Parameters for enabling CDN authorization.

            :param cdn_identifier_secret: The Amazon Resource Name (ARN) for the secret in AWS Secrets Manager that is used for CDN authorization.
            :param secrets_role_arn: The Amazon Resource Name (ARN) for the IAM role that allows AWS Elemental MediaPackage to communicate with AWS Secrets Manager .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-authorization.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                authorization_property = mediapackage.CfnPackagingGroup.AuthorizationProperty(
                    cdn_identifier_secret="cdnIdentifierSecret",
                    secrets_role_arn="secretsRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fa6c921391574b4b282e70426c3be4566d95bf7137942ed0553b6814f022a1fb)
                check_type(argname="argument cdn_identifier_secret", value=cdn_identifier_secret, expected_type=type_hints["cdn_identifier_secret"])
                check_type(argname="argument secrets_role_arn", value=secrets_role_arn, expected_type=type_hints["secrets_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cdn_identifier_secret": cdn_identifier_secret,
                "secrets_role_arn": secrets_role_arn,
            }

        @builtins.property
        def cdn_identifier_secret(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) for the secret in AWS Secrets Manager that is used for CDN authorization.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-authorization.html#cfn-mediapackage-packaginggroup-authorization-cdnidentifiersecret
            '''
            result = self._values.get("cdn_identifier_secret")
            assert result is not None, "Required property 'cdn_identifier_secret' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secrets_role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) for the IAM role that allows AWS Elemental MediaPackage to communicate with AWS Secrets Manager .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-authorization.html#cfn-mediapackage-packaginggroup-authorization-secretsrolearn
            '''
            result = self._values.get("secrets_role_arn")
            assert result is not None, "Required property 'secrets_role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthorizationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediapackage.CfnPackagingGroup.LogConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_name": "logGroupName"},
    )
    class LogConfigurationProperty:
        def __init__(
            self,
            *,
            log_group_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Sets a custom Amazon CloudWatch log group name for egress logs.

            If a log group name isn't specified, the default name is used: /aws/MediaPackage/EgressAccessLogs.

            :param log_group_name: Sets a custom Amazon CloudWatch log group name for egress logs. If a log group name isn't specified, the default name is used: /aws/MediaPackage/EgressAccessLogs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-logconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediapackage as mediapackage
                
                log_configuration_property = mediapackage.CfnPackagingGroup.LogConfigurationProperty(
                    log_group_name="logGroupName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4150658ca39a19a1dfd87e145dfd5096869cfbac1f58d8d09510ec58d44583b3)
                check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_group_name is not None:
                self._values["log_group_name"] = log_group_name

        @builtins.property
        def log_group_name(self) -> typing.Optional[builtins.str]:
            '''Sets a custom Amazon CloudWatch log group name for egress logs.

            If a log group name isn't specified, the default name is used: /aws/MediaPackage/EgressAccessLogs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediapackage-packaginggroup-logconfiguration.html#cfn-mediapackage-packaginggroup-logconfiguration-loggroupname
            '''
            result = self._values.get("log_group_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediapackage.CfnPackagingGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "authorization": "authorization",
        "egress_access_logs": "egressAccessLogs",
        "tags": "tags",
    },
)
class CfnPackagingGroupProps:
    def __init__(
        self,
        *,
        id: builtins.str,
        authorization: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingGroup.AuthorizationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        egress_access_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingGroup.LogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPackagingGroup``.

        :param id: Unique identifier that you assign to the packaging group.
        :param authorization: Parameters for CDN authorization.
        :param egress_access_logs: The configuration parameters for egress access logging.
        :param tags: The tags to assign to the packaging group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediapackage as mediapackage
            
            cfn_packaging_group_props = mediapackage.CfnPackagingGroupProps(
                id="id",
            
                # the properties below are optional
                authorization=mediapackage.CfnPackagingGroup.AuthorizationProperty(
                    cdn_identifier_secret="cdnIdentifierSecret",
                    secrets_role_arn="secretsRoleArn"
                ),
                egress_access_logs=mediapackage.CfnPackagingGroup.LogConfigurationProperty(
                    log_group_name="logGroupName"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5388a440fca30595e75f64ebeb4a2d57f4c3c7281b7f0215ac9e58ac28536ef7)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument authorization", value=authorization, expected_type=type_hints["authorization"])
            check_type(argname="argument egress_access_logs", value=egress_access_logs, expected_type=type_hints["egress_access_logs"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id": id,
        }
        if authorization is not None:
            self._values["authorization"] = authorization
        if egress_access_logs is not None:
            self._values["egress_access_logs"] = egress_access_logs
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def id(self) -> builtins.str:
        '''Unique identifier that you assign to the packaging group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#cfn-mediapackage-packaginggroup-id
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorization(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPackagingGroup.AuthorizationProperty]]:
        '''Parameters for CDN authorization.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#cfn-mediapackage-packaginggroup-authorization
        '''
        result = self._values.get("authorization")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPackagingGroup.AuthorizationProperty]], result)

    @builtins.property
    def egress_access_logs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPackagingGroup.LogConfigurationProperty]]:
        '''The configuration parameters for egress access logging.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#cfn-mediapackage-packaginggroup-egressaccesslogs
        '''
        result = self._values.get("egress_access_logs")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPackagingGroup.LogConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to assign to the packaging group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-packaginggroup.html#cfn-mediapackage-packaginggroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPackagingGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAsset",
    "CfnAssetProps",
    "CfnChannel",
    "CfnChannelProps",
    "CfnOriginEndpoint",
    "CfnOriginEndpointProps",
    "CfnPackagingConfiguration",
    "CfnPackagingConfigurationProps",
    "CfnPackagingGroup",
    "CfnPackagingGroupProps",
]

publication.publish()

def _typecheckingstub__f18cc60b1c4089a35fd436a7258b422078f0fecc32d062615b3434a45a2e2b39(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    id: builtins.str,
    packaging_group_id: builtins.str,
    source_arn: builtins.str,
    source_role_arn: builtins.str,
    egress_endpoints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAsset.EgressEndpointProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2a76b75b5e09e9a8d97792dff99a5272eed0a3f4557a4181b2b56b77f0cdcef(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4389b9d5dd5c3d310e064eeab7db8ef228e477e34d2335664ab83fd39985040(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35b6682ae346664a086b9dff0d456af04d28c65a084cf0ae564d117116459491(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35d95ecd9b726f976edf6a9d1f766835ad6631faef33a2d12b96d6c8d6638d03(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72d3df8af23896f6f5ef3194ec3ed4bbfbb982faf70463969c7c34164fee8ed5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41f7b135121a8ac650206952f41f006f691f4d3be4e73e76fa6bef7576e8f9fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a644764b4a43d734fea1bf555feb1c097efc7cf3b30ba898c866f73a019f663e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAsset.EgressEndpointProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcd0264c72c6ead9699a93d8126ea230415f8b868e98b4a5a1c59fc224a6321b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40009e0bd275773b97adc81d95be811402372bc85c522f243c45a58fa3a41f3e(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d2fee4640b24dddffbfcd26c914f32e00de4b0cf2345061ed96cb652a4b4abb(
    *,
    packaging_configuration_id: builtins.str,
    url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75a0b1d34d977af6555f35f8e5de3877b3368ef3ca4c39da943111a6f5840b01(
    *,
    id: builtins.str,
    packaging_group_id: builtins.str,
    source_arn: builtins.str,
    source_role_arn: builtins.str,
    egress_endpoints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAsset.EgressEndpointProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__affeaf26cf4f8ef0e55a6096e7b94b296b27d02db77d19dbc77989422463b5f7(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    egress_access_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.LogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    hls_ingest: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.HlsIngestProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ingress_access_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.LogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a46a52d6dc51e43bc3260e55b89bbcfdda168c349ea724ce787a0fa6b5f0c0ae(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e92fe8ab8981412f0b93b05f876df2c0ea41b1e4cc736a04a5a927181c9c3611(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dfbfa5e60b31deabc06dac96485918d2f795cb0d3241ec09ac091e73b80a1a4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b5c758b0bb9f06dee32e08926740d41a3cce1b111f1626fa66ea6f82115cc16(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bf5b93815da3604606437071a85affcc9f8a576213172d6442244006725709c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnChannel.LogConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd06c14ed9d8edf5f5e20f5cc9d6e0f82ce9226bf2682de8368e9134dfb2ecca(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnChannel.HlsIngestProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1eba56f28a4c29c9f6a1b3e1b6fce471204f7c3704ad8b8bfc70d8eea07dc4d6(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnChannel.LogConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffcf834ef6a826c28d9aa0d38721dbed5c74dbc38ca930c45f097c244fe6987c(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8879f1cc6590d96234de60e9c45cd369821bc7c5aed33b342acff35c1254cac(
    *,
    ingest_endpoints: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.IngestEndpointProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a0b9e94f252eb78a349be10dd707d652377ae6ccf636f5f08b2754b2de7260e(
    *,
    id: builtins.str,
    password: builtins.str,
    url: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5285b3c3196f5f3515543929d1ccf061692d47e8617d4ea53715cd2b0e00f85e(
    *,
    log_group_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6608d4c68a49ca8e028b5d1d7da6506d3d11de3ed14a5a1bfcc17f851ffd06a5(
    *,
    id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    egress_access_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.LogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    hls_ingest: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.HlsIngestProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ingress_access_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnChannel.LogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01f85bb3acbb258c87305e632e7d154966949216428ef553b6c3235e01417aa8(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    channel_id: builtins.str,
    id: builtins.str,
    authorization: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.AuthorizationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cmaf_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.CmafPackageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dash_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.DashPackageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    hls_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.HlsPackageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    manifest_name: typing.Optional[builtins.str] = None,
    mss_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.MssPackageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    origination: typing.Optional[builtins.str] = None,
    startover_window_seconds: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    time_delay_seconds: typing.Optional[jsii.Number] = None,
    whitelist: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3478aec9c15e91156fc03894a528b9f2055b88884d84bcb16fa53310f28c4cf(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f55a0e1543c341d60565427fa11f8fd24cd6bd09fe56ce62c8e50d2a9a3b8535(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be0b35a7d39f22a922e6d2806701c97a79583ed4cd380349683d0ae31a09565e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99a06c257b6797d9aae3bd64d6eeb55571af3841b86e1ad7d2980726f85a9dc5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__156ab3ebea5a8eacd612f1583257bbe7850d21712c1c3dcd5447fd36f76d3ba2(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.AuthorizationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25473ff4d9f0fbc872a9885f718995cbcc6ad16528e432dfbadeb748e4129584(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.CmafPackageProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0c2c45ab2e510dd522ccbc5accd0905f0fc2d460bf6760ffc34e1a0ce8652f1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.DashPackageProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12d8129533cd4dccc4d114bda308471faa5a22dd061a8c8efe51e6bbe12d5a51(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65497669bad52e91563221a8604146d8b2b151a2211a913fabce3fd05beb01df(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.HlsPackageProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee8a6384d559f558cfc96a8adbf44f42b4b89ad14cf509a9bb35857f61b20531(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5b207fa4f25365ce14c50d90586150f16e19390170ef5cbd3169b1037eace1d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOriginEndpoint.MssPackageProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7d8c8b852ebe894d61bc71a445d8ac7e24da974818f025c346a33de8083a9b9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c528046b9214a04549830faf062051f7418fc9517ba9c6c4a5e6dd283f7850b5(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61e0125a3a7672d5a1bf2f0e24eb93f48b6dd949a3c5d94bda3997afcde3e15a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af85b805197b1d411c4fd747d0ac4e2468574569f1fdb2926834a94c4da3c0f2(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cabc2520080e09c3795d546475e7a04bb502f05de10623e2eaf44596dffcf971(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d25e4ac516c5e88a584ad88a9eff22ac7db2bb6285c6ee8d81d5ec6d823bf9ef(
    *,
    cdn_identifier_secret: builtins.str,
    secrets_role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__665a104be1b3a19db35ae8236df5a37f409cede911767d94187e4c949dd198e9(
    *,
    speke_key_provider: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.SpekeKeyProviderProperty, typing.Dict[builtins.str, typing.Any]]],
    constant_initialization_vector: typing.Optional[builtins.str] = None,
    encryption_method: typing.Optional[builtins.str] = None,
    key_rotation_interval_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2d9ac49bc2a414f54d7fa4069dc81be30a81c60a1a099ba1f19e415e6295078(
    *,
    encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.CmafEncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    hls_manifests: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.HlsManifestProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    segment_duration_seconds: typing.Optional[jsii.Number] = None,
    segment_prefix: typing.Optional[builtins.str] = None,
    stream_selection: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.StreamSelectionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f56c756b424a8b673433bbd23b0af6d3a73ae1da9d39c6467efe26215ce4980(
    *,
    speke_key_provider: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.SpekeKeyProviderProperty, typing.Dict[builtins.str, typing.Any]]],
    key_rotation_interval_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c4696e5d92d7a873900820a774868b04c3d76cad65c252fb49a13d1cdfc76fb(
    *,
    ads_on_delivery_restrictions: typing.Optional[builtins.str] = None,
    ad_triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
    encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.DashEncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    include_iframe_only_stream: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    manifest_layout: typing.Optional[builtins.str] = None,
    manifest_window_seconds: typing.Optional[jsii.Number] = None,
    min_buffer_time_seconds: typing.Optional[jsii.Number] = None,
    min_update_period_seconds: typing.Optional[jsii.Number] = None,
    period_triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
    profile: typing.Optional[builtins.str] = None,
    segment_duration_seconds: typing.Optional[jsii.Number] = None,
    segment_template_format: typing.Optional[builtins.str] = None,
    stream_selection: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.StreamSelectionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    suggested_presentation_delay_seconds: typing.Optional[jsii.Number] = None,
    utc_timing: typing.Optional[builtins.str] = None,
    utc_timing_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d004a027349401a62ecd9b769e520b22a332cbc1fd4ecea898450bbbac2f6f40(
    *,
    preset_speke20_audio: builtins.str,
    preset_speke20_video: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bb2230c09575c8cdc63eb8385b3b1ed5b43e8bd3bdc0da5be4202670b0dfa68(
    *,
    speke_key_provider: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.SpekeKeyProviderProperty, typing.Dict[builtins.str, typing.Any]]],
    constant_initialization_vector: typing.Optional[builtins.str] = None,
    encryption_method: typing.Optional[builtins.str] = None,
    key_rotation_interval_seconds: typing.Optional[jsii.Number] = None,
    repeat_ext_x_key: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4367b7a88cd2fce8b4e47599c1f36f00f1184af4a9a26f40d6b422a374b0ea08(
    *,
    id: builtins.str,
    ad_markers: typing.Optional[builtins.str] = None,
    ads_on_delivery_restrictions: typing.Optional[builtins.str] = None,
    ad_triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
    include_iframe_only_stream: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    manifest_name: typing.Optional[builtins.str] = None,
    playlist_type: typing.Optional[builtins.str] = None,
    playlist_window_seconds: typing.Optional[jsii.Number] = None,
    program_date_time_interval_seconds: typing.Optional[jsii.Number] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87f398a1f56dd5a78638b6c90bb8102a40772d7c15d100576989267626013d86(
    *,
    ad_markers: typing.Optional[builtins.str] = None,
    ads_on_delivery_restrictions: typing.Optional[builtins.str] = None,
    ad_triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
    encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.HlsEncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    include_dvb_subtitles: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_iframe_only_stream: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    playlist_type: typing.Optional[builtins.str] = None,
    playlist_window_seconds: typing.Optional[jsii.Number] = None,
    program_date_time_interval_seconds: typing.Optional[jsii.Number] = None,
    segment_duration_seconds: typing.Optional[jsii.Number] = None,
    stream_selection: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.StreamSelectionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    use_audio_rendition_group: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e810041b25aa758d918a63335aaf66c8260882c17a1f14a0c6024a377e47581(
    *,
    speke_key_provider: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.SpekeKeyProviderProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c969b579bc64ba1fc64cf397aae32417cbae6217efb342f5ca4de656126a4773(
    *,
    encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.MssEncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    manifest_window_seconds: typing.Optional[jsii.Number] = None,
    segment_duration_seconds: typing.Optional[jsii.Number] = None,
    stream_selection: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.StreamSelectionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31902760039319c8326b4b548986fbad0bbd400bebcf315b1f06706a4fe40f37(
    *,
    resource_id: builtins.str,
    role_arn: builtins.str,
    system_ids: typing.Sequence[builtins.str],
    url: builtins.str,
    certificate_arn: typing.Optional[builtins.str] = None,
    encryption_contract_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.EncryptionContractConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4150b724a2d6d3b325b7f3b3e1bb909d659fb82d5ec1b7008d487cfc1e271e2f(
    *,
    max_video_bits_per_second: typing.Optional[jsii.Number] = None,
    min_video_bits_per_second: typing.Optional[jsii.Number] = None,
    stream_order: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a638c7220ef09ddd89f3e4ec10fad1f2325778760d9246eae3b5eeddb860f07(
    *,
    channel_id: builtins.str,
    id: builtins.str,
    authorization: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.AuthorizationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cmaf_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.CmafPackageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dash_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.DashPackageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    hls_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.HlsPackageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    manifest_name: typing.Optional[builtins.str] = None,
    mss_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOriginEndpoint.MssPackageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    origination: typing.Optional[builtins.str] = None,
    startover_window_seconds: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    time_delay_seconds: typing.Optional[jsii.Number] = None,
    whitelist: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__832773f8276f2faf0375005ff4da2278882f295916abd90cfb3e88d27eae60a2(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    id: builtins.str,
    packaging_group_id: builtins.str,
    cmaf_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.CmafPackageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dash_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.DashPackageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    hls_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.HlsPackageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mss_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.MssPackageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7ec79234b846ccf4526d21383984a066ad27bec0c2e18914091e7914cd114d5(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d9c55f0f743c67ba5f7aa4a3cd9e62904c8332212ea90f623849c6606305faf(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ccd7097ed4dd1ba043d8d7c9253de38870b8dbd6a68978af0352c0722f1d408(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af2d37d8a33d032c8adfec86f32ed79504eb5a23c3a492af26657f35f9c92c25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__399ba5c2786cade2c25cb41b1be97be2455fdf5dfbae120613c3942b2fca070b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPackagingConfiguration.CmafPackageProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d5ed5948330815ccf88262bb614ff3bfcfee39a50c798ef93f31fd435b0cb0a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPackagingConfiguration.DashPackageProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d206943acdbd5b0d12e1841cff1d1941ed07fb9970ebf2c082e7e5128cc3bfd7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPackagingConfiguration.HlsPackageProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7861bbe260077025f4e33fb0ae4337195d16c1ee61d7047a4a9952ab287f760(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPackagingConfiguration.MssPackageProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b76635d4a00dd9342ff2aee3d299dfc0b57f29c37ac4af92f1dcc355e82475a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9524f29fa700d32f03cb88bcaf888d88fd8f7cf49d65982f907421d51bf1e5b(
    *,
    speke_key_provider: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.SpekeKeyProviderProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c702574616d01dedc86e0ed18adf341d64a65dc25d07e27989cf1a7627cdc3f(
    *,
    hls_manifests: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.HlsManifestProperty, typing.Dict[builtins.str, typing.Any]]]]],
    encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.CmafEncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    include_encoder_configuration_in_segments: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    segment_duration_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed10aaf0f578003dd8303a56dd49c8e049f64afd412a966e5158993e671c9449(
    *,
    speke_key_provider: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.SpekeKeyProviderProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d63cccb6b1149c27c25ba78c9e135dc5dc3329c0074867c06f2202b77fd09e7(
    *,
    manifest_layout: typing.Optional[builtins.str] = None,
    manifest_name: typing.Optional[builtins.str] = None,
    min_buffer_time_seconds: typing.Optional[jsii.Number] = None,
    profile: typing.Optional[builtins.str] = None,
    scte_markers_source: typing.Optional[builtins.str] = None,
    stream_selection: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.StreamSelectionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__422b40df588f5b400b121c9d8c5b629c038a8d7a2749bbfff023fbfcd76cc148(
    *,
    dash_manifests: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.DashManifestProperty, typing.Dict[builtins.str, typing.Any]]]]],
    encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.DashEncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    include_encoder_configuration_in_segments: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_iframe_only_stream: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    period_triggers: typing.Optional[typing.Sequence[builtins.str]] = None,
    segment_duration_seconds: typing.Optional[jsii.Number] = None,
    segment_template_format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad4a42ef0d5a0f06be0bfc9686a1d03d8c6adffc71b0b1fd88167f62d2451ff2(
    *,
    preset_speke20_audio: builtins.str,
    preset_speke20_video: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a91a602f74cb33fb7d0bcad3ff19da0b98578a86eaffaca958e54308803fb660(
    *,
    speke_key_provider: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.SpekeKeyProviderProperty, typing.Dict[builtins.str, typing.Any]]],
    constant_initialization_vector: typing.Optional[builtins.str] = None,
    encryption_method: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be2ad1e6428cd7b0f61ba8027ea006d43951e79835a6ecdb9f55ffefade062e3(
    *,
    ad_markers: typing.Optional[builtins.str] = None,
    include_iframe_only_stream: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    manifest_name: typing.Optional[builtins.str] = None,
    program_date_time_interval_seconds: typing.Optional[jsii.Number] = None,
    repeat_ext_x_key: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    stream_selection: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.StreamSelectionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5032d80be495792bc2559665437cf537429fe8f9454a4b44eb2b9dbf595fe5c(
    *,
    hls_manifests: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.HlsManifestProperty, typing.Dict[builtins.str, typing.Any]]]]],
    encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.HlsEncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    include_dvb_subtitles: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    segment_duration_seconds: typing.Optional[jsii.Number] = None,
    use_audio_rendition_group: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb108459b8bd360f0e55c35c750eea25c073892cc7dc2872d2902d86a40730a9(
    *,
    speke_key_provider: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.SpekeKeyProviderProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb6c646ceb48085b7a63cfa957ddc2e42178d58c426a068a46acc6f6cddd297f(
    *,
    manifest_name: typing.Optional[builtins.str] = None,
    stream_selection: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.StreamSelectionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__596bd770b476d92d874770e06c5d3f83482d9ae3598af8013af7e947277aabb9(
    *,
    mss_manifests: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.MssManifestProperty, typing.Dict[builtins.str, typing.Any]]]]],
    encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.MssEncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    segment_duration_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6ba84253e87d787b38627704703d459abb9b442b892a848c98fdde4b3cf420f(
    *,
    role_arn: builtins.str,
    system_ids: typing.Sequence[builtins.str],
    url: builtins.str,
    encryption_contract_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.EncryptionContractConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b8f0e52cfccc1ebe0e2ad93d90f039baf326c3a9c8662423b9760f12f1e8e7e(
    *,
    max_video_bits_per_second: typing.Optional[jsii.Number] = None,
    min_video_bits_per_second: typing.Optional[jsii.Number] = None,
    stream_order: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c18c6cdf8ce44ba79abb7799a3f07a9a73c17f6607c07f5bc7d6c847a36c9051(
    *,
    id: builtins.str,
    packaging_group_id: builtins.str,
    cmaf_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.CmafPackageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dash_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.DashPackageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    hls_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.HlsPackageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mss_package: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingConfiguration.MssPackageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbd1b59c1bc28934f2358b37570be82b032aa4ccdab40560578195b02efe423b(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    id: builtins.str,
    authorization: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingGroup.AuthorizationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    egress_access_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingGroup.LogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__607d136c67f456d025fdf14d7dc1e0a69aff157c4c5eeff267508fa2ae54dc75(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47694a446a5f733392635957d4aa0f98d743244185f6d99b37a7b03e69143ff9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c11025591571c1f0afc6d388f54590a0ff4a8b3888c2d0fd58c4dbcd91281aa1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c8371f8b34356b36eff32cf2cbea4d3f14fcd556b4ab0bd7f5dd7bd2ea117d3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPackagingGroup.AuthorizationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b41c84687cbb3318b0cf57c76ee83dd7efbb0ccf04883a441e2999922e95d713(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPackagingGroup.LogConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5205179917b0f19bc336c90cf83e4b7b624469516be6573083daea59caa9f3f(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa6c921391574b4b282e70426c3be4566d95bf7137942ed0553b6814f022a1fb(
    *,
    cdn_identifier_secret: builtins.str,
    secrets_role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4150658ca39a19a1dfd87e145dfd5096869cfbac1f58d8d09510ec58d44583b3(
    *,
    log_group_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5388a440fca30595e75f64ebeb4a2d57f4c3c7281b7f0215ac9e58ac28536ef7(
    *,
    id: builtins.str,
    authorization: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingGroup.AuthorizationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    egress_access_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackagingGroup.LogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
