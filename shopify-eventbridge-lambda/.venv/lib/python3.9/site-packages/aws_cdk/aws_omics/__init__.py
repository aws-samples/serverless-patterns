'''
# AWS::Omics Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_omics as omics
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Omics construct libraries](https://constructs.dev/search?q=omics)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Omics resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Omics.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Omics](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Omics.html).

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
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggable as _ITaggable_36806126,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnAnnotationStore(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_omics.CfnAnnotationStore",
):
    '''Creates an annotation store.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html
    :cloudformationResource: AWS::Omics::AnnotationStore
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_omics as omics
        
        # schema: Any
        
        cfn_annotation_store = omics.CfnAnnotationStore(self, "MyCfnAnnotationStore",
            name="name",
            store_format="storeFormat",
        
            # the properties below are optional
            description="description",
            reference=omics.CfnAnnotationStore.ReferenceItemProperty(
                reference_arn="referenceArn"
            ),
            sse_config=omics.CfnAnnotationStore.SseConfigProperty(
                type="type",
        
                # the properties below are optional
                key_arn="keyArn"
            ),
            store_options=omics.CfnAnnotationStore.StoreOptionsProperty(
                tsv_store_options=omics.CfnAnnotationStore.TsvStoreOptionsProperty(
                    annotation_type="annotationType",
                    format_to_header={
                        "format_to_header_key": "formatToHeader"
                    },
                    schema=schema
                )
            ),
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        store_format: builtins.str,
        description: typing.Optional[builtins.str] = None,
        reference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnnotationStore.ReferenceItemProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        sse_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnnotationStore.SseConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        store_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnnotationStore.StoreOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the Annotation Store.
        :param store_format: The annotation file format of the store.
        :param description: A description for the store.
        :param reference: The genome reference for the store's annotations.
        :param sse_config: The store's server-side encryption (SSE) settings.
        :param store_options: File parsing options for the annotation store.
        :param tags: Tags for the store.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba5dcb906702f10b4a247a16c504ec605912264b052a73f0ae664d93bee73764)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAnnotationStoreProps(
            name=name,
            store_format=store_format,
            description=description,
            reference=reference,
            sse_config=sse_config,
            store_options=store_options,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d66bbde88d332dceb0812bb6bbf08c2418490d8b0e9774a97971a3b895f48b8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aa50ba289bb96ea508cb6a4202ffc1689e383887b754b989d8350c1e79bdf41c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''When the store was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The store's ID.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The store's status.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusMessage")
    def attr_status_message(self) -> builtins.str:
        '''The store's status message.

        :cloudformationAttribute: StatusMessage
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusMessage"))

    @builtins.property
    @jsii.member(jsii_name="attrStoreArn")
    def attr_store_arn(self) -> builtins.str:
        '''The store's ARN.

        :cloudformationAttribute: StoreArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStoreArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStoreSizeBytes")
    def attr_store_size_bytes(self) -> _IResolvable_da3f097b:
        '''The store's size in bytes.

        :cloudformationAttribute: StoreSizeBytes
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrStoreSizeBytes"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdateTime")
    def attr_update_time(self) -> builtins.str:
        '''When the store was updated.

        :cloudformationAttribute: UpdateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdateTime"))

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
        '''The name of the Annotation Store.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d9b73e29df1d36e34609deddf6492296be4ec0e0c99ae60a05f9cab95febd6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="storeFormat")
    def store_format(self) -> builtins.str:
        '''The annotation file format of the store.'''
        return typing.cast(builtins.str, jsii.get(self, "storeFormat"))

    @store_format.setter
    def store_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39db05833c4ce77a84e366d7b58478b995b315232f05d9f9932602373f9c2c7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storeFormat", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the store.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bf53e865a22afeab85ecdb04fcf364678cf903b5624472147bf80f81f04730f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="reference")
    def reference(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnnotationStore.ReferenceItemProperty"]]:
        '''The genome reference for the store's annotations.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnnotationStore.ReferenceItemProperty"]], jsii.get(self, "reference"))

    @reference.setter
    def reference(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnnotationStore.ReferenceItemProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59c0d69a72a95b731117630b98efd8729539c64fef15303dab4addb9eae6ffa4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reference", value)

    @builtins.property
    @jsii.member(jsii_name="sseConfig")
    def sse_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnnotationStore.SseConfigProperty"]]:
        '''The store's server-side encryption (SSE) settings.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnnotationStore.SseConfigProperty"]], jsii.get(self, "sseConfig"))

    @sse_config.setter
    def sse_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnnotationStore.SseConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5edec3d71b0ff38cdce6ec8a872457ab8f95894314688d3b059e6b2fd20a3c07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sseConfig", value)

    @builtins.property
    @jsii.member(jsii_name="storeOptions")
    def store_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnnotationStore.StoreOptionsProperty"]]:
        '''File parsing options for the annotation store.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnnotationStore.StoreOptionsProperty"]], jsii.get(self, "storeOptions"))

    @store_options.setter
    def store_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAnnotationStore.StoreOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e84dfea35f835d11c086ac495c8e1952da55b4069d246ca2b527bb2a7655e94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storeOptions", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags for the store.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bd3f81b2e8f342de3db84fde3693c24cb6514a2f2b2e76534d5136fdc26945b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnAnnotationStore.ReferenceItemProperty",
        jsii_struct_bases=[],
        name_mapping={"reference_arn": "referenceArn"},
    )
    class ReferenceItemProperty:
        def __init__(self, *, reference_arn: builtins.str) -> None:
            '''A genome reference.

            :param reference_arn: The reference's ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-referenceitem.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                reference_item_property = omics.CfnAnnotationStore.ReferenceItemProperty(
                    reference_arn="referenceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f161bf0df41584a24622d738207d338081faec41cddac7f0cda31f0cbf50b695)
                check_type(argname="argument reference_arn", value=reference_arn, expected_type=type_hints["reference_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "reference_arn": reference_arn,
            }

        @builtins.property
        def reference_arn(self) -> builtins.str:
            '''The reference's ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-referenceitem.html#cfn-omics-annotationstore-referenceitem-referencearn
            '''
            result = self._values.get("reference_arn")
            assert result is not None, "Required property 'reference_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReferenceItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnAnnotationStore.SseConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "key_arn": "keyArn"},
    )
    class SseConfigProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Server-side encryption (SSE) settings for a store.

            :param type: The encryption type.
            :param key_arn: An encryption key ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-sseconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                sse_config_property = omics.CfnAnnotationStore.SseConfigProperty(
                    type="type",
                
                    # the properties below are optional
                    key_arn="keyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__30b0283b46d5b34e1109c108b303d6ab3e549e041b5482192ec0ef37b83e6920)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument key_arn", value=key_arn, expected_type=type_hints["key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if key_arn is not None:
                self._values["key_arn"] = key_arn

        @builtins.property
        def type(self) -> builtins.str:
            '''The encryption type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-sseconfig.html#cfn-omics-annotationstore-sseconfig-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_arn(self) -> typing.Optional[builtins.str]:
            '''An encryption key ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-sseconfig.html#cfn-omics-annotationstore-sseconfig-keyarn
            '''
            result = self._values.get("key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SseConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnAnnotationStore.StoreOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"tsv_store_options": "tsvStoreOptions"},
    )
    class StoreOptionsProperty:
        def __init__(
            self,
            *,
            tsv_store_options: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAnnotationStore.TsvStoreOptionsProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The store's file parsing options.

            :param tsv_store_options: Formatting options for a TSV file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-storeoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                # schema: Any
                
                store_options_property = omics.CfnAnnotationStore.StoreOptionsProperty(
                    tsv_store_options=omics.CfnAnnotationStore.TsvStoreOptionsProperty(
                        annotation_type="annotationType",
                        format_to_header={
                            "format_to_header_key": "formatToHeader"
                        },
                        schema=schema
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__68b9968e466757cfc2e4ee7eb053201b466a44d185aa6082edce78e859f4f489)
                check_type(argname="argument tsv_store_options", value=tsv_store_options, expected_type=type_hints["tsv_store_options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "tsv_store_options": tsv_store_options,
            }

        @builtins.property
        def tsv_store_options(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnAnnotationStore.TsvStoreOptionsProperty"]:
            '''Formatting options for a TSV file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-storeoptions.html#cfn-omics-annotationstore-storeoptions-tsvstoreoptions
            '''
            result = self._values.get("tsv_store_options")
            assert result is not None, "Required property 'tsv_store_options' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAnnotationStore.TsvStoreOptionsProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StoreOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnAnnotationStore.TsvStoreOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "annotation_type": "annotationType",
            "format_to_header": "formatToHeader",
            "schema": "schema",
        },
    )
    class TsvStoreOptionsProperty:
        def __init__(
            self,
            *,
            annotation_type: typing.Optional[builtins.str] = None,
            format_to_header: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            schema: typing.Any = None,
        ) -> None:
            '''The store's parsing options.

            :param annotation_type: The store's annotation type.
            :param format_to_header: The store's header key to column name mapping.
            :param schema: The schema of an annotation store.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-tsvstoreoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                # schema: Any
                
                tsv_store_options_property = omics.CfnAnnotationStore.TsvStoreOptionsProperty(
                    annotation_type="annotationType",
                    format_to_header={
                        "format_to_header_key": "formatToHeader"
                    },
                    schema=schema
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__14b0c73be5d34083c239713770a8134020bc8cab75d4b0a1a82a28463074bb3d)
                check_type(argname="argument annotation_type", value=annotation_type, expected_type=type_hints["annotation_type"])
                check_type(argname="argument format_to_header", value=format_to_header, expected_type=type_hints["format_to_header"])
                check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if annotation_type is not None:
                self._values["annotation_type"] = annotation_type
            if format_to_header is not None:
                self._values["format_to_header"] = format_to_header
            if schema is not None:
                self._values["schema"] = schema

        @builtins.property
        def annotation_type(self) -> typing.Optional[builtins.str]:
            '''The store's annotation type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-tsvstoreoptions.html#cfn-omics-annotationstore-tsvstoreoptions-annotationtype
            '''
            result = self._values.get("annotation_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def format_to_header(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''The store's header key to column name mapping.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-tsvstoreoptions.html#cfn-omics-annotationstore-tsvstoreoptions-formattoheader
            '''
            result = self._values.get("format_to_header")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def schema(self) -> typing.Any:
            '''The schema of an annotation store.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-tsvstoreoptions.html#cfn-omics-annotationstore-tsvstoreoptions-schema
            '''
            result = self._values.get("schema")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TsvStoreOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_omics.CfnAnnotationStoreProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "store_format": "storeFormat",
        "description": "description",
        "reference": "reference",
        "sse_config": "sseConfig",
        "store_options": "storeOptions",
        "tags": "tags",
    },
)
class CfnAnnotationStoreProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        store_format: builtins.str,
        description: typing.Optional[builtins.str] = None,
        reference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnnotationStore.ReferenceItemProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        sse_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnnotationStore.SseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        store_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnnotationStore.StoreOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAnnotationStore``.

        :param name: The name of the Annotation Store.
        :param store_format: The annotation file format of the store.
        :param description: A description for the store.
        :param reference: The genome reference for the store's annotations.
        :param sse_config: The store's server-side encryption (SSE) settings.
        :param store_options: File parsing options for the annotation store.
        :param tags: Tags for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_omics as omics
            
            # schema: Any
            
            cfn_annotation_store_props = omics.CfnAnnotationStoreProps(
                name="name",
                store_format="storeFormat",
            
                # the properties below are optional
                description="description",
                reference=omics.CfnAnnotationStore.ReferenceItemProperty(
                    reference_arn="referenceArn"
                ),
                sse_config=omics.CfnAnnotationStore.SseConfigProperty(
                    type="type",
            
                    # the properties below are optional
                    key_arn="keyArn"
                ),
                store_options=omics.CfnAnnotationStore.StoreOptionsProperty(
                    tsv_store_options=omics.CfnAnnotationStore.TsvStoreOptionsProperty(
                        annotation_type="annotationType",
                        format_to_header={
                            "format_to_header_key": "formatToHeader"
                        },
                        schema=schema
                    )
                ),
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db27a54e4b1e96ecf8263cf950eaa96b8620641082ddea726be734d30e205831)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument store_format", value=store_format, expected_type=type_hints["store_format"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument reference", value=reference, expected_type=type_hints["reference"])
            check_type(argname="argument sse_config", value=sse_config, expected_type=type_hints["sse_config"])
            check_type(argname="argument store_options", value=store_options, expected_type=type_hints["store_options"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "store_format": store_format,
        }
        if description is not None:
            self._values["description"] = description
        if reference is not None:
            self._values["reference"] = reference
        if sse_config is not None:
            self._values["sse_config"] = sse_config
        if store_options is not None:
            self._values["store_options"] = store_options
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the Annotation Store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html#cfn-omics-annotationstore-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def store_format(self) -> builtins.str:
        '''The annotation file format of the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html#cfn-omics-annotationstore-storeformat
        '''
        result = self._values.get("store_format")
        assert result is not None, "Required property 'store_format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html#cfn-omics-annotationstore-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reference(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnnotationStore.ReferenceItemProperty]]:
        '''The genome reference for the store's annotations.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html#cfn-omics-annotationstore-reference
        '''
        result = self._values.get("reference")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnnotationStore.ReferenceItemProperty]], result)

    @builtins.property
    def sse_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnnotationStore.SseConfigProperty]]:
        '''The store's server-side encryption (SSE) settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html#cfn-omics-annotationstore-sseconfig
        '''
        result = self._values.get("sse_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnnotationStore.SseConfigProperty]], result)

    @builtins.property
    def store_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnnotationStore.StoreOptionsProperty]]:
        '''File parsing options for the annotation store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html#cfn-omics-annotationstore-storeoptions
        '''
        result = self._values.get("store_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnnotationStore.StoreOptionsProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html#cfn-omics-annotationstore-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAnnotationStoreProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnReferenceStore(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_omics.CfnReferenceStore",
):
    '''Creates a reference store.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-referencestore.html
    :cloudformationResource: AWS::Omics::ReferenceStore
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_omics as omics
        
        cfn_reference_store = omics.CfnReferenceStore(self, "MyCfnReferenceStore",
            name="name",
        
            # the properties below are optional
            description="description",
            sse_config=omics.CfnReferenceStore.SseConfigProperty(
                type="type",
        
                # the properties below are optional
                key_arn="keyArn"
            ),
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        sse_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnReferenceStore.SseConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A name for the store.
        :param description: A description for the store.
        :param sse_config: Server-side encryption (SSE) settings for the store.
        :param tags: Tags for the store.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e38c503967033ff76d3e45880727cc62a1df749cb0aac8298f6d06d14d6e3320)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnReferenceStoreProps(
            name=name, description=description, sse_config=sse_config, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d75805be97b46dc8c38477db9eef63661d2478cb95cd31687daa2a21a351dfd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7a01b78cf451516a0eb2572826af339a051c95495f454b03b62693537679d6e9)
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
        '''The store's ARN.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''When the store was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrReferenceStoreId")
    def attr_reference_store_id(self) -> builtins.str:
        '''The store's ID.

        :cloudformationAttribute: ReferenceStoreId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrReferenceStoreId"))

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
        '''A name for the store.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42a1e17328f2c1518d508a235b2c42ef44e871bafb1772ad49e45f0b8d5583ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the store.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c89d0da98832090d35c5574aec7e23cd54990b36f1507999a687aed1e0a56bbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="sseConfig")
    def sse_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnReferenceStore.SseConfigProperty"]]:
        '''Server-side encryption (SSE) settings for the store.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnReferenceStore.SseConfigProperty"]], jsii.get(self, "sseConfig"))

    @sse_config.setter
    def sse_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnReferenceStore.SseConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63bf4a022de72dc8d560891710d6dee497173e638e81419fd5d8b3c20d9a650b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sseConfig", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags for the store.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5978dd78915de34b6caff418b41982c856f0f6071f77fc0f1306963a5cfe845e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnReferenceStore.SseConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "key_arn": "keyArn"},
    )
    class SseConfigProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Server-side encryption (SSE) settings for a store.

            :param type: The encryption type.
            :param key_arn: An encryption key ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-referencestore-sseconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                sse_config_property = omics.CfnReferenceStore.SseConfigProperty(
                    type="type",
                
                    # the properties below are optional
                    key_arn="keyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a277036a5a95a03f8b276d47ec8bcb3f25bf4f304bc5ee7452d8472c7e1ada3a)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument key_arn", value=key_arn, expected_type=type_hints["key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if key_arn is not None:
                self._values["key_arn"] = key_arn

        @builtins.property
        def type(self) -> builtins.str:
            '''The encryption type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-referencestore-sseconfig.html#cfn-omics-referencestore-sseconfig-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_arn(self) -> typing.Optional[builtins.str]:
            '''An encryption key ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-referencestore-sseconfig.html#cfn-omics-referencestore-sseconfig-keyarn
            '''
            result = self._values.get("key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SseConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_omics.CfnReferenceStoreProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "sse_config": "sseConfig",
        "tags": "tags",
    },
)
class CfnReferenceStoreProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        sse_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReferenceStore.SseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnReferenceStore``.

        :param name: A name for the store.
        :param description: A description for the store.
        :param sse_config: Server-side encryption (SSE) settings for the store.
        :param tags: Tags for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-referencestore.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_omics as omics
            
            cfn_reference_store_props = omics.CfnReferenceStoreProps(
                name="name",
            
                # the properties below are optional
                description="description",
                sse_config=omics.CfnReferenceStore.SseConfigProperty(
                    type="type",
            
                    # the properties below are optional
                    key_arn="keyArn"
                ),
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fa5ddefbb60b1902a7a8a0da56893c57cde7f27eb458a6b71907aad7ac2b4ca)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument sse_config", value=sse_config, expected_type=type_hints["sse_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if sse_config is not None:
            self._values["sse_config"] = sse_config
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-referencestore.html#cfn-omics-referencestore-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-referencestore.html#cfn-omics-referencestore-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sse_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnReferenceStore.SseConfigProperty]]:
        '''Server-side encryption (SSE) settings for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-referencestore.html#cfn-omics-referencestore-sseconfig
        '''
        result = self._values.get("sse_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnReferenceStore.SseConfigProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-referencestore.html#cfn-omics-referencestore-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReferenceStoreProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnRunGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_omics.CfnRunGroup",
):
    '''Creates a run group.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-rungroup.html
    :cloudformationResource: AWS::Omics::RunGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_omics as omics
        
        cfn_run_group = omics.CfnRunGroup(self, "MyCfnRunGroup",
            max_cpus=123,
            max_duration=123,
            max_gpus=123,
            max_runs=123,
            name="name",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        max_cpus: typing.Optional[jsii.Number] = None,
        max_duration: typing.Optional[jsii.Number] = None,
        max_gpus: typing.Optional[jsii.Number] = None,
        max_runs: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param max_cpus: The group's maximum CPU count setting.
        :param max_duration: The group's maximum duration setting in minutes.
        :param max_gpus: The maximum GPUs that can be used by a run group.
        :param max_runs: The group's maximum concurrent run setting.
        :param name: The group's name.
        :param tags: Tags for the group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d92bdf2175b79063decd2ff3bbf2745e423b61fa98f3bf6b832b7632771b7e8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRunGroupProps(
            max_cpus=max_cpus,
            max_duration=max_duration,
            max_gpus=max_gpus,
            max_runs=max_runs,
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
            type_hints = typing.get_type_hints(_typecheckingstub__34a9f76d09fa73ea3c0c86debaea039d1ecfeb5a751151276cc0002d8d2737c1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__61e5e671b78fea2bdc872b82befc94adc6014522a707589b79b6dc63795f14c0)
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
        '''The run group's ARN.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''When the run group was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The run group's ID.

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
    @jsii.member(jsii_name="maxCpus")
    def max_cpus(self) -> typing.Optional[jsii.Number]:
        '''The group's maximum CPU count setting.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxCpus"))

    @max_cpus.setter
    def max_cpus(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2024f9c040e790d1988694b9f616763247d6b00f2fdcd97552dbe2c3cae45b40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxCpus", value)

    @builtins.property
    @jsii.member(jsii_name="maxDuration")
    def max_duration(self) -> typing.Optional[jsii.Number]:
        '''The group's maximum duration setting in minutes.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxDuration"))

    @max_duration.setter
    def max_duration(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6aa9c45084b47d1e497a843bdc464ca31516a118303fa388c0f5db7b5bbd3630)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxDuration", value)

    @builtins.property
    @jsii.member(jsii_name="maxGpus")
    def max_gpus(self) -> typing.Optional[jsii.Number]:
        '''The maximum GPUs that can be used by a run group.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxGpus"))

    @max_gpus.setter
    def max_gpus(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1884be9d7a33f4597167d89c5fb81946a94d32f6879e4877ffa669c1ef0f4f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxGpus", value)

    @builtins.property
    @jsii.member(jsii_name="maxRuns")
    def max_runs(self) -> typing.Optional[jsii.Number]:
        '''The group's maximum concurrent run setting.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRuns"))

    @max_runs.setter
    def max_runs(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__235fda5a64dcc62cd14ad311c90dce78abbc930ce336e74e69a63f027c84b0c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRuns", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The group's name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14846c448c724a5e0421b3370cbf6d8071cc9d1d1f7f635d8b528b854c1db3a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags for the group.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f64a1ae8ed7c7141ee2c0e9f12df462d424e227637fb190daac9751a95f18d1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_omics.CfnRunGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "max_cpus": "maxCpus",
        "max_duration": "maxDuration",
        "max_gpus": "maxGpus",
        "max_runs": "maxRuns",
        "name": "name",
        "tags": "tags",
    },
)
class CfnRunGroupProps:
    def __init__(
        self,
        *,
        max_cpus: typing.Optional[jsii.Number] = None,
        max_duration: typing.Optional[jsii.Number] = None,
        max_gpus: typing.Optional[jsii.Number] = None,
        max_runs: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRunGroup``.

        :param max_cpus: The group's maximum CPU count setting.
        :param max_duration: The group's maximum duration setting in minutes.
        :param max_gpus: The maximum GPUs that can be used by a run group.
        :param max_runs: The group's maximum concurrent run setting.
        :param name: The group's name.
        :param tags: Tags for the group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-rungroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_omics as omics
            
            cfn_run_group_props = omics.CfnRunGroupProps(
                max_cpus=123,
                max_duration=123,
                max_gpus=123,
                max_runs=123,
                name="name",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0687d84f98238d006185c8fc00317ac96c5244d8d1b550e56fda04cb4eca97f9)
            check_type(argname="argument max_cpus", value=max_cpus, expected_type=type_hints["max_cpus"])
            check_type(argname="argument max_duration", value=max_duration, expected_type=type_hints["max_duration"])
            check_type(argname="argument max_gpus", value=max_gpus, expected_type=type_hints["max_gpus"])
            check_type(argname="argument max_runs", value=max_runs, expected_type=type_hints["max_runs"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if max_cpus is not None:
            self._values["max_cpus"] = max_cpus
        if max_duration is not None:
            self._values["max_duration"] = max_duration
        if max_gpus is not None:
            self._values["max_gpus"] = max_gpus
        if max_runs is not None:
            self._values["max_runs"] = max_runs
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def max_cpus(self) -> typing.Optional[jsii.Number]:
        '''The group's maximum CPU count setting.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-rungroup.html#cfn-omics-rungroup-maxcpus
        '''
        result = self._values.get("max_cpus")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_duration(self) -> typing.Optional[jsii.Number]:
        '''The group's maximum duration setting in minutes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-rungroup.html#cfn-omics-rungroup-maxduration
        '''
        result = self._values.get("max_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_gpus(self) -> typing.Optional[jsii.Number]:
        '''The maximum GPUs that can be used by a run group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-rungroup.html#cfn-omics-rungroup-maxgpus
        '''
        result = self._values.get("max_gpus")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_runs(self) -> typing.Optional[jsii.Number]:
        '''The group's maximum concurrent run setting.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-rungroup.html#cfn-omics-rungroup-maxruns
        '''
        result = self._values.get("max_runs")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The group's name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-rungroup.html#cfn-omics-rungroup-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags for the group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-rungroup.html#cfn-omics-rungroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRunGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnSequenceStore(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_omics.CfnSequenceStore",
):
    '''Creates a sequence store.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-sequencestore.html
    :cloudformationResource: AWS::Omics::SequenceStore
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_omics as omics
        
        cfn_sequence_store = omics.CfnSequenceStore(self, "MyCfnSequenceStore",
            name="name",
        
            # the properties below are optional
            description="description",
            fallback_location="fallbackLocation",
            sse_config=omics.CfnSequenceStore.SseConfigProperty(
                type="type",
        
                # the properties below are optional
                key_arn="keyArn"
            ),
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        fallback_location: typing.Optional[builtins.str] = None,
        sse_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSequenceStore.SseConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A name for the store.
        :param description: A description for the store.
        :param fallback_location: An S3 location that is used to store files that have failed a direct upload.
        :param sse_config: Server-side encryption (SSE) settings for the store.
        :param tags: Tags for the store.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a589aadb7c598845d5e4c6ef138fe8cbeb7253209ba9eb0e5e590611eec980dc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSequenceStoreProps(
            name=name,
            description=description,
            fallback_location=fallback_location,
            sse_config=sse_config,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea9a45fe9e84d5319386c1a777f6361e3fed5c916c543c8964323b54759ee470)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b7932486ef43d64891becc28acf4d1c7abdf6063eb9aa69d9bffa95c24d2d9d9)
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
        '''The store's ARN.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''When the store was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrSequenceStoreId")
    def attr_sequence_store_id(self) -> builtins.str:
        '''The store's ID.

        :cloudformationAttribute: SequenceStoreId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSequenceStoreId"))

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
        '''A name for the store.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8e53b0b20084e7e23dc393ceafe95167d7bce2ef95f48e5bca0556a29d78fa9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the store.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__128fafb1df9e961d7c5982e50a60c29fbada98403f437d20e8bab3669320ca5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="fallbackLocation")
    def fallback_location(self) -> typing.Optional[builtins.str]:
        '''An S3 location that is used to store files that have failed a direct upload.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fallbackLocation"))

    @fallback_location.setter
    def fallback_location(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f87faaa51a41810707e9283275d0283e54c3ebebf2803e01abef2984151aca1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fallbackLocation", value)

    @builtins.property
    @jsii.member(jsii_name="sseConfig")
    def sse_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSequenceStore.SseConfigProperty"]]:
        '''Server-side encryption (SSE) settings for the store.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSequenceStore.SseConfigProperty"]], jsii.get(self, "sseConfig"))

    @sse_config.setter
    def sse_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSequenceStore.SseConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92eed2332efa6d161a72ca8ae646e24cacee45f7acbbbb2e0aacb4b034c468be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sseConfig", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags for the store.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ce2c9ded7857e7f4d2115b4b17528bedb51685351fbcf322f7727f4fcf76354)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnSequenceStore.SseConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "key_arn": "keyArn"},
    )
    class SseConfigProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Server-side encryption (SSE) settings for a store.

            :param type: The encryption type.
            :param key_arn: An encryption key ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-sequencestore-sseconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                sse_config_property = omics.CfnSequenceStore.SseConfigProperty(
                    type="type",
                
                    # the properties below are optional
                    key_arn="keyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__16d14d56ac16dd0c8b7ee5046e40e324719a67cf46d9a70bdf176e614b6904fc)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument key_arn", value=key_arn, expected_type=type_hints["key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if key_arn is not None:
                self._values["key_arn"] = key_arn

        @builtins.property
        def type(self) -> builtins.str:
            '''The encryption type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-sequencestore-sseconfig.html#cfn-omics-sequencestore-sseconfig-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_arn(self) -> typing.Optional[builtins.str]:
            '''An encryption key ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-sequencestore-sseconfig.html#cfn-omics-sequencestore-sseconfig-keyarn
            '''
            result = self._values.get("key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SseConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_omics.CfnSequenceStoreProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "fallback_location": "fallbackLocation",
        "sse_config": "sseConfig",
        "tags": "tags",
    },
)
class CfnSequenceStoreProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        fallback_location: typing.Optional[builtins.str] = None,
        sse_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSequenceStore.SseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSequenceStore``.

        :param name: A name for the store.
        :param description: A description for the store.
        :param fallback_location: An S3 location that is used to store files that have failed a direct upload.
        :param sse_config: Server-side encryption (SSE) settings for the store.
        :param tags: Tags for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-sequencestore.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_omics as omics
            
            cfn_sequence_store_props = omics.CfnSequenceStoreProps(
                name="name",
            
                # the properties below are optional
                description="description",
                fallback_location="fallbackLocation",
                sse_config=omics.CfnSequenceStore.SseConfigProperty(
                    type="type",
            
                    # the properties below are optional
                    key_arn="keyArn"
                ),
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c912afa5be2bea750b085186b08f53bd688bc0a1dd08b1f1c6951a21015380fc)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument fallback_location", value=fallback_location, expected_type=type_hints["fallback_location"])
            check_type(argname="argument sse_config", value=sse_config, expected_type=type_hints["sse_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if fallback_location is not None:
            self._values["fallback_location"] = fallback_location
        if sse_config is not None:
            self._values["sse_config"] = sse_config
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-sequencestore.html#cfn-omics-sequencestore-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-sequencestore.html#cfn-omics-sequencestore-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fallback_location(self) -> typing.Optional[builtins.str]:
        '''An S3 location that is used to store files that have failed a direct upload.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-sequencestore.html#cfn-omics-sequencestore-fallbacklocation
        '''
        result = self._values.get("fallback_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sse_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSequenceStore.SseConfigProperty]]:
        '''Server-side encryption (SSE) settings for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-sequencestore.html#cfn-omics-sequencestore-sseconfig
        '''
        result = self._values.get("sse_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSequenceStore.SseConfigProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-sequencestore.html#cfn-omics-sequencestore-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSequenceStoreProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnVariantStore(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_omics.CfnVariantStore",
):
    '''Create a store for variant data.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-variantstore.html
    :cloudformationResource: AWS::Omics::VariantStore
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_omics as omics
        
        cfn_variant_store = omics.CfnVariantStore(self, "MyCfnVariantStore",
            name="name",
            reference=omics.CfnVariantStore.ReferenceItemProperty(
                reference_arn="referenceArn"
            ),
        
            # the properties below are optional
            description="description",
            sse_config=omics.CfnVariantStore.SseConfigProperty(
                type="type",
        
                # the properties below are optional
                key_arn="keyArn"
            ),
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        reference: typing.Union[_IResolvable_da3f097b, typing.Union["CfnVariantStore.ReferenceItemProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        sse_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnVariantStore.SseConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A name for the store.
        :param reference: The genome reference for the store's variants.
        :param description: A description for the store.
        :param sse_config: Server-side encryption (SSE) settings for the store.
        :param tags: Tags for the store.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d38872c12590b13122bc23c110efd40d1aa8369a37e1015fcc0ee2529e01904)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVariantStoreProps(
            name=name,
            reference=reference,
            description=description,
            sse_config=sse_config,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ca6bc97e153eee8b1d732a90be1690a35fffe864b7b05aaaac9e52711640fed)
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
            type_hints = typing.get_type_hints(_typecheckingstub__570cd7098cbc0f8a1520e467e899d1d2ec7d6bc45da494a51344b868369142a6)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''When the store was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The store's ID.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The store's status.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusMessage")
    def attr_status_message(self) -> builtins.str:
        '''The store's status message.

        :cloudformationAttribute: StatusMessage
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusMessage"))

    @builtins.property
    @jsii.member(jsii_name="attrStoreArn")
    def attr_store_arn(self) -> builtins.str:
        '''The store's ARN.

        :cloudformationAttribute: StoreArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStoreArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStoreSizeBytes")
    def attr_store_size_bytes(self) -> _IResolvable_da3f097b:
        '''The store's size in bytes.

        :cloudformationAttribute: StoreSizeBytes
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrStoreSizeBytes"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdateTime")
    def attr_update_time(self) -> builtins.str:
        '''When the store was updated.

        :cloudformationAttribute: UpdateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdateTime"))

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
        '''A name for the store.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a7151068f14ce10b8b0f9147b1e5b5afd6f6b7308067934acd8af16a512c243)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="reference")
    def reference(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnVariantStore.ReferenceItemProperty"]:
        '''The genome reference for the store's variants.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnVariantStore.ReferenceItemProperty"], jsii.get(self, "reference"))

    @reference.setter
    def reference(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnVariantStore.ReferenceItemProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__088cb3f651ad7a064e751c97def87bcf2e6e4149c7bcf54b57474d4b8b7d1b6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reference", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the store.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b58e2ea0e9ae60ac9a3dd7935556c2d0e2dfe3ff2de0f2ef79c50a0f2cdc07d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="sseConfig")
    def sse_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnVariantStore.SseConfigProperty"]]:
        '''Server-side encryption (SSE) settings for the store.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnVariantStore.SseConfigProperty"]], jsii.get(self, "sseConfig"))

    @sse_config.setter
    def sse_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnVariantStore.SseConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14ca86abdbf91bcd47e50c693a441fd60292ffbe1b4f732e112498a42712d29e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sseConfig", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags for the store.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58acd4facff447c8ba521704b60e2e575ce07cca5086f7089300382b0d72deb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnVariantStore.ReferenceItemProperty",
        jsii_struct_bases=[],
        name_mapping={"reference_arn": "referenceArn"},
    )
    class ReferenceItemProperty:
        def __init__(self, *, reference_arn: builtins.str) -> None:
            '''The read set's genome reference ARN.

            :param reference_arn: The reference's ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-variantstore-referenceitem.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                reference_item_property = omics.CfnVariantStore.ReferenceItemProperty(
                    reference_arn="referenceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9d03f1b71084719c634c1eec42eaa49cce433fd4e222652c52e9ca9afca86c44)
                check_type(argname="argument reference_arn", value=reference_arn, expected_type=type_hints["reference_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "reference_arn": reference_arn,
            }

        @builtins.property
        def reference_arn(self) -> builtins.str:
            '''The reference's ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-variantstore-referenceitem.html#cfn-omics-variantstore-referenceitem-referencearn
            '''
            result = self._values.get("reference_arn")
            assert result is not None, "Required property 'reference_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReferenceItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnVariantStore.SseConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "key_arn": "keyArn"},
    )
    class SseConfigProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Server-side encryption (SSE) settings for a store.

            :param type: The encryption type.
            :param key_arn: An encryption key ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-variantstore-sseconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                sse_config_property = omics.CfnVariantStore.SseConfigProperty(
                    type="type",
                
                    # the properties below are optional
                    key_arn="keyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__151f006e709dbecd4ae7c2469b6d65397d70b22812c239977c3f339440eefaf8)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument key_arn", value=key_arn, expected_type=type_hints["key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if key_arn is not None:
                self._values["key_arn"] = key_arn

        @builtins.property
        def type(self) -> builtins.str:
            '''The encryption type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-variantstore-sseconfig.html#cfn-omics-variantstore-sseconfig-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_arn(self) -> typing.Optional[builtins.str]:
            '''An encryption key ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-variantstore-sseconfig.html#cfn-omics-variantstore-sseconfig-keyarn
            '''
            result = self._values.get("key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SseConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_omics.CfnVariantStoreProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "reference": "reference",
        "description": "description",
        "sse_config": "sseConfig",
        "tags": "tags",
    },
)
class CfnVariantStoreProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        reference: typing.Union[_IResolvable_da3f097b, typing.Union[CfnVariantStore.ReferenceItemProperty, typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        sse_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnVariantStore.SseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnVariantStore``.

        :param name: A name for the store.
        :param reference: The genome reference for the store's variants.
        :param description: A description for the store.
        :param sse_config: Server-side encryption (SSE) settings for the store.
        :param tags: Tags for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-variantstore.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_omics as omics
            
            cfn_variant_store_props = omics.CfnVariantStoreProps(
                name="name",
                reference=omics.CfnVariantStore.ReferenceItemProperty(
                    reference_arn="referenceArn"
                ),
            
                # the properties below are optional
                description="description",
                sse_config=omics.CfnVariantStore.SseConfigProperty(
                    type="type",
            
                    # the properties below are optional
                    key_arn="keyArn"
                ),
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cee3839b5919ab156aab54490277c559d790311fd9ea2b761f99373fdb7eaec)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument reference", value=reference, expected_type=type_hints["reference"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument sse_config", value=sse_config, expected_type=type_hints["sse_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "reference": reference,
        }
        if description is not None:
            self._values["description"] = description
        if sse_config is not None:
            self._values["sse_config"] = sse_config
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-variantstore.html#cfn-omics-variantstore-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def reference(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnVariantStore.ReferenceItemProperty]:
        '''The genome reference for the store's variants.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-variantstore.html#cfn-omics-variantstore-reference
        '''
        result = self._values.get("reference")
        assert result is not None, "Required property 'reference' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnVariantStore.ReferenceItemProperty], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-variantstore.html#cfn-omics-variantstore-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sse_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnVariantStore.SseConfigProperty]]:
        '''Server-side encryption (SSE) settings for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-variantstore.html#cfn-omics-variantstore-sseconfig
        '''
        result = self._values.get("sse_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnVariantStore.SseConfigProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-variantstore.html#cfn-omics-variantstore-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVariantStoreProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnWorkflow(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_omics.CfnWorkflow",
):
    '''Creates a workflow.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html
    :cloudformationResource: AWS::Omics::Workflow
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_omics as omics
        
        cfn_workflow = omics.CfnWorkflow(self, "MyCfnWorkflow",
            accelerators="accelerators",
            definition_uri="definitionUri",
            description="description",
            engine="engine",
            main="main",
            name="name",
            parameter_template={
                "parameter_template_key": omics.CfnWorkflow.WorkflowParameterProperty(
                    description="description",
                    optional=False
                )
            },
            storage_capacity=123,
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        accelerators: typing.Optional[builtins.str] = None,
        definition_uri: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        engine: typing.Optional[builtins.str] = None,
        main: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        parameter_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkflow.WorkflowParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        storage_capacity: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param accelerators: 
        :param definition_uri: The URI of a definition for the workflow.
        :param description: The parameter's description.
        :param engine: An engine for the workflow.
        :param main: The path of the main definition file for the workflow.
        :param name: The workflow's name.
        :param parameter_template: The workflow's parameter template.
        :param storage_capacity: The default storage capacity for the workflow runs, in gibibytes.
        :param tags: Tags for the workflow.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2d05cb293836959a925b22dbe1861bc4457d2d510bd3a480ae858ea9f00850d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWorkflowProps(
            accelerators=accelerators,
            definition_uri=definition_uri,
            description=description,
            engine=engine,
            main=main,
            name=name,
            parameter_template=parameter_template,
            storage_capacity=storage_capacity,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98655701238267dcfc2598ca58d2fdf3b94be0fdd6d36c6407b8c9216e530168)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f3d18757469eec460375791b428b2b2a8ebd5be703fbc705cb706233f42a0050)
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
        '''The ARN for the workflow.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''When the workflow was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The workflow's ID.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The workflow's status.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''The workflow's type.

        :cloudformationAttribute: Type
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

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
    @jsii.member(jsii_name="accelerators")
    def accelerators(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accelerators"))

    @accelerators.setter
    def accelerators(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__286f71b00d1993ebc792c6e260606dac95cf17ec599b45b4cb2111b4ca57a0fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accelerators", value)

    @builtins.property
    @jsii.member(jsii_name="definitionUri")
    def definition_uri(self) -> typing.Optional[builtins.str]:
        '''The URI of a definition for the workflow.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "definitionUri"))

    @definition_uri.setter
    def definition_uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc102140c3b77bda25eda4edac3ddf245628b20791c9053f2a901ded02c9b780)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definitionUri", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The parameter's description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73c565083430765eb26563b0a57061f931b2ec1240d0b6c03b6bdad1003055c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="engine")
    def engine(self) -> typing.Optional[builtins.str]:
        '''An engine for the workflow.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engine"))

    @engine.setter
    def engine(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2edee5dfbe37830cd0e2e70344c7e33e9cf08c5c243438272da4a5634eae529f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engine", value)

    @builtins.property
    @jsii.member(jsii_name="main")
    def main(self) -> typing.Optional[builtins.str]:
        '''The path of the main definition file for the workflow.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "main"))

    @main.setter
    def main(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f791067dcd2f7a992bf37cf0c6c81e381b2e0344e60cf85051d19bb08c69bf13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "main", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The workflow's name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6845f053d191fb8caa10b651afe2128f50703f821981813813ed0bb9862dad7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameterTemplate")
    def parameter_template(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnWorkflow.WorkflowParameterProperty"]]]]:
        '''The workflow's parameter template.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnWorkflow.WorkflowParameterProperty"]]]], jsii.get(self, "parameterTemplate"))

    @parameter_template.setter
    def parameter_template(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnWorkflow.WorkflowParameterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd71f853b8475a5b472d76bce0cd20afc1269357412bdaa83e29ea355af8f64b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="storageCapacity")
    def storage_capacity(self) -> typing.Optional[jsii.Number]:
        '''The default storage capacity for the workflow runs, in gibibytes.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "storageCapacity"))

    @storage_capacity.setter
    def storage_capacity(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37c3d929054386cb4ebdbc60c2c3558d7cd34bed65861db5661f96d5d75ce7df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags for the workflow.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__651d8f1caf8b2c987665acfeae50e19a5626bb723832dae7067c423aab3ac2b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnWorkflow.WorkflowParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"description": "description", "optional": "optional"},
    )
    class WorkflowParameterProperty:
        def __init__(
            self,
            *,
            description: typing.Optional[builtins.str] = None,
            optional: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''A workflow parameter.

            :param description: The parameter's description.
            :param optional: Whether the parameter is optional.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-workflowparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                workflow_parameter_property = omics.CfnWorkflow.WorkflowParameterProperty(
                    description="description",
                    optional=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__beb0e924d2102ff644fd2da920cdd60f013b66e8285db8ffc0ce774a694580a5)
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument optional", value=optional, expected_type=type_hints["optional"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if description is not None:
                self._values["description"] = description
            if optional is not None:
                self._values["optional"] = optional

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The parameter's description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-workflowparameter.html#cfn-omics-workflow-workflowparameter-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def optional(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Whether the parameter is optional.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-workflowparameter.html#cfn-omics-workflow-workflowparameter-optional
            '''
            result = self._values.get("optional")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkflowParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_omics.CfnWorkflowProps",
    jsii_struct_bases=[],
    name_mapping={
        "accelerators": "accelerators",
        "definition_uri": "definitionUri",
        "description": "description",
        "engine": "engine",
        "main": "main",
        "name": "name",
        "parameter_template": "parameterTemplate",
        "storage_capacity": "storageCapacity",
        "tags": "tags",
    },
)
class CfnWorkflowProps:
    def __init__(
        self,
        *,
        accelerators: typing.Optional[builtins.str] = None,
        definition_uri: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        engine: typing.Optional[builtins.str] = None,
        main: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        parameter_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.WorkflowParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        storage_capacity: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnWorkflow``.

        :param accelerators: 
        :param definition_uri: The URI of a definition for the workflow.
        :param description: The parameter's description.
        :param engine: An engine for the workflow.
        :param main: The path of the main definition file for the workflow.
        :param name: The workflow's name.
        :param parameter_template: The workflow's parameter template.
        :param storage_capacity: The default storage capacity for the workflow runs, in gibibytes.
        :param tags: Tags for the workflow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_omics as omics
            
            cfn_workflow_props = omics.CfnWorkflowProps(
                accelerators="accelerators",
                definition_uri="definitionUri",
                description="description",
                engine="engine",
                main="main",
                name="name",
                parameter_template={
                    "parameter_template_key": omics.CfnWorkflow.WorkflowParameterProperty(
                        description="description",
                        optional=False
                    )
                },
                storage_capacity=123,
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09bedca50200dd06a4bbe4bb6135e76dacff76287249f3d28b8f285f8205f173)
            check_type(argname="argument accelerators", value=accelerators, expected_type=type_hints["accelerators"])
            check_type(argname="argument definition_uri", value=definition_uri, expected_type=type_hints["definition_uri"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument engine", value=engine, expected_type=type_hints["engine"])
            check_type(argname="argument main", value=main, expected_type=type_hints["main"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parameter_template", value=parameter_template, expected_type=type_hints["parameter_template"])
            check_type(argname="argument storage_capacity", value=storage_capacity, expected_type=type_hints["storage_capacity"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if accelerators is not None:
            self._values["accelerators"] = accelerators
        if definition_uri is not None:
            self._values["definition_uri"] = definition_uri
        if description is not None:
            self._values["description"] = description
        if engine is not None:
            self._values["engine"] = engine
        if main is not None:
            self._values["main"] = main
        if name is not None:
            self._values["name"] = name
        if parameter_template is not None:
            self._values["parameter_template"] = parameter_template
        if storage_capacity is not None:
            self._values["storage_capacity"] = storage_capacity
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def accelerators(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-accelerators
        '''
        result = self._values.get("accelerators")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def definition_uri(self) -> typing.Optional[builtins.str]:
        '''The URI of a definition for the workflow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-definitionuri
        '''
        result = self._values.get("definition_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The parameter's description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine(self) -> typing.Optional[builtins.str]:
        '''An engine for the workflow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-engine
        '''
        result = self._values.get("engine")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def main(self) -> typing.Optional[builtins.str]:
        '''The path of the main definition file for the workflow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-main
        '''
        result = self._values.get("main")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The workflow's name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_template(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnWorkflow.WorkflowParameterProperty]]]]:
        '''The workflow's parameter template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-parametertemplate
        '''
        result = self._values.get("parameter_template")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnWorkflow.WorkflowParameterProperty]]]], result)

    @builtins.property
    def storage_capacity(self) -> typing.Optional[jsii.Number]:
        '''The default storage capacity for the workflow runs, in gibibytes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-storagecapacity
        '''
        result = self._values.get("storage_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags for the workflow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkflowProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAnnotationStore",
    "CfnAnnotationStoreProps",
    "CfnReferenceStore",
    "CfnReferenceStoreProps",
    "CfnRunGroup",
    "CfnRunGroupProps",
    "CfnSequenceStore",
    "CfnSequenceStoreProps",
    "CfnVariantStore",
    "CfnVariantStoreProps",
    "CfnWorkflow",
    "CfnWorkflowProps",
]

