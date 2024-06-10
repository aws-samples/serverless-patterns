'''
# AWS::PCAConnectorAD Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_pcaconnectorad as pcaconnectorad
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for PCAConnectorAD construct libraries](https://constructs.dev/search?q=pcaconnectorad)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::PCAConnectorAD resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_PCAConnectorAD.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::PCAConnectorAD](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_PCAConnectorAD.html).

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
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnConnector(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnConnector",
):
    '''Creates a connector between AWS Private CA and an Active Directory.

    You must specify the private CA, directory ID, and security groups.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-connector.html
    :cloudformationResource: AWS::PCAConnectorAD::Connector
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pcaconnectorad as pcaconnectorad
        
        cfn_connector = pcaconnectorad.CfnConnector(self, "MyCfnConnector",
            certificate_authority_arn="certificateAuthorityArn",
            directory_id="directoryId",
            vpc_information=pcaconnectorad.CfnConnector.VpcInformationProperty(
                security_group_ids=["securityGroupIds"]
            ),
        
            # the properties below are optional
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
        certificate_authority_arn: builtins.str,
        directory_id: builtins.str,
        vpc_information: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnector.VpcInformationProperty", typing.Dict[builtins.str, typing.Any]]],
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param certificate_authority_arn: The Amazon Resource Name (ARN) of the certificate authority being used.
        :param directory_id: The identifier of the Active Directory.
        :param vpc_information: Information of the VPC and security group(s) used with the connector.
        :param tags: Metadata assigned to a connector consisting of a key-value pair.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a12163a6729548e5010cdebd16984d9bc442d61e9fbbf189c986731db6b48d47)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConnectorProps(
            certificate_authority_arn=certificate_authority_arn,
            directory_id=directory_id,
            vpc_information=vpc_information,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__995fc1e26ccbb1d65aff429128879ca6773f054cc4f117a8e1447be68e0afc96)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e3d96af69193b4c63c1a08fc841f1f53484be496914e380a12d6599834d01ef1)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrConnectorArn")
    def attr_connector_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) that was returned when you called `CreateConnector <https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html>`_ .

        :cloudformationAttribute: ConnectorArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConnectorArn"))

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
    @jsii.member(jsii_name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the certificate authority being used.'''
        return typing.cast(builtins.str, jsii.get(self, "certificateAuthorityArn"))

    @certificate_authority_arn.setter
    def certificate_authority_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85ffecf84ef5c66b68d71a320cbd94d944f32371d0084613413b520fe56b8c1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateAuthorityArn", value)

    @builtins.property
    @jsii.member(jsii_name="directoryId")
    def directory_id(self) -> builtins.str:
        '''The identifier of the Active Directory.'''
        return typing.cast(builtins.str, jsii.get(self, "directoryId"))

    @directory_id.setter
    def directory_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__627eac80a9f24ed66c799c77c564a456223f8974b2958400dcf9e2b1083ad097)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryId", value)

    @builtins.property
    @jsii.member(jsii_name="vpcInformation")
    def vpc_information(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnConnector.VpcInformationProperty"]:
        '''Information of the VPC and security group(s) used with the connector.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConnector.VpcInformationProperty"], jsii.get(self, "vpcInformation"))

    @vpc_information.setter
    def vpc_information(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnConnector.VpcInformationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7958644c6b6b742a56d7010b862aba24109f3f57815fa7477ed5ff078f149a85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcInformation", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Metadata assigned to a connector consisting of a key-value pair.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6278c4b97c0032befb9608a0699c8b6bccf6e756f23518e9cd72e3454c4b62b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnConnector.VpcInformationProperty",
        jsii_struct_bases=[],
        name_mapping={"security_group_ids": "securityGroupIds"},
    )
    class VpcInformationProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
        ) -> None:
            '''Information about your VPC and security groups used with the connector.

            :param security_group_ids: The security groups used with the connector. You can use a maximum of 4 security groups with a connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-connector-vpcinformation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                vpc_information_property = pcaconnectorad.CfnConnector.VpcInformationProperty(
                    security_group_ids=["securityGroupIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8b9f29305eaa60cc155622de83a9fdb695e29e88cecf7960456609a9a375b153)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "security_group_ids": security_group_ids,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''The security groups used with the connector.

            You can use a maximum of 4 security groups with a connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-connector-vpcinformation.html#cfn-pcaconnectorad-connector-vpcinformation-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcInformationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnConnectorProps",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_authority_arn": "certificateAuthorityArn",
        "directory_id": "directoryId",
        "vpc_information": "vpcInformation",
        "tags": "tags",
    },
)
class CfnConnectorProps:
    def __init__(
        self,
        *,
        certificate_authority_arn: builtins.str,
        directory_id: builtins.str,
        vpc_information: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.VpcInformationProperty, typing.Dict[builtins.str, typing.Any]]],
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConnector``.

        :param certificate_authority_arn: The Amazon Resource Name (ARN) of the certificate authority being used.
        :param directory_id: The identifier of the Active Directory.
        :param vpc_information: Information of the VPC and security group(s) used with the connector.
        :param tags: Metadata assigned to a connector consisting of a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-connector.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pcaconnectorad as pcaconnectorad
            
            cfn_connector_props = pcaconnectorad.CfnConnectorProps(
                certificate_authority_arn="certificateAuthorityArn",
                directory_id="directoryId",
                vpc_information=pcaconnectorad.CfnConnector.VpcInformationProperty(
                    security_group_ids=["securityGroupIds"]
                ),
            
                # the properties below are optional
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__564156a907862773b47fafbb1b06e4f9c8e0d3d39ffe5d8235c3d7cc34c92a40)
            check_type(argname="argument certificate_authority_arn", value=certificate_authority_arn, expected_type=type_hints["certificate_authority_arn"])
            check_type(argname="argument directory_id", value=directory_id, expected_type=type_hints["directory_id"])
            check_type(argname="argument vpc_information", value=vpc_information, expected_type=type_hints["vpc_information"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_authority_arn": certificate_authority_arn,
            "directory_id": directory_id,
            "vpc_information": vpc_information,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def certificate_authority_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the certificate authority being used.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-connector.html#cfn-pcaconnectorad-connector-certificateauthorityarn
        '''
        result = self._values.get("certificate_authority_arn")
        assert result is not None, "Required property 'certificate_authority_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def directory_id(self) -> builtins.str:
        '''The identifier of the Active Directory.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-connector.html#cfn-pcaconnectorad-connector-directoryid
        '''
        result = self._values.get("directory_id")
        assert result is not None, "Required property 'directory_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_information(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnConnector.VpcInformationProperty]:
        '''Information of the VPC and security group(s) used with the connector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-connector.html#cfn-pcaconnectorad-connector-vpcinformation
        '''
        result = self._values.get("vpc_information")
        assert result is not None, "Required property 'vpc_information' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnConnector.VpcInformationProperty], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Metadata assigned to a connector consisting of a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-connector.html#cfn-pcaconnectorad-connector-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConnectorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnDirectoryRegistration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnDirectoryRegistration",
):
    '''Creates a directory registration that authorizes communication between AWS Private CA and an Active Directory.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-directoryregistration.html
    :cloudformationResource: AWS::PCAConnectorAD::DirectoryRegistration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pcaconnectorad as pcaconnectorad
        
        cfn_directory_registration = pcaconnectorad.CfnDirectoryRegistration(self, "MyCfnDirectoryRegistration",
            directory_id="directoryId",
        
            # the properties below are optional
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
        directory_id: builtins.str,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param directory_id: The identifier of the Active Directory.
        :param tags: Metadata assigned to a directory registration consisting of a key-value pair.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e325d6e149baf8a596306043eb453d2d3f8e118e00d5278dd37d6c33cb8c633)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDirectoryRegistrationProps(directory_id=directory_id, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41b23bf9daa66db7deae4b509cd527669ef15b39a237b53b777a6334ec274485)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f42e0e871a5326bb18faea9ea2f2e7da908aa2959bd095e6e5686bf7e37c2cee)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDirectoryRegistrationArn")
    def attr_directory_registration_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) that was returned when you called `CreateDirectoryRegistration <https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html>`_ .

        :cloudformationAttribute: DirectoryRegistrationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDirectoryRegistrationArn"))

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
    @jsii.member(jsii_name="directoryId")
    def directory_id(self) -> builtins.str:
        '''The identifier of the Active Directory.'''
        return typing.cast(builtins.str, jsii.get(self, "directoryId"))

    @directory_id.setter
    def directory_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe9074c785c14f7e464667b3097652bb1428d371156c62c379bd9e9076c450d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Metadata assigned to a directory registration consisting of a key-value pair.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__177ed6093a034522fdd983b6789c9a099c557cbf446b6555c4af62b49b258c7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnDirectoryRegistrationProps",
    jsii_struct_bases=[],
    name_mapping={"directory_id": "directoryId", "tags": "tags"},
)
class CfnDirectoryRegistrationProps:
    def __init__(
        self,
        *,
        directory_id: builtins.str,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDirectoryRegistration``.

        :param directory_id: The identifier of the Active Directory.
        :param tags: Metadata assigned to a directory registration consisting of a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-directoryregistration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pcaconnectorad as pcaconnectorad
            
            cfn_directory_registration_props = pcaconnectorad.CfnDirectoryRegistrationProps(
                directory_id="directoryId",
            
                # the properties below are optional
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92354fae5f6aaf222ff6a71438d62db5492fa605cf6c14cfaf2176b801600eb4)
            check_type(argname="argument directory_id", value=directory_id, expected_type=type_hints["directory_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "directory_id": directory_id,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def directory_id(self) -> builtins.str:
        '''The identifier of the Active Directory.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-directoryregistration.html#cfn-pcaconnectorad-directoryregistration-directoryid
        '''
        result = self._values.get("directory_id")
        assert result is not None, "Required property 'directory_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Metadata assigned to a directory registration consisting of a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-directoryregistration.html#cfn-pcaconnectorad-directoryregistration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDirectoryRegistrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnServicePrincipalName(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnServicePrincipalName",
):
    '''Creates a service principal name (SPN) for the service account in Active Directory.

    Kerberos authentication uses SPNs to associate a service instance with a service sign-in account.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-serviceprincipalname.html
    :cloudformationResource: AWS::PCAConnectorAD::ServicePrincipalName
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pcaconnectorad as pcaconnectorad
        
        cfn_service_principal_name = pcaconnectorad.CfnServicePrincipalName(self, "MyCfnServicePrincipalName",
            connector_arn="connectorArn",
            directory_registration_arn="directoryRegistrationArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        connector_arn: typing.Optional[builtins.str] = None,
        directory_registration_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param connector_arn: The Amazon Resource Name (ARN) that was returned when you called `CreateConnector.html <https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html>`_ .
        :param directory_registration_arn: The Amazon Resource Name (ARN) that was returned when you called `CreateDirectoryRegistration <https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__779230ef86d4538873fd875cd3babc1ab92f57abdae26cfcea7069e7eb8272d1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServicePrincipalNameProps(
            connector_arn=connector_arn,
            directory_registration_arn=directory_registration_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2282e80f861510398f89d8cf1beed04a57d98bd9fef207e0a43718dd569cca4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7e3d66893530b0ec8229273f184fa5f3458cc9661569945849b363b3554b4295)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="connectorArn")
    def connector_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) that was returned when you called `CreateConnector.html <https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html>`_ .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectorArn"))

    @connector_arn.setter
    def connector_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7336215d5258c7d33cf1355d3c1630bd720ee5b24987f7ee7448a6794e671e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorArn", value)

    @builtins.property
    @jsii.member(jsii_name="directoryRegistrationArn")
    def directory_registration_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) that was returned when you called `CreateDirectoryRegistration <https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html>`_ .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryRegistrationArn"))

    @directory_registration_arn.setter
    def directory_registration_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3b11dc247af37c1b9943c4e484a0d90a5a5c3460e646bf1e2f3ce167a88c6a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryRegistrationArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnServicePrincipalNameProps",
    jsii_struct_bases=[],
    name_mapping={
        "connector_arn": "connectorArn",
        "directory_registration_arn": "directoryRegistrationArn",
    },
)
class CfnServicePrincipalNameProps:
    def __init__(
        self,
        *,
        connector_arn: typing.Optional[builtins.str] = None,
        directory_registration_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnServicePrincipalName``.

        :param connector_arn: The Amazon Resource Name (ARN) that was returned when you called `CreateConnector.html <https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html>`_ .
        :param directory_registration_arn: The Amazon Resource Name (ARN) that was returned when you called `CreateDirectoryRegistration <https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-serviceprincipalname.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pcaconnectorad as pcaconnectorad
            
            cfn_service_principal_name_props = pcaconnectorad.CfnServicePrincipalNameProps(
                connector_arn="connectorArn",
                directory_registration_arn="directoryRegistrationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7da1bc3702a4df8757dbc31f6575b8167128062a021b3ccf901b92314a2c56d8)
            check_type(argname="argument connector_arn", value=connector_arn, expected_type=type_hints["connector_arn"])
            check_type(argname="argument directory_registration_arn", value=directory_registration_arn, expected_type=type_hints["directory_registration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connector_arn is not None:
            self._values["connector_arn"] = connector_arn
        if directory_registration_arn is not None:
            self._values["directory_registration_arn"] = directory_registration_arn

    @builtins.property
    def connector_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) that was returned when you called `CreateConnector.html <https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-serviceprincipalname.html#cfn-pcaconnectorad-serviceprincipalname-connectorarn
        '''
        result = self._values.get("connector_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def directory_registration_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) that was returned when you called `CreateDirectoryRegistration <https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-serviceprincipalname.html#cfn-pcaconnectorad-serviceprincipalname-directoryregistrationarn
        '''
        result = self._values.get("directory_registration_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServicePrincipalNameProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnTemplate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate",
):
    '''Creates an Active Directory compatible certificate template.

    The connectors issues certificates using these templates based on the requester’s Active Directory group membership.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-template.html
    :cloudformationResource: AWS::PCAConnectorAD::Template
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pcaconnectorad as pcaconnectorad
        
        cfn_template = pcaconnectorad.CfnTemplate(self, "MyCfnTemplate",
            connector_arn="connectorArn",
            definition=pcaconnectorad.CfnTemplate.TemplateDefinitionProperty(
                template_v2=pcaconnectorad.CfnTemplate.TemplateV2Property(
                    certificate_validity=pcaconnectorad.CfnTemplate.CertificateValidityProperty(
                        renewal_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                            period=123,
                            period_type="periodType"
                        ),
                        validity_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                            period=123,
                            period_type="periodType"
                        )
                    ),
                    enrollment_flags=pcaconnectorad.CfnTemplate.EnrollmentFlagsV2Property(
                        enable_key_reuse_on_nt_token_keyset_storage_full=False,
                        include_symmetric_algorithms=False,
                        no_security_extension=False,
                        remove_invalid_certificate_from_personal_store=False,
                        user_interaction_required=False
                    ),
                    extensions=pcaconnectorad.CfnTemplate.ExtensionsV2Property(
                        key_usage=pcaconnectorad.CfnTemplate.KeyUsageProperty(
                            usage_flags=pcaconnectorad.CfnTemplate.KeyUsageFlagsProperty(
                                data_encipherment=False,
                                digital_signature=False,
                                key_agreement=False,
                                key_encipherment=False,
                                non_repudiation=False
                            ),
        
                            # the properties below are optional
                            critical=False
                        ),
        
                        # the properties below are optional
                        application_policies=pcaconnectorad.CfnTemplate.ApplicationPoliciesProperty(
                            policies=[pcaconnectorad.CfnTemplate.ApplicationPolicyProperty(
                                policy_object_identifier="policyObjectIdentifier",
                                policy_type="policyType"
                            )],
        
                            # the properties below are optional
                            critical=False
                        )
                    ),
                    general_flags=pcaconnectorad.CfnTemplate.GeneralFlagsV2Property(
                        auto_enrollment=False,
                        machine_type=False
                    ),
                    private_key_attributes=pcaconnectorad.CfnTemplate.PrivateKeyAttributesV2Property(
                        key_spec="keySpec",
                        minimal_key_length=123,
        
                        # the properties below are optional
                        crypto_providers=["cryptoProviders"]
                    ),
                    private_key_flags=pcaconnectorad.CfnTemplate.PrivateKeyFlagsV2Property(
                        client_version="clientVersion",
        
                        # the properties below are optional
                        exportable_key=False,
                        strong_key_protection_required=False
                    ),
                    subject_name_flags=pcaconnectorad.CfnTemplate.SubjectNameFlagsV2Property(
                        require_common_name=False,
                        require_directory_path=False,
                        require_dns_as_cn=False,
                        require_email=False,
                        san_require_directory_guid=False,
                        san_require_dns=False,
                        san_require_domain_dns=False,
                        san_require_email=False,
                        san_require_spn=False,
                        san_require_upn=False
                    ),
        
                    # the properties below are optional
                    superseded_templates=["supersededTemplates"]
                ),
                template_v3=pcaconnectorad.CfnTemplate.TemplateV3Property(
                    certificate_validity=pcaconnectorad.CfnTemplate.CertificateValidityProperty(
                        renewal_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                            period=123,
                            period_type="periodType"
                        ),
                        validity_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                            period=123,
                            period_type="periodType"
                        )
                    ),
                    enrollment_flags=pcaconnectorad.CfnTemplate.EnrollmentFlagsV3Property(
                        enable_key_reuse_on_nt_token_keyset_storage_full=False,
                        include_symmetric_algorithms=False,
                        no_security_extension=False,
                        remove_invalid_certificate_from_personal_store=False,
                        user_interaction_required=False
                    ),
                    extensions=pcaconnectorad.CfnTemplate.ExtensionsV3Property(
                        key_usage=pcaconnectorad.CfnTemplate.KeyUsageProperty(
                            usage_flags=pcaconnectorad.CfnTemplate.KeyUsageFlagsProperty(
                                data_encipherment=False,
                                digital_signature=False,
                                key_agreement=False,
                                key_encipherment=False,
                                non_repudiation=False
                            ),
        
                            # the properties below are optional
                            critical=False
                        ),
        
                        # the properties below are optional
                        application_policies=pcaconnectorad.CfnTemplate.ApplicationPoliciesProperty(
                            policies=[pcaconnectorad.CfnTemplate.ApplicationPolicyProperty(
                                policy_object_identifier="policyObjectIdentifier",
                                policy_type="policyType"
                            )],
        
                            # the properties below are optional
                            critical=False
                        )
                    ),
                    general_flags=pcaconnectorad.CfnTemplate.GeneralFlagsV3Property(
                        auto_enrollment=False,
                        machine_type=False
                    ),
                    hash_algorithm="hashAlgorithm",
                    private_key_attributes=pcaconnectorad.CfnTemplate.PrivateKeyAttributesV3Property(
                        algorithm="algorithm",
                        key_spec="keySpec",
                        key_usage_property=pcaconnectorad.CfnTemplate.KeyUsagePropertyProperty(
                            property_flags=pcaconnectorad.CfnTemplate.KeyUsagePropertyFlagsProperty(
                                decrypt=False,
                                key_agreement=False,
                                sign=False
                            ),
                            property_type="propertyType"
                        ),
                        minimal_key_length=123,
        
                        # the properties below are optional
                        crypto_providers=["cryptoProviders"]
                    ),
                    private_key_flags=pcaconnectorad.CfnTemplate.PrivateKeyFlagsV3Property(
                        client_version="clientVersion",
        
                        # the properties below are optional
                        exportable_key=False,
                        require_alternate_signature_algorithm=False,
                        strong_key_protection_required=False
                    ),
                    subject_name_flags=pcaconnectorad.CfnTemplate.SubjectNameFlagsV3Property(
                        require_common_name=False,
                        require_directory_path=False,
                        require_dns_as_cn=False,
                        require_email=False,
                        san_require_directory_guid=False,
                        san_require_dns=False,
                        san_require_domain_dns=False,
                        san_require_email=False,
                        san_require_spn=False,
                        san_require_upn=False
                    ),
        
                    # the properties below are optional
                    superseded_templates=["supersededTemplates"]
                ),
                template_v4=pcaconnectorad.CfnTemplate.TemplateV4Property(
                    certificate_validity=pcaconnectorad.CfnTemplate.CertificateValidityProperty(
                        renewal_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                            period=123,
                            period_type="periodType"
                        ),
                        validity_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                            period=123,
                            period_type="periodType"
                        )
                    ),
                    enrollment_flags=pcaconnectorad.CfnTemplate.EnrollmentFlagsV4Property(
                        enable_key_reuse_on_nt_token_keyset_storage_full=False,
                        include_symmetric_algorithms=False,
                        no_security_extension=False,
                        remove_invalid_certificate_from_personal_store=False,
                        user_interaction_required=False
                    ),
                    extensions=pcaconnectorad.CfnTemplate.ExtensionsV4Property(
                        key_usage=pcaconnectorad.CfnTemplate.KeyUsageProperty(
                            usage_flags=pcaconnectorad.CfnTemplate.KeyUsageFlagsProperty(
                                data_encipherment=False,
                                digital_signature=False,
                                key_agreement=False,
                                key_encipherment=False,
                                non_repudiation=False
                            ),
        
                            # the properties below are optional
                            critical=False
                        ),
        
                        # the properties below are optional
                        application_policies=pcaconnectorad.CfnTemplate.ApplicationPoliciesProperty(
                            policies=[pcaconnectorad.CfnTemplate.ApplicationPolicyProperty(
                                policy_object_identifier="policyObjectIdentifier",
                                policy_type="policyType"
                            )],
        
                            # the properties below are optional
                            critical=False
                        )
                    ),
                    general_flags=pcaconnectorad.CfnTemplate.GeneralFlagsV4Property(
                        auto_enrollment=False,
                        machine_type=False
                    ),
                    private_key_attributes=pcaconnectorad.CfnTemplate.PrivateKeyAttributesV4Property(
                        key_spec="keySpec",
                        minimal_key_length=123,
        
                        # the properties below are optional
                        algorithm="algorithm",
                        crypto_providers=["cryptoProviders"],
                        key_usage_property=pcaconnectorad.CfnTemplate.KeyUsagePropertyProperty(
                            property_flags=pcaconnectorad.CfnTemplate.KeyUsagePropertyFlagsProperty(
                                decrypt=False,
                                key_agreement=False,
                                sign=False
                            ),
                            property_type="propertyType"
                        )
                    ),
                    private_key_flags=pcaconnectorad.CfnTemplate.PrivateKeyFlagsV4Property(
                        client_version="clientVersion",
        
                        # the properties below are optional
                        exportable_key=False,
                        require_alternate_signature_algorithm=False,
                        require_same_key_renewal=False,
                        strong_key_protection_required=False,
                        use_legacy_provider=False
                    ),
                    subject_name_flags=pcaconnectorad.CfnTemplate.SubjectNameFlagsV4Property(
                        require_common_name=False,
                        require_directory_path=False,
                        require_dns_as_cn=False,
                        require_email=False,
                        san_require_directory_guid=False,
                        san_require_dns=False,
                        san_require_domain_dns=False,
                        san_require_email=False,
                        san_require_spn=False,
                        san_require_upn=False
                    ),
        
                    # the properties below are optional
                    hash_algorithm="hashAlgorithm",
                    superseded_templates=["supersededTemplates"]
                )
            ),
            name="name",
        
            # the properties below are optional
            reenroll_all_certificate_holders=False,
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
        connector_arn: builtins.str,
        definition: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.TemplateDefinitionProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        reenroll_all_certificate_holders: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param connector_arn: The Amazon Resource Name (ARN) that was returned when you called `CreateConnector <https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html>`_ .
        :param definition: Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.
        :param name: Name of the templates. Template names must be unique.
        :param reenroll_all_certificate_holders: This setting allows the major version of a template to be increased automatically. All members of Active Directory groups that are allowed to enroll with a template will receive a new certificate issued using that template.
        :param tags: Metadata assigned to a template consisting of a key-value pair.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__058e4ad420b7fd03441f402ba72d6e3735672960ebcc0af660d043e5de6b6b8b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTemplateProps(
            connector_arn=connector_arn,
            definition=definition,
            name=name,
            reenroll_all_certificate_holders=reenroll_all_certificate_holders,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__522513d3e7f800ff5cbeaf35a1bafe68be5a57527909827ac7a376f1ef743427)
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
            type_hints = typing.get_type_hints(_typecheckingstub__902de0f2c5a1c9d56b19d05be029dfc35dfe777e3a9d654d057b6f1b6926b6de)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrTemplateArn")
    def attr_template_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) that was returned when you called `CreateTemplate <https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html>`_ .

        :cloudformationAttribute: TemplateArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTemplateArn"))

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
    @jsii.member(jsii_name="connectorArn")
    def connector_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) that was returned when you called `CreateConnector <https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html>`_ .'''
        return typing.cast(builtins.str, jsii.get(self, "connectorArn"))

    @connector_arn.setter
    def connector_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__079513a352e43cc7c1ce98dcc5f5e231bf3be2045a92489328ee1b7d9e23157a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorArn", value)

    @builtins.property
    @jsii.member(jsii_name="definition")
    def definition(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.TemplateDefinitionProperty"]:
        '''Template configuration to define the information included in certificates.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.TemplateDefinitionProperty"], jsii.get(self, "definition"))

    @definition.setter
    def definition(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnTemplate.TemplateDefinitionProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa952e9ba8af0e0bd9e62b55d0cfdca23958bf5403c595f909316942859ca793)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definition", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''Name of the templates.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9501917493dbbe580243f80e21fe99ea039183a480eef09ed64d12264f51e0ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="reenrollAllCertificateHolders")
    def reenroll_all_certificate_holders(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''This setting allows the major version of a template to be increased automatically.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "reenrollAllCertificateHolders"))

    @reenroll_all_certificate_holders.setter
    def reenroll_all_certificate_holders(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55f6695aacde4eb1d915673bfb7f61d1f0779f429720942c4806aa7044eea5f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reenrollAllCertificateHolders", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Metadata assigned to a template consisting of a key-value pair.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2661de5cae87e986149f4775b0ec018c21243c4e7dd8205ae490405a376832a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.ApplicationPoliciesProperty",
        jsii_struct_bases=[],
        name_mapping={"policies": "policies", "critical": "critical"},
    )
    class ApplicationPoliciesProperty:
        def __init__(
            self,
            *,
            policies: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.ApplicationPolicyProperty", typing.Dict[builtins.str, typing.Any]]]]],
            critical: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Application policies describe what the certificate can be used for.

            :param policies: Application policies describe what the certificate can be used for.
            :param critical: Marks the application policy extension as critical.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-applicationpolicies.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                application_policies_property = pcaconnectorad.CfnTemplate.ApplicationPoliciesProperty(
                    policies=[pcaconnectorad.CfnTemplate.ApplicationPolicyProperty(
                        policy_object_identifier="policyObjectIdentifier",
                        policy_type="policyType"
                    )],
                
                    # the properties below are optional
                    critical=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3f9807ce79bbe5d1e70285819a93c0d50c131ea1e3ae32f2603d78790d787b8e)
                check_type(argname="argument policies", value=policies, expected_type=type_hints["policies"])
                check_type(argname="argument critical", value=critical, expected_type=type_hints["critical"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "policies": policies,
            }
            if critical is not None:
                self._values["critical"] = critical

        @builtins.property
        def policies(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTemplate.ApplicationPolicyProperty"]]]:
            '''Application policies describe what the certificate can be used for.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-applicationpolicies.html#cfn-pcaconnectorad-template-applicationpolicies-policies
            '''
            result = self._values.get("policies")
            assert result is not None, "Required property 'policies' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTemplate.ApplicationPolicyProperty"]]], result)

        @builtins.property
        def critical(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Marks the application policy extension as critical.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-applicationpolicies.html#cfn-pcaconnectorad-template-applicationpolicies-critical
            '''
            result = self._values.get("critical")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationPoliciesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.ApplicationPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "policy_object_identifier": "policyObjectIdentifier",
            "policy_type": "policyType",
        },
    )
    class ApplicationPolicyProperty:
        def __init__(
            self,
            *,
            policy_object_identifier: typing.Optional[builtins.str] = None,
            policy_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Application policies describe what the certificate can be used for.

            :param policy_object_identifier: The object identifier (OID) of an application policy.
            :param policy_type: The type of application policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-applicationpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                application_policy_property = pcaconnectorad.CfnTemplate.ApplicationPolicyProperty(
                    policy_object_identifier="policyObjectIdentifier",
                    policy_type="policyType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5398e02a2971edff45634bc912f9a2a8e06f7d87c7e08b6975be28903d770e92)
                check_type(argname="argument policy_object_identifier", value=policy_object_identifier, expected_type=type_hints["policy_object_identifier"])
                check_type(argname="argument policy_type", value=policy_type, expected_type=type_hints["policy_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if policy_object_identifier is not None:
                self._values["policy_object_identifier"] = policy_object_identifier
            if policy_type is not None:
                self._values["policy_type"] = policy_type

        @builtins.property
        def policy_object_identifier(self) -> typing.Optional[builtins.str]:
            '''The object identifier (OID) of an application policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-applicationpolicy.html#cfn-pcaconnectorad-template-applicationpolicy-policyobjectidentifier
            '''
            result = self._values.get("policy_object_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def policy_type(self) -> typing.Optional[builtins.str]:
            '''The type of application policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-applicationpolicy.html#cfn-pcaconnectorad-template-applicationpolicy-policytype
            '''
            result = self._values.get("policy_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.CertificateValidityProperty",
        jsii_struct_bases=[],
        name_mapping={
            "renewal_period": "renewalPeriod",
            "validity_period": "validityPeriod",
        },
    )
    class CertificateValidityProperty:
        def __init__(
            self,
            *,
            renewal_period: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.ValidityPeriodProperty", typing.Dict[builtins.str, typing.Any]]],
            validity_period: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.ValidityPeriodProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Information describing the end of the validity period of the certificate.

            This parameter sets the “Not After” date for the certificate. Certificate validity is the period of time during which a certificate is valid. Validity can be expressed as an explicit date and time when the certificate expires, or as a span of time after issuance, stated in days, months, or years. For more information, see Validity in RFC 5280. This value is unaffected when ValidityNotBefore is also specified. For example, if Validity is set to 20 days in the future, the certificate will expire 20 days from issuance time regardless of the ValidityNotBefore value.

            :param renewal_period: Renewal period is the period of time before certificate expiration when a new certificate will be requested.
            :param validity_period: Information describing the end of the validity period of the certificate. This parameter sets the “Not After” date for the certificate. Certificate validity is the period of time during which a certificate is valid. Validity can be expressed as an explicit date and time when the certificate expires, or as a span of time after issuance, stated in days, months, or years. For more information, see Validity in RFC 5280. This value is unaffected when ValidityNotBefore is also specified. For example, if Validity is set to 20 days in the future, the certificate will expire 20 days from issuance time regardless of the ValidityNotBefore value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-certificatevalidity.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                certificate_validity_property = pcaconnectorad.CfnTemplate.CertificateValidityProperty(
                    renewal_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                        period=123,
                        period_type="periodType"
                    ),
                    validity_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                        period=123,
                        period_type="periodType"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b4cdec65aa655f7eeeeab4a379104c931aa1af736720f784aa86045f4e6cade5)
                check_type(argname="argument renewal_period", value=renewal_period, expected_type=type_hints["renewal_period"])
                check_type(argname="argument validity_period", value=validity_period, expected_type=type_hints["validity_period"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "renewal_period": renewal_period,
                "validity_period": validity_period,
            }

        @builtins.property
        def renewal_period(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.ValidityPeriodProperty"]:
            '''Renewal period is the period of time before certificate expiration when a new certificate will be requested.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-certificatevalidity.html#cfn-pcaconnectorad-template-certificatevalidity-renewalperiod
            '''
            result = self._values.get("renewal_period")
            assert result is not None, "Required property 'renewal_period' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.ValidityPeriodProperty"], result)

        @builtins.property
        def validity_period(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.ValidityPeriodProperty"]:
            '''Information describing the end of the validity period of the certificate.

            This parameter sets the “Not After” date for the certificate. Certificate validity is the period of time during which a certificate is valid. Validity can be expressed as an explicit date and time when the certificate expires, or as a span of time after issuance, stated in days, months, or years. For more information, see Validity in RFC 5280. This value is unaffected when ValidityNotBefore is also specified. For example, if Validity is set to 20 days in the future, the certificate will expire 20 days from issuance time regardless of the ValidityNotBefore value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-certificatevalidity.html#cfn-pcaconnectorad-template-certificatevalidity-validityperiod
            '''
            result = self._values.get("validity_period")
            assert result is not None, "Required property 'validity_period' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.ValidityPeriodProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CertificateValidityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.EnrollmentFlagsV2Property",
        jsii_struct_bases=[],
        name_mapping={
            "enable_key_reuse_on_nt_token_keyset_storage_full": "enableKeyReuseOnNtTokenKeysetStorageFull",
            "include_symmetric_algorithms": "includeSymmetricAlgorithms",
            "no_security_extension": "noSecurityExtension",
            "remove_invalid_certificate_from_personal_store": "removeInvalidCertificateFromPersonalStore",
            "user_interaction_required": "userInteractionRequired",
        },
    )
    class EnrollmentFlagsV2Property:
        def __init__(
            self,
            *,
            enable_key_reuse_on_nt_token_keyset_storage_full: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_symmetric_algorithms: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            no_security_extension: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            remove_invalid_certificate_from_personal_store: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            user_interaction_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Template configurations for v2 template schema.

            :param enable_key_reuse_on_nt_token_keyset_storage_full: Allow renewal using the same key.
            :param include_symmetric_algorithms: Include symmetric algorithms allowed by the subject.
            :param no_security_extension: This flag instructs the CA to not include the security extension szOID_NTDS_CA_SECURITY_EXT (OID:1.3.6.1.4.1.311.25.2), as specified in [MS-WCCE] sections 2.2.2.7.7.4 and 3.2.2.6.2.1.4.5.9, in the issued certificate. This addresses a Windows Kerberos elevation-of-privilege vulnerability.
            :param remove_invalid_certificate_from_personal_store: Delete expired or revoked certificates instead of archiving them.
            :param user_interaction_required: Require user interaction when the subject is enrolled and the private key associated with the certificate is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv2.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                enrollment_flags_v2_property = pcaconnectorad.CfnTemplate.EnrollmentFlagsV2Property(
                    enable_key_reuse_on_nt_token_keyset_storage_full=False,
                    include_symmetric_algorithms=False,
                    no_security_extension=False,
                    remove_invalid_certificate_from_personal_store=False,
                    user_interaction_required=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__31d0076b2df64888291f4f323da23d8cbc5d3b6efaf716095d546e42d9d75cb6)
                check_type(argname="argument enable_key_reuse_on_nt_token_keyset_storage_full", value=enable_key_reuse_on_nt_token_keyset_storage_full, expected_type=type_hints["enable_key_reuse_on_nt_token_keyset_storage_full"])
                check_type(argname="argument include_symmetric_algorithms", value=include_symmetric_algorithms, expected_type=type_hints["include_symmetric_algorithms"])
                check_type(argname="argument no_security_extension", value=no_security_extension, expected_type=type_hints["no_security_extension"])
                check_type(argname="argument remove_invalid_certificate_from_personal_store", value=remove_invalid_certificate_from_personal_store, expected_type=type_hints["remove_invalid_certificate_from_personal_store"])
                check_type(argname="argument user_interaction_required", value=user_interaction_required, expected_type=type_hints["user_interaction_required"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enable_key_reuse_on_nt_token_keyset_storage_full is not None:
                self._values["enable_key_reuse_on_nt_token_keyset_storage_full"] = enable_key_reuse_on_nt_token_keyset_storage_full
            if include_symmetric_algorithms is not None:
                self._values["include_symmetric_algorithms"] = include_symmetric_algorithms
            if no_security_extension is not None:
                self._values["no_security_extension"] = no_security_extension
            if remove_invalid_certificate_from_personal_store is not None:
                self._values["remove_invalid_certificate_from_personal_store"] = remove_invalid_certificate_from_personal_store
            if user_interaction_required is not None:
                self._values["user_interaction_required"] = user_interaction_required

        @builtins.property
        def enable_key_reuse_on_nt_token_keyset_storage_full(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Allow renewal using the same key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv2.html#cfn-pcaconnectorad-template-enrollmentflagsv2-enablekeyreuseonnttokenkeysetstoragefull
            '''
            result = self._values.get("enable_key_reuse_on_nt_token_keyset_storage_full")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_symmetric_algorithms(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include symmetric algorithms allowed by the subject.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv2.html#cfn-pcaconnectorad-template-enrollmentflagsv2-includesymmetricalgorithms
            '''
            result = self._values.get("include_symmetric_algorithms")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def no_security_extension(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''This flag instructs the CA to not include the security extension szOID_NTDS_CA_SECURITY_EXT (OID:1.3.6.1.4.1.311.25.2), as specified in [MS-WCCE] sections 2.2.2.7.7.4 and 3.2.2.6.2.1.4.5.9, in the issued certificate. This addresses a Windows Kerberos elevation-of-privilege vulnerability.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv2.html#cfn-pcaconnectorad-template-enrollmentflagsv2-nosecurityextension
            '''
            result = self._values.get("no_security_extension")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def remove_invalid_certificate_from_personal_store(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Delete expired or revoked certificates instead of archiving them.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv2.html#cfn-pcaconnectorad-template-enrollmentflagsv2-removeinvalidcertificatefrompersonalstore
            '''
            result = self._values.get("remove_invalid_certificate_from_personal_store")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def user_interaction_required(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Require user interaction when the subject is enrolled and the private key associated with the certificate is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv2.html#cfn-pcaconnectorad-template-enrollmentflagsv2-userinteractionrequired
            '''
            result = self._values.get("user_interaction_required")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnrollmentFlagsV2Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.EnrollmentFlagsV3Property",
        jsii_struct_bases=[],
        name_mapping={
            "enable_key_reuse_on_nt_token_keyset_storage_full": "enableKeyReuseOnNtTokenKeysetStorageFull",
            "include_symmetric_algorithms": "includeSymmetricAlgorithms",
            "no_security_extension": "noSecurityExtension",
            "remove_invalid_certificate_from_personal_store": "removeInvalidCertificateFromPersonalStore",
            "user_interaction_required": "userInteractionRequired",
        },
    )
    class EnrollmentFlagsV3Property:
        def __init__(
            self,
            *,
            enable_key_reuse_on_nt_token_keyset_storage_full: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_symmetric_algorithms: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            no_security_extension: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            remove_invalid_certificate_from_personal_store: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            user_interaction_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Template configurations for v3 template schema.

            :param enable_key_reuse_on_nt_token_keyset_storage_full: Allow renewal using the same key.
            :param include_symmetric_algorithms: Include symmetric algorithms allowed by the subject.
            :param no_security_extension: This flag instructs the CA to not include the security extension szOID_NTDS_CA_SECURITY_EXT (OID:1.3.6.1.4.1.311.25.2), as specified in [MS-WCCE] sections 2.2.2.7.7.4 and 3.2.2.6.2.1.4.5.9, in the issued certificate. This addresses a Windows Kerberos elevation-of-privilege vulnerability.
            :param remove_invalid_certificate_from_personal_store: Delete expired or revoked certificates instead of archiving them.
            :param user_interaction_required: Require user interaction when the subject is enrolled and the private key associated with the certificate is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv3.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                enrollment_flags_v3_property = pcaconnectorad.CfnTemplate.EnrollmentFlagsV3Property(
                    enable_key_reuse_on_nt_token_keyset_storage_full=False,
                    include_symmetric_algorithms=False,
                    no_security_extension=False,
                    remove_invalid_certificate_from_personal_store=False,
                    user_interaction_required=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__503a76586e23e26e001311af23206f04ade685e0a3481b11037f8b9a352897ea)
                check_type(argname="argument enable_key_reuse_on_nt_token_keyset_storage_full", value=enable_key_reuse_on_nt_token_keyset_storage_full, expected_type=type_hints["enable_key_reuse_on_nt_token_keyset_storage_full"])
                check_type(argname="argument include_symmetric_algorithms", value=include_symmetric_algorithms, expected_type=type_hints["include_symmetric_algorithms"])
                check_type(argname="argument no_security_extension", value=no_security_extension, expected_type=type_hints["no_security_extension"])
                check_type(argname="argument remove_invalid_certificate_from_personal_store", value=remove_invalid_certificate_from_personal_store, expected_type=type_hints["remove_invalid_certificate_from_personal_store"])
                check_type(argname="argument user_interaction_required", value=user_interaction_required, expected_type=type_hints["user_interaction_required"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enable_key_reuse_on_nt_token_keyset_storage_full is not None:
                self._values["enable_key_reuse_on_nt_token_keyset_storage_full"] = enable_key_reuse_on_nt_token_keyset_storage_full
            if include_symmetric_algorithms is not None:
                self._values["include_symmetric_algorithms"] = include_symmetric_algorithms
            if no_security_extension is not None:
                self._values["no_security_extension"] = no_security_extension
            if remove_invalid_certificate_from_personal_store is not None:
                self._values["remove_invalid_certificate_from_personal_store"] = remove_invalid_certificate_from_personal_store
            if user_interaction_required is not None:
                self._values["user_interaction_required"] = user_interaction_required

        @builtins.property
        def enable_key_reuse_on_nt_token_keyset_storage_full(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Allow renewal using the same key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv3.html#cfn-pcaconnectorad-template-enrollmentflagsv3-enablekeyreuseonnttokenkeysetstoragefull
            '''
            result = self._values.get("enable_key_reuse_on_nt_token_keyset_storage_full")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_symmetric_algorithms(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include symmetric algorithms allowed by the subject.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv3.html#cfn-pcaconnectorad-template-enrollmentflagsv3-includesymmetricalgorithms
            '''
            result = self._values.get("include_symmetric_algorithms")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def no_security_extension(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''This flag instructs the CA to not include the security extension szOID_NTDS_CA_SECURITY_EXT (OID:1.3.6.1.4.1.311.25.2), as specified in [MS-WCCE] sections 2.2.2.7.7.4 and 3.2.2.6.2.1.4.5.9, in the issued certificate. This addresses a Windows Kerberos elevation-of-privilege vulnerability.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv3.html#cfn-pcaconnectorad-template-enrollmentflagsv3-nosecurityextension
            '''
            result = self._values.get("no_security_extension")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def remove_invalid_certificate_from_personal_store(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Delete expired or revoked certificates instead of archiving them.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv3.html#cfn-pcaconnectorad-template-enrollmentflagsv3-removeinvalidcertificatefrompersonalstore
            '''
            result = self._values.get("remove_invalid_certificate_from_personal_store")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def user_interaction_required(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Require user interaction when the subject is enrolled and the private key associated with the certificate is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv3.html#cfn-pcaconnectorad-template-enrollmentflagsv3-userinteractionrequired
            '''
            result = self._values.get("user_interaction_required")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnrollmentFlagsV3Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.EnrollmentFlagsV4Property",
        jsii_struct_bases=[],
        name_mapping={
            "enable_key_reuse_on_nt_token_keyset_storage_full": "enableKeyReuseOnNtTokenKeysetStorageFull",
            "include_symmetric_algorithms": "includeSymmetricAlgorithms",
            "no_security_extension": "noSecurityExtension",
            "remove_invalid_certificate_from_personal_store": "removeInvalidCertificateFromPersonalStore",
            "user_interaction_required": "userInteractionRequired",
        },
    )
    class EnrollmentFlagsV4Property:
        def __init__(
            self,
            *,
            enable_key_reuse_on_nt_token_keyset_storage_full: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_symmetric_algorithms: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            no_security_extension: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            remove_invalid_certificate_from_personal_store: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            user_interaction_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Template configurations for v4 template schema.

            :param enable_key_reuse_on_nt_token_keyset_storage_full: Allow renewal using the same key.
            :param include_symmetric_algorithms: Include symmetric algorithms allowed by the subject.
            :param no_security_extension: This flag instructs the CA to not include the security extension szOID_NTDS_CA_SECURITY_EXT (OID:1.3.6.1.4.1.311.25.2), as specified in [MS-WCCE] sections 2.2.2.7.7.4 and 3.2.2.6.2.1.4.5.9, in the issued certificate. This addresses a Windows Kerberos elevation-of-privilege vulnerability.
            :param remove_invalid_certificate_from_personal_store: Delete expired or revoked certificates instead of archiving them.
            :param user_interaction_required: Require user interaction when the subject is enrolled and the private key associated with the certificate is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv4.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                enrollment_flags_v4_property = pcaconnectorad.CfnTemplate.EnrollmentFlagsV4Property(
                    enable_key_reuse_on_nt_token_keyset_storage_full=False,
                    include_symmetric_algorithms=False,
                    no_security_extension=False,
                    remove_invalid_certificate_from_personal_store=False,
                    user_interaction_required=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8c3dbe764d7841c99b8270527bff9cfbf7b80b333e77d3386deefdbae8a0aa63)
                check_type(argname="argument enable_key_reuse_on_nt_token_keyset_storage_full", value=enable_key_reuse_on_nt_token_keyset_storage_full, expected_type=type_hints["enable_key_reuse_on_nt_token_keyset_storage_full"])
                check_type(argname="argument include_symmetric_algorithms", value=include_symmetric_algorithms, expected_type=type_hints["include_symmetric_algorithms"])
                check_type(argname="argument no_security_extension", value=no_security_extension, expected_type=type_hints["no_security_extension"])
                check_type(argname="argument remove_invalid_certificate_from_personal_store", value=remove_invalid_certificate_from_personal_store, expected_type=type_hints["remove_invalid_certificate_from_personal_store"])
                check_type(argname="argument user_interaction_required", value=user_interaction_required, expected_type=type_hints["user_interaction_required"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enable_key_reuse_on_nt_token_keyset_storage_full is not None:
                self._values["enable_key_reuse_on_nt_token_keyset_storage_full"] = enable_key_reuse_on_nt_token_keyset_storage_full
            if include_symmetric_algorithms is not None:
                self._values["include_symmetric_algorithms"] = include_symmetric_algorithms
            if no_security_extension is not None:
                self._values["no_security_extension"] = no_security_extension
            if remove_invalid_certificate_from_personal_store is not None:
                self._values["remove_invalid_certificate_from_personal_store"] = remove_invalid_certificate_from_personal_store
            if user_interaction_required is not None:
                self._values["user_interaction_required"] = user_interaction_required

        @builtins.property
        def enable_key_reuse_on_nt_token_keyset_storage_full(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Allow renewal using the same key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv4.html#cfn-pcaconnectorad-template-enrollmentflagsv4-enablekeyreuseonnttokenkeysetstoragefull
            '''
            result = self._values.get("enable_key_reuse_on_nt_token_keyset_storage_full")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_symmetric_algorithms(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include symmetric algorithms allowed by the subject.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv4.html#cfn-pcaconnectorad-template-enrollmentflagsv4-includesymmetricalgorithms
            '''
            result = self._values.get("include_symmetric_algorithms")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def no_security_extension(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''This flag instructs the CA to not include the security extension szOID_NTDS_CA_SECURITY_EXT (OID:1.3.6.1.4.1.311.25.2), as specified in [MS-WCCE] sections 2.2.2.7.7.4 and 3.2.2.6.2.1.4.5.9, in the issued certificate. This addresses a Windows Kerberos elevation-of-privilege vulnerability.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv4.html#cfn-pcaconnectorad-template-enrollmentflagsv4-nosecurityextension
            '''
            result = self._values.get("no_security_extension")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def remove_invalid_certificate_from_personal_store(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Delete expired or revoked certificates instead of archiving them.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv4.html#cfn-pcaconnectorad-template-enrollmentflagsv4-removeinvalidcertificatefrompersonalstore
            '''
            result = self._values.get("remove_invalid_certificate_from_personal_store")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def user_interaction_required(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Require user interaction when the subject is enrolled and the private key associated with the certificate is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-enrollmentflagsv4.html#cfn-pcaconnectorad-template-enrollmentflagsv4-userinteractionrequired
            '''
            result = self._values.get("user_interaction_required")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnrollmentFlagsV4Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.ExtensionsV2Property",
        jsii_struct_bases=[],
        name_mapping={
            "key_usage": "keyUsage",
            "application_policies": "applicationPolicies",
        },
    )
    class ExtensionsV2Property:
        def __init__(
            self,
            *,
            key_usage: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.KeyUsageProperty", typing.Dict[builtins.str, typing.Any]]],
            application_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.ApplicationPoliciesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Certificate extensions for v2 template schema.

            :param key_usage: The key usage extension defines the purpose (e.g., encipherment, signature, certificate signing) of the key contained in the certificate.
            :param application_policies: Application policies specify what the certificate is used for and its purpose.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-extensionsv2.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                extensions_v2_property = pcaconnectorad.CfnTemplate.ExtensionsV2Property(
                    key_usage=pcaconnectorad.CfnTemplate.KeyUsageProperty(
                        usage_flags=pcaconnectorad.CfnTemplate.KeyUsageFlagsProperty(
                            data_encipherment=False,
                            digital_signature=False,
                            key_agreement=False,
                            key_encipherment=False,
                            non_repudiation=False
                        ),
                
                        # the properties below are optional
                        critical=False
                    ),
                
                    # the properties below are optional
                    application_policies=pcaconnectorad.CfnTemplate.ApplicationPoliciesProperty(
                        policies=[pcaconnectorad.CfnTemplate.ApplicationPolicyProperty(
                            policy_object_identifier="policyObjectIdentifier",
                            policy_type="policyType"
                        )],
                
                        # the properties below are optional
                        critical=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0141d8fd6f7754483c21d402e5a2141226e85c41cd0ed6de1704acfed6d37da8)
                check_type(argname="argument key_usage", value=key_usage, expected_type=type_hints["key_usage"])
                check_type(argname="argument application_policies", value=application_policies, expected_type=type_hints["application_policies"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key_usage": key_usage,
            }
            if application_policies is not None:
                self._values["application_policies"] = application_policies

        @builtins.property
        def key_usage(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.KeyUsageProperty"]:
            '''The key usage extension defines the purpose (e.g., encipherment, signature, certificate signing) of the key contained in the certificate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-extensionsv2.html#cfn-pcaconnectorad-template-extensionsv2-keyusage
            '''
            result = self._values.get("key_usage")
            assert result is not None, "Required property 'key_usage' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.KeyUsageProperty"], result)

        @builtins.property
        def application_policies(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTemplate.ApplicationPoliciesProperty"]]:
            '''Application policies specify what the certificate is used for and its purpose.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-extensionsv2.html#cfn-pcaconnectorad-template-extensionsv2-applicationpolicies
            '''
            result = self._values.get("application_policies")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTemplate.ApplicationPoliciesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExtensionsV2Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.ExtensionsV3Property",
        jsii_struct_bases=[],
        name_mapping={
            "key_usage": "keyUsage",
            "application_policies": "applicationPolicies",
        },
    )
    class ExtensionsV3Property:
        def __init__(
            self,
            *,
            key_usage: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.KeyUsageProperty", typing.Dict[builtins.str, typing.Any]]],
            application_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.ApplicationPoliciesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Certificate extensions for v3 template schema.

            :param key_usage: The key usage extension defines the purpose (e.g., encipherment, signature, certificate signing) of the key contained in the certificate.
            :param application_policies: Application policies specify what the certificate is used for and its purpose.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-extensionsv3.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                extensions_v3_property = pcaconnectorad.CfnTemplate.ExtensionsV3Property(
                    key_usage=pcaconnectorad.CfnTemplate.KeyUsageProperty(
                        usage_flags=pcaconnectorad.CfnTemplate.KeyUsageFlagsProperty(
                            data_encipherment=False,
                            digital_signature=False,
                            key_agreement=False,
                            key_encipherment=False,
                            non_repudiation=False
                        ),
                
                        # the properties below are optional
                        critical=False
                    ),
                
                    # the properties below are optional
                    application_policies=pcaconnectorad.CfnTemplate.ApplicationPoliciesProperty(
                        policies=[pcaconnectorad.CfnTemplate.ApplicationPolicyProperty(
                            policy_object_identifier="policyObjectIdentifier",
                            policy_type="policyType"
                        )],
                
                        # the properties below are optional
                        critical=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5bc196c1d5fd1dd60e51f454b41b5cb30ae245ceec4cd14d522a2deb5ff66714)
                check_type(argname="argument key_usage", value=key_usage, expected_type=type_hints["key_usage"])
                check_type(argname="argument application_policies", value=application_policies, expected_type=type_hints["application_policies"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key_usage": key_usage,
            }
            if application_policies is not None:
                self._values["application_policies"] = application_policies

        @builtins.property
        def key_usage(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.KeyUsageProperty"]:
            '''The key usage extension defines the purpose (e.g., encipherment, signature, certificate signing) of the key contained in the certificate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-extensionsv3.html#cfn-pcaconnectorad-template-extensionsv3-keyusage
            '''
            result = self._values.get("key_usage")
            assert result is not None, "Required property 'key_usage' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.KeyUsageProperty"], result)

        @builtins.property
        def application_policies(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTemplate.ApplicationPoliciesProperty"]]:
            '''Application policies specify what the certificate is used for and its purpose.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-extensionsv3.html#cfn-pcaconnectorad-template-extensionsv3-applicationpolicies
            '''
            result = self._values.get("application_policies")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTemplate.ApplicationPoliciesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExtensionsV3Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.ExtensionsV4Property",
        jsii_struct_bases=[],
        name_mapping={
            "key_usage": "keyUsage",
            "application_policies": "applicationPolicies",
        },
    )
    class ExtensionsV4Property:
        def __init__(
            self,
            *,
            key_usage: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.KeyUsageProperty", typing.Dict[builtins.str, typing.Any]]],
            application_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.ApplicationPoliciesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Certificate extensions for v4 template schema.

            :param key_usage: The key usage extension defines the purpose (e.g., encipherment, signature) of the key contained in the certificate.
            :param application_policies: Application policies specify what the certificate is used for and its purpose.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-extensionsv4.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                extensions_v4_property = pcaconnectorad.CfnTemplate.ExtensionsV4Property(
                    key_usage=pcaconnectorad.CfnTemplate.KeyUsageProperty(
                        usage_flags=pcaconnectorad.CfnTemplate.KeyUsageFlagsProperty(
                            data_encipherment=False,
                            digital_signature=False,
                            key_agreement=False,
                            key_encipherment=False,
                            non_repudiation=False
                        ),
                
                        # the properties below are optional
                        critical=False
                    ),
                
                    # the properties below are optional
                    application_policies=pcaconnectorad.CfnTemplate.ApplicationPoliciesProperty(
                        policies=[pcaconnectorad.CfnTemplate.ApplicationPolicyProperty(
                            policy_object_identifier="policyObjectIdentifier",
                            policy_type="policyType"
                        )],
                
                        # the properties below are optional
                        critical=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__601e4ea2eea3cb68c41cbee071f8b18ff40cd8225923970223bb0622dbe80979)
                check_type(argname="argument key_usage", value=key_usage, expected_type=type_hints["key_usage"])
                check_type(argname="argument application_policies", value=application_policies, expected_type=type_hints["application_policies"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key_usage": key_usage,
            }
            if application_policies is not None:
                self._values["application_policies"] = application_policies

        @builtins.property
        def key_usage(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.KeyUsageProperty"]:
            '''The key usage extension defines the purpose (e.g., encipherment, signature) of the key contained in the certificate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-extensionsv4.html#cfn-pcaconnectorad-template-extensionsv4-keyusage
            '''
            result = self._values.get("key_usage")
            assert result is not None, "Required property 'key_usage' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.KeyUsageProperty"], result)

        @builtins.property
        def application_policies(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTemplate.ApplicationPoliciesProperty"]]:
            '''Application policies specify what the certificate is used for and its purpose.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-extensionsv4.html#cfn-pcaconnectorad-template-extensionsv4-applicationpolicies
            '''
            result = self._values.get("application_policies")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTemplate.ApplicationPoliciesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExtensionsV4Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.GeneralFlagsV2Property",
        jsii_struct_bases=[],
        name_mapping={
            "auto_enrollment": "autoEnrollment",
            "machine_type": "machineType",
        },
    )
    class GeneralFlagsV2Property:
        def __init__(
            self,
            *,
            auto_enrollment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            machine_type: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''General flags for v2 template schema that defines if the template is for a machine or a user and if the template can be issued using autoenrollment.

            :param auto_enrollment: Allows certificate issuance using autoenrollment. Set to TRUE to allow autoenrollment.
            :param machine_type: Defines if the template is for machines or users. Set to TRUE if the template is for machines. Set to FALSE if the template is for users.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-generalflagsv2.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                general_flags_v2_property = pcaconnectorad.CfnTemplate.GeneralFlagsV2Property(
                    auto_enrollment=False,
                    machine_type=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__097faefbc9f8cebe8de0057f783e113aed655061f3c6eed7bd1853fe59e8eff7)
                check_type(argname="argument auto_enrollment", value=auto_enrollment, expected_type=type_hints["auto_enrollment"])
                check_type(argname="argument machine_type", value=machine_type, expected_type=type_hints["machine_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if auto_enrollment is not None:
                self._values["auto_enrollment"] = auto_enrollment
            if machine_type is not None:
                self._values["machine_type"] = machine_type

        @builtins.property
        def auto_enrollment(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Allows certificate issuance using autoenrollment.

            Set to TRUE to allow autoenrollment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-generalflagsv2.html#cfn-pcaconnectorad-template-generalflagsv2-autoenrollment
            '''
            result = self._values.get("auto_enrollment")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def machine_type(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Defines if the template is for machines or users.

            Set to TRUE if the template is for machines. Set to FALSE if the template is for users.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-generalflagsv2.html#cfn-pcaconnectorad-template-generalflagsv2-machinetype
            '''
            result = self._values.get("machine_type")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GeneralFlagsV2Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.GeneralFlagsV3Property",
        jsii_struct_bases=[],
        name_mapping={
            "auto_enrollment": "autoEnrollment",
            "machine_type": "machineType",
        },
    )
    class GeneralFlagsV3Property:
        def __init__(
            self,
            *,
            auto_enrollment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            machine_type: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''General flags for v3 template schema that defines if the template is for a machine or a user and if the template can be issued using autoenrollment.

            :param auto_enrollment: Allows certificate issuance using autoenrollment. Set to TRUE to allow autoenrollment.
            :param machine_type: Defines if the template is for machines or users. Set to TRUE if the template is for machines. Set to FALSE if the template is for users

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-generalflagsv3.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                general_flags_v3_property = pcaconnectorad.CfnTemplate.GeneralFlagsV3Property(
                    auto_enrollment=False,
                    machine_type=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a5cce72190738262664533347db8bc91239197327c27f7f816b4293abe93de3a)
                check_type(argname="argument auto_enrollment", value=auto_enrollment, expected_type=type_hints["auto_enrollment"])
                check_type(argname="argument machine_type", value=machine_type, expected_type=type_hints["machine_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if auto_enrollment is not None:
                self._values["auto_enrollment"] = auto_enrollment
            if machine_type is not None:
                self._values["machine_type"] = machine_type

        @builtins.property
        def auto_enrollment(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Allows certificate issuance using autoenrollment.

            Set to TRUE to allow autoenrollment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-generalflagsv3.html#cfn-pcaconnectorad-template-generalflagsv3-autoenrollment
            '''
            result = self._values.get("auto_enrollment")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def machine_type(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Defines if the template is for machines or users.

            Set to TRUE if the template is for machines. Set to FALSE if the template is for users

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-generalflagsv3.html#cfn-pcaconnectorad-template-generalflagsv3-machinetype
            '''
            result = self._values.get("machine_type")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GeneralFlagsV3Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.GeneralFlagsV4Property",
        jsii_struct_bases=[],
        name_mapping={
            "auto_enrollment": "autoEnrollment",
            "machine_type": "machineType",
        },
    )
    class GeneralFlagsV4Property:
        def __init__(
            self,
            *,
            auto_enrollment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            machine_type: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''General flags for v4 template schema that defines if the template is for a machine or a user and if the template can be issued using autoenrollment.

            :param auto_enrollment: Allows certificate issuance using autoenrollment. Set to TRUE to allow autoenrollment.
            :param machine_type: Defines if the template is for machines or users. Set to TRUE if the template is for machines. Set to FALSE if the template is for users

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-generalflagsv4.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                general_flags_v4_property = pcaconnectorad.CfnTemplate.GeneralFlagsV4Property(
                    auto_enrollment=False,
                    machine_type=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b049cb9c768149c0cf11c978d7de1e5d940749022cdc037468cdb29e00809ba9)
                check_type(argname="argument auto_enrollment", value=auto_enrollment, expected_type=type_hints["auto_enrollment"])
                check_type(argname="argument machine_type", value=machine_type, expected_type=type_hints["machine_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if auto_enrollment is not None:
                self._values["auto_enrollment"] = auto_enrollment
            if machine_type is not None:
                self._values["machine_type"] = machine_type

        @builtins.property
        def auto_enrollment(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Allows certificate issuance using autoenrollment.

            Set to TRUE to allow autoenrollment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-generalflagsv4.html#cfn-pcaconnectorad-template-generalflagsv4-autoenrollment
            '''
            result = self._values.get("auto_enrollment")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def machine_type(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Defines if the template is for machines or users.

            Set to TRUE if the template is for machines. Set to FALSE if the template is for users

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-generalflagsv4.html#cfn-pcaconnectorad-template-generalflagsv4-machinetype
            '''
            result = self._values.get("machine_type")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GeneralFlagsV4Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.KeyUsageFlagsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_encipherment": "dataEncipherment",
            "digital_signature": "digitalSignature",
            "key_agreement": "keyAgreement",
            "key_encipherment": "keyEncipherment",
            "non_repudiation": "nonRepudiation",
        },
    )
    class KeyUsageFlagsProperty:
        def __init__(
            self,
            *,
            data_encipherment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            digital_signature: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            key_agreement: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            key_encipherment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            non_repudiation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The key usage flags represent the purpose (e.g., encipherment, signature) of the key contained in the certificate.

            :param data_encipherment: DataEncipherment is asserted when the subject public key is used for directly enciphering raw user data without the use of an intermediate symmetric cipher.
            :param digital_signature: The digitalSignature is asserted when the subject public key is used for verifying digital signatures.
            :param key_agreement: KeyAgreement is asserted when the subject public key is used for key agreement.
            :param key_encipherment: KeyEncipherment is asserted when the subject public key is used for enciphering private or secret keys, i.e., for key transport.
            :param non_repudiation: NonRepudiation is asserted when the subject public key is used to verify digital signatures.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusageflags.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                key_usage_flags_property = pcaconnectorad.CfnTemplate.KeyUsageFlagsProperty(
                    data_encipherment=False,
                    digital_signature=False,
                    key_agreement=False,
                    key_encipherment=False,
                    non_repudiation=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0c80dba709763d03d37f95ecc20a6778d922627a5e7fff950156e15d8cd108bf)
                check_type(argname="argument data_encipherment", value=data_encipherment, expected_type=type_hints["data_encipherment"])
                check_type(argname="argument digital_signature", value=digital_signature, expected_type=type_hints["digital_signature"])
                check_type(argname="argument key_agreement", value=key_agreement, expected_type=type_hints["key_agreement"])
                check_type(argname="argument key_encipherment", value=key_encipherment, expected_type=type_hints["key_encipherment"])
                check_type(argname="argument non_repudiation", value=non_repudiation, expected_type=type_hints["non_repudiation"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if data_encipherment is not None:
                self._values["data_encipherment"] = data_encipherment
            if digital_signature is not None:
                self._values["digital_signature"] = digital_signature
            if key_agreement is not None:
                self._values["key_agreement"] = key_agreement
            if key_encipherment is not None:
                self._values["key_encipherment"] = key_encipherment
            if non_repudiation is not None:
                self._values["non_repudiation"] = non_repudiation

        @builtins.property
        def data_encipherment(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''DataEncipherment is asserted when the subject public key is used for directly enciphering raw user data without the use of an intermediate symmetric cipher.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusageflags.html#cfn-pcaconnectorad-template-keyusageflags-dataencipherment
            '''
            result = self._values.get("data_encipherment")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def digital_signature(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The digitalSignature is asserted when the subject public key is used for verifying digital signatures.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusageflags.html#cfn-pcaconnectorad-template-keyusageflags-digitalsignature
            '''
            result = self._values.get("digital_signature")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def key_agreement(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''KeyAgreement is asserted when the subject public key is used for key agreement.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusageflags.html#cfn-pcaconnectorad-template-keyusageflags-keyagreement
            '''
            result = self._values.get("key_agreement")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def key_encipherment(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''KeyEncipherment is asserted when the subject public key is used for enciphering private or secret keys, i.e., for key transport.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusageflags.html#cfn-pcaconnectorad-template-keyusageflags-keyencipherment
            '''
            result = self._values.get("key_encipherment")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def non_repudiation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''NonRepudiation is asserted when the subject public key is used to verify digital signatures.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusageflags.html#cfn-pcaconnectorad-template-keyusageflags-nonrepudiation
            '''
            result = self._values.get("non_repudiation")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyUsageFlagsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.KeyUsageProperty",
        jsii_struct_bases=[],
        name_mapping={"usage_flags": "usageFlags", "critical": "critical"},
    )
    class KeyUsageProperty:
        def __init__(
            self,
            *,
            usage_flags: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.KeyUsageFlagsProperty", typing.Dict[builtins.str, typing.Any]]],
            critical: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The key usage extension defines the purpose (e.g., encipherment, signature) of the key contained in the certificate.

            :param usage_flags: The key usage flags represent the purpose (e.g., encipherment, signature) of the key contained in the certificate.
            :param critical: Sets the key usage extension to critical.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                key_usage_property = pcaconnectorad.CfnTemplate.KeyUsageProperty(
                    usage_flags=pcaconnectorad.CfnTemplate.KeyUsageFlagsProperty(
                        data_encipherment=False,
                        digital_signature=False,
                        key_agreement=False,
                        key_encipherment=False,
                        non_repudiation=False
                    ),
                
                    # the properties below are optional
                    critical=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7820e30f088ec528d6503414a4752bd7dc51a8186ee36b410ff7ec91c6b731a2)
                check_type(argname="argument usage_flags", value=usage_flags, expected_type=type_hints["usage_flags"])
                check_type(argname="argument critical", value=critical, expected_type=type_hints["critical"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "usage_flags": usage_flags,
            }
            if critical is not None:
                self._values["critical"] = critical

        @builtins.property
        def usage_flags(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.KeyUsageFlagsProperty"]:
            '''The key usage flags represent the purpose (e.g., encipherment, signature) of the key contained in the certificate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusage.html#cfn-pcaconnectorad-template-keyusage-usageflags
            '''
            result = self._values.get("usage_flags")
            assert result is not None, "Required property 'usage_flags' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.KeyUsageFlagsProperty"], result)

        @builtins.property
        def critical(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Sets the key usage extension to critical.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusage.html#cfn-pcaconnectorad-template-keyusage-critical
            '''
            result = self._values.get("critical")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyUsageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.KeyUsagePropertyFlagsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "decrypt": "decrypt",
            "key_agreement": "keyAgreement",
            "sign": "sign",
        },
    )
    class KeyUsagePropertyFlagsProperty:
        def __init__(
            self,
            *,
            decrypt: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            key_agreement: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            sign: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Specifies key usage.

            :param decrypt: Allows key for encryption and decryption.
            :param key_agreement: Allows key exchange without encryption.
            :param sign: Allow key use for digital signature.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusagepropertyflags.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                key_usage_property_flags_property = pcaconnectorad.CfnTemplate.KeyUsagePropertyFlagsProperty(
                    decrypt=False,
                    key_agreement=False,
                    sign=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3eb45f2f53233d30a1605227f9826c39b26061c0487cbf31b14d99ebda3a3988)
                check_type(argname="argument decrypt", value=decrypt, expected_type=type_hints["decrypt"])
                check_type(argname="argument key_agreement", value=key_agreement, expected_type=type_hints["key_agreement"])
                check_type(argname="argument sign", value=sign, expected_type=type_hints["sign"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if decrypt is not None:
                self._values["decrypt"] = decrypt
            if key_agreement is not None:
                self._values["key_agreement"] = key_agreement
            if sign is not None:
                self._values["sign"] = sign

        @builtins.property
        def decrypt(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Allows key for encryption and decryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusagepropertyflags.html#cfn-pcaconnectorad-template-keyusagepropertyflags-decrypt
            '''
            result = self._values.get("decrypt")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def key_agreement(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Allows key exchange without encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusagepropertyflags.html#cfn-pcaconnectorad-template-keyusagepropertyflags-keyagreement
            '''
            result = self._values.get("key_agreement")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def sign(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Allow key use for digital signature.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusagepropertyflags.html#cfn-pcaconnectorad-template-keyusagepropertyflags-sign
            '''
            result = self._values.get("sign")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyUsagePropertyFlagsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.KeyUsagePropertyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "property_flags": "propertyFlags",
            "property_type": "propertyType",
        },
    )
    class KeyUsagePropertyProperty:
        def __init__(
            self,
            *,
            property_flags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.KeyUsagePropertyFlagsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            property_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The key usage property defines the purpose of the private key contained in the certificate.

            You can specify specific purposes using property flags or all by using property type ALL.

            :param property_flags: You can specify key usage for encryption, key agreement, and signature. You can use property flags or property type but not both.
            :param property_type: You can specify all key usages using property type ALL. You can use property type or property flags but not both.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusageproperty.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                key_usage_property_property = pcaconnectorad.CfnTemplate.KeyUsagePropertyProperty(
                    property_flags=pcaconnectorad.CfnTemplate.KeyUsagePropertyFlagsProperty(
                        decrypt=False,
                        key_agreement=False,
                        sign=False
                    ),
                    property_type="propertyType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__affa60f9efeb947eabcf0c21ec7d80a0c06bcf71ee3f241f69c5b78d4b7f7818)
                check_type(argname="argument property_flags", value=property_flags, expected_type=type_hints["property_flags"])
                check_type(argname="argument property_type", value=property_type, expected_type=type_hints["property_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if property_flags is not None:
                self._values["property_flags"] = property_flags
            if property_type is not None:
                self._values["property_type"] = property_type

        @builtins.property
        def property_flags(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTemplate.KeyUsagePropertyFlagsProperty"]]:
            '''You can specify key usage for encryption, key agreement, and signature.

            You can use property flags or property type but not both.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusageproperty.html#cfn-pcaconnectorad-template-keyusageproperty-propertyflags
            '''
            result = self._values.get("property_flags")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTemplate.KeyUsagePropertyFlagsProperty"]], result)

        @builtins.property
        def property_type(self) -> typing.Optional[builtins.str]:
            '''You can specify all key usages using property type ALL.

            You can use property type or property flags but not both.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-keyusageproperty.html#cfn-pcaconnectorad-template-keyusageproperty-propertytype
            '''
            result = self._values.get("property_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyUsagePropertyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.PrivateKeyAttributesV2Property",
        jsii_struct_bases=[],
        name_mapping={
            "key_spec": "keySpec",
            "minimal_key_length": "minimalKeyLength",
            "crypto_providers": "cryptoProviders",
        },
    )
    class PrivateKeyAttributesV2Property:
        def __init__(
            self,
            *,
            key_spec: builtins.str,
            minimal_key_length: jsii.Number,
            crypto_providers: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Defines the attributes of the private key.

            :param key_spec: Defines the purpose of the private key. Set it to "KEY_EXCHANGE" or "SIGNATURE" value.
            :param minimal_key_length: Set the minimum key length of the private key.
            :param crypto_providers: Defines the cryptographic providers used to generate the private key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv2.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                private_key_attributes_v2_property = pcaconnectorad.CfnTemplate.PrivateKeyAttributesV2Property(
                    key_spec="keySpec",
                    minimal_key_length=123,
                
                    # the properties below are optional
                    crypto_providers=["cryptoProviders"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a0da38511e8586071939df45f55c73f6ea301eca8b340d0c8584b2699e138d8e)
                check_type(argname="argument key_spec", value=key_spec, expected_type=type_hints["key_spec"])
                check_type(argname="argument minimal_key_length", value=minimal_key_length, expected_type=type_hints["minimal_key_length"])
                check_type(argname="argument crypto_providers", value=crypto_providers, expected_type=type_hints["crypto_providers"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key_spec": key_spec,
                "minimal_key_length": minimal_key_length,
            }
            if crypto_providers is not None:
                self._values["crypto_providers"] = crypto_providers

        @builtins.property
        def key_spec(self) -> builtins.str:
            '''Defines the purpose of the private key.

            Set it to "KEY_EXCHANGE" or "SIGNATURE" value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv2.html#cfn-pcaconnectorad-template-privatekeyattributesv2-keyspec
            '''
            result = self._values.get("key_spec")
            assert result is not None, "Required property 'key_spec' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def minimal_key_length(self) -> jsii.Number:
            '''Set the minimum key length of the private key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv2.html#cfn-pcaconnectorad-template-privatekeyattributesv2-minimalkeylength
            '''
            result = self._values.get("minimal_key_length")
            assert result is not None, "Required property 'minimal_key_length' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def crypto_providers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Defines the cryptographic providers used to generate the private key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv2.html#cfn-pcaconnectorad-template-privatekeyattributesv2-cryptoproviders
            '''
            result = self._values.get("crypto_providers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PrivateKeyAttributesV2Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.PrivateKeyAttributesV3Property",
        jsii_struct_bases=[],
        name_mapping={
            "algorithm": "algorithm",
            "key_spec": "keySpec",
            "key_usage_property": "keyUsageProperty",
            "minimal_key_length": "minimalKeyLength",
            "crypto_providers": "cryptoProviders",
        },
    )
    class PrivateKeyAttributesV3Property:
        def __init__(
            self,
            *,
            algorithm: builtins.str,
            key_spec: builtins.str,
            key_usage_property: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.KeyUsagePropertyProperty", typing.Dict[builtins.str, typing.Any]]],
            minimal_key_length: jsii.Number,
            crypto_providers: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Defines the attributes of the private key.

            :param algorithm: Defines the algorithm used to generate the private key.
            :param key_spec: Defines the purpose of the private key. Set it to "KEY_EXCHANGE" or "SIGNATURE" value.
            :param key_usage_property: The key usage property defines the purpose of the private key contained in the certificate. You can specify specific purposes using property flags or all by using property type ALL.
            :param minimal_key_length: Set the minimum key length of the private key.
            :param crypto_providers: Defines the cryptographic providers used to generate the private key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv3.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                private_key_attributes_v3_property = pcaconnectorad.CfnTemplate.PrivateKeyAttributesV3Property(
                    algorithm="algorithm",
                    key_spec="keySpec",
                    key_usage_property=pcaconnectorad.CfnTemplate.KeyUsagePropertyProperty(
                        property_flags=pcaconnectorad.CfnTemplate.KeyUsagePropertyFlagsProperty(
                            decrypt=False,
                            key_agreement=False,
                            sign=False
                        ),
                        property_type="propertyType"
                    ),
                    minimal_key_length=123,
                
                    # the properties below are optional
                    crypto_providers=["cryptoProviders"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2e9e3e2c2671b7460269d56c9b1fa79f71e05a898d752d57c8f7ec1252321c0a)
                check_type(argname="argument algorithm", value=algorithm, expected_type=type_hints["algorithm"])
                check_type(argname="argument key_spec", value=key_spec, expected_type=type_hints["key_spec"])
                check_type(argname="argument key_usage_property", value=key_usage_property, expected_type=type_hints["key_usage_property"])
                check_type(argname="argument minimal_key_length", value=minimal_key_length, expected_type=type_hints["minimal_key_length"])
                check_type(argname="argument crypto_providers", value=crypto_providers, expected_type=type_hints["crypto_providers"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "algorithm": algorithm,
                "key_spec": key_spec,
                "key_usage_property": key_usage_property,
                "minimal_key_length": minimal_key_length,
            }
            if crypto_providers is not None:
                self._values["crypto_providers"] = crypto_providers

        @builtins.property
        def algorithm(self) -> builtins.str:
            '''Defines the algorithm used to generate the private key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv3.html#cfn-pcaconnectorad-template-privatekeyattributesv3-algorithm
            '''
            result = self._values.get("algorithm")
            assert result is not None, "Required property 'algorithm' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_spec(self) -> builtins.str:
            '''Defines the purpose of the private key.

            Set it to "KEY_EXCHANGE" or "SIGNATURE" value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv3.html#cfn-pcaconnectorad-template-privatekeyattributesv3-keyspec
            '''
            result = self._values.get("key_spec")
            assert result is not None, "Required property 'key_spec' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_usage_property(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.KeyUsagePropertyProperty"]:
            '''The key usage property defines the purpose of the private key contained in the certificate.

            You can specify specific purposes using property flags or all by using property type ALL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv3.html#cfn-pcaconnectorad-template-privatekeyattributesv3-keyusageproperty
            '''
            result = self._values.get("key_usage_property")
            assert result is not None, "Required property 'key_usage_property' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.KeyUsagePropertyProperty"], result)

        @builtins.property
        def minimal_key_length(self) -> jsii.Number:
            '''Set the minimum key length of the private key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv3.html#cfn-pcaconnectorad-template-privatekeyattributesv3-minimalkeylength
            '''
            result = self._values.get("minimal_key_length")
            assert result is not None, "Required property 'minimal_key_length' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def crypto_providers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Defines the cryptographic providers used to generate the private key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv3.html#cfn-pcaconnectorad-template-privatekeyattributesv3-cryptoproviders
            '''
            result = self._values.get("crypto_providers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PrivateKeyAttributesV3Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.PrivateKeyAttributesV4Property",
        jsii_struct_bases=[],
        name_mapping={
            "key_spec": "keySpec",
            "minimal_key_length": "minimalKeyLength",
            "algorithm": "algorithm",
            "crypto_providers": "cryptoProviders",
            "key_usage_property": "keyUsageProperty",
        },
    )
    class PrivateKeyAttributesV4Property:
        def __init__(
            self,
            *,
            key_spec: builtins.str,
            minimal_key_length: jsii.Number,
            algorithm: typing.Optional[builtins.str] = None,
            crypto_providers: typing.Optional[typing.Sequence[builtins.str]] = None,
            key_usage_property: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.KeyUsagePropertyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Defines the attributes of the private key.

            :param key_spec: Defines the purpose of the private key. Set it to "KEY_EXCHANGE" or "SIGNATURE" value.
            :param minimal_key_length: Set the minimum key length of the private key.
            :param algorithm: Defines the algorithm used to generate the private key.
            :param crypto_providers: Defines the cryptographic providers used to generate the private key.
            :param key_usage_property: The key usage property defines the purpose of the private key contained in the certificate. You can specify specific purposes using property flags or all by using property type ALL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv4.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                private_key_attributes_v4_property = pcaconnectorad.CfnTemplate.PrivateKeyAttributesV4Property(
                    key_spec="keySpec",
                    minimal_key_length=123,
                
                    # the properties below are optional
                    algorithm="algorithm",
                    crypto_providers=["cryptoProviders"],
                    key_usage_property=pcaconnectorad.CfnTemplate.KeyUsagePropertyProperty(
                        property_flags=pcaconnectorad.CfnTemplate.KeyUsagePropertyFlagsProperty(
                            decrypt=False,
                            key_agreement=False,
                            sign=False
                        ),
                        property_type="propertyType"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a7c5feb1e1b2ba9fa72d5dbc4bfa202c29886082d399af5eaef3697ca7bd3e91)
                check_type(argname="argument key_spec", value=key_spec, expected_type=type_hints["key_spec"])
                check_type(argname="argument minimal_key_length", value=minimal_key_length, expected_type=type_hints["minimal_key_length"])
                check_type(argname="argument algorithm", value=algorithm, expected_type=type_hints["algorithm"])
                check_type(argname="argument crypto_providers", value=crypto_providers, expected_type=type_hints["crypto_providers"])
                check_type(argname="argument key_usage_property", value=key_usage_property, expected_type=type_hints["key_usage_property"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key_spec": key_spec,
                "minimal_key_length": minimal_key_length,
            }
            if algorithm is not None:
                self._values["algorithm"] = algorithm
            if crypto_providers is not None:
                self._values["crypto_providers"] = crypto_providers
            if key_usage_property is not None:
                self._values["key_usage_property"] = key_usage_property

        @builtins.property
        def key_spec(self) -> builtins.str:
            '''Defines the purpose of the private key.

            Set it to "KEY_EXCHANGE" or "SIGNATURE" value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv4.html#cfn-pcaconnectorad-template-privatekeyattributesv4-keyspec
            '''
            result = self._values.get("key_spec")
            assert result is not None, "Required property 'key_spec' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def minimal_key_length(self) -> jsii.Number:
            '''Set the minimum key length of the private key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv4.html#cfn-pcaconnectorad-template-privatekeyattributesv4-minimalkeylength
            '''
            result = self._values.get("minimal_key_length")
            assert result is not None, "Required property 'minimal_key_length' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def algorithm(self) -> typing.Optional[builtins.str]:
            '''Defines the algorithm used to generate the private key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv4.html#cfn-pcaconnectorad-template-privatekeyattributesv4-algorithm
            '''
            result = self._values.get("algorithm")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def crypto_providers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Defines the cryptographic providers used to generate the private key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv4.html#cfn-pcaconnectorad-template-privatekeyattributesv4-cryptoproviders
            '''
            result = self._values.get("crypto_providers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def key_usage_property(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTemplate.KeyUsagePropertyProperty"]]:
            '''The key usage property defines the purpose of the private key contained in the certificate.

            You can specify specific purposes using property flags or all by using property type ALL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyattributesv4.html#cfn-pcaconnectorad-template-privatekeyattributesv4-keyusageproperty
            '''
            result = self._values.get("key_usage_property")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTemplate.KeyUsagePropertyProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PrivateKeyAttributesV4Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.PrivateKeyFlagsV2Property",
        jsii_struct_bases=[],
        name_mapping={
            "client_version": "clientVersion",
            "exportable_key": "exportableKey",
            "strong_key_protection_required": "strongKeyProtectionRequired",
        },
    )
    class PrivateKeyFlagsV2Property:
        def __init__(
            self,
            *,
            client_version: builtins.str,
            exportable_key: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            strong_key_protection_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Private key flags for v2 templates specify the client compatibility, if the private key can be exported, and if user input is required when using a private key.

            :param client_version: Defines the minimum client compatibility.
            :param exportable_key: Allows the private key to be exported.
            :param strong_key_protection_required: Require user input when using the private key for enrollment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv2.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                private_key_flags_v2_property = pcaconnectorad.CfnTemplate.PrivateKeyFlagsV2Property(
                    client_version="clientVersion",
                
                    # the properties below are optional
                    exportable_key=False,
                    strong_key_protection_required=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bcacc2239810164b395e4a383b95ed7bf7d6465116db368e0cc34d314e118d05)
                check_type(argname="argument client_version", value=client_version, expected_type=type_hints["client_version"])
                check_type(argname="argument exportable_key", value=exportable_key, expected_type=type_hints["exportable_key"])
                check_type(argname="argument strong_key_protection_required", value=strong_key_protection_required, expected_type=type_hints["strong_key_protection_required"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "client_version": client_version,
            }
            if exportable_key is not None:
                self._values["exportable_key"] = exportable_key
            if strong_key_protection_required is not None:
                self._values["strong_key_protection_required"] = strong_key_protection_required

        @builtins.property
        def client_version(self) -> builtins.str:
            '''Defines the minimum client compatibility.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv2.html#cfn-pcaconnectorad-template-privatekeyflagsv2-clientversion
            '''
            result = self._values.get("client_version")
            assert result is not None, "Required property 'client_version' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def exportable_key(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Allows the private key to be exported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv2.html#cfn-pcaconnectorad-template-privatekeyflagsv2-exportablekey
            '''
            result = self._values.get("exportable_key")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def strong_key_protection_required(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Require user input when using the private key for enrollment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv2.html#cfn-pcaconnectorad-template-privatekeyflagsv2-strongkeyprotectionrequired
            '''
            result = self._values.get("strong_key_protection_required")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PrivateKeyFlagsV2Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.PrivateKeyFlagsV3Property",
        jsii_struct_bases=[],
        name_mapping={
            "client_version": "clientVersion",
            "exportable_key": "exportableKey",
            "require_alternate_signature_algorithm": "requireAlternateSignatureAlgorithm",
            "strong_key_protection_required": "strongKeyProtectionRequired",
        },
    )
    class PrivateKeyFlagsV3Property:
        def __init__(
            self,
            *,
            client_version: builtins.str,
            exportable_key: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            require_alternate_signature_algorithm: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            strong_key_protection_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Private key flags for v3 templates specify the client compatibility, if the private key can be exported, if user input is required when using a private key, and if an alternate signature algorithm should be used.

            :param client_version: Defines the minimum client compatibility.
            :param exportable_key: Allows the private key to be exported.
            :param require_alternate_signature_algorithm: Reguires the PKCS #1 v2.1 signature format for certificates. You should verify that your CA, objects, and applications can accept this signature format.
            :param strong_key_protection_required: Requirer user input when using the private key for enrollment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv3.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                private_key_flags_v3_property = pcaconnectorad.CfnTemplate.PrivateKeyFlagsV3Property(
                    client_version="clientVersion",
                
                    # the properties below are optional
                    exportable_key=False,
                    require_alternate_signature_algorithm=False,
                    strong_key_protection_required=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7125a0dc03338f06174e788deefaea543edbc61c3ea00ce935559757c5f7ec9b)
                check_type(argname="argument client_version", value=client_version, expected_type=type_hints["client_version"])
                check_type(argname="argument exportable_key", value=exportable_key, expected_type=type_hints["exportable_key"])
                check_type(argname="argument require_alternate_signature_algorithm", value=require_alternate_signature_algorithm, expected_type=type_hints["require_alternate_signature_algorithm"])
                check_type(argname="argument strong_key_protection_required", value=strong_key_protection_required, expected_type=type_hints["strong_key_protection_required"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "client_version": client_version,
            }
            if exportable_key is not None:
                self._values["exportable_key"] = exportable_key
            if require_alternate_signature_algorithm is not None:
                self._values["require_alternate_signature_algorithm"] = require_alternate_signature_algorithm
            if strong_key_protection_required is not None:
                self._values["strong_key_protection_required"] = strong_key_protection_required

        @builtins.property
        def client_version(self) -> builtins.str:
            '''Defines the minimum client compatibility.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv3.html#cfn-pcaconnectorad-template-privatekeyflagsv3-clientversion
            '''
            result = self._values.get("client_version")
            assert result is not None, "Required property 'client_version' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def exportable_key(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Allows the private key to be exported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv3.html#cfn-pcaconnectorad-template-privatekeyflagsv3-exportablekey
            '''
            result = self._values.get("exportable_key")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def require_alternate_signature_algorithm(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Reguires the PKCS #1 v2.1 signature format for certificates. You should verify that your CA, objects, and applications can accept this signature format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv3.html#cfn-pcaconnectorad-template-privatekeyflagsv3-requirealternatesignaturealgorithm
            '''
            result = self._values.get("require_alternate_signature_algorithm")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def strong_key_protection_required(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Requirer user input when using the private key for enrollment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv3.html#cfn-pcaconnectorad-template-privatekeyflagsv3-strongkeyprotectionrequired
            '''
            result = self._values.get("strong_key_protection_required")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PrivateKeyFlagsV3Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.PrivateKeyFlagsV4Property",
        jsii_struct_bases=[],
        name_mapping={
            "client_version": "clientVersion",
            "exportable_key": "exportableKey",
            "require_alternate_signature_algorithm": "requireAlternateSignatureAlgorithm",
            "require_same_key_renewal": "requireSameKeyRenewal",
            "strong_key_protection_required": "strongKeyProtectionRequired",
            "use_legacy_provider": "useLegacyProvider",
        },
    )
    class PrivateKeyFlagsV4Property:
        def __init__(
            self,
            *,
            client_version: builtins.str,
            exportable_key: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            require_alternate_signature_algorithm: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            require_same_key_renewal: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            strong_key_protection_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            use_legacy_provider: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Private key flags for v4 templates specify the client compatibility, if the private key can be exported, if user input is required when using a private key, if an alternate signature algorithm should be used, and if certificates are renewed using the same private key.

            :param client_version: Defines the minimum client compatibility.
            :param exportable_key: Allows the private key to be exported.
            :param require_alternate_signature_algorithm: Requires the PKCS #1 v2.1 signature format for certificates. You should verify that your CA, objects, and applications can accept this signature format.
            :param require_same_key_renewal: Renew certificate using the same private key.
            :param strong_key_protection_required: Require user input when using the private key for enrollment.
            :param use_legacy_provider: Specifies the cryptographic service provider category used to generate private keys. Set to TRUE to use Legacy Cryptographic Service Providers and FALSE to use Key Storage Providers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv4.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                private_key_flags_v4_property = pcaconnectorad.CfnTemplate.PrivateKeyFlagsV4Property(
                    client_version="clientVersion",
                
                    # the properties below are optional
                    exportable_key=False,
                    require_alternate_signature_algorithm=False,
                    require_same_key_renewal=False,
                    strong_key_protection_required=False,
                    use_legacy_provider=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bf7957c0cde147fdfb6b22d46b1ee3896e5bd94b6bbd4c9b61f1665d8bc79956)
                check_type(argname="argument client_version", value=client_version, expected_type=type_hints["client_version"])
                check_type(argname="argument exportable_key", value=exportable_key, expected_type=type_hints["exportable_key"])
                check_type(argname="argument require_alternate_signature_algorithm", value=require_alternate_signature_algorithm, expected_type=type_hints["require_alternate_signature_algorithm"])
                check_type(argname="argument require_same_key_renewal", value=require_same_key_renewal, expected_type=type_hints["require_same_key_renewal"])
                check_type(argname="argument strong_key_protection_required", value=strong_key_protection_required, expected_type=type_hints["strong_key_protection_required"])
                check_type(argname="argument use_legacy_provider", value=use_legacy_provider, expected_type=type_hints["use_legacy_provider"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "client_version": client_version,
            }
            if exportable_key is not None:
                self._values["exportable_key"] = exportable_key
            if require_alternate_signature_algorithm is not None:
                self._values["require_alternate_signature_algorithm"] = require_alternate_signature_algorithm
            if require_same_key_renewal is not None:
                self._values["require_same_key_renewal"] = require_same_key_renewal
            if strong_key_protection_required is not None:
                self._values["strong_key_protection_required"] = strong_key_protection_required
            if use_legacy_provider is not None:
                self._values["use_legacy_provider"] = use_legacy_provider

        @builtins.property
        def client_version(self) -> builtins.str:
            '''Defines the minimum client compatibility.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv4.html#cfn-pcaconnectorad-template-privatekeyflagsv4-clientversion
            '''
            result = self._values.get("client_version")
            assert result is not None, "Required property 'client_version' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def exportable_key(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Allows the private key to be exported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv4.html#cfn-pcaconnectorad-template-privatekeyflagsv4-exportablekey
            '''
            result = self._values.get("exportable_key")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def require_alternate_signature_algorithm(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Requires the PKCS #1 v2.1 signature format for certificates. You should verify that your CA, objects, and applications can accept this signature format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv4.html#cfn-pcaconnectorad-template-privatekeyflagsv4-requirealternatesignaturealgorithm
            '''
            result = self._values.get("require_alternate_signature_algorithm")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def require_same_key_renewal(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Renew certificate using the same private key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv4.html#cfn-pcaconnectorad-template-privatekeyflagsv4-requiresamekeyrenewal
            '''
            result = self._values.get("require_same_key_renewal")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def strong_key_protection_required(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Require user input when using the private key for enrollment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv4.html#cfn-pcaconnectorad-template-privatekeyflagsv4-strongkeyprotectionrequired
            '''
            result = self._values.get("strong_key_protection_required")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def use_legacy_provider(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies the cryptographic service provider category used to generate private keys.

            Set to TRUE to use Legacy Cryptographic Service Providers and FALSE to use Key Storage Providers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-privatekeyflagsv4.html#cfn-pcaconnectorad-template-privatekeyflagsv4-uselegacyprovider
            '''
            result = self._values.get("use_legacy_provider")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PrivateKeyFlagsV4Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.SubjectNameFlagsV2Property",
        jsii_struct_bases=[],
        name_mapping={
            "require_common_name": "requireCommonName",
            "require_directory_path": "requireDirectoryPath",
            "require_dns_as_cn": "requireDnsAsCn",
            "require_email": "requireEmail",
            "san_require_directory_guid": "sanRequireDirectoryGuid",
            "san_require_dns": "sanRequireDns",
            "san_require_domain_dns": "sanRequireDomainDns",
            "san_require_email": "sanRequireEmail",
            "san_require_spn": "sanRequireSpn",
            "san_require_upn": "sanRequireUpn",
        },
    )
    class SubjectNameFlagsV2Property:
        def __init__(
            self,
            *,
            require_common_name: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            require_directory_path: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            require_dns_as_cn: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            require_email: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            san_require_directory_guid: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            san_require_dns: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            san_require_domain_dns: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            san_require_email: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            san_require_spn: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            san_require_upn: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Information to include in the subject name and alternate subject name of the certificate.

            The subject name can be common name, directory path, DNS as common name, or left blank. You can optionally include email to the subject name for user templates. If you leave the subject name blank then you must set a subject alternate name. The subject alternate name (SAN) can include globally unique identifier (GUID), DNS, domain DNS, email, service principal name (SPN), and user principal name (UPN). You can leave the SAN blank. If you leave the SAN blank, then you must set a subject name.

            :param require_common_name: Include the common name in the subject name.
            :param require_directory_path: Include the directory path in the subject name.
            :param require_dns_as_cn: Include the DNS as common name in the subject name.
            :param require_email: Include the subject's email in the subject name.
            :param san_require_directory_guid: Include the globally unique identifier (GUID) in the subject alternate name.
            :param san_require_dns: Include the DNS in the subject alternate name.
            :param san_require_domain_dns: Include the domain DNS in the subject alternate name.
            :param san_require_email: Include the subject's email in the subject alternate name.
            :param san_require_spn: Include the service principal name (SPN) in the subject alternate name.
            :param san_require_upn: Include the user principal name (UPN) in the subject alternate name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv2.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                subject_name_flags_v2_property = pcaconnectorad.CfnTemplate.SubjectNameFlagsV2Property(
                    require_common_name=False,
                    require_directory_path=False,
                    require_dns_as_cn=False,
                    require_email=False,
                    san_require_directory_guid=False,
                    san_require_dns=False,
                    san_require_domain_dns=False,
                    san_require_email=False,
                    san_require_spn=False,
                    san_require_upn=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f7e503c1f26db9d55430becc5fc9c403a6fdcca743366fdd9e02b40df1ebe9f3)
                check_type(argname="argument require_common_name", value=require_common_name, expected_type=type_hints["require_common_name"])
                check_type(argname="argument require_directory_path", value=require_directory_path, expected_type=type_hints["require_directory_path"])
                check_type(argname="argument require_dns_as_cn", value=require_dns_as_cn, expected_type=type_hints["require_dns_as_cn"])
                check_type(argname="argument require_email", value=require_email, expected_type=type_hints["require_email"])
                check_type(argname="argument san_require_directory_guid", value=san_require_directory_guid, expected_type=type_hints["san_require_directory_guid"])
                check_type(argname="argument san_require_dns", value=san_require_dns, expected_type=type_hints["san_require_dns"])
                check_type(argname="argument san_require_domain_dns", value=san_require_domain_dns, expected_type=type_hints["san_require_domain_dns"])
                check_type(argname="argument san_require_email", value=san_require_email, expected_type=type_hints["san_require_email"])
                check_type(argname="argument san_require_spn", value=san_require_spn, expected_type=type_hints["san_require_spn"])
                check_type(argname="argument san_require_upn", value=san_require_upn, expected_type=type_hints["san_require_upn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if require_common_name is not None:
                self._values["require_common_name"] = require_common_name
            if require_directory_path is not None:
                self._values["require_directory_path"] = require_directory_path
            if require_dns_as_cn is not None:
                self._values["require_dns_as_cn"] = require_dns_as_cn
            if require_email is not None:
                self._values["require_email"] = require_email
            if san_require_directory_guid is not None:
                self._values["san_require_directory_guid"] = san_require_directory_guid
            if san_require_dns is not None:
                self._values["san_require_dns"] = san_require_dns
            if san_require_domain_dns is not None:
                self._values["san_require_domain_dns"] = san_require_domain_dns
            if san_require_email is not None:
                self._values["san_require_email"] = san_require_email
            if san_require_spn is not None:
                self._values["san_require_spn"] = san_require_spn
            if san_require_upn is not None:
                self._values["san_require_upn"] = san_require_upn

        @builtins.property
        def require_common_name(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the common name in the subject name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv2.html#cfn-pcaconnectorad-template-subjectnameflagsv2-requirecommonname
            '''
            result = self._values.get("require_common_name")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def require_directory_path(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the directory path in the subject name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv2.html#cfn-pcaconnectorad-template-subjectnameflagsv2-requiredirectorypath
            '''
            result = self._values.get("require_directory_path")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def require_dns_as_cn(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the DNS as common name in the subject name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv2.html#cfn-pcaconnectorad-template-subjectnameflagsv2-requirednsascn
            '''
            result = self._values.get("require_dns_as_cn")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def require_email(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the subject's email in the subject name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv2.html#cfn-pcaconnectorad-template-subjectnameflagsv2-requireemail
            '''
            result = self._values.get("require_email")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def san_require_directory_guid(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the globally unique identifier (GUID) in the subject alternate name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv2.html#cfn-pcaconnectorad-template-subjectnameflagsv2-sanrequiredirectoryguid
            '''
            result = self._values.get("san_require_directory_guid")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def san_require_dns(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the DNS in the subject alternate name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv2.html#cfn-pcaconnectorad-template-subjectnameflagsv2-sanrequiredns
            '''
            result = self._values.get("san_require_dns")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def san_require_domain_dns(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the domain DNS in the subject alternate name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv2.html#cfn-pcaconnectorad-template-subjectnameflagsv2-sanrequiredomaindns
            '''
            result = self._values.get("san_require_domain_dns")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def san_require_email(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the subject's email in the subject alternate name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv2.html#cfn-pcaconnectorad-template-subjectnameflagsv2-sanrequireemail
            '''
            result = self._values.get("san_require_email")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def san_require_spn(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the service principal name (SPN) in the subject alternate name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv2.html#cfn-pcaconnectorad-template-subjectnameflagsv2-sanrequirespn
            '''
            result = self._values.get("san_require_spn")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def san_require_upn(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the user principal name (UPN) in the subject alternate name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv2.html#cfn-pcaconnectorad-template-subjectnameflagsv2-sanrequireupn
            '''
            result = self._values.get("san_require_upn")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubjectNameFlagsV2Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.SubjectNameFlagsV3Property",
        jsii_struct_bases=[],
        name_mapping={
            "require_common_name": "requireCommonName",
            "require_directory_path": "requireDirectoryPath",
            "require_dns_as_cn": "requireDnsAsCn",
            "require_email": "requireEmail",
            "san_require_directory_guid": "sanRequireDirectoryGuid",
            "san_require_dns": "sanRequireDns",
            "san_require_domain_dns": "sanRequireDomainDns",
            "san_require_email": "sanRequireEmail",
            "san_require_spn": "sanRequireSpn",
            "san_require_upn": "sanRequireUpn",
        },
    )
    class SubjectNameFlagsV3Property:
        def __init__(
            self,
            *,
            require_common_name: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            require_directory_path: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            require_dns_as_cn: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            require_email: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            san_require_directory_guid: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            san_require_dns: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            san_require_domain_dns: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            san_require_email: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            san_require_spn: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            san_require_upn: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Information to include in the subject name and alternate subject name of the certificate.

            The subject name can be common name, directory path, DNS as common name, or left blank. You can optionally include email to the subject name for user templates. If you leave the subject name blank then you must set a subject alternate name. The subject alternate name (SAN) can include globally unique identifier (GUID), DNS, domain DNS, email, service principal name (SPN), and user principal name (UPN). You can leave the SAN blank. If you leave the SAN blank, then you must set a subject name.

            :param require_common_name: Include the common name in the subject name.
            :param require_directory_path: Include the directory path in the subject name.
            :param require_dns_as_cn: Include the DNS as common name in the subject name.
            :param require_email: Include the subject's email in the subject name.
            :param san_require_directory_guid: Include the globally unique identifier (GUID) in the subject alternate name.
            :param san_require_dns: Include the DNS in the subject alternate name.
            :param san_require_domain_dns: Include the domain DNS in the subject alternate name.
            :param san_require_email: Include the subject's email in the subject alternate name.
            :param san_require_spn: Include the service principal name (SPN) in the subject alternate name.
            :param san_require_upn: Include the user principal name (UPN) in the subject alternate name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv3.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                subject_name_flags_v3_property = pcaconnectorad.CfnTemplate.SubjectNameFlagsV3Property(
                    require_common_name=False,
                    require_directory_path=False,
                    require_dns_as_cn=False,
                    require_email=False,
                    san_require_directory_guid=False,
                    san_require_dns=False,
                    san_require_domain_dns=False,
                    san_require_email=False,
                    san_require_spn=False,
                    san_require_upn=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6a52f3b78a4f3064dd840a4a38dc2a5628ba7b5b6a05ec68cc52e3bcb1c750ee)
                check_type(argname="argument require_common_name", value=require_common_name, expected_type=type_hints["require_common_name"])
                check_type(argname="argument require_directory_path", value=require_directory_path, expected_type=type_hints["require_directory_path"])
                check_type(argname="argument require_dns_as_cn", value=require_dns_as_cn, expected_type=type_hints["require_dns_as_cn"])
                check_type(argname="argument require_email", value=require_email, expected_type=type_hints["require_email"])
                check_type(argname="argument san_require_directory_guid", value=san_require_directory_guid, expected_type=type_hints["san_require_directory_guid"])
                check_type(argname="argument san_require_dns", value=san_require_dns, expected_type=type_hints["san_require_dns"])
                check_type(argname="argument san_require_domain_dns", value=san_require_domain_dns, expected_type=type_hints["san_require_domain_dns"])
                check_type(argname="argument san_require_email", value=san_require_email, expected_type=type_hints["san_require_email"])
                check_type(argname="argument san_require_spn", value=san_require_spn, expected_type=type_hints["san_require_spn"])
                check_type(argname="argument san_require_upn", value=san_require_upn, expected_type=type_hints["san_require_upn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if require_common_name is not None:
                self._values["require_common_name"] = require_common_name
            if require_directory_path is not None:
                self._values["require_directory_path"] = require_directory_path
            if require_dns_as_cn is not None:
                self._values["require_dns_as_cn"] = require_dns_as_cn
            if require_email is not None:
                self._values["require_email"] = require_email
            if san_require_directory_guid is not None:
                self._values["san_require_directory_guid"] = san_require_directory_guid
            if san_require_dns is not None:
                self._values["san_require_dns"] = san_require_dns
            if san_require_domain_dns is not None:
                self._values["san_require_domain_dns"] = san_require_domain_dns
            if san_require_email is not None:
                self._values["san_require_email"] = san_require_email
            if san_require_spn is not None:
                self._values["san_require_spn"] = san_require_spn
            if san_require_upn is not None:
                self._values["san_require_upn"] = san_require_upn

        @builtins.property
        def require_common_name(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the common name in the subject name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv3.html#cfn-pcaconnectorad-template-subjectnameflagsv3-requirecommonname
            '''
            result = self._values.get("require_common_name")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def require_directory_path(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the directory path in the subject name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv3.html#cfn-pcaconnectorad-template-subjectnameflagsv3-requiredirectorypath
            '''
            result = self._values.get("require_directory_path")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def require_dns_as_cn(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the DNS as common name in the subject name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv3.html#cfn-pcaconnectorad-template-subjectnameflagsv3-requirednsascn
            '''
            result = self._values.get("require_dns_as_cn")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def require_email(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the subject's email in the subject name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv3.html#cfn-pcaconnectorad-template-subjectnameflagsv3-requireemail
            '''
            result = self._values.get("require_email")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def san_require_directory_guid(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the globally unique identifier (GUID) in the subject alternate name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv3.html#cfn-pcaconnectorad-template-subjectnameflagsv3-sanrequiredirectoryguid
            '''
            result = self._values.get("san_require_directory_guid")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def san_require_dns(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the DNS in the subject alternate name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv3.html#cfn-pcaconnectorad-template-subjectnameflagsv3-sanrequiredns
            '''
            result = self._values.get("san_require_dns")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def san_require_domain_dns(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the domain DNS in the subject alternate name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv3.html#cfn-pcaconnectorad-template-subjectnameflagsv3-sanrequiredomaindns
            '''
            result = self._values.get("san_require_domain_dns")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def san_require_email(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the subject's email in the subject alternate name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv3.html#cfn-pcaconnectorad-template-subjectnameflagsv3-sanrequireemail
            '''
            result = self._values.get("san_require_email")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def san_require_spn(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the service principal name (SPN) in the subject alternate name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv3.html#cfn-pcaconnectorad-template-subjectnameflagsv3-sanrequirespn
            '''
            result = self._values.get("san_require_spn")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def san_require_upn(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the user principal name (UPN) in the subject alternate name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv3.html#cfn-pcaconnectorad-template-subjectnameflagsv3-sanrequireupn
            '''
            result = self._values.get("san_require_upn")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubjectNameFlagsV3Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.SubjectNameFlagsV4Property",
        jsii_struct_bases=[],
        name_mapping={
            "require_common_name": "requireCommonName",
            "require_directory_path": "requireDirectoryPath",
            "require_dns_as_cn": "requireDnsAsCn",
            "require_email": "requireEmail",
            "san_require_directory_guid": "sanRequireDirectoryGuid",
            "san_require_dns": "sanRequireDns",
            "san_require_domain_dns": "sanRequireDomainDns",
            "san_require_email": "sanRequireEmail",
            "san_require_spn": "sanRequireSpn",
            "san_require_upn": "sanRequireUpn",
        },
    )
    class SubjectNameFlagsV4Property:
        def __init__(
            self,
            *,
            require_common_name: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            require_directory_path: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            require_dns_as_cn: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            require_email: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            san_require_directory_guid: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            san_require_dns: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            san_require_domain_dns: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            san_require_email: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            san_require_spn: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            san_require_upn: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Information to include in the subject name and alternate subject name of the certificate.

            The subject name can be common name, directory path, DNS as common name, or left blank. You can optionally include email to the subject name for user templates. If you leave the subject name blank then you must set a subject alternate name. The subject alternate name (SAN) can include globally unique identifier (GUID), DNS, domain DNS, email, service principal name (SPN), and user principal name (UPN). You can leave the SAN blank. If you leave the SAN blank, then you must set a subject name.

            :param require_common_name: Include the common name in the subject name.
            :param require_directory_path: Include the directory path in the subject name.
            :param require_dns_as_cn: Include the DNS as common name in the subject name.
            :param require_email: Include the subject's email in the subject name.
            :param san_require_directory_guid: Include the globally unique identifier (GUID) in the subject alternate name.
            :param san_require_dns: Include the DNS in the subject alternate name.
            :param san_require_domain_dns: Include the domain DNS in the subject alternate name.
            :param san_require_email: Include the subject's email in the subject alternate name.
            :param san_require_spn: Include the service principal name (SPN) in the subject alternate name.
            :param san_require_upn: Include the user principal name (UPN) in the subject alternate name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv4.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                subject_name_flags_v4_property = pcaconnectorad.CfnTemplate.SubjectNameFlagsV4Property(
                    require_common_name=False,
                    require_directory_path=False,
                    require_dns_as_cn=False,
                    require_email=False,
                    san_require_directory_guid=False,
                    san_require_dns=False,
                    san_require_domain_dns=False,
                    san_require_email=False,
                    san_require_spn=False,
                    san_require_upn=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9e71f41f55a91f74da966fd2db125279f9d27eaa16bcb61171df96219e48b1c7)
                check_type(argname="argument require_common_name", value=require_common_name, expected_type=type_hints["require_common_name"])
                check_type(argname="argument require_directory_path", value=require_directory_path, expected_type=type_hints["require_directory_path"])
                check_type(argname="argument require_dns_as_cn", value=require_dns_as_cn, expected_type=type_hints["require_dns_as_cn"])
                check_type(argname="argument require_email", value=require_email, expected_type=type_hints["require_email"])
                check_type(argname="argument san_require_directory_guid", value=san_require_directory_guid, expected_type=type_hints["san_require_directory_guid"])
                check_type(argname="argument san_require_dns", value=san_require_dns, expected_type=type_hints["san_require_dns"])
                check_type(argname="argument san_require_domain_dns", value=san_require_domain_dns, expected_type=type_hints["san_require_domain_dns"])
                check_type(argname="argument san_require_email", value=san_require_email, expected_type=type_hints["san_require_email"])
                check_type(argname="argument san_require_spn", value=san_require_spn, expected_type=type_hints["san_require_spn"])
                check_type(argname="argument san_require_upn", value=san_require_upn, expected_type=type_hints["san_require_upn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if require_common_name is not None:
                self._values["require_common_name"] = require_common_name
            if require_directory_path is not None:
                self._values["require_directory_path"] = require_directory_path
            if require_dns_as_cn is not None:
                self._values["require_dns_as_cn"] = require_dns_as_cn
            if require_email is not None:
                self._values["require_email"] = require_email
            if san_require_directory_guid is not None:
                self._values["san_require_directory_guid"] = san_require_directory_guid
            if san_require_dns is not None:
                self._values["san_require_dns"] = san_require_dns
            if san_require_domain_dns is not None:
                self._values["san_require_domain_dns"] = san_require_domain_dns
            if san_require_email is not None:
                self._values["san_require_email"] = san_require_email
            if san_require_spn is not None:
                self._values["san_require_spn"] = san_require_spn
            if san_require_upn is not None:
                self._values["san_require_upn"] = san_require_upn

        @builtins.property
        def require_common_name(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the common name in the subject name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv4.html#cfn-pcaconnectorad-template-subjectnameflagsv4-requirecommonname
            '''
            result = self._values.get("require_common_name")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def require_directory_path(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the directory path in the subject name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv4.html#cfn-pcaconnectorad-template-subjectnameflagsv4-requiredirectorypath
            '''
            result = self._values.get("require_directory_path")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def require_dns_as_cn(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the DNS as common name in the subject name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv4.html#cfn-pcaconnectorad-template-subjectnameflagsv4-requirednsascn
            '''
            result = self._values.get("require_dns_as_cn")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def require_email(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the subject's email in the subject name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv4.html#cfn-pcaconnectorad-template-subjectnameflagsv4-requireemail
            '''
            result = self._values.get("require_email")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def san_require_directory_guid(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the globally unique identifier (GUID) in the subject alternate name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv4.html#cfn-pcaconnectorad-template-subjectnameflagsv4-sanrequiredirectoryguid
            '''
            result = self._values.get("san_require_directory_guid")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def san_require_dns(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the DNS in the subject alternate name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv4.html#cfn-pcaconnectorad-template-subjectnameflagsv4-sanrequiredns
            '''
            result = self._values.get("san_require_dns")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def san_require_domain_dns(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the domain DNS in the subject alternate name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv4.html#cfn-pcaconnectorad-template-subjectnameflagsv4-sanrequiredomaindns
            '''
            result = self._values.get("san_require_domain_dns")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def san_require_email(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the subject's email in the subject alternate name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv4.html#cfn-pcaconnectorad-template-subjectnameflagsv4-sanrequireemail
            '''
            result = self._values.get("san_require_email")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def san_require_spn(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the service principal name (SPN) in the subject alternate name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv4.html#cfn-pcaconnectorad-template-subjectnameflagsv4-sanrequirespn
            '''
            result = self._values.get("san_require_spn")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def san_require_upn(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include the user principal name (UPN) in the subject alternate name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-subjectnameflagsv4.html#cfn-pcaconnectorad-template-subjectnameflagsv4-sanrequireupn
            '''
            result = self._values.get("san_require_upn")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubjectNameFlagsV4Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.TemplateDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "template_v2": "templateV2",
            "template_v3": "templateV3",
            "template_v4": "templateV4",
        },
    )
    class TemplateDefinitionProperty:
        def __init__(
            self,
            *,
            template_v2: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.TemplateV2Property", typing.Dict[builtins.str, typing.Any]]]] = None,
            template_v3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.TemplateV3Property", typing.Dict[builtins.str, typing.Any]]]] = None,
            template_v4: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.TemplateV4Property", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Template configuration to define the information included in certificates.

            Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.

            :param template_v2: Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.
            :param template_v3: Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.
            :param template_v4: Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatedefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                template_definition_property = pcaconnectorad.CfnTemplate.TemplateDefinitionProperty(
                    template_v2=pcaconnectorad.CfnTemplate.TemplateV2Property(
                        certificate_validity=pcaconnectorad.CfnTemplate.CertificateValidityProperty(
                            renewal_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                                period=123,
                                period_type="periodType"
                            ),
                            validity_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                                period=123,
                                period_type="periodType"
                            )
                        ),
                        enrollment_flags=pcaconnectorad.CfnTemplate.EnrollmentFlagsV2Property(
                            enable_key_reuse_on_nt_token_keyset_storage_full=False,
                            include_symmetric_algorithms=False,
                            no_security_extension=False,
                            remove_invalid_certificate_from_personal_store=False,
                            user_interaction_required=False
                        ),
                        extensions=pcaconnectorad.CfnTemplate.ExtensionsV2Property(
                            key_usage=pcaconnectorad.CfnTemplate.KeyUsageProperty(
                                usage_flags=pcaconnectorad.CfnTemplate.KeyUsageFlagsProperty(
                                    data_encipherment=False,
                                    digital_signature=False,
                                    key_agreement=False,
                                    key_encipherment=False,
                                    non_repudiation=False
                                ),
                
                                # the properties below are optional
                                critical=False
                            ),
                
                            # the properties below are optional
                            application_policies=pcaconnectorad.CfnTemplate.ApplicationPoliciesProperty(
                                policies=[pcaconnectorad.CfnTemplate.ApplicationPolicyProperty(
                                    policy_object_identifier="policyObjectIdentifier",
                                    policy_type="policyType"
                                )],
                
                                # the properties below are optional
                                critical=False
                            )
                        ),
                        general_flags=pcaconnectorad.CfnTemplate.GeneralFlagsV2Property(
                            auto_enrollment=False,
                            machine_type=False
                        ),
                        private_key_attributes=pcaconnectorad.CfnTemplate.PrivateKeyAttributesV2Property(
                            key_spec="keySpec",
                            minimal_key_length=123,
                
                            # the properties below are optional
                            crypto_providers=["cryptoProviders"]
                        ),
                        private_key_flags=pcaconnectorad.CfnTemplate.PrivateKeyFlagsV2Property(
                            client_version="clientVersion",
                
                            # the properties below are optional
                            exportable_key=False,
                            strong_key_protection_required=False
                        ),
                        subject_name_flags=pcaconnectorad.CfnTemplate.SubjectNameFlagsV2Property(
                            require_common_name=False,
                            require_directory_path=False,
                            require_dns_as_cn=False,
                            require_email=False,
                            san_require_directory_guid=False,
                            san_require_dns=False,
                            san_require_domain_dns=False,
                            san_require_email=False,
                            san_require_spn=False,
                            san_require_upn=False
                        ),
                
                        # the properties below are optional
                        superseded_templates=["supersededTemplates"]
                    ),
                    template_v3=pcaconnectorad.CfnTemplate.TemplateV3Property(
                        certificate_validity=pcaconnectorad.CfnTemplate.CertificateValidityProperty(
                            renewal_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                                period=123,
                                period_type="periodType"
                            ),
                            validity_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                                period=123,
                                period_type="periodType"
                            )
                        ),
                        enrollment_flags=pcaconnectorad.CfnTemplate.EnrollmentFlagsV3Property(
                            enable_key_reuse_on_nt_token_keyset_storage_full=False,
                            include_symmetric_algorithms=False,
                            no_security_extension=False,
                            remove_invalid_certificate_from_personal_store=False,
                            user_interaction_required=False
                        ),
                        extensions=pcaconnectorad.CfnTemplate.ExtensionsV3Property(
                            key_usage=pcaconnectorad.CfnTemplate.KeyUsageProperty(
                                usage_flags=pcaconnectorad.CfnTemplate.KeyUsageFlagsProperty(
                                    data_encipherment=False,
                                    digital_signature=False,
                                    key_agreement=False,
                                    key_encipherment=False,
                                    non_repudiation=False
                                ),
                
                                # the properties below are optional
                                critical=False
                            ),
                
                            # the properties below are optional
                            application_policies=pcaconnectorad.CfnTemplate.ApplicationPoliciesProperty(
                                policies=[pcaconnectorad.CfnTemplate.ApplicationPolicyProperty(
                                    policy_object_identifier="policyObjectIdentifier",
                                    policy_type="policyType"
                                )],
                
                                # the properties below are optional
                                critical=False
                            )
                        ),
                        general_flags=pcaconnectorad.CfnTemplate.GeneralFlagsV3Property(
                            auto_enrollment=False,
                            machine_type=False
                        ),
                        hash_algorithm="hashAlgorithm",
                        private_key_attributes=pcaconnectorad.CfnTemplate.PrivateKeyAttributesV3Property(
                            algorithm="algorithm",
                            key_spec="keySpec",
                            key_usage_property=pcaconnectorad.CfnTemplate.KeyUsagePropertyProperty(
                                property_flags=pcaconnectorad.CfnTemplate.KeyUsagePropertyFlagsProperty(
                                    decrypt=False,
                                    key_agreement=False,
                                    sign=False
                                ),
                                property_type="propertyType"
                            ),
                            minimal_key_length=123,
                
                            # the properties below are optional
                            crypto_providers=["cryptoProviders"]
                        ),
                        private_key_flags=pcaconnectorad.CfnTemplate.PrivateKeyFlagsV3Property(
                            client_version="clientVersion",
                
                            # the properties below are optional
                            exportable_key=False,
                            require_alternate_signature_algorithm=False,
                            strong_key_protection_required=False
                        ),
                        subject_name_flags=pcaconnectorad.CfnTemplate.SubjectNameFlagsV3Property(
                            require_common_name=False,
                            require_directory_path=False,
                            require_dns_as_cn=False,
                            require_email=False,
                            san_require_directory_guid=False,
                            san_require_dns=False,
                            san_require_domain_dns=False,
                            san_require_email=False,
                            san_require_spn=False,
                            san_require_upn=False
                        ),
                
                        # the properties below are optional
                        superseded_templates=["supersededTemplates"]
                    ),
                    template_v4=pcaconnectorad.CfnTemplate.TemplateV4Property(
                        certificate_validity=pcaconnectorad.CfnTemplate.CertificateValidityProperty(
                            renewal_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                                period=123,
                                period_type="periodType"
                            ),
                            validity_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                                period=123,
                                period_type="periodType"
                            )
                        ),
                        enrollment_flags=pcaconnectorad.CfnTemplate.EnrollmentFlagsV4Property(
                            enable_key_reuse_on_nt_token_keyset_storage_full=False,
                            include_symmetric_algorithms=False,
                            no_security_extension=False,
                            remove_invalid_certificate_from_personal_store=False,
                            user_interaction_required=False
                        ),
                        extensions=pcaconnectorad.CfnTemplate.ExtensionsV4Property(
                            key_usage=pcaconnectorad.CfnTemplate.KeyUsageProperty(
                                usage_flags=pcaconnectorad.CfnTemplate.KeyUsageFlagsProperty(
                                    data_encipherment=False,
                                    digital_signature=False,
                                    key_agreement=False,
                                    key_encipherment=False,
                                    non_repudiation=False
                                ),
                
                                # the properties below are optional
                                critical=False
                            ),
                
                            # the properties below are optional
                            application_policies=pcaconnectorad.CfnTemplate.ApplicationPoliciesProperty(
                                policies=[pcaconnectorad.CfnTemplate.ApplicationPolicyProperty(
                                    policy_object_identifier="policyObjectIdentifier",
                                    policy_type="policyType"
                                )],
                
                                # the properties below are optional
                                critical=False
                            )
                        ),
                        general_flags=pcaconnectorad.CfnTemplate.GeneralFlagsV4Property(
                            auto_enrollment=False,
                            machine_type=False
                        ),
                        private_key_attributes=pcaconnectorad.CfnTemplate.PrivateKeyAttributesV4Property(
                            key_spec="keySpec",
                            minimal_key_length=123,
                
                            # the properties below are optional
                            algorithm="algorithm",
                            crypto_providers=["cryptoProviders"],
                            key_usage_property=pcaconnectorad.CfnTemplate.KeyUsagePropertyProperty(
                                property_flags=pcaconnectorad.CfnTemplate.KeyUsagePropertyFlagsProperty(
                                    decrypt=False,
                                    key_agreement=False,
                                    sign=False
                                ),
                                property_type="propertyType"
                            )
                        ),
                        private_key_flags=pcaconnectorad.CfnTemplate.PrivateKeyFlagsV4Property(
                            client_version="clientVersion",
                
                            # the properties below are optional
                            exportable_key=False,
                            require_alternate_signature_algorithm=False,
                            require_same_key_renewal=False,
                            strong_key_protection_required=False,
                            use_legacy_provider=False
                        ),
                        subject_name_flags=pcaconnectorad.CfnTemplate.SubjectNameFlagsV4Property(
                            require_common_name=False,
                            require_directory_path=False,
                            require_dns_as_cn=False,
                            require_email=False,
                            san_require_directory_guid=False,
                            san_require_dns=False,
                            san_require_domain_dns=False,
                            san_require_email=False,
                            san_require_spn=False,
                            san_require_upn=False
                        ),
                
                        # the properties below are optional
                        hash_algorithm="hashAlgorithm",
                        superseded_templates=["supersededTemplates"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__64b80ea351fed33fc54e6692c72597ccfcccd5060a63508183b4f41674d9fc0c)
                check_type(argname="argument template_v2", value=template_v2, expected_type=type_hints["template_v2"])
                check_type(argname="argument template_v3", value=template_v3, expected_type=type_hints["template_v3"])
                check_type(argname="argument template_v4", value=template_v4, expected_type=type_hints["template_v4"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if template_v2 is not None:
                self._values["template_v2"] = template_v2
            if template_v3 is not None:
                self._values["template_v3"] = template_v3
            if template_v4 is not None:
                self._values["template_v4"] = template_v4

        @builtins.property
        def template_v2(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTemplate.TemplateV2Property"]]:
            '''Template configuration to define the information included in certificates.

            Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatedefinition.html#cfn-pcaconnectorad-template-templatedefinition-templatev2
            '''
            result = self._values.get("template_v2")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTemplate.TemplateV2Property"]], result)

        @builtins.property
        def template_v3(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTemplate.TemplateV3Property"]]:
            '''Template configuration to define the information included in certificates.

            Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatedefinition.html#cfn-pcaconnectorad-template-templatedefinition-templatev3
            '''
            result = self._values.get("template_v3")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTemplate.TemplateV3Property"]], result)

        @builtins.property
        def template_v4(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTemplate.TemplateV4Property"]]:
            '''Template configuration to define the information included in certificates.

            Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatedefinition.html#cfn-pcaconnectorad-template-templatedefinition-templatev4
            '''
            result = self._values.get("template_v4")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTemplate.TemplateV4Property"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TemplateDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.TemplateV2Property",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_validity": "certificateValidity",
            "enrollment_flags": "enrollmentFlags",
            "extensions": "extensions",
            "general_flags": "generalFlags",
            "private_key_attributes": "privateKeyAttributes",
            "private_key_flags": "privateKeyFlags",
            "subject_name_flags": "subjectNameFlags",
            "superseded_templates": "supersededTemplates",
        },
    )
    class TemplateV2Property:
        def __init__(
            self,
            *,
            certificate_validity: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.CertificateValidityProperty", typing.Dict[builtins.str, typing.Any]]],
            enrollment_flags: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.EnrollmentFlagsV2Property", typing.Dict[builtins.str, typing.Any]]],
            extensions: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.ExtensionsV2Property", typing.Dict[builtins.str, typing.Any]]],
            general_flags: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.GeneralFlagsV2Property", typing.Dict[builtins.str, typing.Any]]],
            private_key_attributes: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.PrivateKeyAttributesV2Property", typing.Dict[builtins.str, typing.Any]]],
            private_key_flags: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.PrivateKeyFlagsV2Property", typing.Dict[builtins.str, typing.Any]]],
            subject_name_flags: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.SubjectNameFlagsV2Property", typing.Dict[builtins.str, typing.Any]]],
            superseded_templates: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''v2 template schema that uses Legacy Cryptographic Providers.

            :param certificate_validity: Certificate validity describes the validity and renewal periods of a certificate.
            :param enrollment_flags: Enrollment flags describe the enrollment settings for certificates such as using the existing private key and deleting expired or revoked certificates.
            :param extensions: Extensions describe the key usage extensions and application policies for a template.
            :param general_flags: General flags describe whether the template is used for computers or users and if the template can be used with autoenrollment.
            :param private_key_attributes: Private key attributes allow you to specify the minimal key length, key spec, and cryptographic providers for the private key of a certificate for v2 templates. V2 templates allow you to use Legacy Cryptographic Service Providers.
            :param private_key_flags: Private key flags for v2 templates specify the client compatibility, if the private key can be exported, and if user input is required when using a private key.
            :param subject_name_flags: Subject name flags describe the subject name and subject alternate name that is included in a certificate.
            :param superseded_templates: List of templates in Active Directory that are superseded by this template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev2.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                template_v2_property = pcaconnectorad.CfnTemplate.TemplateV2Property(
                    certificate_validity=pcaconnectorad.CfnTemplate.CertificateValidityProperty(
                        renewal_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                            period=123,
                            period_type="periodType"
                        ),
                        validity_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                            period=123,
                            period_type="periodType"
                        )
                    ),
                    enrollment_flags=pcaconnectorad.CfnTemplate.EnrollmentFlagsV2Property(
                        enable_key_reuse_on_nt_token_keyset_storage_full=False,
                        include_symmetric_algorithms=False,
                        no_security_extension=False,
                        remove_invalid_certificate_from_personal_store=False,
                        user_interaction_required=False
                    ),
                    extensions=pcaconnectorad.CfnTemplate.ExtensionsV2Property(
                        key_usage=pcaconnectorad.CfnTemplate.KeyUsageProperty(
                            usage_flags=pcaconnectorad.CfnTemplate.KeyUsageFlagsProperty(
                                data_encipherment=False,
                                digital_signature=False,
                                key_agreement=False,
                                key_encipherment=False,
                                non_repudiation=False
                            ),
                
                            # the properties below are optional
                            critical=False
                        ),
                
                        # the properties below are optional
                        application_policies=pcaconnectorad.CfnTemplate.ApplicationPoliciesProperty(
                            policies=[pcaconnectorad.CfnTemplate.ApplicationPolicyProperty(
                                policy_object_identifier="policyObjectIdentifier",
                                policy_type="policyType"
                            )],
                
                            # the properties below are optional
                            critical=False
                        )
                    ),
                    general_flags=pcaconnectorad.CfnTemplate.GeneralFlagsV2Property(
                        auto_enrollment=False,
                        machine_type=False
                    ),
                    private_key_attributes=pcaconnectorad.CfnTemplate.PrivateKeyAttributesV2Property(
                        key_spec="keySpec",
                        minimal_key_length=123,
                
                        # the properties below are optional
                        crypto_providers=["cryptoProviders"]
                    ),
                    private_key_flags=pcaconnectorad.CfnTemplate.PrivateKeyFlagsV2Property(
                        client_version="clientVersion",
                
                        # the properties below are optional
                        exportable_key=False,
                        strong_key_protection_required=False
                    ),
                    subject_name_flags=pcaconnectorad.CfnTemplate.SubjectNameFlagsV2Property(
                        require_common_name=False,
                        require_directory_path=False,
                        require_dns_as_cn=False,
                        require_email=False,
                        san_require_directory_guid=False,
                        san_require_dns=False,
                        san_require_domain_dns=False,
                        san_require_email=False,
                        san_require_spn=False,
                        san_require_upn=False
                    ),
                
                    # the properties below are optional
                    superseded_templates=["supersededTemplates"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__151fc4337a303972048fa1af002c8cdbcb6d2ff15c97afedf760ae127b7f5bfc)
                check_type(argname="argument certificate_validity", value=certificate_validity, expected_type=type_hints["certificate_validity"])
                check_type(argname="argument enrollment_flags", value=enrollment_flags, expected_type=type_hints["enrollment_flags"])
                check_type(argname="argument extensions", value=extensions, expected_type=type_hints["extensions"])
                check_type(argname="argument general_flags", value=general_flags, expected_type=type_hints["general_flags"])
                check_type(argname="argument private_key_attributes", value=private_key_attributes, expected_type=type_hints["private_key_attributes"])
                check_type(argname="argument private_key_flags", value=private_key_flags, expected_type=type_hints["private_key_flags"])
                check_type(argname="argument subject_name_flags", value=subject_name_flags, expected_type=type_hints["subject_name_flags"])
                check_type(argname="argument superseded_templates", value=superseded_templates, expected_type=type_hints["superseded_templates"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "certificate_validity": certificate_validity,
                "enrollment_flags": enrollment_flags,
                "extensions": extensions,
                "general_flags": general_flags,
                "private_key_attributes": private_key_attributes,
                "private_key_flags": private_key_flags,
                "subject_name_flags": subject_name_flags,
            }
            if superseded_templates is not None:
                self._values["superseded_templates"] = superseded_templates

        @builtins.property
        def certificate_validity(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.CertificateValidityProperty"]:
            '''Certificate validity describes the validity and renewal periods of a certificate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev2.html#cfn-pcaconnectorad-template-templatev2-certificatevalidity
            '''
            result = self._values.get("certificate_validity")
            assert result is not None, "Required property 'certificate_validity' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.CertificateValidityProperty"], result)

        @builtins.property
        def enrollment_flags(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.EnrollmentFlagsV2Property"]:
            '''Enrollment flags describe the enrollment settings for certificates such as using the existing private key and deleting expired or revoked certificates.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev2.html#cfn-pcaconnectorad-template-templatev2-enrollmentflags
            '''
            result = self._values.get("enrollment_flags")
            assert result is not None, "Required property 'enrollment_flags' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.EnrollmentFlagsV2Property"], result)

        @builtins.property
        def extensions(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.ExtensionsV2Property"]:
            '''Extensions describe the key usage extensions and application policies for a template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev2.html#cfn-pcaconnectorad-template-templatev2-extensions
            '''
            result = self._values.get("extensions")
            assert result is not None, "Required property 'extensions' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.ExtensionsV2Property"], result)

        @builtins.property
        def general_flags(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.GeneralFlagsV2Property"]:
            '''General flags describe whether the template is used for computers or users and if the template can be used with autoenrollment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev2.html#cfn-pcaconnectorad-template-templatev2-generalflags
            '''
            result = self._values.get("general_flags")
            assert result is not None, "Required property 'general_flags' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.GeneralFlagsV2Property"], result)

        @builtins.property
        def private_key_attributes(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.PrivateKeyAttributesV2Property"]:
            '''Private key attributes allow you to specify the minimal key length, key spec, and cryptographic providers for the private key of a certificate for v2 templates.

            V2 templates allow you to use Legacy Cryptographic Service Providers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev2.html#cfn-pcaconnectorad-template-templatev2-privatekeyattributes
            '''
            result = self._values.get("private_key_attributes")
            assert result is not None, "Required property 'private_key_attributes' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.PrivateKeyAttributesV2Property"], result)

        @builtins.property
        def private_key_flags(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.PrivateKeyFlagsV2Property"]:
            '''Private key flags for v2 templates specify the client compatibility, if the private key can be exported, and if user input is required when using a private key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev2.html#cfn-pcaconnectorad-template-templatev2-privatekeyflags
            '''
            result = self._values.get("private_key_flags")
            assert result is not None, "Required property 'private_key_flags' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.PrivateKeyFlagsV2Property"], result)

        @builtins.property
        def subject_name_flags(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.SubjectNameFlagsV2Property"]:
            '''Subject name flags describe the subject name and subject alternate name that is included in a certificate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev2.html#cfn-pcaconnectorad-template-templatev2-subjectnameflags
            '''
            result = self._values.get("subject_name_flags")
            assert result is not None, "Required property 'subject_name_flags' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.SubjectNameFlagsV2Property"], result)

        @builtins.property
        def superseded_templates(self) -> typing.Optional[typing.List[builtins.str]]:
            '''List of templates in Active Directory that are superseded by this template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev2.html#cfn-pcaconnectorad-template-templatev2-supersededtemplates
            '''
            result = self._values.get("superseded_templates")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TemplateV2Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.TemplateV3Property",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_validity": "certificateValidity",
            "enrollment_flags": "enrollmentFlags",
            "extensions": "extensions",
            "general_flags": "generalFlags",
            "hash_algorithm": "hashAlgorithm",
            "private_key_attributes": "privateKeyAttributes",
            "private_key_flags": "privateKeyFlags",
            "subject_name_flags": "subjectNameFlags",
            "superseded_templates": "supersededTemplates",
        },
    )
    class TemplateV3Property:
        def __init__(
            self,
            *,
            certificate_validity: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.CertificateValidityProperty", typing.Dict[builtins.str, typing.Any]]],
            enrollment_flags: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.EnrollmentFlagsV3Property", typing.Dict[builtins.str, typing.Any]]],
            extensions: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.ExtensionsV3Property", typing.Dict[builtins.str, typing.Any]]],
            general_flags: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.GeneralFlagsV3Property", typing.Dict[builtins.str, typing.Any]]],
            hash_algorithm: builtins.str,
            private_key_attributes: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.PrivateKeyAttributesV3Property", typing.Dict[builtins.str, typing.Any]]],
            private_key_flags: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.PrivateKeyFlagsV3Property", typing.Dict[builtins.str, typing.Any]]],
            subject_name_flags: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.SubjectNameFlagsV3Property", typing.Dict[builtins.str, typing.Any]]],
            superseded_templates: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''v3 template schema that uses Key Storage Providers.

            :param certificate_validity: Certificate validity describes the validity and renewal periods of a certificate.
            :param enrollment_flags: Enrollment flags describe the enrollment settings for certificates such as using the existing private key and deleting expired or revoked certificates.
            :param extensions: Extensions describe the key usage extensions and application policies for a template.
            :param general_flags: General flags describe whether the template is used for computers or users and if the template can be used with autoenrollment.
            :param hash_algorithm: Specifies the hash algorithm used to hash the private key.
            :param private_key_attributes: Private key attributes allow you to specify the algorithm, minimal key length, key spec, key usage, and cryptographic providers for the private key of a certificate for v3 templates. V3 templates allow you to use Key Storage Providers.
            :param private_key_flags: Private key flags for v3 templates specify the client compatibility, if the private key can be exported, if user input is required when using a private key, and if an alternate signature algorithm should be used.
            :param subject_name_flags: Subject name flags describe the subject name and subject alternate name that is included in a certificate.
            :param superseded_templates: List of templates in Active Directory that are superseded by this template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev3.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                template_v3_property = pcaconnectorad.CfnTemplate.TemplateV3Property(
                    certificate_validity=pcaconnectorad.CfnTemplate.CertificateValidityProperty(
                        renewal_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                            period=123,
                            period_type="periodType"
                        ),
                        validity_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                            period=123,
                            period_type="periodType"
                        )
                    ),
                    enrollment_flags=pcaconnectorad.CfnTemplate.EnrollmentFlagsV3Property(
                        enable_key_reuse_on_nt_token_keyset_storage_full=False,
                        include_symmetric_algorithms=False,
                        no_security_extension=False,
                        remove_invalid_certificate_from_personal_store=False,
                        user_interaction_required=False
                    ),
                    extensions=pcaconnectorad.CfnTemplate.ExtensionsV3Property(
                        key_usage=pcaconnectorad.CfnTemplate.KeyUsageProperty(
                            usage_flags=pcaconnectorad.CfnTemplate.KeyUsageFlagsProperty(
                                data_encipherment=False,
                                digital_signature=False,
                                key_agreement=False,
                                key_encipherment=False,
                                non_repudiation=False
                            ),
                
                            # the properties below are optional
                            critical=False
                        ),
                
                        # the properties below are optional
                        application_policies=pcaconnectorad.CfnTemplate.ApplicationPoliciesProperty(
                            policies=[pcaconnectorad.CfnTemplate.ApplicationPolicyProperty(
                                policy_object_identifier="policyObjectIdentifier",
                                policy_type="policyType"
                            )],
                
                            # the properties below are optional
                            critical=False
                        )
                    ),
                    general_flags=pcaconnectorad.CfnTemplate.GeneralFlagsV3Property(
                        auto_enrollment=False,
                        machine_type=False
                    ),
                    hash_algorithm="hashAlgorithm",
                    private_key_attributes=pcaconnectorad.CfnTemplate.PrivateKeyAttributesV3Property(
                        algorithm="algorithm",
                        key_spec="keySpec",
                        key_usage_property=pcaconnectorad.CfnTemplate.KeyUsagePropertyProperty(
                            property_flags=pcaconnectorad.CfnTemplate.KeyUsagePropertyFlagsProperty(
                                decrypt=False,
                                key_agreement=False,
                                sign=False
                            ),
                            property_type="propertyType"
                        ),
                        minimal_key_length=123,
                
                        # the properties below are optional
                        crypto_providers=["cryptoProviders"]
                    ),
                    private_key_flags=pcaconnectorad.CfnTemplate.PrivateKeyFlagsV3Property(
                        client_version="clientVersion",
                
                        # the properties below are optional
                        exportable_key=False,
                        require_alternate_signature_algorithm=False,
                        strong_key_protection_required=False
                    ),
                    subject_name_flags=pcaconnectorad.CfnTemplate.SubjectNameFlagsV3Property(
                        require_common_name=False,
                        require_directory_path=False,
                        require_dns_as_cn=False,
                        require_email=False,
                        san_require_directory_guid=False,
                        san_require_dns=False,
                        san_require_domain_dns=False,
                        san_require_email=False,
                        san_require_spn=False,
                        san_require_upn=False
                    ),
                
                    # the properties below are optional
                    superseded_templates=["supersededTemplates"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ac224c6e1a1e0bf613c6d1fe4773237be6044141e87435ae036c086e9bec9e33)
                check_type(argname="argument certificate_validity", value=certificate_validity, expected_type=type_hints["certificate_validity"])
                check_type(argname="argument enrollment_flags", value=enrollment_flags, expected_type=type_hints["enrollment_flags"])
                check_type(argname="argument extensions", value=extensions, expected_type=type_hints["extensions"])
                check_type(argname="argument general_flags", value=general_flags, expected_type=type_hints["general_flags"])
                check_type(argname="argument hash_algorithm", value=hash_algorithm, expected_type=type_hints["hash_algorithm"])
                check_type(argname="argument private_key_attributes", value=private_key_attributes, expected_type=type_hints["private_key_attributes"])
                check_type(argname="argument private_key_flags", value=private_key_flags, expected_type=type_hints["private_key_flags"])
                check_type(argname="argument subject_name_flags", value=subject_name_flags, expected_type=type_hints["subject_name_flags"])
                check_type(argname="argument superseded_templates", value=superseded_templates, expected_type=type_hints["superseded_templates"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "certificate_validity": certificate_validity,
                "enrollment_flags": enrollment_flags,
                "extensions": extensions,
                "general_flags": general_flags,
                "hash_algorithm": hash_algorithm,
                "private_key_attributes": private_key_attributes,
                "private_key_flags": private_key_flags,
                "subject_name_flags": subject_name_flags,
            }
            if superseded_templates is not None:
                self._values["superseded_templates"] = superseded_templates

        @builtins.property
        def certificate_validity(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.CertificateValidityProperty"]:
            '''Certificate validity describes the validity and renewal periods of a certificate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev3.html#cfn-pcaconnectorad-template-templatev3-certificatevalidity
            '''
            result = self._values.get("certificate_validity")
            assert result is not None, "Required property 'certificate_validity' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.CertificateValidityProperty"], result)

        @builtins.property
        def enrollment_flags(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.EnrollmentFlagsV3Property"]:
            '''Enrollment flags describe the enrollment settings for certificates such as using the existing private key and deleting expired or revoked certificates.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev3.html#cfn-pcaconnectorad-template-templatev3-enrollmentflags
            '''
            result = self._values.get("enrollment_flags")
            assert result is not None, "Required property 'enrollment_flags' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.EnrollmentFlagsV3Property"], result)

        @builtins.property
        def extensions(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.ExtensionsV3Property"]:
            '''Extensions describe the key usage extensions and application policies for a template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev3.html#cfn-pcaconnectorad-template-templatev3-extensions
            '''
            result = self._values.get("extensions")
            assert result is not None, "Required property 'extensions' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.ExtensionsV3Property"], result)

        @builtins.property
        def general_flags(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.GeneralFlagsV3Property"]:
            '''General flags describe whether the template is used for computers or users and if the template can be used with autoenrollment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev3.html#cfn-pcaconnectorad-template-templatev3-generalflags
            '''
            result = self._values.get("general_flags")
            assert result is not None, "Required property 'general_flags' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.GeneralFlagsV3Property"], result)

        @builtins.property
        def hash_algorithm(self) -> builtins.str:
            '''Specifies the hash algorithm used to hash the private key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev3.html#cfn-pcaconnectorad-template-templatev3-hashalgorithm
            '''
            result = self._values.get("hash_algorithm")
            assert result is not None, "Required property 'hash_algorithm' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def private_key_attributes(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.PrivateKeyAttributesV3Property"]:
            '''Private key attributes allow you to specify the algorithm, minimal key length, key spec, key usage, and cryptographic providers for the private key of a certificate for v3 templates.

            V3 templates allow you to use Key Storage Providers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev3.html#cfn-pcaconnectorad-template-templatev3-privatekeyattributes
            '''
            result = self._values.get("private_key_attributes")
            assert result is not None, "Required property 'private_key_attributes' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.PrivateKeyAttributesV3Property"], result)

        @builtins.property
        def private_key_flags(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.PrivateKeyFlagsV3Property"]:
            '''Private key flags for v3 templates specify the client compatibility, if the private key can be exported, if user input is required when using a private key, and if an alternate signature algorithm should be used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev3.html#cfn-pcaconnectorad-template-templatev3-privatekeyflags
            '''
            result = self._values.get("private_key_flags")
            assert result is not None, "Required property 'private_key_flags' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.PrivateKeyFlagsV3Property"], result)

        @builtins.property
        def subject_name_flags(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.SubjectNameFlagsV3Property"]:
            '''Subject name flags describe the subject name and subject alternate name that is included in a certificate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev3.html#cfn-pcaconnectorad-template-templatev3-subjectnameflags
            '''
            result = self._values.get("subject_name_flags")
            assert result is not None, "Required property 'subject_name_flags' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.SubjectNameFlagsV3Property"], result)

        @builtins.property
        def superseded_templates(self) -> typing.Optional[typing.List[builtins.str]]:
            '''List of templates in Active Directory that are superseded by this template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev3.html#cfn-pcaconnectorad-template-templatev3-supersededtemplates
            '''
            result = self._values.get("superseded_templates")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TemplateV3Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.TemplateV4Property",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_validity": "certificateValidity",
            "enrollment_flags": "enrollmentFlags",
            "extensions": "extensions",
            "general_flags": "generalFlags",
            "private_key_attributes": "privateKeyAttributes",
            "private_key_flags": "privateKeyFlags",
            "subject_name_flags": "subjectNameFlags",
            "hash_algorithm": "hashAlgorithm",
            "superseded_templates": "supersededTemplates",
        },
    )
    class TemplateV4Property:
        def __init__(
            self,
            *,
            certificate_validity: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.CertificateValidityProperty", typing.Dict[builtins.str, typing.Any]]],
            enrollment_flags: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.EnrollmentFlagsV4Property", typing.Dict[builtins.str, typing.Any]]],
            extensions: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.ExtensionsV4Property", typing.Dict[builtins.str, typing.Any]]],
            general_flags: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.GeneralFlagsV4Property", typing.Dict[builtins.str, typing.Any]]],
            private_key_attributes: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.PrivateKeyAttributesV4Property", typing.Dict[builtins.str, typing.Any]]],
            private_key_flags: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.PrivateKeyFlagsV4Property", typing.Dict[builtins.str, typing.Any]]],
            subject_name_flags: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.SubjectNameFlagsV4Property", typing.Dict[builtins.str, typing.Any]]],
            hash_algorithm: typing.Optional[builtins.str] = None,
            superseded_templates: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''v4 template schema that can use either Legacy Cryptographic Providers or Key Storage Providers.

            :param certificate_validity: Certificate validity describes the validity and renewal periods of a certificate.
            :param enrollment_flags: Enrollment flags describe the enrollment settings for certificates using the existing private key and deleting expired or revoked certificates.
            :param extensions: Extensions describe the key usage extensions and application policies for a template.
            :param general_flags: General flags describe whether the template is used for computers or users and if the template can be used with autoenrollment.
            :param private_key_attributes: Private key attributes allow you to specify the minimal key length, key spec, key usage, and cryptographic providers for the private key of a certificate for v4 templates. V4 templates allow you to use either Key Storage Providers or Legacy Cryptographic Service Providers. You specify the cryptography provider category in private key flags.
            :param private_key_flags: Private key flags for v4 templates specify the client compatibility, if the private key can be exported, if user input is required when using a private key, if an alternate signature algorithm should be used, and if certificates are renewed using the same private key.
            :param subject_name_flags: Subject name flags describe the subject name and subject alternate name that is included in a certificate.
            :param hash_algorithm: Specifies the hash algorithm used to hash the private key. Hash algorithm can only be specified when using Key Storage Providers.
            :param superseded_templates: List of templates in Active Directory that are superseded by this template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev4.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                template_v4_property = pcaconnectorad.CfnTemplate.TemplateV4Property(
                    certificate_validity=pcaconnectorad.CfnTemplate.CertificateValidityProperty(
                        renewal_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                            period=123,
                            period_type="periodType"
                        ),
                        validity_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                            period=123,
                            period_type="periodType"
                        )
                    ),
                    enrollment_flags=pcaconnectorad.CfnTemplate.EnrollmentFlagsV4Property(
                        enable_key_reuse_on_nt_token_keyset_storage_full=False,
                        include_symmetric_algorithms=False,
                        no_security_extension=False,
                        remove_invalid_certificate_from_personal_store=False,
                        user_interaction_required=False
                    ),
                    extensions=pcaconnectorad.CfnTemplate.ExtensionsV4Property(
                        key_usage=pcaconnectorad.CfnTemplate.KeyUsageProperty(
                            usage_flags=pcaconnectorad.CfnTemplate.KeyUsageFlagsProperty(
                                data_encipherment=False,
                                digital_signature=False,
                                key_agreement=False,
                                key_encipherment=False,
                                non_repudiation=False
                            ),
                
                            # the properties below are optional
                            critical=False
                        ),
                
                        # the properties below are optional
                        application_policies=pcaconnectorad.CfnTemplate.ApplicationPoliciesProperty(
                            policies=[pcaconnectorad.CfnTemplate.ApplicationPolicyProperty(
                                policy_object_identifier="policyObjectIdentifier",
                                policy_type="policyType"
                            )],
                
                            # the properties below are optional
                            critical=False
                        )
                    ),
                    general_flags=pcaconnectorad.CfnTemplate.GeneralFlagsV4Property(
                        auto_enrollment=False,
                        machine_type=False
                    ),
                    private_key_attributes=pcaconnectorad.CfnTemplate.PrivateKeyAttributesV4Property(
                        key_spec="keySpec",
                        minimal_key_length=123,
                
                        # the properties below are optional
                        algorithm="algorithm",
                        crypto_providers=["cryptoProviders"],
                        key_usage_property=pcaconnectorad.CfnTemplate.KeyUsagePropertyProperty(
                            property_flags=pcaconnectorad.CfnTemplate.KeyUsagePropertyFlagsProperty(
                                decrypt=False,
                                key_agreement=False,
                                sign=False
                            ),
                            property_type="propertyType"
                        )
                    ),
                    private_key_flags=pcaconnectorad.CfnTemplate.PrivateKeyFlagsV4Property(
                        client_version="clientVersion",
                
                        # the properties below are optional
                        exportable_key=False,
                        require_alternate_signature_algorithm=False,
                        require_same_key_renewal=False,
                        strong_key_protection_required=False,
                        use_legacy_provider=False
                    ),
                    subject_name_flags=pcaconnectorad.CfnTemplate.SubjectNameFlagsV4Property(
                        require_common_name=False,
                        require_directory_path=False,
                        require_dns_as_cn=False,
                        require_email=False,
                        san_require_directory_guid=False,
                        san_require_dns=False,
                        san_require_domain_dns=False,
                        san_require_email=False,
                        san_require_spn=False,
                        san_require_upn=False
                    ),
                
                    # the properties below are optional
                    hash_algorithm="hashAlgorithm",
                    superseded_templates=["supersededTemplates"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c6104d8117de99af2149797a9c5cce3e3eb500e8f80d02ab1eac853d1168121c)
                check_type(argname="argument certificate_validity", value=certificate_validity, expected_type=type_hints["certificate_validity"])
                check_type(argname="argument enrollment_flags", value=enrollment_flags, expected_type=type_hints["enrollment_flags"])
                check_type(argname="argument extensions", value=extensions, expected_type=type_hints["extensions"])
                check_type(argname="argument general_flags", value=general_flags, expected_type=type_hints["general_flags"])
                check_type(argname="argument private_key_attributes", value=private_key_attributes, expected_type=type_hints["private_key_attributes"])
                check_type(argname="argument private_key_flags", value=private_key_flags, expected_type=type_hints["private_key_flags"])
                check_type(argname="argument subject_name_flags", value=subject_name_flags, expected_type=type_hints["subject_name_flags"])
                check_type(argname="argument hash_algorithm", value=hash_algorithm, expected_type=type_hints["hash_algorithm"])
                check_type(argname="argument superseded_templates", value=superseded_templates, expected_type=type_hints["superseded_templates"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "certificate_validity": certificate_validity,
                "enrollment_flags": enrollment_flags,
                "extensions": extensions,
                "general_flags": general_flags,
                "private_key_attributes": private_key_attributes,
                "private_key_flags": private_key_flags,
                "subject_name_flags": subject_name_flags,
            }
            if hash_algorithm is not None:
                self._values["hash_algorithm"] = hash_algorithm
            if superseded_templates is not None:
                self._values["superseded_templates"] = superseded_templates

        @builtins.property
        def certificate_validity(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.CertificateValidityProperty"]:
            '''Certificate validity describes the validity and renewal periods of a certificate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev4.html#cfn-pcaconnectorad-template-templatev4-certificatevalidity
            '''
            result = self._values.get("certificate_validity")
            assert result is not None, "Required property 'certificate_validity' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.CertificateValidityProperty"], result)

        @builtins.property
        def enrollment_flags(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.EnrollmentFlagsV4Property"]:
            '''Enrollment flags describe the enrollment settings for certificates using the existing private key and deleting expired or revoked certificates.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev4.html#cfn-pcaconnectorad-template-templatev4-enrollmentflags
            '''
            result = self._values.get("enrollment_flags")
            assert result is not None, "Required property 'enrollment_flags' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.EnrollmentFlagsV4Property"], result)

        @builtins.property
        def extensions(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.ExtensionsV4Property"]:
            '''Extensions describe the key usage extensions and application policies for a template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev4.html#cfn-pcaconnectorad-template-templatev4-extensions
            '''
            result = self._values.get("extensions")
            assert result is not None, "Required property 'extensions' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.ExtensionsV4Property"], result)

        @builtins.property
        def general_flags(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.GeneralFlagsV4Property"]:
            '''General flags describe whether the template is used for computers or users and if the template can be used with autoenrollment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev4.html#cfn-pcaconnectorad-template-templatev4-generalflags
            '''
            result = self._values.get("general_flags")
            assert result is not None, "Required property 'general_flags' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.GeneralFlagsV4Property"], result)

        @builtins.property
        def private_key_attributes(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.PrivateKeyAttributesV4Property"]:
            '''Private key attributes allow you to specify the minimal key length, key spec, key usage, and cryptographic providers for the private key of a certificate for v4 templates.

            V4 templates allow you to use either Key Storage Providers or Legacy Cryptographic Service Providers. You specify the cryptography provider category in private key flags.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev4.html#cfn-pcaconnectorad-template-templatev4-privatekeyattributes
            '''
            result = self._values.get("private_key_attributes")
            assert result is not None, "Required property 'private_key_attributes' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.PrivateKeyAttributesV4Property"], result)

        @builtins.property
        def private_key_flags(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.PrivateKeyFlagsV4Property"]:
            '''Private key flags for v4 templates specify the client compatibility, if the private key can be exported, if user input is required when using a private key, if an alternate signature algorithm should be used, and if certificates are renewed using the same private key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev4.html#cfn-pcaconnectorad-template-templatev4-privatekeyflags
            '''
            result = self._values.get("private_key_flags")
            assert result is not None, "Required property 'private_key_flags' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.PrivateKeyFlagsV4Property"], result)

        @builtins.property
        def subject_name_flags(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplate.SubjectNameFlagsV4Property"]:
            '''Subject name flags describe the subject name and subject alternate name that is included in a certificate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev4.html#cfn-pcaconnectorad-template-templatev4-subjectnameflags
            '''
            result = self._values.get("subject_name_flags")
            assert result is not None, "Required property 'subject_name_flags' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplate.SubjectNameFlagsV4Property"], result)

        @builtins.property
        def hash_algorithm(self) -> typing.Optional[builtins.str]:
            '''Specifies the hash algorithm used to hash the private key.

            Hash algorithm can only be specified when using Key Storage Providers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev4.html#cfn-pcaconnectorad-template-templatev4-hashalgorithm
            '''
            result = self._values.get("hash_algorithm")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def superseded_templates(self) -> typing.Optional[typing.List[builtins.str]]:
            '''List of templates in Active Directory that are superseded by this template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-templatev4.html#cfn-pcaconnectorad-template-templatev4-supersededtemplates
            '''
            result = self._values.get("superseded_templates")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TemplateV4Property(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplate.ValidityPeriodProperty",
        jsii_struct_bases=[],
        name_mapping={"period": "period", "period_type": "periodType"},
    )
    class ValidityPeriodProperty:
        def __init__(self, *, period: jsii.Number, period_type: builtins.str) -> None:
            '''Information describing the end of the validity period of the certificate.

            This parameter sets the “Not After” date for the certificate. Certificate validity is the period of time during which a certificate is valid. Validity can be expressed as an explicit date and time when the certificate expires, or as a span of time after issuance, stated in hours, days, months, or years. For more information, see Validity in RFC 5280. This value is unaffected when ValidityNotBefore is also specified. For example, if Validity is set to 20 days in the future, the certificate will expire 20 days from issuance time regardless of the ValidityNotBefore value.

            :param period: The numeric value for the validity period.
            :param period_type: The unit of time. You can select hours, days, weeks, months, and years.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-validityperiod.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                validity_period_property = pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                    period=123,
                    period_type="periodType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9b7fd6091b8198bbe84b2f3027ec7cb8b9e3a8a5f69f78123238e5a3c22ee1ab)
                check_type(argname="argument period", value=period, expected_type=type_hints["period"])
                check_type(argname="argument period_type", value=period_type, expected_type=type_hints["period_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "period": period,
                "period_type": period_type,
            }

        @builtins.property
        def period(self) -> jsii.Number:
            '''The numeric value for the validity period.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-validityperiod.html#cfn-pcaconnectorad-template-validityperiod-period
            '''
            result = self._values.get("period")
            assert result is not None, "Required property 'period' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def period_type(self) -> builtins.str:
            '''The unit of time.

            You can select hours, days, weeks, months, and years.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-template-validityperiod.html#cfn-pcaconnectorad-template-validityperiod-periodtype
            '''
            result = self._values.get("period_type")
            assert result is not None, "Required property 'period_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ValidityPeriodProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnTemplateGroupAccessControlEntry(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplateGroupAccessControlEntry",
):
    '''Create a group access control entry.

    Allow or deny Active Directory groups from enrolling and/or autoenrolling with the template based on the group security identifiers (SIDs).

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-templategroupaccesscontrolentry.html
    :cloudformationResource: AWS::PCAConnectorAD::TemplateGroupAccessControlEntry
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_pcaconnectorad as pcaconnectorad
        
        cfn_template_group_access_control_entry = pcaconnectorad.CfnTemplateGroupAccessControlEntry(self, "MyCfnTemplateGroupAccessControlEntry",
            access_rights=pcaconnectorad.CfnTemplateGroupAccessControlEntry.AccessRightsProperty(
                auto_enroll="autoEnroll",
                enroll="enroll"
            ),
            group_display_name="groupDisplayName",
        
            # the properties below are optional
            group_security_identifier="groupSecurityIdentifier",
            template_arn="templateArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        access_rights: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplateGroupAccessControlEntry.AccessRightsProperty", typing.Dict[builtins.str, typing.Any]]],
        group_display_name: builtins.str,
        group_security_identifier: typing.Optional[builtins.str] = None,
        template_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param access_rights: Permissions to allow or deny an Active Directory group to enroll or autoenroll certificates issued against a template.
        :param group_display_name: Name of the Active Directory group. This name does not need to match the group name in Active Directory.
        :param group_security_identifier: Security identifier (SID) of the group object from Active Directory. The SID starts with "S-".
        :param template_arn: The Amazon Resource Name (ARN) that was returned when you called `CreateTemplate <https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3afc1d4e6fd3841e33fcac8256963308de41afb74b2ac0fec481a86647067ec3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTemplateGroupAccessControlEntryProps(
            access_rights=access_rights,
            group_display_name=group_display_name,
            group_security_identifier=group_security_identifier,
            template_arn=template_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2237339544790e2b019a0bf7fd86dfeab241882c8d4366e39039898b39c99ec6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__71d54f04eb15c1354088f2337813be59d6ed5aff5bea943a3e810da7621b06c4)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="accessRights")
    def access_rights(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnTemplateGroupAccessControlEntry.AccessRightsProperty"]:
        '''Permissions to allow or deny an Active Directory group to enroll or autoenroll certificates issued against a template.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTemplateGroupAccessControlEntry.AccessRightsProperty"], jsii.get(self, "accessRights"))

    @access_rights.setter
    def access_rights(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnTemplateGroupAccessControlEntry.AccessRightsProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__186451b885ce1f5d39a9062a1daec093b87a1acb9aaeaab87a9c26d0732b7475)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessRights", value)

    @builtins.property
    @jsii.member(jsii_name="groupDisplayName")
    def group_display_name(self) -> builtins.str:
        '''Name of the Active Directory group.'''
        return typing.cast(builtins.str, jsii.get(self, "groupDisplayName"))

    @group_display_name.setter
    def group_display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba2097b96364b1f0a4e58b04aa0cbb6cc515a5f811754f986deed65990eb077e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupDisplayName", value)

    @builtins.property
    @jsii.member(jsii_name="groupSecurityIdentifier")
    def group_security_identifier(self) -> typing.Optional[builtins.str]:
        '''Security identifier (SID) of the group object from Active Directory.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupSecurityIdentifier"))

    @group_security_identifier.setter
    def group_security_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76b47557e0c980e45e43e15cd1f957c409b393473a036f0ae581dd1b8c6552b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupSecurityIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="templateArn")
    def template_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) that was returned when you called `CreateTemplate <https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html>`_ .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateArn"))

    @template_arn.setter
    def template_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67cb0b070afb7e27a3030dfbdcd7496f1c3ebc2240fb6ab131af4439b7c6e156)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateArn", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplateGroupAccessControlEntry.AccessRightsProperty",
        jsii_struct_bases=[],
        name_mapping={"auto_enroll": "autoEnroll", "enroll": "enroll"},
    )
    class AccessRightsProperty:
        def __init__(
            self,
            *,
            auto_enroll: typing.Optional[builtins.str] = None,
            enroll: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Allow or deny permissions for an Active Directory group to enroll or autoenroll certificates for a template.

            :param auto_enroll: Allow or deny an Active Directory group from autoenrolling certificates issued against a template. The Active Directory group must be allowed to enroll to allow autoenrollment
            :param enroll: Allow or deny an Active Directory group from enrolling certificates issued against a template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-templategroupaccesscontrolentry-accessrights.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_pcaconnectorad as pcaconnectorad
                
                access_rights_property = pcaconnectorad.CfnTemplateGroupAccessControlEntry.AccessRightsProperty(
                    auto_enroll="autoEnroll",
                    enroll="enroll"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cb1f4cfd72a22034fea283dd1de5d715f9b63f5e79755751a507a06a12025b82)
                check_type(argname="argument auto_enroll", value=auto_enroll, expected_type=type_hints["auto_enroll"])
                check_type(argname="argument enroll", value=enroll, expected_type=type_hints["enroll"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if auto_enroll is not None:
                self._values["auto_enroll"] = auto_enroll
            if enroll is not None:
                self._values["enroll"] = enroll

        @builtins.property
        def auto_enroll(self) -> typing.Optional[builtins.str]:
            '''Allow or deny an Active Directory group from autoenrolling certificates issued against a template.

            The Active Directory group must be allowed to enroll to allow autoenrollment

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-templategroupaccesscontrolentry-accessrights.html#cfn-pcaconnectorad-templategroupaccesscontrolentry-accessrights-autoenroll
            '''
            result = self._values.get("auto_enroll")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enroll(self) -> typing.Optional[builtins.str]:
            '''Allow or deny an Active Directory group from enrolling certificates issued against a template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pcaconnectorad-templategroupaccesscontrolentry-accessrights.html#cfn-pcaconnectorad-templategroupaccesscontrolentry-accessrights-enroll
            '''
            result = self._values.get("enroll")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessRightsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplateGroupAccessControlEntryProps",
    jsii_struct_bases=[],
    name_mapping={
        "access_rights": "accessRights",
        "group_display_name": "groupDisplayName",
        "group_security_identifier": "groupSecurityIdentifier",
        "template_arn": "templateArn",
    },
)
class CfnTemplateGroupAccessControlEntryProps:
    def __init__(
        self,
        *,
        access_rights: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplateGroupAccessControlEntry.AccessRightsProperty, typing.Dict[builtins.str, typing.Any]]],
        group_display_name: builtins.str,
        group_security_identifier: typing.Optional[builtins.str] = None,
        template_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnTemplateGroupAccessControlEntry``.

        :param access_rights: Permissions to allow or deny an Active Directory group to enroll or autoenroll certificates issued against a template.
        :param group_display_name: Name of the Active Directory group. This name does not need to match the group name in Active Directory.
        :param group_security_identifier: Security identifier (SID) of the group object from Active Directory. The SID starts with "S-".
        :param template_arn: The Amazon Resource Name (ARN) that was returned when you called `CreateTemplate <https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-templategroupaccesscontrolentry.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pcaconnectorad as pcaconnectorad
            
            cfn_template_group_access_control_entry_props = pcaconnectorad.CfnTemplateGroupAccessControlEntryProps(
                access_rights=pcaconnectorad.CfnTemplateGroupAccessControlEntry.AccessRightsProperty(
                    auto_enroll="autoEnroll",
                    enroll="enroll"
                ),
                group_display_name="groupDisplayName",
            
                # the properties below are optional
                group_security_identifier="groupSecurityIdentifier",
                template_arn="templateArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e09aa5b6a189208934626d51a2a4ce72a03a91c1e114f462f32017df55c81f41)
            check_type(argname="argument access_rights", value=access_rights, expected_type=type_hints["access_rights"])
            check_type(argname="argument group_display_name", value=group_display_name, expected_type=type_hints["group_display_name"])
            check_type(argname="argument group_security_identifier", value=group_security_identifier, expected_type=type_hints["group_security_identifier"])
            check_type(argname="argument template_arn", value=template_arn, expected_type=type_hints["template_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_rights": access_rights,
            "group_display_name": group_display_name,
        }
        if group_security_identifier is not None:
            self._values["group_security_identifier"] = group_security_identifier
        if template_arn is not None:
            self._values["template_arn"] = template_arn

    @builtins.property
    def access_rights(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnTemplateGroupAccessControlEntry.AccessRightsProperty]:
        '''Permissions to allow or deny an Active Directory group to enroll or autoenroll certificates issued against a template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-templategroupaccesscontrolentry.html#cfn-pcaconnectorad-templategroupaccesscontrolentry-accessrights
        '''
        result = self._values.get("access_rights")
        assert result is not None, "Required property 'access_rights' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnTemplateGroupAccessControlEntry.AccessRightsProperty], result)

    @builtins.property
    def group_display_name(self) -> builtins.str:
        '''Name of the Active Directory group.

        This name does not need to match the group name in Active Directory.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-templategroupaccesscontrolentry.html#cfn-pcaconnectorad-templategroupaccesscontrolentry-groupdisplayname
        '''
        result = self._values.get("group_display_name")
        assert result is not None, "Required property 'group_display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_security_identifier(self) -> typing.Optional[builtins.str]:
        '''Security identifier (SID) of the group object from Active Directory.

        The SID starts with "S-".

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-templategroupaccesscontrolentry.html#cfn-pcaconnectorad-templategroupaccesscontrolentry-groupsecurityidentifier
        '''
        result = self._values.get("group_security_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def template_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) that was returned when you called `CreateTemplate <https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-templategroupaccesscontrolentry.html#cfn-pcaconnectorad-templategroupaccesscontrolentry-templatearn
        '''
        result = self._values.get("template_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTemplateGroupAccessControlEntryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_pcaconnectorad.CfnTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "connector_arn": "connectorArn",
        "definition": "definition",
        "name": "name",
        "reenroll_all_certificate_holders": "reenrollAllCertificateHolders",
        "tags": "tags",
    },
)
class CfnTemplateProps:
    def __init__(
        self,
        *,
        connector_arn: builtins.str,
        definition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.TemplateDefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        reenroll_all_certificate_holders: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTemplate``.

        :param connector_arn: The Amazon Resource Name (ARN) that was returned when you called `CreateConnector <https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html>`_ .
        :param definition: Template configuration to define the information included in certificates. Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.
        :param name: Name of the templates. Template names must be unique.
        :param reenroll_all_certificate_holders: This setting allows the major version of a template to be increased automatically. All members of Active Directory groups that are allowed to enroll with a template will receive a new certificate issued using that template.
        :param tags: Metadata assigned to a template consisting of a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-template.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_pcaconnectorad as pcaconnectorad
            
            cfn_template_props = pcaconnectorad.CfnTemplateProps(
                connector_arn="connectorArn",
                definition=pcaconnectorad.CfnTemplate.TemplateDefinitionProperty(
                    template_v2=pcaconnectorad.CfnTemplate.TemplateV2Property(
                        certificate_validity=pcaconnectorad.CfnTemplate.CertificateValidityProperty(
                            renewal_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                                period=123,
                                period_type="periodType"
                            ),
                            validity_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                                period=123,
                                period_type="periodType"
                            )
                        ),
                        enrollment_flags=pcaconnectorad.CfnTemplate.EnrollmentFlagsV2Property(
                            enable_key_reuse_on_nt_token_keyset_storage_full=False,
                            include_symmetric_algorithms=False,
                            no_security_extension=False,
                            remove_invalid_certificate_from_personal_store=False,
                            user_interaction_required=False
                        ),
                        extensions=pcaconnectorad.CfnTemplate.ExtensionsV2Property(
                            key_usage=pcaconnectorad.CfnTemplate.KeyUsageProperty(
                                usage_flags=pcaconnectorad.CfnTemplate.KeyUsageFlagsProperty(
                                    data_encipherment=False,
                                    digital_signature=False,
                                    key_agreement=False,
                                    key_encipherment=False,
                                    non_repudiation=False
                                ),
            
                                # the properties below are optional
                                critical=False
                            ),
            
                            # the properties below are optional
                            application_policies=pcaconnectorad.CfnTemplate.ApplicationPoliciesProperty(
                                policies=[pcaconnectorad.CfnTemplate.ApplicationPolicyProperty(
                                    policy_object_identifier="policyObjectIdentifier",
                                    policy_type="policyType"
                                )],
            
                                # the properties below are optional
                                critical=False
                            )
                        ),
                        general_flags=pcaconnectorad.CfnTemplate.GeneralFlagsV2Property(
                            auto_enrollment=False,
                            machine_type=False
                        ),
                        private_key_attributes=pcaconnectorad.CfnTemplate.PrivateKeyAttributesV2Property(
                            key_spec="keySpec",
                            minimal_key_length=123,
            
                            # the properties below are optional
                            crypto_providers=["cryptoProviders"]
                        ),
                        private_key_flags=pcaconnectorad.CfnTemplate.PrivateKeyFlagsV2Property(
                            client_version="clientVersion",
            
                            # the properties below are optional
                            exportable_key=False,
                            strong_key_protection_required=False
                        ),
                        subject_name_flags=pcaconnectorad.CfnTemplate.SubjectNameFlagsV2Property(
                            require_common_name=False,
                            require_directory_path=False,
                            require_dns_as_cn=False,
                            require_email=False,
                            san_require_directory_guid=False,
                            san_require_dns=False,
                            san_require_domain_dns=False,
                            san_require_email=False,
                            san_require_spn=False,
                            san_require_upn=False
                        ),
            
                        # the properties below are optional
                        superseded_templates=["supersededTemplates"]
                    ),
                    template_v3=pcaconnectorad.CfnTemplate.TemplateV3Property(
                        certificate_validity=pcaconnectorad.CfnTemplate.CertificateValidityProperty(
                            renewal_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                                period=123,
                                period_type="periodType"
                            ),
                            validity_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                                period=123,
                                period_type="periodType"
                            )
                        ),
                        enrollment_flags=pcaconnectorad.CfnTemplate.EnrollmentFlagsV3Property(
                            enable_key_reuse_on_nt_token_keyset_storage_full=False,
                            include_symmetric_algorithms=False,
                            no_security_extension=False,
                            remove_invalid_certificate_from_personal_store=False,
                            user_interaction_required=False
                        ),
                        extensions=pcaconnectorad.CfnTemplate.ExtensionsV3Property(
                            key_usage=pcaconnectorad.CfnTemplate.KeyUsageProperty(
                                usage_flags=pcaconnectorad.CfnTemplate.KeyUsageFlagsProperty(
                                    data_encipherment=False,
                                    digital_signature=False,
                                    key_agreement=False,
                                    key_encipherment=False,
                                    non_repudiation=False
                                ),
            
                                # the properties below are optional
                                critical=False
                            ),
            
                            # the properties below are optional
                            application_policies=pcaconnectorad.CfnTemplate.ApplicationPoliciesProperty(
                                policies=[pcaconnectorad.CfnTemplate.ApplicationPolicyProperty(
                                    policy_object_identifier="policyObjectIdentifier",
                                    policy_type="policyType"
                                )],
            
                                # the properties below are optional
                                critical=False
                            )
                        ),
                        general_flags=pcaconnectorad.CfnTemplate.GeneralFlagsV3Property(
                            auto_enrollment=False,
                            machine_type=False
                        ),
                        hash_algorithm="hashAlgorithm",
                        private_key_attributes=pcaconnectorad.CfnTemplate.PrivateKeyAttributesV3Property(
                            algorithm="algorithm",
                            key_spec="keySpec",
                            key_usage_property=pcaconnectorad.CfnTemplate.KeyUsagePropertyProperty(
                                property_flags=pcaconnectorad.CfnTemplate.KeyUsagePropertyFlagsProperty(
                                    decrypt=False,
                                    key_agreement=False,
                                    sign=False
                                ),
                                property_type="propertyType"
                            ),
                            minimal_key_length=123,
            
                            # the properties below are optional
                            crypto_providers=["cryptoProviders"]
                        ),
                        private_key_flags=pcaconnectorad.CfnTemplate.PrivateKeyFlagsV3Property(
                            client_version="clientVersion",
            
                            # the properties below are optional
                            exportable_key=False,
                            require_alternate_signature_algorithm=False,
                            strong_key_protection_required=False
                        ),
                        subject_name_flags=pcaconnectorad.CfnTemplate.SubjectNameFlagsV3Property(
                            require_common_name=False,
                            require_directory_path=False,
                            require_dns_as_cn=False,
                            require_email=False,
                            san_require_directory_guid=False,
                            san_require_dns=False,
                            san_require_domain_dns=False,
                            san_require_email=False,
                            san_require_spn=False,
                            san_require_upn=False
                        ),
            
                        # the properties below are optional
                        superseded_templates=["supersededTemplates"]
                    ),
                    template_v4=pcaconnectorad.CfnTemplate.TemplateV4Property(
                        certificate_validity=pcaconnectorad.CfnTemplate.CertificateValidityProperty(
                            renewal_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                                period=123,
                                period_type="periodType"
                            ),
                            validity_period=pcaconnectorad.CfnTemplate.ValidityPeriodProperty(
                                period=123,
                                period_type="periodType"
                            )
                        ),
                        enrollment_flags=pcaconnectorad.CfnTemplate.EnrollmentFlagsV4Property(
                            enable_key_reuse_on_nt_token_keyset_storage_full=False,
                            include_symmetric_algorithms=False,
                            no_security_extension=False,
                            remove_invalid_certificate_from_personal_store=False,
                            user_interaction_required=False
                        ),
                        extensions=pcaconnectorad.CfnTemplate.ExtensionsV4Property(
                            key_usage=pcaconnectorad.CfnTemplate.KeyUsageProperty(
                                usage_flags=pcaconnectorad.CfnTemplate.KeyUsageFlagsProperty(
                                    data_encipherment=False,
                                    digital_signature=False,
                                    key_agreement=False,
                                    key_encipherment=False,
                                    non_repudiation=False
                                ),
            
                                # the properties below are optional
                                critical=False
                            ),
            
                            # the properties below are optional
                            application_policies=pcaconnectorad.CfnTemplate.ApplicationPoliciesProperty(
                                policies=[pcaconnectorad.CfnTemplate.ApplicationPolicyProperty(
                                    policy_object_identifier="policyObjectIdentifier",
                                    policy_type="policyType"
                                )],
            
                                # the properties below are optional
                                critical=False
                            )
                        ),
                        general_flags=pcaconnectorad.CfnTemplate.GeneralFlagsV4Property(
                            auto_enrollment=False,
                            machine_type=False
                        ),
                        private_key_attributes=pcaconnectorad.CfnTemplate.PrivateKeyAttributesV4Property(
                            key_spec="keySpec",
                            minimal_key_length=123,
            
                            # the properties below are optional
                            algorithm="algorithm",
                            crypto_providers=["cryptoProviders"],
                            key_usage_property=pcaconnectorad.CfnTemplate.KeyUsagePropertyProperty(
                                property_flags=pcaconnectorad.CfnTemplate.KeyUsagePropertyFlagsProperty(
                                    decrypt=False,
                                    key_agreement=False,
                                    sign=False
                                ),
                                property_type="propertyType"
                            )
                        ),
                        private_key_flags=pcaconnectorad.CfnTemplate.PrivateKeyFlagsV4Property(
                            client_version="clientVersion",
            
                            # the properties below are optional
                            exportable_key=False,
                            require_alternate_signature_algorithm=False,
                            require_same_key_renewal=False,
                            strong_key_protection_required=False,
                            use_legacy_provider=False
                        ),
                        subject_name_flags=pcaconnectorad.CfnTemplate.SubjectNameFlagsV4Property(
                            require_common_name=False,
                            require_directory_path=False,
                            require_dns_as_cn=False,
                            require_email=False,
                            san_require_directory_guid=False,
                            san_require_dns=False,
                            san_require_domain_dns=False,
                            san_require_email=False,
                            san_require_spn=False,
                            san_require_upn=False
                        ),
            
                        # the properties below are optional
                        hash_algorithm="hashAlgorithm",
                        superseded_templates=["supersededTemplates"]
                    )
                ),
                name="name",
            
                # the properties below are optional
                reenroll_all_certificate_holders=False,
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaedf159635a05945c9190de39c64b80921762454b586cb04745b2201ee34048)
            check_type(argname="argument connector_arn", value=connector_arn, expected_type=type_hints["connector_arn"])
            check_type(argname="argument definition", value=definition, expected_type=type_hints["definition"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument reenroll_all_certificate_holders", value=reenroll_all_certificate_holders, expected_type=type_hints["reenroll_all_certificate_holders"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connector_arn": connector_arn,
            "definition": definition,
            "name": name,
        }
        if reenroll_all_certificate_holders is not None:
            self._values["reenroll_all_certificate_holders"] = reenroll_all_certificate_holders
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def connector_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) that was returned when you called `CreateConnector <https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-template.html#cfn-pcaconnectorad-template-connectorarn
        '''
        result = self._values.get("connector_arn")
        assert result is not None, "Required property 'connector_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def definition(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnTemplate.TemplateDefinitionProperty]:
        '''Template configuration to define the information included in certificates.

        Define certificate validity and renewal periods, certificate request handling and enrollment options, key usage extensions, application policies, and cryptography settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-template.html#cfn-pcaconnectorad-template-definition
        '''
        result = self._values.get("definition")
        assert result is not None, "Required property 'definition' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnTemplate.TemplateDefinitionProperty], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the templates.

        Template names must be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-template.html#cfn-pcaconnectorad-template-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def reenroll_all_certificate_holders(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''This setting allows the major version of a template to be increased automatically.

        All members of Active Directory groups that are allowed to enroll with a template will receive a new certificate issued using that template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-template.html#cfn-pcaconnectorad-template-reenrollallcertificateholders
        '''
        result = self._values.get("reenroll_all_certificate_holders")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Metadata assigned to a template consisting of a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pcaconnectorad-template.html#cfn-pcaconnectorad-template-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnConnector",
    "CfnConnectorProps",
    "CfnDirectoryRegistration",
    "CfnDirectoryRegistrationProps",
    "CfnServicePrincipalName",
    "CfnServicePrincipalNameProps",
    "CfnTemplate",
    "CfnTemplateGroupAccessControlEntry",
    "CfnTemplateGroupAccessControlEntryProps",
    "CfnTemplateProps",
]

publication.publish()

def _typecheckingstub__a12163a6729548e5010cdebd16984d9bc442d61e9fbbf189c986731db6b48d47(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    certificate_authority_arn: builtins.str,
    directory_id: builtins.str,
    vpc_information: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.VpcInformationProperty, typing.Dict[builtins.str, typing.Any]]],
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__995fc1e26ccbb1d65aff429128879ca6773f054cc4f117a8e1447be68e0afc96(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3d96af69193b4c63c1a08fc841f1f53484be496914e380a12d6599834d01ef1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85ffecf84ef5c66b68d71a320cbd94d944f32371d0084613413b520fe56b8c1a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__627eac80a9f24ed66c799c77c564a456223f8974b2958400dcf9e2b1083ad097(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7958644c6b6b742a56d7010b862aba24109f3f57815fa7477ed5ff078f149a85(
    value: typing.Union[_IResolvable_da3f097b, CfnConnector.VpcInformationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6278c4b97c0032befb9608a0699c8b6bccf6e756f23518e9cd72e3454c4b62b(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b9f29305eaa60cc155622de83a9fdb695e29e88cecf7960456609a9a375b153(
    *,
    security_group_ids: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__564156a907862773b47fafbb1b06e4f9c8e0d3d39ffe5d8235c3d7cc34c92a40(
    *,
    certificate_authority_arn: builtins.str,
    directory_id: builtins.str,
    vpc_information: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.VpcInformationProperty, typing.Dict[builtins.str, typing.Any]]],
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e325d6e149baf8a596306043eb453d2d3f8e118e00d5278dd37d6c33cb8c633(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    directory_id: builtins.str,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41b23bf9daa66db7deae4b509cd527669ef15b39a237b53b777a6334ec274485(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f42e0e871a5326bb18faea9ea2f2e7da908aa2959bd095e6e5686bf7e37c2cee(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe9074c785c14f7e464667b3097652bb1428d371156c62c379bd9e9076c450d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__177ed6093a034522fdd983b6789c9a099c557cbf446b6555c4af62b49b258c7b(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92354fae5f6aaf222ff6a71438d62db5492fa605cf6c14cfaf2176b801600eb4(
    *,
    directory_id: builtins.str,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__779230ef86d4538873fd875cd3babc1ab92f57abdae26cfcea7069e7eb8272d1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    connector_arn: typing.Optional[builtins.str] = None,
    directory_registration_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2282e80f861510398f89d8cf1beed04a57d98bd9fef207e0a43718dd569cca4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e3d66893530b0ec8229273f184fa5f3458cc9661569945849b363b3554b4295(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7336215d5258c7d33cf1355d3c1630bd720ee5b24987f7ee7448a6794e671e9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3b11dc247af37c1b9943c4e484a0d90a5a5c3460e646bf1e2f3ce167a88c6a4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7da1bc3702a4df8757dbc31f6575b8167128062a021b3ccf901b92314a2c56d8(
    *,
    connector_arn: typing.Optional[builtins.str] = None,
    directory_registration_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__058e4ad420b7fd03441f402ba72d6e3735672960ebcc0af660d043e5de6b6b8b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    connector_arn: builtins.str,
    definition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.TemplateDefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    reenroll_all_certificate_holders: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__522513d3e7f800ff5cbeaf35a1bafe68be5a57527909827ac7a376f1ef743427(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__902de0f2c5a1c9d56b19d05be029dfc35dfe777e3a9d654d057b6f1b6926b6de(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__079513a352e43cc7c1ce98dcc5f5e231bf3be2045a92489328ee1b7d9e23157a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa952e9ba8af0e0bd9e62b55d0cfdca23958bf5403c595f909316942859ca793(
    value: typing.Union[_IResolvable_da3f097b, CfnTemplate.TemplateDefinitionProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9501917493dbbe580243f80e21fe99ea039183a480eef09ed64d12264f51e0ee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55f6695aacde4eb1d915673bfb7f61d1f0779f429720942c4806aa7044eea5f2(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2661de5cae87e986149f4775b0ec018c21243c4e7dd8205ae490405a376832a6(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f9807ce79bbe5d1e70285819a93c0d50c131ea1e3ae32f2603d78790d787b8e(
    *,
    policies: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.ApplicationPolicyProperty, typing.Dict[builtins.str, typing.Any]]]]],
    critical: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5398e02a2971edff45634bc912f9a2a8e06f7d87c7e08b6975be28903d770e92(
    *,
    policy_object_identifier: typing.Optional[builtins.str] = None,
    policy_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4cdec65aa655f7eeeeab4a379104c931aa1af736720f784aa86045f4e6cade5(
    *,
    renewal_period: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.ValidityPeriodProperty, typing.Dict[builtins.str, typing.Any]]],
    validity_period: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.ValidityPeriodProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31d0076b2df64888291f4f323da23d8cbc5d3b6efaf716095d546e42d9d75cb6(
    *,
    enable_key_reuse_on_nt_token_keyset_storage_full: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_symmetric_algorithms: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    no_security_extension: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    remove_invalid_certificate_from_personal_store: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    user_interaction_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__503a76586e23e26e001311af23206f04ade685e0a3481b11037f8b9a352897ea(
    *,
    enable_key_reuse_on_nt_token_keyset_storage_full: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_symmetric_algorithms: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    no_security_extension: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    remove_invalid_certificate_from_personal_store: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    user_interaction_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c3dbe764d7841c99b8270527bff9cfbf7b80b333e77d3386deefdbae8a0aa63(
    *,
    enable_key_reuse_on_nt_token_keyset_storage_full: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_symmetric_algorithms: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    no_security_extension: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    remove_invalid_certificate_from_personal_store: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    user_interaction_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0141d8fd6f7754483c21d402e5a2141226e85c41cd0ed6de1704acfed6d37da8(
    *,
    key_usage: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.KeyUsageProperty, typing.Dict[builtins.str, typing.Any]]],
    application_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.ApplicationPoliciesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bc196c1d5fd1dd60e51f454b41b5cb30ae245ceec4cd14d522a2deb5ff66714(
    *,
    key_usage: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.KeyUsageProperty, typing.Dict[builtins.str, typing.Any]]],
    application_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.ApplicationPoliciesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__601e4ea2eea3cb68c41cbee071f8b18ff40cd8225923970223bb0622dbe80979(
    *,
    key_usage: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.KeyUsageProperty, typing.Dict[builtins.str, typing.Any]]],
    application_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.ApplicationPoliciesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__097faefbc9f8cebe8de0057f783e113aed655061f3c6eed7bd1853fe59e8eff7(
    *,
    auto_enrollment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    machine_type: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5cce72190738262664533347db8bc91239197327c27f7f816b4293abe93de3a(
    *,
    auto_enrollment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    machine_type: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b049cb9c768149c0cf11c978d7de1e5d940749022cdc037468cdb29e00809ba9(
    *,
    auto_enrollment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    machine_type: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c80dba709763d03d37f95ecc20a6778d922627a5e7fff950156e15d8cd108bf(
    *,
    data_encipherment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    digital_signature: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    key_agreement: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    key_encipherment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    non_repudiation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7820e30f088ec528d6503414a4752bd7dc51a8186ee36b410ff7ec91c6b731a2(
    *,
    usage_flags: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.KeyUsageFlagsProperty, typing.Dict[builtins.str, typing.Any]]],
    critical: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3eb45f2f53233d30a1605227f9826c39b26061c0487cbf31b14d99ebda3a3988(
    *,
    decrypt: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    key_agreement: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    sign: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__affa60f9efeb947eabcf0c21ec7d80a0c06bcf71ee3f241f69c5b78d4b7f7818(
    *,
    property_flags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.KeyUsagePropertyFlagsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    property_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0da38511e8586071939df45f55c73f6ea301eca8b340d0c8584b2699e138d8e(
    *,
    key_spec: builtins.str,
    minimal_key_length: jsii.Number,
    crypto_providers: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e9e3e2c2671b7460269d56c9b1fa79f71e05a898d752d57c8f7ec1252321c0a(
    *,
    algorithm: builtins.str,
    key_spec: builtins.str,
    key_usage_property: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.KeyUsagePropertyProperty, typing.Dict[builtins.str, typing.Any]]],
    minimal_key_length: jsii.Number,
    crypto_providers: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7c5feb1e1b2ba9fa72d5dbc4bfa202c29886082d399af5eaef3697ca7bd3e91(
    *,
    key_spec: builtins.str,
    minimal_key_length: jsii.Number,
    algorithm: typing.Optional[builtins.str] = None,
    crypto_providers: typing.Optional[typing.Sequence[builtins.str]] = None,
    key_usage_property: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.KeyUsagePropertyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcacc2239810164b395e4a383b95ed7bf7d6465116db368e0cc34d314e118d05(
    *,
    client_version: builtins.str,
    exportable_key: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    strong_key_protection_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7125a0dc03338f06174e788deefaea543edbc61c3ea00ce935559757c5f7ec9b(
    *,
    client_version: builtins.str,
    exportable_key: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    require_alternate_signature_algorithm: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    strong_key_protection_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf7957c0cde147fdfb6b22d46b1ee3896e5bd94b6bbd4c9b61f1665d8bc79956(
    *,
    client_version: builtins.str,
    exportable_key: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    require_alternate_signature_algorithm: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    require_same_key_renewal: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    strong_key_protection_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    use_legacy_provider: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7e503c1f26db9d55430becc5fc9c403a6fdcca743366fdd9e02b40df1ebe9f3(
    *,
    require_common_name: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    require_directory_path: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    require_dns_as_cn: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    require_email: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    san_require_directory_guid: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    san_require_dns: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    san_require_domain_dns: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    san_require_email: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    san_require_spn: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    san_require_upn: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a52f3b78a4f3064dd840a4a38dc2a5628ba7b5b6a05ec68cc52e3bcb1c750ee(
    *,
    require_common_name: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    require_directory_path: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    require_dns_as_cn: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    require_email: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    san_require_directory_guid: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    san_require_dns: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    san_require_domain_dns: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    san_require_email: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    san_require_spn: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    san_require_upn: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e71f41f55a91f74da966fd2db125279f9d27eaa16bcb61171df96219e48b1c7(
    *,
    require_common_name: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    require_directory_path: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    require_dns_as_cn: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    require_email: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    san_require_directory_guid: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    san_require_dns: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    san_require_domain_dns: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    san_require_email: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    san_require_spn: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    san_require_upn: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64b80ea351fed33fc54e6692c72597ccfcccd5060a63508183b4f41674d9fc0c(
    *,
    template_v2: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.TemplateV2Property, typing.Dict[builtins.str, typing.Any]]]] = None,
    template_v3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.TemplateV3Property, typing.Dict[builtins.str, typing.Any]]]] = None,
    template_v4: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.TemplateV4Property, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__151fc4337a303972048fa1af002c8cdbcb6d2ff15c97afedf760ae127b7f5bfc(
    *,
    certificate_validity: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.CertificateValidityProperty, typing.Dict[builtins.str, typing.Any]]],
    enrollment_flags: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.EnrollmentFlagsV2Property, typing.Dict[builtins.str, typing.Any]]],
    extensions: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.ExtensionsV2Property, typing.Dict[builtins.str, typing.Any]]],
    general_flags: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.GeneralFlagsV2Property, typing.Dict[builtins.str, typing.Any]]],
    private_key_attributes: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.PrivateKeyAttributesV2Property, typing.Dict[builtins.str, typing.Any]]],
    private_key_flags: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.PrivateKeyFlagsV2Property, typing.Dict[builtins.str, typing.Any]]],
    subject_name_flags: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.SubjectNameFlagsV2Property, typing.Dict[builtins.str, typing.Any]]],
    superseded_templates: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac224c6e1a1e0bf613c6d1fe4773237be6044141e87435ae036c086e9bec9e33(
    *,
    certificate_validity: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.CertificateValidityProperty, typing.Dict[builtins.str, typing.Any]]],
    enrollment_flags: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.EnrollmentFlagsV3Property, typing.Dict[builtins.str, typing.Any]]],
    extensions: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.ExtensionsV3Property, typing.Dict[builtins.str, typing.Any]]],
    general_flags: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.GeneralFlagsV3Property, typing.Dict[builtins.str, typing.Any]]],
    hash_algorithm: builtins.str,
    private_key_attributes: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.PrivateKeyAttributesV3Property, typing.Dict[builtins.str, typing.Any]]],
    private_key_flags: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.PrivateKeyFlagsV3Property, typing.Dict[builtins.str, typing.Any]]],
    subject_name_flags: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.SubjectNameFlagsV3Property, typing.Dict[builtins.str, typing.Any]]],
    superseded_templates: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6104d8117de99af2149797a9c5cce3e3eb500e8f80d02ab1eac853d1168121c(
    *,
    certificate_validity: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.CertificateValidityProperty, typing.Dict[builtins.str, typing.Any]]],
    enrollment_flags: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.EnrollmentFlagsV4Property, typing.Dict[builtins.str, typing.Any]]],
    extensions: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.ExtensionsV4Property, typing.Dict[builtins.str, typing.Any]]],
    general_flags: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.GeneralFlagsV4Property, typing.Dict[builtins.str, typing.Any]]],
    private_key_attributes: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.PrivateKeyAttributesV4Property, typing.Dict[builtins.str, typing.Any]]],
    private_key_flags: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.PrivateKeyFlagsV4Property, typing.Dict[builtins.str, typing.Any]]],
    subject_name_flags: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.SubjectNameFlagsV4Property, typing.Dict[builtins.str, typing.Any]]],
    hash_algorithm: typing.Optional[builtins.str] = None,
    superseded_templates: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b7fd6091b8198bbe84b2f3027ec7cb8b9e3a8a5f69f78123238e5a3c22ee1ab(
    *,
    period: jsii.Number,
    period_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3afc1d4e6fd3841e33fcac8256963308de41afb74b2ac0fec481a86647067ec3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_rights: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplateGroupAccessControlEntry.AccessRightsProperty, typing.Dict[builtins.str, typing.Any]]],
    group_display_name: builtins.str,
    group_security_identifier: typing.Optional[builtins.str] = None,
    template_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2237339544790e2b019a0bf7fd86dfeab241882c8d4366e39039898b39c99ec6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71d54f04eb15c1354088f2337813be59d6ed5aff5bea943a3e810da7621b06c4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__186451b885ce1f5d39a9062a1daec093b87a1acb9aaeaab87a9c26d0732b7475(
    value: typing.Union[_IResolvable_da3f097b, CfnTemplateGroupAccessControlEntry.AccessRightsProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba2097b96364b1f0a4e58b04aa0cbb6cc515a5f811754f986deed65990eb077e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76b47557e0c980e45e43e15cd1f957c409b393473a036f0ae581dd1b8c6552b0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67cb0b070afb7e27a3030dfbdcd7496f1c3ebc2240fb6ab131af4439b7c6e156(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb1f4cfd72a22034fea283dd1de5d715f9b63f5e79755751a507a06a12025b82(
    *,
    auto_enroll: typing.Optional[builtins.str] = None,
    enroll: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e09aa5b6a189208934626d51a2a4ce72a03a91c1e114f462f32017df55c81f41(
    *,
    access_rights: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplateGroupAccessControlEntry.AccessRightsProperty, typing.Dict[builtins.str, typing.Any]]],
    group_display_name: builtins.str,
    group_security_identifier: typing.Optional[builtins.str] = None,
    template_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaedf159635a05945c9190de39c64b80921762454b586cb04745b2201ee34048(
    *,
    connector_arn: builtins.str,
    definition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.TemplateDefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    reenroll_all_certificate_holders: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
