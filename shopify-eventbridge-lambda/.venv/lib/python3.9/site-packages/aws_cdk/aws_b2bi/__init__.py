'''
# AWS::B2BI Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_b2bi as b2bi
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for B2BI construct libraries](https://constructs.dev/search?q=b2bi)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::B2BI resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_B2BI.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::B2BI](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_B2BI.html).

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
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnCapability(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_b2bi.CfnCapability",
):
    '''Instantiates a capability based on the specified parameters.

    A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-capability.html
    :cloudformationResource: AWS::B2BI::Capability
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_b2bi as b2bi
        
        cfn_capability = b2bi.CfnCapability(self, "MyCfnCapability",
            configuration=b2bi.CfnCapability.CapabilityConfigurationProperty(
                edi=b2bi.CfnCapability.EdiConfigurationProperty(
                    input_location=b2bi.CfnCapability.S3LocationProperty(
                        bucket_name="bucketName",
                        key="key"
                    ),
                    output_location=b2bi.CfnCapability.S3LocationProperty(
                        bucket_name="bucketName",
                        key="key"
                    ),
                    transformer_id="transformerId",
                    type=b2bi.CfnCapability.EdiTypeProperty(
                        x12_details=b2bi.CfnCapability.X12DetailsProperty(
                            transaction_set="transactionSet",
                            version="version"
                        )
                    )
                )
            ),
            name="name",
            type="type",
        
            # the properties below are optional
            instructions_documents=[b2bi.CfnCapability.S3LocationProperty(
                bucket_name="bucketName",
                key="key"
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
        configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCapability.CapabilityConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        type: builtins.str,
        instructions_documents: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCapability.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param configuration: Specifies a structure that contains the details for a capability.
        :param name: The display name of the capability.
        :param type: Returns the type of the capability. Currently, only ``edi`` is supported.
        :param instructions_documents: Specifies one or more locations in Amazon S3, each specifying an EDI document that can be used with this capability. Each item contains the name of the bucket and the key, to identify the document's location.
        :param tags: Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e2c877d8f658a8bd5b2b87fa89276114a47d5d48d6051351c42b159c7c68d05)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCapabilityProps(
            configuration=configuration,
            name=name,
            type=type,
            instructions_documents=instructions_documents,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69250f68db11c0c5d1b5dc6e2fd42eb03c44b04345584670f06ca66a9283eb35)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e7a0734db8cefbd4089ea9d0b9242a32f9ce5d439e96d8bf60ea3bf4754e3a55)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCapabilityArn")
    def attr_capability_arn(self) -> builtins.str:
        '''Returns an Amazon Resource Name (ARN) for a specific AWS resource, such as a capability, partnership, profile, or transformer.

        :cloudformationAttribute: CapabilityArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCapabilityArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCapabilityId")
    def attr_capability_id(self) -> builtins.str:
        '''Returns a system-assigned unique identifier for the capability.

        :cloudformationAttribute: CapabilityId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCapabilityId"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''Returns a timestamp for creation date and time of the capability.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrModifiedAt")
    def attr_modified_at(self) -> builtins.str:
        '''Returns a timestamp that identifies the most recent date and time that the capability was modified.

        :cloudformationAttribute: ModifiedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModifiedAt"))

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
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnCapability.CapabilityConfigurationProperty"]:
        '''Specifies a structure that contains the details for a capability.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCapability.CapabilityConfigurationProperty"], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnCapability.CapabilityConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e6a4e9debdcf2674a26e8ca0b9f4a771680d6f10a5d05a55ab8bc8c5063b78a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The display name of the capability.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__149152bfddb988a9aebbfe4cc00f98c6da302293c4bccdb6a2521efdcc265cad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''Returns the type of the capability.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0ac989543b8899d87e7022c05ecf79b8ac846fbb7cbefb25e6bf8a03d5b52da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="instructionsDocuments")
    def instructions_documents(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCapability.S3LocationProperty"]]]]:
        '''Specifies one or more locations in Amazon S3, each specifying an EDI document that can be used with this capability.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCapability.S3LocationProperty"]]]], jsii.get(self, "instructionsDocuments"))

    @instructions_documents.setter
    def instructions_documents(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCapability.S3LocationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__933e64c6fb43bdf92fe13796dc8381041bc9d46c8db437f72d8df9acf46d8ef9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instructionsDocuments", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9706dcfa23b620c2db12e1df4414f3a9f0b63bdbd7e3a8ac3944f66549703153)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnCapability.CapabilityConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"edi": "edi"},
    )
    class CapabilityConfigurationProperty:
        def __init__(
            self,
            *,
            edi: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCapability.EdiConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A capability object.

            Currently, only EDI (electronic data interchange) capabilities are supported. A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.

            :param edi: An EDI (electronic data interchange) configuration object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-capabilityconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                capability_configuration_property = b2bi.CfnCapability.CapabilityConfigurationProperty(
                    edi=b2bi.CfnCapability.EdiConfigurationProperty(
                        input_location=b2bi.CfnCapability.S3LocationProperty(
                            bucket_name="bucketName",
                            key="key"
                        ),
                        output_location=b2bi.CfnCapability.S3LocationProperty(
                            bucket_name="bucketName",
                            key="key"
                        ),
                        transformer_id="transformerId",
                        type=b2bi.CfnCapability.EdiTypeProperty(
                            x12_details=b2bi.CfnCapability.X12DetailsProperty(
                                transaction_set="transactionSet",
                                version="version"
                            )
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b39bfeb55ed086d5de5f443fd847773c175cdd988755a308ee0889c0b428322e)
                check_type(argname="argument edi", value=edi, expected_type=type_hints["edi"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "edi": edi,
            }

        @builtins.property
        def edi(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCapability.EdiConfigurationProperty"]:
            '''An EDI (electronic data interchange) configuration object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-capabilityconfiguration.html#cfn-b2bi-capability-capabilityconfiguration-edi
            '''
            result = self._values.get("edi")
            assert result is not None, "Required property 'edi' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCapability.EdiConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CapabilityConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnCapability.EdiConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "input_location": "inputLocation",
            "output_location": "outputLocation",
            "transformer_id": "transformerId",
            "type": "type",
        },
    )
    class EdiConfigurationProperty:
        def __init__(
            self,
            *,
            input_location: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCapability.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]],
            output_location: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCapability.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]],
            transformer_id: builtins.str,
            type: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCapability.EdiTypeProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Specifies the details for the EDI (electronic data interchange) transformation.

            :param input_location: Contains the Amazon S3 bucket and prefix for the location of the input file, which is contained in an ``S3Location`` object.
            :param output_location: Contains the Amazon S3 bucket and prefix for the location of the output file, which is contained in an ``S3Location`` object.
            :param transformer_id: Returns the system-assigned unique identifier for the transformer.
            :param type: Returns the type of the capability. Currently, only ``edi`` is supported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-ediconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                edi_configuration_property = b2bi.CfnCapability.EdiConfigurationProperty(
                    input_location=b2bi.CfnCapability.S3LocationProperty(
                        bucket_name="bucketName",
                        key="key"
                    ),
                    output_location=b2bi.CfnCapability.S3LocationProperty(
                        bucket_name="bucketName",
                        key="key"
                    ),
                    transformer_id="transformerId",
                    type=b2bi.CfnCapability.EdiTypeProperty(
                        x12_details=b2bi.CfnCapability.X12DetailsProperty(
                            transaction_set="transactionSet",
                            version="version"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6057bec99d8a1adeb15f82ebd6a5c206f528d80ccf6eaebcc8e44d83d415ec72)
                check_type(argname="argument input_location", value=input_location, expected_type=type_hints["input_location"])
                check_type(argname="argument output_location", value=output_location, expected_type=type_hints["output_location"])
                check_type(argname="argument transformer_id", value=transformer_id, expected_type=type_hints["transformer_id"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "input_location": input_location,
                "output_location": output_location,
                "transformer_id": transformer_id,
                "type": type,
            }

        @builtins.property
        def input_location(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCapability.S3LocationProperty"]:
            '''Contains the Amazon S3 bucket and prefix for the location of the input file, which is contained in an ``S3Location`` object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-ediconfiguration.html#cfn-b2bi-capability-ediconfiguration-inputlocation
            '''
            result = self._values.get("input_location")
            assert result is not None, "Required property 'input_location' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCapability.S3LocationProperty"], result)

        @builtins.property
        def output_location(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCapability.S3LocationProperty"]:
            '''Contains the Amazon S3 bucket and prefix for the location of the output file, which is contained in an ``S3Location`` object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-ediconfiguration.html#cfn-b2bi-capability-ediconfiguration-outputlocation
            '''
            result = self._values.get("output_location")
            assert result is not None, "Required property 'output_location' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCapability.S3LocationProperty"], result)

        @builtins.property
        def transformer_id(self) -> builtins.str:
            '''Returns the system-assigned unique identifier for the transformer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-ediconfiguration.html#cfn-b2bi-capability-ediconfiguration-transformerid
            '''
            result = self._values.get("transformer_id")
            assert result is not None, "Required property 'transformer_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCapability.EdiTypeProperty"]:
            '''Returns the type of the capability.

            Currently, only ``edi`` is supported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-ediconfiguration.html#cfn-b2bi-capability-ediconfiguration-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCapability.EdiTypeProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EdiConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnCapability.EdiTypeProperty",
        jsii_struct_bases=[],
        name_mapping={"x12_details": "x12Details"},
    )
    class EdiTypeProperty:
        def __init__(
            self,
            *,
            x12_details: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCapability.X12DetailsProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Specifies the details for the EDI standard that is being used for the transformer.

            Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.

            :param x12_details: Returns the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-editype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                edi_type_property = b2bi.CfnCapability.EdiTypeProperty(
                    x12_details=b2bi.CfnCapability.X12DetailsProperty(
                        transaction_set="transactionSet",
                        version="version"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a9ca50562e4e831dbcf7fdb06d87922ec9144632d5572bc4430820884ab15edb)
                check_type(argname="argument x12_details", value=x12_details, expected_type=type_hints["x12_details"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "x12_details": x12_details,
            }

        @builtins.property
        def x12_details(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCapability.X12DetailsProperty"]:
            '''Returns the details for the EDI standard that is being used for the transformer.

            Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-editype.html#cfn-b2bi-capability-editype-x12details
            '''
            result = self._values.get("x12_details")
            assert result is not None, "Required property 'x12_details' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCapability.X12DetailsProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EdiTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnCapability.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_name": "bucketName", "key": "key"},
    )
    class S3LocationProperty:
        def __init__(
            self,
            *,
            bucket_name: typing.Optional[builtins.str] = None,
            key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the details for the Amazon S3 file location that is being used with AWS B2BI Data Interchange.

            File locations in Amazon S3 are identified using a combination of the bucket and key.

            :param bucket_name: Specifies the name of the Amazon S3 bucket.
            :param key: Specifies the Amazon S3 key for the file location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                s3_location_property = b2bi.CfnCapability.S3LocationProperty(
                    bucket_name="bucketName",
                    key="key"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aca06398ec10ba74b5ba2cf86fa1032b9983a30858a85eb04ecadf48a95e5056)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bucket_name is not None:
                self._values["bucket_name"] = bucket_name
            if key is not None:
                self._values["key"] = key

        @builtins.property
        def bucket_name(self) -> typing.Optional[builtins.str]:
            '''Specifies the name of the Amazon S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-s3location.html#cfn-b2bi-capability-s3location-bucketname
            '''
            result = self._values.get("bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''Specifies the Amazon S3 key for the file location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-s3location.html#cfn-b2bi-capability-s3location-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnCapability.X12DetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"transaction_set": "transactionSet", "version": "version"},
    )
    class X12DetailsProperty:
        def __init__(
            self,
            *,
            transaction_set: typing.Optional[builtins.str] = None,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param transaction_set: Returns an enumerated type where each value identifies an X12 transaction set. Transaction sets are maintained by the X12 Accredited Standards Committee.
            :param version: Returns the version to use for the specified X12 transaction set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-x12details.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                x12_details_property = b2bi.CfnCapability.X12DetailsProperty(
                    transaction_set="transactionSet",
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7a92fd26779dc45009be0b9ca0aefb7b988fae928b06b6b46f41995a7bd338e7)
                check_type(argname="argument transaction_set", value=transaction_set, expected_type=type_hints["transaction_set"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if transaction_set is not None:
                self._values["transaction_set"] = transaction_set
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def transaction_set(self) -> typing.Optional[builtins.str]:
            '''Returns an enumerated type where each value identifies an X12 transaction set.

            Transaction sets are maintained by the X12 Accredited Standards Committee.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-x12details.html#cfn-b2bi-capability-x12details-transactionset
            '''
            result = self._values.get("transaction_set")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''Returns the version to use for the specified X12 transaction set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-capability-x12details.html#cfn-b2bi-capability-x12details-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "X12DetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_b2bi.CfnCapabilityProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration": "configuration",
        "name": "name",
        "type": "type",
        "instructions_documents": "instructionsDocuments",
        "tags": "tags",
    },
)
class CfnCapabilityProps:
    def __init__(
        self,
        *,
        configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapability.CapabilityConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        type: builtins.str,
        instructions_documents: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapability.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCapability``.

        :param configuration: Specifies a structure that contains the details for a capability.
        :param name: The display name of the capability.
        :param type: Returns the type of the capability. Currently, only ``edi`` is supported.
        :param instructions_documents: Specifies one or more locations in Amazon S3, each specifying an EDI document that can be used with this capability. Each item contains the name of the bucket and the key, to identify the document's location.
        :param tags: Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-capability.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_b2bi as b2bi
            
            cfn_capability_props = b2bi.CfnCapabilityProps(
                configuration=b2bi.CfnCapability.CapabilityConfigurationProperty(
                    edi=b2bi.CfnCapability.EdiConfigurationProperty(
                        input_location=b2bi.CfnCapability.S3LocationProperty(
                            bucket_name="bucketName",
                            key="key"
                        ),
                        output_location=b2bi.CfnCapability.S3LocationProperty(
                            bucket_name="bucketName",
                            key="key"
                        ),
                        transformer_id="transformerId",
                        type=b2bi.CfnCapability.EdiTypeProperty(
                            x12_details=b2bi.CfnCapability.X12DetailsProperty(
                                transaction_set="transactionSet",
                                version="version"
                            )
                        )
                    )
                ),
                name="name",
                type="type",
            
                # the properties below are optional
                instructions_documents=[b2bi.CfnCapability.S3LocationProperty(
                    bucket_name="bucketName",
                    key="key"
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83b1800b6ac31ea75ae49999ff7054acf5205e3155bfc92964d45204eac123bb)
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument instructions_documents", value=instructions_documents, expected_type=type_hints["instructions_documents"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration": configuration,
            "name": name,
            "type": type,
        }
        if instructions_documents is not None:
            self._values["instructions_documents"] = instructions_documents
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnCapability.CapabilityConfigurationProperty]:
        '''Specifies a structure that contains the details for a capability.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-capability.html#cfn-b2bi-capability-configuration
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnCapability.CapabilityConfigurationProperty], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The display name of the capability.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-capability.html#cfn-b2bi-capability-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Returns the type of the capability.

        Currently, only ``edi`` is supported.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-capability.html#cfn-b2bi-capability-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instructions_documents(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCapability.S3LocationProperty]]]]:
        '''Specifies one or more locations in Amazon S3, each specifying an EDI document that can be used with this capability.

        Each item contains the name of the bucket and the key, to identify the document's location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-capability.html#cfn-b2bi-capability-instructionsdocuments
        '''
        result = self._values.get("instructions_documents")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCapability.S3LocationProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type.

        You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-capability.html#cfn-b2bi-capability-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCapabilityProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnPartnership(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_b2bi.CfnPartnership",
):
    '''Creates a partnership between a customer and a trading partner, based on the supplied parameters.

    A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-partnership.html
    :cloudformationResource: AWS::B2BI::Partnership
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_b2bi as b2bi
        
        cfn_partnership = b2bi.CfnPartnership(self, "MyCfnPartnership",
            email="email",
            name="name",
            profile_id="profileId",
        
            # the properties below are optional
            capabilities=["capabilities"],
            phone="phone",
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
        email: builtins.str,
        name: builtins.str,
        profile_id: builtins.str,
        capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        phone: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param email: 
        :param name: Returns the name of the partnership.
        :param profile_id: Returns the unique, system-generated identifier for the profile connected to this partnership.
        :param capabilities: Returns one or more capabilities associated with this partnership.
        :param phone: 
        :param tags: A key-value pair for a specific partnership. Tags are metadata that you can use to search for and group capabilities for various purposes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__187ce4b824b0d27162e457adfee9761451ebc9ba1fbb31b215de741e20aea463)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPartnershipProps(
            email=email,
            name=name,
            profile_id=profile_id,
            capabilities=capabilities,
            phone=phone,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d250a045aef9262deb5ac9bdfc02b08a37a777ba8e105b1406ebfad2ee8edc9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__97e66f59482a5e62e1d52e1f96109cae79dc6c60b4b84b9ac971718f61abed32)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''Returns a timestamp for creation date and time of the partnership.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrModifiedAt")
    def attr_modified_at(self) -> builtins.str:
        '''Returns a timestamp that identifies the most recent date and time that the partnership was modified.

        :cloudformationAttribute: ModifiedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModifiedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrPartnershipArn")
    def attr_partnership_arn(self) -> builtins.str:
        '''Returns an Amazon Resource Name (ARN) for a specific AWS resource, such as a capability, partnership, profile, or transformer.

        :cloudformationAttribute: PartnershipArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPartnershipArn"))

    @builtins.property
    @jsii.member(jsii_name="attrPartnershipId")
    def attr_partnership_id(self) -> builtins.str:
        '''Returns the unique, system-generated identifier for a partnership.

        :cloudformationAttribute: PartnershipId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPartnershipId"))

    @builtins.property
    @jsii.member(jsii_name="attrTradingPartnerId")
    def attr_trading_partner_id(self) -> builtins.str:
        '''Returns the unique, system-generated identifier for a trading partner.

        :cloudformationAttribute: TradingPartnerId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTradingPartnerId"))

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
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2873a98dfd303be4e91fec1a674c6ab1a7382e5563610406e047403b795f1a06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''Returns the name of the partnership.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2391403bfc3a496d7ff98fb633ece3257a09478e6bed5d4c1c2ec23cd35687c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="profileId")
    def profile_id(self) -> builtins.str:
        '''Returns the unique, system-generated identifier for the profile connected to this partnership.'''
        return typing.cast(builtins.str, jsii.get(self, "profileId"))

    @profile_id.setter
    def profile_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__126b2c043f2647e2a052eca52ec8432ea60287721a3e645fe4dd65583feb42de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profileId", value)

    @builtins.property
    @jsii.member(jsii_name="capabilities")
    def capabilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Returns one or more capabilities associated with this partnership.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "capabilities"))

    @capabilities.setter
    def capabilities(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0980f94d13e92ad52bd4f6a10906045804439d25bf3126b627f3a97eb79eb594)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capabilities", value)

    @builtins.property
    @jsii.member(jsii_name="phone")
    def phone(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "phone"))

    @phone.setter
    def phone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5555f48f20bc825c44c857244fae3207c272ec76cbe060a463105d2c86113010)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phone", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A key-value pair for a specific partnership.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc0c0a6e8431d11899a318046b450bc4efc00486d9f20286940067c7fa335411)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_b2bi.CfnPartnershipProps",
    jsii_struct_bases=[],
    name_mapping={
        "email": "email",
        "name": "name",
        "profile_id": "profileId",
        "capabilities": "capabilities",
        "phone": "phone",
        "tags": "tags",
    },
)
class CfnPartnershipProps:
    def __init__(
        self,
        *,
        email: builtins.str,
        name: builtins.str,
        profile_id: builtins.str,
        capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        phone: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPartnership``.

        :param email: 
        :param name: Returns the name of the partnership.
        :param profile_id: Returns the unique, system-generated identifier for the profile connected to this partnership.
        :param capabilities: Returns one or more capabilities associated with this partnership.
        :param phone: 
        :param tags: A key-value pair for a specific partnership. Tags are metadata that you can use to search for and group capabilities for various purposes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-partnership.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_b2bi as b2bi
            
            cfn_partnership_props = b2bi.CfnPartnershipProps(
                email="email",
                name="name",
                profile_id="profileId",
            
                # the properties below are optional
                capabilities=["capabilities"],
                phone="phone",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18d814bec885d4c9defe3c391c4892f53df8f0ca2dd0011baaccd4959105a243)
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument profile_id", value=profile_id, expected_type=type_hints["profile_id"])
            check_type(argname="argument capabilities", value=capabilities, expected_type=type_hints["capabilities"])
            check_type(argname="argument phone", value=phone, expected_type=type_hints["phone"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "email": email,
            "name": name,
            "profile_id": profile_id,
        }
        if capabilities is not None:
            self._values["capabilities"] = capabilities
        if phone is not None:
            self._values["phone"] = phone
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def email(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-partnership.html#cfn-b2bi-partnership-email
        '''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Returns the name of the partnership.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-partnership.html#cfn-b2bi-partnership-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profile_id(self) -> builtins.str:
        '''Returns the unique, system-generated identifier for the profile connected to this partnership.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-partnership.html#cfn-b2bi-partnership-profileid
        '''
        result = self._values.get("profile_id")
        assert result is not None, "Required property 'profile_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capabilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Returns one or more capabilities associated with this partnership.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-partnership.html#cfn-b2bi-partnership-capabilities
        '''
        result = self._values.get("capabilities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def phone(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-partnership.html#cfn-b2bi-partnership-phone
        '''
        result = self._values.get("phone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A key-value pair for a specific partnership.

        Tags are metadata that you can use to search for and group capabilities for various purposes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-partnership.html#cfn-b2bi-partnership-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPartnershipProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_b2bi.CfnProfile",
):
    '''Creates a customer profile.

    You can have up to five customer profiles, each representing a distinct private network. A profile is the mechanism used to create the concept of a private network.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-profile.html
    :cloudformationResource: AWS::B2BI::Profile
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_b2bi as b2bi
        
        cfn_profile = b2bi.CfnProfile(self, "MyCfnProfile",
            business_name="businessName",
            logging="logging",
            name="name",
            phone="phone",
        
            # the properties below are optional
            email="email",
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
        business_name: builtins.str,
        logging: builtins.str,
        name: builtins.str,
        phone: builtins.str,
        email: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param business_name: Returns the name for the business associated with this profile.
        :param logging: Specifies whether or not logging is enabled for this profile.
        :param name: Returns the display name for profile.
        :param phone: 
        :param email: 
        :param tags: A key-value pair for a specific profile. Tags are metadata that you can use to search for and group capabilities for various purposes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e54fea50428e19dd273372ef5650a89d4610c6422804677c9be788a76aadf8a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProfileProps(
            business_name=business_name,
            logging=logging,
            name=name,
            phone=phone,
            email=email,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5271088abc585a3db11af1eacb47274605ad9acc14f75da9da9239d3a3697541)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a829f83cb367edec2f2e051795937696b3dcb1d1ab356574e9c6ad4badf3ce17)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''Returns the timestamp for creation date and time of the profile.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLogGroupName")
    def attr_log_group_name(self) -> builtins.str:
        '''Returns the name of the logging group.

        :cloudformationAttribute: LogGroupName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLogGroupName"))

    @builtins.property
    @jsii.member(jsii_name="attrModifiedAt")
    def attr_modified_at(self) -> builtins.str:
        '''Returns the timestamp that identifies the most recent date and time that the profile was modified.

        :cloudformationAttribute: ModifiedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModifiedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrProfileArn")
    def attr_profile_arn(self) -> builtins.str:
        '''Returns an Amazon Resource Name (ARN) for the profile.

        :cloudformationAttribute: ProfileArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProfileArn"))

    @builtins.property
    @jsii.member(jsii_name="attrProfileId")
    def attr_profile_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: ProfileId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProfileId"))

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
    @jsii.member(jsii_name="businessName")
    def business_name(self) -> builtins.str:
        '''Returns the name for the business associated with this profile.'''
        return typing.cast(builtins.str, jsii.get(self, "businessName"))

    @business_name.setter
    def business_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__504646617c098f5bad7128cc7a515f70f2c86e5d34b43f63aa27a2ad543b4e01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "businessName", value)

    @builtins.property
    @jsii.member(jsii_name="logging")
    def logging(self) -> builtins.str:
        '''Specifies whether or not logging is enabled for this profile.'''
        return typing.cast(builtins.str, jsii.get(self, "logging"))

    @logging.setter
    def logging(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__127f59e663824bfd0cc39ab3ed6020d41d54a2b30e31fc71b46ce48e510ff366)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logging", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''Returns the display name for profile.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__978cb41c2583c736d786df05be25dfaaa254556b513af9850f95c4f5f7999380)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="phone")
    def phone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "phone"))

    @phone.setter
    def phone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5aa6ce25bb49d6882927fd231d1e147e27ba9905d54248c88718171a9e0fdd5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phone", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "email"))

    @email.setter
    def email(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0936f8c78a965c88641d39b7a6e2d4e7ad2bd7f48de6870270d842ba0ccdc34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A key-value pair for a specific profile.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b70ada00d6d35989093b4f1b185f6deaa1f9c1404a82bc792e6f4dc53684b45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_b2bi.CfnProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "business_name": "businessName",
        "logging": "logging",
        "name": "name",
        "phone": "phone",
        "email": "email",
        "tags": "tags",
    },
)
class CfnProfileProps:
    def __init__(
        self,
        *,
        business_name: builtins.str,
        logging: builtins.str,
        name: builtins.str,
        phone: builtins.str,
        email: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnProfile``.

        :param business_name: Returns the name for the business associated with this profile.
        :param logging: Specifies whether or not logging is enabled for this profile.
        :param name: Returns the display name for profile.
        :param phone: 
        :param email: 
        :param tags: A key-value pair for a specific profile. Tags are metadata that you can use to search for and group capabilities for various purposes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-profile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_b2bi as b2bi
            
            cfn_profile_props = b2bi.CfnProfileProps(
                business_name="businessName",
                logging="logging",
                name="name",
                phone="phone",
            
                # the properties below are optional
                email="email",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85c233c5836835af7c38d9812c75649ec2fc027fa20a2af7be215694f4d322e4)
            check_type(argname="argument business_name", value=business_name, expected_type=type_hints["business_name"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument phone", value=phone, expected_type=type_hints["phone"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "business_name": business_name,
            "logging": logging,
            "name": name,
            "phone": phone,
        }
        if email is not None:
            self._values["email"] = email
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def business_name(self) -> builtins.str:
        '''Returns the name for the business associated with this profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-profile.html#cfn-b2bi-profile-businessname
        '''
        result = self._values.get("business_name")
        assert result is not None, "Required property 'business_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def logging(self) -> builtins.str:
        '''Specifies whether or not logging is enabled for this profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-profile.html#cfn-b2bi-profile-logging
        '''
        result = self._values.get("logging")
        assert result is not None, "Required property 'logging' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Returns the display name for profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-profile.html#cfn-b2bi-profile-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def phone(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-profile.html#cfn-b2bi-profile-phone
        '''
        result = self._values.get("phone")
        assert result is not None, "Required property 'phone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def email(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-profile.html#cfn-b2bi-profile-email
        '''
        result = self._values.get("email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A key-value pair for a specific profile.

        Tags are metadata that you can use to search for and group capabilities for various purposes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-profile.html#cfn-b2bi-profile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnTransformer(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_b2bi.CfnTransformer",
):
    '''Creates a transformer.

    A transformer describes how to process the incoming EDI documents and extract the necessary information to the output file.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-transformer.html
    :cloudformationResource: AWS::B2BI::Transformer
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_b2bi as b2bi
        
        cfn_transformer = b2bi.CfnTransformer(self, "MyCfnTransformer",
            edi_type=b2bi.CfnTransformer.EdiTypeProperty(
                x12_details=b2bi.CfnTransformer.X12DetailsProperty(
                    transaction_set="transactionSet",
                    version="version"
                )
            ),
            file_format="fileFormat",
            mapping_template="mappingTemplate",
            name="name",
            status="status",
        
            # the properties below are optional
            sample_document="sampleDocument",
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
        edi_type: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.EdiTypeProperty", typing.Dict[builtins.str, typing.Any]]],
        file_format: builtins.str,
        mapping_template: builtins.str,
        name: builtins.str,
        status: builtins.str,
        sample_document: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param edi_type: Returns the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.
        :param file_format: Returns that the currently supported file formats for EDI transformations are ``JSON`` and ``XML`` .
        :param mapping_template: Returns a sample EDI document that is used by a transformer as a guide for processing the EDI data.
        :param name: Returns the descriptive name for the transformer.
        :param status: Returns the state of the newly created transformer. The transformer can be either ``active`` or ``inactive`` . For the transformer to be used in a capability, its status must ``active`` .
        :param sample_document: Returns a sample EDI document that is used by a transformer as a guide for processing the EDI data.
        :param tags: A key-value pair for a specific transformer. Tags are metadata that you can use to search for and group capabilities for various purposes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb0d6d0f8083b8bc38eb61c54d65c6e72d668ba067f31569d0213bf7dafff2c9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTransformerProps(
            edi_type=edi_type,
            file_format=file_format,
            mapping_template=mapping_template,
            name=name,
            status=status,
            sample_document=sample_document,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd0b05118fb2d551f3054a5c85d10fe283c5ca2b9e830ef5a31a1eb7e66fce63)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8de580bfd50f433c0cd75e13649e7f911981404484637058415a594dac3eea03)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''Returns a timestamp indicating when the transformer was created.

        For example, ``2023-07-20T19:58:44.624Z`` .

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrModifiedAt")
    def attr_modified_at(self) -> builtins.str:
        '''Returns a timestamp representing the date and time for the most recent change for the transformer object.

        :cloudformationAttribute: ModifiedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModifiedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrTransformerArn")
    def attr_transformer_arn(self) -> builtins.str:
        '''Returns an Amazon Resource Name (ARN) for a specific transformer.

        :cloudformationAttribute: TransformerArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTransformerArn"))

    @builtins.property
    @jsii.member(jsii_name="attrTransformerId")
    def attr_transformer_id(self) -> builtins.str:
        '''The system-assigned unique identifier for the transformer.

        :cloudformationAttribute: TransformerId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTransformerId"))

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
    @jsii.member(jsii_name="ediType")
    def edi_type(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnTransformer.EdiTypeProperty"]:
        '''Returns the details for the EDI standard that is being used for the transformer.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTransformer.EdiTypeProperty"], jsii.get(self, "ediType"))

    @edi_type.setter
    def edi_type(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnTransformer.EdiTypeProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e29c7d30dfbbc72fddf07313c1a9cb2eb14ed42c55e23bc13564603f6928f89c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ediType", value)

    @builtins.property
    @jsii.member(jsii_name="fileFormat")
    def file_format(self) -> builtins.str:
        '''Returns that the currently supported file formats for EDI transformations are ``JSON`` and ``XML`` .'''
        return typing.cast(builtins.str, jsii.get(self, "fileFormat"))

    @file_format.setter
    def file_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2fb21eeda84a5b3d95ee7d5d0e82a546522729b7fd5930fd6ed068055475615)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileFormat", value)

    @builtins.property
    @jsii.member(jsii_name="mappingTemplate")
    def mapping_template(self) -> builtins.str:
        '''Returns a sample EDI document that is used by a transformer as a guide for processing the EDI data.'''
        return typing.cast(builtins.str, jsii.get(self, "mappingTemplate"))

    @mapping_template.setter
    def mapping_template(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__685af615cb66c99ad9251a37e75e2851545a2603e7b07280b617d52d744fdf10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mappingTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''Returns the descriptive name for the transformer.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1302a1da7c175d27a541e2b1a5f25f80a4dac4f0a966ee8cddf6d1014ea81395)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        '''Returns the state of the newly created transformer.'''
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa8b2ecdc80ffc3d3b7ddf2cc4493b19df8fa02a3f0dbcf2ea74744b53c3b54c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="sampleDocument")
    def sample_document(self) -> typing.Optional[builtins.str]:
        '''Returns a sample EDI document that is used by a transformer as a guide for processing the EDI data.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sampleDocument"))

    @sample_document.setter
    def sample_document(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c2214b3717f190a30ff1cc1b45298208906824b8d93bfb181ad552ca17e7a7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sampleDocument", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A key-value pair for a specific transformer.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4ec179f77fa2da856518d97a9b83e88d0c96784ca483f80c070b398e5655b89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnTransformer.EdiTypeProperty",
        jsii_struct_bases=[],
        name_mapping={"x12_details": "x12Details"},
    )
    class EdiTypeProperty:
        def __init__(
            self,
            *,
            x12_details: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransformer.X12DetailsProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Specifies the details for the EDI standard that is being used for the transformer.

            Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.

            :param x12_details: Returns the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-editype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                edi_type_property = b2bi.CfnTransformer.EdiTypeProperty(
                    x12_details=b2bi.CfnTransformer.X12DetailsProperty(
                        transaction_set="transactionSet",
                        version="version"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0a90856b523d4a63e08c58604f08df0cd4ca6647b6d8b2bf4c0c6238831a179a)
                check_type(argname="argument x12_details", value=x12_details, expected_type=type_hints["x12_details"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "x12_details": x12_details,
            }

        @builtins.property
        def x12_details(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTransformer.X12DetailsProperty"]:
            '''Returns the details for the EDI standard that is being used for the transformer.

            Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-editype.html#cfn-b2bi-transformer-editype-x12details
            '''
            result = self._values.get("x12_details")
            assert result is not None, "Required property 'x12_details' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTransformer.X12DetailsProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EdiTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_b2bi.CfnTransformer.X12DetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"transaction_set": "transactionSet", "version": "version"},
    )
    class X12DetailsProperty:
        def __init__(
            self,
            *,
            transaction_set: typing.Optional[builtins.str] = None,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure that contains the X12 transaction set and version.

            The X12 structure is used when the system transforms an EDI (electronic data interchange) file.
            .. epigraph::

               If an EDI input file contains more than one transaction, each transaction must have the same transaction set and version, for example 214/4010. If not, the transformer cannot parse the file.

            :param transaction_set: Returns an enumerated type where each value identifies an X12 transaction set. Transaction sets are maintained by the X12 Accredited Standards Committee.
            :param version: Returns the version to use for the specified X12 transaction set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-x12details.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_b2bi as b2bi
                
                x12_details_property = b2bi.CfnTransformer.X12DetailsProperty(
                    transaction_set="transactionSet",
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6c52ecd7c7c399e4bebfaf5bf8793e65928fdad0c0133ff1ce55c05683b44ac7)
                check_type(argname="argument transaction_set", value=transaction_set, expected_type=type_hints["transaction_set"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if transaction_set is not None:
                self._values["transaction_set"] = transaction_set
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def transaction_set(self) -> typing.Optional[builtins.str]:
            '''Returns an enumerated type where each value identifies an X12 transaction set.

            Transaction sets are maintained by the X12 Accredited Standards Committee.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-x12details.html#cfn-b2bi-transformer-x12details-transactionset
            '''
            result = self._values.get("transaction_set")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''Returns the version to use for the specified X12 transaction set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-b2bi-transformer-x12details.html#cfn-b2bi-transformer-x12details-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "X12DetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_b2bi.CfnTransformerProps",
    jsii_struct_bases=[],
    name_mapping={
        "edi_type": "ediType",
        "file_format": "fileFormat",
        "mapping_template": "mappingTemplate",
        "name": "name",
        "status": "status",
        "sample_document": "sampleDocument",
        "tags": "tags",
    },
)
class CfnTransformerProps:
    def __init__(
        self,
        *,
        edi_type: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.EdiTypeProperty, typing.Dict[builtins.str, typing.Any]]],
        file_format: builtins.str,
        mapping_template: builtins.str,
        name: builtins.str,
        status: builtins.str,
        sample_document: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTransformer``.

        :param edi_type: Returns the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.
        :param file_format: Returns that the currently supported file formats for EDI transformations are ``JSON`` and ``XML`` .
        :param mapping_template: Returns a sample EDI document that is used by a transformer as a guide for processing the EDI data.
        :param name: Returns the descriptive name for the transformer.
        :param status: Returns the state of the newly created transformer. The transformer can be either ``active`` or ``inactive`` . For the transformer to be used in a capability, its status must ``active`` .
        :param sample_document: Returns a sample EDI document that is used by a transformer as a guide for processing the EDI data.
        :param tags: A key-value pair for a specific transformer. Tags are metadata that you can use to search for and group capabilities for various purposes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-transformer.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_b2bi as b2bi
            
            cfn_transformer_props = b2bi.CfnTransformerProps(
                edi_type=b2bi.CfnTransformer.EdiTypeProperty(
                    x12_details=b2bi.CfnTransformer.X12DetailsProperty(
                        transaction_set="transactionSet",
                        version="version"
                    )
                ),
                file_format="fileFormat",
                mapping_template="mappingTemplate",
                name="name",
                status="status",
            
                # the properties below are optional
                sample_document="sampleDocument",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69e342f03b6075725a81423ccb4db79ba04bb935c9a3fd129f49fd2954e7cc21)
            check_type(argname="argument edi_type", value=edi_type, expected_type=type_hints["edi_type"])
            check_type(argname="argument file_format", value=file_format, expected_type=type_hints["file_format"])
            check_type(argname="argument mapping_template", value=mapping_template, expected_type=type_hints["mapping_template"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument sample_document", value=sample_document, expected_type=type_hints["sample_document"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "edi_type": edi_type,
            "file_format": file_format,
            "mapping_template": mapping_template,
            "name": name,
            "status": status,
        }
        if sample_document is not None:
            self._values["sample_document"] = sample_document
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def edi_type(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnTransformer.EdiTypeProperty]:
        '''Returns the details for the EDI standard that is being used for the transformer.

        Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-transformer.html#cfn-b2bi-transformer-editype
        '''
        result = self._values.get("edi_type")
        assert result is not None, "Required property 'edi_type' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnTransformer.EdiTypeProperty], result)

    @builtins.property
    def file_format(self) -> builtins.str:
        '''Returns that the currently supported file formats for EDI transformations are ``JSON`` and ``XML`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-transformer.html#cfn-b2bi-transformer-fileformat
        '''
        result = self._values.get("file_format")
        assert result is not None, "Required property 'file_format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mapping_template(self) -> builtins.str:
        '''Returns a sample EDI document that is used by a transformer as a guide for processing the EDI data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-transformer.html#cfn-b2bi-transformer-mappingtemplate
        '''
        result = self._values.get("mapping_template")
        assert result is not None, "Required property 'mapping_template' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Returns the descriptive name for the transformer.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-transformer.html#cfn-b2bi-transformer-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status(self) -> builtins.str:
        '''Returns the state of the newly created transformer.

        The transformer can be either ``active`` or ``inactive`` . For the transformer to be used in a capability, its status must ``active`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-transformer.html#cfn-b2bi-transformer-status
        '''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sample_document(self) -> typing.Optional[builtins.str]:
        '''Returns a sample EDI document that is used by a transformer as a guide for processing the EDI data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-transformer.html#cfn-b2bi-transformer-sampledocument
        '''
        result = self._values.get("sample_document")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A key-value pair for a specific transformer.

        Tags are metadata that you can use to search for and group capabilities for various purposes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-b2bi-transformer.html#cfn-b2bi-transformer-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTransformerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCapability",
    "CfnCapabilityProps",
    "CfnPartnership",
    "CfnPartnershipProps",
    "CfnProfile",
    "CfnProfileProps",
    "CfnTransformer",
    "CfnTransformerProps",
]

publication.publish()

def _typecheckingstub__0e2c877d8f658a8bd5b2b87fa89276114a47d5d48d6051351c42b159c7c68d05(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapability.CapabilityConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    type: builtins.str,
    instructions_documents: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapability.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69250f68db11c0c5d1b5dc6e2fd42eb03c44b04345584670f06ca66a9283eb35(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7a0734db8cefbd4089ea9d0b9242a32f9ce5d439e96d8bf60ea3bf4754e3a55(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e6a4e9debdcf2674a26e8ca0b9f4a771680d6f10a5d05a55ab8bc8c5063b78a(
    value: typing.Union[_IResolvable_da3f097b, CfnCapability.CapabilityConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__149152bfddb988a9aebbfe4cc00f98c6da302293c4bccdb6a2521efdcc265cad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0ac989543b8899d87e7022c05ecf79b8ac846fbb7cbefb25e6bf8a03d5b52da(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__933e64c6fb43bdf92fe13796dc8381041bc9d46c8db437f72d8df9acf46d8ef9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCapability.S3LocationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9706dcfa23b620c2db12e1df4414f3a9f0b63bdbd7e3a8ac3944f66549703153(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b39bfeb55ed086d5de5f443fd847773c175cdd988755a308ee0889c0b428322e(
    *,
    edi: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapability.EdiConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6057bec99d8a1adeb15f82ebd6a5c206f528d80ccf6eaebcc8e44d83d415ec72(
    *,
    input_location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapability.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]],
    output_location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapability.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]],
    transformer_id: builtins.str,
    type: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapability.EdiTypeProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9ca50562e4e831dbcf7fdb06d87922ec9144632d5572bc4430820884ab15edb(
    *,
    x12_details: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapability.X12DetailsProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aca06398ec10ba74b5ba2cf86fa1032b9983a30858a85eb04ecadf48a95e5056(
    *,
    bucket_name: typing.Optional[builtins.str] = None,
    key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a92fd26779dc45009be0b9ca0aefb7b988fae928b06b6b46f41995a7bd338e7(
    *,
    transaction_set: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83b1800b6ac31ea75ae49999ff7054acf5205e3155bfc92964d45204eac123bb(
    *,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapability.CapabilityConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    type: builtins.str,
    instructions_documents: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCapability.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__187ce4b824b0d27162e457adfee9761451ebc9ba1fbb31b215de741e20aea463(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    email: builtins.str,
    name: builtins.str,
    profile_id: builtins.str,
    capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
    phone: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d250a045aef9262deb5ac9bdfc02b08a37a777ba8e105b1406ebfad2ee8edc9(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97e66f59482a5e62e1d52e1f96109cae79dc6c60b4b84b9ac971718f61abed32(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2873a98dfd303be4e91fec1a674c6ab1a7382e5563610406e047403b795f1a06(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2391403bfc3a496d7ff98fb633ece3257a09478e6bed5d4c1c2ec23cd35687c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__126b2c043f2647e2a052eca52ec8432ea60287721a3e645fe4dd65583feb42de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0980f94d13e92ad52bd4f6a10906045804439d25bf3126b627f3a97eb79eb594(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5555f48f20bc825c44c857244fae3207c272ec76cbe060a463105d2c86113010(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc0c0a6e8431d11899a318046b450bc4efc00486d9f20286940067c7fa335411(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18d814bec885d4c9defe3c391c4892f53df8f0ca2dd0011baaccd4959105a243(
    *,
    email: builtins.str,
    name: builtins.str,
    profile_id: builtins.str,
    capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
    phone: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e54fea50428e19dd273372ef5650a89d4610c6422804677c9be788a76aadf8a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    business_name: builtins.str,
    logging: builtins.str,
    name: builtins.str,
    phone: builtins.str,
    email: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5271088abc585a3db11af1eacb47274605ad9acc14f75da9da9239d3a3697541(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a829f83cb367edec2f2e051795937696b3dcb1d1ab356574e9c6ad4badf3ce17(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__504646617c098f5bad7128cc7a515f70f2c86e5d34b43f63aa27a2ad543b4e01(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__127f59e663824bfd0cc39ab3ed6020d41d54a2b30e31fc71b46ce48e510ff366(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__978cb41c2583c736d786df05be25dfaaa254556b513af9850f95c4f5f7999380(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aa6ce25bb49d6882927fd231d1e147e27ba9905d54248c88718171a9e0fdd5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0936f8c78a965c88641d39b7a6e2d4e7ad2bd7f48de6870270d842ba0ccdc34(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b70ada00d6d35989093b4f1b185f6deaa1f9c1404a82bc792e6f4dc53684b45(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85c233c5836835af7c38d9812c75649ec2fc027fa20a2af7be215694f4d322e4(
    *,
    business_name: builtins.str,
    logging: builtins.str,
    name: builtins.str,
    phone: builtins.str,
    email: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb0d6d0f8083b8bc38eb61c54d65c6e72d668ba067f31569d0213bf7dafff2c9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    edi_type: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.EdiTypeProperty, typing.Dict[builtins.str, typing.Any]]],
    file_format: builtins.str,
    mapping_template: builtins.str,
    name: builtins.str,
    status: builtins.str,
    sample_document: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd0b05118fb2d551f3054a5c85d10fe283c5ca2b9e830ef5a31a1eb7e66fce63(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8de580bfd50f433c0cd75e13649e7f911981404484637058415a594dac3eea03(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e29c7d30dfbbc72fddf07313c1a9cb2eb14ed42c55e23bc13564603f6928f89c(
    value: typing.Union[_IResolvable_da3f097b, CfnTransformer.EdiTypeProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2fb21eeda84a5b3d95ee7d5d0e82a546522729b7fd5930fd6ed068055475615(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__685af615cb66c99ad9251a37e75e2851545a2603e7b07280b617d52d744fdf10(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1302a1da7c175d27a541e2b1a5f25f80a4dac4f0a966ee8cddf6d1014ea81395(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa8b2ecdc80ffc3d3b7ddf2cc4493b19df8fa02a3f0dbcf2ea74744b53c3b54c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c2214b3717f190a30ff1cc1b45298208906824b8d93bfb181ad552ca17e7a7d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4ec179f77fa2da856518d97a9b83e88d0c96784ca483f80c070b398e5655b89(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a90856b523d4a63e08c58604f08df0cd4ca6647b6d8b2bf4c0c6238831a179a(
    *,
    x12_details: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.X12DetailsProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c52ecd7c7c399e4bebfaf5bf8793e65928fdad0c0133ff1ce55c05683b44ac7(
    *,
    transaction_set: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69e342f03b6075725a81423ccb4db79ba04bb935c9a3fd129f49fd2954e7cc21(
    *,
    edi_type: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransformer.EdiTypeProperty, typing.Dict[builtins.str, typing.Any]]],
    file_format: builtins.str,
    mapping_template: builtins.str,
    name: builtins.str,
    status: builtins.str,
    sample_document: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