publication.publish()

def _typecheckingstub__ba5dcb906702f10b4a247a16c504ec605912264b052a73f0ae664d93bee73764(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    store_format: builtins.str,
    description: typing.Optional[builtins.str] = None,
    reference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnnotationStore.ReferenceItemProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sse_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnnotationStore.SseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    store_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnnotationStore.StoreOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d66bbde88d332dceb0812bb6bbf08c2418490d8b0e9774a97971a3b895f48b8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa50ba289bb96ea508cb6a4202ffc1689e383887b754b989d8350c1e79bdf41c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d9b73e29df1d36e34609deddf6492296be4ec0e0c99ae60a05f9cab95febd6e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39db05833c4ce77a84e366d7b58478b995b315232f05d9f9932602373f9c2c7f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bf53e865a22afeab85ecdb04fcf364678cf903b5624472147bf80f81f04730f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59c0d69a72a95b731117630b98efd8729539c64fef15303dab4addb9eae6ffa4(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnnotationStore.ReferenceItemProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5edec3d71b0ff38cdce6ec8a872457ab8f95894314688d3b059e6b2fd20a3c07(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnnotationStore.SseConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e84dfea35f835d11c086ac495c8e1952da55b4069d246ca2b527bb2a7655e94(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnnotationStore.StoreOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bd3f81b2e8f342de3db84fde3693c24cb6514a2f2b2e76534d5136fdc26945b(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f161bf0df41584a24622d738207d338081faec41cddac7f0cda31f0cbf50b695(
    *,
    reference_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30b0283b46d5b34e1109c108b303d6ab3e549e041b5482192ec0ef37b83e6920(
    *,
    type: builtins.str,
    key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68b9968e466757cfc2e4ee7eb053201b466a44d185aa6082edce78e859f4f489(
    *,
    tsv_store_options: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnnotationStore.TsvStoreOptionsProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14b0c73be5d34083c239713770a8134020bc8cab75d4b0a1a82a28463074bb3d(
    *,
    annotation_type: typing.Optional[builtins.str] = None,
    format_to_header: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    schema: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db27a54e4b1e96ecf8263cf950eaa96b8620641082ddea726be734d30e205831(
    *,
    name: builtins.str,
    store_format: builtins.str,
    description: typing.Optional[builtins.str] = None,
    reference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnnotationStore.ReferenceItemProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sse_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnnotationStore.SseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    store_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnnotationStore.StoreOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e38c503967033ff76d3e45880727cc62a1df749cb0aac8298f6d06d14d6e3320(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    sse_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReferenceStore.SseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d75805be97b46dc8c38477db9eef63661d2478cb95cd31687daa2a21a351dfd(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a01b78cf451516a0eb2572826af339a051c95495f454b03b62693537679d6e9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42a1e17328f2c1518d508a235b2c42ef44e871bafb1772ad49e45f0b8d5583ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c89d0da98832090d35c5574aec7e23cd54990b36f1507999a687aed1e0a56bbb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63bf4a022de72dc8d560891710d6dee497173e638e81419fd5d8b3c20d9a650b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnReferenceStore.SseConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5978dd78915de34b6caff418b41982c856f0f6071f77fc0f1306963a5cfe845e(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a277036a5a95a03f8b276d47ec8bcb3f25bf4f304bc5ee7452d8472c7e1ada3a(
    *,
    type: builtins.str,
    key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fa5ddefbb60b1902a7a8a0da56893c57cde7f27eb458a6b71907aad7ac2b4ca(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    sse_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReferenceStore.SseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d92bdf2175b79063decd2ff3bbf2745e423b61fa98f3bf6b832b7632771b7e8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    max_cpus: typing.Optional[jsii.Number] = None,
    max_duration: typing.Optional[jsii.Number] = None,
    max_gpus: typing.Optional[jsii.Number] = None,
    max_runs: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34a9f76d09fa73ea3c0c86debaea039d1ecfeb5a751151276cc0002d8d2737c1(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61e5e671b78fea2bdc872b82befc94adc6014522a707589b79b6dc63795f14c0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2024f9c040e790d1988694b9f616763247d6b00f2fdcd97552dbe2c3cae45b40(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6aa9c45084b47d1e497a843bdc464ca31516a118303fa388c0f5db7b5bbd3630(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1884be9d7a33f4597167d89c5fb81946a94d32f6879e4877ffa669c1ef0f4f7(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__235fda5a64dcc62cd14ad311c90dce78abbc930ce336e74e69a63f027c84b0c0(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14846c448c724a5e0421b3370cbf6d8071cc9d1d1f7f635d8b528b854c1db3a1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f64a1ae8ed7c7141ee2c0e9f12df462d424e227637fb190daac9751a95f18d1a(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0687d84f98238d006185c8fc00317ac96c5244d8d1b550e56fda04cb4eca97f9(
    *,
    max_cpus: typing.Optional[jsii.Number] = None,
    max_duration: typing.Optional[jsii.Number] = None,
    max_gpus: typing.Optional[jsii.Number] = None,
    max_runs: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a589aadb7c598845d5e4c6ef138fe8cbeb7253209ba9eb0e5e590611eec980dc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    fallback_location: typing.Optional[builtins.str] = None,
    sse_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSequenceStore.SseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea9a45fe9e84d5319386c1a777f6361e3fed5c916c543c8964323b54759ee470(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7932486ef43d64891becc28acf4d1c7abdf6063eb9aa69d9bffa95c24d2d9d9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8e53b0b20084e7e23dc393ceafe95167d7bce2ef95f48e5bca0556a29d78fa9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__128fafb1df9e961d7c5982e50a60c29fbada98403f437d20e8bab3669320ca5c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f87faaa51a41810707e9283275d0283e54c3ebebf2803e01abef2984151aca1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92eed2332efa6d161a72ca8ae646e24cacee45f7acbbbb2e0aacb4b034c468be(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSequenceStore.SseConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ce2c9ded7857e7f4d2115b4b17528bedb51685351fbcf322f7727f4fcf76354(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16d14d56ac16dd0c8b7ee5046e40e324719a67cf46d9a70bdf176e614b6904fc(
    *,
    type: builtins.str,
    key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c912afa5be2bea750b085186b08f53bd688bc0a1dd08b1f1c6951a21015380fc(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    fallback_location: typing.Optional[builtins.str] = None,
    sse_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSequenceStore.SseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d38872c12590b13122bc23c110efd40d1aa8369a37e1015fcc0ee2529e01904(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    reference: typing.Union[_IResolvable_da3f097b, typing.Union[CfnVariantStore.ReferenceItemProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    sse_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnVariantStore.SseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ca6bc97e153eee8b1d732a90be1690a35fffe864b7b05aaaac9e52711640fed(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__570cd7098cbc0f8a1520e467e899d1d2ec7d6bc45da494a51344b868369142a6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a7151068f14ce10b8b0f9147b1e5b5afd6f6b7308067934acd8af16a512c243(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__088cb3f651ad7a064e751c97def87bcf2e6e4149c7bcf54b57474d4b8b7d1b6d(
    value: typing.Union[_IResolvable_da3f097b, CfnVariantStore.ReferenceItemProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b58e2ea0e9ae60ac9a3dd7935556c2d0e2dfe3ff2de0f2ef79c50a0f2cdc07d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14ca86abdbf91bcd47e50c693a441fd60292ffbe1b4f732e112498a42712d29e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnVariantStore.SseConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58acd4facff447c8ba521704b60e2e575ce07cca5086f7089300382b0d72deb1(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d03f1b71084719c634c1eec42eaa49cce433fd4e222652c52e9ca9afca86c44(
    *,
    reference_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__151f006e709dbecd4ae7c2469b6d65397d70b22812c239977c3f339440eefaf8(
    *,
    type: builtins.str,
    key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cee3839b5919ab156aab54490277c559d790311fd9ea2b761f99373fdb7eaec(
    *,
    name: builtins.str,
    reference: typing.Union[_IResolvable_da3f097b, typing.Union[CfnVariantStore.ReferenceItemProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    sse_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnVariantStore.SseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2d05cb293836959a925b22dbe1861bc4457d2d510bd3a480ae858ea9f00850d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    accelerators: typing.Optional[builtins.str] = None,
    definition_uri: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    engine: typing.Optional[builtins.str] = None,
    main: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    parameter_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.WorkflowParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    storage_capacity: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98655701238267dcfc2598ca58d2fdf3b94be0fdd6d36c6407b8c9216e530168(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3d18757469eec460375791b428b2b2a8ebd5be703fbc705cb706233f42a0050(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__286f71b00d1993ebc792c6e260606dac95cf17ec599b45b4cb2111b4ca57a0fe(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc102140c3b77bda25eda4edac3ddf245628b20791c9053f2a901ded02c9b780(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73c565083430765eb26563b0a57061f931b2ec1240d0b6c03b6bdad1003055c2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2edee5dfbe37830cd0e2e70344c7e33e9cf08c5c243438272da4a5634eae529f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f791067dcd2f7a992bf37cf0c6c81e381b2e0344e60cf85051d19bb08c69bf13(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6845f053d191fb8caa10b651afe2128f50703f821981813813ed0bb9862dad7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd71f853b8475a5b472d76bce0cd20afc1269357412bdaa83e29ea355af8f64b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnWorkflow.WorkflowParameterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37c3d929054386cb4ebdbc60c2c3558d7cd34bed65861db5661f96d5d75ce7df(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__651d8f1caf8b2c987665acfeae50e19a5626bb723832dae7067c423aab3ac2b5(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beb0e924d2102ff644fd2da920cdd60f013b66e8285db8ffc0ce774a694580a5(
    *,
    description: typing.Optional[builtins.str] = None,
    optional: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09bedca50200dd06a4bbe4bb6135e76dacff76287249f3d28b8f285f8205f173(
    *,
    accelerators: typing.Optional[builtins.str] = None,
    definition_uri: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    engine: typing.Optional[builtins.str] = None,
    main: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    parameter_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.WorkflowParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    storage_capacity: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
