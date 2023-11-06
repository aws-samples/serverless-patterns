'''
# AWS::Wisdom Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_wisdom as wisdom
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Wisdom construct libraries](https://constructs.dev/search?q=wisdom)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Wisdom resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Wisdom.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Wisdom](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Wisdom.html).

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
class CfnAssistant(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAssistant",
):
    '''Specifies an Amazon Connect Wisdom assistant.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wisdom as wisdom
        
        cfn_assistant = wisdom.CfnAssistant(self, "MyCfnAssistant",
            name="name",
            type="type",
        
            # the properties below are optional
            description="description",
            server_side_encryption_configuration=wisdom.CfnAssistant.ServerSideEncryptionConfigurationProperty(
                kms_key_id="kmsKeyId"
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
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        server_side_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAssistant.ServerSideEncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the assistant.
        :param type: The type of assistant.
        :param description: The description of the assistant.
        :param server_side_encryption_configuration: The KMS key used for encryption.
        :param tags: The tags used to organize, track, or control access for this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8078b7e28a17a68ab6f3d362e7de3af6b6867207690b2b344e35797cd6569746)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAssistantProps(
            name=name,
            type=type,
            description=description,
            server_side_encryption_configuration=server_side_encryption_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67a0860b53a1867e3124a155db57aa1ab8bbb2d50c48a1553f8766101996d0b8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4a17095196842a083c7a71c961443f89f6d1dd766154e06248d10cdee66b0113)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAssistantArn")
    def attr_assistant_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the assistant.

        :cloudformationAttribute: AssistantArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssistantArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAssistantId")
    def attr_assistant_id(self) -> builtins.str:
        '''The ID of the Wisdom assistant.

        :cloudformationAttribute: AssistantId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssistantId"))

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
        '''The name of the assistant.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ded25c09bd072cbcb02cdfdf40580d154663664980378f96c5210edc137dd8c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of assistant.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c131b16ef6a21690f65d4e643bc0f04ea3e1fa9afd2bbf0e89a9bd4b96032657)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the assistant.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17115c2ceb35036c54e25dfa13fd4465303e5a759aae943761c84163427b74ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionConfiguration")
    def server_side_encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAssistant.ServerSideEncryptionConfigurationProperty"]]:
        '''The KMS key used for encryption.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAssistant.ServerSideEncryptionConfigurationProperty"]], jsii.get(self, "serverSideEncryptionConfiguration"))

    @server_side_encryption_configuration.setter
    def server_side_encryption_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAssistant.ServerSideEncryptionConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb8470e364668ea9060baa4a3306507e0ded02773f75cc435d33474d30577d1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverSideEncryptionConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a82c89946835215b7304a7033eacc23c202ee6ae8e17e73d0ba34f1dbaf1416)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAssistant.ServerSideEncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_key_id": "kmsKeyId"},
    )
    class ServerSideEncryptionConfigurationProperty:
        def __init__(self, *, kms_key_id: typing.Optional[builtins.str] = None) -> None:
            '''The KMS key used for encryption.

            :param kms_key_id: The KMS key . For information about valid ID values, see `Key identifiers (KeyId) <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id>`_ in the *AWS Key Management Service Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-assistant-serversideencryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                server_side_encryption_configuration_property = wisdom.CfnAssistant.ServerSideEncryptionConfigurationProperty(
                    kms_key_id="kmsKeyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fa78e1cc313485ba353b8f1dc8b01c69bcdd1c5bcecd204b9778596de1e4a07d)
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The KMS key .

            For information about valid ID values, see `Key identifiers (KeyId) <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id>`_ in the *AWS Key Management Service Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-assistant-serversideencryptionconfiguration.html#cfn-wisdom-assistant-serversideencryptionconfiguration-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServerSideEncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnAssistantAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAssistantAssociation",
):
    '''Specifies an association between an Amazon Connect Wisdom assistant and another resource.

    Currently, the only supported association is with a knowledge base. An assistant can have only a single association.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wisdom as wisdom
        
        cfn_assistant_association = wisdom.CfnAssistantAssociation(self, "MyCfnAssistantAssociation",
            assistant_id="assistantId",
            association=wisdom.CfnAssistantAssociation.AssociationDataProperty(
                knowledge_base_id="knowledgeBaseId"
            ),
            association_type="associationType",
        
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
        assistant_id: builtins.str,
        association: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAssistantAssociation.AssociationDataProperty", typing.Dict[builtins.str, typing.Any]]],
        association_type: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param assistant_id: The identifier of the Wisdom assistant.
        :param association: The identifier of the associated resource.
        :param association_type: The type of association.
        :param tags: The tags used to organize, track, or control access for this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17f6f8491bb7be7dab63c57bf64b65f643c4fece381b02f49002f796c7a8f0f9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAssistantAssociationProps(
            assistant_id=assistant_id,
            association=association,
            association_type=association_type,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a96af34ce4ed10cd5d626bf5df7799b86ca3023d4f6b302c0cdb51a0bdd1274)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e84fe37792368fc9821204b49ed0d6e13642f35bcdc7bb2676de0ee949767075)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAssistantArn")
    def attr_assistant_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Wisdom assistant.

        :cloudformationAttribute: AssistantArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssistantArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAssistantAssociationArn")
    def attr_assistant_association_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the assistant association.

        :cloudformationAttribute: AssistantAssociationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssistantAssociationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAssistantAssociationId")
    def attr_assistant_association_id(self) -> builtins.str:
        '''The ID of the association.

        :cloudformationAttribute: AssistantAssociationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssistantAssociationId"))

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
    @jsii.member(jsii_name="assistantId")
    def assistant_id(self) -> builtins.str:
        '''The identifier of the Wisdom assistant.'''
        return typing.cast(builtins.str, jsii.get(self, "assistantId"))

    @assistant_id.setter
    def assistant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c72c215a467df1527e01f95d41dc85287728a80fa94729b3ff14b2b1312fb30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assistantId", value)

    @builtins.property
    @jsii.member(jsii_name="association")
    def association(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnAssistantAssociation.AssociationDataProperty"]:
        '''The identifier of the associated resource.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAssistantAssociation.AssociationDataProperty"], jsii.get(self, "association"))

    @association.setter
    def association(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnAssistantAssociation.AssociationDataProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e46eeb6364ccf0b8f92618927437f56df6248417cb401c056b83fe5692feb0f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "association", value)

    @builtins.property
    @jsii.member(jsii_name="associationType")
    def association_type(self) -> builtins.str:
        '''The type of association.'''
        return typing.cast(builtins.str, jsii.get(self, "associationType"))

    @association_type.setter
    def association_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48fcb269f8dde8b147d1a0d7681e40817cb35b599f00a24aff263a84df4cea90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associationType", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea3d3cb4fe1048c256fc8719ac3d18f47cb21ef29730dd9d1f53a9304ccd4030)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnAssistantAssociation.AssociationDataProperty",
        jsii_struct_bases=[],
        name_mapping={"knowledge_base_id": "knowledgeBaseId"},
    )
    class AssociationDataProperty:
        def __init__(self, *, knowledge_base_id: builtins.str) -> None:
            '''A union type that currently has a single argument, which is the knowledge base ID.

            :param knowledge_base_id: The identifier of the knowledge base.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-assistantassociation-associationdata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                association_data_property = wisdom.CfnAssistantAssociation.AssociationDataProperty(
                    knowledge_base_id="knowledgeBaseId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f6ecf0cfb2eb97624a8ec4ab51e16f75cfa1a5397890274252a2621ff5ad378d)
                check_type(argname="argument knowledge_base_id", value=knowledge_base_id, expected_type=type_hints["knowledge_base_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "knowledge_base_id": knowledge_base_id,
            }

        @builtins.property
        def knowledge_base_id(self) -> builtins.str:
            '''The identifier of the knowledge base.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-assistantassociation-associationdata.html#cfn-wisdom-assistantassociation-associationdata-knowledgebaseid
            '''
            result = self._values.get("knowledge_base_id")
            assert result is not None, "Required property 'knowledge_base_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AssociationDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAssistantAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "assistant_id": "assistantId",
        "association": "association",
        "association_type": "associationType",
        "tags": "tags",
    },
)
class CfnAssistantAssociationProps:
    def __init__(
        self,
        *,
        assistant_id: builtins.str,
        association: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssistantAssociation.AssociationDataProperty, typing.Dict[builtins.str, typing.Any]]],
        association_type: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAssistantAssociation``.

        :param assistant_id: The identifier of the Wisdom assistant.
        :param association: The identifier of the associated resource.
        :param association_type: The type of association.
        :param tags: The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wisdom as wisdom
            
            cfn_assistant_association_props = wisdom.CfnAssistantAssociationProps(
                assistant_id="assistantId",
                association=wisdom.CfnAssistantAssociation.AssociationDataProperty(
                    knowledge_base_id="knowledgeBaseId"
                ),
                association_type="associationType",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__419e70156a249f4fa2bea77a71d532fe9a351e3d150b5939dc8455b174375514)
            check_type(argname="argument assistant_id", value=assistant_id, expected_type=type_hints["assistant_id"])
            check_type(argname="argument association", value=association, expected_type=type_hints["association"])
            check_type(argname="argument association_type", value=association_type, expected_type=type_hints["association_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "assistant_id": assistant_id,
            "association": association,
            "association_type": association_type,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def assistant_id(self) -> builtins.str:
        '''The identifier of the Wisdom assistant.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#cfn-wisdom-assistantassociation-assistantid
        '''
        result = self._values.get("assistant_id")
        assert result is not None, "Required property 'assistant_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def association(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnAssistantAssociation.AssociationDataProperty]:
        '''The identifier of the associated resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#cfn-wisdom-assistantassociation-association
        '''
        result = self._values.get("association")
        assert result is not None, "Required property 'association' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnAssistantAssociation.AssociationDataProperty], result)

    @builtins.property
    def association_type(self) -> builtins.str:
        '''The type of association.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#cfn-wisdom-assistantassociation-associationtype
        '''
        result = self._values.get("association_type")
        assert result is not None, "Required property 'association_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistantassociation.html#cfn-wisdom-assistantassociation-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssistantAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wisdom.CfnAssistantProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "type": "type",
        "description": "description",
        "server_side_encryption_configuration": "serverSideEncryptionConfiguration",
        "tags": "tags",
    },
)
class CfnAssistantProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        server_side_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssistant.ServerSideEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAssistant``.

        :param name: The name of the assistant.
        :param type: The type of assistant.
        :param description: The description of the assistant.
        :param server_side_encryption_configuration: The KMS key used for encryption.
        :param tags: The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wisdom as wisdom
            
            cfn_assistant_props = wisdom.CfnAssistantProps(
                name="name",
                type="type",
            
                # the properties below are optional
                description="description",
                server_side_encryption_configuration=wisdom.CfnAssistant.ServerSideEncryptionConfigurationProperty(
                    kms_key_id="kmsKeyId"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2f6978729a0bccb7cc077df26ee5d379812791b9fe7ec0622251ed958562e07)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument server_side_encryption_configuration", value=server_side_encryption_configuration, expected_type=type_hints["server_side_encryption_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if server_side_encryption_configuration is not None:
            self._values["server_side_encryption_configuration"] = server_side_encryption_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the assistant.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of assistant.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the assistant.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_side_encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAssistant.ServerSideEncryptionConfigurationProperty]]:
        '''The KMS key used for encryption.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-serversideencryptionconfiguration
        '''
        result = self._values.get("server_side_encryption_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAssistant.ServerSideEncryptionConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-assistant.html#cfn-wisdom-assistant-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssistantProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnKnowledgeBase(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase",
):
    '''Specifies a knowledge base.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_wisdom as wisdom
        
        cfn_knowledge_base = wisdom.CfnKnowledgeBase(self, "MyCfnKnowledgeBase",
            knowledge_base_type="knowledgeBaseType",
            name="name",
        
            # the properties below are optional
            description="description",
            rendering_configuration=wisdom.CfnKnowledgeBase.RenderingConfigurationProperty(
                template_uri="templateUri"
            ),
            server_side_encryption_configuration=wisdom.CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty(
                kms_key_id="kmsKeyId"
            ),
            source_configuration=wisdom.CfnKnowledgeBase.SourceConfigurationProperty(
                app_integrations=wisdom.CfnKnowledgeBase.AppIntegrationsConfigurationProperty(
                    app_integration_arn="appIntegrationArn",
        
                    # the properties below are optional
                    object_fields=["objectFields"]
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
        knowledge_base_type: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        rendering_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.RenderingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        server_side_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.SourceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param knowledge_base_type: The type of knowledge base. Only CUSTOM knowledge bases allow you to upload your own content. EXTERNAL knowledge bases support integrations with third-party systems whose content is synchronized automatically.
        :param name: The name of the knowledge base.
        :param description: The description.
        :param rendering_configuration: Information about how to render the content.
        :param server_side_encryption_configuration: The KMS key used for encryption.
        :param source_configuration: The source of the knowledge base content. Only set this argument for EXTERNAL knowledge bases.
        :param tags: The tags used to organize, track, or control access for this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99512a2eb8a3e47802b889aac668fc94bdc0534ee683313dac712b20006ea6ed)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnKnowledgeBaseProps(
            knowledge_base_type=knowledge_base_type,
            name=name,
            description=description,
            rendering_configuration=rendering_configuration,
            server_side_encryption_configuration=server_side_encryption_configuration,
            source_configuration=source_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e12fde615d3c7854b4e97326fea29e89d837485efe274039378606ee08a4be76)
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
            type_hints = typing.get_type_hints(_typecheckingstub__198b767f5d7e7dce9b330a5c5c43441fed236182c59b06b0be2da034b14ce256)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrKnowledgeBaseArn")
    def attr_knowledge_base_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the knowledge base.

        :cloudformationAttribute: KnowledgeBaseArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrKnowledgeBaseArn"))

    @builtins.property
    @jsii.member(jsii_name="attrKnowledgeBaseId")
    def attr_knowledge_base_id(self) -> builtins.str:
        '''The ID of the knowledge base.

        :cloudformationAttribute: KnowledgeBaseId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrKnowledgeBaseId"))

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
    @jsii.member(jsii_name="knowledgeBaseType")
    def knowledge_base_type(self) -> builtins.str:
        '''The type of knowledge base.'''
        return typing.cast(builtins.str, jsii.get(self, "knowledgeBaseType"))

    @knowledge_base_type.setter
    def knowledge_base_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93bc0b75027c2aaed7afea32df7bbe9ea25daf054d032e869d4b65d3c73427e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "knowledgeBaseType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the knowledge base.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06da4251d33a92a96fd91655710caf394cf4fa6fe728e86b20be47c80f50c450)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8e87e39918fdfb349935e6c5b5b76307ecd838c21583fab217f7d88ca3ea67c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="renderingConfiguration")
    def rendering_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.RenderingConfigurationProperty"]]:
        '''Information about how to render the content.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.RenderingConfigurationProperty"]], jsii.get(self, "renderingConfiguration"))

    @rendering_configuration.setter
    def rendering_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.RenderingConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dbfe6a279891a574d7128da28db41ca74ec109e76fb61b5b9db27b1ee815fba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "renderingConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionConfiguration")
    def server_side_encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty"]]:
        '''The KMS key used for encryption.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty"]], jsii.get(self, "serverSideEncryptionConfiguration"))

    @server_side_encryption_configuration.setter
    def server_side_encryption_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__221e4b62cf601d8c0e6300aceb9f7a7bfe38ac19093345137be6abb3f22756d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverSideEncryptionConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="sourceConfiguration")
    def source_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.SourceConfigurationProperty"]]:
        '''The source of the knowledge base content.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.SourceConfigurationProperty"]], jsii.get(self, "sourceConfiguration"))

    @source_configuration.setter
    def source_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.SourceConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ab7292e64b294c529dec00a33cfb2da96ff80581b3e1376c67027a944849691)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b654968450798e9434ae157e80b0efdde965d3d9cf517c41c4fcdcfa66e910f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.AppIntegrationsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "app_integration_arn": "appIntegrationArn",
            "object_fields": "objectFields",
        },
    )
    class AppIntegrationsConfigurationProperty:
        def __init__(
            self,
            *,
            app_integration_arn: builtins.str,
            object_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Configuration information for Amazon AppIntegrations to automatically ingest content.

            :param app_integration_arn: The Amazon Resource Name (ARN) of the AppIntegrations DataIntegration to use for ingesting content. - For `Salesforce <https://docs.aws.amazon.com/https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/sforce_api_objects_knowledge__kav.htm>`_ , your AppIntegrations DataIntegration must have an ObjectConfiguration if objectFields is not provided, including at least ``Id`` , ``ArticleNumber`` , ``VersionNumber`` , ``Title`` , ``PublishStatus`` , and ``IsDeleted`` as source fields. - For `ServiceNow <https://docs.aws.amazon.com/https://developer.servicenow.com/dev.do#!/reference/api/rome/rest/knowledge-management-api>`_ , your AppIntegrations DataIntegration must have an ObjectConfiguration if objectFields is not provided, including at least ``number`` , ``short_description`` , ``sys_mod_count`` , ``workflow_state`` , and ``active`` as source fields. - For `Zendesk <https://docs.aws.amazon.com/https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/>`_ , your AppIntegrations DataIntegration must have an ObjectConfiguration if ``objectFields`` is not provided, including at least ``id`` , ``title`` , ``updated_at`` , and ``draft`` as source fields. - For `SharePoint <https://docs.aws.amazon.com/https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/sharepoint-net-server-csom-jsom-and-rest-api-index>`_ , your AppIntegrations DataIntegration must have a FileConfiguration, including only file extensions that are among ``docx`` , ``pdf`` , ``html`` , ``htm`` , and ``txt`` .
            :param object_fields: The fields from the source that are made available to your agents in Wisdom. Optional if ObjectConfiguration is included in the provided DataIntegration. - For `Salesforce <https://docs.aws.amazon.com/https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/sforce_api_objects_knowledge__kav.htm>`_ , you must include at least ``Id`` , ``ArticleNumber`` , ``VersionNumber`` , ``Title`` , ``PublishStatus`` , and ``IsDeleted`` . - For `ServiceNow <https://docs.aws.amazon.com/https://developer.servicenow.com/dev.do#!/reference/api/rome/rest/knowledge-management-api>`_ , you must include at least ``number`` , ``short_description`` , ``sys_mod_count`` , ``workflow_state`` , and ``active`` . - For `Zendesk <https://docs.aws.amazon.com/https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/>`_ , you must include at least ``id`` , ``title`` , ``updated_at`` , and ``draft`` . Make sure to include additional fields. These fields are indexed and used to source recommendations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-appintegrationsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                app_integrations_configuration_property = wisdom.CfnKnowledgeBase.AppIntegrationsConfigurationProperty(
                    app_integration_arn="appIntegrationArn",
                
                    # the properties below are optional
                    object_fields=["objectFields"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fb5af4edc537ecd6b5dab081c90708156852ccef10f7a6228ff445f6dc0e509c)
                check_type(argname="argument app_integration_arn", value=app_integration_arn, expected_type=type_hints["app_integration_arn"])
                check_type(argname="argument object_fields", value=object_fields, expected_type=type_hints["object_fields"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "app_integration_arn": app_integration_arn,
            }
            if object_fields is not None:
                self._values["object_fields"] = object_fields

        @builtins.property
        def app_integration_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the AppIntegrations DataIntegration to use for ingesting content.

            - For `Salesforce <https://docs.aws.amazon.com/https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/sforce_api_objects_knowledge__kav.htm>`_ , your AppIntegrations DataIntegration must have an ObjectConfiguration if objectFields is not provided, including at least ``Id`` , ``ArticleNumber`` , ``VersionNumber`` , ``Title`` , ``PublishStatus`` , and ``IsDeleted`` as source fields.
            - For `ServiceNow <https://docs.aws.amazon.com/https://developer.servicenow.com/dev.do#!/reference/api/rome/rest/knowledge-management-api>`_ , your AppIntegrations DataIntegration must have an ObjectConfiguration if objectFields is not provided, including at least ``number`` , ``short_description`` , ``sys_mod_count`` , ``workflow_state`` , and ``active`` as source fields.
            - For `Zendesk <https://docs.aws.amazon.com/https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/>`_ , your AppIntegrations DataIntegration must have an ObjectConfiguration if ``objectFields`` is not provided, including at least ``id`` , ``title`` , ``updated_at`` , and ``draft`` as source fields.
            - For `SharePoint <https://docs.aws.amazon.com/https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/sharepoint-net-server-csom-jsom-and-rest-api-index>`_ , your AppIntegrations DataIntegration must have a FileConfiguration, including only file extensions that are among ``docx`` , ``pdf`` , ``html`` , ``htm`` , and ``txt`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-appintegrationsconfiguration.html#cfn-wisdom-knowledgebase-appintegrationsconfiguration-appintegrationarn
            '''
            result = self._values.get("app_integration_arn")
            assert result is not None, "Required property 'app_integration_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def object_fields(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The fields from the source that are made available to your agents in Wisdom.

            Optional if ObjectConfiguration is included in the provided DataIntegration.

            - For `Salesforce <https://docs.aws.amazon.com/https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/sforce_api_objects_knowledge__kav.htm>`_ , you must include at least ``Id`` , ``ArticleNumber`` , ``VersionNumber`` , ``Title`` , ``PublishStatus`` , and ``IsDeleted`` .
            - For `ServiceNow <https://docs.aws.amazon.com/https://developer.servicenow.com/dev.do#!/reference/api/rome/rest/knowledge-management-api>`_ , you must include at least ``number`` , ``short_description`` , ``sys_mod_count`` , ``workflow_state`` , and ``active`` .
            - For `Zendesk <https://docs.aws.amazon.com/https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/>`_ , you must include at least ``id`` , ``title`` , ``updated_at`` , and ``draft`` .

            Make sure to include additional fields. These fields are indexed and used to source recommendations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-appintegrationsconfiguration.html#cfn-wisdom-knowledgebase-appintegrationsconfiguration-objectfields
            '''
            result = self._values.get("object_fields")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AppIntegrationsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.RenderingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"template_uri": "templateUri"},
    )
    class RenderingConfigurationProperty:
        def __init__(
            self,
            *,
            template_uri: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about how to render the content.

            :param template_uri: A URI template containing exactly one variable in ``${variableName}`` format. This can only be set for ``EXTERNAL`` knowledge bases. For Salesforce, ServiceNow, and Zendesk, the variable must be one of the following: - Salesforce: ``Id`` , ``ArticleNumber`` , ``VersionNumber`` , ``Title`` , ``PublishStatus`` , or ``IsDeleted`` - ServiceNow: ``number`` , ``short_description`` , ``sys_mod_count`` , ``workflow_state`` , or ``active`` - Zendesk: ``id`` , ``title`` , ``updated_at`` , or ``draft`` The variable is replaced with the actual value for a piece of content when calling `GetContent <https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetContent.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-renderingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                rendering_configuration_property = wisdom.CfnKnowledgeBase.RenderingConfigurationProperty(
                    template_uri="templateUri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bc0b3350c030b63153dd14a7ab6b7c686549027289e97b41678c46c5c9bce0d1)
                check_type(argname="argument template_uri", value=template_uri, expected_type=type_hints["template_uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if template_uri is not None:
                self._values["template_uri"] = template_uri

        @builtins.property
        def template_uri(self) -> typing.Optional[builtins.str]:
            '''A URI template containing exactly one variable in ``${variableName}`` format.

            This can only be set for ``EXTERNAL`` knowledge bases. For Salesforce, ServiceNow, and Zendesk, the variable must be one of the following:

            - Salesforce: ``Id`` , ``ArticleNumber`` , ``VersionNumber`` , ``Title`` , ``PublishStatus`` , or ``IsDeleted``
            - ServiceNow: ``number`` , ``short_description`` , ``sys_mod_count`` , ``workflow_state`` , or ``active``
            - Zendesk: ``id`` , ``title`` , ``updated_at`` , or ``draft``

            The variable is replaced with the actual value for a piece of content when calling `GetContent <https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetContent.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-renderingconfiguration.html#cfn-wisdom-knowledgebase-renderingconfiguration-templateuri
            '''
            result = self._values.get("template_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RenderingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_key_id": "kmsKeyId"},
    )
    class ServerSideEncryptionConfigurationProperty:
        def __init__(self, *, kms_key_id: typing.Optional[builtins.str] = None) -> None:
            '''The KMS key used for encryption.

            :param kms_key_id: The KMS key . For information about valid ID values, see `Key identifiers (KeyId) <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id>`_ in the *AWS Key Management Service Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-serversideencryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                server_side_encryption_configuration_property = wisdom.CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty(
                    kms_key_id="kmsKeyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f0cd7e6721b8c282e7e8effcea12ef5d59096c2d9eb9611a2269ac2deff0e697)
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The KMS key .

            For information about valid ID values, see `Key identifiers (KeyId) <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id>`_ in the *AWS Key Management Service Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-serversideencryptionconfiguration.html#cfn-wisdom-knowledgebase-serversideencryptionconfiguration-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServerSideEncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBase.SourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"app_integrations": "appIntegrations"},
    )
    class SourceConfigurationProperty:
        def __init__(
            self,
            *,
            app_integrations: typing.Union[_IResolvable_da3f097b, typing.Union["CfnKnowledgeBase.AppIntegrationsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Configuration information about the external data source.

            :param app_integrations: Configuration information for Amazon AppIntegrations to automatically ingest content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-sourceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_wisdom as wisdom
                
                source_configuration_property = wisdom.CfnKnowledgeBase.SourceConfigurationProperty(
                    app_integrations=wisdom.CfnKnowledgeBase.AppIntegrationsConfigurationProperty(
                        app_integration_arn="appIntegrationArn",
                
                        # the properties below are optional
                        object_fields=["objectFields"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__169c34939e73e3c8ce81d921898915b159d4e29ad0c3757e50950775728d0aa0)
                check_type(argname="argument app_integrations", value=app_integrations, expected_type=type_hints["app_integrations"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "app_integrations": app_integrations,
            }

        @builtins.property
        def app_integrations(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.AppIntegrationsConfigurationProperty"]:
            '''Configuration information for Amazon AppIntegrations to automatically ingest content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-wisdom-knowledgebase-sourceconfiguration.html#cfn-wisdom-knowledgebase-sourceconfiguration-appintegrations
            '''
            result = self._values.get("app_integrations")
            assert result is not None, "Required property 'app_integrations' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnKnowledgeBase.AppIntegrationsConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_wisdom.CfnKnowledgeBaseProps",
    jsii_struct_bases=[],
    name_mapping={
        "knowledge_base_type": "knowledgeBaseType",
        "name": "name",
        "description": "description",
        "rendering_configuration": "renderingConfiguration",
        "server_side_encryption_configuration": "serverSideEncryptionConfiguration",
        "source_configuration": "sourceConfiguration",
        "tags": "tags",
    },
)
class CfnKnowledgeBaseProps:
    def __init__(
        self,
        *,
        knowledge_base_type: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        rendering_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.RenderingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        server_side_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.SourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnKnowledgeBase``.

        :param knowledge_base_type: The type of knowledge base. Only CUSTOM knowledge bases allow you to upload your own content. EXTERNAL knowledge bases support integrations with third-party systems whose content is synchronized automatically.
        :param name: The name of the knowledge base.
        :param description: The description.
        :param rendering_configuration: Information about how to render the content.
        :param server_side_encryption_configuration: The KMS key used for encryption.
        :param source_configuration: The source of the knowledge base content. Only set this argument for EXTERNAL knowledge bases.
        :param tags: The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_wisdom as wisdom
            
            cfn_knowledge_base_props = wisdom.CfnKnowledgeBaseProps(
                knowledge_base_type="knowledgeBaseType",
                name="name",
            
                # the properties below are optional
                description="description",
                rendering_configuration=wisdom.CfnKnowledgeBase.RenderingConfigurationProperty(
                    template_uri="templateUri"
                ),
                server_side_encryption_configuration=wisdom.CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty(
                    kms_key_id="kmsKeyId"
                ),
                source_configuration=wisdom.CfnKnowledgeBase.SourceConfigurationProperty(
                    app_integrations=wisdom.CfnKnowledgeBase.AppIntegrationsConfigurationProperty(
                        app_integration_arn="appIntegrationArn",
            
                        # the properties below are optional
                        object_fields=["objectFields"]
                    )
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b2c89f78d66a3c10ed4851c5bc420028f69cc91ddabbe2ac038dd7332ea1edd)
            check_type(argname="argument knowledge_base_type", value=knowledge_base_type, expected_type=type_hints["knowledge_base_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument rendering_configuration", value=rendering_configuration, expected_type=type_hints["rendering_configuration"])
            check_type(argname="argument server_side_encryption_configuration", value=server_side_encryption_configuration, expected_type=type_hints["server_side_encryption_configuration"])
            check_type(argname="argument source_configuration", value=source_configuration, expected_type=type_hints["source_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "knowledge_base_type": knowledge_base_type,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if rendering_configuration is not None:
            self._values["rendering_configuration"] = rendering_configuration
        if server_side_encryption_configuration is not None:
            self._values["server_side_encryption_configuration"] = server_side_encryption_configuration
        if source_configuration is not None:
            self._values["source_configuration"] = source_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def knowledge_base_type(self) -> builtins.str:
        '''The type of knowledge base.

        Only CUSTOM knowledge bases allow you to upload your own content. EXTERNAL knowledge bases support integrations with third-party systems whose content is synchronized automatically.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-knowledgebasetype
        '''
        result = self._values.get("knowledge_base_type")
        assert result is not None, "Required property 'knowledge_base_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the knowledge base.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rendering_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.RenderingConfigurationProperty]]:
        '''Information about how to render the content.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-renderingconfiguration
        '''
        result = self._values.get("rendering_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.RenderingConfigurationProperty]], result)

    @builtins.property
    def server_side_encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty]]:
        '''The KMS key used for encryption.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-serversideencryptionconfiguration
        '''
        result = self._values.get("server_side_encryption_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty]], result)

    @builtins.property
    def source_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.SourceConfigurationProperty]]:
        '''The source of the knowledge base content.

        Only set this argument for EXTERNAL knowledge bases.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-sourceconfiguration
        '''
        result = self._values.get("source_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.SourceConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-knowledgebase.html#cfn-wisdom-knowledgebase-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKnowledgeBaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAssistant",
    "CfnAssistantAssociation",
    "CfnAssistantAssociationProps",
    "CfnAssistantProps",
    "CfnKnowledgeBase",
    "CfnKnowledgeBaseProps",
]

publication.publish()

def _typecheckingstub__8078b7e28a17a68ab6f3d362e7de3af6b6867207690b2b344e35797cd6569746(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    server_side_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssistant.ServerSideEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67a0860b53a1867e3124a155db57aa1ab8bbb2d50c48a1553f8766101996d0b8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a17095196842a083c7a71c961443f89f6d1dd766154e06248d10cdee66b0113(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ded25c09bd072cbcb02cdfdf40580d154663664980378f96c5210edc137dd8c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c131b16ef6a21690f65d4e643bc0f04ea3e1fa9afd2bbf0e89a9bd4b96032657(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17115c2ceb35036c54e25dfa13fd4465303e5a759aae943761c84163427b74ed(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb8470e364668ea9060baa4a3306507e0ded02773f75cc435d33474d30577d1b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAssistant.ServerSideEncryptionConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a82c89946835215b7304a7033eacc23c202ee6ae8e17e73d0ba34f1dbaf1416(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa78e1cc313485ba353b8f1dc8b01c69bcdd1c5bcecd204b9778596de1e4a07d(
    *,
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17f6f8491bb7be7dab63c57bf64b65f643c4fece381b02f49002f796c7a8f0f9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    assistant_id: builtins.str,
    association: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssistantAssociation.AssociationDataProperty, typing.Dict[builtins.str, typing.Any]]],
    association_type: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a96af34ce4ed10cd5d626bf5df7799b86ca3023d4f6b302c0cdb51a0bdd1274(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e84fe37792368fc9821204b49ed0d6e13642f35bcdc7bb2676de0ee949767075(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c72c215a467df1527e01f95d41dc85287728a80fa94729b3ff14b2b1312fb30(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e46eeb6364ccf0b8f92618927437f56df6248417cb401c056b83fe5692feb0f8(
    value: typing.Union[_IResolvable_da3f097b, CfnAssistantAssociation.AssociationDataProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48fcb269f8dde8b147d1a0d7681e40817cb35b599f00a24aff263a84df4cea90(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea3d3cb4fe1048c256fc8719ac3d18f47cb21ef29730dd9d1f53a9304ccd4030(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6ecf0cfb2eb97624a8ec4ab51e16f75cfa1a5397890274252a2621ff5ad378d(
    *,
    knowledge_base_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__419e70156a249f4fa2bea77a71d532fe9a351e3d150b5939dc8455b174375514(
    *,
    assistant_id: builtins.str,
    association: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssistantAssociation.AssociationDataProperty, typing.Dict[builtins.str, typing.Any]]],
    association_type: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2f6978729a0bccb7cc077df26ee5d379812791b9fe7ec0622251ed958562e07(
    *,
    name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    server_side_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssistant.ServerSideEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99512a2eb8a3e47802b889aac668fc94bdc0534ee683313dac712b20006ea6ed(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    knowledge_base_type: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    rendering_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.RenderingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    server_side_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.SourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e12fde615d3c7854b4e97326fea29e89d837485efe274039378606ee08a4be76(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__198b767f5d7e7dce9b330a5c5c43441fed236182c59b06b0be2da034b14ce256(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93bc0b75027c2aaed7afea32df7bbe9ea25daf054d032e869d4b65d3c73427e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06da4251d33a92a96fd91655710caf394cf4fa6fe728e86b20be47c80f50c450(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8e87e39918fdfb349935e6c5b5b76307ecd838c21583fab217f7d88ca3ea67c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dbfe6a279891a574d7128da28db41ca74ec109e76fb61b5b9db27b1ee815fba(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.RenderingConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__221e4b62cf601d8c0e6300aceb9f7a7bfe38ac19093345137be6abb3f22756d8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ab7292e64b294c529dec00a33cfb2da96ff80581b3e1376c67027a944849691(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnKnowledgeBase.SourceConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b654968450798e9434ae157e80b0efdde965d3d9cf517c41c4fcdcfa66e910f8(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb5af4edc537ecd6b5dab081c90708156852ccef10f7a6228ff445f6dc0e509c(
    *,
    app_integration_arn: builtins.str,
    object_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc0b3350c030b63153dd14a7ab6b7c686549027289e97b41678c46c5c9bce0d1(
    *,
    template_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0cd7e6721b8c282e7e8effcea12ef5d59096c2d9eb9611a2269ac2deff0e697(
    *,
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__169c34939e73e3c8ce81d921898915b159d4e29ad0c3757e50950775728d0aa0(
    *,
    app_integrations: typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.AppIntegrationsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b2c89f78d66a3c10ed4851c5bc420028f69cc91ddabbe2ac038dd7332ea1edd(
    *,
    knowledge_base_type: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    rendering_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.RenderingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    server_side_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.ServerSideEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnKnowledgeBase.SourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
