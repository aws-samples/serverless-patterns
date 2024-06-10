'''
# AWS::ImageBuilder Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_imagebuilder as imagebuilder
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ImageBuilder construct libraries](https://constructs.dev/search?q=imagebuilder)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::ImageBuilder resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ImageBuilder.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::ImageBuilder](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ImageBuilder.html).

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
class CfnComponent(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_imagebuilder.CfnComponent",
):
    '''Creates a new component that can be used to build, validate, test, and assess your image.

    The component is based on a YAML document that you specify using exactly one of the following methods:

    - Inline, using the ``data`` property in the request body.
    - A URL that points to a YAML document file stored in Amazon S3, using the ``uri`` property in the request body.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html
    :cloudformationResource: AWS::ImageBuilder::Component
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_imagebuilder as imagebuilder
        
        cfn_component = imagebuilder.CfnComponent(self, "MyCfnComponent",
            name="name",
            platform="platform",
            version="version",
        
            # the properties below are optional
            change_description="changeDescription",
            data="data",
            description="description",
            kms_key_id="kmsKeyId",
            supported_os_versions=["supportedOsVersions"],
            tags={
                "tags_key": "tags"
            },
            uri="uri"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        platform: builtins.str,
        version: builtins.str,
        change_description: typing.Optional[builtins.str] = None,
        data: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        supported_os_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the component.
        :param platform: The operating system platform of the component.
        :param version: The component version. For example, ``1.0.0`` .
        :param change_description: The change description of the component. Describes what change has been made in this version, or what makes this version different from other versions of the component.
        :param data: Component ``data`` contains inline YAML document content for the component. Alternatively, you can specify the ``uri`` of a YAML document file stored in Amazon S3. However, you cannot specify both properties.
        :param description: Describes the contents of the component.
        :param kms_key_id: The ID of the KMS key that is used to encrypt this component.
        :param supported_os_versions: The operating system (OS) version supported by the component. If the OS information is available, a prefix match is performed against the base image OS version during image recipe creation.
        :param tags: The tags that apply to the component.
        :param uri: The ``uri`` of a YAML component document file. This must be an S3 URL ( ``s3://bucket/key`` ), and the requester must have permission to access the S3 bucket it points to. If you use Amazon S3, you can specify component content up to your service quota. Alternatively, you can specify the YAML document inline, using the component ``data`` property. You cannot specify both properties.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cee6f52d40719e283a6d76c8b6a6d4fb48180c9c7f4901a21ff32e8627d45b9e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnComponentProps(
            name=name,
            platform=platform,
            version=version,
            change_description=change_description,
            data=data,
            description=description,
            kms_key_id=kms_key_id,
            supported_os_versions=supported_os_versions,
            tags=tags,
            uri=uri,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40b669a1c43c3b3079f4db289296a5190bc19737cdacec67b41121ffeb77db84)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aa56b38fd57c0ef3c75a0f7854e12f5650c218ee9da1e6a0fc3566f2d0bb250e)
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
        '''Returns the Amazon Resource Name (ARN) of the component.

        The following pattern is applied: ``^arn:aws[^:]*:imagebuilder:[^:]+:(?:\\d{12}|aws):(?:image-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline)/[a-z0-9-_]+(?:/(?:(?:x|\\d+)\\.(?:x|\\d+)\\.(?:x|\\d+))(?:/\\d+)?)?$`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrEncrypted")
    def attr_encrypted(self) -> _IResolvable_da3f097b:
        '''Returns the encryption status of the component.

        For example ``true`` or ``false`` .

        :cloudformationAttribute: Encrypted
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrEncrypted"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''Returns the name of the component.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''Image Builder determines the component type based on the phases that are defined in the component document.

        If there is only one phase, and its name is "test", then the type is ``TEST`` . For all other components, the type is ``BUILD`` .

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the component.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad2e949f47b8d1f3fa28e8aecc85097ba0e494b4114a67857ca7449b71baa7eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="platform")
    def platform(self) -> builtins.str:
        '''The operating system platform of the component.'''
        return typing.cast(builtins.str, jsii.get(self, "platform"))

    @platform.setter
    def platform(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0512be6fd4c9842ff94428cb157263d19145ec3979a5af8b91ef02839bf0a59a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platform", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''The component version.'''
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff0f73dccd3a4b2cd5091fd524dac54a149f454f8e4b95ebdbc8bf2d847d695a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="changeDescription")
    def change_description(self) -> typing.Optional[builtins.str]:
        '''The change description of the component.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "changeDescription"))

    @change_description.setter
    def change_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__789ae8523d5582d7b263d5e4e40edc52e6cd54e33a4a8a9da22ce8a46158e664)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "changeDescription", value)

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> typing.Optional[builtins.str]:
        '''Component ``data`` contains inline YAML document content for the component.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "data"))

    @data.setter
    def data(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87721af8240816306f3213003a08de03e0d6e02c52557a8099b6c11f6103e348)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Describes the contents of the component.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fc3d50c994f77416bd1fab3b0e2629efe837f684884eb6608ef71e4e7806ece)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the KMS key that is used to encrypt this component.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa81ab3ceec1f0c67b1340d453195ce21694d45be0f3dc0f50e114a74e30b9dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="supportedOsVersions")
    def supported_os_versions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The operating system (OS) version supported by the component.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "supportedOsVersions"))

    @supported_os_versions.setter
    def supported_os_versions(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0eed3fe1a4cf44875823a85284d0c8b80bbf155582b1e12432340633e2da8c80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supportedOsVersions", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags that apply to the component.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4a5d66d386d51bc332acca6c875fb548297567b633e53e35d7da1075f8af119)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> typing.Optional[builtins.str]:
        '''The ``uri`` of a YAML component document file.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6efe7a7fb79c1c8d2effb9d5fa5a6b2b46eefe80a1dce4011093db23ed26368d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_imagebuilder.CfnComponentProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "platform": "platform",
        "version": "version",
        "change_description": "changeDescription",
        "data": "data",
        "description": "description",
        "kms_key_id": "kmsKeyId",
        "supported_os_versions": "supportedOsVersions",
        "tags": "tags",
        "uri": "uri",
    },
)
class CfnComponentProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        platform: builtins.str,
        version: builtins.str,
        change_description: typing.Optional[builtins.str] = None,
        data: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        supported_os_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnComponent``.

        :param name: The name of the component.
        :param platform: The operating system platform of the component.
        :param version: The component version. For example, ``1.0.0`` .
        :param change_description: The change description of the component. Describes what change has been made in this version, or what makes this version different from other versions of the component.
        :param data: Component ``data`` contains inline YAML document content for the component. Alternatively, you can specify the ``uri`` of a YAML document file stored in Amazon S3. However, you cannot specify both properties.
        :param description: Describes the contents of the component.
        :param kms_key_id: The ID of the KMS key that is used to encrypt this component.
        :param supported_os_versions: The operating system (OS) version supported by the component. If the OS information is available, a prefix match is performed against the base image OS version during image recipe creation.
        :param tags: The tags that apply to the component.
        :param uri: The ``uri`` of a YAML component document file. This must be an S3 URL ( ``s3://bucket/key`` ), and the requester must have permission to access the S3 bucket it points to. If you use Amazon S3, you can specify component content up to your service quota. Alternatively, you can specify the YAML document inline, using the component ``data`` property. You cannot specify both properties.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_imagebuilder as imagebuilder
            
            cfn_component_props = imagebuilder.CfnComponentProps(
                name="name",
                platform="platform",
                version="version",
            
                # the properties below are optional
                change_description="changeDescription",
                data="data",
                description="description",
                kms_key_id="kmsKeyId",
                supported_os_versions=["supportedOsVersions"],
                tags={
                    "tags_key": "tags"
                },
                uri="uri"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__802f9cef9476f7041238f4927a50fed552e7bbbc1054ce0eda41a7b9d75d2d80)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument change_description", value=change_description, expected_type=type_hints["change_description"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument supported_os_versions", value=supported_os_versions, expected_type=type_hints["supported_os_versions"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "platform": platform,
            "version": version,
        }
        if change_description is not None:
            self._values["change_description"] = change_description
        if data is not None:
            self._values["data"] = data
        if description is not None:
            self._values["description"] = description
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if supported_os_versions is not None:
            self._values["supported_os_versions"] = supported_os_versions
        if tags is not None:
            self._values["tags"] = tags
        if uri is not None:
            self._values["uri"] = uri

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the component.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def platform(self) -> builtins.str:
        '''The operating system platform of the component.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-platform
        '''
        result = self._values.get("platform")
        assert result is not None, "Required property 'platform' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''The component version.

        For example, ``1.0.0`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-version
        '''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def change_description(self) -> typing.Optional[builtins.str]:
        '''The change description of the component.

        Describes what change has been made in this version, or what makes this version different from other versions of the component.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-changedescription
        '''
        result = self._values.get("change_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data(self) -> typing.Optional[builtins.str]:
        '''Component ``data`` contains inline YAML document content for the component.

        Alternatively, you can specify the ``uri`` of a YAML document file stored in Amazon S3. However, you cannot specify both properties.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-data
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Describes the contents of the component.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the KMS key that is used to encrypt this component.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def supported_os_versions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The operating system (OS) version supported by the component.

        If the OS information is available, a prefix match is performed against the base image OS version during image recipe creation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-supportedosversions
        '''
        result = self._values.get("supported_os_versions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags that apply to the component.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def uri(self) -> typing.Optional[builtins.str]:
        '''The ``uri`` of a YAML component document file.

        This must be an S3 URL ( ``s3://bucket/key`` ), and the requester must have permission to access the S3 bucket it points to. If you use Amazon S3, you can specify component content up to your service quota.

        Alternatively, you can specify the YAML document inline, using the component ``data`` property. You cannot specify both properties.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-component.html#cfn-imagebuilder-component-uri
        '''
        result = self._values.get("uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnComponentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnContainerRecipe(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_imagebuilder.CfnContainerRecipe",
):
    '''Creates a new container recipe.

    Container recipes define how images are configured, tested, and assessed.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html
    :cloudformationResource: AWS::ImageBuilder::ContainerRecipe
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_imagebuilder as imagebuilder
        
        cfn_container_recipe = imagebuilder.CfnContainerRecipe(self, "MyCfnContainerRecipe",
            components=[imagebuilder.CfnContainerRecipe.ComponentConfigurationProperty(
                component_arn="componentArn",
                parameters=[imagebuilder.CfnContainerRecipe.ComponentParameterProperty(
                    name="name",
                    value=["value"]
                )]
            )],
            container_type="containerType",
            name="name",
            parent_image="parentImage",
            target_repository=imagebuilder.CfnContainerRecipe.TargetContainerRepositoryProperty(
                repository_name="repositoryName",
                service="service"
            ),
            version="version",
        
            # the properties below are optional
            description="description",
            dockerfile_template_data="dockerfileTemplateData",
            dockerfile_template_uri="dockerfileTemplateUri",
            image_os_version_override="imageOsVersionOverride",
            instance_configuration=imagebuilder.CfnContainerRecipe.InstanceConfigurationProperty(
                block_device_mappings=[imagebuilder.CfnContainerRecipe.InstanceBlockDeviceMappingProperty(
                    device_name="deviceName",
                    ebs=imagebuilder.CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty(
                        delete_on_termination=False,
                        encrypted=False,
                        iops=123,
                        kms_key_id="kmsKeyId",
                        snapshot_id="snapshotId",
                        throughput=123,
                        volume_size=123,
                        volume_type="volumeType"
                    ),
                    no_device="noDevice",
                    virtual_name="virtualName"
                )],
                image="image"
            ),
            kms_key_id="kmsKeyId",
            platform_override="platformOverride",
            tags={
                "tags_key": "tags"
            },
            working_directory="workingDirectory"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        components: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerRecipe.ComponentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]],
        container_type: builtins.str,
        name: builtins.str,
        parent_image: builtins.str,
        target_repository: typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerRecipe.TargetContainerRepositoryProperty", typing.Dict[builtins.str, typing.Any]]],
        version: builtins.str,
        description: typing.Optional[builtins.str] = None,
        dockerfile_template_data: typing.Optional[builtins.str] = None,
        dockerfile_template_uri: typing.Optional[builtins.str] = None,
        image_os_version_override: typing.Optional[builtins.str] = None,
        instance_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerRecipe.InstanceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        platform_override: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param components: Build and test components that are included in the container recipe. Recipes require a minimum of one build component, and can have a maximum of 20 build and test components in any combination.
        :param container_type: Specifies the type of container, such as Docker.
        :param name: The name of the container recipe.
        :param parent_image: The base image for the container recipe.
        :param target_repository: The destination repository for the container image.
        :param version: The semantic version of the container recipe. .. epigraph:: The semantic version has four nodes: ../. You can assign values for the first three, and can filter on all of them. *Assignment:* For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node. *Patterns:* You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01. *Filtering:* With semantic versioning, you have the flexibility to use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.
        :param description: The description of the container recipe.
        :param dockerfile_template_data: Dockerfiles are text documents that are used to build Docker containers, and ensure that they contain all of the elements required by the application running inside. The template data consists of contextual variables where Image Builder places build information or scripts, based on your container image recipe.
        :param dockerfile_template_uri: The S3 URI for the Dockerfile that will be used to build your container image.
        :param image_os_version_override: Specifies the operating system version for the base image.
        :param instance_configuration: A group of options that can be used to configure an instance for building and testing container images.
        :param kms_key_id: Identifies which KMS key is used to encrypt the container image for distribution to the target Region.
        :param platform_override: Specifies the operating system platform when you use a custom base image.
        :param tags: Tags that are attached to the container recipe.
        :param working_directory: The working directory for use during build and test workflows.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c468d5dd819e845b41b9c236fc6bca416c9fb91fff1a793739f89182c73cf78)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnContainerRecipeProps(
            components=components,
            container_type=container_type,
            name=name,
            parent_image=parent_image,
            target_repository=target_repository,
            version=version,
            description=description,
            dockerfile_template_data=dockerfile_template_data,
            dockerfile_template_uri=dockerfile_template_uri,
            image_os_version_override=image_os_version_override,
            instance_configuration=instance_configuration,
            kms_key_id=kms_key_id,
            platform_override=platform_override,
            tags=tags,
            working_directory=working_directory,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d50e15547c09a07cb55adb827ff274c67146acfeb8490458d35e268611168856)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6d5b6469a4e69272bf90156a8e5963ff835a02f4987b9ff4170884d2625b3457)
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
        '''Returns the Amazon Resource Name (ARN) of the container recipe.

        For example, ``arn:aws:imagebuilder:us-east-1:123456789012:container-recipe/mybasicrecipe/2020.12.17`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''Returns the name of the container recipe.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

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
    @jsii.member(jsii_name="components")
    def components(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerRecipe.ComponentConfigurationProperty"]]]:
        '''Build and test components that are included in the container recipe.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerRecipe.ComponentConfigurationProperty"]]], jsii.get(self, "components"))

    @components.setter
    def components(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerRecipe.ComponentConfigurationProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be58a433b37609a8e2de38ae9ea0ad32cd2b7ed8705e29e10ecdad873c143b52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "components", value)

    @builtins.property
    @jsii.member(jsii_name="containerType")
    def container_type(self) -> builtins.str:
        '''Specifies the type of container, such as Docker.'''
        return typing.cast(builtins.str, jsii.get(self, "containerType"))

    @container_type.setter
    def container_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98ecd1f7f5bf2b0da0835263286f741cee38c6800e6fd533eb229b76138500e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the container recipe.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3ef18d5728c61a917559c323946757e6be1a7002f20cf91c52bc506c172ef2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parentImage")
    def parent_image(self) -> builtins.str:
        '''The base image for the container recipe.'''
        return typing.cast(builtins.str, jsii.get(self, "parentImage"))

    @parent_image.setter
    def parent_image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06c6a4b42b1e6b26e1648401dcfd1d06a1f54758e6c6c4292c89fcf15aa87b82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parentImage", value)

    @builtins.property
    @jsii.member(jsii_name="targetRepository")
    def target_repository(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnContainerRecipe.TargetContainerRepositoryProperty"]:
        '''The destination repository for the container image.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnContainerRecipe.TargetContainerRepositoryProperty"], jsii.get(self, "targetRepository"))

    @target_repository.setter
    def target_repository(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnContainerRecipe.TargetContainerRepositoryProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a16a6d97d9686aa1fd4e3b9328c4a5a0dd0f749b7ac9889c9035ec5469af398)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetRepository", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''The semantic version of the container recipe.'''
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa6a91dc94efb2a0dd29d944476e7c6c946c97198b7d6387befefe9d97730e5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the container recipe.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1009255c37bcedc70c2d5b858539398c6cb8a82b82af65eaec140a4b08d8f0fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="dockerfileTemplateData")
    def dockerfile_template_data(self) -> typing.Optional[builtins.str]:
        '''Dockerfiles are text documents that are used to build Docker containers, and ensure that they contain all of the elements required by the application running inside.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dockerfileTemplateData"))

    @dockerfile_template_data.setter
    def dockerfile_template_data(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23f0305ca1ea92dfb02b54888f1e788091cf6224ebfaefc930cb4edf9f55995a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dockerfileTemplateData", value)

    @builtins.property
    @jsii.member(jsii_name="dockerfileTemplateUri")
    def dockerfile_template_uri(self) -> typing.Optional[builtins.str]:
        '''The S3 URI for the Dockerfile that will be used to build your container image.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dockerfileTemplateUri"))

    @dockerfile_template_uri.setter
    def dockerfile_template_uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61ed4ed2ebf18638bf7613451687122c6102ece171fee5ba16df758fa37bf12d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dockerfileTemplateUri", value)

    @builtins.property
    @jsii.member(jsii_name="imageOsVersionOverride")
    def image_os_version_override(self) -> typing.Optional[builtins.str]:
        '''Specifies the operating system version for the base image.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageOsVersionOverride"))

    @image_os_version_override.setter
    def image_os_version_override(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6285254ee49b214efc138390c48b3810e45bc304eedb7b87306c2c5e93db5e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageOsVersionOverride", value)

    @builtins.property
    @jsii.member(jsii_name="instanceConfiguration")
    def instance_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerRecipe.InstanceConfigurationProperty"]]:
        '''A group of options that can be used to configure an instance for building and testing container images.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerRecipe.InstanceConfigurationProperty"]], jsii.get(self, "instanceConfiguration"))

    @instance_configuration.setter
    def instance_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerRecipe.InstanceConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba690c6c26b1b3cf3117b63e2f6c837ceb170174c72f085086b1fc988d04a3ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Identifies which KMS key is used to encrypt the container image for distribution to the target Region.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__817846eff0dde79bf417507baefc907f2d5812073cd40bbaec60927922c4c1b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="platformOverride")
    def platform_override(self) -> typing.Optional[builtins.str]:
        '''Specifies the operating system platform when you use a custom base image.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "platformOverride"))

    @platform_override.setter
    def platform_override(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17de30bf20bf8e3ad9fd881a20af8cf79eb9d79af37be867e8f89d583a732b3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platformOverride", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags that are attached to the container recipe.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a1dfc2cdd2904573a5d1ce3b6718ef45ba5250e56b864c223bc455a6441ee05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="workingDirectory")
    def working_directory(self) -> typing.Optional[builtins.str]:
        '''The working directory for use during build and test workflows.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workingDirectory"))

    @working_directory.setter
    def working_directory(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4d9839ccfba608b5591637bb041c5f1859bc5d3d5efc70fc1dbfd3fb7ee6f05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workingDirectory", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnContainerRecipe.ComponentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"component_arn": "componentArn", "parameters": "parameters"},
    )
    class ComponentConfigurationProperty:
        def __init__(
            self,
            *,
            component_arn: typing.Optional[builtins.str] = None,
            parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerRecipe.ComponentParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Configuration details of the component.

            :param component_arn: The Amazon Resource Name (ARN) of the component.
            :param parameters: A group of parameter settings that Image Builder uses to configure the component for a specific recipe.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-componentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                component_configuration_property = imagebuilder.CfnContainerRecipe.ComponentConfigurationProperty(
                    component_arn="componentArn",
                    parameters=[imagebuilder.CfnContainerRecipe.ComponentParameterProperty(
                        name="name",
                        value=["value"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7567002303b2f6603b88563d854827508e4c039225dbff9d2d6511ea3f96404d)
                check_type(argname="argument component_arn", value=component_arn, expected_type=type_hints["component_arn"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if component_arn is not None:
                self._values["component_arn"] = component_arn
            if parameters is not None:
                self._values["parameters"] = parameters

        @builtins.property
        def component_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the component.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-componentconfiguration.html#cfn-imagebuilder-containerrecipe-componentconfiguration-componentarn
            '''
            result = self._values.get("component_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerRecipe.ComponentParameterProperty"]]]]:
            '''A group of parameter settings that Image Builder uses to configure the component for a specific recipe.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-componentconfiguration.html#cfn-imagebuilder-containerrecipe-componentconfiguration-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerRecipe.ComponentParameterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnContainerRecipe.ComponentParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class ComponentParameterProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            value: typing.Sequence[builtins.str],
        ) -> None:
            '''Contains a key/value pair that sets the named component parameter.

            :param name: The name of the component parameter to set.
            :param value: Sets the value for the named component parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-componentparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                component_parameter_property = imagebuilder.CfnContainerRecipe.ComponentParameterProperty(
                    name="name",
                    value=["value"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b194072bb1a463ebdad3622ec5d6ba4a31027cdc36eed1498bba4ffa49ccc1b6)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the component parameter to set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-componentparameter.html#cfn-imagebuilder-containerrecipe-componentparameter-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> typing.List[builtins.str]:
            '''Sets the value for the named component parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-componentparameter.html#cfn-imagebuilder-containerrecipe-componentparameter-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delete_on_termination": "deleteOnTermination",
            "encrypted": "encrypted",
            "iops": "iops",
            "kms_key_id": "kmsKeyId",
            "snapshot_id": "snapshotId",
            "throughput": "throughput",
            "volume_size": "volumeSize",
            "volume_type": "volumeType",
        },
    )
    class EbsInstanceBlockDeviceSpecificationProperty:
        def __init__(
            self,
            *,
            delete_on_termination: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            iops: typing.Optional[jsii.Number] = None,
            kms_key_id: typing.Optional[builtins.str] = None,
            snapshot_id: typing.Optional[builtins.str] = None,
            throughput: typing.Optional[jsii.Number] = None,
            volume_size: typing.Optional[jsii.Number] = None,
            volume_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Amazon EBS-specific block device mapping specifications.

            :param delete_on_termination: Use to configure delete on termination of the associated device.
            :param encrypted: Use to configure device encryption.
            :param iops: Use to configure device IOPS.
            :param kms_key_id: Use to configure the KMS key to use when encrypting the device.
            :param snapshot_id: The snapshot that defines the device contents.
            :param throughput: *For GP3 volumes only* – The throughput in MiB/s that the volume supports.
            :param volume_size: Use to override the device's volume size.
            :param volume_type: Use to override the device's volume type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                ebs_instance_block_device_specification_property = imagebuilder.CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty(
                    delete_on_termination=False,
                    encrypted=False,
                    iops=123,
                    kms_key_id="kmsKeyId",
                    snapshot_id="snapshotId",
                    throughput=123,
                    volume_size=123,
                    volume_type="volumeType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4001b2a6da944a393abf9e0bec60a2ee3d635268cb764774d8cb4d5cdc96a2dc)
                check_type(argname="argument delete_on_termination", value=delete_on_termination, expected_type=type_hints["delete_on_termination"])
                check_type(argname="argument encrypted", value=encrypted, expected_type=type_hints["encrypted"])
                check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
                check_type(argname="argument snapshot_id", value=snapshot_id, expected_type=type_hints["snapshot_id"])
                check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
                check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
                check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if delete_on_termination is not None:
                self._values["delete_on_termination"] = delete_on_termination
            if encrypted is not None:
                self._values["encrypted"] = encrypted
            if iops is not None:
                self._values["iops"] = iops
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id
            if snapshot_id is not None:
                self._values["snapshot_id"] = snapshot_id
            if throughput is not None:
                self._values["throughput"] = throughput
            if volume_size is not None:
                self._values["volume_size"] = volume_size
            if volume_type is not None:
                self._values["volume_type"] = volume_type

        @builtins.property
        def delete_on_termination(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Use to configure delete on termination of the associated device.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-deleteontermination
            '''
            result = self._values.get("delete_on_termination")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def encrypted(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Use to configure device encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-encrypted
            '''
            result = self._values.get("encrypted")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def iops(self) -> typing.Optional[jsii.Number]:
            '''Use to configure device IOPS.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-iops
            '''
            result = self._values.get("iops")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''Use to configure the KMS key to use when encrypting the device.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def snapshot_id(self) -> typing.Optional[builtins.str]:
            '''The snapshot that defines the device contents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-snapshotid
            '''
            result = self._values.get("snapshot_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def throughput(self) -> typing.Optional[jsii.Number]:
            '''*For GP3 volumes only* – The throughput in MiB/s that the volume supports.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-throughput
            '''
            result = self._values.get("throughput")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def volume_size(self) -> typing.Optional[jsii.Number]:
            '''Use to override the device's volume size.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-volumesize
            '''
            result = self._values.get("volume_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def volume_type(self) -> typing.Optional[builtins.str]:
            '''Use to override the device's volume type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-containerrecipe-ebsinstanceblockdevicespecification-volumetype
            '''
            result = self._values.get("volume_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EbsInstanceBlockDeviceSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnContainerRecipe.InstanceBlockDeviceMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "device_name": "deviceName",
            "ebs": "ebs",
            "no_device": "noDevice",
            "virtual_name": "virtualName",
        },
    )
    class InstanceBlockDeviceMappingProperty:
        def __init__(
            self,
            *,
            device_name: typing.Optional[builtins.str] = None,
            ebs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            no_device: typing.Optional[builtins.str] = None,
            virtual_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines block device mappings for the instance used to configure your image.

            :param device_name: The device to which these mappings apply.
            :param ebs: Use to manage Amazon EBS-specific configuration for this mapping.
            :param no_device: Use to remove a mapping from the base image.
            :param virtual_name: Use to manage instance ephemeral devices.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                instance_block_device_mapping_property = imagebuilder.CfnContainerRecipe.InstanceBlockDeviceMappingProperty(
                    device_name="deviceName",
                    ebs=imagebuilder.CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty(
                        delete_on_termination=False,
                        encrypted=False,
                        iops=123,
                        kms_key_id="kmsKeyId",
                        snapshot_id="snapshotId",
                        throughput=123,
                        volume_size=123,
                        volume_type="volumeType"
                    ),
                    no_device="noDevice",
                    virtual_name="virtualName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__50cdb18d882d2c0ab0523c7289014397408b0fd15593ed1334bacde7c89c007e)
                check_type(argname="argument device_name", value=device_name, expected_type=type_hints["device_name"])
                check_type(argname="argument ebs", value=ebs, expected_type=type_hints["ebs"])
                check_type(argname="argument no_device", value=no_device, expected_type=type_hints["no_device"])
                check_type(argname="argument virtual_name", value=virtual_name, expected_type=type_hints["virtual_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if device_name is not None:
                self._values["device_name"] = device_name
            if ebs is not None:
                self._values["ebs"] = ebs
            if no_device is not None:
                self._values["no_device"] = no_device
            if virtual_name is not None:
                self._values["virtual_name"] = virtual_name

        @builtins.property
        def device_name(self) -> typing.Optional[builtins.str]:
            '''The device to which these mappings apply.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping.html#cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-devicename
            '''
            result = self._values.get("device_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ebs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty"]]:
            '''Use to manage Amazon EBS-specific configuration for this mapping.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping.html#cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-ebs
            '''
            result = self._values.get("ebs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty"]], result)

        @builtins.property
        def no_device(self) -> typing.Optional[builtins.str]:
            '''Use to remove a mapping from the base image.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping.html#cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-nodevice
            '''
            result = self._values.get("no_device")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def virtual_name(self) -> typing.Optional[builtins.str]:
            '''Use to manage instance ephemeral devices.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceblockdevicemapping.html#cfn-imagebuilder-containerrecipe-instanceblockdevicemapping-virtualname
            '''
            result = self._values.get("virtual_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceBlockDeviceMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnContainerRecipe.InstanceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "block_device_mappings": "blockDeviceMappings",
            "image": "image",
        },
    )
    class InstanceConfigurationProperty:
        def __init__(
            self,
            *,
            block_device_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerRecipe.InstanceBlockDeviceMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            image: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines a custom base AMI and block device mapping configurations of an instance used for building and testing container images.

            :param block_device_mappings: Defines the block devices to attach for building an instance from this Image Builder AMI.
            :param image: The AMI ID to use as the base image for a container build and test instance. If not specified, Image Builder will use the appropriate ECS-optimized AMI as a base image.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                instance_configuration_property = imagebuilder.CfnContainerRecipe.InstanceConfigurationProperty(
                    block_device_mappings=[imagebuilder.CfnContainerRecipe.InstanceBlockDeviceMappingProperty(
                        device_name="deviceName",
                        ebs=imagebuilder.CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty(
                            delete_on_termination=False,
                            encrypted=False,
                            iops=123,
                            kms_key_id="kmsKeyId",
                            snapshot_id="snapshotId",
                            throughput=123,
                            volume_size=123,
                            volume_type="volumeType"
                        ),
                        no_device="noDevice",
                        virtual_name="virtualName"
                    )],
                    image="image"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__94feecd62024b3049c94588a2a0ff057d5b85caf4f2a481eda383b2a7df9a710)
                check_type(argname="argument block_device_mappings", value=block_device_mappings, expected_type=type_hints["block_device_mappings"])
                check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if block_device_mappings is not None:
                self._values["block_device_mappings"] = block_device_mappings
            if image is not None:
                self._values["image"] = image

        @builtins.property
        def block_device_mappings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerRecipe.InstanceBlockDeviceMappingProperty"]]]]:
            '''Defines the block devices to attach for building an instance from this Image Builder AMI.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceconfiguration.html#cfn-imagebuilder-containerrecipe-instanceconfiguration-blockdevicemappings
            '''
            result = self._values.get("block_device_mappings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerRecipe.InstanceBlockDeviceMappingProperty"]]]], result)

        @builtins.property
        def image(self) -> typing.Optional[builtins.str]:
            '''The AMI ID to use as the base image for a container build and test instance.

            If not specified, Image Builder will use the appropriate ECS-optimized AMI as a base image.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-instanceconfiguration.html#cfn-imagebuilder-containerrecipe-instanceconfiguration-image
            '''
            result = self._values.get("image")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnContainerRecipe.TargetContainerRepositoryProperty",
        jsii_struct_bases=[],
        name_mapping={"repository_name": "repositoryName", "service": "service"},
    )
    class TargetContainerRepositoryProperty:
        def __init__(
            self,
            *,
            repository_name: typing.Optional[builtins.str] = None,
            service: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The container repository where the output container image is stored.

            :param repository_name: The name of the container repository where the output container image is stored. This name is prefixed by the repository location.
            :param service: Specifies the service in which this image was registered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-targetcontainerrepository.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                target_container_repository_property = imagebuilder.CfnContainerRecipe.TargetContainerRepositoryProperty(
                    repository_name="repositoryName",
                    service="service"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__34199ca5f676bc80945fe7e849c29056158da64657ff83277eecd5cd3b62b859)
                check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
                check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if repository_name is not None:
                self._values["repository_name"] = repository_name
            if service is not None:
                self._values["service"] = service

        @builtins.property
        def repository_name(self) -> typing.Optional[builtins.str]:
            '''The name of the container repository where the output container image is stored.

            This name is prefixed by the repository location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-targetcontainerrepository.html#cfn-imagebuilder-containerrecipe-targetcontainerrepository-repositoryname
            '''
            result = self._values.get("repository_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def service(self) -> typing.Optional[builtins.str]:
            '''Specifies the service in which this image was registered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-containerrecipe-targetcontainerrepository.html#cfn-imagebuilder-containerrecipe-targetcontainerrepository-service
            '''
            result = self._values.get("service")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetContainerRepositoryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_imagebuilder.CfnContainerRecipeProps",
    jsii_struct_bases=[],
    name_mapping={
        "components": "components",
        "container_type": "containerType",
        "name": "name",
        "parent_image": "parentImage",
        "target_repository": "targetRepository",
        "version": "version",
        "description": "description",
        "dockerfile_template_data": "dockerfileTemplateData",
        "dockerfile_template_uri": "dockerfileTemplateUri",
        "image_os_version_override": "imageOsVersionOverride",
        "instance_configuration": "instanceConfiguration",
        "kms_key_id": "kmsKeyId",
        "platform_override": "platformOverride",
        "tags": "tags",
        "working_directory": "workingDirectory",
    },
)
class CfnContainerRecipeProps:
    def __init__(
        self,
        *,
        components: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerRecipe.ComponentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
        container_type: builtins.str,
        name: builtins.str,
        parent_image: builtins.str,
        target_repository: typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerRecipe.TargetContainerRepositoryProperty, typing.Dict[builtins.str, typing.Any]]],
        version: builtins.str,
        description: typing.Optional[builtins.str] = None,
        dockerfile_template_data: typing.Optional[builtins.str] = None,
        dockerfile_template_uri: typing.Optional[builtins.str] = None,
        image_os_version_override: typing.Optional[builtins.str] = None,
        instance_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerRecipe.InstanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        platform_override: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnContainerRecipe``.

        :param components: Build and test components that are included in the container recipe. Recipes require a minimum of one build component, and can have a maximum of 20 build and test components in any combination.
        :param container_type: Specifies the type of container, such as Docker.
        :param name: The name of the container recipe.
        :param parent_image: The base image for the container recipe.
        :param target_repository: The destination repository for the container image.
        :param version: The semantic version of the container recipe. .. epigraph:: The semantic version has four nodes: ../. You can assign values for the first three, and can filter on all of them. *Assignment:* For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node. *Patterns:* You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01. *Filtering:* With semantic versioning, you have the flexibility to use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.
        :param description: The description of the container recipe.
        :param dockerfile_template_data: Dockerfiles are text documents that are used to build Docker containers, and ensure that they contain all of the elements required by the application running inside. The template data consists of contextual variables where Image Builder places build information or scripts, based on your container image recipe.
        :param dockerfile_template_uri: The S3 URI for the Dockerfile that will be used to build your container image.
        :param image_os_version_override: Specifies the operating system version for the base image.
        :param instance_configuration: A group of options that can be used to configure an instance for building and testing container images.
        :param kms_key_id: Identifies which KMS key is used to encrypt the container image for distribution to the target Region.
        :param platform_override: Specifies the operating system platform when you use a custom base image.
        :param tags: Tags that are attached to the container recipe.
        :param working_directory: The working directory for use during build and test workflows.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_imagebuilder as imagebuilder
            
            cfn_container_recipe_props = imagebuilder.CfnContainerRecipeProps(
                components=[imagebuilder.CfnContainerRecipe.ComponentConfigurationProperty(
                    component_arn="componentArn",
                    parameters=[imagebuilder.CfnContainerRecipe.ComponentParameterProperty(
                        name="name",
                        value=["value"]
                    )]
                )],
                container_type="containerType",
                name="name",
                parent_image="parentImage",
                target_repository=imagebuilder.CfnContainerRecipe.TargetContainerRepositoryProperty(
                    repository_name="repositoryName",
                    service="service"
                ),
                version="version",
            
                # the properties below are optional
                description="description",
                dockerfile_template_data="dockerfileTemplateData",
                dockerfile_template_uri="dockerfileTemplateUri",
                image_os_version_override="imageOsVersionOverride",
                instance_configuration=imagebuilder.CfnContainerRecipe.InstanceConfigurationProperty(
                    block_device_mappings=[imagebuilder.CfnContainerRecipe.InstanceBlockDeviceMappingProperty(
                        device_name="deviceName",
                        ebs=imagebuilder.CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty(
                            delete_on_termination=False,
                            encrypted=False,
                            iops=123,
                            kms_key_id="kmsKeyId",
                            snapshot_id="snapshotId",
                            throughput=123,
                            volume_size=123,
                            volume_type="volumeType"
                        ),
                        no_device="noDevice",
                        virtual_name="virtualName"
                    )],
                    image="image"
                ),
                kms_key_id="kmsKeyId",
                platform_override="platformOverride",
                tags={
                    "tags_key": "tags"
                },
                working_directory="workingDirectory"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67f8d0f3d1045e15583795ba863ee1d218908e506567e7d12e0aa5861d44ab17)
            check_type(argname="argument components", value=components, expected_type=type_hints["components"])
            check_type(argname="argument container_type", value=container_type, expected_type=type_hints["container_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parent_image", value=parent_image, expected_type=type_hints["parent_image"])
            check_type(argname="argument target_repository", value=target_repository, expected_type=type_hints["target_repository"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument dockerfile_template_data", value=dockerfile_template_data, expected_type=type_hints["dockerfile_template_data"])
            check_type(argname="argument dockerfile_template_uri", value=dockerfile_template_uri, expected_type=type_hints["dockerfile_template_uri"])
            check_type(argname="argument image_os_version_override", value=image_os_version_override, expected_type=type_hints["image_os_version_override"])
            check_type(argname="argument instance_configuration", value=instance_configuration, expected_type=type_hints["instance_configuration"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument platform_override", value=platform_override, expected_type=type_hints["platform_override"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument working_directory", value=working_directory, expected_type=type_hints["working_directory"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "components": components,
            "container_type": container_type,
            "name": name,
            "parent_image": parent_image,
            "target_repository": target_repository,
            "version": version,
        }
        if description is not None:
            self._values["description"] = description
        if dockerfile_template_data is not None:
            self._values["dockerfile_template_data"] = dockerfile_template_data
        if dockerfile_template_uri is not None:
            self._values["dockerfile_template_uri"] = dockerfile_template_uri
        if image_os_version_override is not None:
            self._values["image_os_version_override"] = image_os_version_override
        if instance_configuration is not None:
            self._values["instance_configuration"] = instance_configuration
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if platform_override is not None:
            self._values["platform_override"] = platform_override
        if tags is not None:
            self._values["tags"] = tags
        if working_directory is not None:
            self._values["working_directory"] = working_directory

    @builtins.property
    def components(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContainerRecipe.ComponentConfigurationProperty]]]:
        '''Build and test components that are included in the container recipe.

        Recipes require a minimum of one build component, and can have a maximum of 20 build and test components in any combination.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-components
        '''
        result = self._values.get("components")
        assert result is not None, "Required property 'components' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContainerRecipe.ComponentConfigurationProperty]]], result)

    @builtins.property
    def container_type(self) -> builtins.str:
        '''Specifies the type of container, such as Docker.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-containertype
        '''
        result = self._values.get("container_type")
        assert result is not None, "Required property 'container_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the container recipe.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parent_image(self) -> builtins.str:
        '''The base image for the container recipe.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-parentimage
        '''
        result = self._values.get("parent_image")
        assert result is not None, "Required property 'parent_image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_repository(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnContainerRecipe.TargetContainerRepositoryProperty]:
        '''The destination repository for the container image.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-targetrepository
        '''
        result = self._values.get("target_repository")
        assert result is not None, "Required property 'target_repository' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnContainerRecipe.TargetContainerRepositoryProperty], result)

    @builtins.property
    def version(self) -> builtins.str:
        '''The semantic version of the container recipe.

        .. epigraph::

           The semantic version has four nodes: ../. You can assign values for the first three, and can filter on all of them.

           *Assignment:* For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node.

           *Patterns:* You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.

           *Filtering:* With semantic versioning, you have the flexibility to use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-version
        '''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the container recipe.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dockerfile_template_data(self) -> typing.Optional[builtins.str]:
        '''Dockerfiles are text documents that are used to build Docker containers, and ensure that they contain all of the elements required by the application running inside.

        The template data consists of contextual variables where Image Builder places build information or scripts, based on your container image recipe.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-dockerfiletemplatedata
        '''
        result = self._values.get("dockerfile_template_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dockerfile_template_uri(self) -> typing.Optional[builtins.str]:
        '''The S3 URI for the Dockerfile that will be used to build your container image.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-dockerfiletemplateuri
        '''
        result = self._values.get("dockerfile_template_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_os_version_override(self) -> typing.Optional[builtins.str]:
        '''Specifies the operating system version for the base image.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-imageosversionoverride
        '''
        result = self._values.get("image_os_version_override")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnContainerRecipe.InstanceConfigurationProperty]]:
        '''A group of options that can be used to configure an instance for building and testing container images.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-instanceconfiguration
        '''
        result = self._values.get("instance_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnContainerRecipe.InstanceConfigurationProperty]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Identifies which KMS key is used to encrypt the container image for distribution to the target Region.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def platform_override(self) -> typing.Optional[builtins.str]:
        '''Specifies the operating system platform when you use a custom base image.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-platformoverride
        '''
        result = self._values.get("platform_override")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags that are attached to the container recipe.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def working_directory(self) -> typing.Optional[builtins.str]:
        '''The working directory for use during build and test workflows.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-containerrecipe.html#cfn-imagebuilder-containerrecipe-workingdirectory
        '''
        result = self._values.get("working_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnContainerRecipeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDistributionConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_imagebuilder.CfnDistributionConfiguration",
):
    '''A distribution configuration allows you to specify the name and description of your output AMI, authorize other AWS account s to launch the AMI, and replicate the AMI to other AWS Regions .

    It also allows you to export the AMI to Amazon S3 .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html
    :cloudformationResource: AWS::ImageBuilder::DistributionConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_imagebuilder as imagebuilder
        
        # ami_distribution_configuration: Any
        # container_distribution_configuration: Any
        
        cfn_distribution_configuration = imagebuilder.CfnDistributionConfiguration(self, "MyCfnDistributionConfiguration",
            distributions=[imagebuilder.CfnDistributionConfiguration.DistributionProperty(
                region="region",
        
                # the properties below are optional
                ami_distribution_configuration=ami_distribution_configuration,
                container_distribution_configuration=container_distribution_configuration,
                fast_launch_configurations=[imagebuilder.CfnDistributionConfiguration.FastLaunchConfigurationProperty(
                    account_id="accountId",
                    enabled=False,
                    launch_template=imagebuilder.CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty(
                        launch_template_id="launchTemplateId",
                        launch_template_name="launchTemplateName",
                        launch_template_version="launchTemplateVersion"
                    ),
                    max_parallel_launches=123,
                    snapshot_configuration=imagebuilder.CfnDistributionConfiguration.FastLaunchSnapshotConfigurationProperty(
                        target_resource_count=123
                    )
                )],
                launch_template_configurations=[imagebuilder.CfnDistributionConfiguration.LaunchTemplateConfigurationProperty(
                    account_id="accountId",
                    launch_template_id="launchTemplateId",
                    set_default_version=False
                )],
                license_configuration_arns=["licenseConfigurationArns"]
            )],
            name="name",
        
            # the properties below are optional
            description="description",
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
        distributions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDistributionConfiguration.DistributionProperty", typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param distributions: The distributions of this distribution configuration formatted as an array of Distribution objects.
        :param name: The name of this distribution configuration.
        :param description: The description of this distribution configuration.
        :param tags: The tags of this distribution configuration.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__424bed49628b17ab96124c2266e56c022dd960de454a320aa631249933b84238)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDistributionConfigurationProps(
            distributions=distributions, name=name, description=description, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8c93c8ee1a0cc67cfc5275e236e88b22ff03327ff16d67734ff3d6686a9dbaa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fdfd733425feec8767a979bc76f1a0c04fdefa9d54e164ffd669456e35f87530)
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
        '''Returns the Amazon Resource Name (ARN) of this distribution configuration.

        The following pattern is applied: ``^arn:aws[^:]*:imagebuilder:[^:]+:(?:\\d{12}|aws):(?:image-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline)/[a-z0-9-_]+(?:/(?:(?:x|\\d+)\\.(?:x|\\d+)\\.(?:x|\\d+))(?:/\\d+)?)?$`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''Returns the name of the distribution configuration.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

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
    @jsii.member(jsii_name="distributions")
    def distributions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDistributionConfiguration.DistributionProperty"]]]:
        '''The distributions of this distribution configuration formatted as an array of Distribution objects.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDistributionConfiguration.DistributionProperty"]]], jsii.get(self, "distributions"))

    @distributions.setter
    def distributions(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDistributionConfiguration.DistributionProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__417065f936904d5b1e579e864b23c068bcff521f939e2da134dd0f6a48a5e283)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "distributions", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of this distribution configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d3861330f505671935d810b9849097b7dcf3fe793afbea38a794f2efbf3e528)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of this distribution configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95c7f83d3e50ed6eaf60e3cbf261f7ba851636ae7674d9e772ea1b967db2676e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags of this distribution configuration.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e9679e68354d4ed7fd182e9633596a907a1b8af3224253b40b59ab4ac641ac0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnDistributionConfiguration.AmiDistributionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ami_tags": "amiTags",
            "description": "description",
            "kms_key_id": "kmsKeyId",
            "launch_permission_configuration": "launchPermissionConfiguration",
            "name": "name",
            "target_account_ids": "targetAccountIds",
        },
    )
    class AmiDistributionConfigurationProperty:
        def __init__(
            self,
            *,
            ami_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            description: typing.Optional[builtins.str] = None,
            kms_key_id: typing.Optional[builtins.str] = None,
            launch_permission_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDistributionConfiguration.LaunchPermissionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            name: typing.Optional[builtins.str] = None,
            target_account_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Define and configure the output AMIs of the pipeline.

            :param ami_tags: The tags to apply to AMIs distributed to this Region.
            :param description: The description of the AMI distribution configuration. Minimum and maximum length are in characters.
            :param kms_key_id: The KMS key identifier used to encrypt the distributed image.
            :param launch_permission_configuration: Launch permissions can be used to configure which AWS account s can use the AMI to launch instances.
            :param name: The name of the output AMI.
            :param target_account_ids: The ID of an account to which you want to distribute an image.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                ami_distribution_configuration_property = imagebuilder.CfnDistributionConfiguration.AmiDistributionConfigurationProperty(
                    ami_tags={
                        "ami_tags_key": "amiTags"
                    },
                    description="description",
                    kms_key_id="kmsKeyId",
                    launch_permission_configuration=imagebuilder.CfnDistributionConfiguration.LaunchPermissionConfigurationProperty(
                        organizational_unit_arns=["organizationalUnitArns"],
                        organization_arns=["organizationArns"],
                        user_groups=["userGroups"],
                        user_ids=["userIds"]
                    ),
                    name="name",
                    target_account_ids=["targetAccountIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__78b16e4a7c76877b5dc3dc5bc7508b79d60aed5becf1610e01c5aba5acf7f818)
                check_type(argname="argument ami_tags", value=ami_tags, expected_type=type_hints["ami_tags"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
                check_type(argname="argument launch_permission_configuration", value=launch_permission_configuration, expected_type=type_hints["launch_permission_configuration"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument target_account_ids", value=target_account_ids, expected_type=type_hints["target_account_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ami_tags is not None:
                self._values["ami_tags"] = ami_tags
            if description is not None:
                self._values["description"] = description
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id
            if launch_permission_configuration is not None:
                self._values["launch_permission_configuration"] = launch_permission_configuration
            if name is not None:
                self._values["name"] = name
            if target_account_ids is not None:
                self._values["target_account_ids"] = target_account_ids

        @builtins.property
        def ami_tags(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''The tags to apply to AMIs distributed to this Region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-amitags
            '''
            result = self._values.get("ami_tags")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description of the AMI distribution configuration.

            Minimum and maximum length are in characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The KMS key identifier used to encrypt the distributed image.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def launch_permission_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDistributionConfiguration.LaunchPermissionConfigurationProperty"]]:
            '''Launch permissions can be used to configure which AWS account s can use the AMI to launch instances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-launchpermissionconfiguration
            '''
            result = self._values.get("launch_permission_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDistributionConfiguration.LaunchPermissionConfigurationProperty"]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the output AMI.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_account_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The ID of an account to which you want to distribute an image.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-amidistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-amidistributionconfiguration-targetaccountids
            '''
            result = self._values.get("target_account_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmiDistributionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnDistributionConfiguration.ContainerDistributionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_tags": "containerTags",
            "description": "description",
            "target_repository": "targetRepository",
        },
    )
    class ContainerDistributionConfigurationProperty:
        def __init__(
            self,
            *,
            container_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
            description: typing.Optional[builtins.str] = None,
            target_repository: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDistributionConfiguration.TargetContainerRepositoryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Container distribution settings for encryption, licensing, and sharing in a specific Region.

            :param container_tags: Tags that are attached to the container distribution configuration.
            :param description: The description of the container distribution configuration.
            :param target_repository: The destination repository for the container distribution configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-containerdistributionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                container_distribution_configuration_property = imagebuilder.CfnDistributionConfiguration.ContainerDistributionConfigurationProperty(
                    container_tags=["containerTags"],
                    description="description",
                    target_repository=imagebuilder.CfnDistributionConfiguration.TargetContainerRepositoryProperty(
                        repository_name="repositoryName",
                        service="service"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__125e3573ab2e6c73f141e1784bd0d6c99de3714f6122708d9404d939bfa152b5)
                check_type(argname="argument container_tags", value=container_tags, expected_type=type_hints["container_tags"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument target_repository", value=target_repository, expected_type=type_hints["target_repository"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if container_tags is not None:
                self._values["container_tags"] = container_tags
            if description is not None:
                self._values["description"] = description
            if target_repository is not None:
                self._values["target_repository"] = target_repository

        @builtins.property
        def container_tags(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Tags that are attached to the container distribution configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-containerdistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-containerdistributionconfiguration-containertags
            '''
            result = self._values.get("container_tags")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description of the container distribution configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-containerdistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-containerdistributionconfiguration-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_repository(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDistributionConfiguration.TargetContainerRepositoryProperty"]]:
            '''The destination repository for the container distribution configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-containerdistributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-containerdistributionconfiguration-targetrepository
            '''
            result = self._values.get("target_repository")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDistributionConfiguration.TargetContainerRepositoryProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerDistributionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnDistributionConfiguration.DistributionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "region": "region",
            "ami_distribution_configuration": "amiDistributionConfiguration",
            "container_distribution_configuration": "containerDistributionConfiguration",
            "fast_launch_configurations": "fastLaunchConfigurations",
            "launch_template_configurations": "launchTemplateConfigurations",
            "license_configuration_arns": "licenseConfigurationArns",
        },
    )
    class DistributionProperty:
        def __init__(
            self,
            *,
            region: builtins.str,
            ami_distribution_configuration: typing.Any = None,
            container_distribution_configuration: typing.Any = None,
            fast_launch_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDistributionConfiguration.FastLaunchConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            launch_template_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDistributionConfiguration.LaunchTemplateConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            license_configuration_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The distribution configuration distribution defines the settings for a specific Region in the Distribution Configuration.

            You must specify whether the distribution is for an AMI or a container image. To do so, include exactly one of the following data types for your distribution:

            - amiDistributionConfiguration
            - containerDistributionConfiguration

            :param region: The target Region for the Distribution Configuration. For example, ``eu-west-1`` .
            :param ami_distribution_configuration: The specific AMI settings, such as launch permissions and AMI tags. For details, see example schema below.
            :param container_distribution_configuration: Container distribution settings for encryption, licensing, and sharing in a specific Region. For details, see example schema below.
            :param fast_launch_configurations: The Windows faster-launching configurations to use for AMI distribution.
            :param launch_template_configurations: A group of launchTemplateConfiguration settings that apply to image distribution for specified accounts.
            :param license_configuration_arns: The License Manager Configuration to associate with the AMI in the specified Region. For more information, see the `LicenseConfiguration API <https://docs.aws.amazon.com/license-manager/latest/APIReference/API_LicenseConfiguration.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                # ami_distribution_configuration: Any
                # container_distribution_configuration: Any
                
                distribution_property = imagebuilder.CfnDistributionConfiguration.DistributionProperty(
                    region="region",
                
                    # the properties below are optional
                    ami_distribution_configuration=ami_distribution_configuration,
                    container_distribution_configuration=container_distribution_configuration,
                    fast_launch_configurations=[imagebuilder.CfnDistributionConfiguration.FastLaunchConfigurationProperty(
                        account_id="accountId",
                        enabled=False,
                        launch_template=imagebuilder.CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty(
                            launch_template_id="launchTemplateId",
                            launch_template_name="launchTemplateName",
                            launch_template_version="launchTemplateVersion"
                        ),
                        max_parallel_launches=123,
                        snapshot_configuration=imagebuilder.CfnDistributionConfiguration.FastLaunchSnapshotConfigurationProperty(
                            target_resource_count=123
                        )
                    )],
                    launch_template_configurations=[imagebuilder.CfnDistributionConfiguration.LaunchTemplateConfigurationProperty(
                        account_id="accountId",
                        launch_template_id="launchTemplateId",
                        set_default_version=False
                    )],
                    license_configuration_arns=["licenseConfigurationArns"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__29d1f34d5faec16ba828ad2333ee9218a18df31808a5a350be9b29d048555c54)
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument ami_distribution_configuration", value=ami_distribution_configuration, expected_type=type_hints["ami_distribution_configuration"])
                check_type(argname="argument container_distribution_configuration", value=container_distribution_configuration, expected_type=type_hints["container_distribution_configuration"])
                check_type(argname="argument fast_launch_configurations", value=fast_launch_configurations, expected_type=type_hints["fast_launch_configurations"])
                check_type(argname="argument launch_template_configurations", value=launch_template_configurations, expected_type=type_hints["launch_template_configurations"])
                check_type(argname="argument license_configuration_arns", value=license_configuration_arns, expected_type=type_hints["license_configuration_arns"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "region": region,
            }
            if ami_distribution_configuration is not None:
                self._values["ami_distribution_configuration"] = ami_distribution_configuration
            if container_distribution_configuration is not None:
                self._values["container_distribution_configuration"] = container_distribution_configuration
            if fast_launch_configurations is not None:
                self._values["fast_launch_configurations"] = fast_launch_configurations
            if launch_template_configurations is not None:
                self._values["launch_template_configurations"] = launch_template_configurations
            if license_configuration_arns is not None:
                self._values["license_configuration_arns"] = license_configuration_arns

        @builtins.property
        def region(self) -> builtins.str:
            '''The target Region for the Distribution Configuration.

            For example, ``eu-west-1`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html#cfn-imagebuilder-distributionconfiguration-distribution-region
            '''
            result = self._values.get("region")
            assert result is not None, "Required property 'region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def ami_distribution_configuration(self) -> typing.Any:
            '''The specific AMI settings, such as launch permissions and AMI tags.

            For details, see example schema below.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html#cfn-imagebuilder-distributionconfiguration-distribution-amidistributionconfiguration
            '''
            result = self._values.get("ami_distribution_configuration")
            return typing.cast(typing.Any, result)

        @builtins.property
        def container_distribution_configuration(self) -> typing.Any:
            '''Container distribution settings for encryption, licensing, and sharing in a specific Region.

            For details, see example schema below.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html#cfn-imagebuilder-distributionconfiguration-distribution-containerdistributionconfiguration
            '''
            result = self._values.get("container_distribution_configuration")
            return typing.cast(typing.Any, result)

        @builtins.property
        def fast_launch_configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDistributionConfiguration.FastLaunchConfigurationProperty"]]]]:
            '''The Windows faster-launching configurations to use for AMI distribution.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html#cfn-imagebuilder-distributionconfiguration-distribution-fastlaunchconfigurations
            '''
            result = self._values.get("fast_launch_configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDistributionConfiguration.FastLaunchConfigurationProperty"]]]], result)

        @builtins.property
        def launch_template_configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDistributionConfiguration.LaunchTemplateConfigurationProperty"]]]]:
            '''A group of launchTemplateConfiguration settings that apply to image distribution for specified accounts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html#cfn-imagebuilder-distributionconfiguration-distribution-launchtemplateconfigurations
            '''
            result = self._values.get("launch_template_configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDistributionConfiguration.LaunchTemplateConfigurationProperty"]]]], result)

        @builtins.property
        def license_configuration_arns(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''The License Manager Configuration to associate with the AMI in the specified Region.

            For more information, see the `LicenseConfiguration API <https://docs.aws.amazon.com/license-manager/latest/APIReference/API_LicenseConfiguration.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-distribution.html#cfn-imagebuilder-distributionconfiguration-distribution-licenseconfigurationarns
            '''
            result = self._values.get("license_configuration_arns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DistributionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnDistributionConfiguration.FastLaunchConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_id": "accountId",
            "enabled": "enabled",
            "launch_template": "launchTemplate",
            "max_parallel_launches": "maxParallelLaunches",
            "snapshot_configuration": "snapshotConfiguration",
        },
    )
    class FastLaunchConfigurationProperty:
        def __init__(
            self,
            *,
            account_id: typing.Optional[builtins.str] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            launch_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            max_parallel_launches: typing.Optional[jsii.Number] = None,
            snapshot_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDistributionConfiguration.FastLaunchSnapshotConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Define and configure faster launching for output Windows AMIs.

            :param account_id: The owner account ID for the fast-launch enabled Windows AMI.
            :param enabled: A Boolean that represents the current state of faster launching for the Windows AMI. Set to ``true`` to start using Windows faster launching, or ``false`` to stop using it.
            :param launch_template: The launch template that the fast-launch enabled Windows AMI uses when it launches Windows instances to create pre-provisioned snapshots.
            :param max_parallel_launches: The maximum number of parallel instances that are launched for creating resources.
            :param snapshot_configuration: Configuration settings for managing the number of snapshots that are created from pre-provisioned instances for the Windows AMI when faster launching is enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                fast_launch_configuration_property = imagebuilder.CfnDistributionConfiguration.FastLaunchConfigurationProperty(
                    account_id="accountId",
                    enabled=False,
                    launch_template=imagebuilder.CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty(
                        launch_template_id="launchTemplateId",
                        launch_template_name="launchTemplateName",
                        launch_template_version="launchTemplateVersion"
                    ),
                    max_parallel_launches=123,
                    snapshot_configuration=imagebuilder.CfnDistributionConfiguration.FastLaunchSnapshotConfigurationProperty(
                        target_resource_count=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__55c8e6821fd98707615f7982782feb32e6fa579e64adbef7db96af2d7b0c40ea)
                check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument launch_template", value=launch_template, expected_type=type_hints["launch_template"])
                check_type(argname="argument max_parallel_launches", value=max_parallel_launches, expected_type=type_hints["max_parallel_launches"])
                check_type(argname="argument snapshot_configuration", value=snapshot_configuration, expected_type=type_hints["snapshot_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if account_id is not None:
                self._values["account_id"] = account_id
            if enabled is not None:
                self._values["enabled"] = enabled
            if launch_template is not None:
                self._values["launch_template"] = launch_template
            if max_parallel_launches is not None:
                self._values["max_parallel_launches"] = max_parallel_launches
            if snapshot_configuration is not None:
                self._values["snapshot_configuration"] = snapshot_configuration

        @builtins.property
        def account_id(self) -> typing.Optional[builtins.str]:
            '''The owner account ID for the fast-launch enabled Windows AMI.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.html#cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-accountid
            '''
            result = self._values.get("account_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A Boolean that represents the current state of faster launching for the Windows AMI.

            Set to ``true`` to start using Windows faster launching, or ``false`` to stop using it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.html#cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def launch_template(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty"]]:
            '''The launch template that the fast-launch enabled Windows AMI uses when it launches Windows instances to create pre-provisioned snapshots.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.html#cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-launchtemplate
            '''
            result = self._values.get("launch_template")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty"]], result)

        @builtins.property
        def max_parallel_launches(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of parallel instances that are launched for creating resources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.html#cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-maxparallellaunches
            '''
            result = self._values.get("max_parallel_launches")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def snapshot_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDistributionConfiguration.FastLaunchSnapshotConfigurationProperty"]]:
            '''Configuration settings for managing the number of snapshots that are created from pre-provisioned instances for the Windows AMI when faster launching is enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchconfiguration.html#cfn-imagebuilder-distributionconfiguration-fastlaunchconfiguration-snapshotconfiguration
            '''
            result = self._values.get("snapshot_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDistributionConfiguration.FastLaunchSnapshotConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FastLaunchConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "launch_template_id": "launchTemplateId",
            "launch_template_name": "launchTemplateName",
            "launch_template_version": "launchTemplateVersion",
        },
    )
    class FastLaunchLaunchTemplateSpecificationProperty:
        def __init__(
            self,
            *,
            launch_template_id: typing.Optional[builtins.str] = None,
            launch_template_name: typing.Optional[builtins.str] = None,
            launch_template_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Identifies the launch template that the associated Windows AMI uses for launching an instance when faster launching is enabled.

            .. epigraph::

               You can specify either the ``launchTemplateName`` or the ``launchTemplateId`` , but not both.

            :param launch_template_id: The ID of the launch template to use for faster launching for a Windows AMI.
            :param launch_template_name: The name of the launch template to use for faster launching for a Windows AMI.
            :param launch_template_version: The version of the launch template to use for faster launching for a Windows AMI.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                fast_launch_launch_template_specification_property = imagebuilder.CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty(
                    launch_template_id="launchTemplateId",
                    launch_template_name="launchTemplateName",
                    launch_template_version="launchTemplateVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__021d1b3db5c8ca8f6806bf8d9d829821d8e3b628222bed84a3d6f72106555ee3)
                check_type(argname="argument launch_template_id", value=launch_template_id, expected_type=type_hints["launch_template_id"])
                check_type(argname="argument launch_template_name", value=launch_template_name, expected_type=type_hints["launch_template_name"])
                check_type(argname="argument launch_template_version", value=launch_template_version, expected_type=type_hints["launch_template_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if launch_template_id is not None:
                self._values["launch_template_id"] = launch_template_id
            if launch_template_name is not None:
                self._values["launch_template_name"] = launch_template_name
            if launch_template_version is not None:
                self._values["launch_template_version"] = launch_template_version

        @builtins.property
        def launch_template_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the launch template to use for faster launching for a Windows AMI.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification.html#cfn-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification-launchtemplateid
            '''
            result = self._values.get("launch_template_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def launch_template_name(self) -> typing.Optional[builtins.str]:
            '''The name of the launch template to use for faster launching for a Windows AMI.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification.html#cfn-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification-launchtemplatename
            '''
            result = self._values.get("launch_template_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def launch_template_version(self) -> typing.Optional[builtins.str]:
            '''The version of the launch template to use for faster launching for a Windows AMI.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification.html#cfn-imagebuilder-distributionconfiguration-fastlaunchlaunchtemplatespecification-launchtemplateversion
            '''
            result = self._values.get("launch_template_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FastLaunchLaunchTemplateSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnDistributionConfiguration.FastLaunchSnapshotConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"target_resource_count": "targetResourceCount"},
    )
    class FastLaunchSnapshotConfigurationProperty:
        def __init__(
            self,
            *,
            target_resource_count: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Configuration settings for creating and managing pre-provisioned snapshots for a fast-launch enabled Windows AMI.

            :param target_resource_count: The number of pre-provisioned snapshots to keep on hand for a fast-launch enabled Windows AMI.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchsnapshotconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                fast_launch_snapshot_configuration_property = imagebuilder.CfnDistributionConfiguration.FastLaunchSnapshotConfigurationProperty(
                    target_resource_count=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__742f14fac4b1a3338b9e181cf90ffe52f3bc892fe33258d6ee8e31f32b62e25f)
                check_type(argname="argument target_resource_count", value=target_resource_count, expected_type=type_hints["target_resource_count"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if target_resource_count is not None:
                self._values["target_resource_count"] = target_resource_count

        @builtins.property
        def target_resource_count(self) -> typing.Optional[jsii.Number]:
            '''The number of pre-provisioned snapshots to keep on hand for a fast-launch enabled Windows AMI.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-fastlaunchsnapshotconfiguration.html#cfn-imagebuilder-distributionconfiguration-fastlaunchsnapshotconfiguration-targetresourcecount
            '''
            result = self._values.get("target_resource_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FastLaunchSnapshotConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnDistributionConfiguration.LaunchPermissionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "organizational_unit_arns": "organizationalUnitArns",
            "organization_arns": "organizationArns",
            "user_groups": "userGroups",
            "user_ids": "userIds",
        },
    )
    class LaunchPermissionConfigurationProperty:
        def __init__(
            self,
            *,
            organizational_unit_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
            organization_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
            user_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
            user_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Describes the configuration for a launch permission.

            The launch permission modification request is sent to the `Amazon EC2 ModifyImageAttribute <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyImageAttribute.html>`_ API on behalf of the user for each Region they have selected to distribute the AMI. To make an AMI public, set the launch permission authorized accounts to ``all`` . See the examples for making an AMI public at `Amazon EC2 ModifyImageAttribute <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyImageAttribute.html>`_ .

            :param organizational_unit_arns: The ARN for an AWS Organizations organizational unit (OU) that you want to share your AMI with. For more information about key concepts for AWS Organizations , see `AWS Organizations terminology and concepts <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html>`_ .
            :param organization_arns: The ARN for an AWS Organization that you want to share your AMI with. For more information, see `What is AWS Organizations ? <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html>`_ .
            :param user_groups: The name of the group.
            :param user_ids: The AWS account ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchpermissionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                launch_permission_configuration_property = imagebuilder.CfnDistributionConfiguration.LaunchPermissionConfigurationProperty(
                    organizational_unit_arns=["organizationalUnitArns"],
                    organization_arns=["organizationArns"],
                    user_groups=["userGroups"],
                    user_ids=["userIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0184c66c3ce1b1a9581759138f6b03cdf0b49876c0cd4e7191f619d41bc6a8f7)
                check_type(argname="argument organizational_unit_arns", value=organizational_unit_arns, expected_type=type_hints["organizational_unit_arns"])
                check_type(argname="argument organization_arns", value=organization_arns, expected_type=type_hints["organization_arns"])
                check_type(argname="argument user_groups", value=user_groups, expected_type=type_hints["user_groups"])
                check_type(argname="argument user_ids", value=user_ids, expected_type=type_hints["user_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if organizational_unit_arns is not None:
                self._values["organizational_unit_arns"] = organizational_unit_arns
            if organization_arns is not None:
                self._values["organization_arns"] = organization_arns
            if user_groups is not None:
                self._values["user_groups"] = user_groups
            if user_ids is not None:
                self._values["user_ids"] = user_ids

        @builtins.property
        def organizational_unit_arns(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''The ARN for an AWS Organizations organizational unit (OU) that you want to share your AMI with.

            For more information about key concepts for AWS Organizations , see `AWS Organizations terminology and concepts <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchpermissionconfiguration.html#cfn-imagebuilder-distributionconfiguration-launchpermissionconfiguration-organizationalunitarns
            '''
            result = self._values.get("organizational_unit_arns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def organization_arns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The ARN for an AWS Organization that you want to share your AMI with.

            For more information, see `What is AWS Organizations ? <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchpermissionconfiguration.html#cfn-imagebuilder-distributionconfiguration-launchpermissionconfiguration-organizationarns
            '''
            result = self._values.get("organization_arns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def user_groups(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The name of the group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchpermissionconfiguration.html#cfn-imagebuilder-distributionconfiguration-launchpermissionconfiguration-usergroups
            '''
            result = self._values.get("user_groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def user_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The AWS account ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchpermissionconfiguration.html#cfn-imagebuilder-distributionconfiguration-launchpermissionconfiguration-userids
            '''
            result = self._values.get("user_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LaunchPermissionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnDistributionConfiguration.LaunchTemplateConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_id": "accountId",
            "launch_template_id": "launchTemplateId",
            "set_default_version": "setDefaultVersion",
        },
    )
    class LaunchTemplateConfigurationProperty:
        def __init__(
            self,
            *,
            account_id: typing.Optional[builtins.str] = None,
            launch_template_id: typing.Optional[builtins.str] = None,
            set_default_version: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Identifies an Amazon EC2 launch template to use for a specific account.

            :param account_id: The account ID that this configuration applies to.
            :param launch_template_id: Identifies the Amazon EC2 launch template to use.
            :param set_default_version: Set the specified Amazon EC2 launch template as the default launch template for the specified account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchtemplateconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                launch_template_configuration_property = imagebuilder.CfnDistributionConfiguration.LaunchTemplateConfigurationProperty(
                    account_id="accountId",
                    launch_template_id="launchTemplateId",
                    set_default_version=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0b4c1c669ce6e1367a73060d15f089faa5ce58e96063ee38204bf9af12043035)
                check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
                check_type(argname="argument launch_template_id", value=launch_template_id, expected_type=type_hints["launch_template_id"])
                check_type(argname="argument set_default_version", value=set_default_version, expected_type=type_hints["set_default_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if account_id is not None:
                self._values["account_id"] = account_id
            if launch_template_id is not None:
                self._values["launch_template_id"] = launch_template_id
            if set_default_version is not None:
                self._values["set_default_version"] = set_default_version

        @builtins.property
        def account_id(self) -> typing.Optional[builtins.str]:
            '''The account ID that this configuration applies to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchtemplateconfiguration.html#cfn-imagebuilder-distributionconfiguration-launchtemplateconfiguration-accountid
            '''
            result = self._values.get("account_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def launch_template_id(self) -> typing.Optional[builtins.str]:
            '''Identifies the Amazon EC2 launch template to use.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchtemplateconfiguration.html#cfn-imagebuilder-distributionconfiguration-launchtemplateconfiguration-launchtemplateid
            '''
            result = self._values.get("launch_template_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def set_default_version(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set the specified Amazon EC2 launch template as the default launch template for the specified account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-launchtemplateconfiguration.html#cfn-imagebuilder-distributionconfiguration-launchtemplateconfiguration-setdefaultversion
            '''
            result = self._values.get("set_default_version")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LaunchTemplateConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnDistributionConfiguration.TargetContainerRepositoryProperty",
        jsii_struct_bases=[],
        name_mapping={"repository_name": "repositoryName", "service": "service"},
    )
    class TargetContainerRepositoryProperty:
        def __init__(
            self,
            *,
            repository_name: typing.Optional[builtins.str] = None,
            service: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The container repository where the output container image is stored.

            :param repository_name: The name of the container repository where the output container image is stored. This name is prefixed by the repository location.
            :param service: Specifies the service in which this image was registered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-targetcontainerrepository.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                target_container_repository_property = imagebuilder.CfnDistributionConfiguration.TargetContainerRepositoryProperty(
                    repository_name="repositoryName",
                    service="service"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fd67a7cda75ae308d03a62ceb5b017b8de54cd08fd47374326a441ec680438a5)
                check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
                check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if repository_name is not None:
                self._values["repository_name"] = repository_name
            if service is not None:
                self._values["service"] = service

        @builtins.property
        def repository_name(self) -> typing.Optional[builtins.str]:
            '''The name of the container repository where the output container image is stored.

            This name is prefixed by the repository location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-targetcontainerrepository.html#cfn-imagebuilder-distributionconfiguration-targetcontainerrepository-repositoryname
            '''
            result = self._values.get("repository_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def service(self) -> typing.Optional[builtins.str]:
            '''Specifies the service in which this image was registered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-distributionconfiguration-targetcontainerrepository.html#cfn-imagebuilder-distributionconfiguration-targetcontainerrepository-service
            '''
            result = self._values.get("service")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetContainerRepositoryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_imagebuilder.CfnDistributionConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "distributions": "distributions",
        "name": "name",
        "description": "description",
        "tags": "tags",
    },
)
class CfnDistributionConfigurationProps:
    def __init__(
        self,
        *,
        distributions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDistributionConfiguration.DistributionProperty, typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDistributionConfiguration``.

        :param distributions: The distributions of this distribution configuration formatted as an array of Distribution objects.
        :param name: The name of this distribution configuration.
        :param description: The description of this distribution configuration.
        :param tags: The tags of this distribution configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_imagebuilder as imagebuilder
            
            # ami_distribution_configuration: Any
            # container_distribution_configuration: Any
            
            cfn_distribution_configuration_props = imagebuilder.CfnDistributionConfigurationProps(
                distributions=[imagebuilder.CfnDistributionConfiguration.DistributionProperty(
                    region="region",
            
                    # the properties below are optional
                    ami_distribution_configuration=ami_distribution_configuration,
                    container_distribution_configuration=container_distribution_configuration,
                    fast_launch_configurations=[imagebuilder.CfnDistributionConfiguration.FastLaunchConfigurationProperty(
                        account_id="accountId",
                        enabled=False,
                        launch_template=imagebuilder.CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty(
                            launch_template_id="launchTemplateId",
                            launch_template_name="launchTemplateName",
                            launch_template_version="launchTemplateVersion"
                        ),
                        max_parallel_launches=123,
                        snapshot_configuration=imagebuilder.CfnDistributionConfiguration.FastLaunchSnapshotConfigurationProperty(
                            target_resource_count=123
                        )
                    )],
                    launch_template_configurations=[imagebuilder.CfnDistributionConfiguration.LaunchTemplateConfigurationProperty(
                        account_id="accountId",
                        launch_template_id="launchTemplateId",
                        set_default_version=False
                    )],
                    license_configuration_arns=["licenseConfigurationArns"]
                )],
                name="name",
            
                # the properties below are optional
                description="description",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f16c19e0cbb34ea9e02eb4cfcaa69a6cdf4c60af0ca2736a9d0dd6b74445c9d8)
            check_type(argname="argument distributions", value=distributions, expected_type=type_hints["distributions"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "distributions": distributions,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def distributions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDistributionConfiguration.DistributionProperty]]]:
        '''The distributions of this distribution configuration formatted as an array of Distribution objects.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-distributions
        '''
        result = self._values.get("distributions")
        assert result is not None, "Required property 'distributions' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDistributionConfiguration.DistributionProperty]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of this distribution configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of this distribution configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags of this distribution configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-distributionconfiguration.html#cfn-imagebuilder-distributionconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDistributionConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnImage(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_imagebuilder.CfnImage",
):
    '''Creates a new image.

    This request will create a new image along with all of the configured output resources defined in the distribution configuration. You must specify exactly one recipe for your image, using either a ContainerRecipeArn or an ImageRecipeArn.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html
    :cloudformationResource: AWS::ImageBuilder::Image
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_imagebuilder as imagebuilder
        
        cfn_image = imagebuilder.CfnImage(self, "MyCfnImage",
            infrastructure_configuration_arn="infrastructureConfigurationArn",
        
            # the properties below are optional
            container_recipe_arn="containerRecipeArn",
            distribution_configuration_arn="distributionConfigurationArn",
            enhanced_image_metadata_enabled=False,
            execution_role="executionRole",
            image_recipe_arn="imageRecipeArn",
            image_scanning_configuration=imagebuilder.CfnImage.ImageScanningConfigurationProperty(
                ecr_configuration=imagebuilder.CfnImage.EcrConfigurationProperty(
                    container_tags=["containerTags"],
                    repository_name="repositoryName"
                ),
                image_scanning_enabled=False
            ),
            image_tests_configuration=imagebuilder.CfnImage.ImageTestsConfigurationProperty(
                image_tests_enabled=False,
                timeout_minutes=123
            ),
            tags={
                "tags_key": "tags"
            },
            workflows=[imagebuilder.CfnImage.WorkflowConfigurationProperty(
                on_failure="onFailure",
                parallel_group="parallelGroup",
                parameters=[imagebuilder.CfnImage.WorkflowParameterProperty(
                    name="name",
                    value=["value"]
                )],
                workflow_arn="workflowArn"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        infrastructure_configuration_arn: builtins.str,
        container_recipe_arn: typing.Optional[builtins.str] = None,
        distribution_configuration_arn: typing.Optional[builtins.str] = None,
        enhanced_image_metadata_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        execution_role: typing.Optional[builtins.str] = None,
        image_recipe_arn: typing.Optional[builtins.str] = None,
        image_scanning_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnImage.ImageScanningConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        image_tests_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnImage.ImageTestsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        workflows: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnImage.WorkflowConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param infrastructure_configuration_arn: The Amazon Resource Name (ARN) of the infrastructure configuration that defines the environment in which your image will be built and tested.
        :param container_recipe_arn: The Amazon Resource Name (ARN) of the container recipe that defines how images are configured and tested.
        :param distribution_configuration_arn: The Amazon Resource Name (ARN) of the distribution configuration that defines and configures the outputs of your pipeline.
        :param enhanced_image_metadata_enabled: Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.
        :param execution_role: The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.
        :param image_recipe_arn: The Amazon Resource Name (ARN) of the image recipe that defines how images are configured, tested, and assessed.
        :param image_scanning_configuration: Contains settings for vulnerability scans.
        :param image_tests_configuration: The image tests configuration of the image.
        :param tags: The tags of the image.
        :param workflows: Contains an array of workflow configuration objects.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1406bc225111bc54a87c50d1d8180aed46d22e10134235c4fa581d3137e5bddf)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnImageProps(
            infrastructure_configuration_arn=infrastructure_configuration_arn,
            container_recipe_arn=container_recipe_arn,
            distribution_configuration_arn=distribution_configuration_arn,
            enhanced_image_metadata_enabled=enhanced_image_metadata_enabled,
            execution_role=execution_role,
            image_recipe_arn=image_recipe_arn,
            image_scanning_configuration=image_scanning_configuration,
            image_tests_configuration=image_tests_configuration,
            tags=tags,
            workflows=workflows,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5772703e735ab7511274ad4c83f3ee56bfacba182fbe209189bed84d493649c5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8052419a8d8b963d7c9b1b75cd6654f49a4ad3b49a754eb0e90c63bf70d1fa6b)
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
        '''Returns the Amazon Resource Name (ARN) of the image.

        For example, ``arn:aws:imagebuilder:us-west-2:123456789012:image/mybasicrecipe/2019.12.03/1`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrImageId")
    def attr_image_id(self) -> builtins.str:
        '''Returns the AMI ID of the Amazon EC2 AMI in the Region in which you are using Image Builder.

        Values are returned only for AMIs, and not for container images.

        :cloudformationAttribute: ImageId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrImageId"))

    @builtins.property
    @jsii.member(jsii_name="attrImageUri")
    def attr_image_uri(self) -> builtins.str:
        '''Returns the URI for a container image created in the context Region.

        Values are returned only for container images, and not for AMIs.

        :cloudformationAttribute: ImageUri
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrImageUri"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''Returns the name of the image.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

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
    @jsii.member(jsii_name="infrastructureConfigurationArn")
    def infrastructure_configuration_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the infrastructure configuration that defines the environment in which your image will be built and tested.'''
        return typing.cast(builtins.str, jsii.get(self, "infrastructureConfigurationArn"))

    @infrastructure_configuration_arn.setter
    def infrastructure_configuration_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a190431e330e97015561230a0d9b0477abed6793472228169b2ce3d498e18c8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "infrastructureConfigurationArn", value)

    @builtins.property
    @jsii.member(jsii_name="containerRecipeArn")
    def container_recipe_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the container recipe that defines how images are configured and tested.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerRecipeArn"))

    @container_recipe_arn.setter
    def container_recipe_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6e036331c49a5f902af4e72bc4f291c89a7f5f03a4453a10c55e0f2bde10ac7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerRecipeArn", value)

    @builtins.property
    @jsii.member(jsii_name="distributionConfigurationArn")
    def distribution_configuration_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the distribution configuration that defines and configures the outputs of your pipeline.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "distributionConfigurationArn"))

    @distribution_configuration_arn.setter
    def distribution_configuration_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__889890f98c732641897f78af3545740dd9c7c236d01f0d3e3c038263bc80498c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "distributionConfigurationArn", value)

    @builtins.property
    @jsii.member(jsii_name="enhancedImageMetadataEnabled")
    def enhanced_image_metadata_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Collects additional information about the image being created, including the operating system (OS) version and package list.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enhancedImageMetadataEnabled"))

    @enhanced_image_metadata_enabled.setter
    def enhanced_image_metadata_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5e9d51fefc7d1e1bc910eea2e49d7094b0e13fbcbdb19541025c130619890a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enhancedImageMetadataEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="executionRole")
    def execution_role(self) -> typing.Optional[builtins.str]:
        '''The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRole"))

    @execution_role.setter
    def execution_role(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94668d5e5e8eb55befbec215426086ba0771bd0ba96fb3d147c8a3a31346c1b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRole", value)

    @builtins.property
    @jsii.member(jsii_name="imageRecipeArn")
    def image_recipe_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the image recipe that defines how images are configured, tested, and assessed.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageRecipeArn"))

    @image_recipe_arn.setter
    def image_recipe_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__308fe5eed4210d0740b5702c5e8451b42918877aa2da6ce7940407e47733f736)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageRecipeArn", value)

    @builtins.property
    @jsii.member(jsii_name="imageScanningConfiguration")
    def image_scanning_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImage.ImageScanningConfigurationProperty"]]:
        '''Contains settings for vulnerability scans.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImage.ImageScanningConfigurationProperty"]], jsii.get(self, "imageScanningConfiguration"))

    @image_scanning_configuration.setter
    def image_scanning_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImage.ImageScanningConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4b9045c9ec605b9ea33dd14470f4bb513ecf0e38fc4830ac2ce68670a13c7e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageScanningConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="imageTestsConfiguration")
    def image_tests_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImage.ImageTestsConfigurationProperty"]]:
        '''The image tests configuration of the image.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImage.ImageTestsConfigurationProperty"]], jsii.get(self, "imageTestsConfiguration"))

    @image_tests_configuration.setter
    def image_tests_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImage.ImageTestsConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e66513eb336b5e3ebc869a424fc1c9d0df46865060b926ea955e8a9df5c29efa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageTestsConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags of the image.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0e6ba55682dabdf30b5bb38534688ff3dbd8c6a8044f77eb6180bb8d815ceb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="workflows")
    def workflows(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnImage.WorkflowConfigurationProperty"]]]]:
        '''Contains an array of workflow configuration objects.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnImage.WorkflowConfigurationProperty"]]]], jsii.get(self, "workflows"))

    @workflows.setter
    def workflows(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnImage.WorkflowConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97523463f160d96768440c69c3873ddb86b0d5ac22775529d935489f314a6737)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workflows", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnImage.EcrConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_tags": "containerTags",
            "repository_name": "repositoryName",
        },
    )
    class EcrConfigurationProperty:
        def __init__(
            self,
            *,
            container_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
            repository_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Settings that Image Builder uses to configure the ECR repository and the output container images that Amazon Inspector scans.

            :param container_tags: Tags for Image Builder to apply to the output container image that &INS; scans. Tags can help you identify and manage your scanned images.
            :param repository_name: The name of the container repository that Amazon Inspector scans to identify findings for your container images. The name includes the path for the repository location. If you don’t provide this information, Image Builder creates a repository in your account named ``image-builder-image-scanning-repository`` for vulnerability scans of your output container images.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-ecrconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                ecr_configuration_property = imagebuilder.CfnImage.EcrConfigurationProperty(
                    container_tags=["containerTags"],
                    repository_name="repositoryName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8e752dc7f51b470c209f9741b4ee9c9b1b8ab926ba9ba46ae3160a1876f4c556)
                check_type(argname="argument container_tags", value=container_tags, expected_type=type_hints["container_tags"])
                check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if container_tags is not None:
                self._values["container_tags"] = container_tags
            if repository_name is not None:
                self._values["repository_name"] = repository_name

        @builtins.property
        def container_tags(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Tags for Image Builder to apply to the output container image that &INS;

            scans. Tags can help you identify and manage your scanned images.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-ecrconfiguration.html#cfn-imagebuilder-image-ecrconfiguration-containertags
            '''
            result = self._values.get("container_tags")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def repository_name(self) -> typing.Optional[builtins.str]:
            '''The name of the container repository that Amazon Inspector scans to identify findings for your container images.

            The name includes the path for the repository location. If you don’t provide this information, Image Builder creates a repository in your account named ``image-builder-image-scanning-repository`` for vulnerability scans of your output container images.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-ecrconfiguration.html#cfn-imagebuilder-image-ecrconfiguration-repositoryname
            '''
            result = self._values.get("repository_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EcrConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnImage.ImageScanningConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ecr_configuration": "ecrConfiguration",
            "image_scanning_enabled": "imageScanningEnabled",
        },
    )
    class ImageScanningConfigurationProperty:
        def __init__(
            self,
            *,
            ecr_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnImage.EcrConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            image_scanning_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Contains settings for Image Builder image resource and container image scans.

            :param ecr_configuration: Contains Amazon ECR settings for vulnerability scans.
            :param image_scanning_enabled: A setting that indicates whether Image Builder keeps a snapshot of the vulnerability scans that Amazon Inspector runs against the build instance when you create a new image.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-imagescanningconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                image_scanning_configuration_property = imagebuilder.CfnImage.ImageScanningConfigurationProperty(
                    ecr_configuration=imagebuilder.CfnImage.EcrConfigurationProperty(
                        container_tags=["containerTags"],
                        repository_name="repositoryName"
                    ),
                    image_scanning_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__155636d4b270ff858336d445a5c3a434623faaa989317a61b024d7142948911e)
                check_type(argname="argument ecr_configuration", value=ecr_configuration, expected_type=type_hints["ecr_configuration"])
                check_type(argname="argument image_scanning_enabled", value=image_scanning_enabled, expected_type=type_hints["image_scanning_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ecr_configuration is not None:
                self._values["ecr_configuration"] = ecr_configuration
            if image_scanning_enabled is not None:
                self._values["image_scanning_enabled"] = image_scanning_enabled

        @builtins.property
        def ecr_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImage.EcrConfigurationProperty"]]:
            '''Contains Amazon ECR settings for vulnerability scans.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-imagescanningconfiguration.html#cfn-imagebuilder-image-imagescanningconfiguration-ecrconfiguration
            '''
            result = self._values.get("ecr_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImage.EcrConfigurationProperty"]], result)

        @builtins.property
        def image_scanning_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A setting that indicates whether Image Builder keeps a snapshot of the vulnerability scans that Amazon Inspector runs against the build instance when you create a new image.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-imagescanningconfiguration.html#cfn-imagebuilder-image-imagescanningconfiguration-imagescanningenabled
            '''
            result = self._values.get("image_scanning_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageScanningConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnImage.ImageTestsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image_tests_enabled": "imageTestsEnabled",
            "timeout_minutes": "timeoutMinutes",
        },
    )
    class ImageTestsConfigurationProperty:
        def __init__(
            self,
            *,
            image_tests_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            timeout_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''When you create an image or container recipe with Image Builder , you can add the build or test components that are used to create the final image.

            You must have at least one build component to create a recipe, but test components are not required. If you have added tests, they run after the image is created, to ensure that the target image is functional and can be used reliably for launching Amazon EC2 instances.

            :param image_tests_enabled: Determines if tests should run after building the image. Image Builder defaults to enable tests to run following the image build, before image distribution.
            :param timeout_minutes: The maximum time in minutes that tests are permitted to run. .. epigraph:: The timeoutMinutes attribute is not currently active. This value is ignored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-imagetestsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                image_tests_configuration_property = imagebuilder.CfnImage.ImageTestsConfigurationProperty(
                    image_tests_enabled=False,
                    timeout_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e8cfede11f4b11fc577c8fddf9438af7db50acddcb364073adeaf606a8eeb506)
                check_type(argname="argument image_tests_enabled", value=image_tests_enabled, expected_type=type_hints["image_tests_enabled"])
                check_type(argname="argument timeout_minutes", value=timeout_minutes, expected_type=type_hints["timeout_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if image_tests_enabled is not None:
                self._values["image_tests_enabled"] = image_tests_enabled
            if timeout_minutes is not None:
                self._values["timeout_minutes"] = timeout_minutes

        @builtins.property
        def image_tests_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Determines if tests should run after building the image.

            Image Builder defaults to enable tests to run following the image build, before image distribution.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-imagetestsconfiguration.html#cfn-imagebuilder-image-imagetestsconfiguration-imagetestsenabled
            '''
            result = self._values.get("image_tests_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def timeout_minutes(self) -> typing.Optional[jsii.Number]:
            '''The maximum time in minutes that tests are permitted to run.

            .. epigraph::

               The timeoutMinutes attribute is not currently active. This value is ignored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-imagetestsconfiguration.html#cfn-imagebuilder-image-imagetestsconfiguration-timeoutminutes
            '''
            result = self._values.get("timeout_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageTestsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnImage.WorkflowConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "on_failure": "onFailure",
            "parallel_group": "parallelGroup",
            "parameters": "parameters",
            "workflow_arn": "workflowArn",
        },
    )
    class WorkflowConfigurationProperty:
        def __init__(
            self,
            *,
            on_failure: typing.Optional[builtins.str] = None,
            parallel_group: typing.Optional[builtins.str] = None,
            parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnImage.WorkflowParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            workflow_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains control settings and configurable inputs for a workflow resource.

            :param on_failure: The action to take if the workflow fails.
            :param parallel_group: Test workflows are defined within named runtime groups called parallel groups. The parallel group is the named group that contains this test workflow. Test workflows within a parallel group can run at the same time. Image Builder starts up to five test workflows in the group at the same time, and starts additional workflows as others complete, until all workflows in the group have completed. This field only applies for test workflows.
            :param parameters: Contains parameter values for each of the parameters that the workflow document defined for the workflow resource.
            :param workflow_arn: The Amazon Resource Name (ARN) of the workflow resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-workflowconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                workflow_configuration_property = imagebuilder.CfnImage.WorkflowConfigurationProperty(
                    on_failure="onFailure",
                    parallel_group="parallelGroup",
                    parameters=[imagebuilder.CfnImage.WorkflowParameterProperty(
                        name="name",
                        value=["value"]
                    )],
                    workflow_arn="workflowArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a82febc1a7fafa923553117d043e1c9475f024e84431a24b2b8a4d66c3a73ed6)
                check_type(argname="argument on_failure", value=on_failure, expected_type=type_hints["on_failure"])
                check_type(argname="argument parallel_group", value=parallel_group, expected_type=type_hints["parallel_group"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
                check_type(argname="argument workflow_arn", value=workflow_arn, expected_type=type_hints["workflow_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if on_failure is not None:
                self._values["on_failure"] = on_failure
            if parallel_group is not None:
                self._values["parallel_group"] = parallel_group
            if parameters is not None:
                self._values["parameters"] = parameters
            if workflow_arn is not None:
                self._values["workflow_arn"] = workflow_arn

        @builtins.property
        def on_failure(self) -> typing.Optional[builtins.str]:
            '''The action to take if the workflow fails.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-workflowconfiguration.html#cfn-imagebuilder-image-workflowconfiguration-onfailure
            '''
            result = self._values.get("on_failure")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parallel_group(self) -> typing.Optional[builtins.str]:
            '''Test workflows are defined within named runtime groups called parallel groups.

            The parallel group is the named group that contains this test workflow. Test workflows within a parallel group can run at the same time. Image Builder starts up to five test workflows in the group at the same time, and starts additional workflows as others complete, until all workflows in the group have completed. This field only applies for test workflows.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-workflowconfiguration.html#cfn-imagebuilder-image-workflowconfiguration-parallelgroup
            '''
            result = self._values.get("parallel_group")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnImage.WorkflowParameterProperty"]]]]:
            '''Contains parameter values for each of the parameters that the workflow document defined for the workflow resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-workflowconfiguration.html#cfn-imagebuilder-image-workflowconfiguration-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnImage.WorkflowParameterProperty"]]]], result)

        @builtins.property
        def workflow_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the workflow resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-workflowconfiguration.html#cfn-imagebuilder-image-workflowconfiguration-workflowarn
            '''
            result = self._values.get("workflow_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkflowConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnImage.WorkflowParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class WorkflowParameterProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            value: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Contains a key/value pair that sets the named workflow parameter.

            :param name: The name of the workflow parameter to set.
            :param value: Sets the value for the named workflow parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-workflowparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                workflow_parameter_property = imagebuilder.CfnImage.WorkflowParameterProperty(
                    name="name",
                    value=["value"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fd39ec0b160c618e3ecd8108c0d630fdf1cd5460552b39c91e63a7ddbf1f09b7)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the workflow parameter to set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-workflowparameter.html#cfn-imagebuilder-image-workflowparameter-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Sets the value for the named workflow parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-image-workflowparameter.html#cfn-imagebuilder-image-workflowparameter-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkflowParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnImagePipeline(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_imagebuilder.CfnImagePipeline",
):
    '''An image pipeline is the automation configuration for building secure OS images on AWS .

    The Image Builder image pipeline is associated with an image recipe that defines the build, validation, and test phases for an image build lifecycle. An image pipeline can be associated with an infrastructure configuration that defines where your image is built. You can define attributes, such as instance types, a subnet for your VPC, security groups, logging, and other infrastructure-related configurations. You can also associate your image pipeline with a distribution configuration to define how you would like to deploy your image.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html
    :cloudformationResource: AWS::ImageBuilder::ImagePipeline
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_imagebuilder as imagebuilder
        
        cfn_image_pipeline = imagebuilder.CfnImagePipeline(self, "MyCfnImagePipeline",
            infrastructure_configuration_arn="infrastructureConfigurationArn",
            name="name",
        
            # the properties below are optional
            container_recipe_arn="containerRecipeArn",
            description="description",
            distribution_configuration_arn="distributionConfigurationArn",
            enhanced_image_metadata_enabled=False,
            execution_role="executionRole",
            image_recipe_arn="imageRecipeArn",
            image_scanning_configuration=imagebuilder.CfnImagePipeline.ImageScanningConfigurationProperty(
                ecr_configuration=imagebuilder.CfnImagePipeline.EcrConfigurationProperty(
                    container_tags=["containerTags"],
                    repository_name="repositoryName"
                ),
                image_scanning_enabled=False
            ),
            image_tests_configuration=imagebuilder.CfnImagePipeline.ImageTestsConfigurationProperty(
                image_tests_enabled=False,
                timeout_minutes=123
            ),
            schedule=imagebuilder.CfnImagePipeline.ScheduleProperty(
                pipeline_execution_start_condition="pipelineExecutionStartCondition",
                schedule_expression="scheduleExpression"
            ),
            status="status",
            tags={
                "tags_key": "tags"
            },
            workflows=[imagebuilder.CfnImagePipeline.WorkflowConfigurationProperty(
                on_failure="onFailure",
                parallel_group="parallelGroup",
                parameters=[imagebuilder.CfnImagePipeline.WorkflowParameterProperty(
                    name="name",
                    value=["value"]
                )],
                workflow_arn="workflowArn"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        infrastructure_configuration_arn: builtins.str,
        name: builtins.str,
        container_recipe_arn: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        distribution_configuration_arn: typing.Optional[builtins.str] = None,
        enhanced_image_metadata_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        execution_role: typing.Optional[builtins.str] = None,
        image_recipe_arn: typing.Optional[builtins.str] = None,
        image_scanning_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnImagePipeline.ImageScanningConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        image_tests_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnImagePipeline.ImageTestsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnImagePipeline.ScheduleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        workflows: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnImagePipeline.WorkflowConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param infrastructure_configuration_arn: The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.
        :param name: The name of the image pipeline.
        :param container_recipe_arn: The Amazon Resource Name (ARN) of the container recipe that is used for this pipeline.
        :param description: The description of this image pipeline.
        :param distribution_configuration_arn: The Amazon Resource Name (ARN) of the distribution configuration associated with this image pipeline.
        :param enhanced_image_metadata_enabled: Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.
        :param execution_role: The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.
        :param image_recipe_arn: The Amazon Resource Name (ARN) of the image recipe associated with this image pipeline.
        :param image_scanning_configuration: Contains settings for vulnerability scans.
        :param image_tests_configuration: The configuration of the image tests that run after image creation to ensure the quality of the image that was created.
        :param schedule: The schedule of the image pipeline. A schedule configures how often and when a pipeline automatically creates a new image.
        :param status: The status of the image pipeline.
        :param tags: The tags of this image pipeline.
        :param workflows: Contains the workflows that run for the image pipeline.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2d099702ab4ebcb03c34ae00fedabfa81a0c5d3662aa1605c47ff1fcaf0b3a5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnImagePipelineProps(
            infrastructure_configuration_arn=infrastructure_configuration_arn,
            name=name,
            container_recipe_arn=container_recipe_arn,
            description=description,
            distribution_configuration_arn=distribution_configuration_arn,
            enhanced_image_metadata_enabled=enhanced_image_metadata_enabled,
            execution_role=execution_role,
            image_recipe_arn=image_recipe_arn,
            image_scanning_configuration=image_scanning_configuration,
            image_tests_configuration=image_tests_configuration,
            schedule=schedule,
            status=status,
            tags=tags,
            workflows=workflows,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8446f898a5728a2569b09b248ec039f33570944e39527609ca77ad743aa2981)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cdf805d788cd08883285d15aaa10bc7ba4e53741d409a94e68aed68476e684ce)
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
        '''Returns the Amazon Resource Name (ARN) of the image pipeline.

        For example, ``arn:aws:imagebuilder:us-west-2:123456789012:image-pipeline/mywindows2016pipeline`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''Returns the name of the image pipeline.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

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
    @jsii.member(jsii_name="infrastructureConfigurationArn")
    def infrastructure_configuration_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.'''
        return typing.cast(builtins.str, jsii.get(self, "infrastructureConfigurationArn"))

    @infrastructure_configuration_arn.setter
    def infrastructure_configuration_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6e5ee80f47b2929d2902efd995e0248d5c8ae9ed8dbf8d1e4fb71b7855eabb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "infrastructureConfigurationArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the image pipeline.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfcf09da283c32d27a69667105a1cc2b1df47359866f14696d1326d14bde2b6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="containerRecipeArn")
    def container_recipe_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the container recipe that is used for this pipeline.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerRecipeArn"))

    @container_recipe_arn.setter
    def container_recipe_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f690c089494ff15e372c4f0a35406b7a51b38c81b470cac3aa12ba03f2e931a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerRecipeArn", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of this image pipeline.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78b1f1bb0cc881de12c4611c1d5f8f4cff0231dd64a754971cca27ad89c67de1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="distributionConfigurationArn")
    def distribution_configuration_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the distribution configuration associated with this image pipeline.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "distributionConfigurationArn"))

    @distribution_configuration_arn.setter
    def distribution_configuration_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b07039612cc24dd193ca16223d4b76d3c790b575da52c3cdf9cfc191185287c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "distributionConfigurationArn", value)

    @builtins.property
    @jsii.member(jsii_name="enhancedImageMetadataEnabled")
    def enhanced_image_metadata_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Collects additional information about the image being created, including the operating system (OS) version and package list.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enhancedImageMetadataEnabled"))

    @enhanced_image_metadata_enabled.setter
    def enhanced_image_metadata_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca199afdbf91ba45c1ad064f501dfd9423062e198e14171ce04f43dd1f06dd41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enhancedImageMetadataEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="executionRole")
    def execution_role(self) -> typing.Optional[builtins.str]:
        '''The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRole"))

    @execution_role.setter
    def execution_role(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ebcf34a24070ac97fff298c2904bf78391a1a430eba771320445f80a0ff1f2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRole", value)

    @builtins.property
    @jsii.member(jsii_name="imageRecipeArn")
    def image_recipe_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the image recipe associated with this image pipeline.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageRecipeArn"))

    @image_recipe_arn.setter
    def image_recipe_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87996b3149c3f25f36e8d94641a0031c8b619b9cf13e699704fbe22cc370d491)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageRecipeArn", value)

    @builtins.property
    @jsii.member(jsii_name="imageScanningConfiguration")
    def image_scanning_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImagePipeline.ImageScanningConfigurationProperty"]]:
        '''Contains settings for vulnerability scans.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImagePipeline.ImageScanningConfigurationProperty"]], jsii.get(self, "imageScanningConfiguration"))

    @image_scanning_configuration.setter
    def image_scanning_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImagePipeline.ImageScanningConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0daaa16e9e563843b4889c318a714595d70349ae6d61ed80bf9f14b99f18be56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageScanningConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="imageTestsConfiguration")
    def image_tests_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImagePipeline.ImageTestsConfigurationProperty"]]:
        '''The configuration of the image tests that run after image creation to ensure the quality of the image that was created.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImagePipeline.ImageTestsConfigurationProperty"]], jsii.get(self, "imageTestsConfiguration"))

    @image_tests_configuration.setter
    def image_tests_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImagePipeline.ImageTestsConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9e327e008ef0b95ddde8197947e86b8bc9160733d270caa11482a88db735cc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageTestsConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImagePipeline.ScheduleProperty"]]:
        '''The schedule of the image pipeline.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImagePipeline.ScheduleProperty"]], jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImagePipeline.ScheduleProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7493819df4798ffd45cd31ff99c66a5c22065a41d47c9c3792eaaf9d4c4150a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the image pipeline.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3ffb79c4adfe85e809f1adea3ddcdf54c817c4a4f4c97a2f65d9c38b4e0f38b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags of this image pipeline.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10f1255c06095afaded88e7544051acdac47218f9be5e78474eeaaedafede76f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="workflows")
    def workflows(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnImagePipeline.WorkflowConfigurationProperty"]]]]:
        '''Contains the workflows that run for the image pipeline.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnImagePipeline.WorkflowConfigurationProperty"]]]], jsii.get(self, "workflows"))

    @workflows.setter
    def workflows(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnImagePipeline.WorkflowConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d31373519ea07e5936785c1446524bda21756ca2eb6c12f87303f5a12dc18c4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workflows", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnImagePipeline.EcrConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_tags": "containerTags",
            "repository_name": "repositoryName",
        },
    )
    class EcrConfigurationProperty:
        def __init__(
            self,
            *,
            container_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
            repository_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Settings that Image Builder uses to configure the ECR repository and the output container images that Amazon Inspector scans.

            :param container_tags: Tags for Image Builder to apply to the output container image that &INS; scans. Tags can help you identify and manage your scanned images.
            :param repository_name: The name of the container repository that Amazon Inspector scans to identify findings for your container images. The name includes the path for the repository location. If you don’t provide this information, Image Builder creates a repository in your account named ``image-builder-image-scanning-repository`` for vulnerability scans of your output container images.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-ecrconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                ecr_configuration_property = imagebuilder.CfnImagePipeline.EcrConfigurationProperty(
                    container_tags=["containerTags"],
                    repository_name="repositoryName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1ad9ee4365967b325aac7636f417b9a691b4b50560fe8f594198933e7ed13aca)
                check_type(argname="argument container_tags", value=container_tags, expected_type=type_hints["container_tags"])
                check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if container_tags is not None:
                self._values["container_tags"] = container_tags
            if repository_name is not None:
                self._values["repository_name"] = repository_name

        @builtins.property
        def container_tags(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Tags for Image Builder to apply to the output container image that &INS;

            scans. Tags can help you identify and manage your scanned images.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-ecrconfiguration.html#cfn-imagebuilder-imagepipeline-ecrconfiguration-containertags
            '''
            result = self._values.get("container_tags")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def repository_name(self) -> typing.Optional[builtins.str]:
            '''The name of the container repository that Amazon Inspector scans to identify findings for your container images.

            The name includes the path for the repository location. If you don’t provide this information, Image Builder creates a repository in your account named ``image-builder-image-scanning-repository`` for vulnerability scans of your output container images.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-ecrconfiguration.html#cfn-imagebuilder-imagepipeline-ecrconfiguration-repositoryname
            '''
            result = self._values.get("repository_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EcrConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnImagePipeline.ImageScanningConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ecr_configuration": "ecrConfiguration",
            "image_scanning_enabled": "imageScanningEnabled",
        },
    )
    class ImageScanningConfigurationProperty:
        def __init__(
            self,
            *,
            ecr_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnImagePipeline.EcrConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            image_scanning_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Contains settings for Image Builder image resource and container image scans.

            :param ecr_configuration: Contains Amazon ECR settings for vulnerability scans.
            :param image_scanning_enabled: A setting that indicates whether Image Builder keeps a snapshot of the vulnerability scans that Amazon Inspector runs against the build instance when you create a new image.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagescanningconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                image_scanning_configuration_property = imagebuilder.CfnImagePipeline.ImageScanningConfigurationProperty(
                    ecr_configuration=imagebuilder.CfnImagePipeline.EcrConfigurationProperty(
                        container_tags=["containerTags"],
                        repository_name="repositoryName"
                    ),
                    image_scanning_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8e9c4bcdf41e69c9224e93798644f93b8f44565c0bd7edb8e6b49dc0367bc5b6)
                check_type(argname="argument ecr_configuration", value=ecr_configuration, expected_type=type_hints["ecr_configuration"])
                check_type(argname="argument image_scanning_enabled", value=image_scanning_enabled, expected_type=type_hints["image_scanning_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ecr_configuration is not None:
                self._values["ecr_configuration"] = ecr_configuration
            if image_scanning_enabled is not None:
                self._values["image_scanning_enabled"] = image_scanning_enabled

        @builtins.property
        def ecr_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImagePipeline.EcrConfigurationProperty"]]:
            '''Contains Amazon ECR settings for vulnerability scans.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagescanningconfiguration.html#cfn-imagebuilder-imagepipeline-imagescanningconfiguration-ecrconfiguration
            '''
            result = self._values.get("ecr_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImagePipeline.EcrConfigurationProperty"]], result)

        @builtins.property
        def image_scanning_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A setting that indicates whether Image Builder keeps a snapshot of the vulnerability scans that Amazon Inspector runs against the build instance when you create a new image.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagescanningconfiguration.html#cfn-imagebuilder-imagepipeline-imagescanningconfiguration-imagescanningenabled
            '''
            result = self._values.get("image_scanning_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageScanningConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnImagePipeline.ImageTestsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image_tests_enabled": "imageTestsEnabled",
            "timeout_minutes": "timeoutMinutes",
        },
    )
    class ImageTestsConfigurationProperty:
        def __init__(
            self,
            *,
            image_tests_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            timeout_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''When you create an image or container recipe with Image Builder , you can add the build or test components that your image pipeline uses to create the final image.

            You must have at least one build component to create a recipe, but test components are not required. Your pipeline runs tests after it builds the image, to ensure that the target image is functional and can be used reliably for launching Amazon EC2 instances.

            :param image_tests_enabled: Defines if tests should be executed when building this image. For example, ``true`` or ``false`` .
            :param timeout_minutes: The maximum time in minutes that tests are permitted to run. .. epigraph:: The timeoutMinutes attribute is not currently active. This value is ignored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                image_tests_configuration_property = imagebuilder.CfnImagePipeline.ImageTestsConfigurationProperty(
                    image_tests_enabled=False,
                    timeout_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ae3643f34d20caf9e518f587e7eacbe6f2163c4d76025d717d8d8ea1b31feed6)
                check_type(argname="argument image_tests_enabled", value=image_tests_enabled, expected_type=type_hints["image_tests_enabled"])
                check_type(argname="argument timeout_minutes", value=timeout_minutes, expected_type=type_hints["timeout_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if image_tests_enabled is not None:
                self._values["image_tests_enabled"] = image_tests_enabled
            if timeout_minutes is not None:
                self._values["timeout_minutes"] = timeout_minutes

        @builtins.property
        def image_tests_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Defines if tests should be executed when building this image.

            For example, ``true`` or ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration.html#cfn-imagebuilder-imagepipeline-imagetestsconfiguration-imagetestsenabled
            '''
            result = self._values.get("image_tests_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def timeout_minutes(self) -> typing.Optional[jsii.Number]:
            '''The maximum time in minutes that tests are permitted to run.

            .. epigraph::

               The timeoutMinutes attribute is not currently active. This value is ignored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-imagetestsconfiguration.html#cfn-imagebuilder-imagepipeline-imagetestsconfiguration-timeoutminutes
            '''
            result = self._values.get("timeout_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageTestsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnImagePipeline.ScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "pipeline_execution_start_condition": "pipelineExecutionStartCondition",
            "schedule_expression": "scheduleExpression",
        },
    )
    class ScheduleProperty:
        def __init__(
            self,
            *,
            pipeline_execution_start_condition: typing.Optional[builtins.str] = None,
            schedule_expression: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A schedule configures when and how often a pipeline will automatically create a new image.

            :param pipeline_execution_start_condition: The condition configures when the pipeline should trigger a new image build. When the ``pipelineExecutionStartCondition`` is set to ``EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE`` , and you use semantic version filters on the base image or components in your image recipe, Image Builder will build a new image only when there are new versions of the image or components in your recipe that match the semantic version filter. When it is set to ``EXPRESSION_MATCH_ONLY`` , it will build a new image every time the CRON expression matches the current time. For semantic version syntax, see `CreateComponent <https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateComponent.html>`_ in the *Image Builder API Reference* .
            :param schedule_expression: The cron expression determines how often EC2 Image Builder evaluates your ``pipelineExecutionStartCondition`` . For information on how to format a cron expression in Image Builder, see `Use cron expressions in EC2 Image Builder <https://docs.aws.amazon.com/imagebuilder/latest/userguide/image-builder-cron.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-schedule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                schedule_property = imagebuilder.CfnImagePipeline.ScheduleProperty(
                    pipeline_execution_start_condition="pipelineExecutionStartCondition",
                    schedule_expression="scheduleExpression"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__02783d051498bb630cd6a27d361c0750914a59f05623585e0808549e9248bae0)
                check_type(argname="argument pipeline_execution_start_condition", value=pipeline_execution_start_condition, expected_type=type_hints["pipeline_execution_start_condition"])
                check_type(argname="argument schedule_expression", value=schedule_expression, expected_type=type_hints["schedule_expression"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if pipeline_execution_start_condition is not None:
                self._values["pipeline_execution_start_condition"] = pipeline_execution_start_condition
            if schedule_expression is not None:
                self._values["schedule_expression"] = schedule_expression

        @builtins.property
        def pipeline_execution_start_condition(self) -> typing.Optional[builtins.str]:
            '''The condition configures when the pipeline should trigger a new image build.

            When the ``pipelineExecutionStartCondition`` is set to ``EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE`` , and you use semantic version filters on the base image or components in your image recipe, Image Builder will build a new image only when there are new versions of the image or components in your recipe that match the semantic version filter. When it is set to ``EXPRESSION_MATCH_ONLY`` , it will build a new image every time the CRON expression matches the current time. For semantic version syntax, see `CreateComponent <https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateComponent.html>`_ in the *Image Builder API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-schedule.html#cfn-imagebuilder-imagepipeline-schedule-pipelineexecutionstartcondition
            '''
            result = self._values.get("pipeline_execution_start_condition")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def schedule_expression(self) -> typing.Optional[builtins.str]:
            '''The cron expression determines how often EC2 Image Builder evaluates your ``pipelineExecutionStartCondition`` .

            For information on how to format a cron expression in Image Builder, see `Use cron expressions in EC2 Image Builder <https://docs.aws.amazon.com/imagebuilder/latest/userguide/image-builder-cron.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-schedule.html#cfn-imagebuilder-imagepipeline-schedule-scheduleexpression
            '''
            result = self._values.get("schedule_expression")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnImagePipeline.WorkflowConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "on_failure": "onFailure",
            "parallel_group": "parallelGroup",
            "parameters": "parameters",
            "workflow_arn": "workflowArn",
        },
    )
    class WorkflowConfigurationProperty:
        def __init__(
            self,
            *,
            on_failure: typing.Optional[builtins.str] = None,
            parallel_group: typing.Optional[builtins.str] = None,
            parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnImagePipeline.WorkflowParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            workflow_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains control settings and configurable inputs for a workflow resource.

            :param on_failure: The action to take if the workflow fails.
            :param parallel_group: Test workflows are defined within named runtime groups called parallel groups. The parallel group is the named group that contains this test workflow. Test workflows within a parallel group can run at the same time. Image Builder starts up to five test workflows in the group at the same time, and starts additional workflows as others complete, until all workflows in the group have completed. This field only applies for test workflows.
            :param parameters: Contains parameter values for each of the parameters that the workflow document defined for the workflow resource.
            :param workflow_arn: The Amazon Resource Name (ARN) of the workflow resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-workflowconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                workflow_configuration_property = imagebuilder.CfnImagePipeline.WorkflowConfigurationProperty(
                    on_failure="onFailure",
                    parallel_group="parallelGroup",
                    parameters=[imagebuilder.CfnImagePipeline.WorkflowParameterProperty(
                        name="name",
                        value=["value"]
                    )],
                    workflow_arn="workflowArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__665a1259d83ae867bae960e30b1d2c041292af4f49417c7f7eca3bd35857c4a3)
                check_type(argname="argument on_failure", value=on_failure, expected_type=type_hints["on_failure"])
                check_type(argname="argument parallel_group", value=parallel_group, expected_type=type_hints["parallel_group"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
                check_type(argname="argument workflow_arn", value=workflow_arn, expected_type=type_hints["workflow_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if on_failure is not None:
                self._values["on_failure"] = on_failure
            if parallel_group is not None:
                self._values["parallel_group"] = parallel_group
            if parameters is not None:
                self._values["parameters"] = parameters
            if workflow_arn is not None:
                self._values["workflow_arn"] = workflow_arn

        @builtins.property
        def on_failure(self) -> typing.Optional[builtins.str]:
            '''The action to take if the workflow fails.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-workflowconfiguration.html#cfn-imagebuilder-imagepipeline-workflowconfiguration-onfailure
            '''
            result = self._values.get("on_failure")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parallel_group(self) -> typing.Optional[builtins.str]:
            '''Test workflows are defined within named runtime groups called parallel groups.

            The parallel group is the named group that contains this test workflow. Test workflows within a parallel group can run at the same time. Image Builder starts up to five test workflows in the group at the same time, and starts additional workflows as others complete, until all workflows in the group have completed. This field only applies for test workflows.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-workflowconfiguration.html#cfn-imagebuilder-imagepipeline-workflowconfiguration-parallelgroup
            '''
            result = self._values.get("parallel_group")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnImagePipeline.WorkflowParameterProperty"]]]]:
            '''Contains parameter values for each of the parameters that the workflow document defined for the workflow resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-workflowconfiguration.html#cfn-imagebuilder-imagepipeline-workflowconfiguration-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnImagePipeline.WorkflowParameterProperty"]]]], result)

        @builtins.property
        def workflow_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the workflow resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-workflowconfiguration.html#cfn-imagebuilder-imagepipeline-workflowconfiguration-workflowarn
            '''
            result = self._values.get("workflow_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkflowConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnImagePipeline.WorkflowParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class WorkflowParameterProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            value: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Contains a key/value pair that sets the named workflow parameter.

            :param name: The name of the workflow parameter to set.
            :param value: Sets the value for the named workflow parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-workflowparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                workflow_parameter_property = imagebuilder.CfnImagePipeline.WorkflowParameterProperty(
                    name="name",
                    value=["value"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2e3c12bbd170116ab79a812e4141a317f3b456ad0a64acefae39ebbdf20aa068)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the workflow parameter to set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-workflowparameter.html#cfn-imagebuilder-imagepipeline-workflowparameter-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Sets the value for the named workflow parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagepipeline-workflowparameter.html#cfn-imagebuilder-imagepipeline-workflowparameter-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkflowParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_imagebuilder.CfnImagePipelineProps",
    jsii_struct_bases=[],
    name_mapping={
        "infrastructure_configuration_arn": "infrastructureConfigurationArn",
        "name": "name",
        "container_recipe_arn": "containerRecipeArn",
        "description": "description",
        "distribution_configuration_arn": "distributionConfigurationArn",
        "enhanced_image_metadata_enabled": "enhancedImageMetadataEnabled",
        "execution_role": "executionRole",
        "image_recipe_arn": "imageRecipeArn",
        "image_scanning_configuration": "imageScanningConfiguration",
        "image_tests_configuration": "imageTestsConfiguration",
        "schedule": "schedule",
        "status": "status",
        "tags": "tags",
        "workflows": "workflows",
    },
)
class CfnImagePipelineProps:
    def __init__(
        self,
        *,
        infrastructure_configuration_arn: builtins.str,
        name: builtins.str,
        container_recipe_arn: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        distribution_configuration_arn: typing.Optional[builtins.str] = None,
        enhanced_image_metadata_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        execution_role: typing.Optional[builtins.str] = None,
        image_recipe_arn: typing.Optional[builtins.str] = None,
        image_scanning_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImagePipeline.ImageScanningConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        image_tests_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImagePipeline.ImageTestsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImagePipeline.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        workflows: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImagePipeline.WorkflowConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnImagePipeline``.

        :param infrastructure_configuration_arn: The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.
        :param name: The name of the image pipeline.
        :param container_recipe_arn: The Amazon Resource Name (ARN) of the container recipe that is used for this pipeline.
        :param description: The description of this image pipeline.
        :param distribution_configuration_arn: The Amazon Resource Name (ARN) of the distribution configuration associated with this image pipeline.
        :param enhanced_image_metadata_enabled: Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.
        :param execution_role: The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.
        :param image_recipe_arn: The Amazon Resource Name (ARN) of the image recipe associated with this image pipeline.
        :param image_scanning_configuration: Contains settings for vulnerability scans.
        :param image_tests_configuration: The configuration of the image tests that run after image creation to ensure the quality of the image that was created.
        :param schedule: The schedule of the image pipeline. A schedule configures how often and when a pipeline automatically creates a new image.
        :param status: The status of the image pipeline.
        :param tags: The tags of this image pipeline.
        :param workflows: Contains the workflows that run for the image pipeline.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_imagebuilder as imagebuilder
            
            cfn_image_pipeline_props = imagebuilder.CfnImagePipelineProps(
                infrastructure_configuration_arn="infrastructureConfigurationArn",
                name="name",
            
                # the properties below are optional
                container_recipe_arn="containerRecipeArn",
                description="description",
                distribution_configuration_arn="distributionConfigurationArn",
                enhanced_image_metadata_enabled=False,
                execution_role="executionRole",
                image_recipe_arn="imageRecipeArn",
                image_scanning_configuration=imagebuilder.CfnImagePipeline.ImageScanningConfigurationProperty(
                    ecr_configuration=imagebuilder.CfnImagePipeline.EcrConfigurationProperty(
                        container_tags=["containerTags"],
                        repository_name="repositoryName"
                    ),
                    image_scanning_enabled=False
                ),
                image_tests_configuration=imagebuilder.CfnImagePipeline.ImageTestsConfigurationProperty(
                    image_tests_enabled=False,
                    timeout_minutes=123
                ),
                schedule=imagebuilder.CfnImagePipeline.ScheduleProperty(
                    pipeline_execution_start_condition="pipelineExecutionStartCondition",
                    schedule_expression="scheduleExpression"
                ),
                status="status",
                tags={
                    "tags_key": "tags"
                },
                workflows=[imagebuilder.CfnImagePipeline.WorkflowConfigurationProperty(
                    on_failure="onFailure",
                    parallel_group="parallelGroup",
                    parameters=[imagebuilder.CfnImagePipeline.WorkflowParameterProperty(
                        name="name",
                        value=["value"]
                    )],
                    workflow_arn="workflowArn"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95f10c4451c6bf3f2cf15951831cd372e35975262c0be294c1ae7c774045ad9b)
            check_type(argname="argument infrastructure_configuration_arn", value=infrastructure_configuration_arn, expected_type=type_hints["infrastructure_configuration_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument container_recipe_arn", value=container_recipe_arn, expected_type=type_hints["container_recipe_arn"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument distribution_configuration_arn", value=distribution_configuration_arn, expected_type=type_hints["distribution_configuration_arn"])
            check_type(argname="argument enhanced_image_metadata_enabled", value=enhanced_image_metadata_enabled, expected_type=type_hints["enhanced_image_metadata_enabled"])
            check_type(argname="argument execution_role", value=execution_role, expected_type=type_hints["execution_role"])
            check_type(argname="argument image_recipe_arn", value=image_recipe_arn, expected_type=type_hints["image_recipe_arn"])
            check_type(argname="argument image_scanning_configuration", value=image_scanning_configuration, expected_type=type_hints["image_scanning_configuration"])
            check_type(argname="argument image_tests_configuration", value=image_tests_configuration, expected_type=type_hints["image_tests_configuration"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument workflows", value=workflows, expected_type=type_hints["workflows"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "infrastructure_configuration_arn": infrastructure_configuration_arn,
            "name": name,
        }
        if container_recipe_arn is not None:
            self._values["container_recipe_arn"] = container_recipe_arn
        if description is not None:
            self._values["description"] = description
        if distribution_configuration_arn is not None:
            self._values["distribution_configuration_arn"] = distribution_configuration_arn
        if enhanced_image_metadata_enabled is not None:
            self._values["enhanced_image_metadata_enabled"] = enhanced_image_metadata_enabled
        if execution_role is not None:
            self._values["execution_role"] = execution_role
        if image_recipe_arn is not None:
            self._values["image_recipe_arn"] = image_recipe_arn
        if image_scanning_configuration is not None:
            self._values["image_scanning_configuration"] = image_scanning_configuration
        if image_tests_configuration is not None:
            self._values["image_tests_configuration"] = image_tests_configuration
        if schedule is not None:
            self._values["schedule"] = schedule
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags
        if workflows is not None:
            self._values["workflows"] = workflows

    @builtins.property
    def infrastructure_configuration_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the infrastructure configuration associated with this image pipeline.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-infrastructureconfigurationarn
        '''
        result = self._values.get("infrastructure_configuration_arn")
        assert result is not None, "Required property 'infrastructure_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the image pipeline.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_recipe_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the container recipe that is used for this pipeline.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-containerrecipearn
        '''
        result = self._values.get("container_recipe_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of this image pipeline.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def distribution_configuration_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the distribution configuration associated with this image pipeline.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-distributionconfigurationarn
        '''
        result = self._values.get("distribution_configuration_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enhanced_image_metadata_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Collects additional information about the image being created, including the operating system (OS) version and package list.

        This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-enhancedimagemetadataenabled
        '''
        result = self._values.get("enhanced_image_metadata_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def execution_role(self) -> typing.Optional[builtins.str]:
        '''The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-executionrole
        '''
        result = self._values.get("execution_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_recipe_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the image recipe associated with this image pipeline.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-imagerecipearn
        '''
        result = self._values.get("image_recipe_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_scanning_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnImagePipeline.ImageScanningConfigurationProperty]]:
        '''Contains settings for vulnerability scans.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-imagescanningconfiguration
        '''
        result = self._values.get("image_scanning_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnImagePipeline.ImageScanningConfigurationProperty]], result)

    @builtins.property
    def image_tests_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnImagePipeline.ImageTestsConfigurationProperty]]:
        '''The configuration of the image tests that run after image creation to ensure the quality of the image that was created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-imagetestsconfiguration
        '''
        result = self._values.get("image_tests_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnImagePipeline.ImageTestsConfigurationProperty]], result)

    @builtins.property
    def schedule(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnImagePipeline.ScheduleProperty]]:
        '''The schedule of the image pipeline.

        A schedule configures how often and when a pipeline automatically creates a new image.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-schedule
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnImagePipeline.ScheduleProperty]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the image pipeline.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags of this image pipeline.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def workflows(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnImagePipeline.WorkflowConfigurationProperty]]]]:
        '''Contains the workflows that run for the image pipeline.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.html#cfn-imagebuilder-imagepipeline-workflows
        '''
        result = self._values.get("workflows")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnImagePipeline.WorkflowConfigurationProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnImagePipelineProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_imagebuilder.CfnImageProps",
    jsii_struct_bases=[],
    name_mapping={
        "infrastructure_configuration_arn": "infrastructureConfigurationArn",
        "container_recipe_arn": "containerRecipeArn",
        "distribution_configuration_arn": "distributionConfigurationArn",
        "enhanced_image_metadata_enabled": "enhancedImageMetadataEnabled",
        "execution_role": "executionRole",
        "image_recipe_arn": "imageRecipeArn",
        "image_scanning_configuration": "imageScanningConfiguration",
        "image_tests_configuration": "imageTestsConfiguration",
        "tags": "tags",
        "workflows": "workflows",
    },
)
class CfnImageProps:
    def __init__(
        self,
        *,
        infrastructure_configuration_arn: builtins.str,
        container_recipe_arn: typing.Optional[builtins.str] = None,
        distribution_configuration_arn: typing.Optional[builtins.str] = None,
        enhanced_image_metadata_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        execution_role: typing.Optional[builtins.str] = None,
        image_recipe_arn: typing.Optional[builtins.str] = None,
        image_scanning_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImage.ImageScanningConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        image_tests_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImage.ImageTestsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        workflows: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImage.WorkflowConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnImage``.

        :param infrastructure_configuration_arn: The Amazon Resource Name (ARN) of the infrastructure configuration that defines the environment in which your image will be built and tested.
        :param container_recipe_arn: The Amazon Resource Name (ARN) of the container recipe that defines how images are configured and tested.
        :param distribution_configuration_arn: The Amazon Resource Name (ARN) of the distribution configuration that defines and configures the outputs of your pipeline.
        :param enhanced_image_metadata_enabled: Collects additional information about the image being created, including the operating system (OS) version and package list. This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.
        :param execution_role: The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.
        :param image_recipe_arn: The Amazon Resource Name (ARN) of the image recipe that defines how images are configured, tested, and assessed.
        :param image_scanning_configuration: Contains settings for vulnerability scans.
        :param image_tests_configuration: The image tests configuration of the image.
        :param tags: The tags of the image.
        :param workflows: Contains an array of workflow configuration objects.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_imagebuilder as imagebuilder
            
            cfn_image_props = imagebuilder.CfnImageProps(
                infrastructure_configuration_arn="infrastructureConfigurationArn",
            
                # the properties below are optional
                container_recipe_arn="containerRecipeArn",
                distribution_configuration_arn="distributionConfigurationArn",
                enhanced_image_metadata_enabled=False,
                execution_role="executionRole",
                image_recipe_arn="imageRecipeArn",
                image_scanning_configuration=imagebuilder.CfnImage.ImageScanningConfigurationProperty(
                    ecr_configuration=imagebuilder.CfnImage.EcrConfigurationProperty(
                        container_tags=["containerTags"],
                        repository_name="repositoryName"
                    ),
                    image_scanning_enabled=False
                ),
                image_tests_configuration=imagebuilder.CfnImage.ImageTestsConfigurationProperty(
                    image_tests_enabled=False,
                    timeout_minutes=123
                ),
                tags={
                    "tags_key": "tags"
                },
                workflows=[imagebuilder.CfnImage.WorkflowConfigurationProperty(
                    on_failure="onFailure",
                    parallel_group="parallelGroup",
                    parameters=[imagebuilder.CfnImage.WorkflowParameterProperty(
                        name="name",
                        value=["value"]
                    )],
                    workflow_arn="workflowArn"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f217922888735234464ee573256caba679b2c1215a99c91ad609c9c75d22d47)
            check_type(argname="argument infrastructure_configuration_arn", value=infrastructure_configuration_arn, expected_type=type_hints["infrastructure_configuration_arn"])
            check_type(argname="argument container_recipe_arn", value=container_recipe_arn, expected_type=type_hints["container_recipe_arn"])
            check_type(argname="argument distribution_configuration_arn", value=distribution_configuration_arn, expected_type=type_hints["distribution_configuration_arn"])
            check_type(argname="argument enhanced_image_metadata_enabled", value=enhanced_image_metadata_enabled, expected_type=type_hints["enhanced_image_metadata_enabled"])
            check_type(argname="argument execution_role", value=execution_role, expected_type=type_hints["execution_role"])
            check_type(argname="argument image_recipe_arn", value=image_recipe_arn, expected_type=type_hints["image_recipe_arn"])
            check_type(argname="argument image_scanning_configuration", value=image_scanning_configuration, expected_type=type_hints["image_scanning_configuration"])
            check_type(argname="argument image_tests_configuration", value=image_tests_configuration, expected_type=type_hints["image_tests_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument workflows", value=workflows, expected_type=type_hints["workflows"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "infrastructure_configuration_arn": infrastructure_configuration_arn,
        }
        if container_recipe_arn is not None:
            self._values["container_recipe_arn"] = container_recipe_arn
        if distribution_configuration_arn is not None:
            self._values["distribution_configuration_arn"] = distribution_configuration_arn
        if enhanced_image_metadata_enabled is not None:
            self._values["enhanced_image_metadata_enabled"] = enhanced_image_metadata_enabled
        if execution_role is not None:
            self._values["execution_role"] = execution_role
        if image_recipe_arn is not None:
            self._values["image_recipe_arn"] = image_recipe_arn
        if image_scanning_configuration is not None:
            self._values["image_scanning_configuration"] = image_scanning_configuration
        if image_tests_configuration is not None:
            self._values["image_tests_configuration"] = image_tests_configuration
        if tags is not None:
            self._values["tags"] = tags
        if workflows is not None:
            self._values["workflows"] = workflows

    @builtins.property
    def infrastructure_configuration_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the infrastructure configuration that defines the environment in which your image will be built and tested.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-infrastructureconfigurationarn
        '''
        result = self._values.get("infrastructure_configuration_arn")
        assert result is not None, "Required property 'infrastructure_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_recipe_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the container recipe that defines how images are configured and tested.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-containerrecipearn
        '''
        result = self._values.get("container_recipe_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def distribution_configuration_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the distribution configuration that defines and configures the outputs of your pipeline.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-distributionconfigurationarn
        '''
        result = self._values.get("distribution_configuration_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enhanced_image_metadata_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Collects additional information about the image being created, including the operating system (OS) version and package list.

        This information is used to enhance the overall experience of using EC2 Image Builder. Enabled by default.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-enhancedimagemetadataenabled
        '''
        result = self._values.get("enhanced_image_metadata_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def execution_role(self) -> typing.Optional[builtins.str]:
        '''The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to perform workflow actions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-executionrole
        '''
        result = self._values.get("execution_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_recipe_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the image recipe that defines how images are configured, tested, and assessed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-imagerecipearn
        '''
        result = self._values.get("image_recipe_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_scanning_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnImage.ImageScanningConfigurationProperty]]:
        '''Contains settings for vulnerability scans.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-imagescanningconfiguration
        '''
        result = self._values.get("image_scanning_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnImage.ImageScanningConfigurationProperty]], result)

    @builtins.property
    def image_tests_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnImage.ImageTestsConfigurationProperty]]:
        '''The image tests configuration of the image.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-imagetestsconfiguration
        '''
        result = self._values.get("image_tests_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnImage.ImageTestsConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags of the image.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def workflows(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnImage.WorkflowConfigurationProperty]]]]:
        '''Contains an array of workflow configuration objects.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-image.html#cfn-imagebuilder-image-workflows
        '''
        result = self._values.get("workflows")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnImage.WorkflowConfigurationProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnImageProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnImageRecipe(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_imagebuilder.CfnImageRecipe",
):
    '''An Image Builder image recipe is a document that defines the base image and the components to be applied to the base image to produce the desired configuration for the output image.

    You can use an image recipe to duplicate builds. Image Builder image recipes can be shared, branched, and edited using the console wizard, the AWS CLI , or the API. You can use image recipes with your version control software to maintain shareable versioned image recipes.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html
    :cloudformationResource: AWS::ImageBuilder::ImageRecipe
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_imagebuilder as imagebuilder
        
        cfn_image_recipe = imagebuilder.CfnImageRecipe(self, "MyCfnImageRecipe",
            components=[imagebuilder.CfnImageRecipe.ComponentConfigurationProperty(
                component_arn="componentArn",
                parameters=[imagebuilder.CfnImageRecipe.ComponentParameterProperty(
                    name="name",
                    value=["value"]
                )]
            )],
            name="name",
            parent_image="parentImage",
            version="version",
        
            # the properties below are optional
            additional_instance_configuration=imagebuilder.CfnImageRecipe.AdditionalInstanceConfigurationProperty(
                systems_manager_agent=imagebuilder.CfnImageRecipe.SystemsManagerAgentProperty(
                    uninstall_after_build=False
                ),
                user_data_override="userDataOverride"
            ),
            block_device_mappings=[imagebuilder.CfnImageRecipe.InstanceBlockDeviceMappingProperty(
                device_name="deviceName",
                ebs=imagebuilder.CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty(
                    delete_on_termination=False,
                    encrypted=False,
                    iops=123,
                    kms_key_id="kmsKeyId",
                    snapshot_id="snapshotId",
                    throughput=123,
                    volume_size=123,
                    volume_type="volumeType"
                ),
                no_device="noDevice",
                virtual_name="virtualName"
            )],
            description="description",
            tags={
                "tags_key": "tags"
            },
            working_directory="workingDirectory"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        components: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnImageRecipe.ComponentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        parent_image: builtins.str,
        version: builtins.str,
        additional_instance_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnImageRecipe.AdditionalInstanceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        block_device_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnImageRecipe.InstanceBlockDeviceMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param components: The components of the image recipe. Components are orchestration documents that define a sequence of steps for downloading, installing, configuring, and testing software packages. They also define validation and security hardening steps. A component is defined using a YAML document format.
        :param name: The name of the image recipe.
        :param parent_image: The parent image of the image recipe. The string must be either an Image ARN or an AMI ID.
        :param version: The semantic version of the image recipe.
        :param additional_instance_configuration: Before you create a new AMI, Image Builder launches temporary Amazon EC2 instances to build and test your image configuration. Instance configuration adds a layer of control over those instances. You can define settings and add scripts to run when an instance is launched from your AMI.
        :param block_device_mappings: The block device mappings to apply when creating images from this recipe.
        :param description: The description of the image recipe.
        :param tags: The tags of the image recipe.
        :param working_directory: The working directory to be used during build and test workflows.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b92e909d03413ceab5b5ff0737ae582bf88ebb71e7e89f62cc57922d15e14688)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnImageRecipeProps(
            components=components,
            name=name,
            parent_image=parent_image,
            version=version,
            additional_instance_configuration=additional_instance_configuration,
            block_device_mappings=block_device_mappings,
            description=description,
            tags=tags,
            working_directory=working_directory,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d29dc31863102f18f5de9644424c5516f4485067e44de21830a39789f498ba1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__33501f1fede0354860af9711623bf5d9a7cf482716f9a1ca43757a3dcf91988e)
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
        '''Returns the Amazon Resource Name (ARN) of the image recipe.

        For example, ``arn:aws:imagebuilder:us-east-1:123456789012:image-recipe/mybasicrecipe/2019.12.03`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''The name of the image recipe.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

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
    @jsii.member(jsii_name="components")
    def components(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnImageRecipe.ComponentConfigurationProperty"]]]:
        '''The components of the image recipe.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnImageRecipe.ComponentConfigurationProperty"]]], jsii.get(self, "components"))

    @components.setter
    def components(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnImageRecipe.ComponentConfigurationProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5aa78705ac6fd96606f64b6a20b05295ef53335ad8d08aa3a0a956ce040dd62c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "components", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the image recipe.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02513ed6c05b6aecc9c7c9494100db2c7a4dd5eecdafd9ed44b5ac5fe0cf5fce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parentImage")
    def parent_image(self) -> builtins.str:
        '''The parent image of the image recipe.'''
        return typing.cast(builtins.str, jsii.get(self, "parentImage"))

    @parent_image.setter
    def parent_image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47f2fc68afde57d2508c6a78ab44bf38f32703a4704e869ddfc9e1abda62a8fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parentImage", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''The semantic version of the image recipe.'''
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73fc08f00d9d100507462b08c6b2bbdf08927d138dd7cc3a56174082719ac0f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="additionalInstanceConfiguration")
    def additional_instance_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImageRecipe.AdditionalInstanceConfigurationProperty"]]:
        '''Before you create a new AMI, Image Builder launches temporary Amazon EC2 instances to build and test your image configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImageRecipe.AdditionalInstanceConfigurationProperty"]], jsii.get(self, "additionalInstanceConfiguration"))

    @additional_instance_configuration.setter
    def additional_instance_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImageRecipe.AdditionalInstanceConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcc3e434aa1a301be5e1a5341bc64287bfcf82761f08ef98de5711b1b1bc6038)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalInstanceConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="blockDeviceMappings")
    def block_device_mappings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnImageRecipe.InstanceBlockDeviceMappingProperty"]]]]:
        '''The block device mappings to apply when creating images from this recipe.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnImageRecipe.InstanceBlockDeviceMappingProperty"]]]], jsii.get(self, "blockDeviceMappings"))

    @block_device_mappings.setter
    def block_device_mappings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnImageRecipe.InstanceBlockDeviceMappingProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f9ee0bcfa7d5f48279416991e3a05c2143a695ca605b7c215eb5e8cc38d2174)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockDeviceMappings", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the image recipe.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f01685cf10dbac31ad7c61e710cacf41f2fc80e0f75749cd095d2cc67a293114)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags of the image recipe.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17b26e47cb85f6d4988562240bd59263533005f817aafcbcd75d58254cc7edad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="workingDirectory")
    def working_directory(self) -> typing.Optional[builtins.str]:
        '''The working directory to be used during build and test workflows.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workingDirectory"))

    @working_directory.setter
    def working_directory(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48af3414043e30c9e59d200f83f2c6ae4f17671a82842e7504894e55cd148e59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workingDirectory", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnImageRecipe.AdditionalInstanceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "systems_manager_agent": "systemsManagerAgent",
            "user_data_override": "userDataOverride",
        },
    )
    class AdditionalInstanceConfigurationProperty:
        def __init__(
            self,
            *,
            systems_manager_agent: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnImageRecipe.SystemsManagerAgentProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            user_data_override: typing.Optional[builtins.str] = None,
        ) -> None:
            '''In addition to your infrastructure configuration, these settings provide an extra layer of control over your build instances.

            You can also specify commands to run on launch for all of your build instances.

            Image Builder does not automatically install the Systems Manager agent on Windows instances. If your base image includes the Systems Manager agent, then the AMI that you create will also include the agent. For Linux instances, if the base image does not already include the Systems Manager agent, Image Builder installs it. For Linux instances where Image Builder installs the Systems Manager agent, you can choose whether to keep it for the AMI that you create.

            :param systems_manager_agent: Contains settings for the Systems Manager agent on your build instance.
            :param user_data_override: Use this property to provide commands or a command script to run when you launch your build instance. The userDataOverride property replaces any commands that Image Builder might have added to ensure that Systems Manager is installed on your Linux build instance. If you override the user data, make sure that you add commands to install Systems Manager, if it is not pre-installed on your base image. .. epigraph:: The user data is always base 64 encoded. For example, the following commands are encoded as ``IyEvYmluL2Jhc2gKbWtkaXIgLXAgL3Zhci9iYi8KdG91Y2ggL3Zhci$`` : *#!/bin/bash* mkdir -p /var/bb/ touch /var

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-additionalinstanceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                additional_instance_configuration_property = imagebuilder.CfnImageRecipe.AdditionalInstanceConfigurationProperty(
                    systems_manager_agent=imagebuilder.CfnImageRecipe.SystemsManagerAgentProperty(
                        uninstall_after_build=False
                    ),
                    user_data_override="userDataOverride"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9ca77073ea53566254c7a7a5d44918ec6646ad40315ed7ca9745e76d11503a2d)
                check_type(argname="argument systems_manager_agent", value=systems_manager_agent, expected_type=type_hints["systems_manager_agent"])
                check_type(argname="argument user_data_override", value=user_data_override, expected_type=type_hints["user_data_override"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if systems_manager_agent is not None:
                self._values["systems_manager_agent"] = systems_manager_agent
            if user_data_override is not None:
                self._values["user_data_override"] = user_data_override

        @builtins.property
        def systems_manager_agent(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImageRecipe.SystemsManagerAgentProperty"]]:
            '''Contains settings for the Systems Manager agent on your build instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-additionalinstanceconfiguration.html#cfn-imagebuilder-imagerecipe-additionalinstanceconfiguration-systemsmanageragent
            '''
            result = self._values.get("systems_manager_agent")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImageRecipe.SystemsManagerAgentProperty"]], result)

        @builtins.property
        def user_data_override(self) -> typing.Optional[builtins.str]:
            '''Use this property to provide commands or a command script to run when you launch your build instance.

            The userDataOverride property replaces any commands that Image Builder might have added to ensure that Systems Manager is installed on your Linux build instance. If you override the user data, make sure that you add commands to install Systems Manager, if it is not pre-installed on your base image.
            .. epigraph::

               The user data is always base 64 encoded. For example, the following commands are encoded as ``IyEvYmluL2Jhc2gKbWtkaXIgLXAgL3Zhci9iYi8KdG91Y2ggL3Zhci$`` :

               *#!/bin/bash*

               mkdir -p /var/bb/

               touch /var

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-additionalinstanceconfiguration.html#cfn-imagebuilder-imagerecipe-additionalinstanceconfiguration-userdataoverride
            '''
            result = self._values.get("user_data_override")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdditionalInstanceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnImageRecipe.ComponentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"component_arn": "componentArn", "parameters": "parameters"},
    )
    class ComponentConfigurationProperty:
        def __init__(
            self,
            *,
            component_arn: typing.Optional[builtins.str] = None,
            parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnImageRecipe.ComponentParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Configuration details of the component.

            :param component_arn: The Amazon Resource Name (ARN) of the component.
            :param parameters: A group of parameter settings that Image Builder uses to configure the component for a specific recipe.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                component_configuration_property = imagebuilder.CfnImageRecipe.ComponentConfigurationProperty(
                    component_arn="componentArn",
                    parameters=[imagebuilder.CfnImageRecipe.ComponentParameterProperty(
                        name="name",
                        value=["value"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3572edbb0a8e7d685c2a1b27e3b1ad62a69873f648cc201056f7b56000df8cbd)
                check_type(argname="argument component_arn", value=component_arn, expected_type=type_hints["component_arn"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if component_arn is not None:
                self._values["component_arn"] = component_arn
            if parameters is not None:
                self._values["parameters"] = parameters

        @builtins.property
        def component_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the component.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentconfiguration.html#cfn-imagebuilder-imagerecipe-componentconfiguration-componentarn
            '''
            result = self._values.get("component_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnImageRecipe.ComponentParameterProperty"]]]]:
            '''A group of parameter settings that Image Builder uses to configure the component for a specific recipe.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentconfiguration.html#cfn-imagebuilder-imagerecipe-componentconfiguration-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnImageRecipe.ComponentParameterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnImageRecipe.ComponentParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class ComponentParameterProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            value: typing.Sequence[builtins.str],
        ) -> None:
            '''Contains a key/value pair that sets the named component parameter.

            :param name: The name of the component parameter to set.
            :param value: Sets the value for the named component parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                component_parameter_property = imagebuilder.CfnImageRecipe.ComponentParameterProperty(
                    name="name",
                    value=["value"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__03682261f9797b7505c9117911d4b41776919fa663a3e5511922fc505c2d63de)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the component parameter to set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentparameter.html#cfn-imagebuilder-imagerecipe-componentparameter-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> typing.List[builtins.str]:
            '''Sets the value for the named component parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-componentparameter.html#cfn-imagebuilder-imagerecipe-componentparameter-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delete_on_termination": "deleteOnTermination",
            "encrypted": "encrypted",
            "iops": "iops",
            "kms_key_id": "kmsKeyId",
            "snapshot_id": "snapshotId",
            "throughput": "throughput",
            "volume_size": "volumeSize",
            "volume_type": "volumeType",
        },
    )
    class EbsInstanceBlockDeviceSpecificationProperty:
        def __init__(
            self,
            *,
            delete_on_termination: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            iops: typing.Optional[jsii.Number] = None,
            kms_key_id: typing.Optional[builtins.str] = None,
            snapshot_id: typing.Optional[builtins.str] = None,
            throughput: typing.Optional[jsii.Number] = None,
            volume_size: typing.Optional[jsii.Number] = None,
            volume_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The image recipe EBS instance block device specification includes the Amazon EBS-specific block device mapping specifications for the image.

            :param delete_on_termination: Configures delete on termination of the associated device.
            :param encrypted: Use to configure device encryption.
            :param iops: Use to configure device IOPS.
            :param kms_key_id: Use to configure the KMS key to use when encrypting the device.
            :param snapshot_id: The snapshot that defines the device contents.
            :param throughput: *For GP3 volumes only* – The throughput in MiB/s that the volume supports.
            :param volume_size: Overrides the volume size of the device.
            :param volume_type: Overrides the volume type of the device.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                ebs_instance_block_device_specification_property = imagebuilder.CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty(
                    delete_on_termination=False,
                    encrypted=False,
                    iops=123,
                    kms_key_id="kmsKeyId",
                    snapshot_id="snapshotId",
                    throughput=123,
                    volume_size=123,
                    volume_type="volumeType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ecfec9c1a0d0607e08e359aadb38abc8238828e27448a6003ed03d928265c878)
                check_type(argname="argument delete_on_termination", value=delete_on_termination, expected_type=type_hints["delete_on_termination"])
                check_type(argname="argument encrypted", value=encrypted, expected_type=type_hints["encrypted"])
                check_type(argname="argument iops", value=iops, expected_type=type_hints["iops"])
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
                check_type(argname="argument snapshot_id", value=snapshot_id, expected_type=type_hints["snapshot_id"])
                check_type(argname="argument throughput", value=throughput, expected_type=type_hints["throughput"])
                check_type(argname="argument volume_size", value=volume_size, expected_type=type_hints["volume_size"])
                check_type(argname="argument volume_type", value=volume_type, expected_type=type_hints["volume_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if delete_on_termination is not None:
                self._values["delete_on_termination"] = delete_on_termination
            if encrypted is not None:
                self._values["encrypted"] = encrypted
            if iops is not None:
                self._values["iops"] = iops
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id
            if snapshot_id is not None:
                self._values["snapshot_id"] = snapshot_id
            if throughput is not None:
                self._values["throughput"] = throughput
            if volume_size is not None:
                self._values["volume_size"] = volume_size
            if volume_type is not None:
                self._values["volume_type"] = volume_type

        @builtins.property
        def delete_on_termination(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Configures delete on termination of the associated device.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-deleteontermination
            '''
            result = self._values.get("delete_on_termination")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def encrypted(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Use to configure device encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-encrypted
            '''
            result = self._values.get("encrypted")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def iops(self) -> typing.Optional[jsii.Number]:
            '''Use to configure device IOPS.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-iops
            '''
            result = self._values.get("iops")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''Use to configure the KMS key to use when encrypting the device.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def snapshot_id(self) -> typing.Optional[builtins.str]:
            '''The snapshot that defines the device contents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-snapshotid
            '''
            result = self._values.get("snapshot_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def throughput(self) -> typing.Optional[jsii.Number]:
            '''*For GP3 volumes only* – The throughput in MiB/s that the volume supports.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-throughput
            '''
            result = self._values.get("throughput")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def volume_size(self) -> typing.Optional[jsii.Number]:
            '''Overrides the volume size of the device.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-volumesize
            '''
            result = self._values.get("volume_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def volume_type(self) -> typing.Optional[builtins.str]:
            '''Overrides the volume type of the device.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification.html#cfn-imagebuilder-imagerecipe-ebsinstanceblockdevicespecification-volumetype
            '''
            result = self._values.get("volume_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EbsInstanceBlockDeviceSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnImageRecipe.InstanceBlockDeviceMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "device_name": "deviceName",
            "ebs": "ebs",
            "no_device": "noDevice",
            "virtual_name": "virtualName",
        },
    )
    class InstanceBlockDeviceMappingProperty:
        def __init__(
            self,
            *,
            device_name: typing.Optional[builtins.str] = None,
            ebs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            no_device: typing.Optional[builtins.str] = None,
            virtual_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines block device mappings for the instance used to configure your image.

            :param device_name: The device to which these mappings apply.
            :param ebs: Use to manage Amazon EBS-specific configuration for this mapping.
            :param no_device: Enter an empty string to remove a mapping from the parent image. The following is an example of an empty string value in the ``NoDevice`` field. ``NoDevice:""``
            :param virtual_name: Manages the instance ephemeral devices.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                instance_block_device_mapping_property = imagebuilder.CfnImageRecipe.InstanceBlockDeviceMappingProperty(
                    device_name="deviceName",
                    ebs=imagebuilder.CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty(
                        delete_on_termination=False,
                        encrypted=False,
                        iops=123,
                        kms_key_id="kmsKeyId",
                        snapshot_id="snapshotId",
                        throughput=123,
                        volume_size=123,
                        volume_type="volumeType"
                    ),
                    no_device="noDevice",
                    virtual_name="virtualName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__49d4c4575e6e8aa63b1188dcd39472139fc5b35a563c27e7b8a0bdf273eb23ff)
                check_type(argname="argument device_name", value=device_name, expected_type=type_hints["device_name"])
                check_type(argname="argument ebs", value=ebs, expected_type=type_hints["ebs"])
                check_type(argname="argument no_device", value=no_device, expected_type=type_hints["no_device"])
                check_type(argname="argument virtual_name", value=virtual_name, expected_type=type_hints["virtual_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if device_name is not None:
                self._values["device_name"] = device_name
            if ebs is not None:
                self._values["ebs"] = ebs
            if no_device is not None:
                self._values["no_device"] = no_device
            if virtual_name is not None:
                self._values["virtual_name"] = virtual_name

        @builtins.property
        def device_name(self) -> typing.Optional[builtins.str]:
            '''The device to which these mappings apply.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html#cfn-imagebuilder-imagerecipe-instanceblockdevicemapping-devicename
            '''
            result = self._values.get("device_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ebs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty"]]:
            '''Use to manage Amazon EBS-specific configuration for this mapping.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html#cfn-imagebuilder-imagerecipe-instanceblockdevicemapping-ebs
            '''
            result = self._values.get("ebs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty"]], result)

        @builtins.property
        def no_device(self) -> typing.Optional[builtins.str]:
            '''Enter an empty string to remove a mapping from the parent image.

            The following is an example of an empty string value in the ``NoDevice`` field.

            ``NoDevice:""``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html#cfn-imagebuilder-imagerecipe-instanceblockdevicemapping-nodevice
            '''
            result = self._values.get("no_device")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def virtual_name(self) -> typing.Optional[builtins.str]:
            '''Manages the instance ephemeral devices.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-instanceblockdevicemapping.html#cfn-imagebuilder-imagerecipe-instanceblockdevicemapping-virtualname
            '''
            result = self._values.get("virtual_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceBlockDeviceMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnImageRecipe.SystemsManagerAgentProperty",
        jsii_struct_bases=[],
        name_mapping={"uninstall_after_build": "uninstallAfterBuild"},
    )
    class SystemsManagerAgentProperty:
        def __init__(
            self,
            *,
            uninstall_after_build: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Contains settings for the Systems Manager agent on your build instance.

            :param uninstall_after_build: Controls whether the Systems Manager agent is removed from your final build image, prior to creating the new AMI. If this is set to true, then the agent is removed from the final image. If it's set to false, then the agent is left in, so that it is included in the new AMI. The default value is false.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-systemsmanageragent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                systems_manager_agent_property = imagebuilder.CfnImageRecipe.SystemsManagerAgentProperty(
                    uninstall_after_build=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ad92f3ddc08f7f471aea45f4940171af1f13b6aca47dcb6cecd2627b25787032)
                check_type(argname="argument uninstall_after_build", value=uninstall_after_build, expected_type=type_hints["uninstall_after_build"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if uninstall_after_build is not None:
                self._values["uninstall_after_build"] = uninstall_after_build

        @builtins.property
        def uninstall_after_build(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Controls whether the Systems Manager agent is removed from your final build image, prior to creating the new AMI.

            If this is set to true, then the agent is removed from the final image. If it's set to false, then the agent is left in, so that it is included in the new AMI. The default value is false.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-imagerecipe-systemsmanageragent.html#cfn-imagebuilder-imagerecipe-systemsmanageragent-uninstallafterbuild
            '''
            result = self._values.get("uninstall_after_build")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SystemsManagerAgentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_imagebuilder.CfnImageRecipeProps",
    jsii_struct_bases=[],
    name_mapping={
        "components": "components",
        "name": "name",
        "parent_image": "parentImage",
        "version": "version",
        "additional_instance_configuration": "additionalInstanceConfiguration",
        "block_device_mappings": "blockDeviceMappings",
        "description": "description",
        "tags": "tags",
        "working_directory": "workingDirectory",
    },
)
class CfnImageRecipeProps:
    def __init__(
        self,
        *,
        components: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImageRecipe.ComponentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        parent_image: builtins.str,
        version: builtins.str,
        additional_instance_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImageRecipe.AdditionalInstanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        block_device_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImageRecipe.InstanceBlockDeviceMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnImageRecipe``.

        :param components: The components of the image recipe. Components are orchestration documents that define a sequence of steps for downloading, installing, configuring, and testing software packages. They also define validation and security hardening steps. A component is defined using a YAML document format.
        :param name: The name of the image recipe.
        :param parent_image: The parent image of the image recipe. The string must be either an Image ARN or an AMI ID.
        :param version: The semantic version of the image recipe.
        :param additional_instance_configuration: Before you create a new AMI, Image Builder launches temporary Amazon EC2 instances to build and test your image configuration. Instance configuration adds a layer of control over those instances. You can define settings and add scripts to run when an instance is launched from your AMI.
        :param block_device_mappings: The block device mappings to apply when creating images from this recipe.
        :param description: The description of the image recipe.
        :param tags: The tags of the image recipe.
        :param working_directory: The working directory to be used during build and test workflows.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_imagebuilder as imagebuilder
            
            cfn_image_recipe_props = imagebuilder.CfnImageRecipeProps(
                components=[imagebuilder.CfnImageRecipe.ComponentConfigurationProperty(
                    component_arn="componentArn",
                    parameters=[imagebuilder.CfnImageRecipe.ComponentParameterProperty(
                        name="name",
                        value=["value"]
                    )]
                )],
                name="name",
                parent_image="parentImage",
                version="version",
            
                # the properties below are optional
                additional_instance_configuration=imagebuilder.CfnImageRecipe.AdditionalInstanceConfigurationProperty(
                    systems_manager_agent=imagebuilder.CfnImageRecipe.SystemsManagerAgentProperty(
                        uninstall_after_build=False
                    ),
                    user_data_override="userDataOverride"
                ),
                block_device_mappings=[imagebuilder.CfnImageRecipe.InstanceBlockDeviceMappingProperty(
                    device_name="deviceName",
                    ebs=imagebuilder.CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty(
                        delete_on_termination=False,
                        encrypted=False,
                        iops=123,
                        kms_key_id="kmsKeyId",
                        snapshot_id="snapshotId",
                        throughput=123,
                        volume_size=123,
                        volume_type="volumeType"
                    ),
                    no_device="noDevice",
                    virtual_name="virtualName"
                )],
                description="description",
                tags={
                    "tags_key": "tags"
                },
                working_directory="workingDirectory"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a289ec10c5f4c9443f1dfb0dc4ecb78a20e5f6e491ed688cb2e3a59ad3d6c88a)
            check_type(argname="argument components", value=components, expected_type=type_hints["components"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parent_image", value=parent_image, expected_type=type_hints["parent_image"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument additional_instance_configuration", value=additional_instance_configuration, expected_type=type_hints["additional_instance_configuration"])
            check_type(argname="argument block_device_mappings", value=block_device_mappings, expected_type=type_hints["block_device_mappings"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument working_directory", value=working_directory, expected_type=type_hints["working_directory"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "components": components,
            "name": name,
            "parent_image": parent_image,
            "version": version,
        }
        if additional_instance_configuration is not None:
            self._values["additional_instance_configuration"] = additional_instance_configuration
        if block_device_mappings is not None:
            self._values["block_device_mappings"] = block_device_mappings
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags
        if working_directory is not None:
            self._values["working_directory"] = working_directory

    @builtins.property
    def components(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnImageRecipe.ComponentConfigurationProperty]]]:
        '''The components of the image recipe.

        Components are orchestration documents that define a sequence of steps for downloading, installing, configuring, and testing software packages. They also define validation and security hardening steps. A component is defined using a YAML document format.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-components
        '''
        result = self._values.get("components")
        assert result is not None, "Required property 'components' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnImageRecipe.ComponentConfigurationProperty]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the image recipe.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parent_image(self) -> builtins.str:
        '''The parent image of the image recipe.

        The string must be either an Image ARN or an AMI ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-parentimage
        '''
        result = self._values.get("parent_image")
        assert result is not None, "Required property 'parent_image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''The semantic version of the image recipe.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-version
        '''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_instance_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnImageRecipe.AdditionalInstanceConfigurationProperty]]:
        '''Before you create a new AMI, Image Builder launches temporary Amazon EC2 instances to build and test your image configuration.

        Instance configuration adds a layer of control over those instances. You can define settings and add scripts to run when an instance is launched from your AMI.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-additionalinstanceconfiguration
        '''
        result = self._values.get("additional_instance_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnImageRecipe.AdditionalInstanceConfigurationProperty]], result)

    @builtins.property
    def block_device_mappings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnImageRecipe.InstanceBlockDeviceMappingProperty]]]]:
        '''The block device mappings to apply when creating images from this recipe.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-blockdevicemappings
        '''
        result = self._values.get("block_device_mappings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnImageRecipe.InstanceBlockDeviceMappingProperty]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the image recipe.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags of the image recipe.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def working_directory(self) -> typing.Optional[builtins.str]:
        '''The working directory to be used during build and test workflows.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.html#cfn-imagebuilder-imagerecipe-workingdirectory
        '''
        result = self._values.get("working_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnImageRecipeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnInfrastructureConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_imagebuilder.CfnInfrastructureConfiguration",
):
    '''The infrastructure configuration allows you to specify the infrastructure within which to build and test your image.

    In the infrastructure configuration, you can specify instance types, subnets, and security groups to associate with your instance. You can also associate an Amazon EC2 key pair with the instance used to build your image. This allows you to log on to your instance to troubleshoot if your build fails and you set terminateInstanceOnFailure to false.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html
    :cloudformationResource: AWS::ImageBuilder::InfrastructureConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_imagebuilder as imagebuilder
        
        cfn_infrastructure_configuration = imagebuilder.CfnInfrastructureConfiguration(self, "MyCfnInfrastructureConfiguration",
            instance_profile_name="instanceProfileName",
            name="name",
        
            # the properties below are optional
            description="description",
            instance_metadata_options=imagebuilder.CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty(
                http_put_response_hop_limit=123,
                http_tokens="httpTokens"
            ),
            instance_types=["instanceTypes"],
            key_pair="keyPair",
            logging=imagebuilder.CfnInfrastructureConfiguration.LoggingProperty(
                s3_logs=imagebuilder.CfnInfrastructureConfiguration.S3LogsProperty(
                    s3_bucket_name="s3BucketName",
                    s3_key_prefix="s3KeyPrefix"
                )
            ),
            resource_tags={
                "resource_tags_key": "resourceTags"
            },
            security_group_ids=["securityGroupIds"],
            sns_topic_arn="snsTopicArn",
            subnet_id="subnetId",
            tags={
                "tags_key": "tags"
            },
            terminate_instance_on_failure=False
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        instance_profile_name: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        instance_metadata_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        key_pair: typing.Optional[builtins.str] = None,
        logging: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInfrastructureConfiguration.LoggingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        sns_topic_arn: typing.Optional[builtins.str] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        terminate_instance_on_failure: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_profile_name: The instance profile of the infrastructure configuration.
        :param name: The name of the infrastructure configuration.
        :param description: The description of the infrastructure configuration.
        :param instance_metadata_options: The instance metadata option settings for the infrastructure configuration.
        :param instance_types: The instance types of the infrastructure configuration.
        :param key_pair: The Amazon EC2 key pair of the infrastructure configuration.
        :param logging: The logging configuration defines where Image Builder uploads your logs.
        :param resource_tags: The tags attached to the resource created by Image Builder.
        :param security_group_ids: The security group IDs of the infrastructure configuration.
        :param sns_topic_arn: The Amazon Resource Name (ARN) of the SNS topic for the infrastructure configuration.
        :param subnet_id: The subnet ID of the infrastructure configuration.
        :param tags: The tags of the infrastructure configuration.
        :param terminate_instance_on_failure: The terminate instance on failure configuration of the infrastructure configuration.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8df8a03094d1fe92963a315a657a78657df102ba9fbe66eda2c26bb8eac04479)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnInfrastructureConfigurationProps(
            instance_profile_name=instance_profile_name,
            name=name,
            description=description,
            instance_metadata_options=instance_metadata_options,
            instance_types=instance_types,
            key_pair=key_pair,
            logging=logging,
            resource_tags=resource_tags,
            security_group_ids=security_group_ids,
            sns_topic_arn=sns_topic_arn,
            subnet_id=subnet_id,
            tags=tags,
            terminate_instance_on_failure=terminate_instance_on_failure,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74669b982a2428b807ea1c9303f9f6436fc7a33f979476a1d362fd55ce646030)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a8aa110274058962353c14921a3072455f5cdd4c719f811fc3f2016a06124c7d)
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
        '''Returns the Amazon Resource Name (ARN) of the infrastructure configuration.

        The following pattern is applied: ``^arn:aws[^:]*:imagebuilder:[^:]+:(?:\\d{12}|aws):(?:image-recipe|infrastructure-configuration|distribution-configuration|component|image|image-pipeline)/[a-z0-9-_]+(?:/(?:(?:x|\\d+)\\.(?:x|\\d+)\\.(?:x|\\d+))(?:/\\d+)?)?$`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''The name of the infrastructure configuration.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

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
    @jsii.member(jsii_name="instanceProfileName")
    def instance_profile_name(self) -> builtins.str:
        '''The instance profile of the infrastructure configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceProfileName"))

    @instance_profile_name.setter
    def instance_profile_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__567cc48eac63fe7658bac22f92aeaef43a88d570458848aaa616a242a0016f53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceProfileName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the infrastructure configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89c441de9755e4528e9501910ffe1b142c79898b858765b54a344edeeb4efcfd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the infrastructure configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11b2528bf4f2f0bc20addb08562906606bf8256aa4bf3a799c73a8f967d324d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="instanceMetadataOptions")
    def instance_metadata_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty"]]:
        '''The instance metadata option settings for the infrastructure configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty"]], jsii.get(self, "instanceMetadataOptions"))

    @instance_metadata_options.setter
    def instance_metadata_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3afa319d538769cad5489226f5f03b6a41c1e6d9b00312872b1f94b18c5a5634)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceMetadataOptions", value)

    @builtins.property
    @jsii.member(jsii_name="instanceTypes")
    def instance_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The instance types of the infrastructure configuration.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "instanceTypes"))

    @instance_types.setter
    def instance_types(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a0b92316d3ef8d02213fb858da5f3aa9757691f73babe9e86e3ee4702b556d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceTypes", value)

    @builtins.property
    @jsii.member(jsii_name="keyPair")
    def key_pair(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 key pair of the infrastructure configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyPair"))

    @key_pair.setter
    def key_pair(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__087a308543348827d9b884784d17ddc6bdce8ecaa0b65300cd6ddb789fd692fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyPair", value)

    @builtins.property
    @jsii.member(jsii_name="logging")
    def logging(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInfrastructureConfiguration.LoggingProperty"]]:
        '''The logging configuration defines where Image Builder uploads your logs.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInfrastructureConfiguration.LoggingProperty"]], jsii.get(self, "logging"))

    @logging.setter
    def logging(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInfrastructureConfiguration.LoggingProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d17651b37e2f4aa5ce6c6076a887fc7270cae14e1f7330e9b48dc5412a83cad9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logging", value)

    @builtins.property
    @jsii.member(jsii_name="resourceTags")
    def resource_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''The tags attached to the resource created by Image Builder.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "resourceTags"))

    @resource_tags.setter
    def resource_tags(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4e6c2bbdd440425ebe7067a9a03bf4079bbfef4001b7877cb6ce3dcd44c4cb0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceTags", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The security group IDs of the infrastructure configuration.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__219d1428ff3821670f8bcafa92479bb91549e3dc36bf8751ba20a7ebcd289712)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="snsTopicArn")
    def sns_topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the SNS topic for the infrastructure configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snsTopicArn"))

    @sns_topic_arn.setter
    def sns_topic_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1588cdfeef854d08e3c06f677829311cc7ab992c28b306cad9fb6cbf3909a7ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snsTopicArn", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''The subnet ID of the infrastructure configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e15394d6263f20f733a1287663578d35f680875e7ea77d8afb2d17f6150efe9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags of the infrastructure configuration.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc5a3a7adbaeb667678ab511c655f1ae0df213cbf0afc14685b60d46b8852e6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="terminateInstanceOnFailure")
    def terminate_instance_on_failure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''The terminate instance on failure configuration of the infrastructure configuration.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "terminateInstanceOnFailure"))

    @terminate_instance_on_failure.setter
    def terminate_instance_on_failure(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7249b107702cdaa94b0beadeaf7622e73dee8dfe6ae5b06188bce3dbefe11423)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terminateInstanceOnFailure", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "http_put_response_hop_limit": "httpPutResponseHopLimit",
            "http_tokens": "httpTokens",
        },
    )
    class InstanceMetadataOptionsProperty:
        def __init__(
            self,
            *,
            http_put_response_hop_limit: typing.Optional[jsii.Number] = None,
            http_tokens: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The instance metadata options that apply to the HTTP requests that pipeline builds use to launch EC2 build and test instances.

            For more information about instance metadata options, see `Configure the instance metadata options <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html>`_ in the **Amazon EC2 User Guide** for Linux instances, or `Configure the instance metadata options <https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/configuring-instance-metadata-options.html>`_ in the **Amazon EC2 Windows Guide** for Windows instances.

            :param http_put_response_hop_limit: Limit the number of hops that an instance metadata request can traverse to reach its destination. The default is one hop. However, if HTTP tokens are required, container image builds need a minimum of two hops.
            :param http_tokens: Indicates whether a signed token header is required for instance metadata retrieval requests. The values affect the response as follows: - *required* – When you retrieve the IAM role credentials, version 2.0 credentials are returned in all cases. - *optional* – You can include a signed token header in your request to retrieve instance metadata, or you can leave it out. If you include it, version 2.0 credentials are returned for the IAM role. Otherwise, version 1.0 credentials are returned. The default setting is *optional* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-instancemetadataoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                instance_metadata_options_property = imagebuilder.CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty(
                    http_put_response_hop_limit=123,
                    http_tokens="httpTokens"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1141979976cfe1199d14e004e82c4b5c7d9823434580281c214438e94c027783)
                check_type(argname="argument http_put_response_hop_limit", value=http_put_response_hop_limit, expected_type=type_hints["http_put_response_hop_limit"])
                check_type(argname="argument http_tokens", value=http_tokens, expected_type=type_hints["http_tokens"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if http_put_response_hop_limit is not None:
                self._values["http_put_response_hop_limit"] = http_put_response_hop_limit
            if http_tokens is not None:
                self._values["http_tokens"] = http_tokens

        @builtins.property
        def http_put_response_hop_limit(self) -> typing.Optional[jsii.Number]:
            '''Limit the number of hops that an instance metadata request can traverse to reach its destination.

            The default is one hop. However, if HTTP tokens are required, container image builds need a minimum of two hops.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-instancemetadataoptions.html#cfn-imagebuilder-infrastructureconfiguration-instancemetadataoptions-httpputresponsehoplimit
            '''
            result = self._values.get("http_put_response_hop_limit")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def http_tokens(self) -> typing.Optional[builtins.str]:
            '''Indicates whether a signed token header is required for instance metadata retrieval requests.

            The values affect the response as follows:

            - *required* – When you retrieve the IAM role credentials, version 2.0 credentials are returned in all cases.
            - *optional* – You can include a signed token header in your request to retrieve instance metadata, or you can leave it out. If you include it, version 2.0 credentials are returned for the IAM role. Otherwise, version 1.0 credentials are returned.

            The default setting is *optional* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-instancemetadataoptions.html#cfn-imagebuilder-infrastructureconfiguration-instancemetadataoptions-httptokens
            '''
            result = self._values.get("http_tokens")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceMetadataOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnInfrastructureConfiguration.LoggingProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_logs": "s3Logs"},
    )
    class LoggingProperty:
        def __init__(
            self,
            *,
            s3_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInfrastructureConfiguration.S3LogsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Logging configuration defines where Image Builder uploads your logs.

            :param s3_logs: The Amazon S3 logging configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-logging.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                logging_property = imagebuilder.CfnInfrastructureConfiguration.LoggingProperty(
                    s3_logs=imagebuilder.CfnInfrastructureConfiguration.S3LogsProperty(
                        s3_bucket_name="s3BucketName",
                        s3_key_prefix="s3KeyPrefix"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d7c7b472c2127725031940b44ae4cf826450bdc016814ad2356cca6734e1ab2e)
                check_type(argname="argument s3_logs", value=s3_logs, expected_type=type_hints["s3_logs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if s3_logs is not None:
                self._values["s3_logs"] = s3_logs

        @builtins.property
        def s3_logs(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInfrastructureConfiguration.S3LogsProperty"]]:
            '''The Amazon S3 logging configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-logging.html#cfn-imagebuilder-infrastructureconfiguration-logging-s3logs
            '''
            result = self._values.get("s3_logs")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInfrastructureConfiguration.S3LogsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnInfrastructureConfiguration.S3LogsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "s3_bucket_name": "s3BucketName",
            "s3_key_prefix": "s3KeyPrefix",
        },
    )
    class S3LogsProperty:
        def __init__(
            self,
            *,
            s3_bucket_name: typing.Optional[builtins.str] = None,
            s3_key_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Amazon S3 logging configuration.

            :param s3_bucket_name: The S3 bucket in which to store the logs.
            :param s3_key_prefix: The Amazon S3 path to the bucket where the logs are stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-s3logs.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                s3_logs_property = imagebuilder.CfnInfrastructureConfiguration.S3LogsProperty(
                    s3_bucket_name="s3BucketName",
                    s3_key_prefix="s3KeyPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__606aaff62e915101e470a1274dc963d43831117f9a85493e01f09a1eebe8e6b6)
                check_type(argname="argument s3_bucket_name", value=s3_bucket_name, expected_type=type_hints["s3_bucket_name"])
                check_type(argname="argument s3_key_prefix", value=s3_key_prefix, expected_type=type_hints["s3_key_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if s3_bucket_name is not None:
                self._values["s3_bucket_name"] = s3_bucket_name
            if s3_key_prefix is not None:
                self._values["s3_key_prefix"] = s3_key_prefix

        @builtins.property
        def s3_bucket_name(self) -> typing.Optional[builtins.str]:
            '''The S3 bucket in which to store the logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-s3logs.html#cfn-imagebuilder-infrastructureconfiguration-s3logs-s3bucketname
            '''
            result = self._values.get("s3_bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_key_prefix(self) -> typing.Optional[builtins.str]:
            '''The Amazon S3 path to the bucket where the logs are stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-infrastructureconfiguration-s3logs.html#cfn-imagebuilder-infrastructureconfiguration-s3logs-s3keyprefix
            '''
            result = self._values.get("s3_key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LogsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_imagebuilder.CfnInfrastructureConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_profile_name": "instanceProfileName",
        "name": "name",
        "description": "description",
        "instance_metadata_options": "instanceMetadataOptions",
        "instance_types": "instanceTypes",
        "key_pair": "keyPair",
        "logging": "logging",
        "resource_tags": "resourceTags",
        "security_group_ids": "securityGroupIds",
        "sns_topic_arn": "snsTopicArn",
        "subnet_id": "subnetId",
        "tags": "tags",
        "terminate_instance_on_failure": "terminateInstanceOnFailure",
    },
)
class CfnInfrastructureConfigurationProps:
    def __init__(
        self,
        *,
        instance_profile_name: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        instance_metadata_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        key_pair: typing.Optional[builtins.str] = None,
        logging: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInfrastructureConfiguration.LoggingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        sns_topic_arn: typing.Optional[builtins.str] = None,
        subnet_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        terminate_instance_on_failure: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ) -> None:
        '''Properties for defining a ``CfnInfrastructureConfiguration``.

        :param instance_profile_name: The instance profile of the infrastructure configuration.
        :param name: The name of the infrastructure configuration.
        :param description: The description of the infrastructure configuration.
        :param instance_metadata_options: The instance metadata option settings for the infrastructure configuration.
        :param instance_types: The instance types of the infrastructure configuration.
        :param key_pair: The Amazon EC2 key pair of the infrastructure configuration.
        :param logging: The logging configuration defines where Image Builder uploads your logs.
        :param resource_tags: The tags attached to the resource created by Image Builder.
        :param security_group_ids: The security group IDs of the infrastructure configuration.
        :param sns_topic_arn: The Amazon Resource Name (ARN) of the SNS topic for the infrastructure configuration.
        :param subnet_id: The subnet ID of the infrastructure configuration.
        :param tags: The tags of the infrastructure configuration.
        :param terminate_instance_on_failure: The terminate instance on failure configuration of the infrastructure configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_imagebuilder as imagebuilder
            
            cfn_infrastructure_configuration_props = imagebuilder.CfnInfrastructureConfigurationProps(
                instance_profile_name="instanceProfileName",
                name="name",
            
                # the properties below are optional
                description="description",
                instance_metadata_options=imagebuilder.CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty(
                    http_put_response_hop_limit=123,
                    http_tokens="httpTokens"
                ),
                instance_types=["instanceTypes"],
                key_pair="keyPair",
                logging=imagebuilder.CfnInfrastructureConfiguration.LoggingProperty(
                    s3_logs=imagebuilder.CfnInfrastructureConfiguration.S3LogsProperty(
                        s3_bucket_name="s3BucketName",
                        s3_key_prefix="s3KeyPrefix"
                    )
                ),
                resource_tags={
                    "resource_tags_key": "resourceTags"
                },
                security_group_ids=["securityGroupIds"],
                sns_topic_arn="snsTopicArn",
                subnet_id="subnetId",
                tags={
                    "tags_key": "tags"
                },
                terminate_instance_on_failure=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf8c493013f64742391c2bf93c7050f371ffeff0d9a35a3791f0b9fbb6019d47)
            check_type(argname="argument instance_profile_name", value=instance_profile_name, expected_type=type_hints["instance_profile_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument instance_metadata_options", value=instance_metadata_options, expected_type=type_hints["instance_metadata_options"])
            check_type(argname="argument instance_types", value=instance_types, expected_type=type_hints["instance_types"])
            check_type(argname="argument key_pair", value=key_pair, expected_type=type_hints["key_pair"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
            check_type(argname="argument resource_tags", value=resource_tags, expected_type=type_hints["resource_tags"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument sns_topic_arn", value=sns_topic_arn, expected_type=type_hints["sns_topic_arn"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument terminate_instance_on_failure", value=terminate_instance_on_failure, expected_type=type_hints["terminate_instance_on_failure"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_profile_name": instance_profile_name,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if instance_metadata_options is not None:
            self._values["instance_metadata_options"] = instance_metadata_options
        if instance_types is not None:
            self._values["instance_types"] = instance_types
        if key_pair is not None:
            self._values["key_pair"] = key_pair
        if logging is not None:
            self._values["logging"] = logging
        if resource_tags is not None:
            self._values["resource_tags"] = resource_tags
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if sns_topic_arn is not None:
            self._values["sns_topic_arn"] = sns_topic_arn
        if subnet_id is not None:
            self._values["subnet_id"] = subnet_id
        if tags is not None:
            self._values["tags"] = tags
        if terminate_instance_on_failure is not None:
            self._values["terminate_instance_on_failure"] = terminate_instance_on_failure

    @builtins.property
    def instance_profile_name(self) -> builtins.str:
        '''The instance profile of the infrastructure configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-instanceprofilename
        '''
        result = self._values.get("instance_profile_name")
        assert result is not None, "Required property 'instance_profile_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the infrastructure configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the infrastructure configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_metadata_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty]]:
        '''The instance metadata option settings for the infrastructure configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-instancemetadataoptions
        '''
        result = self._values.get("instance_metadata_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty]], result)

    @builtins.property
    def instance_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The instance types of the infrastructure configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-instancetypes
        '''
        result = self._values.get("instance_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def key_pair(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 key pair of the infrastructure configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-keypair
        '''
        result = self._values.get("key_pair")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInfrastructureConfiguration.LoggingProperty]]:
        '''The logging configuration defines where Image Builder uploads your logs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-logging
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInfrastructureConfiguration.LoggingProperty]], result)

    @builtins.property
    def resource_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''The tags attached to the resource created by Image Builder.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-resourcetags
        '''
        result = self._values.get("resource_tags")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The security group IDs of the infrastructure configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def sns_topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the SNS topic for the infrastructure configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-snstopicarn
        '''
        result = self._values.get("sns_topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subnet_id(self) -> typing.Optional[builtins.str]:
        '''The subnet ID of the infrastructure configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-subnetid
        '''
        result = self._values.get("subnet_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags of the infrastructure configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def terminate_instance_on_failure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''The terminate instance on failure configuration of the infrastructure configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-infrastructureconfiguration.html#cfn-imagebuilder-infrastructureconfiguration-terminateinstanceonfailure
        '''
        result = self._values.get("terminate_instance_on_failure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInfrastructureConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnLifecyclePolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_imagebuilder.CfnLifecyclePolicy",
):
    '''Create a lifecycle policy resource.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-lifecyclepolicy.html
    :cloudformationResource: AWS::ImageBuilder::LifecyclePolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_imagebuilder as imagebuilder
        
        cfn_lifecycle_policy = imagebuilder.CfnLifecyclePolicy(self, "MyCfnLifecyclePolicy",
            execution_role="executionRole",
            name="name",
            policy_details=[imagebuilder.CfnLifecyclePolicy.PolicyDetailProperty(
                action=imagebuilder.CfnLifecyclePolicy.ActionProperty(
                    type="type",
        
                    # the properties below are optional
                    include_resources=imagebuilder.CfnLifecyclePolicy.IncludeResourcesProperty(
                        amis=False,
                        containers=False,
                        snapshots=False
                    )
                ),
                filter=imagebuilder.CfnLifecyclePolicy.FilterProperty(
                    type="type",
                    value=123,
        
                    # the properties below are optional
                    retain_at_least=123,
                    unit="unit"
                ),
        
                # the properties below are optional
                exclusion_rules=imagebuilder.CfnLifecyclePolicy.ExclusionRulesProperty(
                    amis=imagebuilder.CfnLifecyclePolicy.AmiExclusionRulesProperty(
                        is_public=False,
                        last_launched=imagebuilder.CfnLifecyclePolicy.LastLaunchedProperty(
                            unit="unit",
                            value=123
                        ),
                        regions=["regions"],
                        shared_accounts=["sharedAccounts"],
                        tag_map={
                            "tag_map_key": "tagMap"
                        }
                    ),
                    tag_map={
                        "tag_map_key": "tagMap"
                    }
                )
            )],
            resource_selection=imagebuilder.CfnLifecyclePolicy.ResourceSelectionProperty(
                recipes=[imagebuilder.CfnLifecyclePolicy.RecipeSelectionProperty(
                    name="name",
                    semantic_version="semanticVersion"
                )],
                tag_map={
                    "tag_map_key": "tagMap"
                }
            ),
            resource_type="resourceType",
        
            # the properties below are optional
            description="description",
            status="status",
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
        execution_role: builtins.str,
        name: builtins.str,
        policy_details: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.PolicyDetailProperty", typing.Dict[builtins.str, typing.Any]]]]],
        resource_selection: typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.ResourceSelectionProperty", typing.Dict[builtins.str, typing.Any]]],
        resource_type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param execution_role: The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to run lifecycle actions.
        :param name: The name of the lifecycle policy to create.
        :param policy_details: Configuration details for the lifecycle policy rules.
        :param resource_selection: Selection criteria for the resources that the lifecycle policy applies to.
        :param resource_type: The type of Image Builder resource that the lifecycle policy applies to.
        :param description: Optional description for the lifecycle policy.
        :param status: Indicates whether the lifecycle policy resource is enabled.
        :param tags: Tags to apply to the lifecycle policy resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b441913a83fc39b85885667ae1a4a4add28d162c2540cbe5daf576611d89c45)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLifecyclePolicyProps(
            execution_role=execution_role,
            name=name,
            policy_details=policy_details,
            resource_selection=resource_selection,
            resource_type=resource_type,
            description=description,
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
            type_hints = typing.get_type_hints(_typecheckingstub__997e669ab2d70b66c1108c2056de12da3e2fbc0e1c654655fa0e1f32c1ff9bf7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0fdfac6ebe159cab7b348eba63d9c7a30850f500328f1f2b743390507b1dfbf8)
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
        '''The Amazon Resource Name (ARN) of the lifecycle policy resource.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="executionRole")
    def execution_role(self) -> builtins.str:
        '''The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to run lifecycle actions.'''
        return typing.cast(builtins.str, jsii.get(self, "executionRole"))

    @execution_role.setter
    def execution_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7df981cc48b094d72f929d5a9e77620bf8387063d8f4c0452877bf8470bf5bb0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRole", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the lifecycle policy to create.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__318284e60031de2bbfe99eda11ff55a12c3bb44318c2cbeeaa90b5f7ee610f25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="policyDetails")
    def policy_details(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.PolicyDetailProperty"]]]:
        '''Configuration details for the lifecycle policy rules.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.PolicyDetailProperty"]]], jsii.get(self, "policyDetails"))

    @policy_details.setter
    def policy_details(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.PolicyDetailProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73010b9d10e9b09b5491821779561d5585cd76eea481797eb3122d8b9ee8508c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDetails", value)

    @builtins.property
    @jsii.member(jsii_name="resourceSelection")
    def resource_selection(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ResourceSelectionProperty"]:
        '''Selection criteria for the resources that the lifecycle policy applies to.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ResourceSelectionProperty"], jsii.get(self, "resourceSelection"))

    @resource_selection.setter
    def resource_selection(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ResourceSelectionProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa4f13ae99ebd0f4eaf2e189e0687bda23b3ff6f7f3a1716d1eadfe529976a3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceSelection", value)

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''The type of Image Builder resource that the lifecycle policy applies to.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @resource_type.setter
    def resource_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64fe4860941ec7baf85181482da4f12aa4fb911b934f3b02a8a7b1c56d2c8226)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceType", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Optional description for the lifecycle policy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e996dee13897dcb4e83e73e4d73bcd855080996d0417f2f74f5628205c5234a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''Indicates whether the lifecycle policy resource is enabled.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5495e49fe08c27baf854c2e3f3005125f1e5f20e9b6cacfa47e41c4d319b9034)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags to apply to the lifecycle policy resource.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4e72af6227539e4a5e696bb41f6d2e0df2d6f0d3f943785a49eefa13944b953)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnLifecyclePolicy.ActionProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "include_resources": "includeResources"},
    )
    class ActionProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            include_resources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.IncludeResourcesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains selection criteria for the lifecycle policy.

            :param type: Specifies the lifecycle action to take.
            :param include_resources: Specifies the resources that the lifecycle policy applies to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                action_property = imagebuilder.CfnLifecyclePolicy.ActionProperty(
                    type="type",
                
                    # the properties below are optional
                    include_resources=imagebuilder.CfnLifecyclePolicy.IncludeResourcesProperty(
                        amis=False,
                        containers=False,
                        snapshots=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9b3703bb1789e55ea0843aa78bd8e86cf376052d4aa4bb2c85cc78069a805ac0)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument include_resources", value=include_resources, expected_type=type_hints["include_resources"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if include_resources is not None:
                self._values["include_resources"] = include_resources

        @builtins.property
        def type(self) -> builtins.str:
            '''Specifies the lifecycle action to take.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-action.html#cfn-imagebuilder-lifecyclepolicy-action-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def include_resources(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.IncludeResourcesProperty"]]:
            '''Specifies the resources that the lifecycle policy applies to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-action.html#cfn-imagebuilder-lifecyclepolicy-action-includeresources
            '''
            result = self._values.get("include_resources")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.IncludeResourcesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnLifecyclePolicy.AmiExclusionRulesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "is_public": "isPublic",
            "last_launched": "lastLaunched",
            "regions": "regions",
            "shared_accounts": "sharedAccounts",
            "tag_map": "tagMap",
        },
    )
    class AmiExclusionRulesProperty:
        def __init__(
            self,
            *,
            is_public: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            last_launched: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.LastLaunchedProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            regions: typing.Optional[typing.Sequence[builtins.str]] = None,
            shared_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
            tag_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        ) -> None:
            '''Defines criteria for AMIs that are excluded from lifecycle actions.

            :param is_public: Configures whether public AMIs are excluded from the lifecycle action.
            :param last_launched: Specifies configuration details for Image Builder to exclude the most recent resources from lifecycle actions.
            :param regions: Configures AWS Region s that are excluded from the lifecycle action.
            :param shared_accounts: Specifies AWS account s whose resources are excluded from the lifecycle action.
            :param tag_map: Lists tags that should be excluded from lifecycle actions for the AMIs that have them.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-amiexclusionrules.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                ami_exclusion_rules_property = imagebuilder.CfnLifecyclePolicy.AmiExclusionRulesProperty(
                    is_public=False,
                    last_launched=imagebuilder.CfnLifecyclePolicy.LastLaunchedProperty(
                        unit="unit",
                        value=123
                    ),
                    regions=["regions"],
                    shared_accounts=["sharedAccounts"],
                    tag_map={
                        "tag_map_key": "tagMap"
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__05134c25c9cdb0bbc6009541532ec2b9cbb483cc3413a7a624d12232b29a003b)
                check_type(argname="argument is_public", value=is_public, expected_type=type_hints["is_public"])
                check_type(argname="argument last_launched", value=last_launched, expected_type=type_hints["last_launched"])
                check_type(argname="argument regions", value=regions, expected_type=type_hints["regions"])
                check_type(argname="argument shared_accounts", value=shared_accounts, expected_type=type_hints["shared_accounts"])
                check_type(argname="argument tag_map", value=tag_map, expected_type=type_hints["tag_map"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if is_public is not None:
                self._values["is_public"] = is_public
            if last_launched is not None:
                self._values["last_launched"] = last_launched
            if regions is not None:
                self._values["regions"] = regions
            if shared_accounts is not None:
                self._values["shared_accounts"] = shared_accounts
            if tag_map is not None:
                self._values["tag_map"] = tag_map

        @builtins.property
        def is_public(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Configures whether public AMIs are excluded from the lifecycle action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-amiexclusionrules.html#cfn-imagebuilder-lifecyclepolicy-amiexclusionrules-ispublic
            '''
            result = self._values.get("is_public")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def last_launched(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.LastLaunchedProperty"]]:
            '''Specifies configuration details for Image Builder to exclude the most recent resources from lifecycle actions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-amiexclusionrules.html#cfn-imagebuilder-lifecyclepolicy-amiexclusionrules-lastlaunched
            '''
            result = self._values.get("last_launched")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.LastLaunchedProperty"]], result)

        @builtins.property
        def regions(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Configures AWS Region s that are excluded from the lifecycle action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-amiexclusionrules.html#cfn-imagebuilder-lifecyclepolicy-amiexclusionrules-regions
            '''
            result = self._values.get("regions")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def shared_accounts(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Specifies AWS account s whose resources are excluded from the lifecycle action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-amiexclusionrules.html#cfn-imagebuilder-lifecyclepolicy-amiexclusionrules-sharedaccounts
            '''
            result = self._values.get("shared_accounts")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def tag_map(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''Lists tags that should be excluded from lifecycle actions for the AMIs that have them.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-amiexclusionrules.html#cfn-imagebuilder-lifecyclepolicy-amiexclusionrules-tagmap
            '''
            result = self._values.get("tag_map")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmiExclusionRulesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnLifecyclePolicy.ExclusionRulesProperty",
        jsii_struct_bases=[],
        name_mapping={"amis": "amis", "tag_map": "tagMap"},
    )
    class ExclusionRulesProperty:
        def __init__(
            self,
            *,
            amis: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.AmiExclusionRulesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            tag_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        ) -> None:
            '''Specifies resources that lifecycle policy actions should not apply to.

            :param amis: Lists configuration values that apply to AMIs that Image Builder should exclude from the lifecycle action.
            :param tag_map: Contains a list of tags that Image Builder uses to skip lifecycle actions for Image Builder image resources that have them.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-exclusionrules.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                exclusion_rules_property = imagebuilder.CfnLifecyclePolicy.ExclusionRulesProperty(
                    amis=imagebuilder.CfnLifecyclePolicy.AmiExclusionRulesProperty(
                        is_public=False,
                        last_launched=imagebuilder.CfnLifecyclePolicy.LastLaunchedProperty(
                            unit="unit",
                            value=123
                        ),
                        regions=["regions"],
                        shared_accounts=["sharedAccounts"],
                        tag_map={
                            "tag_map_key": "tagMap"
                        }
                    ),
                    tag_map={
                        "tag_map_key": "tagMap"
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__284c02a995f46d8f38f0f1c9b8aa842e2acafc4d2a0cd2a09a7ccfd618f97a70)
                check_type(argname="argument amis", value=amis, expected_type=type_hints["amis"])
                check_type(argname="argument tag_map", value=tag_map, expected_type=type_hints["tag_map"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if amis is not None:
                self._values["amis"] = amis
            if tag_map is not None:
                self._values["tag_map"] = tag_map

        @builtins.property
        def amis(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.AmiExclusionRulesProperty"]]:
            '''Lists configuration values that apply to AMIs that Image Builder should exclude from the lifecycle action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-exclusionrules.html#cfn-imagebuilder-lifecyclepolicy-exclusionrules-amis
            '''
            result = self._values.get("amis")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.AmiExclusionRulesProperty"]], result)

        @builtins.property
        def tag_map(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''Contains a list of tags that Image Builder uses to skip lifecycle actions for Image Builder image resources that have them.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-exclusionrules.html#cfn-imagebuilder-lifecyclepolicy-exclusionrules-tagmap
            '''
            result = self._values.get("tag_map")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExclusionRulesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnLifecyclePolicy.FilterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "type": "type",
            "value": "value",
            "retain_at_least": "retainAtLeast",
            "unit": "unit",
        },
    )
    class FilterProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            value: jsii.Number,
            retain_at_least: typing.Optional[jsii.Number] = None,
            unit: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines filters that the lifecycle policy uses to determine impacted resource.

            :param type: Filter resources based on either ``age`` or ``count`` .
            :param value: The number of units for the time period or for the count. For example, a value of ``6`` might refer to six months or six AMIs. .. epigraph:: For count-based filters, this value represents the minimum number of resources to keep on hand. If you have fewer resources than this number, the resource is excluded from lifecycle actions.
            :param retain_at_least: For age-based filters, this is the number of resources to keep on hand after the lifecycle ``DELETE`` action is applied. Impacted resources are only deleted if you have more than this number of resources. If you have fewer resources than this number, the impacted resource is not deleted.
            :param unit: Defines the unit of time that the lifecycle policy uses to determine impacted resources. This is required for age-based rules.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-filter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                filter_property = imagebuilder.CfnLifecyclePolicy.FilterProperty(
                    type="type",
                    value=123,
                
                    # the properties below are optional
                    retain_at_least=123,
                    unit="unit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ae34685f55ed44c43efb8db0e7558cbf62100f081f22ea4b62ca781cc202e062)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
                check_type(argname="argument retain_at_least", value=retain_at_least, expected_type=type_hints["retain_at_least"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
                "value": value,
            }
            if retain_at_least is not None:
                self._values["retain_at_least"] = retain_at_least
            if unit is not None:
                self._values["unit"] = unit

        @builtins.property
        def type(self) -> builtins.str:
            '''Filter resources based on either ``age`` or ``count`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-filter.html#cfn-imagebuilder-lifecyclepolicy-filter-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> jsii.Number:
            '''The number of units for the time period or for the count.

            For example, a value of ``6`` might refer to six months or six AMIs.
            .. epigraph::

               For count-based filters, this value represents the minimum number of resources to keep on hand. If you have fewer resources than this number, the resource is excluded from lifecycle actions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-filter.html#cfn-imagebuilder-lifecyclepolicy-filter-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def retain_at_least(self) -> typing.Optional[jsii.Number]:
            '''For age-based filters, this is the number of resources to keep on hand after the lifecycle ``DELETE`` action is applied.

            Impacted resources are only deleted if you have more than this number of resources. If you have fewer resources than this number, the impacted resource is not deleted.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-filter.html#cfn-imagebuilder-lifecyclepolicy-filter-retainatleast
            '''
            result = self._values.get("retain_at_least")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def unit(self) -> typing.Optional[builtins.str]:
            '''Defines the unit of time that the lifecycle policy uses to determine impacted resources.

            This is required for age-based rules.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-filter.html#cfn-imagebuilder-lifecyclepolicy-filter-unit
            '''
            result = self._values.get("unit")
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
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnLifecyclePolicy.IncludeResourcesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "amis": "amis",
            "containers": "containers",
            "snapshots": "snapshots",
        },
    )
    class IncludeResourcesProperty:
        def __init__(
            self,
            *,
            amis: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            containers: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            snapshots: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Specifies how the lifecycle policy should apply actions to selected resources.

            :param amis: Specifies whether the lifecycle action should apply to distributed AMIs.
            :param containers: Specifies whether the lifecycle action should apply to distributed containers.
            :param snapshots: Specifies whether the lifecycle action should apply to snapshots associated with distributed AMIs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-includeresources.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                include_resources_property = imagebuilder.CfnLifecyclePolicy.IncludeResourcesProperty(
                    amis=False,
                    containers=False,
                    snapshots=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2a71a92276a1b69aaf0a934da7eaa5abd8843fdc821b5c0c5aa37a81d55eed8d)
                check_type(argname="argument amis", value=amis, expected_type=type_hints["amis"])
                check_type(argname="argument containers", value=containers, expected_type=type_hints["containers"])
                check_type(argname="argument snapshots", value=snapshots, expected_type=type_hints["snapshots"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if amis is not None:
                self._values["amis"] = amis
            if containers is not None:
                self._values["containers"] = containers
            if snapshots is not None:
                self._values["snapshots"] = snapshots

        @builtins.property
        def amis(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether the lifecycle action should apply to distributed AMIs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-includeresources.html#cfn-imagebuilder-lifecyclepolicy-includeresources-amis
            '''
            result = self._values.get("amis")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def containers(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether the lifecycle action should apply to distributed containers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-includeresources.html#cfn-imagebuilder-lifecyclepolicy-includeresources-containers
            '''
            result = self._values.get("containers")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def snapshots(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether the lifecycle action should apply to snapshots associated with distributed AMIs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-includeresources.html#cfn-imagebuilder-lifecyclepolicy-includeresources-snapshots
            '''
            result = self._values.get("snapshots")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IncludeResourcesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnLifecyclePolicy.LastLaunchedProperty",
        jsii_struct_bases=[],
        name_mapping={"unit": "unit", "value": "value"},
    )
    class LastLaunchedProperty:
        def __init__(self, *, unit: builtins.str, value: jsii.Number) -> None:
            '''Defines criteria to exclude AMIs from lifecycle actions based on the last time they were used to launch an instance.

            :param unit: Defines the unit of time that the lifecycle policy uses to calculate elapsed time since the last instance launched from the AMI. For example: days, weeks, months, or years.
            :param value: The integer number of units for the time period. For example ``6`` (months).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-lastlaunched.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                last_launched_property = imagebuilder.CfnLifecyclePolicy.LastLaunchedProperty(
                    unit="unit",
                    value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b873acb7ad8c3039d17767ab82c3f8a2b2b0d314b00e2e45dc73e897b6495cfe)
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "unit": unit,
                "value": value,
            }

        @builtins.property
        def unit(self) -> builtins.str:
            '''Defines the unit of time that the lifecycle policy uses to calculate elapsed time since the last instance launched from the AMI.

            For example: days, weeks, months, or years.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-lastlaunched.html#cfn-imagebuilder-lifecyclepolicy-lastlaunched-unit
            '''
            result = self._values.get("unit")
            assert result is not None, "Required property 'unit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> jsii.Number:
            '''The integer number of units for the time period.

            For example ``6`` (months).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-lastlaunched.html#cfn-imagebuilder-lifecyclepolicy-lastlaunched-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LastLaunchedProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnLifecyclePolicy.PolicyDetailProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "filter": "filter",
            "exclusion_rules": "exclusionRules",
        },
    )
    class PolicyDetailProperty:
        def __init__(
            self,
            *,
            action: typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.ActionProperty", typing.Dict[builtins.str, typing.Any]]],
            filter: typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.FilterProperty", typing.Dict[builtins.str, typing.Any]]],
            exclusion_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.ExclusionRulesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration details for a lifecycle policy resource.

            :param action: Configuration details for the policy action.
            :param filter: Specifies the resources that the lifecycle policy applies to.
            :param exclusion_rules: Additional rules to specify resources that should be exempt from policy actions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-policydetail.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                policy_detail_property = imagebuilder.CfnLifecyclePolicy.PolicyDetailProperty(
                    action=imagebuilder.CfnLifecyclePolicy.ActionProperty(
                        type="type",
                
                        # the properties below are optional
                        include_resources=imagebuilder.CfnLifecyclePolicy.IncludeResourcesProperty(
                            amis=False,
                            containers=False,
                            snapshots=False
                        )
                    ),
                    filter=imagebuilder.CfnLifecyclePolicy.FilterProperty(
                        type="type",
                        value=123,
                
                        # the properties below are optional
                        retain_at_least=123,
                        unit="unit"
                    ),
                
                    # the properties below are optional
                    exclusion_rules=imagebuilder.CfnLifecyclePolicy.ExclusionRulesProperty(
                        amis=imagebuilder.CfnLifecyclePolicy.AmiExclusionRulesProperty(
                            is_public=False,
                            last_launched=imagebuilder.CfnLifecyclePolicy.LastLaunchedProperty(
                                unit="unit",
                                value=123
                            ),
                            regions=["regions"],
                            shared_accounts=["sharedAccounts"],
                            tag_map={
                                "tag_map_key": "tagMap"
                            }
                        ),
                        tag_map={
                            "tag_map_key": "tagMap"
                        }
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bf722d246758df8a2a9189fea40552c11f02659c91c03c64c9245d5331394cd0)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
                check_type(argname="argument exclusion_rules", value=exclusion_rules, expected_type=type_hints["exclusion_rules"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action": action,
                "filter": filter,
            }
            if exclusion_rules is not None:
                self._values["exclusion_rules"] = exclusion_rules

        @builtins.property
        def action(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ActionProperty"]:
            '''Configuration details for the policy action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-policydetail.html#cfn-imagebuilder-lifecyclepolicy-policydetail-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ActionProperty"], result)

        @builtins.property
        def filter(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.FilterProperty"]:
            '''Specifies the resources that the lifecycle policy applies to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-policydetail.html#cfn-imagebuilder-lifecyclepolicy-policydetail-filter
            '''
            result = self._values.get("filter")
            assert result is not None, "Required property 'filter' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.FilterProperty"], result)

        @builtins.property
        def exclusion_rules(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ExclusionRulesProperty"]]:
            '''Additional rules to specify resources that should be exempt from policy actions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-policydetail.html#cfn-imagebuilder-lifecyclepolicy-policydetail-exclusionrules
            '''
            result = self._values.get("exclusion_rules")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.ExclusionRulesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PolicyDetailProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnLifecyclePolicy.RecipeSelectionProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "semantic_version": "semanticVersion"},
    )
    class RecipeSelectionProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            semantic_version: builtins.str,
        ) -> None:
            '''Specifies an Image Builder recipe that the lifecycle policy uses for resource selection.

            :param name: The name of an Image Builder recipe that the lifecycle policy uses for resource selection.
            :param semantic_version: The version of the Image Builder recipe specified by the ``name`` field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-recipeselection.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                recipe_selection_property = imagebuilder.CfnLifecyclePolicy.RecipeSelectionProperty(
                    name="name",
                    semantic_version="semanticVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__16450d1b17b0ea545ae61c434c161a1873c39c7215299585bcf233621d5c8c5e)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument semantic_version", value=semantic_version, expected_type=type_hints["semantic_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "semantic_version": semantic_version,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of an Image Builder recipe that the lifecycle policy uses for resource selection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-recipeselection.html#cfn-imagebuilder-lifecyclepolicy-recipeselection-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def semantic_version(self) -> builtins.str:
            '''The version of the Image Builder recipe specified by the ``name`` field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-recipeselection.html#cfn-imagebuilder-lifecyclepolicy-recipeselection-semanticversion
            '''
            result = self._values.get("semantic_version")
            assert result is not None, "Required property 'semantic_version' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecipeSelectionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_imagebuilder.CfnLifecyclePolicy.ResourceSelectionProperty",
        jsii_struct_bases=[],
        name_mapping={"recipes": "recipes", "tag_map": "tagMap"},
    )
    class ResourceSelectionProperty:
        def __init__(
            self,
            *,
            recipes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnLifecyclePolicy.RecipeSelectionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            tag_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        ) -> None:
            '''Resource selection criteria for the lifecycle policy.

            :param recipes: A list of recipes that are used as selection criteria for the output images that the lifecycle policy applies to.
            :param tag_map: A list of tags that are used as selection criteria for the Image Builder image resources that the lifecycle policy applies to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-resourceselection.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_imagebuilder as imagebuilder
                
                resource_selection_property = imagebuilder.CfnLifecyclePolicy.ResourceSelectionProperty(
                    recipes=[imagebuilder.CfnLifecyclePolicy.RecipeSelectionProperty(
                        name="name",
                        semantic_version="semanticVersion"
                    )],
                    tag_map={
                        "tag_map_key": "tagMap"
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a50d1f1937c770dfb0439cdf4e09d340344cb42f76c244b1320fe680a4c4e82c)
                check_type(argname="argument recipes", value=recipes, expected_type=type_hints["recipes"])
                check_type(argname="argument tag_map", value=tag_map, expected_type=type_hints["tag_map"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if recipes is not None:
                self._values["recipes"] = recipes
            if tag_map is not None:
                self._values["tag_map"] = tag_map

        @builtins.property
        def recipes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.RecipeSelectionProperty"]]]]:
            '''A list of recipes that are used as selection criteria for the output images that the lifecycle policy applies to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-resourceselection.html#cfn-imagebuilder-lifecyclepolicy-resourceselection-recipes
            '''
            result = self._values.get("recipes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnLifecyclePolicy.RecipeSelectionProperty"]]]], result)

        @builtins.property
        def tag_map(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''A list of tags that are used as selection criteria for the Image Builder image resources that the lifecycle policy applies to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-imagebuilder-lifecyclepolicy-resourceselection.html#cfn-imagebuilder-lifecyclepolicy-resourceselection-tagmap
            '''
            result = self._values.get("tag_map")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceSelectionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_imagebuilder.CfnLifecyclePolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "execution_role": "executionRole",
        "name": "name",
        "policy_details": "policyDetails",
        "resource_selection": "resourceSelection",
        "resource_type": "resourceType",
        "description": "description",
        "status": "status",
        "tags": "tags",
    },
)
class CfnLifecyclePolicyProps:
    def __init__(
        self,
        *,
        execution_role: builtins.str,
        name: builtins.str,
        policy_details: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.PolicyDetailProperty, typing.Dict[builtins.str, typing.Any]]]]],
        resource_selection: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.ResourceSelectionProperty, typing.Dict[builtins.str, typing.Any]]],
        resource_type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLifecyclePolicy``.

        :param execution_role: The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to run lifecycle actions.
        :param name: The name of the lifecycle policy to create.
        :param policy_details: Configuration details for the lifecycle policy rules.
        :param resource_selection: Selection criteria for the resources that the lifecycle policy applies to.
        :param resource_type: The type of Image Builder resource that the lifecycle policy applies to.
        :param description: Optional description for the lifecycle policy.
        :param status: Indicates whether the lifecycle policy resource is enabled.
        :param tags: Tags to apply to the lifecycle policy resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-lifecyclepolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_imagebuilder as imagebuilder
            
            cfn_lifecycle_policy_props = imagebuilder.CfnLifecyclePolicyProps(
                execution_role="executionRole",
                name="name",
                policy_details=[imagebuilder.CfnLifecyclePolicy.PolicyDetailProperty(
                    action=imagebuilder.CfnLifecyclePolicy.ActionProperty(
                        type="type",
            
                        # the properties below are optional
                        include_resources=imagebuilder.CfnLifecyclePolicy.IncludeResourcesProperty(
                            amis=False,
                            containers=False,
                            snapshots=False
                        )
                    ),
                    filter=imagebuilder.CfnLifecyclePolicy.FilterProperty(
                        type="type",
                        value=123,
            
                        # the properties below are optional
                        retain_at_least=123,
                        unit="unit"
                    ),
            
                    # the properties below are optional
                    exclusion_rules=imagebuilder.CfnLifecyclePolicy.ExclusionRulesProperty(
                        amis=imagebuilder.CfnLifecyclePolicy.AmiExclusionRulesProperty(
                            is_public=False,
                            last_launched=imagebuilder.CfnLifecyclePolicy.LastLaunchedProperty(
                                unit="unit",
                                value=123
                            ),
                            regions=["regions"],
                            shared_accounts=["sharedAccounts"],
                            tag_map={
                                "tag_map_key": "tagMap"
                            }
                        ),
                        tag_map={
                            "tag_map_key": "tagMap"
                        }
                    )
                )],
                resource_selection=imagebuilder.CfnLifecyclePolicy.ResourceSelectionProperty(
                    recipes=[imagebuilder.CfnLifecyclePolicy.RecipeSelectionProperty(
                        name="name",
                        semantic_version="semanticVersion"
                    )],
                    tag_map={
                        "tag_map_key": "tagMap"
                    }
                ),
                resource_type="resourceType",
            
                # the properties below are optional
                description="description",
                status="status",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d645dc30df568adc41cd2d0c464f623b51b54d8bb6b1351018d90d6c338846f)
            check_type(argname="argument execution_role", value=execution_role, expected_type=type_hints["execution_role"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument policy_details", value=policy_details, expected_type=type_hints["policy_details"])
            check_type(argname="argument resource_selection", value=resource_selection, expected_type=type_hints["resource_selection"])
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "execution_role": execution_role,
            "name": name,
            "policy_details": policy_details,
            "resource_selection": resource_selection,
            "resource_type": resource_type,
        }
        if description is not None:
            self._values["description"] = description
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def execution_role(self) -> builtins.str:
        '''The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to run lifecycle actions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-lifecyclepolicy.html#cfn-imagebuilder-lifecyclepolicy-executionrole
        '''
        result = self._values.get("execution_role")
        assert result is not None, "Required property 'execution_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the lifecycle policy to create.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-lifecyclepolicy.html#cfn-imagebuilder-lifecyclepolicy-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_details(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLifecyclePolicy.PolicyDetailProperty]]]:
        '''Configuration details for the lifecycle policy rules.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-lifecyclepolicy.html#cfn-imagebuilder-lifecyclepolicy-policydetails
        '''
        result = self._values.get("policy_details")
        assert result is not None, "Required property 'policy_details' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLifecyclePolicy.PolicyDetailProperty]]], result)

    @builtins.property
    def resource_selection(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnLifecyclePolicy.ResourceSelectionProperty]:
        '''Selection criteria for the resources that the lifecycle policy applies to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-lifecyclepolicy.html#cfn-imagebuilder-lifecyclepolicy-resourceselection
        '''
        result = self._values.get("resource_selection")
        assert result is not None, "Required property 'resource_selection' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnLifecyclePolicy.ResourceSelectionProperty], result)

    @builtins.property
    def resource_type(self) -> builtins.str:
        '''The type of Image Builder resource that the lifecycle policy applies to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-lifecyclepolicy.html#cfn-imagebuilder-lifecyclepolicy-resourcetype
        '''
        result = self._values.get("resource_type")
        assert result is not None, "Required property 'resource_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Optional description for the lifecycle policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-lifecyclepolicy.html#cfn-imagebuilder-lifecyclepolicy-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Indicates whether the lifecycle policy resource is enabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-lifecyclepolicy.html#cfn-imagebuilder-lifecyclepolicy-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags to apply to the lifecycle policy resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-lifecyclepolicy.html#cfn-imagebuilder-lifecyclepolicy-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLifecyclePolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnWorkflow(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_imagebuilder.CfnWorkflow",
):
    '''Create a new workflow or a new version of an existing workflow.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-workflow.html
    :cloudformationResource: AWS::ImageBuilder::Workflow
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_imagebuilder as imagebuilder
        
        cfn_workflow = imagebuilder.CfnWorkflow(self, "MyCfnWorkflow",
            name="name",
            type="type",
            version="version",
        
            # the properties below are optional
            change_description="changeDescription",
            data="data",
            description="description",
            kms_key_id="kmsKeyId",
            tags={
                "tags_key": "tags"
            },
            uri="uri"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        type: builtins.str,
        version: builtins.str,
        change_description: typing.Optional[builtins.str] = None,
        data: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the workflow to create.
        :param type: The phase in the image build process for which the workflow resource is responsible.
        :param version: The semantic version of this workflow resource. The semantic version syntax adheres to the following rules. .. epigraph:: The semantic version has four nodes: ../. You can assign values for the first three, and can filter on all of them. *Assignment:* For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node. *Patterns:* You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.
        :param change_description: Describes what change has been made in this version of the workflow, or what makes this version different from other versions of the workflow.
        :param data: Contains the UTF-8 encoded YAML document content for the workflow. Alternatively, you can specify the ``uri`` of a YAML document file stored in Amazon S3. However, you cannot specify both properties.
        :param description: Describes the workflow.
        :param kms_key_id: The ID of the KMS key that is used to encrypt this workflow resource.
        :param tags: Tags that apply to the workflow resource.
        :param uri: The ``uri`` of a YAML component document file. This must be an S3 URL ( ``s3://bucket/key`` ), and the requester must have permission to access the S3 bucket it points to. If you use Amazon S3, you can specify component content up to your service quota. Alternatively, you can specify the YAML document inline, using the component ``data`` property. You cannot specify both properties.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd82b8722476efd9ae3c84a0cf5b8f1d6b48550745017b0d128afabf5f24b5b2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWorkflowProps(
            name=name,
            type=type,
            version=version,
            change_description=change_description,
            data=data,
            description=description,
            kms_key_id=kms_key_id,
            tags=tags,
            uri=uri,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb3d8659b8d763c14b7737c9410afacee05a27e95b64c0ed4b73165d968ab03c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__56f66168df4b459392919a074261a67669f13f593780de274f36bbeb7bc11b3c)
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
        '''The Amazon Resource Name (ARN) of the workflow resource.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the workflow to create.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9ca2ede358f8e6d6f27ece2e03d7d871d14d1daaeba3cb4c788afc33c2bc227)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The phase in the image build process for which the workflow resource is responsible.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41b009fd9ca27b9f352338a895a62a4f074e2c7eb510b43e13f8792747f571c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''The semantic version of this workflow resource.

        The semantic version syntax adheres to the following rules.
        '''
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ce08768a8ac00cab8a7fb60330cb7f716c6376d6d056e8ade1e44a26436417d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="changeDescription")
    def change_description(self) -> typing.Optional[builtins.str]:
        '''Describes what change has been made in this version of the workflow, or what makes this version different from other versions of the workflow.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "changeDescription"))

    @change_description.setter
    def change_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b245fa74b6c4cb04ff6723da66ff8f8cd6af6cd5bcb55ede52fbb7a4519992d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "changeDescription", value)

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> typing.Optional[builtins.str]:
        '''Contains the UTF-8 encoded YAML document content for the workflow.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "data"))

    @data.setter
    def data(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57d165db317968c3d0b9096bb379e7548f28dec9638ea2beebdc78b7bdf0e904)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Describes the workflow.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b296abb92cd399ea05e8c119ac7fdf0c7ac681e045dc5b83cfc6d9b0d97b7233)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the KMS key that is used to encrypt this workflow resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b8bb7c0820c2fd1205773d0df64a2953848236b9ead853f32d65a2239aaafa0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags that apply to the workflow resource.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1212a2dd4ab9ee1b3006c19c3027125ab0148561c4bc08b5d80fc0e29bfdf854)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> typing.Optional[builtins.str]:
        '''The ``uri`` of a YAML component document file.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e36c0e0583778b96be119919e9f8e273d4b8ff0bfa5e58c3049f2cc89a520dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_imagebuilder.CfnWorkflowProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "type": "type",
        "version": "version",
        "change_description": "changeDescription",
        "data": "data",
        "description": "description",
        "kms_key_id": "kmsKeyId",
        "tags": "tags",
        "uri": "uri",
    },
)
class CfnWorkflowProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        version: builtins.str,
        change_description: typing.Optional[builtins.str] = None,
        data: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnWorkflow``.

        :param name: The name of the workflow to create.
        :param type: The phase in the image build process for which the workflow resource is responsible.
        :param version: The semantic version of this workflow resource. The semantic version syntax adheres to the following rules. .. epigraph:: The semantic version has four nodes: ../. You can assign values for the first three, and can filter on all of them. *Assignment:* For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node. *Patterns:* You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.
        :param change_description: Describes what change has been made in this version of the workflow, or what makes this version different from other versions of the workflow.
        :param data: Contains the UTF-8 encoded YAML document content for the workflow. Alternatively, you can specify the ``uri`` of a YAML document file stored in Amazon S3. However, you cannot specify both properties.
        :param description: Describes the workflow.
        :param kms_key_id: The ID of the KMS key that is used to encrypt this workflow resource.
        :param tags: Tags that apply to the workflow resource.
        :param uri: The ``uri`` of a YAML component document file. This must be an S3 URL ( ``s3://bucket/key`` ), and the requester must have permission to access the S3 bucket it points to. If you use Amazon S3, you can specify component content up to your service quota. Alternatively, you can specify the YAML document inline, using the component ``data`` property. You cannot specify both properties.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-workflow.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_imagebuilder as imagebuilder
            
            cfn_workflow_props = imagebuilder.CfnWorkflowProps(
                name="name",
                type="type",
                version="version",
            
                # the properties below are optional
                change_description="changeDescription",
                data="data",
                description="description",
                kms_key_id="kmsKeyId",
                tags={
                    "tags_key": "tags"
                },
                uri="uri"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35d88d62d7ed1f4b6deb48b19f5f6a93db101eada9232a0e7f6cc8c59ce9e078)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument change_description", value=change_description, expected_type=type_hints["change_description"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "type": type,
            "version": version,
        }
        if change_description is not None:
            self._values["change_description"] = change_description
        if data is not None:
            self._values["data"] = data
        if description is not None:
            self._values["description"] = description
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if tags is not None:
            self._values["tags"] = tags
        if uri is not None:
            self._values["uri"] = uri

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the workflow to create.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-workflow.html#cfn-imagebuilder-workflow-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The phase in the image build process for which the workflow resource is responsible.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-workflow.html#cfn-imagebuilder-workflow-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''The semantic version of this workflow resource. The semantic version syntax adheres to the following rules.

        .. epigraph::

           The semantic version has four nodes: ../. You can assign values for the first three, and can filter on all of them.

           *Assignment:* For the first three nodes you can assign any positive integer value, including zero, with an upper limit of 2^30-1, or 1073741823 for each node. Image Builder automatically assigns the build number to the fourth node.

           *Patterns:* You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-workflow.html#cfn-imagebuilder-workflow-version
        '''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def change_description(self) -> typing.Optional[builtins.str]:
        '''Describes what change has been made in this version of the workflow, or what makes this version different from other versions of the workflow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-workflow.html#cfn-imagebuilder-workflow-changedescription
        '''
        result = self._values.get("change_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data(self) -> typing.Optional[builtins.str]:
        '''Contains the UTF-8 encoded YAML document content for the workflow.

        Alternatively, you can specify the ``uri`` of a YAML document file stored in Amazon S3. However, you cannot specify both properties.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-workflow.html#cfn-imagebuilder-workflow-data
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Describes the workflow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-workflow.html#cfn-imagebuilder-workflow-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the KMS key that is used to encrypt this workflow resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-workflow.html#cfn-imagebuilder-workflow-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags that apply to the workflow resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-workflow.html#cfn-imagebuilder-workflow-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def uri(self) -> typing.Optional[builtins.str]:
        '''The ``uri`` of a YAML component document file.

        This must be an S3 URL ( ``s3://bucket/key`` ), and the requester must have permission to access the S3 bucket it points to. If you use Amazon S3, you can specify component content up to your service quota.

        Alternatively, you can specify the YAML document inline, using the component ``data`` property. You cannot specify both properties.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-workflow.html#cfn-imagebuilder-workflow-uri
        '''
        result = self._values.get("uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkflowProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnComponent",
    "CfnComponentProps",
    "CfnContainerRecipe",
    "CfnContainerRecipeProps",
    "CfnDistributionConfiguration",
    "CfnDistributionConfigurationProps",
    "CfnImage",
    "CfnImagePipeline",
    "CfnImagePipelineProps",
    "CfnImageProps",
    "CfnImageRecipe",
    "CfnImageRecipeProps",
    "CfnInfrastructureConfiguration",
    "CfnInfrastructureConfigurationProps",
    "CfnLifecyclePolicy",
    "CfnLifecyclePolicyProps",
    "CfnWorkflow",
    "CfnWorkflowProps",
]

publication.publish()

def _typecheckingstub__cee6f52d40719e283a6d76c8b6a6d4fb48180c9c7f4901a21ff32e8627d45b9e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    platform: builtins.str,
    version: builtins.str,
    change_description: typing.Optional[builtins.str] = None,
    data: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    supported_os_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40b669a1c43c3b3079f4db289296a5190bc19737cdacec67b41121ffeb77db84(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa56b38fd57c0ef3c75a0f7854e12f5650c218ee9da1e6a0fc3566f2d0bb250e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad2e949f47b8d1f3fa28e8aecc85097ba0e494b4114a67857ca7449b71baa7eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0512be6fd4c9842ff94428cb157263d19145ec3979a5af8b91ef02839bf0a59a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff0f73dccd3a4b2cd5091fd524dac54a149f454f8e4b95ebdbc8bf2d847d695a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__789ae8523d5582d7b263d5e4e40edc52e6cd54e33a4a8a9da22ce8a46158e664(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87721af8240816306f3213003a08de03e0d6e02c52557a8099b6c11f6103e348(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fc3d50c994f77416bd1fab3b0e2629efe837f684884eb6608ef71e4e7806ece(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa81ab3ceec1f0c67b1340d453195ce21694d45be0f3dc0f50e114a74e30b9dd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0eed3fe1a4cf44875823a85284d0c8b80bbf155582b1e12432340633e2da8c80(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4a5d66d386d51bc332acca6c875fb548297567b633e53e35d7da1075f8af119(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6efe7a7fb79c1c8d2effb9d5fa5a6b2b46eefe80a1dce4011093db23ed26368d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__802f9cef9476f7041238f4927a50fed552e7bbbc1054ce0eda41a7b9d75d2d80(
    *,
    name: builtins.str,
    platform: builtins.str,
    version: builtins.str,
    change_description: typing.Optional[builtins.str] = None,
    data: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    supported_os_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c468d5dd819e845b41b9c236fc6bca416c9fb91fff1a793739f89182c73cf78(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    components: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerRecipe.ComponentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    container_type: builtins.str,
    name: builtins.str,
    parent_image: builtins.str,
    target_repository: typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerRecipe.TargetContainerRepositoryProperty, typing.Dict[builtins.str, typing.Any]]],
    version: builtins.str,
    description: typing.Optional[builtins.str] = None,
    dockerfile_template_data: typing.Optional[builtins.str] = None,
    dockerfile_template_uri: typing.Optional[builtins.str] = None,
    image_os_version_override: typing.Optional[builtins.str] = None,
    instance_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerRecipe.InstanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    platform_override: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    working_directory: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d50e15547c09a07cb55adb827ff274c67146acfeb8490458d35e268611168856(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d5b6469a4e69272bf90156a8e5963ff835a02f4987b9ff4170884d2625b3457(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be58a433b37609a8e2de38ae9ea0ad32cd2b7ed8705e29e10ecdad873c143b52(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContainerRecipe.ComponentConfigurationProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98ecd1f7f5bf2b0da0835263286f741cee38c6800e6fd533eb229b76138500e1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3ef18d5728c61a917559c323946757e6be1a7002f20cf91c52bc506c172ef2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06c6a4b42b1e6b26e1648401dcfd1d06a1f54758e6c6c4292c89fcf15aa87b82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a16a6d97d9686aa1fd4e3b9328c4a5a0dd0f749b7ac9889c9035ec5469af398(
    value: typing.Union[_IResolvable_da3f097b, CfnContainerRecipe.TargetContainerRepositoryProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa6a91dc94efb2a0dd29d944476e7c6c946c97198b7d6387befefe9d97730e5c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1009255c37bcedc70c2d5b858539398c6cb8a82b82af65eaec140a4b08d8f0fc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23f0305ca1ea92dfb02b54888f1e788091cf6224ebfaefc930cb4edf9f55995a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61ed4ed2ebf18638bf7613451687122c6102ece171fee5ba16df758fa37bf12d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6285254ee49b214efc138390c48b3810e45bc304eedb7b87306c2c5e93db5e5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba690c6c26b1b3cf3117b63e2f6c837ceb170174c72f085086b1fc988d04a3ab(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnContainerRecipe.InstanceConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__817846eff0dde79bf417507baefc907f2d5812073cd40bbaec60927922c4c1b6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17de30bf20bf8e3ad9fd881a20af8cf79eb9d79af37be867e8f89d583a732b3a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a1dfc2cdd2904573a5d1ce3b6718ef45ba5250e56b864c223bc455a6441ee05(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4d9839ccfba608b5591637bb041c5f1859bc5d3d5efc70fc1dbfd3fb7ee6f05(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7567002303b2f6603b88563d854827508e4c039225dbff9d2d6511ea3f96404d(
    *,
    component_arn: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerRecipe.ComponentParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b194072bb1a463ebdad3622ec5d6ba4a31027cdc36eed1498bba4ffa49ccc1b6(
    *,
    name: builtins.str,
    value: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4001b2a6da944a393abf9e0bec60a2ee3d635268cb764774d8cb4d5cdc96a2dc(
    *,
    delete_on_termination: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    iops: typing.Optional[jsii.Number] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    snapshot_id: typing.Optional[builtins.str] = None,
    throughput: typing.Optional[jsii.Number] = None,
    volume_size: typing.Optional[jsii.Number] = None,
    volume_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50cdb18d882d2c0ab0523c7289014397408b0fd15593ed1334bacde7c89c007e(
    *,
    device_name: typing.Optional[builtins.str] = None,
    ebs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerRecipe.EbsInstanceBlockDeviceSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    no_device: typing.Optional[builtins.str] = None,
    virtual_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94feecd62024b3049c94588a2a0ff057d5b85caf4f2a481eda383b2a7df9a710(
    *,
    block_device_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerRecipe.InstanceBlockDeviceMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    image: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34199ca5f676bc80945fe7e849c29056158da64657ff83277eecd5cd3b62b859(
    *,
    repository_name: typing.Optional[builtins.str] = None,
    service: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67f8d0f3d1045e15583795ba863ee1d218908e506567e7d12e0aa5861d44ab17(
    *,
    components: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerRecipe.ComponentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    container_type: builtins.str,
    name: builtins.str,
    parent_image: builtins.str,
    target_repository: typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerRecipe.TargetContainerRepositoryProperty, typing.Dict[builtins.str, typing.Any]]],
    version: builtins.str,
    description: typing.Optional[builtins.str] = None,
    dockerfile_template_data: typing.Optional[builtins.str] = None,
    dockerfile_template_uri: typing.Optional[builtins.str] = None,
    image_os_version_override: typing.Optional[builtins.str] = None,
    instance_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerRecipe.InstanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    platform_override: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    working_directory: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__424bed49628b17ab96124c2266e56c022dd960de454a320aa631249933b84238(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    distributions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDistributionConfiguration.DistributionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8c93c8ee1a0cc67cfc5275e236e88b22ff03327ff16d67734ff3d6686a9dbaa(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdfd733425feec8767a979bc76f1a0c04fdefa9d54e164ffd669456e35f87530(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__417065f936904d5b1e579e864b23c068bcff521f939e2da134dd0f6a48a5e283(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDistributionConfiguration.DistributionProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d3861330f505671935d810b9849097b7dcf3fe793afbea38a794f2efbf3e528(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95c7f83d3e50ed6eaf60e3cbf261f7ba851636ae7674d9e772ea1b967db2676e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e9679e68354d4ed7fd182e9633596a907a1b8af3224253b40b59ab4ac641ac0(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78b16e4a7c76877b5dc3dc5bc7508b79d60aed5becf1610e01c5aba5acf7f818(
    *,
    ami_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    description: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    launch_permission_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDistributionConfiguration.LaunchPermissionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    target_account_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__125e3573ab2e6c73f141e1784bd0d6c99de3714f6122708d9404d939bfa152b5(
    *,
    container_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    target_repository: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDistributionConfiguration.TargetContainerRepositoryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29d1f34d5faec16ba828ad2333ee9218a18df31808a5a350be9b29d048555c54(
    *,
    region: builtins.str,
    ami_distribution_configuration: typing.Any = None,
    container_distribution_configuration: typing.Any = None,
    fast_launch_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDistributionConfiguration.FastLaunchConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    launch_template_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDistributionConfiguration.LaunchTemplateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    license_configuration_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55c8e6821fd98707615f7982782feb32e6fa579e64adbef7db96af2d7b0c40ea(
    *,
    account_id: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    launch_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDistributionConfiguration.FastLaunchLaunchTemplateSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    max_parallel_launches: typing.Optional[jsii.Number] = None,
    snapshot_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDistributionConfiguration.FastLaunchSnapshotConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__021d1b3db5c8ca8f6806bf8d9d829821d8e3b628222bed84a3d6f72106555ee3(
    *,
    launch_template_id: typing.Optional[builtins.str] = None,
    launch_template_name: typing.Optional[builtins.str] = None,
    launch_template_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__742f14fac4b1a3338b9e181cf90ffe52f3bc892fe33258d6ee8e31f32b62e25f(
    *,
    target_resource_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0184c66c3ce1b1a9581759138f6b03cdf0b49876c0cd4e7191f619d41bc6a8f7(
    *,
    organizational_unit_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    organization_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    user_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    user_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b4c1c669ce6e1367a73060d15f089faa5ce58e96063ee38204bf9af12043035(
    *,
    account_id: typing.Optional[builtins.str] = None,
    launch_template_id: typing.Optional[builtins.str] = None,
    set_default_version: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd67a7cda75ae308d03a62ceb5b017b8de54cd08fd47374326a441ec680438a5(
    *,
    repository_name: typing.Optional[builtins.str] = None,
    service: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f16c19e0cbb34ea9e02eb4cfcaa69a6cdf4c60af0ca2736a9d0dd6b74445c9d8(
    *,
    distributions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDistributionConfiguration.DistributionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1406bc225111bc54a87c50d1d8180aed46d22e10134235c4fa581d3137e5bddf(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    infrastructure_configuration_arn: builtins.str,
    container_recipe_arn: typing.Optional[builtins.str] = None,
    distribution_configuration_arn: typing.Optional[builtins.str] = None,
    enhanced_image_metadata_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    execution_role: typing.Optional[builtins.str] = None,
    image_recipe_arn: typing.Optional[builtins.str] = None,
    image_scanning_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImage.ImageScanningConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_tests_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImage.ImageTestsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    workflows: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImage.WorkflowConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5772703e735ab7511274ad4c83f3ee56bfacba182fbe209189bed84d493649c5(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8052419a8d8b963d7c9b1b75cd6654f49a4ad3b49a754eb0e90c63bf70d1fa6b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a190431e330e97015561230a0d9b0477abed6793472228169b2ce3d498e18c8e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6e036331c49a5f902af4e72bc4f291c89a7f5f03a4453a10c55e0f2bde10ac7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__889890f98c732641897f78af3545740dd9c7c236d01f0d3e3c038263bc80498c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5e9d51fefc7d1e1bc910eea2e49d7094b0e13fbcbdb19541025c130619890a1(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94668d5e5e8eb55befbec215426086ba0771bd0ba96fb3d147c8a3a31346c1b4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__308fe5eed4210d0740b5702c5e8451b42918877aa2da6ce7940407e47733f736(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4b9045c9ec605b9ea33dd14470f4bb513ecf0e38fc4830ac2ce68670a13c7e7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnImage.ImageScanningConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e66513eb336b5e3ebc869a424fc1c9d0df46865060b926ea955e8a9df5c29efa(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnImage.ImageTestsConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0e6ba55682dabdf30b5bb38534688ff3dbd8c6a8044f77eb6180bb8d815ceb8(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97523463f160d96768440c69c3873ddb86b0d5ac22775529d935489f314a6737(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnImage.WorkflowConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e752dc7f51b470c209f9741b4ee9c9b1b8ab926ba9ba46ae3160a1876f4c556(
    *,
    container_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    repository_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__155636d4b270ff858336d445a5c3a434623faaa989317a61b024d7142948911e(
    *,
    ecr_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImage.EcrConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_scanning_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8cfede11f4b11fc577c8fddf9438af7db50acddcb364073adeaf606a8eeb506(
    *,
    image_tests_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    timeout_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a82febc1a7fafa923553117d043e1c9475f024e84431a24b2b8a4d66c3a73ed6(
    *,
    on_failure: typing.Optional[builtins.str] = None,
    parallel_group: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImage.WorkflowParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    workflow_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd39ec0b160c618e3ecd8108c0d630fdf1cd5460552b39c91e63a7ddbf1f09b7(
    *,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2d099702ab4ebcb03c34ae00fedabfa81a0c5d3662aa1605c47ff1fcaf0b3a5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    infrastructure_configuration_arn: builtins.str,
    name: builtins.str,
    container_recipe_arn: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    distribution_configuration_arn: typing.Optional[builtins.str] = None,
    enhanced_image_metadata_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    execution_role: typing.Optional[builtins.str] = None,
    image_recipe_arn: typing.Optional[builtins.str] = None,
    image_scanning_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImagePipeline.ImageScanningConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_tests_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImagePipeline.ImageTestsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImagePipeline.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    workflows: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImagePipeline.WorkflowConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8446f898a5728a2569b09b248ec039f33570944e39527609ca77ad743aa2981(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdf805d788cd08883285d15aaa10bc7ba4e53741d409a94e68aed68476e684ce(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6e5ee80f47b2929d2902efd995e0248d5c8ae9ed8dbf8d1e4fb71b7855eabb8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfcf09da283c32d27a69667105a1cc2b1df47359866f14696d1326d14bde2b6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f690c089494ff15e372c4f0a35406b7a51b38c81b470cac3aa12ba03f2e931a1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78b1f1bb0cc881de12c4611c1d5f8f4cff0231dd64a754971cca27ad89c67de1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b07039612cc24dd193ca16223d4b76d3c790b575da52c3cdf9cfc191185287c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca199afdbf91ba45c1ad064f501dfd9423062e198e14171ce04f43dd1f06dd41(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ebcf34a24070ac97fff298c2904bf78391a1a430eba771320445f80a0ff1f2d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87996b3149c3f25f36e8d94641a0031c8b619b9cf13e699704fbe22cc370d491(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0daaa16e9e563843b4889c318a714595d70349ae6d61ed80bf9f14b99f18be56(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnImagePipeline.ImageScanningConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9e327e008ef0b95ddde8197947e86b8bc9160733d270caa11482a88db735cc2(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnImagePipeline.ImageTestsConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7493819df4798ffd45cd31ff99c66a5c22065a41d47c9c3792eaaf9d4c4150a1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnImagePipeline.ScheduleProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3ffb79c4adfe85e809f1adea3ddcdf54c817c4a4f4c97a2f65d9c38b4e0f38b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10f1255c06095afaded88e7544051acdac47218f9be5e78474eeaaedafede76f(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d31373519ea07e5936785c1446524bda21756ca2eb6c12f87303f5a12dc18c4f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnImagePipeline.WorkflowConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ad9ee4365967b325aac7636f417b9a691b4b50560fe8f594198933e7ed13aca(
    *,
    container_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    repository_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e9c4bcdf41e69c9224e93798644f93b8f44565c0bd7edb8e6b49dc0367bc5b6(
    *,
    ecr_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImagePipeline.EcrConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_scanning_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae3643f34d20caf9e518f587e7eacbe6f2163c4d76025d717d8d8ea1b31feed6(
    *,
    image_tests_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    timeout_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02783d051498bb630cd6a27d361c0750914a59f05623585e0808549e9248bae0(
    *,
    pipeline_execution_start_condition: typing.Optional[builtins.str] = None,
    schedule_expression: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__665a1259d83ae867bae960e30b1d2c041292af4f49417c7f7eca3bd35857c4a3(
    *,
    on_failure: typing.Optional[builtins.str] = None,
    parallel_group: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImagePipeline.WorkflowParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    workflow_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e3c12bbd170116ab79a812e4141a317f3b456ad0a64acefae39ebbdf20aa068(
    *,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95f10c4451c6bf3f2cf15951831cd372e35975262c0be294c1ae7c774045ad9b(
    *,
    infrastructure_configuration_arn: builtins.str,
    name: builtins.str,
    container_recipe_arn: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    distribution_configuration_arn: typing.Optional[builtins.str] = None,
    enhanced_image_metadata_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    execution_role: typing.Optional[builtins.str] = None,
    image_recipe_arn: typing.Optional[builtins.str] = None,
    image_scanning_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImagePipeline.ImageScanningConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_tests_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImagePipeline.ImageTestsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImagePipeline.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    workflows: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImagePipeline.WorkflowConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f217922888735234464ee573256caba679b2c1215a99c91ad609c9c75d22d47(
    *,
    infrastructure_configuration_arn: builtins.str,
    container_recipe_arn: typing.Optional[builtins.str] = None,
    distribution_configuration_arn: typing.Optional[builtins.str] = None,
    enhanced_image_metadata_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    execution_role: typing.Optional[builtins.str] = None,
    image_recipe_arn: typing.Optional[builtins.str] = None,
    image_scanning_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImage.ImageScanningConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_tests_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImage.ImageTestsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    workflows: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImage.WorkflowConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b92e909d03413ceab5b5ff0737ae582bf88ebb71e7e89f62cc57922d15e14688(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    components: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImageRecipe.ComponentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    parent_image: builtins.str,
    version: builtins.str,
    additional_instance_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImageRecipe.AdditionalInstanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    block_device_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImageRecipe.InstanceBlockDeviceMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    working_directory: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d29dc31863102f18f5de9644424c5516f4485067e44de21830a39789f498ba1(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33501f1fede0354860af9711623bf5d9a7cf482716f9a1ca43757a3dcf91988e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aa78705ac6fd96606f64b6a20b05295ef53335ad8d08aa3a0a956ce040dd62c(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnImageRecipe.ComponentConfigurationProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02513ed6c05b6aecc9c7c9494100db2c7a4dd5eecdafd9ed44b5ac5fe0cf5fce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47f2fc68afde57d2508c6a78ab44bf38f32703a4704e869ddfc9e1abda62a8fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73fc08f00d9d100507462b08c6b2bbdf08927d138dd7cc3a56174082719ac0f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcc3e434aa1a301be5e1a5341bc64287bfcf82761f08ef98de5711b1b1bc6038(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnImageRecipe.AdditionalInstanceConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f9ee0bcfa7d5f48279416991e3a05c2143a695ca605b7c215eb5e8cc38d2174(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnImageRecipe.InstanceBlockDeviceMappingProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f01685cf10dbac31ad7c61e710cacf41f2fc80e0f75749cd095d2cc67a293114(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17b26e47cb85f6d4988562240bd59263533005f817aafcbcd75d58254cc7edad(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48af3414043e30c9e59d200f83f2c6ae4f17671a82842e7504894e55cd148e59(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ca77073ea53566254c7a7a5d44918ec6646ad40315ed7ca9745e76d11503a2d(
    *,
    systems_manager_agent: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImageRecipe.SystemsManagerAgentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_data_override: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3572edbb0a8e7d685c2a1b27e3b1ad62a69873f648cc201056f7b56000df8cbd(
    *,
    component_arn: typing.Optional[builtins.str] = None,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImageRecipe.ComponentParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03682261f9797b7505c9117911d4b41776919fa663a3e5511922fc505c2d63de(
    *,
    name: builtins.str,
    value: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecfec9c1a0d0607e08e359aadb38abc8238828e27448a6003ed03d928265c878(
    *,
    delete_on_termination: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    encrypted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    iops: typing.Optional[jsii.Number] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    snapshot_id: typing.Optional[builtins.str] = None,
    throughput: typing.Optional[jsii.Number] = None,
    volume_size: typing.Optional[jsii.Number] = None,
    volume_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49d4c4575e6e8aa63b1188dcd39472139fc5b35a563c27e7b8a0bdf273eb23ff(
    *,
    device_name: typing.Optional[builtins.str] = None,
    ebs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImageRecipe.EbsInstanceBlockDeviceSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    no_device: typing.Optional[builtins.str] = None,
    virtual_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad92f3ddc08f7f471aea45f4940171af1f13b6aca47dcb6cecd2627b25787032(
    *,
    uninstall_after_build: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a289ec10c5f4c9443f1dfb0dc4ecb78a20e5f6e491ed688cb2e3a59ad3d6c88a(
    *,
    components: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImageRecipe.ComponentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    parent_image: builtins.str,
    version: builtins.str,
    additional_instance_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImageRecipe.AdditionalInstanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    block_device_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnImageRecipe.InstanceBlockDeviceMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    working_directory: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8df8a03094d1fe92963a315a657a78657df102ba9fbe66eda2c26bb8eac04479(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_profile_name: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    instance_metadata_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    key_pair: typing.Optional[builtins.str] = None,
    logging: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInfrastructureConfiguration.LoggingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    sns_topic_arn: typing.Optional[builtins.str] = None,
    subnet_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    terminate_instance_on_failure: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74669b982a2428b807ea1c9303f9f6436fc7a33f979476a1d362fd55ce646030(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8aa110274058962353c14921a3072455f5cdd4c719f811fc3f2016a06124c7d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__567cc48eac63fe7658bac22f92aeaef43a88d570458848aaa616a242a0016f53(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89c441de9755e4528e9501910ffe1b142c79898b858765b54a344edeeb4efcfd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11b2528bf4f2f0bc20addb08562906606bf8256aa4bf3a799c73a8f967d324d5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3afa319d538769cad5489226f5f03b6a41c1e6d9b00312872b1f94b18c5a5634(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a0b92316d3ef8d02213fb858da5f3aa9757691f73babe9e86e3ee4702b556d8(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__087a308543348827d9b884784d17ddc6bdce8ecaa0b65300cd6ddb789fd692fe(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d17651b37e2f4aa5ce6c6076a887fc7270cae14e1f7330e9b48dc5412a83cad9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInfrastructureConfiguration.LoggingProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4e6c2bbdd440425ebe7067a9a03bf4079bbfef4001b7877cb6ce3dcd44c4cb0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__219d1428ff3821670f8bcafa92479bb91549e3dc36bf8751ba20a7ebcd289712(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1588cdfeef854d08e3c06f677829311cc7ab992c28b306cad9fb6cbf3909a7ab(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e15394d6263f20f733a1287663578d35f680875e7ea77d8afb2d17f6150efe9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc5a3a7adbaeb667678ab511c655f1ae0df213cbf0afc14685b60d46b8852e6e(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7249b107702cdaa94b0beadeaf7622e73dee8dfe6ae5b06188bce3dbefe11423(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1141979976cfe1199d14e004e82c4b5c7d9823434580281c214438e94c027783(
    *,
    http_put_response_hop_limit: typing.Optional[jsii.Number] = None,
    http_tokens: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7c7b472c2127725031940b44ae4cf826450bdc016814ad2356cca6734e1ab2e(
    *,
    s3_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInfrastructureConfiguration.S3LogsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__606aaff62e915101e470a1274dc963d43831117f9a85493e01f09a1eebe8e6b6(
    *,
    s3_bucket_name: typing.Optional[builtins.str] = None,
    s3_key_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf8c493013f64742391c2bf93c7050f371ffeff0d9a35a3791f0b9fbb6019d47(
    *,
    instance_profile_name: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    instance_metadata_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInfrastructureConfiguration.InstanceMetadataOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    key_pair: typing.Optional[builtins.str] = None,
    logging: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInfrastructureConfiguration.LoggingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    sns_topic_arn: typing.Optional[builtins.str] = None,
    subnet_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    terminate_instance_on_failure: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b441913a83fc39b85885667ae1a4a4add28d162c2540cbe5daf576611d89c45(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    execution_role: builtins.str,
    name: builtins.str,
    policy_details: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.PolicyDetailProperty, typing.Dict[builtins.str, typing.Any]]]]],
    resource_selection: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.ResourceSelectionProperty, typing.Dict[builtins.str, typing.Any]]],
    resource_type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__997e669ab2d70b66c1108c2056de12da3e2fbc0e1c654655fa0e1f32c1ff9bf7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fdfac6ebe159cab7b348eba63d9c7a30850f500328f1f2b743390507b1dfbf8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7df981cc48b094d72f929d5a9e77620bf8387063d8f4c0452877bf8470bf5bb0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__318284e60031de2bbfe99eda11ff55a12c3bb44318c2cbeeaa90b5f7ee610f25(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73010b9d10e9b09b5491821779561d5585cd76eea481797eb3122d8b9ee8508c(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLifecyclePolicy.PolicyDetailProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa4f13ae99ebd0f4eaf2e189e0687bda23b3ff6f7f3a1716d1eadfe529976a3c(
    value: typing.Union[_IResolvable_da3f097b, CfnLifecyclePolicy.ResourceSelectionProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64fe4860941ec7baf85181482da4f12aa4fb911b934f3b02a8a7b1c56d2c8226(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e996dee13897dcb4e83e73e4d73bcd855080996d0417f2f74f5628205c5234a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5495e49fe08c27baf854c2e3f3005125f1e5f20e9b6cacfa47e41c4d319b9034(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4e72af6227539e4a5e696bb41f6d2e0df2d6f0d3f943785a49eefa13944b953(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b3703bb1789e55ea0843aa78bd8e86cf376052d4aa4bb2c85cc78069a805ac0(
    *,
    type: builtins.str,
    include_resources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.IncludeResourcesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05134c25c9cdb0bbc6009541532ec2b9cbb483cc3413a7a624d12232b29a003b(
    *,
    is_public: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    last_launched: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.LastLaunchedProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    shared_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    tag_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__284c02a995f46d8f38f0f1c9b8aa842e2acafc4d2a0cd2a09a7ccfd618f97a70(
    *,
    amis: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.AmiExclusionRulesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tag_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae34685f55ed44c43efb8db0e7558cbf62100f081f22ea4b62ca781cc202e062(
    *,
    type: builtins.str,
    value: jsii.Number,
    retain_at_least: typing.Optional[jsii.Number] = None,
    unit: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a71a92276a1b69aaf0a934da7eaa5abd8843fdc821b5c0c5aa37a81d55eed8d(
    *,
    amis: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    containers: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    snapshots: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b873acb7ad8c3039d17767ab82c3f8a2b2b0d314b00e2e45dc73e897b6495cfe(
    *,
    unit: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf722d246758df8a2a9189fea40552c11f02659c91c03c64c9245d5331394cd0(
    *,
    action: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.ActionProperty, typing.Dict[builtins.str, typing.Any]]],
    filter: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.FilterProperty, typing.Dict[builtins.str, typing.Any]]],
    exclusion_rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.ExclusionRulesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16450d1b17b0ea545ae61c434c161a1873c39c7215299585bcf233621d5c8c5e(
    *,
    name: builtins.str,
    semantic_version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a50d1f1937c770dfb0439cdf4e09d340344cb42f76c244b1320fe680a4c4e82c(
    *,
    recipes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.RecipeSelectionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tag_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d645dc30df568adc41cd2d0c464f623b51b54d8bb6b1351018d90d6c338846f(
    *,
    execution_role: builtins.str,
    name: builtins.str,
    policy_details: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.PolicyDetailProperty, typing.Dict[builtins.str, typing.Any]]]]],
    resource_selection: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLifecyclePolicy.ResourceSelectionProperty, typing.Dict[builtins.str, typing.Any]]],
    resource_type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd82b8722476efd9ae3c84a0cf5b8f1d6b48550745017b0d128afabf5f24b5b2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    type: builtins.str,
    version: builtins.str,
    change_description: typing.Optional[builtins.str] = None,
    data: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb3d8659b8d763c14b7737c9410afacee05a27e95b64c0ed4b73165d968ab03c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56f66168df4b459392919a074261a67669f13f593780de274f36bbeb7bc11b3c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9ca2ede358f8e6d6f27ece2e03d7d871d14d1daaeba3cb4c788afc33c2bc227(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41b009fd9ca27b9f352338a895a62a4f074e2c7eb510b43e13f8792747f571c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ce08768a8ac00cab8a7fb60330cb7f716c6376d6d056e8ade1e44a26436417d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b245fa74b6c4cb04ff6723da66ff8f8cd6af6cd5bcb55ede52fbb7a4519992d9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57d165db317968c3d0b9096bb379e7548f28dec9638ea2beebdc78b7bdf0e904(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b296abb92cd399ea05e8c119ac7fdf0c7ac681e045dc5b83cfc6d9b0d97b7233(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b8bb7c0820c2fd1205773d0df64a2953848236b9ead853f32d65a2239aaafa0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1212a2dd4ab9ee1b3006c19c3027125ab0148561c4bc08b5d80fc0e29bfdf854(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e36c0e0583778b96be119919e9f8e273d4b8ff0bfa5e58c3049f2cc89a520dd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35d88d62d7ed1f4b6deb48b19f5f6a93db101eada9232a0e7f6cc8c59ce9e078(
    *,
    name: builtins.str,
    type: builtins.str,
    version: builtins.str,
    change_description: typing.Optional[builtins.str] = None,
    data: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
