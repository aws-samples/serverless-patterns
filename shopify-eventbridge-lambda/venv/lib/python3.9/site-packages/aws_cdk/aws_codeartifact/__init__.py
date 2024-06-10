'''
# AWS::CodeArtifact Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_codeartifact as codeartifact
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for CodeArtifact construct libraries](https://constructs.dev/search?q=codeartifact)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::CodeArtifact resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodeArtifact.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::CodeArtifact](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodeArtifact.html).

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
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDomain(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codeartifact.CfnDomain",
):
    '''The ``AWS::CodeArtifact::Domain`` resource creates an AWS CodeArtifact domain.

    CodeArtifact *domains* make it easier to manage multiple repositories across an organization. You can use a domain to apply permissions across many repositories owned by different AWS accounts. For more information about domains, see the `Domain concepts information <https://docs.aws.amazon.com/codeartifact/latest/ug/codeartifact-concepts.html#welcome-concepts-domain>`_ in the *CodeArtifact User Guide* . For more information about the ``CreateDomain`` API, see `CreateDomain <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_CreateDomain.html>`_ in the *CodeArtifact API Reference* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-domain.html
    :cloudformationResource: AWS::CodeArtifact::Domain
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_codeartifact as codeartifact
        
        # permissions_policy_document: Any
        
        cfn_domain = codeartifact.CfnDomain(self, "MyCfnDomain",
            domain_name="domainName",
        
            # the properties below are optional
            encryption_key="encryptionKey",
            permissions_policy_document=permissions_policy_document,
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
        domain_name: builtins.str,
        encryption_key: typing.Optional[builtins.str] = None,
        permissions_policy_document: typing.Any = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_name: A string that specifies the name of the requested domain.
        :param encryption_key: The ARN of an AWS Key Management Service (AWS KMS) key associated with a domain.
        :param permissions_policy_document: The document that defines the resource policy that is set on a domain.
        :param tags: A list of tags to be applied to the domain.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fb789fedc85855c1509949f2cf10c2dd0562b804efa5820bf00577753b9d8b7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDomainProps(
            domain_name=domain_name,
            encryption_key=encryption_key,
            permissions_policy_document=permissions_policy_document,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46d9fe40fc43e31cea0a6a2e9dfd751eb16b8a46da32d7dccd9603f803712f90)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a2a99c05ff9a326ace2300aa6eea08d05c5801006bd439dac683557fc824f972)
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
        '''When you pass the logical ID of this resource, the function returns the Amazon Resource Name (ARN) of the domain.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrEncryptionKey")
    def attr_encryption_key(self) -> builtins.str:
        '''When you pass the logical ID of this resource, the function returns the key used to encrypt the domain.

        :cloudformationAttribute: EncryptionKey
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEncryptionKey"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''When you pass the logical ID of this resource, the function returns the name of the domain.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

    @builtins.property
    @jsii.member(jsii_name="attrOwner")
    def attr_owner(self) -> builtins.str:
        '''When you pass the logical ID of this resource, the function returns the 12-digit account number of the AWS account that owns the domain.

        :cloudformationAttribute: Owner
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwner"))

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
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''A string that specifies the name of the requested domain.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__020dc2753ebcfeb3fc3126169a639eb6863967fddf54f8990d248b3c17684e90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> typing.Optional[builtins.str]:
        '''The ARN of an AWS Key Management Service (AWS KMS) key associated with a domain.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionKey"))

    @encryption_key.setter
    def encryption_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a60707c2e5754637c6feec657151278ead04566ec407a5201952b87113e7daa8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionKey", value)

    @builtins.property
    @jsii.member(jsii_name="permissionsPolicyDocument")
    def permissions_policy_document(self) -> typing.Any:
        '''The document that defines the resource policy that is set on a domain.'''
        return typing.cast(typing.Any, jsii.get(self, "permissionsPolicyDocument"))

    @permissions_policy_document.setter
    def permissions_policy_document(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__912eada525b5990b51696702eabe0044019487d7cefa00a70be77c94c889c313)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionsPolicyDocument", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags to be applied to the domain.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3d141e3a88261a459532756257673073502431714e2b0bae8c140a9b055f07b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codeartifact.CfnDomainProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "encryption_key": "encryptionKey",
        "permissions_policy_document": "permissionsPolicyDocument",
        "tags": "tags",
    },
)
class CfnDomainProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        encryption_key: typing.Optional[builtins.str] = None,
        permissions_policy_document: typing.Any = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDomain``.

        :param domain_name: A string that specifies the name of the requested domain.
        :param encryption_key: The ARN of an AWS Key Management Service (AWS KMS) key associated with a domain.
        :param permissions_policy_document: The document that defines the resource policy that is set on a domain.
        :param tags: A list of tags to be applied to the domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-domain.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codeartifact as codeartifact
            
            # permissions_policy_document: Any
            
            cfn_domain_props = codeartifact.CfnDomainProps(
                domain_name="domainName",
            
                # the properties below are optional
                encryption_key="encryptionKey",
                permissions_policy_document=permissions_policy_document,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed4a67a72fcc7050f3a4ea650fb97fc3375ca5e90727251a483297144826487d)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            check_type(argname="argument permissions_policy_document", value=permissions_policy_document, expected_type=type_hints["permissions_policy_document"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
        }
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if permissions_policy_document is not None:
            self._values["permissions_policy_document"] = permissions_policy_document
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''A string that specifies the name of the requested domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-domain.html#cfn-codeartifact-domain-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[builtins.str]:
        '''The ARN of an AWS Key Management Service (AWS KMS) key associated with a domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-domain.html#cfn-codeartifact-domain-encryptionkey
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions_policy_document(self) -> typing.Any:
        '''The document that defines the resource policy that is set on a domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-domain.html#cfn-codeartifact-domain-permissionspolicydocument
        '''
        result = self._values.get("permissions_policy_document")
        return typing.cast(typing.Any, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags to be applied to the domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-domain.html#cfn-codeartifact-domain-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDomainProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnPackageGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codeartifact.CfnPackageGroup",
):
    '''Creates a package group.

    For more information about creating package groups, including example CLI commands, see `Create a package group <https://docs.aws.amazon.com/codeartifact/latest/ug/create-package-group.html>`_ in the *CodeArtifact User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-packagegroup.html
    :cloudformationResource: AWS::CodeArtifact::PackageGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_codeartifact as codeartifact
        
        cfn_package_group = codeartifact.CfnPackageGroup(self, "MyCfnPackageGroup",
            domain_name="domainName",
            pattern="pattern",
        
            # the properties below are optional
            contact_info="contactInfo",
            description="description",
            domain_owner="domainOwner",
            origin_configuration=codeartifact.CfnPackageGroup.OriginConfigurationProperty(
                restrictions=codeartifact.CfnPackageGroup.RestrictionsProperty(
                    external_upstream=codeartifact.CfnPackageGroup.RestrictionTypeProperty(
                        restriction_mode="restrictionMode",
        
                        # the properties below are optional
                        repositories=["repositories"]
                    ),
                    internal_upstream=codeartifact.CfnPackageGroup.RestrictionTypeProperty(
                        restriction_mode="restrictionMode",
        
                        # the properties below are optional
                        repositories=["repositories"]
                    ),
                    publish=codeartifact.CfnPackageGroup.RestrictionTypeProperty(
                        restriction_mode="restrictionMode",
        
                        # the properties below are optional
                        repositories=["repositories"]
                    )
                )
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
        domain_name: builtins.str,
        pattern: builtins.str,
        contact_info: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        domain_owner: typing.Optional[builtins.str] = None,
        origin_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackageGroup.OriginConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_name: The domain that contains the package group.
        :param pattern: The pattern of the package group. The pattern determines which packages are associated with the package group.
        :param contact_info: The contact information of the package group.
        :param description: The description of the package group.
        :param domain_owner: The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
        :param origin_configuration: Details about the package origin configuration of a package group.
        :param tags: A list of tags to be applied to the package group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a8aaa0852b2af2f8381bac18421469d96d102aa57d00f002433c862966b5603)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPackageGroupProps(
            domain_name=domain_name,
            pattern=pattern,
            contact_info=contact_info,
            description=description,
            domain_owner=domain_owner,
            origin_configuration=origin_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ce81570371704a4089ff9d234920c939ca57e8078fae0ed77580614455f254b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__73902d03882d362546bad830a7e307a86e67195728c52e0a2837b7a05804b314)
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
        '''When you pass the logical ID of this resource, the function returns the Amazon Resource Name (ARN) of the package group.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''The domain that contains the package group.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa73b50d995f7005fa2ec82631d018ef1849c9ffebef0125fbb6a4ee774b2163)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="pattern")
    def pattern(self) -> builtins.str:
        '''The pattern of the package group.'''
        return typing.cast(builtins.str, jsii.get(self, "pattern"))

    @pattern.setter
    def pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2718281da222f54ccce3c7a3bf6ded0f2b7a3bdcd9d30fbeea35abc3e153fd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pattern", value)

    @builtins.property
    @jsii.member(jsii_name="contactInfo")
    def contact_info(self) -> typing.Optional[builtins.str]:
        '''The contact information of the package group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contactInfo"))

    @contact_info.setter
    def contact_info(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26fdce972c6efcbdd12712f2d1406046a1aaf63a8d0f3da99813e261e4029f97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactInfo", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the package group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b9671c9b67b0351b5842cb8cda895b5db7d8202b0617a306719b29c79b2309d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="domainOwner")
    def domain_owner(self) -> typing.Optional[builtins.str]:
        '''The 12-digit account number of the AWS account that owns the domain.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainOwner"))

    @domain_owner.setter
    def domain_owner(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15d889231b62e097fa73baf944ef89bab375256fa4ae0bdb93c27049076c51c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainOwner", value)

    @builtins.property
    @jsii.member(jsii_name="originConfiguration")
    def origin_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackageGroup.OriginConfigurationProperty"]]:
        '''Details about the package origin configuration of a package group.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackageGroup.OriginConfigurationProperty"]], jsii.get(self, "originConfiguration"))

    @origin_configuration.setter
    def origin_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackageGroup.OriginConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63bcaafc797c7b557351ce8e1bfa571001310be1e41896261bec63105e81cae6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags to be applied to the package group.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e756db6ce537f9d80da313912b16eef0c2a610ee05772d30b4df98a4ddebee96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codeartifact.CfnPackageGroup.OriginConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"restrictions": "restrictions"},
    )
    class OriginConfigurationProperty:
        def __init__(
            self,
            *,
            restrictions: typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackageGroup.RestrictionsProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The package group origin configuration that determines how package versions can enter repositories.

            :param restrictions: The origin configuration settings that determine how package versions can enter repositories.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeartifact-packagegroup-originconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codeartifact as codeartifact
                
                origin_configuration_property = codeartifact.CfnPackageGroup.OriginConfigurationProperty(
                    restrictions=codeartifact.CfnPackageGroup.RestrictionsProperty(
                        external_upstream=codeartifact.CfnPackageGroup.RestrictionTypeProperty(
                            restriction_mode="restrictionMode",
                
                            # the properties below are optional
                            repositories=["repositories"]
                        ),
                        internal_upstream=codeartifact.CfnPackageGroup.RestrictionTypeProperty(
                            restriction_mode="restrictionMode",
                
                            # the properties below are optional
                            repositories=["repositories"]
                        ),
                        publish=codeartifact.CfnPackageGroup.RestrictionTypeProperty(
                            restriction_mode="restrictionMode",
                
                            # the properties below are optional
                            repositories=["repositories"]
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__46aa889310dd45252527135dfe1c0e1137811a871c8d0978ef0c8c7dcf8636fa)
                check_type(argname="argument restrictions", value=restrictions, expected_type=type_hints["restrictions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "restrictions": restrictions,
            }

        @builtins.property
        def restrictions(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnPackageGroup.RestrictionsProperty"]:
            '''The origin configuration settings that determine how package versions can enter repositories.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeartifact-packagegroup-originconfiguration.html#cfn-codeartifact-packagegroup-originconfiguration-restrictions
            '''
            result = self._values.get("restrictions")
            assert result is not None, "Required property 'restrictions' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnPackageGroup.RestrictionsProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OriginConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codeartifact.CfnPackageGroup.RestrictionTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "restriction_mode": "restrictionMode",
            "repositories": "repositories",
        },
    )
    class RestrictionTypeProperty:
        def __init__(
            self,
            *,
            restriction_mode: builtins.str,
            repositories: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The ``RestrictionType`` property type specifies the package group origin configuration restriction mode, and the repositories when the ``RestrictionMode`` is set to ``ALLOW_SPECIFIC_REPOSITORIES`` .

            :param restriction_mode: The package group origin restriction setting. When the value is ``INHERIT`` , the value is set to the value of the first parent package group which does not have a value of ``INHERIT`` .
            :param repositories: The repositories to add to the allowed repositories list. The allowed repositories list is used when the ``RestrictionMode`` is set to ``ALLOW_SPECIFIC_REPOSITORIES`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeartifact-packagegroup-restrictiontype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codeartifact as codeartifact
                
                restriction_type_property = codeartifact.CfnPackageGroup.RestrictionTypeProperty(
                    restriction_mode="restrictionMode",
                
                    # the properties below are optional
                    repositories=["repositories"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b33f9d054f35f5ec68410c8313f2ffd1872a95e319e44f40a0c6992c3455211a)
                check_type(argname="argument restriction_mode", value=restriction_mode, expected_type=type_hints["restriction_mode"])
                check_type(argname="argument repositories", value=repositories, expected_type=type_hints["repositories"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "restriction_mode": restriction_mode,
            }
            if repositories is not None:
                self._values["repositories"] = repositories

        @builtins.property
        def restriction_mode(self) -> builtins.str:
            '''The package group origin restriction setting.

            When the value is ``INHERIT`` , the value is set to the value of the first parent package group which does not have a value of ``INHERIT`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeartifact-packagegroup-restrictiontype.html#cfn-codeartifact-packagegroup-restrictiontype-restrictionmode
            '''
            result = self._values.get("restriction_mode")
            assert result is not None, "Required property 'restriction_mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def repositories(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The repositories to add to the allowed repositories list.

            The allowed repositories list is used when the ``RestrictionMode`` is set to ``ALLOW_SPECIFIC_REPOSITORIES`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeartifact-packagegroup-restrictiontype.html#cfn-codeartifact-packagegroup-restrictiontype-repositories
            '''
            result = self._values.get("repositories")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RestrictionTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codeartifact.CfnPackageGroup.RestrictionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "external_upstream": "externalUpstream",
            "internal_upstream": "internalUpstream",
            "publish": "publish",
        },
    )
    class RestrictionsProperty:
        def __init__(
            self,
            *,
            external_upstream: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackageGroup.RestrictionTypeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            internal_upstream: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackageGroup.RestrictionTypeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            publish: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPackageGroup.RestrictionTypeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains information about the configured restrictions of the origin controls of a package group.

            :param external_upstream: The package group origin restriction setting for external, upstream repositories.
            :param internal_upstream: The package group origin restriction setting for internal, upstream repositories.
            :param publish: The package group origin restriction setting for publishing packages.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeartifact-packagegroup-restrictions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codeartifact as codeartifact
                
                restrictions_property = codeartifact.CfnPackageGroup.RestrictionsProperty(
                    external_upstream=codeartifact.CfnPackageGroup.RestrictionTypeProperty(
                        restriction_mode="restrictionMode",
                
                        # the properties below are optional
                        repositories=["repositories"]
                    ),
                    internal_upstream=codeartifact.CfnPackageGroup.RestrictionTypeProperty(
                        restriction_mode="restrictionMode",
                
                        # the properties below are optional
                        repositories=["repositories"]
                    ),
                    publish=codeartifact.CfnPackageGroup.RestrictionTypeProperty(
                        restriction_mode="restrictionMode",
                
                        # the properties below are optional
                        repositories=["repositories"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c52406159408ff95f368a7de422beb3ef5a838a22e051fd0602f67aab0b1299d)
                check_type(argname="argument external_upstream", value=external_upstream, expected_type=type_hints["external_upstream"])
                check_type(argname="argument internal_upstream", value=internal_upstream, expected_type=type_hints["internal_upstream"])
                check_type(argname="argument publish", value=publish, expected_type=type_hints["publish"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if external_upstream is not None:
                self._values["external_upstream"] = external_upstream
            if internal_upstream is not None:
                self._values["internal_upstream"] = internal_upstream
            if publish is not None:
                self._values["publish"] = publish

        @builtins.property
        def external_upstream(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackageGroup.RestrictionTypeProperty"]]:
            '''The package group origin restriction setting for external, upstream repositories.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeartifact-packagegroup-restrictions.html#cfn-codeartifact-packagegroup-restrictions-externalupstream
            '''
            result = self._values.get("external_upstream")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackageGroup.RestrictionTypeProperty"]], result)

        @builtins.property
        def internal_upstream(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackageGroup.RestrictionTypeProperty"]]:
            '''The package group origin restriction setting for internal, upstream repositories.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeartifact-packagegroup-restrictions.html#cfn-codeartifact-packagegroup-restrictions-internalupstream
            '''
            result = self._values.get("internal_upstream")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackageGroup.RestrictionTypeProperty"]], result)

        @builtins.property
        def publish(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackageGroup.RestrictionTypeProperty"]]:
            '''The package group origin restriction setting for publishing packages.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codeartifact-packagegroup-restrictions.html#cfn-codeartifact-packagegroup-restrictions-publish
            '''
            result = self._values.get("publish")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPackageGroup.RestrictionTypeProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RestrictionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codeartifact.CfnPackageGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "pattern": "pattern",
        "contact_info": "contactInfo",
        "description": "description",
        "domain_owner": "domainOwner",
        "origin_configuration": "originConfiguration",
        "tags": "tags",
    },
)
class CfnPackageGroupProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        pattern: builtins.str,
        contact_info: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        domain_owner: typing.Optional[builtins.str] = None,
        origin_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackageGroup.OriginConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPackageGroup``.

        :param domain_name: The domain that contains the package group.
        :param pattern: The pattern of the package group. The pattern determines which packages are associated with the package group.
        :param contact_info: The contact information of the package group.
        :param description: The description of the package group.
        :param domain_owner: The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.
        :param origin_configuration: Details about the package origin configuration of a package group.
        :param tags: A list of tags to be applied to the package group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-packagegroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codeartifact as codeartifact
            
            cfn_package_group_props = codeartifact.CfnPackageGroupProps(
                domain_name="domainName",
                pattern="pattern",
            
                # the properties below are optional
                contact_info="contactInfo",
                description="description",
                domain_owner="domainOwner",
                origin_configuration=codeartifact.CfnPackageGroup.OriginConfigurationProperty(
                    restrictions=codeartifact.CfnPackageGroup.RestrictionsProperty(
                        external_upstream=codeartifact.CfnPackageGroup.RestrictionTypeProperty(
                            restriction_mode="restrictionMode",
            
                            # the properties below are optional
                            repositories=["repositories"]
                        ),
                        internal_upstream=codeartifact.CfnPackageGroup.RestrictionTypeProperty(
                            restriction_mode="restrictionMode",
            
                            # the properties below are optional
                            repositories=["repositories"]
                        ),
                        publish=codeartifact.CfnPackageGroup.RestrictionTypeProperty(
                            restriction_mode="restrictionMode",
            
                            # the properties below are optional
                            repositories=["repositories"]
                        )
                    )
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25201ca742777c6bda1acf009c5a015a6a51866eef1a9bc32a2ebf1a5352ecf3)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
            check_type(argname="argument contact_info", value=contact_info, expected_type=type_hints["contact_info"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument domain_owner", value=domain_owner, expected_type=type_hints["domain_owner"])
            check_type(argname="argument origin_configuration", value=origin_configuration, expected_type=type_hints["origin_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
            "pattern": pattern,
        }
        if contact_info is not None:
            self._values["contact_info"] = contact_info
        if description is not None:
            self._values["description"] = description
        if domain_owner is not None:
            self._values["domain_owner"] = domain_owner
        if origin_configuration is not None:
            self._values["origin_configuration"] = origin_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The domain that contains the package group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-packagegroup.html#cfn-codeartifact-packagegroup-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pattern(self) -> builtins.str:
        '''The pattern of the package group.

        The pattern determines which packages are associated with the package group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-packagegroup.html#cfn-codeartifact-packagegroup-pattern
        '''
        result = self._values.get("pattern")
        assert result is not None, "Required property 'pattern' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def contact_info(self) -> typing.Optional[builtins.str]:
        '''The contact information of the package group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-packagegroup.html#cfn-codeartifact-packagegroup-contactinfo
        '''
        result = self._values.get("contact_info")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the package group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-packagegroup.html#cfn-codeartifact-packagegroup-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_owner(self) -> typing.Optional[builtins.str]:
        '''The 12-digit account number of the AWS account that owns the domain.

        It does not include dashes or spaces.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-packagegroup.html#cfn-codeartifact-packagegroup-domainowner
        '''
        result = self._values.get("domain_owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPackageGroup.OriginConfigurationProperty]]:
        '''Details about the package origin configuration of a package group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-packagegroup.html#cfn-codeartifact-packagegroup-originconfiguration
        '''
        result = self._values.get("origin_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPackageGroup.OriginConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags to be applied to the package group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-packagegroup.html#cfn-codeartifact-packagegroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPackageGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnRepository(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codeartifact.CfnRepository",
):
    '''The ``AWS::CodeArtifact::Repository`` resource creates an AWS CodeArtifact repository.

    CodeArtifact *repositories* contain a set of package versions. For more information about repositories, see the `Repository concepts information <https://docs.aws.amazon.com/codeartifact/latest/ug/codeartifact-concepts.html#welcome-concepts-repository>`_ in the *CodeArtifact User Guide* . For more information about the ``CreateRepository`` API, see `CreateRepository <https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_CreateRepository.html>`_ in the *CodeArtifact API Reference* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-repository.html
    :cloudformationResource: AWS::CodeArtifact::Repository
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_codeartifact as codeartifact
        
        # permissions_policy_document: Any
        
        cfn_repository = codeartifact.CfnRepository(self, "MyCfnRepository",
            domain_name="domainName",
            repository_name="repositoryName",
        
            # the properties below are optional
            description="description",
            domain_owner="domainOwner",
            external_connections=["externalConnections"],
            permissions_policy_document=permissions_policy_document,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            upstreams=["upstreams"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_name: builtins.str,
        repository_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        domain_owner: typing.Optional[builtins.str] = None,
        external_connections: typing.Optional[typing.Sequence[builtins.str]] = None,
        permissions_policy_document: typing.Any = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        upstreams: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_name: The name of the domain that contains the repository.
        :param repository_name: The name of an upstream repository.
        :param description: A text description of the repository.
        :param domain_owner: The 12-digit account ID of the AWS account that owns the domain.
        :param external_connections: An array of external connections associated with the repository. For more information, see `Supported external connection repositories <https://docs.aws.amazon.com/codeartifact/latest/ug/external-connection.html#supported-public-repositories>`_ in the *CodeArtifact user guide* .
        :param permissions_policy_document: The document that defines the resource policy that is set on a repository.
        :param tags: A list of tags to be applied to the repository.
        :param upstreams: A list of upstream repositories to associate with the repository. The order of the upstream repositories in the list determines their priority order when AWS CodeArtifact looks for a requested package version. For more information, see `Working with upstream repositories <https://docs.aws.amazon.com/codeartifact/latest/ug/repos-upstream.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4fb8e90c9d866f1bfe7bd9bf2e46e1f97b3f66247b8086423fecb6029b669e4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRepositoryProps(
            domain_name=domain_name,
            repository_name=repository_name,
            description=description,
            domain_owner=domain_owner,
            external_connections=external_connections,
            permissions_policy_document=permissions_policy_document,
            tags=tags,
            upstreams=upstreams,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14419efb740b55005573cc7f534a273bf2f02fe55f2b8b0a1a7c3e547e53cf17)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dea27ea8112a8554ed16a2ab68f5975c90735183eed4a308f91074201e1d3a11)
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
        '''When you pass the logical ID of this resource, the function returns the Amazon Resource Name (ARN) of the repository.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainName")
    def attr_domain_name(self) -> builtins.str:
        '''When you pass the logical ID of this resource, the function returns the domain name that contains the repository.

        :cloudformationAttribute: DomainName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainName"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainOwner")
    def attr_domain_owner(self) -> builtins.str:
        '''When you pass the logical ID of this resource, the function returns the 12-digit account number of the AWS account that owns the domain that contains the repository.

        :cloudformationAttribute: DomainOwner
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainOwner"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''When you pass the logical ID of this resource, the function returns the name of the repository.

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
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''The name of the domain that contains the repository.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00ba74acfa0c33c4fae675e1b25d2be0f71988064b24926c12199963df7fc78e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="repositoryName")
    def repository_name(self) -> builtins.str:
        '''The name of an upstream repository.'''
        return typing.cast(builtins.str, jsii.get(self, "repositoryName"))

    @repository_name.setter
    def repository_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a83fb63b6e2c7629433d470d902d70a3909aadfa55f55d4269da462d63250ad9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryName", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A text description of the repository.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7c0e7def7c7bbb9ff13c896e62e115981ffb1f862a86a71803aae85f136b05f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="domainOwner")
    def domain_owner(self) -> typing.Optional[builtins.str]:
        '''The 12-digit account ID of the AWS account that owns the domain.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainOwner"))

    @domain_owner.setter
    def domain_owner(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d28afb901607f9ab6b3fe057b5807de7e3feeb54a77c448871ba10210b88ca6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainOwner", value)

    @builtins.property
    @jsii.member(jsii_name="externalConnections")
    def external_connections(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of external connections associated with the repository.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "externalConnections"))

    @external_connections.setter
    def external_connections(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b57d3ca6e53363d4e96e0ea3b4abadc4b325c54502d845d394fe93954e1440d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "externalConnections", value)

    @builtins.property
    @jsii.member(jsii_name="permissionsPolicyDocument")
    def permissions_policy_document(self) -> typing.Any:
        '''The document that defines the resource policy that is set on a repository.'''
        return typing.cast(typing.Any, jsii.get(self, "permissionsPolicyDocument"))

    @permissions_policy_document.setter
    def permissions_policy_document(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a46a16b2d085bb751bab7c709cfc8d98bdb0183c734e7aae69ecfaa0c762cfab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionsPolicyDocument", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags to be applied to the repository.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de95686b67ad4abe694cdd668a988205994b9ad92dcd587a4ebff7a0ceac3e74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="upstreams")
    def upstreams(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of upstream repositories to associate with the repository.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "upstreams"))

    @upstreams.setter
    def upstreams(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea3cff06cb396a8c85d4d848e533286b31b4698444335eba208a18cfa179936b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "upstreams", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codeartifact.CfnRepositoryProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "repository_name": "repositoryName",
        "description": "description",
        "domain_owner": "domainOwner",
        "external_connections": "externalConnections",
        "permissions_policy_document": "permissionsPolicyDocument",
        "tags": "tags",
        "upstreams": "upstreams",
    },
)
class CfnRepositoryProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        repository_name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        domain_owner: typing.Optional[builtins.str] = None,
        external_connections: typing.Optional[typing.Sequence[builtins.str]] = None,
        permissions_policy_document: typing.Any = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        upstreams: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRepository``.

        :param domain_name: The name of the domain that contains the repository.
        :param repository_name: The name of an upstream repository.
        :param description: A text description of the repository.
        :param domain_owner: The 12-digit account ID of the AWS account that owns the domain.
        :param external_connections: An array of external connections associated with the repository. For more information, see `Supported external connection repositories <https://docs.aws.amazon.com/codeartifact/latest/ug/external-connection.html#supported-public-repositories>`_ in the *CodeArtifact user guide* .
        :param permissions_policy_document: The document that defines the resource policy that is set on a repository.
        :param tags: A list of tags to be applied to the repository.
        :param upstreams: A list of upstream repositories to associate with the repository. The order of the upstream repositories in the list determines their priority order when AWS CodeArtifact looks for a requested package version. For more information, see `Working with upstream repositories <https://docs.aws.amazon.com/codeartifact/latest/ug/repos-upstream.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-repository.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codeartifact as codeartifact
            
            # permissions_policy_document: Any
            
            cfn_repository_props = codeartifact.CfnRepositoryProps(
                domain_name="domainName",
                repository_name="repositoryName",
            
                # the properties below are optional
                description="description",
                domain_owner="domainOwner",
                external_connections=["externalConnections"],
                permissions_policy_document=permissions_policy_document,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                upstreams=["upstreams"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f500688c503a5f634dfec2094e49169b45632084082b87918656c86e67748c46)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument domain_owner", value=domain_owner, expected_type=type_hints["domain_owner"])
            check_type(argname="argument external_connections", value=external_connections, expected_type=type_hints["external_connections"])
            check_type(argname="argument permissions_policy_document", value=permissions_policy_document, expected_type=type_hints["permissions_policy_document"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument upstreams", value=upstreams, expected_type=type_hints["upstreams"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
            "repository_name": repository_name,
        }
        if description is not None:
            self._values["description"] = description
        if domain_owner is not None:
            self._values["domain_owner"] = domain_owner
        if external_connections is not None:
            self._values["external_connections"] = external_connections
        if permissions_policy_document is not None:
            self._values["permissions_policy_document"] = permissions_policy_document
        if tags is not None:
            self._values["tags"] = tags
        if upstreams is not None:
            self._values["upstreams"] = upstreams

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The name of the domain that contains the repository.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-repository.html#cfn-codeartifact-repository-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository_name(self) -> builtins.str:
        '''The name of an upstream repository.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-repository.html#cfn-codeartifact-repository-repositoryname
        '''
        result = self._values.get("repository_name")
        assert result is not None, "Required property 'repository_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A text description of the repository.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-repository.html#cfn-codeartifact-repository-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_owner(self) -> typing.Optional[builtins.str]:
        '''The 12-digit account ID of the AWS account that owns the domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-repository.html#cfn-codeartifact-repository-domainowner
        '''
        result = self._values.get("domain_owner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def external_connections(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of external connections associated with the repository.

        For more information, see `Supported external connection repositories <https://docs.aws.amazon.com/codeartifact/latest/ug/external-connection.html#supported-public-repositories>`_ in the *CodeArtifact user guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-repository.html#cfn-codeartifact-repository-externalconnections
        '''
        result = self._values.get("external_connections")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def permissions_policy_document(self) -> typing.Any:
        '''The document that defines the resource policy that is set on a repository.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-repository.html#cfn-codeartifact-repository-permissionspolicydocument
        '''
        result = self._values.get("permissions_policy_document")
        return typing.cast(typing.Any, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags to be applied to the repository.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-repository.html#cfn-codeartifact-repository-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def upstreams(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of upstream repositories to associate with the repository.

        The order of the upstream repositories in the list determines their priority order when AWS CodeArtifact looks for a requested package version. For more information, see `Working with upstream repositories <https://docs.aws.amazon.com/codeartifact/latest/ug/repos-upstream.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codeartifact-repository.html#cfn-codeartifact-repository-upstreams
        '''
        result = self._values.get("upstreams")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRepositoryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDomain",
    "CfnDomainProps",
    "CfnPackageGroup",
    "CfnPackageGroupProps",
    "CfnRepository",
    "CfnRepositoryProps",
]

publication.publish()

def _typecheckingstub__1fb789fedc85855c1509949f2cf10c2dd0562b804efa5820bf00577753b9d8b7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_name: builtins.str,
    encryption_key: typing.Optional[builtins.str] = None,
    permissions_policy_document: typing.Any = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46d9fe40fc43e31cea0a6a2e9dfd751eb16b8a46da32d7dccd9603f803712f90(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2a99c05ff9a326ace2300aa6eea08d05c5801006bd439dac683557fc824f972(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__020dc2753ebcfeb3fc3126169a639eb6863967fddf54f8990d248b3c17684e90(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a60707c2e5754637c6feec657151278ead04566ec407a5201952b87113e7daa8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__912eada525b5990b51696702eabe0044019487d7cefa00a70be77c94c889c313(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3d141e3a88261a459532756257673073502431714e2b0bae8c140a9b055f07b(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed4a67a72fcc7050f3a4ea650fb97fc3375ca5e90727251a483297144826487d(
    *,
    domain_name: builtins.str,
    encryption_key: typing.Optional[builtins.str] = None,
    permissions_policy_document: typing.Any = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a8aaa0852b2af2f8381bac18421469d96d102aa57d00f002433c862966b5603(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_name: builtins.str,
    pattern: builtins.str,
    contact_info: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    domain_owner: typing.Optional[builtins.str] = None,
    origin_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackageGroup.OriginConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ce81570371704a4089ff9d234920c939ca57e8078fae0ed77580614455f254b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73902d03882d362546bad830a7e307a86e67195728c52e0a2837b7a05804b314(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa73b50d995f7005fa2ec82631d018ef1849c9ffebef0125fbb6a4ee774b2163(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2718281da222f54ccce3c7a3bf6ded0f2b7a3bdcd9d30fbeea35abc3e153fd1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26fdce972c6efcbdd12712f2d1406046a1aaf63a8d0f3da99813e261e4029f97(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b9671c9b67b0351b5842cb8cda895b5db7d8202b0617a306719b29c79b2309d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15d889231b62e097fa73baf944ef89bab375256fa4ae0bdb93c27049076c51c7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63bcaafc797c7b557351ce8e1bfa571001310be1e41896261bec63105e81cae6(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPackageGroup.OriginConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e756db6ce537f9d80da313912b16eef0c2a610ee05772d30b4df98a4ddebee96(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46aa889310dd45252527135dfe1c0e1137811a871c8d0978ef0c8c7dcf8636fa(
    *,
    restrictions: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackageGroup.RestrictionsProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b33f9d054f35f5ec68410c8313f2ffd1872a95e319e44f40a0c6992c3455211a(
    *,
    restriction_mode: builtins.str,
    repositories: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c52406159408ff95f368a7de422beb3ef5a838a22e051fd0602f67aab0b1299d(
    *,
    external_upstream: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackageGroup.RestrictionTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    internal_upstream: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackageGroup.RestrictionTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    publish: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackageGroup.RestrictionTypeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25201ca742777c6bda1acf009c5a015a6a51866eef1a9bc32a2ebf1a5352ecf3(
    *,
    domain_name: builtins.str,
    pattern: builtins.str,
    contact_info: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    domain_owner: typing.Optional[builtins.str] = None,
    origin_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPackageGroup.OriginConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4fb8e90c9d866f1bfe7bd9bf2e46e1f97b3f66247b8086423fecb6029b669e4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_name: builtins.str,
    repository_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    domain_owner: typing.Optional[builtins.str] = None,
    external_connections: typing.Optional[typing.Sequence[builtins.str]] = None,
    permissions_policy_document: typing.Any = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    upstreams: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14419efb740b55005573cc7f534a273bf2f02fe55f2b8b0a1a7c3e547e53cf17(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dea27ea8112a8554ed16a2ab68f5975c90735183eed4a308f91074201e1d3a11(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00ba74acfa0c33c4fae675e1b25d2be0f71988064b24926c12199963df7fc78e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a83fb63b6e2c7629433d470d902d70a3909aadfa55f55d4269da462d63250ad9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7c0e7def7c7bbb9ff13c896e62e115981ffb1f862a86a71803aae85f136b05f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d28afb901607f9ab6b3fe057b5807de7e3feeb54a77c448871ba10210b88ca6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b57d3ca6e53363d4e96e0ea3b4abadc4b325c54502d845d394fe93954e1440d9(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a46a16b2d085bb751bab7c709cfc8d98bdb0183c734e7aae69ecfaa0c762cfab(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de95686b67ad4abe694cdd668a988205994b9ad92dcd587a4ebff7a0ceac3e74(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea3cff06cb396a8c85d4d848e533286b31b4698444335eba208a18cfa179936b(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f500688c503a5f634dfec2094e49169b45632084082b87918656c86e67748c46(
    *,
    domain_name: builtins.str,
    repository_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    domain_owner: typing.Optional[builtins.str] = None,
    external_connections: typing.Optional[typing.Sequence[builtins.str]] = None,
    permissions_policy_document: typing.Any = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    upstreams: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
