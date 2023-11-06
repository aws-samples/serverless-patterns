'''
# AWS::Rekognition Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_rekognition as rekognition
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Rekognition construct libraries](https://constructs.dev/search?q=rekognition)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Rekognition resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Rekognition.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Rekognition](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Rekognition.html).

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
class CfnCollection(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_rekognition.CfnCollection",
):
    '''The ``AWS::Rekognition::Collection`` type creates a server-side container called a collection.

    You can use a collection to store information about detected faces and search for known faces in images, stored videos, and streaming videos.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-collection.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_rekognition as rekognition
        
        cfn_collection = rekognition.CfnCollection(self, "MyCfnCollection",
            collection_id="collectionId",
        
            # the properties below are optional
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
        collection_id: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param collection_id: ID for the collection that you are creating.
        :param tags: A set of tags (key-value pairs) that you want to attach to the collection.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__001405b167561982ca01f91c85c5f23fd1bfd335896f67495614aef9fdc1ebbf)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCollectionProps(collection_id=collection_id, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b782257f4d64c4abcb4d4415ba27cde118213945920a4b2608a0dc326e124dc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ef7614d7ac1ab1a1108a4489935df88c874c2a92a6ca3448ab8aba35c8c23d2e)
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
        '''Returns the Amazon Resource Name of the collection.

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
    @jsii.member(jsii_name="collectionId")
    def collection_id(self) -> builtins.str:
        '''ID for the collection that you are creating.'''
        return typing.cast(builtins.str, jsii.get(self, "collectionId"))

    @collection_id.setter
    def collection_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8475d528ae41527da38a3e3ef20b3988703938f0440df9c74be2cd4234cdb6d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collectionId", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A set of tags (key-value pairs) that you want to attach to the collection.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77f5ab15cea02999fa32036e3558af08ca21b17032d4915d2d3fc7c0c790bbbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_rekognition.CfnCollectionProps",
    jsii_struct_bases=[],
    name_mapping={"collection_id": "collectionId", "tags": "tags"},
)
class CfnCollectionProps:
    def __init__(
        self,
        *,
        collection_id: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCollection``.

        :param collection_id: ID for the collection that you are creating.
        :param tags: A set of tags (key-value pairs) that you want to attach to the collection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-collection.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_rekognition as rekognition
            
            cfn_collection_props = rekognition.CfnCollectionProps(
                collection_id="collectionId",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfc582deefac2ef5bf0ca7c04ad06966543ece2be4f36ffdaa97fbaf33bfb064)
            check_type(argname="argument collection_id", value=collection_id, expected_type=type_hints["collection_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "collection_id": collection_id,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def collection_id(self) -> builtins.str:
        '''ID for the collection that you are creating.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-collection.html#cfn-rekognition-collection-collectionid
        '''
        result = self._values.get("collection_id")
        assert result is not None, "Required property 'collection_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A set of tags (key-value pairs) that you want to attach to the collection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-collection.html#cfn-rekognition-collection-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCollectionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnProject(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_rekognition.CfnProject",
):
    '''The ``AWS::Rekognition::Project`` type creates an Amazon Rekognition Custom Labels project.

    A project is a group of resources needed to create and manage versions of an Amazon Rekognition Custom Labels model.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-project.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_rekognition as rekognition
        
        cfn_project = rekognition.CfnProject(self, "MyCfnProject",
            project_name="projectName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        project_name: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param project_name: The name of the project to create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14434bd621070d38889fc701fc289b3379981bee9c73fd7502773f1ee6007596)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProjectProps(project_name=project_name)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0172e641847a31da5e6877581313d2ece51b9650bcb74b1b80ba13e563323cc0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ecd6c0ddb539c1c7c5df4ac80934172fad202067215980c77299274cd21f9555)
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
        '''Returns the Amazon Resource Name of the project.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="projectName")
    def project_name(self) -> builtins.str:
        '''The name of the project to create.'''
        return typing.cast(builtins.str, jsii.get(self, "projectName"))

    @project_name.setter
    def project_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a1962fa2cac2e24ef346e8a95c9cce8b1cf9023aaeae155bf61e10c5dbddf83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_rekognition.CfnProjectProps",
    jsii_struct_bases=[],
    name_mapping={"project_name": "projectName"},
)
class CfnProjectProps:
    def __init__(self, *, project_name: builtins.str) -> None:
        '''Properties for defining a ``CfnProject``.

        :param project_name: The name of the project to create.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-project.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_rekognition as rekognition
            
            cfn_project_props = rekognition.CfnProjectProps(
                project_name="projectName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6ffefd83213c744dc48a7e730e4f4ba6abf92dfd04904ffa9f7361b3df6c6d3)
            check_type(argname="argument project_name", value=project_name, expected_type=type_hints["project_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project_name": project_name,
        }

    @builtins.property
    def project_name(self) -> builtins.str:
        '''The name of the project to create.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-project.html#cfn-rekognition-project-projectname
        '''
        result = self._values.get("project_name")
        assert result is not None, "Required property 'project_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnStreamProcessor(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_rekognition.CfnStreamProcessor",
):
    '''The ``AWS::Rekognition::StreamProcessor`` type creates a stream processor used to detect and recognize faces or to detect connected home labels in a streaming video.

    Amazon Rekognition Video is a consumer of live video from Amazon Kinesis Video Streams. There are two different settings for stream processors in Amazon Rekognition, one for detecting faces and one for connected home features.

    If you are creating a stream processor for detecting faces, you provide a Kinesis video stream (input) and a Kinesis data stream (output). You also specify the face recognition criteria in FaceSearchSettings. For example, the collection containing faces that you want to recognize.

    If you are creating a stream processor for detection of connected home labels, you provide a Kinesis video stream for input, and for output an Amazon S3 bucket and an Amazon SNS topic. You can also provide a KMS key ID to encrypt the data sent to your Amazon S3 bucket. You specify what you want to detect in ConnectedHomeSettings, such as people, packages, and pets.

    You can also specify where in the frame you want Amazon Rekognition to monitor with BoundingBoxRegionsOfInterest and PolygonRegionsOfInterest. The Name is used to manage the stream processor and it is the identifier for the stream processor. The ``AWS::Rekognition::StreamProcessor`` resource creates a stream processor in the same Region where you create the Amazon CloudFormation stack.

    For more information, see `CreateStreamProcessor <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_rekognition as rekognition
        
        # polygon_regions_of_interest: Any
        
        cfn_stream_processor = rekognition.CfnStreamProcessor(self, "MyCfnStreamProcessor",
            kinesis_video_stream=rekognition.CfnStreamProcessor.KinesisVideoStreamProperty(
                arn="arn"
            ),
            role_arn="roleArn",
        
            # the properties below are optional
            bounding_box_regions_of_interest=[rekognition.CfnStreamProcessor.BoundingBoxProperty(
                height=123,
                left=123,
                top=123,
                width=123
            )],
            connected_home_settings=rekognition.CfnStreamProcessor.ConnectedHomeSettingsProperty(
                labels=["labels"],
        
                # the properties below are optional
                min_confidence=123
            ),
            data_sharing_preference=rekognition.CfnStreamProcessor.DataSharingPreferenceProperty(
                opt_in=False
            ),
            face_search_settings=rekognition.CfnStreamProcessor.FaceSearchSettingsProperty(
                collection_id="collectionId",
        
                # the properties below are optional
                face_match_threshold=123
            ),
            kinesis_data_stream=rekognition.CfnStreamProcessor.KinesisDataStreamProperty(
                arn="arn"
            ),
            kms_key_id="kmsKeyId",
            name="name",
            notification_channel=rekognition.CfnStreamProcessor.NotificationChannelProperty(
                arn="arn"
            ),
            polygon_regions_of_interest=polygon_regions_of_interest,
            s3_destination=rekognition.CfnStreamProcessor.S3DestinationProperty(
                bucket_name="bucketName",
        
                # the properties below are optional
                object_key_prefix="objectKeyPrefix"
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
        kinesis_video_stream: typing.Union[_IResolvable_da3f097b, typing.Union["CfnStreamProcessor.KinesisVideoStreamProperty", typing.Dict[builtins.str, typing.Any]]],
        role_arn: builtins.str,
        bounding_box_regions_of_interest: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStreamProcessor.BoundingBoxProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        connected_home_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStreamProcessor.ConnectedHomeSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        data_sharing_preference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStreamProcessor.DataSharingPreferenceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        face_search_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStreamProcessor.FaceSearchSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        kinesis_data_stream: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStreamProcessor.KinesisDataStreamProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        notification_channel: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStreamProcessor.NotificationChannelProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        polygon_regions_of_interest: typing.Any = None,
        s3_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStreamProcessor.S3DestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param kinesis_video_stream: The Kinesis video stream that provides the source of the streaming video for an Amazon Rekognition Video stream processor. For more information, see `KinesisVideoStream <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_KinesisVideoStream>`_ .
        :param role_arn: The ARN of the IAM role that allows access to the stream processor. The IAM role provides Rekognition read permissions to the Kinesis stream. It also provides write permissions to an Amazon S3 bucket and Amazon Simple Notification Service topic for a connected home stream processor. This is required for both face search and connected home stream processors. For information about constraints, see the RoleArn section of `CreateStreamProcessor <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor>`_ .
        :param bounding_box_regions_of_interest: List of BoundingBox objects, each of which denotes a region of interest on screen. For more information, see the BoundingBox field of `RegionOfInterest <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_RegionOfInterest>`_ .
        :param connected_home_settings: Connected home settings to use on a streaming video. You can use a stream processor for connected home features and select what you want the stream processor to detect, such as people or pets. When the stream processor has started, one notification is sent for each object class specified. For more information, see the ConnectedHome section of `StreamProcessorSettings <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessorSettings>`_ .
        :param data_sharing_preference: Allows you to opt in or opt out to share data with Rekognition to improve model performance. You can choose this option at the account level or on a per-stream basis. Note that if you opt out at the account level this setting is ignored on individual streams. For more information, see `StreamProcessorDataSharingPreference <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessorDataSharingPreference>`_ .
        :param face_search_settings: The input parameters used to recognize faces in a streaming video analyzed by an Amazon Rekognition stream processor. For more information regarding the contents of the parameters, see `FaceSearchSettings <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_FaceSearchSettings>`_ .
        :param kinesis_data_stream: Amazon Rekognition's Video Stream Processor takes a Kinesis video stream as input. This is the Amazon Kinesis Data Streams instance to which the Amazon Rekognition stream processor streams the analysis results. This must be created within the constraints specified at `KinesisDataStream <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_KinesisDataStream>`_ .
        :param kms_key_id: The identifier for your Amazon Key Management Service key (Amazon KMS key). Optional parameter for connected home stream processors used to encrypt results and data published to your Amazon S3 bucket. For more information, see the KMSKeyId section of `CreateStreamProcessor <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor>`_ .
        :param name: The Name attribute specifies the name of the stream processor and it must be within the constraints described in the Name section of `StreamProcessor <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessor>`_ . If you don't specify a name, Amazon CloudFormation generates a unique ID and uses that ID for the stream processor name.
        :param notification_channel: The Amazon Simple Notification Service topic to which Amazon Rekognition publishes the object detection results and completion status of a video analysis operation. Amazon Rekognition publishes a notification the first time an object of interest or a person is detected in the video stream. Amazon Rekognition also publishes an end-of-session notification with a summary when the stream processing session is complete. For more information, see `StreamProcessorNotificationChannel <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessorNotificationChannel>`_ .
        :param polygon_regions_of_interest: A set of ordered lists of `Point <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_Point>`_ objects. Each entry of the set contains a polygon denoting a region of interest on the screen. Each polygon is an ordered list of `Point <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_Point>`_ objects. For more information, see the Polygon field of `RegionOfInterest <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_RegionOfInterest>`_ .
        :param s3_destination: The Amazon S3 bucket location to which Amazon Rekognition publishes the detailed inference results of a video analysis operation. For more information, see the S3Destination section of `StreamProcessorOutput <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessorOutput>`_ .
        :param tags: A set of tags (key-value pairs) that you want to attach to the stream processor. For more information, see the Tags section of `CreateStreamProcessor <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db29995773d1d6016b19ea60d9d43e43a080dc683708f8f6806c20b41de3b4e9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStreamProcessorProps(
            kinesis_video_stream=kinesis_video_stream,
            role_arn=role_arn,
            bounding_box_regions_of_interest=bounding_box_regions_of_interest,
            connected_home_settings=connected_home_settings,
            data_sharing_preference=data_sharing_preference,
            face_search_settings=face_search_settings,
            kinesis_data_stream=kinesis_data_stream,
            kms_key_id=kms_key_id,
            name=name,
            notification_channel=notification_channel,
            polygon_regions_of_interest=polygon_regions_of_interest,
            s3_destination=s3_destination,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40ab64ef7968d6308fa66fa8cd30426d2afa22a69cd4c0add4fad58d1123b3d8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__682d423a7e9ce2fa6f2875579551bac52247181a6905c21784d80a153db8261e)
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
        '''Amazon Resource Name for the newly created stream processor.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''Current status of the Amazon Rekognition stream processor.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusMessage")
    def attr_status_message(self) -> builtins.str:
        '''Detailed status message about the stream processor.

        :cloudformationAttribute: StatusMessage
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusMessage"))

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
    @jsii.member(jsii_name="kinesisVideoStream")
    def kinesis_video_stream(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnStreamProcessor.KinesisVideoStreamProperty"]:
        '''The Kinesis video stream that provides the source of the streaming video for an Amazon Rekognition Video stream processor.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnStreamProcessor.KinesisVideoStreamProperty"], jsii.get(self, "kinesisVideoStream"))

    @kinesis_video_stream.setter
    def kinesis_video_stream(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnStreamProcessor.KinesisVideoStreamProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__544bd519e8f2f595255e1dda00353bdad3a1f366808872e2a020ab7ac0c68ede)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kinesisVideoStream", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The ARN of the IAM role that allows access to the stream processor.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ceb033b416a9b50d7e1f7b205e95dc9fc9eeaa5ebe8b01d77b8db945e1617e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="boundingBoxRegionsOfInterest")
    def bounding_box_regions_of_interest(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStreamProcessor.BoundingBoxProperty"]]]]:
        '''List of BoundingBox objects, each of which denotes a region of interest on screen.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStreamProcessor.BoundingBoxProperty"]]]], jsii.get(self, "boundingBoxRegionsOfInterest"))

    @bounding_box_regions_of_interest.setter
    def bounding_box_regions_of_interest(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStreamProcessor.BoundingBoxProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acc75e18dc798eb00941485f051f88d386cbeab51667cb8be061da0b98c63396)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "boundingBoxRegionsOfInterest", value)

    @builtins.property
    @jsii.member(jsii_name="connectedHomeSettings")
    def connected_home_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStreamProcessor.ConnectedHomeSettingsProperty"]]:
        '''Connected home settings to use on a streaming video.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStreamProcessor.ConnectedHomeSettingsProperty"]], jsii.get(self, "connectedHomeSettings"))

    @connected_home_settings.setter
    def connected_home_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStreamProcessor.ConnectedHomeSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8917bfe75ce52160b79d51e35bc32988d0117df4b4c5c2fcc5738d3adcbff9b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectedHomeSettings", value)

    @builtins.property
    @jsii.member(jsii_name="dataSharingPreference")
    def data_sharing_preference(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStreamProcessor.DataSharingPreferenceProperty"]]:
        '''Allows you to opt in or opt out to share data with Rekognition to improve model performance.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStreamProcessor.DataSharingPreferenceProperty"]], jsii.get(self, "dataSharingPreference"))

    @data_sharing_preference.setter
    def data_sharing_preference(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStreamProcessor.DataSharingPreferenceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb32e5089c11a4939bd2e9bee353c9a78566e808db896e1c677dd43c12926ebd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSharingPreference", value)

    @builtins.property
    @jsii.member(jsii_name="faceSearchSettings")
    def face_search_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStreamProcessor.FaceSearchSettingsProperty"]]:
        '''The input parameters used to recognize faces in a streaming video analyzed by an Amazon Rekognition stream processor.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStreamProcessor.FaceSearchSettingsProperty"]], jsii.get(self, "faceSearchSettings"))

    @face_search_settings.setter
    def face_search_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStreamProcessor.FaceSearchSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__566df51893024802a690a50b28be352b9fc757428a22f708bee01096b284279f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "faceSearchSettings", value)

    @builtins.property
    @jsii.member(jsii_name="kinesisDataStream")
    def kinesis_data_stream(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStreamProcessor.KinesisDataStreamProperty"]]:
        '''Amazon Rekognition's Video Stream Processor takes a Kinesis video stream as input.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStreamProcessor.KinesisDataStreamProperty"]], jsii.get(self, "kinesisDataStream"))

    @kinesis_data_stream.setter
    def kinesis_data_stream(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStreamProcessor.KinesisDataStreamProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__389631c246d3fdbe6ca66d4b9806147f81f4854193101c9c3341c10c3a06de51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kinesisDataStream", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The identifier for your Amazon Key Management Service key (Amazon KMS key).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9c6d353ba33bff601fce6ba9916bbea7fe2b890b0842c5ce26e962eb292dc57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The Name attribute specifies the name of the stream processor and it must be within the constraints described in the Name section of `StreamProcessor <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessor>`_ . If you don't specify a name, Amazon CloudFormation generates a unique ID and uses that ID for the stream processor name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eea2935c2a6e509f6f9b8bac8defe6d3a7c700401c6d0e1fed5c595cc78a49a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="notificationChannel")
    def notification_channel(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStreamProcessor.NotificationChannelProperty"]]:
        '''The Amazon Simple Notification Service topic to which Amazon Rekognition publishes the object detection results and completion status of a video analysis operation.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStreamProcessor.NotificationChannelProperty"]], jsii.get(self, "notificationChannel"))

    @notification_channel.setter
    def notification_channel(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStreamProcessor.NotificationChannelProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8781502f6d929597da76936c53e5a7d0df2ea7201c636dff5961d377bee07178)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationChannel", value)

    @builtins.property
    @jsii.member(jsii_name="polygonRegionsOfInterest")
    def polygon_regions_of_interest(self) -> typing.Any:
        '''A set of ordered lists of `Point <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_Point>`_ objects. Each entry of the set contains a polygon denoting a region of interest on the screen. Each polygon is an ordered list of `Point <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_Point>`_ objects. For more information, see the Polygon field of `RegionOfInterest <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_RegionOfInterest>`_ .'''
        return typing.cast(typing.Any, jsii.get(self, "polygonRegionsOfInterest"))

    @polygon_regions_of_interest.setter
    def polygon_regions_of_interest(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32adcb2805477bf062e3a38ebed38564ceb277accb2b42fac998c1b5ce354c54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "polygonRegionsOfInterest", value)

    @builtins.property
    @jsii.member(jsii_name="s3Destination")
    def s3_destination(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStreamProcessor.S3DestinationProperty"]]:
        '''The Amazon S3 bucket location to which Amazon Rekognition publishes the detailed inference results of a video analysis operation.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStreamProcessor.S3DestinationProperty"]], jsii.get(self, "s3Destination"))

    @s3_destination.setter
    def s3_destination(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStreamProcessor.S3DestinationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0366aae7f57073426925f9ebba0e5762ee7449ce53690b7fc2381679f27838c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Destination", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A set of tags (key-value pairs) that you want to attach to the stream processor.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a544bfd783dfe89e1f97d483f2cfa712d54a14e78538c5e39f6f4febe9970aeb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rekognition.CfnStreamProcessor.BoundingBoxProperty",
        jsii_struct_bases=[],
        name_mapping={
            "height": "height",
            "left": "left",
            "top": "top",
            "width": "width",
        },
    )
    class BoundingBoxProperty:
        def __init__(
            self,
            *,
            height: jsii.Number,
            left: jsii.Number,
            top: jsii.Number,
            width: jsii.Number,
        ) -> None:
            '''Identifies the bounding box around the label, face, text, or personal protective equipment.

            The ``left`` (x-coordinate) and ``top`` (y-coordinate) are coordinates representing the top and left sides of the bounding box. Note that the upper-left corner of the image is the origin (0,0).

            The ``top`` and ``left`` values returned are ratios of the overall image size. For example, if the input image is 700x200 pixels, and the top-left coordinate of the bounding box is 350x50 pixels, the API returns a ``left`` value of 0.5 (350/700) and a ``top`` value of 0.25 (50/200).

            The ``width`` and ``height`` values represent the dimensions of the bounding box as a ratio of the overall image dimension. For example, if the input image is 700x200 pixels, and the bounding box width is 70 pixels, the width returned is 0.1. For more information, see `BoundingBox <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_BoundingBox>`_ .
            .. epigraph::

               The bounding box coordinates can have negative values. For example, if Amazon Rekognition is able to detect a face that is at the image edge and is only partially visible, the service can return coordinates that are outside the image bounds and, depending on the image edge, you might get negative values or values greater than 1 for the ``left`` or ``top`` values.

            :param height: Height of the bounding box as a ratio of the overall image height.
            :param left: Left coordinate of the bounding box as a ratio of overall image width.
            :param top: Top coordinate of the bounding box as a ratio of overall image height.
            :param width: Width of the bounding box as a ratio of the overall image width.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-boundingbox.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rekognition as rekognition
                
                bounding_box_property = rekognition.CfnStreamProcessor.BoundingBoxProperty(
                    height=123,
                    left=123,
                    top=123,
                    width=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c7bad855b7d71ef59694b32449dc63de52f35f2ad462103fe21128c7c33206a1)
                check_type(argname="argument height", value=height, expected_type=type_hints["height"])
                check_type(argname="argument left", value=left, expected_type=type_hints["left"])
                check_type(argname="argument top", value=top, expected_type=type_hints["top"])
                check_type(argname="argument width", value=width, expected_type=type_hints["width"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "height": height,
                "left": left,
                "top": top,
                "width": width,
            }

        @builtins.property
        def height(self) -> jsii.Number:
            '''Height of the bounding box as a ratio of the overall image height.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-boundingbox.html#cfn-rekognition-streamprocessor-boundingbox-height
            '''
            result = self._values.get("height")
            assert result is not None, "Required property 'height' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def left(self) -> jsii.Number:
            '''Left coordinate of the bounding box as a ratio of overall image width.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-boundingbox.html#cfn-rekognition-streamprocessor-boundingbox-left
            '''
            result = self._values.get("left")
            assert result is not None, "Required property 'left' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def top(self) -> jsii.Number:
            '''Top coordinate of the bounding box as a ratio of overall image height.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-boundingbox.html#cfn-rekognition-streamprocessor-boundingbox-top
            '''
            result = self._values.get("top")
            assert result is not None, "Required property 'top' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def width(self) -> jsii.Number:
            '''Width of the bounding box as a ratio of the overall image width.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-boundingbox.html#cfn-rekognition-streamprocessor-boundingbox-width
            '''
            result = self._values.get("width")
            assert result is not None, "Required property 'width' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BoundingBoxProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rekognition.CfnStreamProcessor.ConnectedHomeSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"labels": "labels", "min_confidence": "minConfidence"},
    )
    class ConnectedHomeSettingsProperty:
        def __init__(
            self,
            *,
            labels: typing.Sequence[builtins.str],
            min_confidence: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Connected home settings to use on a streaming video.

            Defining the settings is required in the request parameter for ``CreateStreamProcessor`` . Including this setting in the CreateStreamProcessor request lets you use the stream processor for connected home features. You can then select what you want the stream processor to detect, such as people or pets.

            When the stream processor has started, one notification is sent for each object class specified. For example, if packages and pets are selected, one SNS notification is published the first time a package is detected and one SNS notification is published the first time a pet is detected. An end-of-session summary is also published. For more information, see the ConnectedHome section of `StreamProcessorSettings <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessorSettings>`_ .

            :param labels: Specifies what you want to detect in the video, such as people, packages, or pets. The current valid labels you can include in this list are: "PERSON", "PET", "PACKAGE", and "ALL".
            :param min_confidence: The minimum confidence required to label an object in the video.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-connectedhomesettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rekognition as rekognition
                
                connected_home_settings_property = rekognition.CfnStreamProcessor.ConnectedHomeSettingsProperty(
                    labels=["labels"],
                
                    # the properties below are optional
                    min_confidence=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__586438043baa3b2c31178aa9461612acb2d0d0ae0aac237b6e61cabac7e5de67)
                check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
                check_type(argname="argument min_confidence", value=min_confidence, expected_type=type_hints["min_confidence"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "labels": labels,
            }
            if min_confidence is not None:
                self._values["min_confidence"] = min_confidence

        @builtins.property
        def labels(self) -> typing.List[builtins.str]:
            '''Specifies what you want to detect in the video, such as people, packages, or pets.

            The current valid labels you can include in this list are: "PERSON", "PET", "PACKAGE", and "ALL".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-connectedhomesettings.html#cfn-rekognition-streamprocessor-connectedhomesettings-labels
            '''
            result = self._values.get("labels")
            assert result is not None, "Required property 'labels' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def min_confidence(self) -> typing.Optional[jsii.Number]:
            '''The minimum confidence required to label an object in the video.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-connectedhomesettings.html#cfn-rekognition-streamprocessor-connectedhomesettings-minconfidence
            '''
            result = self._values.get("min_confidence")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectedHomeSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rekognition.CfnStreamProcessor.DataSharingPreferenceProperty",
        jsii_struct_bases=[],
        name_mapping={"opt_in": "optIn"},
    )
    class DataSharingPreferenceProperty:
        def __init__(
            self,
            *,
            opt_in: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''Allows you to opt in or opt out to share data with Rekognition to improve model performance.

            You can choose this option at the account level or on a per-stream basis. Note that if you opt out at the account level, this setting is ignored on individual streams. For more information, see `StreamProcessorDataSharingPreference <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessorDataSharingPreference>`_ .

            :param opt_in: Describes the opt-in status applied to a stream processor's data sharing policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-datasharingpreference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rekognition as rekognition
                
                data_sharing_preference_property = rekognition.CfnStreamProcessor.DataSharingPreferenceProperty(
                    opt_in=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3ebd03a0efbe12d5f07382e61ebfcb962dda51221996e196f2b8497594573d49)
                check_type(argname="argument opt_in", value=opt_in, expected_type=type_hints["opt_in"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "opt_in": opt_in,
            }

        @builtins.property
        def opt_in(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Describes the opt-in status applied to a stream processor's data sharing policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-datasharingpreference.html#cfn-rekognition-streamprocessor-datasharingpreference-optin
            '''
            result = self._values.get("opt_in")
            assert result is not None, "Required property 'opt_in' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSharingPreferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rekognition.CfnStreamProcessor.FaceSearchSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "collection_id": "collectionId",
            "face_match_threshold": "faceMatchThreshold",
        },
    )
    class FaceSearchSettingsProperty:
        def __init__(
            self,
            *,
            collection_id: builtins.str,
            face_match_threshold: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The input parameters used to recognize faces in a streaming video analyzed by a Amazon Rekognition stream processor.

            ``FaceSearchSettings`` is a request parameter for `CreateStreamProcessor <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor>`_ . For more information, see `FaceSearchSettings <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_FaceSearchSettings>`_ .

            :param collection_id: The ID of a collection that contains faces that you want to search for.
            :param face_match_threshold: Minimum face match confidence score that must be met to return a result for a recognized face. The default is 80. 0 is the lowest confidence. 100 is the highest confidence. Values between 0 and 100 are accepted, and values lower than 80 are set to 80.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-facesearchsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rekognition as rekognition
                
                face_search_settings_property = rekognition.CfnStreamProcessor.FaceSearchSettingsProperty(
                    collection_id="collectionId",
                
                    # the properties below are optional
                    face_match_threshold=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b1d920a4a5c5227a1362117b6d7177bc83ca757ab3ddf859bfaea3e1bf2b2128)
                check_type(argname="argument collection_id", value=collection_id, expected_type=type_hints["collection_id"])
                check_type(argname="argument face_match_threshold", value=face_match_threshold, expected_type=type_hints["face_match_threshold"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "collection_id": collection_id,
            }
            if face_match_threshold is not None:
                self._values["face_match_threshold"] = face_match_threshold

        @builtins.property
        def collection_id(self) -> builtins.str:
            '''The ID of a collection that contains faces that you want to search for.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-facesearchsettings.html#cfn-rekognition-streamprocessor-facesearchsettings-collectionid
            '''
            result = self._values.get("collection_id")
            assert result is not None, "Required property 'collection_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def face_match_threshold(self) -> typing.Optional[jsii.Number]:
            '''Minimum face match confidence score that must be met to return a result for a recognized face.

            The default is 80. 0 is the lowest confidence. 100 is the highest confidence. Values between 0 and 100 are accepted, and values lower than 80 are set to 80.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-facesearchsettings.html#cfn-rekognition-streamprocessor-facesearchsettings-facematchthreshold
            '''
            result = self._values.get("face_match_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FaceSearchSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rekognition.CfnStreamProcessor.KinesisDataStreamProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn"},
    )
    class KinesisDataStreamProperty:
        def __init__(self, *, arn: builtins.str) -> None:
            '''Amazon Rekognition Video Stream Processor take as input a Kinesis video stream (Input) and a Kinesis data stream (Output).

            This is the Amazon Kinesis Data Streams instance to which the Amazon Rekognition stream processor streams the analysis results. This must be created within the constraints specified at `KinesisDataStream <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_KinesisDataStream>`_ .

            :param arn: ARN of the output Amazon Kinesis Data Streams stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-kinesisdatastream.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rekognition as rekognition
                
                kinesis_data_stream_property = rekognition.CfnStreamProcessor.KinesisDataStreamProperty(
                    arn="arn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d1a9643f21ce9cd202be0cc632d42c8de7c3bc2d1ec5dc6e2a56db210204aa04)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "arn": arn,
            }

        @builtins.property
        def arn(self) -> builtins.str:
            '''ARN of the output Amazon Kinesis Data Streams stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-kinesisdatastream.html#cfn-rekognition-streamprocessor-kinesisdatastream-arn
            '''
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisDataStreamProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rekognition.CfnStreamProcessor.KinesisVideoStreamProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn"},
    )
    class KinesisVideoStreamProperty:
        def __init__(self, *, arn: builtins.str) -> None:
            '''The Kinesis video stream that provides the source of the streaming video for an Amazon Rekognition Video stream processor.

            For more information, see `KinesisVideoStream <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_KinesisVideoStream>`_ .

            :param arn: ARN of the Kinesis video stream stream that streams the source video.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-kinesisvideostream.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rekognition as rekognition
                
                kinesis_video_stream_property = rekognition.CfnStreamProcessor.KinesisVideoStreamProperty(
                    arn="arn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__11c5113726b14e2f510aef1499acb05b38edb79b09083d31795eefd5f67eaf71)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "arn": arn,
            }

        @builtins.property
        def arn(self) -> builtins.str:
            '''ARN of the Kinesis video stream stream that streams the source video.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-kinesisvideostream.html#cfn-rekognition-streamprocessor-kinesisvideostream-arn
            '''
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisVideoStreamProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rekognition.CfnStreamProcessor.NotificationChannelProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn"},
    )
    class NotificationChannelProperty:
        def __init__(self, *, arn: builtins.str) -> None:
            '''The Amazon Simple Notification Service topic to which Amazon Rekognition publishes the object detection results and completion status of a video analysis operation.

            Amazon Rekognition publishes a notification the first time an object of interest or a person is detected in the video stream. Amazon Rekognition also publishes an an end-of-session notification with a summary when the stream processing session is complete. For more information, see `StreamProcessorNotificationChannel <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessorNotificationChannel>`_ .

            :param arn: The ARN of the SNS topic that receives notifications.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-notificationchannel.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rekognition as rekognition
                
                notification_channel_property = rekognition.CfnStreamProcessor.NotificationChannelProperty(
                    arn="arn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bf89b771464a553c692cbb9b3c1b09ca50ed7849163df9f19249032781e02e78)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "arn": arn,
            }

        @builtins.property
        def arn(self) -> builtins.str:
            '''The ARN of the SNS topic that receives notifications.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-notificationchannel.html#cfn-rekognition-streamprocessor-notificationchannel-arn
            '''
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotificationChannelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rekognition.CfnStreamProcessor.PointProperty",
        jsii_struct_bases=[],
        name_mapping={"x": "x", "y": "y"},
    )
    class PointProperty:
        def __init__(self, *, x: jsii.Number, y: jsii.Number) -> None:
            '''An (X, Y) cartesian coordinate denoting a point on the frame.

            :param x: The X coordinate of the point.
            :param y: The Y coordinate of the point.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-point.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rekognition as rekognition
                
                point_property = rekognition.CfnStreamProcessor.PointProperty(
                    x=123,
                    y=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e73e14e2930474187d1e5f6a0777aed81ad8438a2a23547a3ed5ca26b468afe6)
                check_type(argname="argument x", value=x, expected_type=type_hints["x"])
                check_type(argname="argument y", value=y, expected_type=type_hints["y"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "x": x,
                "y": y,
            }

        @builtins.property
        def x(self) -> jsii.Number:
            '''The X coordinate of the point.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-point.html#cfn-rekognition-streamprocessor-point-x
            '''
            result = self._values.get("x")
            assert result is not None, "Required property 'x' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def y(self) -> jsii.Number:
            '''The Y coordinate of the point.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-point.html#cfn-rekognition-streamprocessor-point-y
            '''
            result = self._values.get("y")
            assert result is not None, "Required property 'y' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PointProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rekognition.CfnStreamProcessor.S3DestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_name": "bucketName",
            "object_key_prefix": "objectKeyPrefix",
        },
    )
    class S3DestinationProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            object_key_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The Amazon S3 bucket location to which Amazon Rekognition publishes the detailed inference results of a video analysis operation.

            These results include the name of the stream processor resource, the session ID of the stream processing session, and labeled timestamps and bounding boxes for detected labels. For more information, see `S3Destination <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_S3Destination>`_ .

            :param bucket_name: Describes the destination Amazon Simple Storage Service (Amazon S3) bucket name of a stream processor's exports.
            :param object_key_prefix: Describes the destination Amazon Simple Storage Service (Amazon S3) object keys of a stream processor's exports.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-s3destination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rekognition as rekognition
                
                s3_destination_property = rekognition.CfnStreamProcessor.S3DestinationProperty(
                    bucket_name="bucketName",
                
                    # the properties below are optional
                    object_key_prefix="objectKeyPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e523487c02bfde11953c715444eddb9f2ed729eec0aa81767c2868bf914262ce)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument object_key_prefix", value=object_key_prefix, expected_type=type_hints["object_key_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
            }
            if object_key_prefix is not None:
                self._values["object_key_prefix"] = object_key_prefix

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''Describes the destination Amazon Simple Storage Service (Amazon S3) bucket name of a stream processor's exports.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-s3destination.html#cfn-rekognition-streamprocessor-s3destination-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def object_key_prefix(self) -> typing.Optional[builtins.str]:
            '''Describes the destination Amazon Simple Storage Service (Amazon S3) object keys of a stream processor's exports.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rekognition-streamprocessor-s3destination.html#cfn-rekognition-streamprocessor-s3destination-objectkeyprefix
            '''
            result = self._values.get("object_key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3DestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_rekognition.CfnStreamProcessorProps",
    jsii_struct_bases=[],
    name_mapping={
        "kinesis_video_stream": "kinesisVideoStream",
        "role_arn": "roleArn",
        "bounding_box_regions_of_interest": "boundingBoxRegionsOfInterest",
        "connected_home_settings": "connectedHomeSettings",
        "data_sharing_preference": "dataSharingPreference",
        "face_search_settings": "faceSearchSettings",
        "kinesis_data_stream": "kinesisDataStream",
        "kms_key_id": "kmsKeyId",
        "name": "name",
        "notification_channel": "notificationChannel",
        "polygon_regions_of_interest": "polygonRegionsOfInterest",
        "s3_destination": "s3Destination",
        "tags": "tags",
    },
)
class CfnStreamProcessorProps:
    def __init__(
        self,
        *,
        kinesis_video_stream: typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamProcessor.KinesisVideoStreamProperty, typing.Dict[builtins.str, typing.Any]]],
        role_arn: builtins.str,
        bounding_box_regions_of_interest: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamProcessor.BoundingBoxProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        connected_home_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamProcessor.ConnectedHomeSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        data_sharing_preference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamProcessor.DataSharingPreferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        face_search_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamProcessor.FaceSearchSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        kinesis_data_stream: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamProcessor.KinesisDataStreamProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        notification_channel: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamProcessor.NotificationChannelProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        polygon_regions_of_interest: typing.Any = None,
        s3_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamProcessor.S3DestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnStreamProcessor``.

        :param kinesis_video_stream: The Kinesis video stream that provides the source of the streaming video for an Amazon Rekognition Video stream processor. For more information, see `KinesisVideoStream <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_KinesisVideoStream>`_ .
        :param role_arn: The ARN of the IAM role that allows access to the stream processor. The IAM role provides Rekognition read permissions to the Kinesis stream. It also provides write permissions to an Amazon S3 bucket and Amazon Simple Notification Service topic for a connected home stream processor. This is required for both face search and connected home stream processors. For information about constraints, see the RoleArn section of `CreateStreamProcessor <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor>`_ .
        :param bounding_box_regions_of_interest: List of BoundingBox objects, each of which denotes a region of interest on screen. For more information, see the BoundingBox field of `RegionOfInterest <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_RegionOfInterest>`_ .
        :param connected_home_settings: Connected home settings to use on a streaming video. You can use a stream processor for connected home features and select what you want the stream processor to detect, such as people or pets. When the stream processor has started, one notification is sent for each object class specified. For more information, see the ConnectedHome section of `StreamProcessorSettings <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessorSettings>`_ .
        :param data_sharing_preference: Allows you to opt in or opt out to share data with Rekognition to improve model performance. You can choose this option at the account level or on a per-stream basis. Note that if you opt out at the account level this setting is ignored on individual streams. For more information, see `StreamProcessorDataSharingPreference <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessorDataSharingPreference>`_ .
        :param face_search_settings: The input parameters used to recognize faces in a streaming video analyzed by an Amazon Rekognition stream processor. For more information regarding the contents of the parameters, see `FaceSearchSettings <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_FaceSearchSettings>`_ .
        :param kinesis_data_stream: Amazon Rekognition's Video Stream Processor takes a Kinesis video stream as input. This is the Amazon Kinesis Data Streams instance to which the Amazon Rekognition stream processor streams the analysis results. This must be created within the constraints specified at `KinesisDataStream <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_KinesisDataStream>`_ .
        :param kms_key_id: The identifier for your Amazon Key Management Service key (Amazon KMS key). Optional parameter for connected home stream processors used to encrypt results and data published to your Amazon S3 bucket. For more information, see the KMSKeyId section of `CreateStreamProcessor <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor>`_ .
        :param name: The Name attribute specifies the name of the stream processor and it must be within the constraints described in the Name section of `StreamProcessor <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessor>`_ . If you don't specify a name, Amazon CloudFormation generates a unique ID and uses that ID for the stream processor name.
        :param notification_channel: The Amazon Simple Notification Service topic to which Amazon Rekognition publishes the object detection results and completion status of a video analysis operation. Amazon Rekognition publishes a notification the first time an object of interest or a person is detected in the video stream. Amazon Rekognition also publishes an end-of-session notification with a summary when the stream processing session is complete. For more information, see `StreamProcessorNotificationChannel <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessorNotificationChannel>`_ .
        :param polygon_regions_of_interest: A set of ordered lists of `Point <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_Point>`_ objects. Each entry of the set contains a polygon denoting a region of interest on the screen. Each polygon is an ordered list of `Point <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_Point>`_ objects. For more information, see the Polygon field of `RegionOfInterest <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_RegionOfInterest>`_ .
        :param s3_destination: The Amazon S3 bucket location to which Amazon Rekognition publishes the detailed inference results of a video analysis operation. For more information, see the S3Destination section of `StreamProcessorOutput <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessorOutput>`_ .
        :param tags: A set of tags (key-value pairs) that you want to attach to the stream processor. For more information, see the Tags section of `CreateStreamProcessor <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_rekognition as rekognition
            
            # polygon_regions_of_interest: Any
            
            cfn_stream_processor_props = rekognition.CfnStreamProcessorProps(
                kinesis_video_stream=rekognition.CfnStreamProcessor.KinesisVideoStreamProperty(
                    arn="arn"
                ),
                role_arn="roleArn",
            
                # the properties below are optional
                bounding_box_regions_of_interest=[rekognition.CfnStreamProcessor.BoundingBoxProperty(
                    height=123,
                    left=123,
                    top=123,
                    width=123
                )],
                connected_home_settings=rekognition.CfnStreamProcessor.ConnectedHomeSettingsProperty(
                    labels=["labels"],
            
                    # the properties below are optional
                    min_confidence=123
                ),
                data_sharing_preference=rekognition.CfnStreamProcessor.DataSharingPreferenceProperty(
                    opt_in=False
                ),
                face_search_settings=rekognition.CfnStreamProcessor.FaceSearchSettingsProperty(
                    collection_id="collectionId",
            
                    # the properties below are optional
                    face_match_threshold=123
                ),
                kinesis_data_stream=rekognition.CfnStreamProcessor.KinesisDataStreamProperty(
                    arn="arn"
                ),
                kms_key_id="kmsKeyId",
                name="name",
                notification_channel=rekognition.CfnStreamProcessor.NotificationChannelProperty(
                    arn="arn"
                ),
                polygon_regions_of_interest=polygon_regions_of_interest,
                s3_destination=rekognition.CfnStreamProcessor.S3DestinationProperty(
                    bucket_name="bucketName",
            
                    # the properties below are optional
                    object_key_prefix="objectKeyPrefix"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c127c0832431498dadda03367902d22729b1e3b0a97f31a10822f1232161834)
            check_type(argname="argument kinesis_video_stream", value=kinesis_video_stream, expected_type=type_hints["kinesis_video_stream"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument bounding_box_regions_of_interest", value=bounding_box_regions_of_interest, expected_type=type_hints["bounding_box_regions_of_interest"])
            check_type(argname="argument connected_home_settings", value=connected_home_settings, expected_type=type_hints["connected_home_settings"])
            check_type(argname="argument data_sharing_preference", value=data_sharing_preference, expected_type=type_hints["data_sharing_preference"])
            check_type(argname="argument face_search_settings", value=face_search_settings, expected_type=type_hints["face_search_settings"])
            check_type(argname="argument kinesis_data_stream", value=kinesis_data_stream, expected_type=type_hints["kinesis_data_stream"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument notification_channel", value=notification_channel, expected_type=type_hints["notification_channel"])
            check_type(argname="argument polygon_regions_of_interest", value=polygon_regions_of_interest, expected_type=type_hints["polygon_regions_of_interest"])
            check_type(argname="argument s3_destination", value=s3_destination, expected_type=type_hints["s3_destination"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "kinesis_video_stream": kinesis_video_stream,
            "role_arn": role_arn,
        }
        if bounding_box_regions_of_interest is not None:
            self._values["bounding_box_regions_of_interest"] = bounding_box_regions_of_interest
        if connected_home_settings is not None:
            self._values["connected_home_settings"] = connected_home_settings
        if data_sharing_preference is not None:
            self._values["data_sharing_preference"] = data_sharing_preference
        if face_search_settings is not None:
            self._values["face_search_settings"] = face_search_settings
        if kinesis_data_stream is not None:
            self._values["kinesis_data_stream"] = kinesis_data_stream
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if name is not None:
            self._values["name"] = name
        if notification_channel is not None:
            self._values["notification_channel"] = notification_channel
        if polygon_regions_of_interest is not None:
            self._values["polygon_regions_of_interest"] = polygon_regions_of_interest
        if s3_destination is not None:
            self._values["s3_destination"] = s3_destination
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def kinesis_video_stream(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnStreamProcessor.KinesisVideoStreamProperty]:
        '''The Kinesis video stream that provides the source of the streaming video for an Amazon Rekognition Video stream processor.

        For more information, see `KinesisVideoStream <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_KinesisVideoStream>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-kinesisvideostream
        '''
        result = self._values.get("kinesis_video_stream")
        assert result is not None, "Required property 'kinesis_video_stream' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnStreamProcessor.KinesisVideoStreamProperty], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The ARN of the IAM role that allows access to the stream processor.

        The IAM role provides Rekognition read permissions to the Kinesis stream. It also provides write permissions to an Amazon S3 bucket and Amazon Simple Notification Service topic for a connected home stream processor. This is required for both face search and connected home stream processors. For information about constraints, see the RoleArn section of `CreateStreamProcessor <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bounding_box_regions_of_interest(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStreamProcessor.BoundingBoxProperty]]]]:
        '''List of BoundingBox objects, each of which denotes a region of interest on screen.

        For more information, see the BoundingBox field of `RegionOfInterest <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_RegionOfInterest>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-boundingboxregionsofinterest
        '''
        result = self._values.get("bounding_box_regions_of_interest")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStreamProcessor.BoundingBoxProperty]]]], result)

    @builtins.property
    def connected_home_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStreamProcessor.ConnectedHomeSettingsProperty]]:
        '''Connected home settings to use on a streaming video.

        You can use a stream processor for connected home features and select what you want the stream processor to detect, such as people or pets. When the stream processor has started, one notification is sent for each object class specified. For more information, see the ConnectedHome section of `StreamProcessorSettings <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessorSettings>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-connectedhomesettings
        '''
        result = self._values.get("connected_home_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStreamProcessor.ConnectedHomeSettingsProperty]], result)

    @builtins.property
    def data_sharing_preference(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStreamProcessor.DataSharingPreferenceProperty]]:
        '''Allows you to opt in or opt out to share data with Rekognition to improve model performance.

        You can choose this option at the account level or on a per-stream basis. Note that if you opt out at the account level this setting is ignored on individual streams. For more information, see `StreamProcessorDataSharingPreference <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessorDataSharingPreference>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-datasharingpreference
        '''
        result = self._values.get("data_sharing_preference")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStreamProcessor.DataSharingPreferenceProperty]], result)

    @builtins.property
    def face_search_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStreamProcessor.FaceSearchSettingsProperty]]:
        '''The input parameters used to recognize faces in a streaming video analyzed by an Amazon Rekognition stream processor.

        For more information regarding the contents of the parameters, see `FaceSearchSettings <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_FaceSearchSettings>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-facesearchsettings
        '''
        result = self._values.get("face_search_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStreamProcessor.FaceSearchSettingsProperty]], result)

    @builtins.property
    def kinesis_data_stream(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStreamProcessor.KinesisDataStreamProperty]]:
        '''Amazon Rekognition's Video Stream Processor takes a Kinesis video stream as input.

        This is the Amazon Kinesis Data Streams instance to which the Amazon Rekognition stream processor streams the analysis results. This must be created within the constraints specified at `KinesisDataStream <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_KinesisDataStream>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-kinesisdatastream
        '''
        result = self._values.get("kinesis_data_stream")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStreamProcessor.KinesisDataStreamProperty]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The identifier for your Amazon Key Management Service key (Amazon KMS key).

        Optional parameter for connected home stream processors used to encrypt results and data published to your Amazon S3 bucket. For more information, see the KMSKeyId section of `CreateStreamProcessor <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The Name attribute specifies the name of the stream processor and it must be within the constraints described in the Name section of `StreamProcessor <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessor>`_ . If you don't specify a name, Amazon CloudFormation generates a unique ID and uses that ID for the stream processor name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def notification_channel(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStreamProcessor.NotificationChannelProperty]]:
        '''The Amazon Simple Notification Service topic to which Amazon Rekognition publishes the object detection results and completion status of a video analysis operation.

        Amazon Rekognition publishes a notification the first time an object of interest or a person is detected in the video stream. Amazon Rekognition also publishes an end-of-session notification with a summary when the stream processing session is complete. For more information, see `StreamProcessorNotificationChannel <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessorNotificationChannel>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-notificationchannel
        '''
        result = self._values.get("notification_channel")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStreamProcessor.NotificationChannelProperty]], result)

    @builtins.property
    def polygon_regions_of_interest(self) -> typing.Any:
        '''A set of ordered lists of `Point <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_Point>`_ objects. Each entry of the set contains a polygon denoting a region of interest on the screen. Each polygon is an ordered list of `Point <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_Point>`_ objects. For more information, see the Polygon field of `RegionOfInterest <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_RegionOfInterest>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-polygonregionsofinterest
        '''
        result = self._values.get("polygon_regions_of_interest")
        return typing.cast(typing.Any, result)

    @builtins.property
    def s3_destination(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStreamProcessor.S3DestinationProperty]]:
        '''The Amazon S3 bucket location to which Amazon Rekognition publishes the detailed inference results of a video analysis operation.

        For more information, see the S3Destination section of `StreamProcessorOutput <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StreamProcessorOutput>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-s3destination
        '''
        result = self._values.get("s3_destination")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStreamProcessor.S3DestinationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A set of tags (key-value pairs) that you want to attach to the stream processor.

        For more information, see the Tags section of `CreateStreamProcessor <https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rekognition-streamprocessor.html#cfn-rekognition-streamprocessor-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStreamProcessorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCollection",
    "CfnCollectionProps",
    "CfnProject",
    "CfnProjectProps",
    "CfnStreamProcessor",
    "CfnStreamProcessorProps",
]

publication.publish()

def _typecheckingstub__001405b167561982ca01f91c85c5f23fd1bfd335896f67495614aef9fdc1ebbf(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    collection_id: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b782257f4d64c4abcb4d4415ba27cde118213945920a4b2608a0dc326e124dc(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef7614d7ac1ab1a1108a4489935df88c874c2a92a6ca3448ab8aba35c8c23d2e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8475d528ae41527da38a3e3ef20b3988703938f0440df9c74be2cd4234cdb6d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77f5ab15cea02999fa32036e3558af08ca21b17032d4915d2d3fc7c0c790bbbc(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfc582deefac2ef5bf0ca7c04ad06966543ece2be4f36ffdaa97fbaf33bfb064(
    *,
    collection_id: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14434bd621070d38889fc701fc289b3379981bee9c73fd7502773f1ee6007596(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    project_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0172e641847a31da5e6877581313d2ece51b9650bcb74b1b80ba13e563323cc0(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecd6c0ddb539c1c7c5df4ac80934172fad202067215980c77299274cd21f9555(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a1962fa2cac2e24ef346e8a95c9cce8b1cf9023aaeae155bf61e10c5dbddf83(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6ffefd83213c744dc48a7e730e4f4ba6abf92dfd04904ffa9f7361b3df6c6d3(
    *,
    project_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db29995773d1d6016b19ea60d9d43e43a080dc683708f8f6806c20b41de3b4e9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    kinesis_video_stream: typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamProcessor.KinesisVideoStreamProperty, typing.Dict[builtins.str, typing.Any]]],
    role_arn: builtins.str,
    bounding_box_regions_of_interest: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamProcessor.BoundingBoxProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    connected_home_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamProcessor.ConnectedHomeSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    data_sharing_preference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamProcessor.DataSharingPreferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    face_search_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamProcessor.FaceSearchSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kinesis_data_stream: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamProcessor.KinesisDataStreamProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    notification_channel: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamProcessor.NotificationChannelProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    polygon_regions_of_interest: typing.Any = None,
    s3_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamProcessor.S3DestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40ab64ef7968d6308fa66fa8cd30426d2afa22a69cd4c0add4fad58d1123b3d8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__682d423a7e9ce2fa6f2875579551bac52247181a6905c21784d80a153db8261e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__544bd519e8f2f595255e1dda00353bdad3a1f366808872e2a020ab7ac0c68ede(
    value: typing.Union[_IResolvable_da3f097b, CfnStreamProcessor.KinesisVideoStreamProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ceb033b416a9b50d7e1f7b205e95dc9fc9eeaa5ebe8b01d77b8db945e1617e5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acc75e18dc798eb00941485f051f88d386cbeab51667cb8be061da0b98c63396(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnStreamProcessor.BoundingBoxProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8917bfe75ce52160b79d51e35bc32988d0117df4b4c5c2fcc5738d3adcbff9b9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStreamProcessor.ConnectedHomeSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb32e5089c11a4939bd2e9bee353c9a78566e808db896e1c677dd43c12926ebd(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStreamProcessor.DataSharingPreferenceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__566df51893024802a690a50b28be352b9fc757428a22f708bee01096b284279f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStreamProcessor.FaceSearchSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__389631c246d3fdbe6ca66d4b9806147f81f4854193101c9c3341c10c3a06de51(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStreamProcessor.KinesisDataStreamProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9c6d353ba33bff601fce6ba9916bbea7fe2b890b0842c5ce26e962eb292dc57(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eea2935c2a6e509f6f9b8bac8defe6d3a7c700401c6d0e1fed5c595cc78a49a1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8781502f6d929597da76936c53e5a7d0df2ea7201c636dff5961d377bee07178(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStreamProcessor.NotificationChannelProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32adcb2805477bf062e3a38ebed38564ceb277accb2b42fac998c1b5ce354c54(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0366aae7f57073426925f9ebba0e5762ee7449ce53690b7fc2381679f27838c5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStreamProcessor.S3DestinationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a544bfd783dfe89e1f97d483f2cfa712d54a14e78538c5e39f6f4febe9970aeb(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7bad855b7d71ef59694b32449dc63de52f35f2ad462103fe21128c7c33206a1(
    *,
    height: jsii.Number,
    left: jsii.Number,
    top: jsii.Number,
    width: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__586438043baa3b2c31178aa9461612acb2d0d0ae0aac237b6e61cabac7e5de67(
    *,
    labels: typing.Sequence[builtins.str],
    min_confidence: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ebd03a0efbe12d5f07382e61ebfcb962dda51221996e196f2b8497594573d49(
    *,
    opt_in: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1d920a4a5c5227a1362117b6d7177bc83ca757ab3ddf859bfaea3e1bf2b2128(
    *,
    collection_id: builtins.str,
    face_match_threshold: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1a9643f21ce9cd202be0cc632d42c8de7c3bc2d1ec5dc6e2a56db210204aa04(
    *,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11c5113726b14e2f510aef1499acb05b38edb79b09083d31795eefd5f67eaf71(
    *,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf89b771464a553c692cbb9b3c1b09ca50ed7849163df9f19249032781e02e78(
    *,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e73e14e2930474187d1e5f6a0777aed81ad8438a2a23547a3ed5ca26b468afe6(
    *,
    x: jsii.Number,
    y: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e523487c02bfde11953c715444eddb9f2ed729eec0aa81767c2868bf914262ce(
    *,
    bucket_name: builtins.str,
    object_key_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c127c0832431498dadda03367902d22729b1e3b0a97f31a10822f1232161834(
    *,
    kinesis_video_stream: typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamProcessor.KinesisVideoStreamProperty, typing.Dict[builtins.str, typing.Any]]],
    role_arn: builtins.str,
    bounding_box_regions_of_interest: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamProcessor.BoundingBoxProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    connected_home_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamProcessor.ConnectedHomeSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    data_sharing_preference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamProcessor.DataSharingPreferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    face_search_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamProcessor.FaceSearchSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kinesis_data_stream: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamProcessor.KinesisDataStreamProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    notification_channel: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamProcessor.NotificationChannelProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    polygon_regions_of_interest: typing.Any = None,
    s3_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStreamProcessor.S3DestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
