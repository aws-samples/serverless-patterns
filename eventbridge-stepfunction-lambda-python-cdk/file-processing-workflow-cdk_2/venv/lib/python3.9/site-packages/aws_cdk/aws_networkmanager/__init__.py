'''
# AWS::NetworkManager Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_networkmanager as networkmanager
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for NetworkManager construct libraries](https://constructs.dev/search?q=networkmanager)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::NetworkManager resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_NetworkManager.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::NetworkManager](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_NetworkManager.html).

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
class CfnConnectAttachment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnConnectAttachment",
):
    '''Creates a core network Connect attachment from a specified core network attachment.

    A core network Connect attachment is a GRE-based tunnel attachment that you can use to establish a connection between a core network and an appliance. A core network Connect attachment uses an existing VPC attachment as the underlying transport mechanism.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        cfn_connect_attachment = networkmanager.CfnConnectAttachment(self, "MyCfnConnectAttachment",
            core_network_id="coreNetworkId",
            edge_location="edgeLocation",
            options=networkmanager.CfnConnectAttachment.ConnectAttachmentOptionsProperty(
                protocol="protocol"
            ),
            transport_attachment_id="transportAttachmentId",
        
            # the properties below are optional
            proposed_segment_change=networkmanager.CfnConnectAttachment.ProposedSegmentChangeProperty(
                attachment_policy_rule_number=123,
                segment_name="segmentName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
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
        core_network_id: builtins.str,
        edge_location: builtins.str,
        options: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectAttachment.ConnectAttachmentOptionsProperty", typing.Dict[builtins.str, typing.Any]]],
        transport_attachment_id: builtins.str,
        proposed_segment_change: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectAttachment.ProposedSegmentChangeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param core_network_id: The ID of the core network where the Connect attachment is located.
        :param edge_location: The Region where the edge is located.
        :param options: Options for connecting an attachment.
        :param transport_attachment_id: The ID of the transport attachment.
        :param proposed_segment_change: The attachment to move from one segment to another.
        :param tags: Tags for the attachment.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7415843def493b65c590878e3897c27e4c459f5d736fb5ee9738e5a17aad441)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConnectAttachmentProps(
            core_network_id=core_network_id,
            edge_location=edge_location,
            options=options,
            transport_attachment_id=transport_attachment_id,
            proposed_segment_change=proposed_segment_change,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44665bf65f06575cd3323d1c866a2dc00c17092a359aac8101e622ad9bf92f5c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec45c4dbbf2822b7186c9d48a08a52feeb96db87ca1ed98a3c52fb2284f4f9de)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAttachmentId")
    def attr_attachment_id(self) -> builtins.str:
        '''The ID of the Connect attachment.

        :cloudformationAttribute: AttachmentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAttachmentId"))

    @builtins.property
    @jsii.member(jsii_name="attrAttachmentPolicyRuleNumber")
    def attr_attachment_policy_rule_number(self) -> jsii.Number:
        '''The rule number associated with the attachment.

        :cloudformationAttribute: AttachmentPolicyRuleNumber
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrAttachmentPolicyRuleNumber"))

    @builtins.property
    @jsii.member(jsii_name="attrAttachmentType")
    def attr_attachment_type(self) -> builtins.str:
        '''The type of attachment.

        This will be ``CONNECT`` .

        :cloudformationAttribute: AttachmentType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAttachmentType"))

    @builtins.property
    @jsii.member(jsii_name="attrCoreNetworkArn")
    def attr_core_network_arn(self) -> builtins.str:
        '''The ARN of the core network.

        :cloudformationAttribute: CoreNetworkArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCoreNetworkArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the Connect attachment was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrOwnerAccountId")
    def attr_owner_account_id(self) -> builtins.str:
        '''The ID of the Connect attachment owner.

        :cloudformationAttribute: OwnerAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerAccountId"))

    @builtins.property
    @jsii.member(jsii_name="attrResourceArn")
    def attr_resource_arn(self) -> builtins.str:
        '''The resource ARN for the Connect attachment.

        :cloudformationAttribute: ResourceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSegmentName")
    def attr_segment_name(self) -> builtins.str:
        '''The name of the Connect attachment's segment.

        :cloudformationAttribute: SegmentName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSegmentName"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The state of the Connect attachment.

        This can be: ``REJECTED`` | ``PENDING_ATTACHMENT_ACCEPTANCE`` | ``CREATING`` | ``FAILED`` | ``AVAILABLE`` | ``UPDATING`` | ``PENDING_NETWORK_UPDATE`` | ``PENDING_TAG_ACCEPTANCE`` | ``DELETING`` .

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp when the Connect attachment was last updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

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
    @jsii.member(jsii_name="coreNetworkId")
    def core_network_id(self) -> builtins.str:
        '''The ID of the core network where the Connect attachment is located.'''
        return typing.cast(builtins.str, jsii.get(self, "coreNetworkId"))

    @core_network_id.setter
    def core_network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1019c9f66ae0f0b6c31480b08f0844a5328118d1f4beeb166ff2f71b6068b0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coreNetworkId", value)

    @builtins.property
    @jsii.member(jsii_name="edgeLocation")
    def edge_location(self) -> builtins.str:
        '''The Region where the edge is located.'''
        return typing.cast(builtins.str, jsii.get(self, "edgeLocation"))

    @edge_location.setter
    def edge_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65f8076caf77f777faab35b0ff1e31902eae6e5c1507ec93cdcdef28bd00b0bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "edgeLocation", value)

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnConnectAttachment.ConnectAttachmentOptionsProperty"]:
        '''Options for connecting an attachment.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConnectAttachment.ConnectAttachmentOptionsProperty"], jsii.get(self, "options"))

    @options.setter
    def options(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnConnectAttachment.ConnectAttachmentOptionsProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3ec27706fe61280d3c2f24d80b9b25fadffd2d87cfb1922fb82b4b8309feeab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "options", value)

    @builtins.property
    @jsii.member(jsii_name="transportAttachmentId")
    def transport_attachment_id(self) -> builtins.str:
        '''The ID of the transport attachment.'''
        return typing.cast(builtins.str, jsii.get(self, "transportAttachmentId"))

    @transport_attachment_id.setter
    def transport_attachment_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f45177b471df4bf392fc7f3cd3a02af202d007968b4b8f463eab9717182e743e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transportAttachmentId", value)

    @builtins.property
    @jsii.member(jsii_name="proposedSegmentChange")
    def proposed_segment_change(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectAttachment.ProposedSegmentChangeProperty"]]:
        '''The attachment to move from one segment to another.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectAttachment.ProposedSegmentChangeProperty"]], jsii.get(self, "proposedSegmentChange"))

    @proposed_segment_change.setter
    def proposed_segment_change(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectAttachment.ProposedSegmentChangeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84b1c89b7abda3eee8505aae6dbce09c5893b6a4187a20a6c43a4204cea40ffd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proposedSegmentChange", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags for the attachment.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffc7890372457410bdf1574c98526291062406f7166b95fd35ac58c7cbd3e98c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkmanager.CfnConnectAttachment.ConnectAttachmentOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"protocol": "protocol"},
    )
    class ConnectAttachmentOptionsProperty:
        def __init__(self, *, protocol: typing.Optional[builtins.str] = None) -> None:
            '''Describes a core network Connect attachment options.

            :param protocol: The protocol used for the attachment connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectattachment-connectattachmentoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkmanager as networkmanager
                
                connect_attachment_options_property = networkmanager.CfnConnectAttachment.ConnectAttachmentOptionsProperty(
                    protocol="protocol"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bc0fa092684fa44dd4fe83501bbb7802a95737bd2a72c5eaea2e09e6d7c8b31f)
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if protocol is not None:
                self._values["protocol"] = protocol

        @builtins.property
        def protocol(self) -> typing.Optional[builtins.str]:
            '''The protocol used for the attachment connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectattachment-connectattachmentoptions.html#cfn-networkmanager-connectattachment-connectattachmentoptions-protocol
            '''
            result = self._values.get("protocol")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectAttachmentOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkmanager.CfnConnectAttachment.ProposedSegmentChangeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attachment_policy_rule_number": "attachmentPolicyRuleNumber",
            "segment_name": "segmentName",
            "tags": "tags",
        },
    )
    class ProposedSegmentChangeProperty:
        def __init__(
            self,
            *,
            attachment_policy_rule_number: typing.Optional[jsii.Number] = None,
            segment_name: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes a proposed segment change.

            In some cases, the segment change must first be evaluated and accepted.

            :param attachment_policy_rule_number: The rule number in the policy document that applies to this change.
            :param segment_name: The name of the segment to change.
            :param tags: The list of key-value tags that changed for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectattachment-proposedsegmentchange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkmanager as networkmanager
                
                proposed_segment_change_property = networkmanager.CfnConnectAttachment.ProposedSegmentChangeProperty(
                    attachment_policy_rule_number=123,
                    segment_name="segmentName",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__33f3ba0307020211126665ce4fb2d25caae1b2af6cc7e2712bd85408f247a0da)
                check_type(argname="argument attachment_policy_rule_number", value=attachment_policy_rule_number, expected_type=type_hints["attachment_policy_rule_number"])
                check_type(argname="argument segment_name", value=segment_name, expected_type=type_hints["segment_name"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if attachment_policy_rule_number is not None:
                self._values["attachment_policy_rule_number"] = attachment_policy_rule_number
            if segment_name is not None:
                self._values["segment_name"] = segment_name
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def attachment_policy_rule_number(self) -> typing.Optional[jsii.Number]:
            '''The rule number in the policy document that applies to this change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectattachment-proposedsegmentchange.html#cfn-networkmanager-connectattachment-proposedsegmentchange-attachmentpolicyrulenumber
            '''
            result = self._values.get("attachment_policy_rule_number")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def segment_name(self) -> typing.Optional[builtins.str]:
            '''The name of the segment to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectattachment-proposedsegmentchange.html#cfn-networkmanager-connectattachment-proposedsegmentchange-segmentname
            '''
            result = self._values.get("segment_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
            '''The list of key-value tags that changed for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectattachment-proposedsegmentchange.html#cfn-networkmanager-connectattachment-proposedsegmentchange-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProposedSegmentChangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnConnectAttachmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "core_network_id": "coreNetworkId",
        "edge_location": "edgeLocation",
        "options": "options",
        "transport_attachment_id": "transportAttachmentId",
        "proposed_segment_change": "proposedSegmentChange",
        "tags": "tags",
    },
)
class CfnConnectAttachmentProps:
    def __init__(
        self,
        *,
        core_network_id: builtins.str,
        edge_location: builtins.str,
        options: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectAttachment.ConnectAttachmentOptionsProperty, typing.Dict[builtins.str, typing.Any]]],
        transport_attachment_id: builtins.str,
        proposed_segment_change: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectAttachment.ProposedSegmentChangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConnectAttachment``.

        :param core_network_id: The ID of the core network where the Connect attachment is located.
        :param edge_location: The Region where the edge is located.
        :param options: Options for connecting an attachment.
        :param transport_attachment_id: The ID of the transport attachment.
        :param proposed_segment_change: The attachment to move from one segment to another.
        :param tags: Tags for the attachment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            cfn_connect_attachment_props = networkmanager.CfnConnectAttachmentProps(
                core_network_id="coreNetworkId",
                edge_location="edgeLocation",
                options=networkmanager.CfnConnectAttachment.ConnectAttachmentOptionsProperty(
                    protocol="protocol"
                ),
                transport_attachment_id="transportAttachmentId",
            
                # the properties below are optional
                proposed_segment_change=networkmanager.CfnConnectAttachment.ProposedSegmentChangeProperty(
                    attachment_policy_rule_number=123,
                    segment_name="segmentName",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b62006d4f48143066c9708819150b6dc03f2315028ddb6bd7d7d8ecbc955531)
            check_type(argname="argument core_network_id", value=core_network_id, expected_type=type_hints["core_network_id"])
            check_type(argname="argument edge_location", value=edge_location, expected_type=type_hints["edge_location"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument transport_attachment_id", value=transport_attachment_id, expected_type=type_hints["transport_attachment_id"])
            check_type(argname="argument proposed_segment_change", value=proposed_segment_change, expected_type=type_hints["proposed_segment_change"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "core_network_id": core_network_id,
            "edge_location": edge_location,
            "options": options,
            "transport_attachment_id": transport_attachment_id,
        }
        if proposed_segment_change is not None:
            self._values["proposed_segment_change"] = proposed_segment_change
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def core_network_id(self) -> builtins.str:
        '''The ID of the core network where the Connect attachment is located.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html#cfn-networkmanager-connectattachment-corenetworkid
        '''
        result = self._values.get("core_network_id")
        assert result is not None, "Required property 'core_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def edge_location(self) -> builtins.str:
        '''The Region where the edge is located.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html#cfn-networkmanager-connectattachment-edgelocation
        '''
        result = self._values.get("edge_location")
        assert result is not None, "Required property 'edge_location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def options(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnConnectAttachment.ConnectAttachmentOptionsProperty]:
        '''Options for connecting an attachment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html#cfn-networkmanager-connectattachment-options
        '''
        result = self._values.get("options")
        assert result is not None, "Required property 'options' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnConnectAttachment.ConnectAttachmentOptionsProperty], result)

    @builtins.property
    def transport_attachment_id(self) -> builtins.str:
        '''The ID of the transport attachment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html#cfn-networkmanager-connectattachment-transportattachmentid
        '''
        result = self._values.get("transport_attachment_id")
        assert result is not None, "Required property 'transport_attachment_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def proposed_segment_change(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnectAttachment.ProposedSegmentChangeProperty]]:
        '''The attachment to move from one segment to another.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html#cfn-networkmanager-connectattachment-proposedsegmentchange
        '''
        result = self._values.get("proposed_segment_change")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnectAttachment.ProposedSegmentChangeProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags for the attachment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectattachment.html#cfn-networkmanager-connectattachment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConnectAttachmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnConnectPeer(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnConnectPeer",
):
    '''Creates a core network Connect peer for a specified core network connect attachment between a core network and an appliance.

    The peer address and transit gateway address must be the same IP address family (IPv4 or IPv6).

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        cfn_connect_peer = networkmanager.CfnConnectPeer(self, "MyCfnConnectPeer",
            connect_attachment_id="connectAttachmentId",
            peer_address="peerAddress",
        
            # the properties below are optional
            bgp_options=networkmanager.CfnConnectPeer.BgpOptionsProperty(
                peer_asn=123
            ),
            core_network_address="coreNetworkAddress",
            inside_cidr_blocks=["insideCidrBlocks"],
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
        connect_attachment_id: builtins.str,
        peer_address: builtins.str,
        bgp_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectPeer.BgpOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        core_network_address: typing.Optional[builtins.str] = None,
        inside_cidr_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param connect_attachment_id: The ID of the attachment to connect.
        :param peer_address: The IP address of the Connect peer.
        :param bgp_options: Bgp options.
        :param core_network_address: The IP address of a core network.
        :param inside_cidr_blocks: The inside IP addresses used for a Connect peer configuration.
        :param tags: The list of key-value tags associated with the Connect peer.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__614dda353f68a248b8ae08e0094dfb5ecab0817abd8f24330d861cce6ffc7797)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConnectPeerProps(
            connect_attachment_id=connect_attachment_id,
            peer_address=peer_address,
            bgp_options=bgp_options,
            core_network_address=core_network_address,
            inside_cidr_blocks=inside_cidr_blocks,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7c4b91f985873f74931b033eca32fbff8cdd4309b9150310c66ccf9f6a4fc7c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a37b71a0670025bcb8e024070ea19783e142b007e3bbb76e1b2cec30a6a8c9df)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrConfiguration")
    def attr_configuration(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: Configuration
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="attrConfigurationBgpConfigurations")
    def attr_configuration_bgp_configurations(self) -> _IResolvable_da3f097b:
        '''
        :cloudformationAttribute: Configuration.BgpConfigurations
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrConfigurationBgpConfigurations"))

    @builtins.property
    @jsii.member(jsii_name="attrConfigurationCoreNetworkAddress")
    def attr_configuration_core_network_address(self) -> builtins.str:
        '''The IP address of a core network.

        :cloudformationAttribute: Configuration.CoreNetworkAddress
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConfigurationCoreNetworkAddress"))

    @builtins.property
    @jsii.member(jsii_name="attrConfigurationInsideCidrBlocks")
    def attr_configuration_inside_cidr_blocks(self) -> typing.List[builtins.str]:
        '''The inside IP addresses used for a Connect peer configuration.

        :cloudformationAttribute: Configuration.InsideCidrBlocks
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrConfigurationInsideCidrBlocks"))

    @builtins.property
    @jsii.member(jsii_name="attrConfigurationPeerAddress")
    def attr_configuration_peer_address(self) -> builtins.str:
        '''The IP address of the Connect peer.

        :cloudformationAttribute: Configuration.PeerAddress
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConfigurationPeerAddress"))

    @builtins.property
    @jsii.member(jsii_name="attrConfigurationProtocol")
    def attr_configuration_protocol(self) -> builtins.str:
        '''Tunnel protocol type (Only support GRE for now).

        :cloudformationAttribute: Configuration.Protocol
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConfigurationProtocol"))

    @builtins.property
    @jsii.member(jsii_name="attrConnectPeerId")
    def attr_connect_peer_id(self) -> builtins.str:
        '''The ID of the Connect peer.

        :cloudformationAttribute: ConnectPeerId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConnectPeerId"))

    @builtins.property
    @jsii.member(jsii_name="attrCoreNetworkId")
    def attr_core_network_id(self) -> builtins.str:
        '''The core network ID.

        :cloudformationAttribute: CoreNetworkId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCoreNetworkId"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the Connect peer was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrEdgeLocation")
    def attr_edge_location(self) -> builtins.str:
        '''The Region where the edge is located.

        :cloudformationAttribute: EdgeLocation
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEdgeLocation"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The state of the Connect peer.

        This will be: ``REJECTED`` | ``PENDING_ATTACHMENT_ACCEPTANCE`` | ``CREATING`` | ``FAILED`` | ``AVAILABLE`` | ``UPDATING`` | ``PENDING_NETWORK_UPDATE`` | ``PENDING_TAG_ACCEPTANCE`` | ``DELETING`` .

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

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
    @jsii.member(jsii_name="connectAttachmentId")
    def connect_attachment_id(self) -> builtins.str:
        '''The ID of the attachment to connect.'''
        return typing.cast(builtins.str, jsii.get(self, "connectAttachmentId"))

    @connect_attachment_id.setter
    def connect_attachment_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6837b16f8b774f684a7de66e3e0192162c799f4ccc35d48270125b5a9867f69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectAttachmentId", value)

    @builtins.property
    @jsii.member(jsii_name="peerAddress")
    def peer_address(self) -> builtins.str:
        '''The IP address of the Connect peer.'''
        return typing.cast(builtins.str, jsii.get(self, "peerAddress"))

    @peer_address.setter
    def peer_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c390f124a44254d44c9db6c9600d7d4bedeaa234040db5482b9da71be5ba3267)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerAddress", value)

    @builtins.property
    @jsii.member(jsii_name="bgpOptions")
    def bgp_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectPeer.BgpOptionsProperty"]]:
        '''Bgp options.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectPeer.BgpOptionsProperty"]], jsii.get(self, "bgpOptions"))

    @bgp_options.setter
    def bgp_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectPeer.BgpOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09c2cde583ab1ee0b8539941f5f59464104e4b15a665812986be376af521cd7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bgpOptions", value)

    @builtins.property
    @jsii.member(jsii_name="coreNetworkAddress")
    def core_network_address(self) -> typing.Optional[builtins.str]:
        '''The IP address of a core network.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "coreNetworkAddress"))

    @core_network_address.setter
    def core_network_address(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ccd872c8477548a54a56ce63aa9266f60d6d4a8ce8da83adaf0c37aa370d21d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coreNetworkAddress", value)

    @builtins.property
    @jsii.member(jsii_name="insideCidrBlocks")
    def inside_cidr_blocks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The inside IP addresses used for a Connect peer configuration.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "insideCidrBlocks"))

    @inside_cidr_blocks.setter
    def inside_cidr_blocks(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6579db2e8401c4c460fad5541ac628299f109239ae0b747856b5b464e0fb2394)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "insideCidrBlocks", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of key-value tags associated with the Connect peer.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be35c1c86a9354575519ff51daf71188a8d6c995c7f05b5070cfc8f935af359f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkmanager.CfnConnectPeer.BgpOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"peer_asn": "peerAsn"},
    )
    class BgpOptionsProperty:
        def __init__(self, *, peer_asn: typing.Optional[jsii.Number] = None) -> None:
            '''Describes the BGP options.

            :param peer_asn: The Peer ASN of the BGP.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-bgpoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkmanager as networkmanager
                
                bgp_options_property = networkmanager.CfnConnectPeer.BgpOptionsProperty(
                    peer_asn=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__820b80243250388311dea6e86ec715c97ac8bef0b52b69d918604b35a112a01c)
                check_type(argname="argument peer_asn", value=peer_asn, expected_type=type_hints["peer_asn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if peer_asn is not None:
                self._values["peer_asn"] = peer_asn

        @builtins.property
        def peer_asn(self) -> typing.Optional[jsii.Number]:
            '''The Peer ASN of the BGP.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-bgpoptions.html#cfn-networkmanager-connectpeer-bgpoptions-peerasn
            '''
            result = self._values.get("peer_asn")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BgpOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkmanager.CfnConnectPeer.ConnectPeerBgpConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "core_network_address": "coreNetworkAddress",
            "core_network_asn": "coreNetworkAsn",
            "peer_address": "peerAddress",
            "peer_asn": "peerAsn",
        },
    )
    class ConnectPeerBgpConfigurationProperty:
        def __init__(
            self,
            *,
            core_network_address: typing.Optional[builtins.str] = None,
            core_network_asn: typing.Optional[jsii.Number] = None,
            peer_address: typing.Optional[builtins.str] = None,
            peer_asn: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes a core network BGP configuration.

            :param core_network_address: The address of a core network.
            :param core_network_asn: The ASN of the Coret Network.
            :param peer_address: The address of a core network Connect peer.
            :param peer_asn: The ASN of the Connect peer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-connectpeerbgpconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkmanager as networkmanager
                
                connect_peer_bgp_configuration_property = networkmanager.CfnConnectPeer.ConnectPeerBgpConfigurationProperty(
                    core_network_address="coreNetworkAddress",
                    core_network_asn=123,
                    peer_address="peerAddress",
                    peer_asn=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5e94639c3bff646ba2bdeccdcea4a34256f4fc82522c3c1437b767fc6295f0b7)
                check_type(argname="argument core_network_address", value=core_network_address, expected_type=type_hints["core_network_address"])
                check_type(argname="argument core_network_asn", value=core_network_asn, expected_type=type_hints["core_network_asn"])
                check_type(argname="argument peer_address", value=peer_address, expected_type=type_hints["peer_address"])
                check_type(argname="argument peer_asn", value=peer_asn, expected_type=type_hints["peer_asn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if core_network_address is not None:
                self._values["core_network_address"] = core_network_address
            if core_network_asn is not None:
                self._values["core_network_asn"] = core_network_asn
            if peer_address is not None:
                self._values["peer_address"] = peer_address
            if peer_asn is not None:
                self._values["peer_asn"] = peer_asn

        @builtins.property
        def core_network_address(self) -> typing.Optional[builtins.str]:
            '''The address of a core network.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-connectpeerbgpconfiguration.html#cfn-networkmanager-connectpeer-connectpeerbgpconfiguration-corenetworkaddress
            '''
            result = self._values.get("core_network_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def core_network_asn(self) -> typing.Optional[jsii.Number]:
            '''The ASN of the Coret Network.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-connectpeerbgpconfiguration.html#cfn-networkmanager-connectpeer-connectpeerbgpconfiguration-corenetworkasn
            '''
            result = self._values.get("core_network_asn")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def peer_address(self) -> typing.Optional[builtins.str]:
            '''The address of a core network Connect peer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-connectpeerbgpconfiguration.html#cfn-networkmanager-connectpeer-connectpeerbgpconfiguration-peeraddress
            '''
            result = self._values.get("peer_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def peer_asn(self) -> typing.Optional[jsii.Number]:
            '''The ASN of the Connect peer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-connectpeerbgpconfiguration.html#cfn-networkmanager-connectpeer-connectpeerbgpconfiguration-peerasn
            '''
            result = self._values.get("peer_asn")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectPeerBgpConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkmanager.CfnConnectPeer.ConnectPeerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bgp_configurations": "bgpConfigurations",
            "core_network_address": "coreNetworkAddress",
            "inside_cidr_blocks": "insideCidrBlocks",
            "peer_address": "peerAddress",
            "protocol": "protocol",
        },
    )
    class ConnectPeerConfigurationProperty:
        def __init__(
            self,
            *,
            bgp_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectPeer.ConnectPeerBgpConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            core_network_address: typing.Optional[builtins.str] = None,
            inside_cidr_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
            peer_address: typing.Optional[builtins.str] = None,
            protocol: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes a core network Connect peer configuration.

            :param bgp_configurations: The Connect peer BGP configurations.
            :param core_network_address: The IP address of a core network.
            :param inside_cidr_blocks: The inside IP addresses used for a Connect peer configuration.
            :param peer_address: The IP address of the Connect peer.
            :param protocol: The protocol used for a Connect peer configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-connectpeerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkmanager as networkmanager
                
                connect_peer_configuration_property = networkmanager.CfnConnectPeer.ConnectPeerConfigurationProperty(
                    bgp_configurations=[networkmanager.CfnConnectPeer.ConnectPeerBgpConfigurationProperty(
                        core_network_address="coreNetworkAddress",
                        core_network_asn=123,
                        peer_address="peerAddress",
                        peer_asn=123
                    )],
                    core_network_address="coreNetworkAddress",
                    inside_cidr_blocks=["insideCidrBlocks"],
                    peer_address="peerAddress",
                    protocol="protocol"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2a9ed6409a3fe862bfaa3b6216c0ea60f1182083169100da39cfa761f53167bc)
                check_type(argname="argument bgp_configurations", value=bgp_configurations, expected_type=type_hints["bgp_configurations"])
                check_type(argname="argument core_network_address", value=core_network_address, expected_type=type_hints["core_network_address"])
                check_type(argname="argument inside_cidr_blocks", value=inside_cidr_blocks, expected_type=type_hints["inside_cidr_blocks"])
                check_type(argname="argument peer_address", value=peer_address, expected_type=type_hints["peer_address"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bgp_configurations is not None:
                self._values["bgp_configurations"] = bgp_configurations
            if core_network_address is not None:
                self._values["core_network_address"] = core_network_address
            if inside_cidr_blocks is not None:
                self._values["inside_cidr_blocks"] = inside_cidr_blocks
            if peer_address is not None:
                self._values["peer_address"] = peer_address
            if protocol is not None:
                self._values["protocol"] = protocol

        @builtins.property
        def bgp_configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConnectPeer.ConnectPeerBgpConfigurationProperty"]]]]:
            '''The Connect peer BGP configurations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-connectpeerconfiguration.html#cfn-networkmanager-connectpeer-connectpeerconfiguration-bgpconfigurations
            '''
            result = self._values.get("bgp_configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConnectPeer.ConnectPeerBgpConfigurationProperty"]]]], result)

        @builtins.property
        def core_network_address(self) -> typing.Optional[builtins.str]:
            '''The IP address of a core network.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-connectpeerconfiguration.html#cfn-networkmanager-connectpeer-connectpeerconfiguration-corenetworkaddress
            '''
            result = self._values.get("core_network_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inside_cidr_blocks(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The inside IP addresses used for a Connect peer configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-connectpeerconfiguration.html#cfn-networkmanager-connectpeer-connectpeerconfiguration-insidecidrblocks
            '''
            result = self._values.get("inside_cidr_blocks")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def peer_address(self) -> typing.Optional[builtins.str]:
            '''The IP address of the Connect peer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-connectpeerconfiguration.html#cfn-networkmanager-connectpeer-connectpeerconfiguration-peeraddress
            '''
            result = self._values.get("peer_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def protocol(self) -> typing.Optional[builtins.str]:
            '''The protocol used for a Connect peer configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-connectpeer-connectpeerconfiguration.html#cfn-networkmanager-connectpeer-connectpeerconfiguration-protocol
            '''
            result = self._values.get("protocol")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectPeerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnConnectPeerProps",
    jsii_struct_bases=[],
    name_mapping={
        "connect_attachment_id": "connectAttachmentId",
        "peer_address": "peerAddress",
        "bgp_options": "bgpOptions",
        "core_network_address": "coreNetworkAddress",
        "inside_cidr_blocks": "insideCidrBlocks",
        "tags": "tags",
    },
)
class CfnConnectPeerProps:
    def __init__(
        self,
        *,
        connect_attachment_id: builtins.str,
        peer_address: builtins.str,
        bgp_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectPeer.BgpOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        core_network_address: typing.Optional[builtins.str] = None,
        inside_cidr_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConnectPeer``.

        :param connect_attachment_id: The ID of the attachment to connect.
        :param peer_address: The IP address of the Connect peer.
        :param bgp_options: Bgp options.
        :param core_network_address: The IP address of a core network.
        :param inside_cidr_blocks: The inside IP addresses used for a Connect peer configuration.
        :param tags: The list of key-value tags associated with the Connect peer.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            cfn_connect_peer_props = networkmanager.CfnConnectPeerProps(
                connect_attachment_id="connectAttachmentId",
                peer_address="peerAddress",
            
                # the properties below are optional
                bgp_options=networkmanager.CfnConnectPeer.BgpOptionsProperty(
                    peer_asn=123
                ),
                core_network_address="coreNetworkAddress",
                inside_cidr_blocks=["insideCidrBlocks"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c4bd06b5a27f2d168dc63dd01d3d754fafe1dd8ea823eede0c4909db15718f8)
            check_type(argname="argument connect_attachment_id", value=connect_attachment_id, expected_type=type_hints["connect_attachment_id"])
            check_type(argname="argument peer_address", value=peer_address, expected_type=type_hints["peer_address"])
            check_type(argname="argument bgp_options", value=bgp_options, expected_type=type_hints["bgp_options"])
            check_type(argname="argument core_network_address", value=core_network_address, expected_type=type_hints["core_network_address"])
            check_type(argname="argument inside_cidr_blocks", value=inside_cidr_blocks, expected_type=type_hints["inside_cidr_blocks"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connect_attachment_id": connect_attachment_id,
            "peer_address": peer_address,
        }
        if bgp_options is not None:
            self._values["bgp_options"] = bgp_options
        if core_network_address is not None:
            self._values["core_network_address"] = core_network_address
        if inside_cidr_blocks is not None:
            self._values["inside_cidr_blocks"] = inside_cidr_blocks
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def connect_attachment_id(self) -> builtins.str:
        '''The ID of the attachment to connect.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html#cfn-networkmanager-connectpeer-connectattachmentid
        '''
        result = self._values.get("connect_attachment_id")
        assert result is not None, "Required property 'connect_attachment_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def peer_address(self) -> builtins.str:
        '''The IP address of the Connect peer.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html#cfn-networkmanager-connectpeer-peeraddress
        '''
        result = self._values.get("peer_address")
        assert result is not None, "Required property 'peer_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bgp_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnectPeer.BgpOptionsProperty]]:
        '''Bgp options.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html#cfn-networkmanager-connectpeer-bgpoptions
        '''
        result = self._values.get("bgp_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnectPeer.BgpOptionsProperty]], result)

    @builtins.property
    def core_network_address(self) -> typing.Optional[builtins.str]:
        '''The IP address of a core network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html#cfn-networkmanager-connectpeer-corenetworkaddress
        '''
        result = self._values.get("core_network_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inside_cidr_blocks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The inside IP addresses used for a Connect peer configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html#cfn-networkmanager-connectpeer-insidecidrblocks
        '''
        result = self._values.get("inside_cidr_blocks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of key-value tags associated with the Connect peer.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-connectpeer.html#cfn-networkmanager-connectpeer-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConnectPeerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnCoreNetwork(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnCoreNetwork",
):
    '''Describes a core network.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-corenetwork.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        # policy_document: Any
        
        cfn_core_network = networkmanager.CfnCoreNetwork(self, "MyCfnCoreNetwork",
            global_network_id="globalNetworkId",
        
            # the properties below are optional
            description="description",
            policy_document=policy_document,
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
        global_network_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        policy_document: typing.Any = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param global_network_id: The ID of the global network that your core network is a part of.
        :param description: The description of a core network.
        :param policy_document: Describes a core network policy. For more information, see `Core network policies <https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-change-sets.html>`_ . If you update the policy document, CloudFormation will apply the core network change set generated from the updated policy document, and then set it as the LIVE policy.
        :param tags: The list of key-value tags associated with a core network.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef3cb1cd4abb4fa5b383cbcb25ab3b19985891cac9ee903fdc80a4b7855c3861)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCoreNetworkProps(
            global_network_id=global_network_id,
            description=description,
            policy_document=policy_document,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab8dfe0941f0bb31d0cd5ffec09e9e0e64f454ca60a61a7e724ae83857fed362)
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
            type_hints = typing.get_type_hints(_typecheckingstub__64d8a77d9a9f53702b00cebe4bcbe33b1dcc035bc69a26e96bb10401bee44fd4)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCoreNetworkArn")
    def attr_core_network_arn(self) -> builtins.str:
        '''The ARN of the core network.

        :cloudformationAttribute: CoreNetworkArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCoreNetworkArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCoreNetworkId")
    def attr_core_network_id(self) -> builtins.str:
        '''The ID of the core network.

        :cloudformationAttribute: CoreNetworkId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCoreNetworkId"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the core network was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrEdges")
    def attr_edges(self) -> _IResolvable_da3f097b:
        '''The edges.

        :cloudformationAttribute: Edges
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrEdges"))

    @builtins.property
    @jsii.member(jsii_name="attrOwnerAccount")
    def attr_owner_account(self) -> builtins.str:
        '''Owner of the core network.

        :cloudformationAttribute: OwnerAccount
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerAccount"))

    @builtins.property
    @jsii.member(jsii_name="attrSegments")
    def attr_segments(self) -> _IResolvable_da3f097b:
        '''The segments.

        :cloudformationAttribute: Segments
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrSegments"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The current state of the core network.

        These states are: ``CREATING`` | ``UPDATING`` | ``AVAILABLE`` | ``DELETING`` .

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

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
    @jsii.member(jsii_name="globalNetworkId")
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network that your core network is a part of.'''
        return typing.cast(builtins.str, jsii.get(self, "globalNetworkId"))

    @global_network_id.setter
    def global_network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86408588b749b814a7197fcea933176b0c59fa27af364e497dd8c35db9c2767b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalNetworkId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of a core network.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd943ed85c9a7352421e16d77f69b1d40ca95e68eac8600af543194df8d324f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Any:
        '''Describes a core network policy.

        For more information, see `Core network policies <https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-change-sets.html>`_ .
        '''
        return typing.cast(typing.Any, jsii.get(self, "policyDocument"))

    @policy_document.setter
    def policy_document(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95fd0d184423074af0fbb9e444ffac5c0adbdbe161eb0520bbbd67705f54b4d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDocument", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of key-value tags associated with a core network.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96b99af1b4897054c775f7c57c33730e70cc058523a18542f6bac227d93d5e39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkmanager.CfnCoreNetwork.CoreNetworkEdgeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "asn": "asn",
            "edge_location": "edgeLocation",
            "inside_cidr_blocks": "insideCidrBlocks",
        },
    )
    class CoreNetworkEdgeProperty:
        def __init__(
            self,
            *,
            asn: typing.Optional[jsii.Number] = None,
            edge_location: typing.Optional[builtins.str] = None,
            inside_cidr_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Describes a core network edge.

            :param asn: The ASN of a core network edge.
            :param edge_location: The Region where a core network edge is located.
            :param inside_cidr_blocks: The inside IP addresses used for core network edges.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworkedge.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkmanager as networkmanager
                
                core_network_edge_property = networkmanager.CfnCoreNetwork.CoreNetworkEdgeProperty(
                    asn=123,
                    edge_location="edgeLocation",
                    inside_cidr_blocks=["insideCidrBlocks"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7fbb8f1859ef14e326882885a8fee653ca3ab95025fac14894453976df1d1187)
                check_type(argname="argument asn", value=asn, expected_type=type_hints["asn"])
                check_type(argname="argument edge_location", value=edge_location, expected_type=type_hints["edge_location"])
                check_type(argname="argument inside_cidr_blocks", value=inside_cidr_blocks, expected_type=type_hints["inside_cidr_blocks"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if asn is not None:
                self._values["asn"] = asn
            if edge_location is not None:
                self._values["edge_location"] = edge_location
            if inside_cidr_blocks is not None:
                self._values["inside_cidr_blocks"] = inside_cidr_blocks

        @builtins.property
        def asn(self) -> typing.Optional[jsii.Number]:
            '''The ASN of a core network edge.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworkedge.html#cfn-networkmanager-corenetwork-corenetworkedge-asn
            '''
            result = self._values.get("asn")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def edge_location(self) -> typing.Optional[builtins.str]:
            '''The Region where a core network edge is located.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworkedge.html#cfn-networkmanager-corenetwork-corenetworkedge-edgelocation
            '''
            result = self._values.get("edge_location")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inside_cidr_blocks(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The inside IP addresses used for core network edges.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworkedge.html#cfn-networkmanager-corenetwork-corenetworkedge-insidecidrblocks
            '''
            result = self._values.get("inside_cidr_blocks")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CoreNetworkEdgeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkmanager.CfnCoreNetwork.CoreNetworkSegmentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "edge_locations": "edgeLocations",
            "name": "name",
            "shared_segments": "sharedSegments",
        },
    )
    class CoreNetworkSegmentProperty:
        def __init__(
            self,
            *,
            edge_locations: typing.Optional[typing.Sequence[builtins.str]] = None,
            name: typing.Optional[builtins.str] = None,
            shared_segments: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Describes a core network segment, which are dedicated routes.

            Only attachments within this segment can communicate with each other.

            :param edge_locations: The Regions where the edges are located.
            :param name: The name of a core network segment.
            :param shared_segments: The shared segments of a core network.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworksegment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkmanager as networkmanager
                
                core_network_segment_property = networkmanager.CfnCoreNetwork.CoreNetworkSegmentProperty(
                    edge_locations=["edgeLocations"],
                    name="name",
                    shared_segments=["sharedSegments"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__935d45f9acdf79c9cd7e8fd50a27ef19f966892baf4d9d758c80af0c36b222e0)
                check_type(argname="argument edge_locations", value=edge_locations, expected_type=type_hints["edge_locations"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument shared_segments", value=shared_segments, expected_type=type_hints["shared_segments"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if edge_locations is not None:
                self._values["edge_locations"] = edge_locations
            if name is not None:
                self._values["name"] = name
            if shared_segments is not None:
                self._values["shared_segments"] = shared_segments

        @builtins.property
        def edge_locations(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The Regions where the edges are located.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworksegment.html#cfn-networkmanager-corenetwork-corenetworksegment-edgelocations
            '''
            result = self._values.get("edge_locations")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of a core network segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworksegment.html#cfn-networkmanager-corenetwork-corenetworksegment-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def shared_segments(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The shared segments of a core network.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-corenetwork-corenetworksegment.html#cfn-networkmanager-corenetwork-corenetworksegment-sharedsegments
            '''
            result = self._values.get("shared_segments")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CoreNetworkSegmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnCoreNetworkProps",
    jsii_struct_bases=[],
    name_mapping={
        "global_network_id": "globalNetworkId",
        "description": "description",
        "policy_document": "policyDocument",
        "tags": "tags",
    },
)
class CfnCoreNetworkProps:
    def __init__(
        self,
        *,
        global_network_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        policy_document: typing.Any = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCoreNetwork``.

        :param global_network_id: The ID of the global network that your core network is a part of.
        :param description: The description of a core network.
        :param policy_document: Describes a core network policy. For more information, see `Core network policies <https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-change-sets.html>`_ . If you update the policy document, CloudFormation will apply the core network change set generated from the updated policy document, and then set it as the LIVE policy.
        :param tags: The list of key-value tags associated with a core network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-corenetwork.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            # policy_document: Any
            
            cfn_core_network_props = networkmanager.CfnCoreNetworkProps(
                global_network_id="globalNetworkId",
            
                # the properties below are optional
                description="description",
                policy_document=policy_document,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__153eb0a5a16cd071b499d3d1d86d232667e61cbcf2cfa1cc52e04a3afcc48c15)
            check_type(argname="argument global_network_id", value=global_network_id, expected_type=type_hints["global_network_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "global_network_id": global_network_id,
        }
        if description is not None:
            self._values["description"] = description
        if policy_document is not None:
            self._values["policy_document"] = policy_document
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network that your core network is a part of.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-corenetwork.html#cfn-networkmanager-corenetwork-globalnetworkid
        '''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of a core network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-corenetwork.html#cfn-networkmanager-corenetwork-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy_document(self) -> typing.Any:
        '''Describes a core network policy. For more information, see `Core network policies <https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-change-sets.html>`_ .

        If you update the policy document, CloudFormation will apply the core network change set generated from the updated policy document, and then set it as the LIVE policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-corenetwork.html#cfn-networkmanager-corenetwork-policydocument
        '''
        result = self._values.get("policy_document")
        return typing.cast(typing.Any, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of key-value tags associated with a core network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-corenetwork.html#cfn-networkmanager-corenetwork-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCoreNetworkProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnCustomerGatewayAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnCustomerGatewayAssociation",
):
    '''Specifies an association between a customer gateway, a device, and optionally, a link.

    If you specify a link, it must be associated with the specified device. The customer gateway must be connected to a VPN attachment on a transit gateway that's registered in your global network.

    You cannot associate a customer gateway with more than one device and link.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        cfn_customer_gateway_association = networkmanager.CfnCustomerGatewayAssociation(self, "MyCfnCustomerGatewayAssociation",
            customer_gateway_arn="customerGatewayArn",
            device_id="deviceId",
            global_network_id="globalNetworkId",
        
            # the properties below are optional
            link_id="linkId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        customer_gateway_arn: builtins.str,
        device_id: builtins.str,
        global_network_id: builtins.str,
        link_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param customer_gateway_arn: The Amazon Resource Name (ARN) of the customer gateway.
        :param device_id: The ID of the device.
        :param global_network_id: The ID of the global network.
        :param link_id: The ID of the link.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8530cc09738d1161c48c06739c9d69bc634930a0d627d82903f1538ebcf9311)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCustomerGatewayAssociationProps(
            customer_gateway_arn=customer_gateway_arn,
            device_id=device_id,
            global_network_id=global_network_id,
            link_id=link_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76fdbb6c450fbfa3056f4acf441be5bffc42673ec2dfe0703ea52c261027d133)
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
            type_hints = typing.get_type_hints(_typecheckingstub__011cc1dd9dedcd5ceb6fd112e35fb270aa4dbdbcb47c0083f341fcaae13d391c)
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
    @jsii.member(jsii_name="customerGatewayArn")
    def customer_gateway_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the customer gateway.'''
        return typing.cast(builtins.str, jsii.get(self, "customerGatewayArn"))

    @customer_gateway_arn.setter
    def customer_gateway_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f23e31195cfb70367760a032bd3771e71ab9a3e41af843be539654bd26f895a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerGatewayArn", value)

    @builtins.property
    @jsii.member(jsii_name="deviceId")
    def device_id(self) -> builtins.str:
        '''The ID of the device.'''
        return typing.cast(builtins.str, jsii.get(self, "deviceId"))

    @device_id.setter
    def device_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b65adc2efb3c3657aee3b06f73070c15bae503de5f5b47afedb7a41ddb49d96a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceId", value)

    @builtins.property
    @jsii.member(jsii_name="globalNetworkId")
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network.'''
        return typing.cast(builtins.str, jsii.get(self, "globalNetworkId"))

    @global_network_id.setter
    def global_network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b47d831038fea5cc72a69621a49acee67d94496b914cdf714d36f59c8572340)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalNetworkId", value)

    @builtins.property
    @jsii.member(jsii_name="linkId")
    def link_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the link.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "linkId"))

    @link_id.setter
    def link_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f1a9d0d94d8a37a3549e10ffcd4469d4dd99b00032e3bfcfe63c53b1b505a80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnCustomerGatewayAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "customer_gateway_arn": "customerGatewayArn",
        "device_id": "deviceId",
        "global_network_id": "globalNetworkId",
        "link_id": "linkId",
    },
)
class CfnCustomerGatewayAssociationProps:
    def __init__(
        self,
        *,
        customer_gateway_arn: builtins.str,
        device_id: builtins.str,
        global_network_id: builtins.str,
        link_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnCustomerGatewayAssociation``.

        :param customer_gateway_arn: The Amazon Resource Name (ARN) of the customer gateway.
        :param device_id: The ID of the device.
        :param global_network_id: The ID of the global network.
        :param link_id: The ID of the link.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            cfn_customer_gateway_association_props = networkmanager.CfnCustomerGatewayAssociationProps(
                customer_gateway_arn="customerGatewayArn",
                device_id="deviceId",
                global_network_id="globalNetworkId",
            
                # the properties below are optional
                link_id="linkId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eec004eba5efaff43d4770c050984dada45fff22cb42feef066ca3d48d22ad62)
            check_type(argname="argument customer_gateway_arn", value=customer_gateway_arn, expected_type=type_hints["customer_gateway_arn"])
            check_type(argname="argument device_id", value=device_id, expected_type=type_hints["device_id"])
            check_type(argname="argument global_network_id", value=global_network_id, expected_type=type_hints["global_network_id"])
            check_type(argname="argument link_id", value=link_id, expected_type=type_hints["link_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "customer_gateway_arn": customer_gateway_arn,
            "device_id": device_id,
            "global_network_id": global_network_id,
        }
        if link_id is not None:
            self._values["link_id"] = link_id

    @builtins.property
    def customer_gateway_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the customer gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-customergatewayarn
        '''
        result = self._values.get("customer_gateway_arn")
        assert result is not None, "Required property 'customer_gateway_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def device_id(self) -> builtins.str:
        '''The ID of the device.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-deviceid
        '''
        result = self._values.get("device_id")
        assert result is not None, "Required property 'device_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-globalnetworkid
        '''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def link_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the link.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html#cfn-networkmanager-customergatewayassociation-linkid
        '''
        result = self._values.get("link_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCustomerGatewayAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDevice(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnDevice",
):
    '''Specifies a device.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        cfn_device = networkmanager.CfnDevice(self, "MyCfnDevice",
            global_network_id="globalNetworkId",
        
            # the properties below are optional
            aws_location=networkmanager.CfnDevice.AWSLocationProperty(
                subnet_arn="subnetArn",
                zone="zone"
            ),
            description="description",
            location=networkmanager.CfnDevice.LocationProperty(
                address="address",
                latitude="latitude",
                longitude="longitude"
            ),
            model="model",
            serial_number="serialNumber",
            site_id="siteId",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            type="type",
            vendor="vendor"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        global_network_id: builtins.str,
        aws_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDevice.AWSLocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDevice.LocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        model: typing.Optional[builtins.str] = None,
        serial_number: typing.Optional[builtins.str] = None,
        site_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
        vendor: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param global_network_id: The ID of the global network.
        :param aws_location: The Amazon Web Services location of the device, if applicable.
        :param description: A description of the device. Constraints: Maximum length of 256 characters.
        :param location: The site location.
        :param model: The model of the device. Constraints: Maximum length of 128 characters.
        :param serial_number: The serial number of the device. Constraints: Maximum length of 128 characters.
        :param site_id: The site ID.
        :param tags: The tags for the device.
        :param type: The device type.
        :param vendor: The vendor of the device. Constraints: Maximum length of 128 characters.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ad564c84e64f3433b234887d19dd14a76b326ebbe6db1b2c11c4e75c1bb9111)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDeviceProps(
            global_network_id=global_network_id,
            aws_location=aws_location,
            description=description,
            location=location,
            model=model,
            serial_number=serial_number,
            site_id=site_id,
            tags=tags,
            type=type,
            vendor=vendor,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__681ebe70583a2bd7db602c1014aaeb6e8470966be63f6b5f27003ab0c22980fa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4c9df1ab9e4ab9cd8105624838a2ce4542052964f13801c0ab69b542ef8a1700)
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
        '''The date and time that the device was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrDeviceArn")
    def attr_device_arn(self) -> builtins.str:
        '''The ARN of the device.

        For example, ``arn:aws:networkmanager::123456789012:device/global-network-01231231231231231/device-07f6fd08867abc123`` .

        :cloudformationAttribute: DeviceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDeviceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDeviceId")
    def attr_device_id(self) -> builtins.str:
        '''The ID of the device.

        For example, ``device-07f6fd08867abc123`` .

        :cloudformationAttribute: DeviceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDeviceId"))

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
    @jsii.member(jsii_name="globalNetworkId")
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network.'''
        return typing.cast(builtins.str, jsii.get(self, "globalNetworkId"))

    @global_network_id.setter
    def global_network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfe93f5f35db9797ee30d721c0dc9a87d465bbfaee9d289f745d2ec564240fc8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalNetworkId", value)

    @builtins.property
    @jsii.member(jsii_name="awsLocation")
    def aws_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDevice.AWSLocationProperty"]]:
        '''The Amazon Web Services location of the device, if applicable.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDevice.AWSLocationProperty"]], jsii.get(self, "awsLocation"))

    @aws_location.setter
    def aws_location(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDevice.AWSLocationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4583117af731ea782790ab60127926847bd464d6c6710eae89844bbfd59bb491)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsLocation", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the device.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e735fe734530f45aa89056e48a9a7241fe5d210c4f83b0fad47adf9be3677fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDevice.LocationProperty"]]:
        '''The site location.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDevice.LocationProperty"]], jsii.get(self, "location"))

    @location.setter
    def location(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDevice.LocationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b88d3e1b4865be708f6cc69c3a68a598b6d1f850245deb4c3da99d1a4a2a4a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="model")
    def model(self) -> typing.Optional[builtins.str]:
        '''The model of the device.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "model"))

    @model.setter
    def model(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af59216267fbe291d9a86c89712257d97c0d6866de65577764718a5ab20e656f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "model", value)

    @builtins.property
    @jsii.member(jsii_name="serialNumber")
    def serial_number(self) -> typing.Optional[builtins.str]:
        '''The serial number of the device.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serialNumber"))

    @serial_number.setter
    def serial_number(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__391e1294cca69f190d4b32c42e15faead42d783500f2807a30c3f0ab04e10580)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serialNumber", value)

    @builtins.property
    @jsii.member(jsii_name="siteId")
    def site_id(self) -> typing.Optional[builtins.str]:
        '''The site ID.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "siteId"))

    @site_id.setter
    def site_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d356eccb03811c1a8c04efa44c470e4d99c9e5426ac16419449ff2c9e066b2e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "siteId", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the device.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26c263b233a1cae0165c1b45058ac8409a2bfaff22af7d0609a990d166cef3fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''The device type.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c61590f79bc7db569a8dd74aab8282cec9db607de9dca86bfdb39ebe67ec719)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="vendor")
    def vendor(self) -> typing.Optional[builtins.str]:
        '''The vendor of the device.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vendor"))

    @vendor.setter
    def vendor(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dfaeac3f3ef9890082ea071cb4a3ac124e205509c2a2fe6537128d482a516ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vendor", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkmanager.CfnDevice.AWSLocationProperty",
        jsii_struct_bases=[],
        name_mapping={"subnet_arn": "subnetArn", "zone": "zone"},
    )
    class AWSLocationProperty:
        def __init__(
            self,
            *,
            subnet_arn: typing.Optional[builtins.str] = None,
            zone: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The Amazon Web Services location of the device, if applicable.

            :param subnet_arn: The Amazon Resource Name (ARN) of the subnet that the device is located in.
            :param zone: The Zone that the device is located in. Specify the ID of an Availability Zone, Local Zone, Wavelength Zone, or an Outpost.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-awslocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkmanager as networkmanager
                
                a_wSLocation_property = networkmanager.CfnDevice.AWSLocationProperty(
                    subnet_arn="subnetArn",
                    zone="zone"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aef84c7e0700dce028a9d7b943fcbc3917928af3851e826cc4e321829d809a40)
                check_type(argname="argument subnet_arn", value=subnet_arn, expected_type=type_hints["subnet_arn"])
                check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if subnet_arn is not None:
                self._values["subnet_arn"] = subnet_arn
            if zone is not None:
                self._values["zone"] = zone

        @builtins.property
        def subnet_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the subnet that the device is located in.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-awslocation.html#cfn-networkmanager-device-awslocation-subnetarn
            '''
            result = self._values.get("subnet_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def zone(self) -> typing.Optional[builtins.str]:
            '''The Zone that the device is located in.

            Specify the ID of an Availability Zone, Local Zone, Wavelength Zone, or an Outpost.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-awslocation.html#cfn-networkmanager-device-awslocation-zone
            '''
            result = self._values.get("zone")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AWSLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkmanager.CfnDevice.LocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "address": "address",
            "latitude": "latitude",
            "longitude": "longitude",
        },
    )
    class LocationProperty:
        def __init__(
            self,
            *,
            address: typing.Optional[builtins.str] = None,
            latitude: typing.Optional[builtins.str] = None,
            longitude: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes a location.

            :param address: The physical address.
            :param latitude: The latitude.
            :param longitude: The longitude.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkmanager as networkmanager
                
                location_property = networkmanager.CfnDevice.LocationProperty(
                    address="address",
                    latitude="latitude",
                    longitude="longitude"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c70126f53370661902dca458745ecdc5b30b4ec88d37a1f028e6fb646c83d696)
                check_type(argname="argument address", value=address, expected_type=type_hints["address"])
                check_type(argname="argument latitude", value=latitude, expected_type=type_hints["latitude"])
                check_type(argname="argument longitude", value=longitude, expected_type=type_hints["longitude"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if address is not None:
                self._values["address"] = address
            if latitude is not None:
                self._values["latitude"] = latitude
            if longitude is not None:
                self._values["longitude"] = longitude

        @builtins.property
        def address(self) -> typing.Optional[builtins.str]:
            '''The physical address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html#cfn-networkmanager-device-location-address
            '''
            result = self._values.get("address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def latitude(self) -> typing.Optional[builtins.str]:
            '''The latitude.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html#cfn-networkmanager-device-location-latitude
            '''
            result = self._values.get("latitude")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def longitude(self) -> typing.Optional[builtins.str]:
            '''The longitude.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-device-location.html#cfn-networkmanager-device-location-longitude
            '''
            result = self._values.get("longitude")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnDeviceProps",
    jsii_struct_bases=[],
    name_mapping={
        "global_network_id": "globalNetworkId",
        "aws_location": "awsLocation",
        "description": "description",
        "location": "location",
        "model": "model",
        "serial_number": "serialNumber",
        "site_id": "siteId",
        "tags": "tags",
        "type": "type",
        "vendor": "vendor",
    },
)
class CfnDeviceProps:
    def __init__(
        self,
        *,
        global_network_id: builtins.str,
        aws_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDevice.AWSLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDevice.LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        model: typing.Optional[builtins.str] = None,
        serial_number: typing.Optional[builtins.str] = None,
        site_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
        vendor: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnDevice``.

        :param global_network_id: The ID of the global network.
        :param aws_location: The Amazon Web Services location of the device, if applicable.
        :param description: A description of the device. Constraints: Maximum length of 256 characters.
        :param location: The site location.
        :param model: The model of the device. Constraints: Maximum length of 128 characters.
        :param serial_number: The serial number of the device. Constraints: Maximum length of 128 characters.
        :param site_id: The site ID.
        :param tags: The tags for the device.
        :param type: The device type.
        :param vendor: The vendor of the device. Constraints: Maximum length of 128 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            cfn_device_props = networkmanager.CfnDeviceProps(
                global_network_id="globalNetworkId",
            
                # the properties below are optional
                aws_location=networkmanager.CfnDevice.AWSLocationProperty(
                    subnet_arn="subnetArn",
                    zone="zone"
                ),
                description="description",
                location=networkmanager.CfnDevice.LocationProperty(
                    address="address",
                    latitude="latitude",
                    longitude="longitude"
                ),
                model="model",
                serial_number="serialNumber",
                site_id="siteId",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                type="type",
                vendor="vendor"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__214d65d41aacb7028ea3820823a63765a7ea304d6d4501f238a41dd41254186e)
            check_type(argname="argument global_network_id", value=global_network_id, expected_type=type_hints["global_network_id"])
            check_type(argname="argument aws_location", value=aws_location, expected_type=type_hints["aws_location"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument model", value=model, expected_type=type_hints["model"])
            check_type(argname="argument serial_number", value=serial_number, expected_type=type_hints["serial_number"])
            check_type(argname="argument site_id", value=site_id, expected_type=type_hints["site_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument vendor", value=vendor, expected_type=type_hints["vendor"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "global_network_id": global_network_id,
        }
        if aws_location is not None:
            self._values["aws_location"] = aws_location
        if description is not None:
            self._values["description"] = description
        if location is not None:
            self._values["location"] = location
        if model is not None:
            self._values["model"] = model
        if serial_number is not None:
            self._values["serial_number"] = serial_number
        if site_id is not None:
            self._values["site_id"] = site_id
        if tags is not None:
            self._values["tags"] = tags
        if type is not None:
            self._values["type"] = type
        if vendor is not None:
            self._values["vendor"] = vendor

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-globalnetworkid
        '''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDevice.AWSLocationProperty]]:
        '''The Amazon Web Services location of the device, if applicable.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-awslocation
        '''
        result = self._values.get("aws_location")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDevice.AWSLocationProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the device.

        Constraints: Maximum length of 256 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDevice.LocationProperty]]:
        '''The site location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-location
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDevice.LocationProperty]], result)

    @builtins.property
    def model(self) -> typing.Optional[builtins.str]:
        '''The model of the device.

        Constraints: Maximum length of 128 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-model
        '''
        result = self._values.get("model")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def serial_number(self) -> typing.Optional[builtins.str]:
        '''The serial number of the device.

        Constraints: Maximum length of 128 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-serialnumber
        '''
        result = self._values.get("serial_number")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def site_id(self) -> typing.Optional[builtins.str]:
        '''The site ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-siteid
        '''
        result = self._values.get("site_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the device.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The device type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vendor(self) -> typing.Optional[builtins.str]:
        '''The vendor of the device.

        Constraints: Maximum length of 128 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html#cfn-networkmanager-device-vendor
        '''
        result = self._values.get("vendor")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeviceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnGlobalNetwork(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnGlobalNetwork",
):
    '''Creates a new, empty global network.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        cfn_global_network = networkmanager.CfnGlobalNetwork(self, "MyCfnGlobalNetwork",
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
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param description: A description of the global network. Constraints: Maximum length of 256 characters.
        :param tags: The tags for the global network.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcd77a1264244ecd5c8ad8fbf6038975eda0a4a49d5da9ba92306e218841f74f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGlobalNetworkProps(description=description, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a4d6bdc69ded81dc7371bcc908a8c470d45d7400be9b04c8aab8fda39abcee9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4a1cf0c8bf170de7441b97dd3d9ba7d4a7ca45d0d94c6f2c0053236748c5531d)
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
        '''The ARN of the global network.

        For example, ``arn:aws:networkmanager::123456789012:global-network/global-network-01231231231231231`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the global network.

        For example, ``global-network-01231231231231231`` .

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
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the global network.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19a1a1c3b45eed0a10e7c5e3bb7a960be34852e62b1241a92db880448eba0301)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the global network.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e1af222068741701cde749bdf31ed3994009b5ed482f7ae4e4901c954d350ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnGlobalNetworkProps",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "tags": "tags"},
)
class CfnGlobalNetworkProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnGlobalNetwork``.

        :param description: A description of the global network. Constraints: Maximum length of 256 characters.
        :param tags: The tags for the global network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            cfn_global_network_props = networkmanager.CfnGlobalNetworkProps(
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d4e8224b803ee7837da430965223a7bb5cc1d471fadf277c44910dc5f851005)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the global network.

        Constraints: Maximum length of 256 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html#cfn-networkmanager-globalnetwork-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the global network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html#cfn-networkmanager-globalnetwork-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGlobalNetworkProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnLink(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnLink",
):
    '''Specifies a link for a site.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        cfn_link = networkmanager.CfnLink(self, "MyCfnLink",
            bandwidth=networkmanager.CfnLink.BandwidthProperty(
                download_speed=123,
                upload_speed=123
            ),
            global_network_id="globalNetworkId",
            site_id="siteId",
        
            # the properties below are optional
            description="description",
            provider="provider",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            type="type"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        bandwidth: typing.Union[_IResolvable_da3f097b, typing.Union["CfnLink.BandwidthProperty", typing.Dict[builtins.str, typing.Any]]],
        global_network_id: builtins.str,
        site_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        provider: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param bandwidth: The bandwidth for the link.
        :param global_network_id: The ID of the global network.
        :param site_id: The ID of the site.
        :param description: A description of the link. Constraints: Maximum length of 256 characters.
        :param provider: The provider of the link. Constraints: Maximum length of 128 characters. Cannot include the following characters: | \\ ^
        :param tags: The tags for the link.
        :param type: The type of the link. Constraints: Maximum length of 128 characters. Cannot include the following characters: | \\ ^
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a85b1ccff185ece01ba7173d98d2c10359b58386e88607b0ea915c94a4650cdd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLinkProps(
            bandwidth=bandwidth,
            global_network_id=global_network_id,
            site_id=site_id,
            description=description,
            provider=provider,
            tags=tags,
            type=type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7013af1fb84ea807547650ea0acaaf21554964c39b4664177013638d646dc4d2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__928a1929b4243ced484546933d81b0b53abb5463d5f704ef92ac52897599ad66)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrLinkArn")
    def attr_link_arn(self) -> builtins.str:
        '''The ARN of the link.

        For example, ``arn:aws:networkmanager::123456789012:link/global-network-01231231231231231/link-11112222aaaabbbb1`` .

        :cloudformationAttribute: LinkArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLinkArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLinkId")
    def attr_link_id(self) -> builtins.str:
        '''The ID of the link.

        For example, ``link-11112222aaaabbbb1`` .

        :cloudformationAttribute: LinkId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLinkId"))

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
    @jsii.member(jsii_name="bandwidth")
    def bandwidth(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnLink.BandwidthProperty"]:
        '''The bandwidth for the link.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnLink.BandwidthProperty"], jsii.get(self, "bandwidth"))

    @bandwidth.setter
    def bandwidth(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnLink.BandwidthProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__988888cdb37dacfb2adb77af73f778a15dd9db7b8586f6a4a0748cc7ae082b96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bandwidth", value)

    @builtins.property
    @jsii.member(jsii_name="globalNetworkId")
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network.'''
        return typing.cast(builtins.str, jsii.get(self, "globalNetworkId"))

    @global_network_id.setter
    def global_network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5259ab5861d067f6495afc71e1f3826c064c92b18d3401e69328a415b375f60b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalNetworkId", value)

    @builtins.property
    @jsii.member(jsii_name="siteId")
    def site_id(self) -> builtins.str:
        '''The ID of the site.'''
        return typing.cast(builtins.str, jsii.get(self, "siteId"))

    @site_id.setter
    def site_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__820ae0c9b3b49e33e7da67095da21a8f43e171b3d4aae4e715300b82480190f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "siteId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the link.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c24e7374c54735ea9b48c8a23a947605911fd130fd389dcc21e481484b5ca689)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="provider")
    def provider(self) -> typing.Optional[builtins.str]:
        '''The provider of the link.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "provider"))

    @provider.setter
    def provider(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51a319abdcd33f238855c8baffca80d87f52d9a8d1ee39a68ebd9fa1f1b6a1ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provider", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the link.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3d04cb05f180d4cf6476de9fd9cb617bb7f8aafae4932b64bf61314e0e8bdf5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of the link.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9091a25b0a2281020308a09f55e57da148e2f12e522813a9ad84ab34db3d06a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkmanager.CfnLink.BandwidthProperty",
        jsii_struct_bases=[],
        name_mapping={
            "download_speed": "downloadSpeed",
            "upload_speed": "uploadSpeed",
        },
    )
    class BandwidthProperty:
        def __init__(
            self,
            *,
            download_speed: typing.Optional[jsii.Number] = None,
            upload_speed: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes bandwidth information.

            :param download_speed: Download speed in Mbps.
            :param upload_speed: Upload speed in Mbps.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-link-bandwidth.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkmanager as networkmanager
                
                bandwidth_property = networkmanager.CfnLink.BandwidthProperty(
                    download_speed=123,
                    upload_speed=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3a21a41aa06c59bba0d07e362c3f22e406cbe06a4eacb6a820867b23316cc7f2)
                check_type(argname="argument download_speed", value=download_speed, expected_type=type_hints["download_speed"])
                check_type(argname="argument upload_speed", value=upload_speed, expected_type=type_hints["upload_speed"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if download_speed is not None:
                self._values["download_speed"] = download_speed
            if upload_speed is not None:
                self._values["upload_speed"] = upload_speed

        @builtins.property
        def download_speed(self) -> typing.Optional[jsii.Number]:
            '''Download speed in Mbps.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-link-bandwidth.html#cfn-networkmanager-link-bandwidth-downloadspeed
            '''
            result = self._values.get("download_speed")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def upload_speed(self) -> typing.Optional[jsii.Number]:
            '''Upload speed in Mbps.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-link-bandwidth.html#cfn-networkmanager-link-bandwidth-uploadspeed
            '''
            result = self._values.get("upload_speed")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BandwidthProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnLinkAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnLinkAssociation",
):
    '''Describes the association between a device and a link.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        cfn_link_association = networkmanager.CfnLinkAssociation(self, "MyCfnLinkAssociation",
            device_id="deviceId",
            global_network_id="globalNetworkId",
            link_id="linkId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        device_id: builtins.str,
        global_network_id: builtins.str,
        link_id: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param device_id: The device ID for the link association.
        :param global_network_id: The ID of the global network.
        :param link_id: The ID of the link.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__592b4a4bb0948269132e914835a818ca4909b73e88f0d3cfeeea0fb241485511)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLinkAssociationProps(
            device_id=device_id, global_network_id=global_network_id, link_id=link_id
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__193a8eac91ef709592b8ccf2b0620553a807381f865616069b571a5a14ff02d1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6c6cff788e17dcd4c0aa7bce78dbc0573997ce9011f9ee8444cea36c3274115e)
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
    @jsii.member(jsii_name="deviceId")
    def device_id(self) -> builtins.str:
        '''The device ID for the link association.'''
        return typing.cast(builtins.str, jsii.get(self, "deviceId"))

    @device_id.setter
    def device_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed1cdb15e97d2900717e8b201967996154300677713c8143598891b7d417d675)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceId", value)

    @builtins.property
    @jsii.member(jsii_name="globalNetworkId")
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network.'''
        return typing.cast(builtins.str, jsii.get(self, "globalNetworkId"))

    @global_network_id.setter
    def global_network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96f86556261820395986ba7acbd7b8156cfa0a1672e1c38e2bb4cf7cd9c5fad1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalNetworkId", value)

    @builtins.property
    @jsii.member(jsii_name="linkId")
    def link_id(self) -> builtins.str:
        '''The ID of the link.'''
        return typing.cast(builtins.str, jsii.get(self, "linkId"))

    @link_id.setter
    def link_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67215c31eae75fa556251496e69b477a798d5564fa5dc3454d37ea75d2afe359)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnLinkAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "device_id": "deviceId",
        "global_network_id": "globalNetworkId",
        "link_id": "linkId",
    },
)
class CfnLinkAssociationProps:
    def __init__(
        self,
        *,
        device_id: builtins.str,
        global_network_id: builtins.str,
        link_id: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnLinkAssociation``.

        :param device_id: The device ID for the link association.
        :param global_network_id: The ID of the global network.
        :param link_id: The ID of the link.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            cfn_link_association_props = networkmanager.CfnLinkAssociationProps(
                device_id="deviceId",
                global_network_id="globalNetworkId",
                link_id="linkId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__687ba637c511969867f98bb143efd0735e1b70c11d4e7819f7a1815b3b809b32)
            check_type(argname="argument device_id", value=device_id, expected_type=type_hints["device_id"])
            check_type(argname="argument global_network_id", value=global_network_id, expected_type=type_hints["global_network_id"])
            check_type(argname="argument link_id", value=link_id, expected_type=type_hints["link_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "device_id": device_id,
            "global_network_id": global_network_id,
            "link_id": link_id,
        }

    @builtins.property
    def device_id(self) -> builtins.str:
        '''The device ID for the link association.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html#cfn-networkmanager-linkassociation-deviceid
        '''
        result = self._values.get("device_id")
        assert result is not None, "Required property 'device_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html#cfn-networkmanager-linkassociation-globalnetworkid
        '''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def link_id(self) -> builtins.str:
        '''The ID of the link.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html#cfn-networkmanager-linkassociation-linkid
        '''
        result = self._values.get("link_id")
        assert result is not None, "Required property 'link_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinkAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnLinkProps",
    jsii_struct_bases=[],
    name_mapping={
        "bandwidth": "bandwidth",
        "global_network_id": "globalNetworkId",
        "site_id": "siteId",
        "description": "description",
        "provider": "provider",
        "tags": "tags",
        "type": "type",
    },
)
class CfnLinkProps:
    def __init__(
        self,
        *,
        bandwidth: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLink.BandwidthProperty, typing.Dict[builtins.str, typing.Any]]],
        global_network_id: builtins.str,
        site_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        provider: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnLink``.

        :param bandwidth: The bandwidth for the link.
        :param global_network_id: The ID of the global network.
        :param site_id: The ID of the site.
        :param description: A description of the link. Constraints: Maximum length of 256 characters.
        :param provider: The provider of the link. Constraints: Maximum length of 128 characters. Cannot include the following characters: | \\ ^
        :param tags: The tags for the link.
        :param type: The type of the link. Constraints: Maximum length of 128 characters. Cannot include the following characters: | \\ ^

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            cfn_link_props = networkmanager.CfnLinkProps(
                bandwidth=networkmanager.CfnLink.BandwidthProperty(
                    download_speed=123,
                    upload_speed=123
                ),
                global_network_id="globalNetworkId",
                site_id="siteId",
            
                # the properties below are optional
                description="description",
                provider="provider",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                type="type"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cefe7342b597379997b369b9f4aa644a8902928545cfe9bb1b97c6c52cffdc09)
            check_type(argname="argument bandwidth", value=bandwidth, expected_type=type_hints["bandwidth"])
            check_type(argname="argument global_network_id", value=global_network_id, expected_type=type_hints["global_network_id"])
            check_type(argname="argument site_id", value=site_id, expected_type=type_hints["site_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bandwidth": bandwidth,
            "global_network_id": global_network_id,
            "site_id": site_id,
        }
        if description is not None:
            self._values["description"] = description
        if provider is not None:
            self._values["provider"] = provider
        if tags is not None:
            self._values["tags"] = tags
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def bandwidth(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnLink.BandwidthProperty]:
        '''The bandwidth for the link.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-bandwidth
        '''
        result = self._values.get("bandwidth")
        assert result is not None, "Required property 'bandwidth' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnLink.BandwidthProperty], result)

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-globalnetworkid
        '''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def site_id(self) -> builtins.str:
        '''The ID of the site.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-siteid
        '''
        result = self._values.get("site_id")
        assert result is not None, "Required property 'site_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the link.

        Constraints: Maximum length of 256 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provider(self) -> typing.Optional[builtins.str]:
        '''The provider of the link.

        Constraints: Maximum length of 128 characters. Cannot include the following characters: | \\ ^

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-provider
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the link.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of the link.

        Constraints: Maximum length of 128 characters. Cannot include the following characters: | \\ ^

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html#cfn-networkmanager-link-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinkProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnSite(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnSite",
):
    '''Creates a new site in a global network.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        cfn_site = networkmanager.CfnSite(self, "MyCfnSite",
            global_network_id="globalNetworkId",
        
            # the properties below are optional
            description="description",
            location=networkmanager.CfnSite.LocationProperty(
                address="address",
                latitude="latitude",
                longitude="longitude"
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
        global_network_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSite.LocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param global_network_id: The ID of the global network.
        :param description: A description of your site. Constraints: Maximum length of 256 characters.
        :param location: The site location. This information is used for visualization in the Network Manager console. If you specify the address, the latitude and longitude are automatically calculated. - ``Address`` : The physical address of the site. - ``Latitude`` : The latitude of the site. - ``Longitude`` : The longitude of the site.
        :param tags: The tags for the site.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02d26caf3b597f4f3cac9111625d8131c4deeefd4ab607c87a0c1af546b9443d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSiteProps(
            global_network_id=global_network_id,
            description=description,
            location=location,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96fa61768102beaf099a9b62810c042cab8f1fbfda673150548342bfbd975456)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ef7c7e1062c44ef0b7feb9417caa96ed9f6d6b6d43b0dd03a5aa5b911cd74a1c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrSiteArn")
    def attr_site_arn(self) -> builtins.str:
        '''The ARN of the site.

        For example, ``arn:aws:networkmanager::123456789012:site/global-network-01231231231231231/site-444555aaabbb11223`` .

        :cloudformationAttribute: SiteArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSiteArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSiteId")
    def attr_site_id(self) -> builtins.str:
        '''The ID of the site.

        For example, ``site-444555aaabbb11223`` .

        :cloudformationAttribute: SiteId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSiteId"))

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
    @jsii.member(jsii_name="globalNetworkId")
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network.'''
        return typing.cast(builtins.str, jsii.get(self, "globalNetworkId"))

    @global_network_id.setter
    def global_network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc8803e9a4461e26d551cc4a419b4cd5d0bada265b033a999052a427929cfb6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalNetworkId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of your site.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46188c191417eab8a9ca7f0b8f39542585227143528c34a981df829dff8b3e73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSite.LocationProperty"]]:
        '''The site location.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSite.LocationProperty"]], jsii.get(self, "location"))

    @location.setter
    def location(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSite.LocationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9fbc23ce76923bed7902ba8ee0048c3665c496e695387f60a440db911264548)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the site.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4acfa4f7a596e57882e361fb67af36d8b498b641763fab5731de8c92e52197e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkmanager.CfnSite.LocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "address": "address",
            "latitude": "latitude",
            "longitude": "longitude",
        },
    )
    class LocationProperty:
        def __init__(
            self,
            *,
            address: typing.Optional[builtins.str] = None,
            latitude: typing.Optional[builtins.str] = None,
            longitude: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes a location.

            :param address: The physical address.
            :param latitude: The latitude.
            :param longitude: The longitude.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkmanager as networkmanager
                
                location_property = networkmanager.CfnSite.LocationProperty(
                    address="address",
                    latitude="latitude",
                    longitude="longitude"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__344f92c555fd2fc51fc42431c1ad3cd65a444ef3fa2fde5c0169d29240c01aaa)
                check_type(argname="argument address", value=address, expected_type=type_hints["address"])
                check_type(argname="argument latitude", value=latitude, expected_type=type_hints["latitude"])
                check_type(argname="argument longitude", value=longitude, expected_type=type_hints["longitude"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if address is not None:
                self._values["address"] = address
            if latitude is not None:
                self._values["latitude"] = latitude
            if longitude is not None:
                self._values["longitude"] = longitude

        @builtins.property
        def address(self) -> typing.Optional[builtins.str]:
            '''The physical address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html#cfn-networkmanager-site-location-address
            '''
            result = self._values.get("address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def latitude(self) -> typing.Optional[builtins.str]:
            '''The latitude.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html#cfn-networkmanager-site-location-latitude
            '''
            result = self._values.get("latitude")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def longitude(self) -> typing.Optional[builtins.str]:
            '''The longitude.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-site-location.html#cfn-networkmanager-site-location-longitude
            '''
            result = self._values.get("longitude")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnSiteProps",
    jsii_struct_bases=[],
    name_mapping={
        "global_network_id": "globalNetworkId",
        "description": "description",
        "location": "location",
        "tags": "tags",
    },
)
class CfnSiteProps:
    def __init__(
        self,
        *,
        global_network_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSite.LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSite``.

        :param global_network_id: The ID of the global network.
        :param description: A description of your site. Constraints: Maximum length of 256 characters.
        :param location: The site location. This information is used for visualization in the Network Manager console. If you specify the address, the latitude and longitude are automatically calculated. - ``Address`` : The physical address of the site. - ``Latitude`` : The latitude of the site. - ``Longitude`` : The longitude of the site.
        :param tags: The tags for the site.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            cfn_site_props = networkmanager.CfnSiteProps(
                global_network_id="globalNetworkId",
            
                # the properties below are optional
                description="description",
                location=networkmanager.CfnSite.LocationProperty(
                    address="address",
                    latitude="latitude",
                    longitude="longitude"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__912c70020ab3c3833a813b389454ccf6e661a3c53f4d78e732b56acd3d19510f)
            check_type(argname="argument global_network_id", value=global_network_id, expected_type=type_hints["global_network_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "global_network_id": global_network_id,
        }
        if description is not None:
            self._values["description"] = description
        if location is not None:
            self._values["location"] = location
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-globalnetworkid
        '''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of your site.

        Constraints: Maximum length of 256 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSite.LocationProperty]]:
        '''The site location.

        This information is used for visualization in the Network Manager console. If you specify the address, the latitude and longitude are automatically calculated.

        - ``Address`` : The physical address of the site.
        - ``Latitude`` : The latitude of the site.
        - ``Longitude`` : The longitude of the site.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-location
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSite.LocationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the site.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html#cfn-networkmanager-site-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSiteProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnSiteToSiteVpnAttachment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnSiteToSiteVpnAttachment",
):
    '''Creates an Amazon Web Services site-to-site VPN attachment on an edge location of a core network.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-sitetositevpnattachment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        cfn_site_to_site_vpn_attachment = networkmanager.CfnSiteToSiteVpnAttachment(self, "MyCfnSiteToSiteVpnAttachment",
            core_network_id="coreNetworkId",
            vpn_connection_arn="vpnConnectionArn",
        
            # the properties below are optional
            proposed_segment_change=networkmanager.CfnSiteToSiteVpnAttachment.ProposedSegmentChangeProperty(
                attachment_policy_rule_number=123,
                segment_name="segmentName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
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
        core_network_id: builtins.str,
        vpn_connection_arn: builtins.str,
        proposed_segment_change: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSiteToSiteVpnAttachment.ProposedSegmentChangeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param core_network_id: The ID of a core network where you're creating a site-to-site VPN attachment.
        :param vpn_connection_arn: The ARN of the site-to-site VPN attachment.
        :param proposed_segment_change: The attachment to move from one segment to another.
        :param tags: Tags for the attachment.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aabf08c6f82f3c177f73a39833791562d59537dbe20329f7f5c42adbe2b1f639)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSiteToSiteVpnAttachmentProps(
            core_network_id=core_network_id,
            vpn_connection_arn=vpn_connection_arn,
            proposed_segment_change=proposed_segment_change,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a153038e0b02e958bd16c723a6208f7c87539a3c7d5b6826d1e7a48d50c721fe)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3b47c74813a6cf63d4e08bfd46dc0c202c79ee346a65b09f04a4512be0f8e600)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAttachmentId")
    def attr_attachment_id(self) -> builtins.str:
        '''The ID of the site-to-site VPN attachment.

        :cloudformationAttribute: AttachmentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAttachmentId"))

    @builtins.property
    @jsii.member(jsii_name="attrAttachmentPolicyRuleNumber")
    def attr_attachment_policy_rule_number(self) -> jsii.Number:
        '''The policy rule number associated with the attachment.

        :cloudformationAttribute: AttachmentPolicyRuleNumber
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrAttachmentPolicyRuleNumber"))

    @builtins.property
    @jsii.member(jsii_name="attrAttachmentType")
    def attr_attachment_type(self) -> builtins.str:
        '''The type of attachment.

        This will be ``SITE_TO_SITE_VPN`` .

        :cloudformationAttribute: AttachmentType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAttachmentType"))

    @builtins.property
    @jsii.member(jsii_name="attrCoreNetworkArn")
    def attr_core_network_arn(self) -> builtins.str:
        '''The ARN of the core network.

        :cloudformationAttribute: CoreNetworkArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCoreNetworkArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the site-to-site VPN attachment was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrEdgeLocation")
    def attr_edge_location(self) -> builtins.str:
        '''The Region where the core network edge is located.

        :cloudformationAttribute: EdgeLocation
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEdgeLocation"))

    @builtins.property
    @jsii.member(jsii_name="attrOwnerAccountId")
    def attr_owner_account_id(self) -> builtins.str:
        '''The ID of the site-to-site VPN attachment owner.

        :cloudformationAttribute: OwnerAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerAccountId"))

    @builtins.property
    @jsii.member(jsii_name="attrResourceArn")
    def attr_resource_arn(self) -> builtins.str:
        '''The resource ARN for the site-to-site VPN attachment.

        :cloudformationAttribute: ResourceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSegmentName")
    def attr_segment_name(self) -> builtins.str:
        '''The name of the site-to-site VPN attachment's segment.

        :cloudformationAttribute: SegmentName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSegmentName"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The state of the site-to-site VPN attachment.

        This can be: ``REJECTED`` | ``PENDING_ATTACHMENT_ACCEPTANCE`` | ``CREATING`` | ``FAILED`` | ``AVAILABLE`` | ``UPDATING`` | ``PENDING_NETWORK_UPDATE`` | ``PENDING_TAG_ACCEPTANCE`` | ``DELETING`` .

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp when the site-to-site VPN attachment was last updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

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
    @jsii.member(jsii_name="coreNetworkId")
    def core_network_id(self) -> builtins.str:
        '''The ID of a core network where you're creating a site-to-site VPN attachment.'''
        return typing.cast(builtins.str, jsii.get(self, "coreNetworkId"))

    @core_network_id.setter
    def core_network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fba7832d3fd7c322d67c2d3ab554048476534725099669bbb27f6c353ee461a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coreNetworkId", value)

    @builtins.property
    @jsii.member(jsii_name="vpnConnectionArn")
    def vpn_connection_arn(self) -> builtins.str:
        '''The ARN of the site-to-site VPN attachment.'''
        return typing.cast(builtins.str, jsii.get(self, "vpnConnectionArn"))

    @vpn_connection_arn.setter
    def vpn_connection_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fde85f146ddbfe5918124ff34f04b28072bbe0389091946f95c9fe8cd8980f34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpnConnectionArn", value)

    @builtins.property
    @jsii.member(jsii_name="proposedSegmentChange")
    def proposed_segment_change(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSiteToSiteVpnAttachment.ProposedSegmentChangeProperty"]]:
        '''The attachment to move from one segment to another.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSiteToSiteVpnAttachment.ProposedSegmentChangeProperty"]], jsii.get(self, "proposedSegmentChange"))

    @proposed_segment_change.setter
    def proposed_segment_change(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSiteToSiteVpnAttachment.ProposedSegmentChangeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d5770719477965190780ebbb69883c941393da5c6c09af57bdb312f48810fbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proposedSegmentChange", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags for the attachment.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fedbd82359a7000ba160b74b2d678e59cb496867f32af82ab2500c7e1a61da46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkmanager.CfnSiteToSiteVpnAttachment.ProposedSegmentChangeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attachment_policy_rule_number": "attachmentPolicyRuleNumber",
            "segment_name": "segmentName",
            "tags": "tags",
        },
    )
    class ProposedSegmentChangeProperty:
        def __init__(
            self,
            *,
            attachment_policy_rule_number: typing.Optional[jsii.Number] = None,
            segment_name: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes a proposed segment change.

            In some cases, the segment change must first be evaluated and accepted.

            :param attachment_policy_rule_number: The rule number in the policy document that applies to this change.
            :param segment_name: The name of the segment to change.
            :param tags: The list of key-value tags that changed for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-sitetositevpnattachment-proposedsegmentchange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkmanager as networkmanager
                
                proposed_segment_change_property = networkmanager.CfnSiteToSiteVpnAttachment.ProposedSegmentChangeProperty(
                    attachment_policy_rule_number=123,
                    segment_name="segmentName",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__06bfa908f0244b4545d5fbff4fedab4e6c5def43fd0f8e30eee7f0c11bdf579d)
                check_type(argname="argument attachment_policy_rule_number", value=attachment_policy_rule_number, expected_type=type_hints["attachment_policy_rule_number"])
                check_type(argname="argument segment_name", value=segment_name, expected_type=type_hints["segment_name"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if attachment_policy_rule_number is not None:
                self._values["attachment_policy_rule_number"] = attachment_policy_rule_number
            if segment_name is not None:
                self._values["segment_name"] = segment_name
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def attachment_policy_rule_number(self) -> typing.Optional[jsii.Number]:
            '''The rule number in the policy document that applies to this change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-sitetositevpnattachment-proposedsegmentchange.html#cfn-networkmanager-sitetositevpnattachment-proposedsegmentchange-attachmentpolicyrulenumber
            '''
            result = self._values.get("attachment_policy_rule_number")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def segment_name(self) -> typing.Optional[builtins.str]:
            '''The name of the segment to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-sitetositevpnattachment-proposedsegmentchange.html#cfn-networkmanager-sitetositevpnattachment-proposedsegmentchange-segmentname
            '''
            result = self._values.get("segment_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
            '''The list of key-value tags that changed for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-sitetositevpnattachment-proposedsegmentchange.html#cfn-networkmanager-sitetositevpnattachment-proposedsegmentchange-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProposedSegmentChangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnSiteToSiteVpnAttachmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "core_network_id": "coreNetworkId",
        "vpn_connection_arn": "vpnConnectionArn",
        "proposed_segment_change": "proposedSegmentChange",
        "tags": "tags",
    },
)
class CfnSiteToSiteVpnAttachmentProps:
    def __init__(
        self,
        *,
        core_network_id: builtins.str,
        vpn_connection_arn: builtins.str,
        proposed_segment_change: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSiteToSiteVpnAttachment.ProposedSegmentChangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSiteToSiteVpnAttachment``.

        :param core_network_id: The ID of a core network where you're creating a site-to-site VPN attachment.
        :param vpn_connection_arn: The ARN of the site-to-site VPN attachment.
        :param proposed_segment_change: The attachment to move from one segment to another.
        :param tags: Tags for the attachment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-sitetositevpnattachment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            cfn_site_to_site_vpn_attachment_props = networkmanager.CfnSiteToSiteVpnAttachmentProps(
                core_network_id="coreNetworkId",
                vpn_connection_arn="vpnConnectionArn",
            
                # the properties below are optional
                proposed_segment_change=networkmanager.CfnSiteToSiteVpnAttachment.ProposedSegmentChangeProperty(
                    attachment_policy_rule_number=123,
                    segment_name="segmentName",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__113def3967f836e31386ebfbfb261bf671b49bfa26918b1a903a386050490f06)
            check_type(argname="argument core_network_id", value=core_network_id, expected_type=type_hints["core_network_id"])
            check_type(argname="argument vpn_connection_arn", value=vpn_connection_arn, expected_type=type_hints["vpn_connection_arn"])
            check_type(argname="argument proposed_segment_change", value=proposed_segment_change, expected_type=type_hints["proposed_segment_change"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "core_network_id": core_network_id,
            "vpn_connection_arn": vpn_connection_arn,
        }
        if proposed_segment_change is not None:
            self._values["proposed_segment_change"] = proposed_segment_change
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def core_network_id(self) -> builtins.str:
        '''The ID of a core network where you're creating a site-to-site VPN attachment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-sitetositevpnattachment.html#cfn-networkmanager-sitetositevpnattachment-corenetworkid
        '''
        result = self._values.get("core_network_id")
        assert result is not None, "Required property 'core_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpn_connection_arn(self) -> builtins.str:
        '''The ARN of the site-to-site VPN attachment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-sitetositevpnattachment.html#cfn-networkmanager-sitetositevpnattachment-vpnconnectionarn
        '''
        result = self._values.get("vpn_connection_arn")
        assert result is not None, "Required property 'vpn_connection_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def proposed_segment_change(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSiteToSiteVpnAttachment.ProposedSegmentChangeProperty]]:
        '''The attachment to move from one segment to another.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-sitetositevpnattachment.html#cfn-networkmanager-sitetositevpnattachment-proposedsegmentchange
        '''
        result = self._values.get("proposed_segment_change")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSiteToSiteVpnAttachment.ProposedSegmentChangeProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags for the attachment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-sitetositevpnattachment.html#cfn-networkmanager-sitetositevpnattachment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSiteToSiteVpnAttachmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnTransitGatewayPeering(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnTransitGatewayPeering",
):
    '''Creates a transit gateway peering connection.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewaypeering.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        cfn_transit_gateway_peering = networkmanager.CfnTransitGatewayPeering(self, "MyCfnTransitGatewayPeering",
            core_network_id="coreNetworkId",
            transit_gateway_arn="transitGatewayArn",
        
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
        core_network_id: builtins.str,
        transit_gateway_arn: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param core_network_id: The ID of the core network.
        :param transit_gateway_arn: The ARN of the transit gateway.
        :param tags: The list of key-value tags associated with the peering.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4fde2115bf574df497915820af61760b6c93b7557e556e0c61e96cab2148cca)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTransitGatewayPeeringProps(
            core_network_id=core_network_id,
            transit_gateway_arn=transit_gateway_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba04e436e3f0fbb5dc75d1bddfe8ea60eec91eccd85c9024ef441f25478231f6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2a5454eff64fdb72ed40b9d0015efa7e0dadbfef17a53e7c427f3c0ddfa8cefc)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCoreNetworkArn")
    def attr_core_network_arn(self) -> builtins.str:
        '''The ARN of the core network.

        :cloudformationAttribute: CoreNetworkArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCoreNetworkArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the core network peering was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrEdgeLocation")
    def attr_edge_location(self) -> builtins.str:
        '''The edge location for the peer.

        :cloudformationAttribute: EdgeLocation
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEdgeLocation"))

    @builtins.property
    @jsii.member(jsii_name="attrOwnerAccountId")
    def attr_owner_account_id(self) -> builtins.str:
        '''The ID of the account owner.

        :cloudformationAttribute: OwnerAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerAccountId"))

    @builtins.property
    @jsii.member(jsii_name="attrPeeringId")
    def attr_peering_id(self) -> builtins.str:
        '''The ID of the peering.

        :cloudformationAttribute: PeeringId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPeeringId"))

    @builtins.property
    @jsii.member(jsii_name="attrPeeringType")
    def attr_peering_type(self) -> builtins.str:
        '''The peering type.

        This will be ``TRANSIT_GATEWAY`` .

        :cloudformationAttribute: PeeringType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPeeringType"))

    @builtins.property
    @jsii.member(jsii_name="attrResourceArn")
    def attr_resource_arn(self) -> builtins.str:
        '''The ARN of the resource peered to a core network.

        :cloudformationAttribute: ResourceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The current state of the peer.

        This can be ``CREATING`` | ``FAILED`` | ``AVAILABLE`` | ``DELETING`` .

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property
    @jsii.member(jsii_name="attrTransitGatewayPeeringAttachmentId")
    def attr_transit_gateway_peering_attachment_id(self) -> builtins.str:
        '''The ID of the peering attachment.

        :cloudformationAttribute: TransitGatewayPeeringAttachmentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTransitGatewayPeeringAttachmentId"))

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
    @jsii.member(jsii_name="coreNetworkId")
    def core_network_id(self) -> builtins.str:
        '''The ID of the core network.'''
        return typing.cast(builtins.str, jsii.get(self, "coreNetworkId"))

    @core_network_id.setter
    def core_network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__439082e4f08493cbbc6d80e894b6f4dfd77144360df686a8c6f3a8211c56db01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coreNetworkId", value)

    @builtins.property
    @jsii.member(jsii_name="transitGatewayArn")
    def transit_gateway_arn(self) -> builtins.str:
        '''The ARN of the transit gateway.'''
        return typing.cast(builtins.str, jsii.get(self, "transitGatewayArn"))

    @transit_gateway_arn.setter
    def transit_gateway_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f61bd1b63b20558994e70ffe5513360796b00386f6642583ee771667f950f000)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transitGatewayArn", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of key-value tags associated with the peering.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__832f5e84db21f837c9c3c23bc334ca3604552518624f6a01c6743e9ad31fa391)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnTransitGatewayPeeringProps",
    jsii_struct_bases=[],
    name_mapping={
        "core_network_id": "coreNetworkId",
        "transit_gateway_arn": "transitGatewayArn",
        "tags": "tags",
    },
)
class CfnTransitGatewayPeeringProps:
    def __init__(
        self,
        *,
        core_network_id: builtins.str,
        transit_gateway_arn: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTransitGatewayPeering``.

        :param core_network_id: The ID of the core network.
        :param transit_gateway_arn: The ARN of the transit gateway.
        :param tags: The list of key-value tags associated with the peering.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewaypeering.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            cfn_transit_gateway_peering_props = networkmanager.CfnTransitGatewayPeeringProps(
                core_network_id="coreNetworkId",
                transit_gateway_arn="transitGatewayArn",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f875d5ddd6d4a16daeb616b41e1fe7b1f7aaab846db198d5fe405165ecae0b21)
            check_type(argname="argument core_network_id", value=core_network_id, expected_type=type_hints["core_network_id"])
            check_type(argname="argument transit_gateway_arn", value=transit_gateway_arn, expected_type=type_hints["transit_gateway_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "core_network_id": core_network_id,
            "transit_gateway_arn": transit_gateway_arn,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def core_network_id(self) -> builtins.str:
        '''The ID of the core network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewaypeering.html#cfn-networkmanager-transitgatewaypeering-corenetworkid
        '''
        result = self._values.get("core_network_id")
        assert result is not None, "Required property 'core_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def transit_gateway_arn(self) -> builtins.str:
        '''The ARN of the transit gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewaypeering.html#cfn-networkmanager-transitgatewaypeering-transitgatewayarn
        '''
        result = self._values.get("transit_gateway_arn")
        assert result is not None, "Required property 'transit_gateway_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of key-value tags associated with the peering.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewaypeering.html#cfn-networkmanager-transitgatewaypeering-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTransitGatewayPeeringProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnTransitGatewayRegistration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnTransitGatewayRegistration",
):
    '''Registers a transit gateway in your global network.

    Not all Regions support transit gateways for global networks. For a list of the supported Regions, see `Region Availability <https://docs.aws.amazon.com/network-manager/latest/tgwnm/what-are-global-networks.html#nm-available-regions>`_ in the *AWS Transit Gateways for Global Networks User Guide* . The transit gateway can be in any of the supported AWS Regions, but it must be owned by the same AWS account that owns the global network. You cannot register a transit gateway in more than one global network.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        cfn_transit_gateway_registration = networkmanager.CfnTransitGatewayRegistration(self, "MyCfnTransitGatewayRegistration",
            global_network_id="globalNetworkId",
            transit_gateway_arn="transitGatewayArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        global_network_id: builtins.str,
        transit_gateway_arn: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param global_network_id: The ID of the global network.
        :param transit_gateway_arn: The Amazon Resource Name (ARN) of the transit gateway.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d58980f8dc1987d036b6c6bdc2763c637f0d4882af63c260e581bf1489765c0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTransitGatewayRegistrationProps(
            global_network_id=global_network_id,
            transit_gateway_arn=transit_gateway_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b56abe01b4a10699a6a1c9ddbb6f2e6278f67eaa846769c67428a51d1a919d3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c4d12a2b835477bb65ab3df0f003b8ed235c9cb74d2882ad2c3ffe69eb90b5e4)
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
    @jsii.member(jsii_name="globalNetworkId")
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network.'''
        return typing.cast(builtins.str, jsii.get(self, "globalNetworkId"))

    @global_network_id.setter
    def global_network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3479609666aeb26b1973c2e635f65d0a6808b4152046244ab06699694f8afbee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "globalNetworkId", value)

    @builtins.property
    @jsii.member(jsii_name="transitGatewayArn")
    def transit_gateway_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the transit gateway.'''
        return typing.cast(builtins.str, jsii.get(self, "transitGatewayArn"))

    @transit_gateway_arn.setter
    def transit_gateway_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7660bc4e9fada811170861b820a6606047adea2f279a8d4735670e4fa3b4aec0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transitGatewayArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnTransitGatewayRegistrationProps",
    jsii_struct_bases=[],
    name_mapping={
        "global_network_id": "globalNetworkId",
        "transit_gateway_arn": "transitGatewayArn",
    },
)
class CfnTransitGatewayRegistrationProps:
    def __init__(
        self,
        *,
        global_network_id: builtins.str,
        transit_gateway_arn: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnTransitGatewayRegistration``.

        :param global_network_id: The ID of the global network.
        :param transit_gateway_arn: The Amazon Resource Name (ARN) of the transit gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            cfn_transit_gateway_registration_props = networkmanager.CfnTransitGatewayRegistrationProps(
                global_network_id="globalNetworkId",
                transit_gateway_arn="transitGatewayArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__168dccdac681a836e54cbf046c9c06f14467cc24f0848929cbd9cb756b713041)
            check_type(argname="argument global_network_id", value=global_network_id, expected_type=type_hints["global_network_id"])
            check_type(argname="argument transit_gateway_arn", value=transit_gateway_arn, expected_type=type_hints["transit_gateway_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "global_network_id": global_network_id,
            "transit_gateway_arn": transit_gateway_arn,
        }

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''The ID of the global network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html#cfn-networkmanager-transitgatewayregistration-globalnetworkid
        '''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def transit_gateway_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the transit gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html#cfn-networkmanager-transitgatewayregistration-transitgatewayarn
        '''
        result = self._values.get("transit_gateway_arn")
        assert result is not None, "Required property 'transit_gateway_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTransitGatewayRegistrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnTransitGatewayRouteTableAttachment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnTransitGatewayRouteTableAttachment",
):
    '''Creates a transit gateway route table attachment.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayroutetableattachment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        cfn_transit_gateway_route_table_attachment = networkmanager.CfnTransitGatewayRouteTableAttachment(self, "MyCfnTransitGatewayRouteTableAttachment",
            peering_id="peeringId",
            transit_gateway_route_table_arn="transitGatewayRouteTableArn",
        
            # the properties below are optional
            proposed_segment_change=networkmanager.CfnTransitGatewayRouteTableAttachment.ProposedSegmentChangeProperty(
                attachment_policy_rule_number=123,
                segment_name="segmentName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
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
        peering_id: builtins.str,
        transit_gateway_route_table_arn: builtins.str,
        proposed_segment_change: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTransitGatewayRouteTableAttachment.ProposedSegmentChangeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param peering_id: The ID of the transit gateway peering.
        :param transit_gateway_route_table_arn: The ARN of the transit gateway attachment route table. For example, ``"TransitGatewayRouteTableArn": "arn:aws:ec2:us-west-2:123456789012:transit-gateway-route-table/tgw-rtb-9876543210123456"`` .
        :param proposed_segment_change: This property is read-only. Values can't be assigned to it.
        :param tags: The list of key-value pairs associated with the transit gateway route table attachment.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76fd48cd4f7728733266eb51b353c86fecd583f774019081446c28ca5e2c04d8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTransitGatewayRouteTableAttachmentProps(
            peering_id=peering_id,
            transit_gateway_route_table_arn=transit_gateway_route_table_arn,
            proposed_segment_change=proposed_segment_change,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0eacc5d0b9706dded3d1c3179af64961084f56b76cdf528e23831708a5829099)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5b83f1113ed5dd75a49a660552a54731d108a3e06a6ebd26415d5db93b873737)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAttachmentId")
    def attr_attachment_id(self) -> builtins.str:
        '''The ID of the transit gateway route table attachment.

        :cloudformationAttribute: AttachmentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAttachmentId"))

    @builtins.property
    @jsii.member(jsii_name="attrAttachmentPolicyRuleNumber")
    def attr_attachment_policy_rule_number(self) -> jsii.Number:
        '''The policy rule number associated with the attachment.

        :cloudformationAttribute: AttachmentPolicyRuleNumber
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrAttachmentPolicyRuleNumber"))

    @builtins.property
    @jsii.member(jsii_name="attrAttachmentType")
    def attr_attachment_type(self) -> builtins.str:
        '''The type of attachment.

        This will be ``TRANSIT_GATEWAY_ROUTE_TABLE`` .

        :cloudformationAttribute: AttachmentType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAttachmentType"))

    @builtins.property
    @jsii.member(jsii_name="attrCoreNetworkArn")
    def attr_core_network_arn(self) -> builtins.str:
        '''The ARN of the core network.

        :cloudformationAttribute: CoreNetworkArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCoreNetworkArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCoreNetworkId")
    def attr_core_network_id(self) -> builtins.str:
        '''The ID of the core network.

        :cloudformationAttribute: CoreNetworkId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCoreNetworkId"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the transit gateway route table attachment was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrEdgeLocation")
    def attr_edge_location(self) -> builtins.str:
        '''The Region where the core network edge is located.

        :cloudformationAttribute: EdgeLocation
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEdgeLocation"))

    @builtins.property
    @jsii.member(jsii_name="attrOwnerAccountId")
    def attr_owner_account_id(self) -> builtins.str:
        '''The ID of the transit gateway route table attachment owner.

        :cloudformationAttribute: OwnerAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerAccountId"))

    @builtins.property
    @jsii.member(jsii_name="attrResourceArn")
    def attr_resource_arn(self) -> builtins.str:
        '''The resource ARN for the transit gateway route table attachment.

        :cloudformationAttribute: ResourceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSegmentName")
    def attr_segment_name(self) -> builtins.str:
        '''The name of the attachment's segment.

        :cloudformationAttribute: SegmentName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSegmentName"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The state of the attachment.

        This can be: ``REJECTED`` | ``PENDING_ATTACHMENT_ACCEPTANCE`` | ``CREATING`` | ``FAILED`` | ``AVAILABLE`` | ``UPDATING`` | ``PENDING_NETWORK_UPDATE`` | ``PENDING_TAG_ACCEPTANCE`` | ``DELETING`` .

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp when the transit gateway route table attachment was last updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

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
    @jsii.member(jsii_name="peeringId")
    def peering_id(self) -> builtins.str:
        '''The ID of the transit gateway peering.'''
        return typing.cast(builtins.str, jsii.get(self, "peeringId"))

    @peering_id.setter
    def peering_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc057602684fcd6d30d72064e2609de0278fcd49507560ee02b7a0f7eea74a4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peeringId", value)

    @builtins.property
    @jsii.member(jsii_name="transitGatewayRouteTableArn")
    def transit_gateway_route_table_arn(self) -> builtins.str:
        '''The ARN of the transit gateway attachment route table.'''
        return typing.cast(builtins.str, jsii.get(self, "transitGatewayRouteTableArn"))

    @transit_gateway_route_table_arn.setter
    def transit_gateway_route_table_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e96460515a73cddc08c4eeb7c5c0d62b3470f6ba77019112fad9b6b67d9b4313)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transitGatewayRouteTableArn", value)

    @builtins.property
    @jsii.member(jsii_name="proposedSegmentChange")
    def proposed_segment_change(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransitGatewayRouteTableAttachment.ProposedSegmentChangeProperty"]]:
        '''This property is read-only.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransitGatewayRouteTableAttachment.ProposedSegmentChangeProperty"]], jsii.get(self, "proposedSegmentChange"))

    @proposed_segment_change.setter
    def proposed_segment_change(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTransitGatewayRouteTableAttachment.ProposedSegmentChangeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__833b64ddb00aa1bf9b86b7f76ee36148417740e18097f46e7c35c82b700f36f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proposedSegmentChange", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of key-value pairs associated with the transit gateway route table attachment.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3b7316bcb7e40529995cb7c98b7c558e8ac3b24b7e6b5bcf786ac3da836b14a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkmanager.CfnTransitGatewayRouteTableAttachment.ProposedSegmentChangeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attachment_policy_rule_number": "attachmentPolicyRuleNumber",
            "segment_name": "segmentName",
            "tags": "tags",
        },
    )
    class ProposedSegmentChangeProperty:
        def __init__(
            self,
            *,
            attachment_policy_rule_number: typing.Optional[jsii.Number] = None,
            segment_name: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes a proposed segment change.

            In some cases, the segment change must first be evaluated and accepted.

            :param attachment_policy_rule_number: The rule number in the policy document that applies to this change.
            :param segment_name: The name of the segment to change.
            :param tags: The list of key-value tags that changed for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-transitgatewayroutetableattachment-proposedsegmentchange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkmanager as networkmanager
                
                proposed_segment_change_property = networkmanager.CfnTransitGatewayRouteTableAttachment.ProposedSegmentChangeProperty(
                    attachment_policy_rule_number=123,
                    segment_name="segmentName",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__add1834976b0aa622dc8de71fbd481ec1596649e9c54a7426f53fab96a8fc95a)
                check_type(argname="argument attachment_policy_rule_number", value=attachment_policy_rule_number, expected_type=type_hints["attachment_policy_rule_number"])
                check_type(argname="argument segment_name", value=segment_name, expected_type=type_hints["segment_name"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if attachment_policy_rule_number is not None:
                self._values["attachment_policy_rule_number"] = attachment_policy_rule_number
            if segment_name is not None:
                self._values["segment_name"] = segment_name
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def attachment_policy_rule_number(self) -> typing.Optional[jsii.Number]:
            '''The rule number in the policy document that applies to this change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-transitgatewayroutetableattachment-proposedsegmentchange.html#cfn-networkmanager-transitgatewayroutetableattachment-proposedsegmentchange-attachmentpolicyrulenumber
            '''
            result = self._values.get("attachment_policy_rule_number")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def segment_name(self) -> typing.Optional[builtins.str]:
            '''The name of the segment to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-transitgatewayroutetableattachment-proposedsegmentchange.html#cfn-networkmanager-transitgatewayroutetableattachment-proposedsegmentchange-segmentname
            '''
            result = self._values.get("segment_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
            '''The list of key-value tags that changed for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-transitgatewayroutetableattachment-proposedsegmentchange.html#cfn-networkmanager-transitgatewayroutetableattachment-proposedsegmentchange-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProposedSegmentChangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnTransitGatewayRouteTableAttachmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "peering_id": "peeringId",
        "transit_gateway_route_table_arn": "transitGatewayRouteTableArn",
        "proposed_segment_change": "proposedSegmentChange",
        "tags": "tags",
    },
)
class CfnTransitGatewayRouteTableAttachmentProps:
    def __init__(
        self,
        *,
        peering_id: builtins.str,
        transit_gateway_route_table_arn: builtins.str,
        proposed_segment_change: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransitGatewayRouteTableAttachment.ProposedSegmentChangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTransitGatewayRouteTableAttachment``.

        :param peering_id: The ID of the transit gateway peering.
        :param transit_gateway_route_table_arn: The ARN of the transit gateway attachment route table. For example, ``"TransitGatewayRouteTableArn": "arn:aws:ec2:us-west-2:123456789012:transit-gateway-route-table/tgw-rtb-9876543210123456"`` .
        :param proposed_segment_change: This property is read-only. Values can't be assigned to it.
        :param tags: The list of key-value pairs associated with the transit gateway route table attachment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayroutetableattachment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            cfn_transit_gateway_route_table_attachment_props = networkmanager.CfnTransitGatewayRouteTableAttachmentProps(
                peering_id="peeringId",
                transit_gateway_route_table_arn="transitGatewayRouteTableArn",
            
                # the properties below are optional
                proposed_segment_change=networkmanager.CfnTransitGatewayRouteTableAttachment.ProposedSegmentChangeProperty(
                    attachment_policy_rule_number=123,
                    segment_name="segmentName",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32c28142db297494ed9a38267ab8bd9715938d6419db97dd30cc2434fec11a0a)
            check_type(argname="argument peering_id", value=peering_id, expected_type=type_hints["peering_id"])
            check_type(argname="argument transit_gateway_route_table_arn", value=transit_gateway_route_table_arn, expected_type=type_hints["transit_gateway_route_table_arn"])
            check_type(argname="argument proposed_segment_change", value=proposed_segment_change, expected_type=type_hints["proposed_segment_change"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "peering_id": peering_id,
            "transit_gateway_route_table_arn": transit_gateway_route_table_arn,
        }
        if proposed_segment_change is not None:
            self._values["proposed_segment_change"] = proposed_segment_change
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def peering_id(self) -> builtins.str:
        '''The ID of the transit gateway peering.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayroutetableattachment.html#cfn-networkmanager-transitgatewayroutetableattachment-peeringid
        '''
        result = self._values.get("peering_id")
        assert result is not None, "Required property 'peering_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def transit_gateway_route_table_arn(self) -> builtins.str:
        '''The ARN of the transit gateway attachment route table.

        For example, ``"TransitGatewayRouteTableArn": "arn:aws:ec2:us-west-2:123456789012:transit-gateway-route-table/tgw-rtb-9876543210123456"`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayroutetableattachment.html#cfn-networkmanager-transitgatewayroutetableattachment-transitgatewayroutetablearn
        '''
        result = self._values.get("transit_gateway_route_table_arn")
        assert result is not None, "Required property 'transit_gateway_route_table_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def proposed_segment_change(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTransitGatewayRouteTableAttachment.ProposedSegmentChangeProperty]]:
        '''This property is read-only.

        Values can't be assigned to it.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayroutetableattachment.html#cfn-networkmanager-transitgatewayroutetableattachment-proposedsegmentchange
        '''
        result = self._values.get("proposed_segment_change")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTransitGatewayRouteTableAttachment.ProposedSegmentChangeProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The list of key-value pairs associated with the transit gateway route table attachment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayroutetableattachment.html#cfn-networkmanager-transitgatewayroutetableattachment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTransitGatewayRouteTableAttachmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnVpcAttachment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnVpcAttachment",
):
    '''Creates a VPC attachment on an edge location of a core network.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_networkmanager as networkmanager
        
        cfn_vpc_attachment = networkmanager.CfnVpcAttachment(self, "MyCfnVpcAttachment",
            core_network_id="coreNetworkId",
            subnet_arns=["subnetArns"],
            vpc_arn="vpcArn",
        
            # the properties below are optional
            options=networkmanager.CfnVpcAttachment.VpcOptionsProperty(
                appliance_mode_support=False,
                ipv6_support=False
            ),
            proposed_segment_change=networkmanager.CfnVpcAttachment.ProposedSegmentChangeProperty(
                attachment_policy_rule_number=123,
                segment_name="segmentName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
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
        core_network_id: builtins.str,
        subnet_arns: typing.Sequence[builtins.str],
        vpc_arn: builtins.str,
        options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnVpcAttachment.VpcOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        proposed_segment_change: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnVpcAttachment.ProposedSegmentChangeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param core_network_id: The core network ID.
        :param subnet_arns: The subnet ARNs.
        :param vpc_arn: The ARN of the VPC attachment.
        :param options: Options for creating the VPC attachment.
        :param proposed_segment_change: The attachment to move from one segment to another.
        :param tags: The tags associated with the VPC attachment.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__962ef8273d6d2d97a33b00603b7bf87793fdecfaae4031352d9cbc1bc6746602)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVpcAttachmentProps(
            core_network_id=core_network_id,
            subnet_arns=subnet_arns,
            vpc_arn=vpc_arn,
            options=options,
            proposed_segment_change=proposed_segment_change,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__066721874248356323b7edc6b2c638d14ec9d95fc08966f64139e05c40164db7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b6a55bcf004239ce3b8b35d751875ec35c945b0b0645aa75a4d598eb6ea406b1)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAttachmentId")
    def attr_attachment_id(self) -> builtins.str:
        '''The ID of the VPC attachment.

        :cloudformationAttribute: AttachmentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAttachmentId"))

    @builtins.property
    @jsii.member(jsii_name="attrAttachmentPolicyRuleNumber")
    def attr_attachment_policy_rule_number(self) -> jsii.Number:
        '''The policy rule number associated with the attachment.

        :cloudformationAttribute: AttachmentPolicyRuleNumber
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrAttachmentPolicyRuleNumber"))

    @builtins.property
    @jsii.member(jsii_name="attrAttachmentType")
    def attr_attachment_type(self) -> builtins.str:
        '''The type of attachment.

        This will be ``VPC`` .

        :cloudformationAttribute: AttachmentType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAttachmentType"))

    @builtins.property
    @jsii.member(jsii_name="attrCoreNetworkArn")
    def attr_core_network_arn(self) -> builtins.str:
        '''The ARN of the core network.

        :cloudformationAttribute: CoreNetworkArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCoreNetworkArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the VPC attachment was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrEdgeLocation")
    def attr_edge_location(self) -> builtins.str:
        '''The Region where the core network edge is located.

        :cloudformationAttribute: EdgeLocation
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEdgeLocation"))

    @builtins.property
    @jsii.member(jsii_name="attrOwnerAccountId")
    def attr_owner_account_id(self) -> builtins.str:
        '''The ID of the VPC attachment owner.

        :cloudformationAttribute: OwnerAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerAccountId"))

    @builtins.property
    @jsii.member(jsii_name="attrResourceArn")
    def attr_resource_arn(self) -> builtins.str:
        '''The resource ARN for the VPC attachment.

        :cloudformationAttribute: ResourceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResourceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSegmentName")
    def attr_segment_name(self) -> builtins.str:
        '''The name of the attachment's segment.

        :cloudformationAttribute: SegmentName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSegmentName"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The state of the attachment.

        This can be: ``REJECTED`` | ``PENDING_ATTACHMENT_ACCEPTANCE`` | ``CREATING`` | ``FAILED`` | ``AVAILABLE`` | ``UPDATING`` | ``PENDING_NETWORK_UPDATE`` | ``PENDING_TAG_ACCEPTANCE`` | ``DELETING`` .

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp when the VPC attachment was last updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

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
    @jsii.member(jsii_name="coreNetworkId")
    def core_network_id(self) -> builtins.str:
        '''The core network ID.'''
        return typing.cast(builtins.str, jsii.get(self, "coreNetworkId"))

    @core_network_id.setter
    def core_network_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dc45980bc0f76e5b64f54c910888f2fbc61f8035b57f4cc2da0873460ceb6d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "coreNetworkId", value)

    @builtins.property
    @jsii.member(jsii_name="subnetArns")
    def subnet_arns(self) -> typing.List[builtins.str]:
        '''The subnet ARNs.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetArns"))

    @subnet_arns.setter
    def subnet_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44eff42e1086acb3f04b3edb054dd6dc4f08bc4fde2b55e1211110fd05e54030)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetArns", value)

    @builtins.property
    @jsii.member(jsii_name="vpcArn")
    def vpc_arn(self) -> builtins.str:
        '''The ARN of the VPC attachment.'''
        return typing.cast(builtins.str, jsii.get(self, "vpcArn"))

    @vpc_arn.setter
    def vpc_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__292ee8d1f17d2877219f1e655a187015b2e1a10520732d288dbc03f196471402)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcArn", value)

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnVpcAttachment.VpcOptionsProperty"]]:
        '''Options for creating the VPC attachment.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnVpcAttachment.VpcOptionsProperty"]], jsii.get(self, "options"))

    @options.setter
    def options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnVpcAttachment.VpcOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4df78b42bf8dafd3f4ef447404aa6d3bb210d4de6d8c8238c7b7509fee4e6dc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "options", value)

    @builtins.property
    @jsii.member(jsii_name="proposedSegmentChange")
    def proposed_segment_change(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnVpcAttachment.ProposedSegmentChangeProperty"]]:
        '''The attachment to move from one segment to another.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnVpcAttachment.ProposedSegmentChangeProperty"]], jsii.get(self, "proposedSegmentChange"))

    @proposed_segment_change.setter
    def proposed_segment_change(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnVpcAttachment.ProposedSegmentChangeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e08a82721c316f3d57592bb6309e39f40fb575ea68e4532f8a4bb8f162f0e1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proposedSegmentChange", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags associated with the VPC attachment.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10a9a6020f018ebc6f503414f839aac623a810484c578e3cc55c00a2aabd965f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkmanager.CfnVpcAttachment.ProposedSegmentChangeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attachment_policy_rule_number": "attachmentPolicyRuleNumber",
            "segment_name": "segmentName",
            "tags": "tags",
        },
    )
    class ProposedSegmentChangeProperty:
        def __init__(
            self,
            *,
            attachment_policy_rule_number: typing.Optional[jsii.Number] = None,
            segment_name: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes a proposed segment change.

            In some cases, the segment change must first be evaluated and accepted.

            :param attachment_policy_rule_number: The rule number in the policy document that applies to this change.
            :param segment_name: The name of the segment to change.
            :param tags: The list of key-value tags that changed for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-vpcattachment-proposedsegmentchange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkmanager as networkmanager
                
                proposed_segment_change_property = networkmanager.CfnVpcAttachment.ProposedSegmentChangeProperty(
                    attachment_policy_rule_number=123,
                    segment_name="segmentName",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__557bf3a5ccb396638b970920d51e56a5af3a62c8b836006da453e705f15020ff)
                check_type(argname="argument attachment_policy_rule_number", value=attachment_policy_rule_number, expected_type=type_hints["attachment_policy_rule_number"])
                check_type(argname="argument segment_name", value=segment_name, expected_type=type_hints["segment_name"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if attachment_policy_rule_number is not None:
                self._values["attachment_policy_rule_number"] = attachment_policy_rule_number
            if segment_name is not None:
                self._values["segment_name"] = segment_name
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def attachment_policy_rule_number(self) -> typing.Optional[jsii.Number]:
            '''The rule number in the policy document that applies to this change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-vpcattachment-proposedsegmentchange.html#cfn-networkmanager-vpcattachment-proposedsegmentchange-attachmentpolicyrulenumber
            '''
            result = self._values.get("attachment_policy_rule_number")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def segment_name(self) -> typing.Optional[builtins.str]:
            '''The name of the segment to change.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-vpcattachment-proposedsegmentchange.html#cfn-networkmanager-vpcattachment-proposedsegmentchange-segmentname
            '''
            result = self._values.get("segment_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
            '''The list of key-value tags that changed for the segment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-vpcattachment-proposedsegmentchange.html#cfn-networkmanager-vpcattachment-proposedsegmentchange-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProposedSegmentChangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_networkmanager.CfnVpcAttachment.VpcOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "appliance_mode_support": "applianceModeSupport",
            "ipv6_support": "ipv6Support",
        },
    )
    class VpcOptionsProperty:
        def __init__(
            self,
            *,
            appliance_mode_support: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            ipv6_support: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Describes the VPC options.

            :param appliance_mode_support: Indicates whether appliance mode is supported. If enabled, traffic flow between a source and destination use the same Availability Zone for the VPC attachment for the lifetime of that flow. The default value is ``false`` . Default: - false
            :param ipv6_support: Indicates whether IPv6 is supported. Default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-vpcattachment-vpcoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_networkmanager as networkmanager
                
                vpc_options_property = networkmanager.CfnVpcAttachment.VpcOptionsProperty(
                    appliance_mode_support=False,
                    ipv6_support=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e0178ed6021c1858c87186be29fec1d6351e020d4e0f48dd2207432dbeaf7b50)
                check_type(argname="argument appliance_mode_support", value=appliance_mode_support, expected_type=type_hints["appliance_mode_support"])
                check_type(argname="argument ipv6_support", value=ipv6_support, expected_type=type_hints["ipv6_support"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if appliance_mode_support is not None:
                self._values["appliance_mode_support"] = appliance_mode_support
            if ipv6_support is not None:
                self._values["ipv6_support"] = ipv6_support

        @builtins.property
        def appliance_mode_support(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether appliance mode is supported.

            If enabled, traffic flow between a source and destination use the same Availability Zone for the VPC attachment for the lifetime of that flow. The default value is ``false`` .

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-vpcattachment-vpcoptions.html#cfn-networkmanager-vpcattachment-vpcoptions-appliancemodesupport
            '''
            result = self._values.get("appliance_mode_support")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def ipv6_support(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether IPv6 is supported.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkmanager-vpcattachment-vpcoptions.html#cfn-networkmanager-vpcattachment-vpcoptions-ipv6support
            '''
            result = self._values.get("ipv6_support")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_networkmanager.CfnVpcAttachmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "core_network_id": "coreNetworkId",
        "subnet_arns": "subnetArns",
        "vpc_arn": "vpcArn",
        "options": "options",
        "proposed_segment_change": "proposedSegmentChange",
        "tags": "tags",
    },
)
class CfnVpcAttachmentProps:
    def __init__(
        self,
        *,
        core_network_id: builtins.str,
        subnet_arns: typing.Sequence[builtins.str],
        vpc_arn: builtins.str,
        options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnVpcAttachment.VpcOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        proposed_segment_change: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnVpcAttachment.ProposedSegmentChangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnVpcAttachment``.

        :param core_network_id: The core network ID.
        :param subnet_arns: The subnet ARNs.
        :param vpc_arn: The ARN of the VPC attachment.
        :param options: Options for creating the VPC attachment.
        :param proposed_segment_change: The attachment to move from one segment to another.
        :param tags: The tags associated with the VPC attachment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_networkmanager as networkmanager
            
            cfn_vpc_attachment_props = networkmanager.CfnVpcAttachmentProps(
                core_network_id="coreNetworkId",
                subnet_arns=["subnetArns"],
                vpc_arn="vpcArn",
            
                # the properties below are optional
                options=networkmanager.CfnVpcAttachment.VpcOptionsProperty(
                    appliance_mode_support=False,
                    ipv6_support=False
                ),
                proposed_segment_change=networkmanager.CfnVpcAttachment.ProposedSegmentChangeProperty(
                    attachment_policy_rule_number=123,
                    segment_name="segmentName",
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12d5c20c6145e2cfb5336d480d3ded8850bc2ee5b31fe21ab1b44a90d4ad3e95)
            check_type(argname="argument core_network_id", value=core_network_id, expected_type=type_hints["core_network_id"])
            check_type(argname="argument subnet_arns", value=subnet_arns, expected_type=type_hints["subnet_arns"])
            check_type(argname="argument vpc_arn", value=vpc_arn, expected_type=type_hints["vpc_arn"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument proposed_segment_change", value=proposed_segment_change, expected_type=type_hints["proposed_segment_change"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "core_network_id": core_network_id,
            "subnet_arns": subnet_arns,
            "vpc_arn": vpc_arn,
        }
        if options is not None:
            self._values["options"] = options
        if proposed_segment_change is not None:
            self._values["proposed_segment_change"] = proposed_segment_change
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def core_network_id(self) -> builtins.str:
        '''The core network ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html#cfn-networkmanager-vpcattachment-corenetworkid
        '''
        result = self._values.get("core_network_id")
        assert result is not None, "Required property 'core_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_arns(self) -> typing.List[builtins.str]:
        '''The subnet ARNs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html#cfn-networkmanager-vpcattachment-subnetarns
        '''
        result = self._values.get("subnet_arns")
        assert result is not None, "Required property 'subnet_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def vpc_arn(self) -> builtins.str:
        '''The ARN of the VPC attachment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html#cfn-networkmanager-vpcattachment-vpcarn
        '''
        result = self._values.get("vpc_arn")
        assert result is not None, "Required property 'vpc_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnVpcAttachment.VpcOptionsProperty]]:
        '''Options for creating the VPC attachment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html#cfn-networkmanager-vpcattachment-options
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnVpcAttachment.VpcOptionsProperty]], result)

    @builtins.property
    def proposed_segment_change(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnVpcAttachment.ProposedSegmentChangeProperty]]:
        '''The attachment to move from one segment to another.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html#cfn-networkmanager-vpcattachment-proposedsegmentchange
        '''
        result = self._values.get("proposed_segment_change")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnVpcAttachment.ProposedSegmentChangeProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags associated with the VPC attachment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-vpcattachment.html#cfn-networkmanager-vpcattachment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcAttachmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnConnectAttachment",
    "CfnConnectAttachmentProps",
    "CfnConnectPeer",
    "CfnConnectPeerProps",
    "CfnCoreNetwork",
    "CfnCoreNetworkProps",
    "CfnCustomerGatewayAssociation",
    "CfnCustomerGatewayAssociationProps",
    "CfnDevice",
    "CfnDeviceProps",
    "CfnGlobalNetwork",
    "CfnGlobalNetworkProps",
    "CfnLink",
    "CfnLinkAssociation",
    "CfnLinkAssociationProps",
    "CfnLinkProps",
    "CfnSite",
    "CfnSiteProps",
    "CfnSiteToSiteVpnAttachment",
    "CfnSiteToSiteVpnAttachmentProps",
    "CfnTransitGatewayPeering",
    "CfnTransitGatewayPeeringProps",
    "CfnTransitGatewayRegistration",
    "CfnTransitGatewayRegistrationProps",
    "CfnTransitGatewayRouteTableAttachment",
    "CfnTransitGatewayRouteTableAttachmentProps",
    "CfnVpcAttachment",
    "CfnVpcAttachmentProps",
]

publication.publish()

def _typecheckingstub__d7415843def493b65c590878e3897c27e4c459f5d736fb5ee9738e5a17aad441(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    core_network_id: builtins.str,
    edge_location: builtins.str,
    options: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectAttachment.ConnectAttachmentOptionsProperty, typing.Dict[builtins.str, typing.Any]]],
    transport_attachment_id: builtins.str,
    proposed_segment_change: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectAttachment.ProposedSegmentChangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44665bf65f06575cd3323d1c866a2dc00c17092a359aac8101e622ad9bf92f5c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec45c4dbbf2822b7186c9d48a08a52feeb96db87ca1ed98a3c52fb2284f4f9de(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1019c9f66ae0f0b6c31480b08f0844a5328118d1f4beeb166ff2f71b6068b0a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65f8076caf77f777faab35b0ff1e31902eae6e5c1507ec93cdcdef28bd00b0bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3ec27706fe61280d3c2f24d80b9b25fadffd2d87cfb1922fb82b4b8309feeab(
    value: typing.Union[_IResolvable_da3f097b, CfnConnectAttachment.ConnectAttachmentOptionsProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f45177b471df4bf392fc7f3cd3a02af202d007968b4b8f463eab9717182e743e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84b1c89b7abda3eee8505aae6dbce09c5893b6a4187a20a6c43a4204cea40ffd(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnectAttachment.ProposedSegmentChangeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffc7890372457410bdf1574c98526291062406f7166b95fd35ac58c7cbd3e98c(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc0fa092684fa44dd4fe83501bbb7802a95737bd2a72c5eaea2e09e6d7c8b31f(
    *,
    protocol: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33f3ba0307020211126665ce4fb2d25caae1b2af6cc7e2712bd85408f247a0da(
    *,
    attachment_policy_rule_number: typing.Optional[jsii.Number] = None,
    segment_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b62006d4f48143066c9708819150b6dc03f2315028ddb6bd7d7d8ecbc955531(
    *,
    core_network_id: builtins.str,
    edge_location: builtins.str,
    options: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectAttachment.ConnectAttachmentOptionsProperty, typing.Dict[builtins.str, typing.Any]]],
    transport_attachment_id: builtins.str,
    proposed_segment_change: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectAttachment.ProposedSegmentChangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__614dda353f68a248b8ae08e0094dfb5ecab0817abd8f24330d861cce6ffc7797(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    connect_attachment_id: builtins.str,
    peer_address: builtins.str,
    bgp_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectPeer.BgpOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    core_network_address: typing.Optional[builtins.str] = None,
    inside_cidr_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7c4b91f985873f74931b033eca32fbff8cdd4309b9150310c66ccf9f6a4fc7c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a37b71a0670025bcb8e024070ea19783e142b007e3bbb76e1b2cec30a6a8c9df(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6837b16f8b774f684a7de66e3e0192162c799f4ccc35d48270125b5a9867f69(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c390f124a44254d44c9db6c9600d7d4bedeaa234040db5482b9da71be5ba3267(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09c2cde583ab1ee0b8539941f5f59464104e4b15a665812986be376af521cd7c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnectPeer.BgpOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ccd872c8477548a54a56ce63aa9266f60d6d4a8ce8da83adaf0c37aa370d21d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6579db2e8401c4c460fad5541ac628299f109239ae0b747856b5b464e0fb2394(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be35c1c86a9354575519ff51daf71188a8d6c995c7f05b5070cfc8f935af359f(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__820b80243250388311dea6e86ec715c97ac8bef0b52b69d918604b35a112a01c(
    *,
    peer_asn: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e94639c3bff646ba2bdeccdcea4a34256f4fc82522c3c1437b767fc6295f0b7(
    *,
    core_network_address: typing.Optional[builtins.str] = None,
    core_network_asn: typing.Optional[jsii.Number] = None,
    peer_address: typing.Optional[builtins.str] = None,
    peer_asn: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a9ed6409a3fe862bfaa3b6216c0ea60f1182083169100da39cfa761f53167bc(
    *,
    bgp_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectPeer.ConnectPeerBgpConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    core_network_address: typing.Optional[builtins.str] = None,
    inside_cidr_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
    peer_address: typing.Optional[builtins.str] = None,
    protocol: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c4bd06b5a27f2d168dc63dd01d3d754fafe1dd8ea823eede0c4909db15718f8(
    *,
    connect_attachment_id: builtins.str,
    peer_address: builtins.str,
    bgp_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectPeer.BgpOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    core_network_address: typing.Optional[builtins.str] = None,
    inside_cidr_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef3cb1cd4abb4fa5b383cbcb25ab3b19985891cac9ee903fdc80a4b7855c3861(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    global_network_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    policy_document: typing.Any = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab8dfe0941f0bb31d0cd5ffec09e9e0e64f454ca60a61a7e724ae83857fed362(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64d8a77d9a9f53702b00cebe4bcbe33b1dcc035bc69a26e96bb10401bee44fd4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86408588b749b814a7197fcea933176b0c59fa27af364e497dd8c35db9c2767b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd943ed85c9a7352421e16d77f69b1d40ca95e68eac8600af543194df8d324f7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95fd0d184423074af0fbb9e444ffac5c0adbdbe161eb0520bbbd67705f54b4d2(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96b99af1b4897054c775f7c57c33730e70cc058523a18542f6bac227d93d5e39(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fbb8f1859ef14e326882885a8fee653ca3ab95025fac14894453976df1d1187(
    *,
    asn: typing.Optional[jsii.Number] = None,
    edge_location: typing.Optional[builtins.str] = None,
    inside_cidr_blocks: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__935d45f9acdf79c9cd7e8fd50a27ef19f966892baf4d9d758c80af0c36b222e0(
    *,
    edge_locations: typing.Optional[typing.Sequence[builtins.str]] = None,
    name: typing.Optional[builtins.str] = None,
    shared_segments: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__153eb0a5a16cd071b499d3d1d86d232667e61cbcf2cfa1cc52e04a3afcc48c15(
    *,
    global_network_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    policy_document: typing.Any = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8530cc09738d1161c48c06739c9d69bc634930a0d627d82903f1538ebcf9311(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    customer_gateway_arn: builtins.str,
    device_id: builtins.str,
    global_network_id: builtins.str,
    link_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76fdbb6c450fbfa3056f4acf441be5bffc42673ec2dfe0703ea52c261027d133(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__011cc1dd9dedcd5ceb6fd112e35fb270aa4dbdbcb47c0083f341fcaae13d391c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f23e31195cfb70367760a032bd3771e71ab9a3e41af843be539654bd26f895a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b65adc2efb3c3657aee3b06f73070c15bae503de5f5b47afedb7a41ddb49d96a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b47d831038fea5cc72a69621a49acee67d94496b914cdf714d36f59c8572340(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f1a9d0d94d8a37a3549e10ffcd4469d4dd99b00032e3bfcfe63c53b1b505a80(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eec004eba5efaff43d4770c050984dada45fff22cb42feef066ca3d48d22ad62(
    *,
    customer_gateway_arn: builtins.str,
    device_id: builtins.str,
    global_network_id: builtins.str,
    link_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ad564c84e64f3433b234887d19dd14a76b326ebbe6db1b2c11c4e75c1bb9111(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    global_network_id: builtins.str,
    aws_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDevice.AWSLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDevice.LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    model: typing.Optional[builtins.str] = None,
    serial_number: typing.Optional[builtins.str] = None,
    site_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
    vendor: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__681ebe70583a2bd7db602c1014aaeb6e8470966be63f6b5f27003ab0c22980fa(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c9df1ab9e4ab9cd8105624838a2ce4542052964f13801c0ab69b542ef8a1700(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfe93f5f35db9797ee30d721c0dc9a87d465bbfaee9d289f745d2ec564240fc8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4583117af731ea782790ab60127926847bd464d6c6710eae89844bbfd59bb491(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDevice.AWSLocationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e735fe734530f45aa89056e48a9a7241fe5d210c4f83b0fad47adf9be3677fd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b88d3e1b4865be708f6cc69c3a68a598b6d1f850245deb4c3da99d1a4a2a4a7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDevice.LocationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af59216267fbe291d9a86c89712257d97c0d6866de65577764718a5ab20e656f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__391e1294cca69f190d4b32c42e15faead42d783500f2807a30c3f0ab04e10580(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d356eccb03811c1a8c04efa44c470e4d99c9e5426ac16419449ff2c9e066b2e0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26c263b233a1cae0165c1b45058ac8409a2bfaff22af7d0609a990d166cef3fd(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c61590f79bc7db569a8dd74aab8282cec9db607de9dca86bfdb39ebe67ec719(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dfaeac3f3ef9890082ea071cb4a3ac124e205509c2a2fe6537128d482a516ac(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aef84c7e0700dce028a9d7b943fcbc3917928af3851e826cc4e321829d809a40(
    *,
    subnet_arn: typing.Optional[builtins.str] = None,
    zone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c70126f53370661902dca458745ecdc5b30b4ec88d37a1f028e6fb646c83d696(
    *,
    address: typing.Optional[builtins.str] = None,
    latitude: typing.Optional[builtins.str] = None,
    longitude: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__214d65d41aacb7028ea3820823a63765a7ea304d6d4501f238a41dd41254186e(
    *,
    global_network_id: builtins.str,
    aws_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDevice.AWSLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDevice.LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    model: typing.Optional[builtins.str] = None,
    serial_number: typing.Optional[builtins.str] = None,
    site_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
    vendor: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcd77a1264244ecd5c8ad8fbf6038975eda0a4a49d5da9ba92306e218841f74f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a4d6bdc69ded81dc7371bcc908a8c470d45d7400be9b04c8aab8fda39abcee9(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a1cf0c8bf170de7441b97dd3d9ba7d4a7ca45d0d94c6f2c0053236748c5531d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19a1a1c3b45eed0a10e7c5e3bb7a960be34852e62b1241a92db880448eba0301(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e1af222068741701cde749bdf31ed3994009b5ed482f7ae4e4901c954d350ff(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d4e8224b803ee7837da430965223a7bb5cc1d471fadf277c44910dc5f851005(
    *,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a85b1ccff185ece01ba7173d98d2c10359b58386e88607b0ea915c94a4650cdd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bandwidth: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLink.BandwidthProperty, typing.Dict[builtins.str, typing.Any]]],
    global_network_id: builtins.str,
    site_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    provider: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7013af1fb84ea807547650ea0acaaf21554964c39b4664177013638d646dc4d2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__928a1929b4243ced484546933d81b0b53abb5463d5f704ef92ac52897599ad66(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__988888cdb37dacfb2adb77af73f778a15dd9db7b8586f6a4a0748cc7ae082b96(
    value: typing.Union[_IResolvable_da3f097b, CfnLink.BandwidthProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5259ab5861d067f6495afc71e1f3826c064c92b18d3401e69328a415b375f60b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__820ae0c9b3b49e33e7da67095da21a8f43e171b3d4aae4e715300b82480190f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c24e7374c54735ea9b48c8a23a947605911fd130fd389dcc21e481484b5ca689(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51a319abdcd33f238855c8baffca80d87f52d9a8d1ee39a68ebd9fa1f1b6a1ab(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3d04cb05f180d4cf6476de9fd9cb617bb7f8aafae4932b64bf61314e0e8bdf5(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9091a25b0a2281020308a09f55e57da148e2f12e522813a9ad84ab34db3d06a7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a21a41aa06c59bba0d07e362c3f22e406cbe06a4eacb6a820867b23316cc7f2(
    *,
    download_speed: typing.Optional[jsii.Number] = None,
    upload_speed: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__592b4a4bb0948269132e914835a818ca4909b73e88f0d3cfeeea0fb241485511(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    device_id: builtins.str,
    global_network_id: builtins.str,
    link_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__193a8eac91ef709592b8ccf2b0620553a807381f865616069b571a5a14ff02d1(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c6cff788e17dcd4c0aa7bce78dbc0573997ce9011f9ee8444cea36c3274115e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed1cdb15e97d2900717e8b201967996154300677713c8143598891b7d417d675(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96f86556261820395986ba7acbd7b8156cfa0a1672e1c38e2bb4cf7cd9c5fad1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67215c31eae75fa556251496e69b477a798d5564fa5dc3454d37ea75d2afe359(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__687ba637c511969867f98bb143efd0735e1b70c11d4e7819f7a1815b3b809b32(
    *,
    device_id: builtins.str,
    global_network_id: builtins.str,
    link_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cefe7342b597379997b369b9f4aa644a8902928545cfe9bb1b97c6c52cffdc09(
    *,
    bandwidth: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLink.BandwidthProperty, typing.Dict[builtins.str, typing.Any]]],
    global_network_id: builtins.str,
    site_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    provider: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02d26caf3b597f4f3cac9111625d8131c4deeefd4ab607c87a0c1af546b9443d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    global_network_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSite.LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96fa61768102beaf099a9b62810c042cab8f1fbfda673150548342bfbd975456(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef7c7e1062c44ef0b7feb9417caa96ed9f6d6b6d43b0dd03a5aa5b911cd74a1c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc8803e9a4461e26d551cc4a419b4cd5d0bada265b033a999052a427929cfb6b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46188c191417eab8a9ca7f0b8f39542585227143528c34a981df829dff8b3e73(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9fbc23ce76923bed7902ba8ee0048c3665c496e695387f60a440db911264548(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSite.LocationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4acfa4f7a596e57882e361fb67af36d8b498b641763fab5731de8c92e52197e3(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__344f92c555fd2fc51fc42431c1ad3cd65a444ef3fa2fde5c0169d29240c01aaa(
    *,
    address: typing.Optional[builtins.str] = None,
    latitude: typing.Optional[builtins.str] = None,
    longitude: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__912c70020ab3c3833a813b389454ccf6e661a3c53f4d78e732b56acd3d19510f(
    *,
    global_network_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSite.LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aabf08c6f82f3c177f73a39833791562d59537dbe20329f7f5c42adbe2b1f639(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    core_network_id: builtins.str,
    vpn_connection_arn: builtins.str,
    proposed_segment_change: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSiteToSiteVpnAttachment.ProposedSegmentChangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a153038e0b02e958bd16c723a6208f7c87539a3c7d5b6826d1e7a48d50c721fe(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b47c74813a6cf63d4e08bfd46dc0c202c79ee346a65b09f04a4512be0f8e600(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fba7832d3fd7c322d67c2d3ab554048476534725099669bbb27f6c353ee461a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fde85f146ddbfe5918124ff34f04b28072bbe0389091946f95c9fe8cd8980f34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d5770719477965190780ebbb69883c941393da5c6c09af57bdb312f48810fbf(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSiteToSiteVpnAttachment.ProposedSegmentChangeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fedbd82359a7000ba160b74b2d678e59cb496867f32af82ab2500c7e1a61da46(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06bfa908f0244b4545d5fbff4fedab4e6c5def43fd0f8e30eee7f0c11bdf579d(
    *,
    attachment_policy_rule_number: typing.Optional[jsii.Number] = None,
    segment_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__113def3967f836e31386ebfbfb261bf671b49bfa26918b1a903a386050490f06(
    *,
    core_network_id: builtins.str,
    vpn_connection_arn: builtins.str,
    proposed_segment_change: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSiteToSiteVpnAttachment.ProposedSegmentChangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4fde2115bf574df497915820af61760b6c93b7557e556e0c61e96cab2148cca(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    core_network_id: builtins.str,
    transit_gateway_arn: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba04e436e3f0fbb5dc75d1bddfe8ea60eec91eccd85c9024ef441f25478231f6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a5454eff64fdb72ed40b9d0015efa7e0dadbfef17a53e7c427f3c0ddfa8cefc(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__439082e4f08493cbbc6d80e894b6f4dfd77144360df686a8c6f3a8211c56db01(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f61bd1b63b20558994e70ffe5513360796b00386f6642583ee771667f950f000(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__832f5e84db21f837c9c3c23bc334ca3604552518624f6a01c6743e9ad31fa391(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f875d5ddd6d4a16daeb616b41e1fe7b1f7aaab846db198d5fe405165ecae0b21(
    *,
    core_network_id: builtins.str,
    transit_gateway_arn: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d58980f8dc1987d036b6c6bdc2763c637f0d4882af63c260e581bf1489765c0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    global_network_id: builtins.str,
    transit_gateway_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b56abe01b4a10699a6a1c9ddbb6f2e6278f67eaa846769c67428a51d1a919d3(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4d12a2b835477bb65ab3df0f003b8ed235c9cb74d2882ad2c3ffe69eb90b5e4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3479609666aeb26b1973c2e635f65d0a6808b4152046244ab06699694f8afbee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7660bc4e9fada811170861b820a6606047adea2f279a8d4735670e4fa3b4aec0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__168dccdac681a836e54cbf046c9c06f14467cc24f0848929cbd9cb756b713041(
    *,
    global_network_id: builtins.str,
    transit_gateway_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76fd48cd4f7728733266eb51b353c86fecd583f774019081446c28ca5e2c04d8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    peering_id: builtins.str,
    transit_gateway_route_table_arn: builtins.str,
    proposed_segment_change: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransitGatewayRouteTableAttachment.ProposedSegmentChangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0eacc5d0b9706dded3d1c3179af64961084f56b76cdf528e23831708a5829099(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b83f1113ed5dd75a49a660552a54731d108a3e06a6ebd26415d5db93b873737(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc057602684fcd6d30d72064e2609de0278fcd49507560ee02b7a0f7eea74a4b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e96460515a73cddc08c4eeb7c5c0d62b3470f6ba77019112fad9b6b67d9b4313(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__833b64ddb00aa1bf9b86b7f76ee36148417740e18097f46e7c35c82b700f36f6(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTransitGatewayRouteTableAttachment.ProposedSegmentChangeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3b7316bcb7e40529995cb7c98b7c558e8ac3b24b7e6b5bcf786ac3da836b14a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__add1834976b0aa622dc8de71fbd481ec1596649e9c54a7426f53fab96a8fc95a(
    *,
    attachment_policy_rule_number: typing.Optional[jsii.Number] = None,
    segment_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32c28142db297494ed9a38267ab8bd9715938d6419db97dd30cc2434fec11a0a(
    *,
    peering_id: builtins.str,
    transit_gateway_route_table_arn: builtins.str,
    proposed_segment_change: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransitGatewayRouteTableAttachment.ProposedSegmentChangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__962ef8273d6d2d97a33b00603b7bf87793fdecfaae4031352d9cbc1bc6746602(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    core_network_id: builtins.str,
    subnet_arns: typing.Sequence[builtins.str],
    vpc_arn: builtins.str,
    options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnVpcAttachment.VpcOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    proposed_segment_change: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnVpcAttachment.ProposedSegmentChangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__066721874248356323b7edc6b2c638d14ec9d95fc08966f64139e05c40164db7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6a55bcf004239ce3b8b35d751875ec35c945b0b0645aa75a4d598eb6ea406b1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dc45980bc0f76e5b64f54c910888f2fbc61f8035b57f4cc2da0873460ceb6d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44eff42e1086acb3f04b3edb054dd6dc4f08bc4fde2b55e1211110fd05e54030(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__292ee8d1f17d2877219f1e655a187015b2e1a10520732d288dbc03f196471402(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4df78b42bf8dafd3f4ef447404aa6d3bb210d4de6d8c8238c7b7509fee4e6dc1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnVpcAttachment.VpcOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e08a82721c316f3d57592bb6309e39f40fb575ea68e4532f8a4bb8f162f0e1c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnVpcAttachment.ProposedSegmentChangeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10a9a6020f018ebc6f503414f839aac623a810484c578e3cc55c00a2aabd965f(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__557bf3a5ccb396638b970920d51e56a5af3a62c8b836006da453e705f15020ff(
    *,
    attachment_policy_rule_number: typing.Optional[jsii.Number] = None,
    segment_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0178ed6021c1858c87186be29fec1d6351e020d4e0f48dd2207432dbeaf7b50(
    *,
    appliance_mode_support: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ipv6_support: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12d5c20c6145e2cfb5336d480d3ded8850bc2ee5b31fe21ab1b44a90d4ad3e95(
    *,
    core_network_id: builtins.str,
    subnet_arns: typing.Sequence[builtins.str],
    vpc_arn: builtins.str,
    options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnVpcAttachment.VpcOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    proposed_segment_change: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnVpcAttachment.ProposedSegmentChangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
