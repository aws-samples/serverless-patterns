'''
# AWS::Connect Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_connect as connect
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Connect construct libraries](https://constructs.dev/search?q=connect)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Connect resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Connect.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Connect](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Connect.html).

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


@jsii.implements(_IInspectable_c2943556)
class CfnApprovedOrigin(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnApprovedOrigin",
):
    '''The approved origin for the instance.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-approvedorigin.html
    :cloudformationResource: AWS::Connect::ApprovedOrigin
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_approved_origin = connect.CfnApprovedOrigin(self, "MyCfnApprovedOrigin",
            instance_id="instanceId",
            origin="origin"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        instance_id: builtins.str,
        origin: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_id: The Amazon Resource Name (ARN) of the instance. *Minimum* : ``1`` *Maximum* : ``100``
        :param origin: Domain name to be added to the allow-list of the instance. *Maximum* : ``267``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44955422cb4c00b338f45e52a0d4136fdcdb94c8e433595b636f468d589e514a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApprovedOriginProps(instance_id=instance_id, origin=origin)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15b611bd9c5a92c253c2e2b0cba97b9f73bad0cfc8494953acb694fda143bba2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bc2ef7b8d5a06b007fe66bb9f5b0208e869ed47a6e5af0d6bf354f4df2d4d6c8)
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
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fd219e5b157d40fbc4254297a9308245796269c824a72c0b9db3bad7013261c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceId", value)

    @builtins.property
    @jsii.member(jsii_name="origin")
    def origin(self) -> builtins.str:
        '''Domain name to be added to the allow-list of the instance.'''
        return typing.cast(builtins.str, jsii.get(self, "origin"))

    @origin.setter
    def origin(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49fb9b02cf4a1b22d6433eac9cb35377d1877512b477dbf9c030fec47fb54f75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "origin", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnApprovedOriginProps",
    jsii_struct_bases=[],
    name_mapping={"instance_id": "instanceId", "origin": "origin"},
)
class CfnApprovedOriginProps:
    def __init__(self, *, instance_id: builtins.str, origin: builtins.str) -> None:
        '''Properties for defining a ``CfnApprovedOrigin``.

        :param instance_id: The Amazon Resource Name (ARN) of the instance. *Minimum* : ``1`` *Maximum* : ``100``
        :param origin: Domain name to be added to the allow-list of the instance. *Maximum* : ``267``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-approvedorigin.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_approved_origin_props = connect.CfnApprovedOriginProps(
                instance_id="instanceId",
                origin="origin"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__437fb8bad3e7665288233ec7ee3b4db6669d85ab53efddb888b5d729979a4e2f)
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
            check_type(argname="argument origin", value=origin, expected_type=type_hints["origin"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_id": instance_id,
            "origin": origin,
        }

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance.

        *Minimum* : ``1``

        *Maximum* : ``100``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-approvedorigin.html#cfn-connect-approvedorigin-instanceid
        '''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def origin(self) -> builtins.str:
        '''Domain name to be added to the allow-list of the instance.

        *Maximum* : ``267``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-approvedorigin.html#cfn-connect-approvedorigin-origin
        '''
        result = self._values.get("origin")
        assert result is not None, "Required property 'origin' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApprovedOriginProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnContactFlow(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnContactFlow",
):
    '''Specifies a flow for an Amazon Connect instance.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html
    :cloudformationResource: AWS::Connect::ContactFlow
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_contact_flow = connect.CfnContactFlow(self, "MyCfnContactFlow",
            content="content",
            instance_arn="instanceArn",
            name="name",
            type="type",
        
            # the properties below are optional
            description="description",
            state="state",
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
        content: builtins.str,
        instance_arn: builtins.str,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param content: The content of the flow. For more information, see `Amazon Connect Flow language <https://docs.aws.amazon.com/connect/latest/adminguide/flow-language.html>`_ in the *Amazon Connect Administrator Guide* .
        :param instance_arn: The Amazon Resource Name (ARN) of the Amazon Connect instance.
        :param name: The name of the flow.
        :param type: The type of the flow. For descriptions of the available types, see `Choose a flow type <https://docs.aws.amazon.com/connect/latest/adminguide/create-contact-flow.html#contact-flow-types>`_ in the *Amazon Connect Administrator Guide* .
        :param description: The description of the flow.
        :param state: The state of the flow.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bacec198fd7006a7e922c6b62694383eb7200d23c3f8da491f520191bdc8353f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnContactFlowProps(
            content=content,
            instance_arn=instance_arn,
            name=name,
            type=type,
            description=description,
            state=state,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aca14ea5542ff9acc3dc06746c7580c88c1e0b75d66bf0ac0a8cd785404cc173)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f4b3abb60d405603981215ec7d659c3d8939dbf9b5de879c8d56dfd0631f9d5b)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrContactFlowArn")
    def attr_contact_flow_arn(self) -> builtins.str:
        '''``Ref`` returns the Amazon Resource Name (ARN) of the flow. For example:.

        ``{ "Ref": "myFlowArn" }``

        :cloudformationAttribute: ContactFlowArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrContactFlowArn"))

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
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        '''The content of the flow.'''
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a517102f202efaced50f937df38d5374d2d8ae33c5659296852d677cbe73e2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon Connect instance.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20f6a7aacca6b49f3791bf907484b7af427677a1079ea79db9a45489b963b9d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the flow.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76f576a62faffae972ec30039ac3019bddb9b613e8dd2dce2b52723ba8a64dbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of the flow.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__213719edbc55495f331c0d1f51b7ab8a359f2c5cc563f3fa97077760121c6aa9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the flow.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e4573df3b75ab7b2ea3d0cba32ff3c515f11f6cbec43c0885d9ee30d25616a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> typing.Optional[builtins.str]:
        '''The state of the flow.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "state"))

    @state.setter
    def state(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7b6f72cf71dca93b2b2baae1d002d73d66de8e16bec7709efdb45c4bb811336)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22bc442433d76b98a1dae3304e1215f20c67d932bbfc6f02619483fbdb5d808d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnContactFlowModule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnContactFlowModule",
):
    '''Specifies a flow module for an Amazon Connect instance.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html
    :cloudformationResource: AWS::Connect::ContactFlowModule
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_contact_flow_module = connect.CfnContactFlowModule(self, "MyCfnContactFlowModule",
            content="content",
            instance_arn="instanceArn",
            name="name",
        
            # the properties below are optional
            description="description",
            state="state",
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
        content: builtins.str,
        instance_arn: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param content: The content of the flow module.
        :param instance_arn: The Amazon Resource Name (ARN) of the Amazon Connect instance.
        :param name: The name of the flow module.
        :param description: The description of the flow module.
        :param state: The state of the flow module.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__008a6ee0ce6447d7f5f7c62774a959e253bc4a69cef26848e6d3f74cf2381193)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnContactFlowModuleProps(
            content=content,
            instance_arn=instance_arn,
            name=name,
            description=description,
            state=state,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82176173dbe238b7a4715d8a94792d3696ada52a4372f823ab10f4c590c6193f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7f3e317a83e30b22f766c5d65c8451e4d9e5ffcd6510573aa22d0063860e7b99)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrContactFlowModuleArn")
    def attr_contact_flow_module_arn(self) -> builtins.str:
        '''``Ref`` returns the Amazon Resource Name (ARN) of the flow module. For example:.

        ``{ "Ref": "myFlowModuleArn" }``

        :cloudformationAttribute: ContactFlowModuleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrContactFlowModuleArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the contact flow module.

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
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        '''The content of the flow module.'''
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1701812aa93a58317265edab1cd66b5a843fc9845a1aed0b81f83c4f738b5b0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon Connect instance.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68b9231af4bcfc40233b3b8fbbd6acd02fe21a59b2f962738d2ce93d6ffa7fa7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the flow module.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e18e7239d9aefba3afcb9b93bf7f3ec9f6e4f173d51f91e93f5543efe25658a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the flow module.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c1841af03e44ad4a3c471a24f30aa57c457ec766515db087b0745fb9a6a68d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> typing.Optional[builtins.str]:
        '''The state of the flow module.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "state"))

    @state.setter
    def state(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25db523d57560a8813a16f507ae8c09c28625a53b6a24b5744ca978282ff51a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47de1c508f0616d427a0546578e35f062250082b28649c8985770019609a4881)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnContactFlowModuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "instance_arn": "instanceArn",
        "name": "name",
        "description": "description",
        "state": "state",
        "tags": "tags",
    },
)
class CfnContactFlowModuleProps:
    def __init__(
        self,
        *,
        content: builtins.str,
        instance_arn: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnContactFlowModule``.

        :param content: The content of the flow module.
        :param instance_arn: The Amazon Resource Name (ARN) of the Amazon Connect instance.
        :param name: The name of the flow module.
        :param description: The description of the flow module.
        :param state: The state of the flow module.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_contact_flow_module_props = connect.CfnContactFlowModuleProps(
                content="content",
                instance_arn="instanceArn",
                name="name",
            
                # the properties below are optional
                description="description",
                state="state",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84f0f2ba3fd7010e7e0bb6aaa71b591e31e6d4c4ad736e9c4e08be6f11de0102)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "content": content,
            "instance_arn": instance_arn,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if state is not None:
            self._values["state"] = state
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def content(self) -> builtins.str:
        '''The content of the flow module.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-content
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon Connect instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the flow module.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the flow module.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''The state of the flow module.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-state
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflowmodule.html#cfn-connect-contactflowmodule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnContactFlowModuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnContactFlowProps",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "instance_arn": "instanceArn",
        "name": "name",
        "type": "type",
        "description": "description",
        "state": "state",
        "tags": "tags",
    },
)
class CfnContactFlowProps:
    def __init__(
        self,
        *,
        content: builtins.str,
        instance_arn: builtins.str,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnContactFlow``.

        :param content: The content of the flow. For more information, see `Amazon Connect Flow language <https://docs.aws.amazon.com/connect/latest/adminguide/flow-language.html>`_ in the *Amazon Connect Administrator Guide* .
        :param instance_arn: The Amazon Resource Name (ARN) of the Amazon Connect instance.
        :param name: The name of the flow.
        :param type: The type of the flow. For descriptions of the available types, see `Choose a flow type <https://docs.aws.amazon.com/connect/latest/adminguide/create-contact-flow.html#contact-flow-types>`_ in the *Amazon Connect Administrator Guide* .
        :param description: The description of the flow.
        :param state: The state of the flow.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_contact_flow_props = connect.CfnContactFlowProps(
                content="content",
                instance_arn="instanceArn",
                name="name",
                type="type",
            
                # the properties below are optional
                description="description",
                state="state",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0555b19a226cc1a8bd054951921ffd23e0c635fe29a3d69a330d8262710a7d8)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "content": content,
            "instance_arn": instance_arn,
            "name": name,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if state is not None:
            self._values["state"] = state
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def content(self) -> builtins.str:
        '''The content of the flow.

        For more information, see `Amazon Connect Flow language <https://docs.aws.amazon.com/connect/latest/adminguide/flow-language.html>`_ in the *Amazon Connect Administrator Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-content
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon Connect instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the flow.

        For descriptions of the available types, see `Choose a flow type <https://docs.aws.amazon.com/connect/latest/adminguide/create-contact-flow.html#contact-flow-types>`_ in the *Amazon Connect Administrator Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''The state of the flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-state
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-contactflow.html#cfn-connect-contactflow-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnContactFlowProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnEvaluationForm(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnEvaluationForm",
):
    '''Creates an evaluation form for the specified Amazon Connect instance.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-evaluationform.html
    :cloudformationResource: AWS::Connect::EvaluationForm
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        # evaluation_form_section_property_: connect.CfnEvaluationForm.EvaluationFormSectionProperty
        
        cfn_evaluation_form = connect.CfnEvaluationForm(self, "MyCfnEvaluationForm",
            instance_arn="instanceArn",
            items=[connect.CfnEvaluationForm.EvaluationFormBaseItemProperty(
                section=connect.CfnEvaluationForm.EvaluationFormSectionProperty(
                    ref_id="refId",
                    title="title",
        
                    # the properties below are optional
                    instructions="instructions",
                    items=[connect.CfnEvaluationForm.EvaluationFormItemProperty(
                        question=connect.CfnEvaluationForm.EvaluationFormQuestionProperty(
                            question_type="questionType",
                            ref_id="refId",
                            title="title",
        
                            # the properties below are optional
                            instructions="instructions",
                            not_applicable_enabled=False,
                            question_type_properties=connect.CfnEvaluationForm.EvaluationFormQuestionTypePropertiesProperty(
                                numeric=connect.CfnEvaluationForm.EvaluationFormNumericQuestionPropertiesProperty(
                                    max_value=123,
                                    min_value=123,
        
                                    # the properties below are optional
                                    automation=connect.CfnEvaluationForm.EvaluationFormNumericQuestionAutomationProperty(
                                        property_value=connect.CfnEvaluationForm.NumericQuestionPropertyValueAutomationProperty(
                                            label="label"
                                        )
                                    ),
                                    options=[connect.CfnEvaluationForm.EvaluationFormNumericQuestionOptionProperty(
                                        max_value=123,
                                        min_value=123,
        
                                        # the properties below are optional
                                        automatic_fail=False,
                                        score=123
                                    )]
                                ),
                                single_select=connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionPropertiesProperty(
                                    options=[connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionOptionProperty(
                                        ref_id="refId",
                                        text="text",
        
                                        # the properties below are optional
                                        automatic_fail=False,
                                        score=123
                                    )],
        
                                    # the properties below are optional
                                    automation=connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationProperty(
                                        options=[connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationOptionProperty(
                                            rule_category=connect.CfnEvaluationForm.SingleSelectQuestionRuleCategoryAutomationProperty(
                                                category="category",
                                                condition="condition",
                                                option_ref_id="optionRefId"
                                            )
                                        )],
        
                                        # the properties below are optional
                                        default_option_ref_id="defaultOptionRefId"
                                    ),
                                    display_as="displayAs"
                                )
                            ),
                            weight=123
                        ),
                        section=evaluation_form_section_property_
                    )],
                    weight=123
                )
            )],
            status="status",
            title="title",
        
            # the properties below are optional
            description="description",
            scoring_strategy=connect.CfnEvaluationForm.ScoringStrategyProperty(
                mode="mode",
                status="status"
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
        instance_arn: builtins.str,
        items: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEvaluationForm.EvaluationFormBaseItemProperty", typing.Dict[builtins.str, typing.Any]]]]],
        status: builtins.str,
        title: builtins.str,
        description: typing.Optional[builtins.str] = None,
        scoring_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEvaluationForm.ScoringStrategyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_arn: The identifier of the Amazon Connect instance.
        :param items: Items that are part of the evaluation form. The total number of sections and questions must not exceed 100 each. Questions must be contained in a section. *Minimum size* : 1 *Maximum size* : 100
        :param status: The status of the evaluation form. *Allowed values* : ``DRAFT`` | ``ACTIVE`` Default: - "DRAFT"
        :param title: A title of the evaluation form.
        :param description: The description of the evaluation form. *Length Constraints* : Minimum length of 0. Maximum length of 1024.
        :param scoring_strategy: A scoring strategy of the evaluation form.
        :param tags: The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67672e07b9b284918b4f61d0c04df64749fd2f5f1f5a07e093b1e338fae6f20d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEvaluationFormProps(
            instance_arn=instance_arn,
            items=items,
            status=status,
            title=title,
            description=description,
            scoring_strategy=scoring_strategy,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8420425768038ffe2547f9ff300fef6a49b05240841e0c7ad3e44c95c4ab5725)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9c7ab1fa85562638f3f809a803e50bdd9d399a8c4e22aad540db331656c5a7e4)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrEvaluationFormArn")
    def attr_evaluation_form_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the evaluation form.

        :cloudformationAttribute: EvaluationFormArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEvaluationFormArn"))

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
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The identifier of the Amazon Connect instance.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e8c997caf14ee62e4089ac89d3358aef59cbdf6698b52bd57527b1af0ea2ebb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="items")
    def items(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormBaseItemProperty"]]]:
        '''Items that are part of the evaluation form.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormBaseItemProperty"]]], jsii.get(self, "items"))

    @items.setter
    def items(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormBaseItemProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24592bd80085495fe88d36be53b16b2dc291afc06a041b2135eb47206f64c9d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "items", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        '''The status of the evaluation form.'''
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__989b0b560f041388bf986f0dcb8487074564673bc25c4ffe3be8bbfd6e1a74b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        '''A title of the evaluation form.'''
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fe499614d5f5501fca8c029af605f671cdbfd45404bbcf2cb1dca048ab19e45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the evaluation form.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b9daef123f8c8ba72731239424846e3251f3e39a09700e6514170d316f71293)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="scoringStrategy")
    def scoring_strategy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.ScoringStrategyProperty"]]:
        '''A scoring strategy of the evaluation form.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.ScoringStrategyProperty"]], jsii.get(self, "scoringStrategy"))

    @scoring_strategy.setter
    def scoring_strategy(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.ScoringStrategyProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8ab41606e6f4148f72499568c63a3750f38b857a5fc25e01a04fcefb15350c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scoringStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec087e4492b70f062d224ca25c2f0d81dc78704ad8d957b26ed60e8e67176df5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnEvaluationForm.EvaluationFormBaseItemProperty",
        jsii_struct_bases=[],
        name_mapping={"section": "section"},
    )
    class EvaluationFormBaseItemProperty:
        def __init__(
            self,
            *,
            section: typing.Union[_IResolvable_da3f097b, typing.Union["CfnEvaluationForm.EvaluationFormSectionProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''An item at the root level.

            All items must be sections.

            :param section: A subsection or inner section of an item.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformbaseitem.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                # evaluation_form_section_property_: connect.CfnEvaluationForm.EvaluationFormSectionProperty
                
                evaluation_form_base_item_property = connect.CfnEvaluationForm.EvaluationFormBaseItemProperty(
                    section=connect.CfnEvaluationForm.EvaluationFormSectionProperty(
                        ref_id="refId",
                        title="title",
                
                        # the properties below are optional
                        instructions="instructions",
                        items=[connect.CfnEvaluationForm.EvaluationFormItemProperty(
                            question=connect.CfnEvaluationForm.EvaluationFormQuestionProperty(
                                question_type="questionType",
                                ref_id="refId",
                                title="title",
                
                                # the properties below are optional
                                instructions="instructions",
                                not_applicable_enabled=False,
                                question_type_properties=connect.CfnEvaluationForm.EvaluationFormQuestionTypePropertiesProperty(
                                    numeric=connect.CfnEvaluationForm.EvaluationFormNumericQuestionPropertiesProperty(
                                        max_value=123,
                                        min_value=123,
                
                                        # the properties below are optional
                                        automation=connect.CfnEvaluationForm.EvaluationFormNumericQuestionAutomationProperty(
                                            property_value=connect.CfnEvaluationForm.NumericQuestionPropertyValueAutomationProperty(
                                                label="label"
                                            )
                                        ),
                                        options=[connect.CfnEvaluationForm.EvaluationFormNumericQuestionOptionProperty(
                                            max_value=123,
                                            min_value=123,
                
                                            # the properties below are optional
                                            automatic_fail=False,
                                            score=123
                                        )]
                                    ),
                                    single_select=connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionPropertiesProperty(
                                        options=[connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionOptionProperty(
                                            ref_id="refId",
                                            text="text",
                
                                            # the properties below are optional
                                            automatic_fail=False,
                                            score=123
                                        )],
                
                                        # the properties below are optional
                                        automation=connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationProperty(
                                            options=[connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationOptionProperty(
                                                rule_category=connect.CfnEvaluationForm.SingleSelectQuestionRuleCategoryAutomationProperty(
                                                    category="category",
                                                    condition="condition",
                                                    option_ref_id="optionRefId"
                                                )
                                            )],
                
                                            # the properties below are optional
                                            default_option_ref_id="defaultOptionRefId"
                                        ),
                                        display_as="displayAs"
                                    )
                                ),
                                weight=123
                            ),
                            section=evaluation_form_section_property_
                        )],
                        weight=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5f23a880d7bbcb8fab0eba70189a52c3eb1d392f5651dc0f0a2fe54cf4df27d7)
                check_type(argname="argument section", value=section, expected_type=type_hints["section"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "section": section,
            }

        @builtins.property
        def section(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormSectionProperty"]:
            '''A subsection or inner section of an item.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformbaseitem.html#cfn-connect-evaluationform-evaluationformbaseitem-section
            '''
            result = self._values.get("section")
            assert result is not None, "Required property 'section' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormSectionProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EvaluationFormBaseItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnEvaluationForm.EvaluationFormItemProperty",
        jsii_struct_bases=[],
        name_mapping={"question": "question", "section": "section"},
    )
    class EvaluationFormItemProperty:
        def __init__(
            self,
            *,
            question: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEvaluationForm.EvaluationFormQuestionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            section: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEvaluationForm.EvaluationFormSectionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Items that are part of the evaluation form.

            The total number of sections and questions must not exceed 100 each. Questions must be contained in a section.

            :param question: The information of the question.
            :param section: The information of the section.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformitem.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                # evaluation_form_item_property_: connect.CfnEvaluationForm.EvaluationFormItemProperty
                
                evaluation_form_item_property = connect.CfnEvaluationForm.EvaluationFormItemProperty(
                    question=connect.CfnEvaluationForm.EvaluationFormQuestionProperty(
                        question_type="questionType",
                        ref_id="refId",
                        title="title",
                
                        # the properties below are optional
                        instructions="instructions",
                        not_applicable_enabled=False,
                        question_type_properties=connect.CfnEvaluationForm.EvaluationFormQuestionTypePropertiesProperty(
                            numeric=connect.CfnEvaluationForm.EvaluationFormNumericQuestionPropertiesProperty(
                                max_value=123,
                                min_value=123,
                
                                # the properties below are optional
                                automation=connect.CfnEvaluationForm.EvaluationFormNumericQuestionAutomationProperty(
                                    property_value=connect.CfnEvaluationForm.NumericQuestionPropertyValueAutomationProperty(
                                        label="label"
                                    )
                                ),
                                options=[connect.CfnEvaluationForm.EvaluationFormNumericQuestionOptionProperty(
                                    max_value=123,
                                    min_value=123,
                
                                    # the properties below are optional
                                    automatic_fail=False,
                                    score=123
                                )]
                            ),
                            single_select=connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionPropertiesProperty(
                                options=[connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionOptionProperty(
                                    ref_id="refId",
                                    text="text",
                
                                    # the properties below are optional
                                    automatic_fail=False,
                                    score=123
                                )],
                
                                # the properties below are optional
                                automation=connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationProperty(
                                    options=[connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationOptionProperty(
                                        rule_category=connect.CfnEvaluationForm.SingleSelectQuestionRuleCategoryAutomationProperty(
                                            category="category",
                                            condition="condition",
                                            option_ref_id="optionRefId"
                                        )
                                    )],
                
                                    # the properties below are optional
                                    default_option_ref_id="defaultOptionRefId"
                                ),
                                display_as="displayAs"
                            )
                        ),
                        weight=123
                    ),
                    section=connect.CfnEvaluationForm.EvaluationFormSectionProperty(
                        ref_id="refId",
                        title="title",
                
                        # the properties below are optional
                        instructions="instructions",
                        items=[evaluation_form_item_property_],
                        weight=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1ed93558b58ad3642a506969313dd38d56ce0f003f808635135ccaf5c8c578e4)
                check_type(argname="argument question", value=question, expected_type=type_hints["question"])
                check_type(argname="argument section", value=section, expected_type=type_hints["section"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if question is not None:
                self._values["question"] = question
            if section is not None:
                self._values["section"] = section

        @builtins.property
        def question(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormQuestionProperty"]]:
            '''The information of the question.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformitem.html#cfn-connect-evaluationform-evaluationformitem-question
            '''
            result = self._values.get("question")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormQuestionProperty"]], result)

        @builtins.property
        def section(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormSectionProperty"]]:
            '''The information of the section.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformitem.html#cfn-connect-evaluationform-evaluationformitem-section
            '''
            result = self._values.get("section")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormSectionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EvaluationFormItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnEvaluationForm.EvaluationFormNumericQuestionAutomationProperty",
        jsii_struct_bases=[],
        name_mapping={"property_value": "propertyValue"},
    )
    class EvaluationFormNumericQuestionAutomationProperty:
        def __init__(
            self,
            *,
            property_value: typing.Union[_IResolvable_da3f097b, typing.Union["CfnEvaluationForm.NumericQuestionPropertyValueAutomationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Information about the automation configuration in numeric questions.

            :param property_value: The property value of the automation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformnumericquestionautomation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                evaluation_form_numeric_question_automation_property = connect.CfnEvaluationForm.EvaluationFormNumericQuestionAutomationProperty(
                    property_value=connect.CfnEvaluationForm.NumericQuestionPropertyValueAutomationProperty(
                        label="label"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b81afcd26ca2b7f7f360e53cfff837a4d204082391c2522686bc1415137d9bb0)
                check_type(argname="argument property_value", value=property_value, expected_type=type_hints["property_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "property_value": property_value,
            }

        @builtins.property
        def property_value(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.NumericQuestionPropertyValueAutomationProperty"]:
            '''The property value of the automation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformnumericquestionautomation.html#cfn-connect-evaluationform-evaluationformnumericquestionautomation-propertyvalue
            '''
            result = self._values.get("property_value")
            assert result is not None, "Required property 'property_value' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.NumericQuestionPropertyValueAutomationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EvaluationFormNumericQuestionAutomationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnEvaluationForm.EvaluationFormNumericQuestionOptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_value": "maxValue",
            "min_value": "minValue",
            "automatic_fail": "automaticFail",
            "score": "score",
        },
    )
    class EvaluationFormNumericQuestionOptionProperty:
        def __init__(
            self,
            *,
            max_value: jsii.Number,
            min_value: jsii.Number,
            automatic_fail: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            score: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Information about the option range used for scoring in numeric questions.

            :param max_value: The maximum answer value of the range option.
            :param min_value: The minimum answer value of the range option.
            :param automatic_fail: The flag to mark the option as automatic fail. If an automatic fail answer is provided, the overall evaluation gets a score of 0.
            :param score: The score assigned to answer values within the range option. *Minimum* : 0 *Maximum* : 10

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformnumericquestionoption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                evaluation_form_numeric_question_option_property = connect.CfnEvaluationForm.EvaluationFormNumericQuestionOptionProperty(
                    max_value=123,
                    min_value=123,
                
                    # the properties below are optional
                    automatic_fail=False,
                    score=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b52418aba140bb56125771f8a631543b2ff66b57a21d4994b919cafe548ec537)
                check_type(argname="argument max_value", value=max_value, expected_type=type_hints["max_value"])
                check_type(argname="argument min_value", value=min_value, expected_type=type_hints["min_value"])
                check_type(argname="argument automatic_fail", value=automatic_fail, expected_type=type_hints["automatic_fail"])
                check_type(argname="argument score", value=score, expected_type=type_hints["score"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "max_value": max_value,
                "min_value": min_value,
            }
            if automatic_fail is not None:
                self._values["automatic_fail"] = automatic_fail
            if score is not None:
                self._values["score"] = score

        @builtins.property
        def max_value(self) -> jsii.Number:
            '''The maximum answer value of the range option.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformnumericquestionoption.html#cfn-connect-evaluationform-evaluationformnumericquestionoption-maxvalue
            '''
            result = self._values.get("max_value")
            assert result is not None, "Required property 'max_value' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def min_value(self) -> jsii.Number:
            '''The minimum answer value of the range option.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformnumericquestionoption.html#cfn-connect-evaluationform-evaluationformnumericquestionoption-minvalue
            '''
            result = self._values.get("min_value")
            assert result is not None, "Required property 'min_value' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def automatic_fail(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The flag to mark the option as automatic fail.

            If an automatic fail answer is provided, the overall evaluation gets a score of 0.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformnumericquestionoption.html#cfn-connect-evaluationform-evaluationformnumericquestionoption-automaticfail
            '''
            result = self._values.get("automatic_fail")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def score(self) -> typing.Optional[jsii.Number]:
            '''The score assigned to answer values within the range option.

            *Minimum* : 0

            *Maximum* : 10

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformnumericquestionoption.html#cfn-connect-evaluationform-evaluationformnumericquestionoption-score
            '''
            result = self._values.get("score")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EvaluationFormNumericQuestionOptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnEvaluationForm.EvaluationFormNumericQuestionPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_value": "maxValue",
            "min_value": "minValue",
            "automation": "automation",
            "options": "options",
        },
    )
    class EvaluationFormNumericQuestionPropertiesProperty:
        def __init__(
            self,
            *,
            max_value: jsii.Number,
            min_value: jsii.Number,
            automation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEvaluationForm.EvaluationFormNumericQuestionAutomationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEvaluationForm.EvaluationFormNumericQuestionOptionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Information about properties for a numeric question in an evaluation form.

            :param max_value: The maximum answer value.
            :param min_value: The minimum answer value.
            :param automation: The automation properties of the numeric question.
            :param options: The scoring options of the numeric question.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformnumericquestionproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                evaluation_form_numeric_question_properties_property = connect.CfnEvaluationForm.EvaluationFormNumericQuestionPropertiesProperty(
                    max_value=123,
                    min_value=123,
                
                    # the properties below are optional
                    automation=connect.CfnEvaluationForm.EvaluationFormNumericQuestionAutomationProperty(
                        property_value=connect.CfnEvaluationForm.NumericQuestionPropertyValueAutomationProperty(
                            label="label"
                        )
                    ),
                    options=[connect.CfnEvaluationForm.EvaluationFormNumericQuestionOptionProperty(
                        max_value=123,
                        min_value=123,
                
                        # the properties below are optional
                        automatic_fail=False,
                        score=123
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6fdebefe553e70e8e484dd5dc1c652ee40882ca2d19bc3a12aa677060f0c897d)
                check_type(argname="argument max_value", value=max_value, expected_type=type_hints["max_value"])
                check_type(argname="argument min_value", value=min_value, expected_type=type_hints["min_value"])
                check_type(argname="argument automation", value=automation, expected_type=type_hints["automation"])
                check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "max_value": max_value,
                "min_value": min_value,
            }
            if automation is not None:
                self._values["automation"] = automation
            if options is not None:
                self._values["options"] = options

        @builtins.property
        def max_value(self) -> jsii.Number:
            '''The maximum answer value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformnumericquestionproperties.html#cfn-connect-evaluationform-evaluationformnumericquestionproperties-maxvalue
            '''
            result = self._values.get("max_value")
            assert result is not None, "Required property 'max_value' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def min_value(self) -> jsii.Number:
            '''The minimum answer value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformnumericquestionproperties.html#cfn-connect-evaluationform-evaluationformnumericquestionproperties-minvalue
            '''
            result = self._values.get("min_value")
            assert result is not None, "Required property 'min_value' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def automation(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormNumericQuestionAutomationProperty"]]:
            '''The automation properties of the numeric question.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformnumericquestionproperties.html#cfn-connect-evaluationform-evaluationformnumericquestionproperties-automation
            '''
            result = self._values.get("automation")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormNumericQuestionAutomationProperty"]], result)

        @builtins.property
        def options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormNumericQuestionOptionProperty"]]]]:
            '''The scoring options of the numeric question.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformnumericquestionproperties.html#cfn-connect-evaluationform-evaluationformnumericquestionproperties-options
            '''
            result = self._values.get("options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormNumericQuestionOptionProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EvaluationFormNumericQuestionPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnEvaluationForm.EvaluationFormQuestionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "question_type": "questionType",
            "ref_id": "refId",
            "title": "title",
            "instructions": "instructions",
            "not_applicable_enabled": "notApplicableEnabled",
            "question_type_properties": "questionTypeProperties",
            "weight": "weight",
        },
    )
    class EvaluationFormQuestionProperty:
        def __init__(
            self,
            *,
            question_type: builtins.str,
            ref_id: builtins.str,
            title: builtins.str,
            instructions: typing.Optional[builtins.str] = None,
            not_applicable_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            question_type_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEvaluationForm.EvaluationFormQuestionTypePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            weight: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Information about a question from an evaluation form.

            :param question_type: The type of the question. *Allowed values* : ``NUMERIC`` | ``SINGLESELECT`` | ``TEXT``
            :param ref_id: The identifier of the question. An identifier must be unique within the evaluation form. *Length Constraints* : Minimum length of 1. Maximum length of 40.
            :param title: The title of the question. *Length Constraints* : Minimum length of 1. Maximum length of 350.
            :param instructions: The instructions of the section. *Length Constraints* : Minimum length of 0. Maximum length of 1024.
            :param not_applicable_enabled: The flag to enable not applicable answers to the question.
            :param question_type_properties: The properties of the type of question. Text questions do not have to define question type properties.
            :param weight: The scoring weight of the section. *Minimum* : 0 *Maximum* : 100

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformquestion.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                evaluation_form_question_property = connect.CfnEvaluationForm.EvaluationFormQuestionProperty(
                    question_type="questionType",
                    ref_id="refId",
                    title="title",
                
                    # the properties below are optional
                    instructions="instructions",
                    not_applicable_enabled=False,
                    question_type_properties=connect.CfnEvaluationForm.EvaluationFormQuestionTypePropertiesProperty(
                        numeric=connect.CfnEvaluationForm.EvaluationFormNumericQuestionPropertiesProperty(
                            max_value=123,
                            min_value=123,
                
                            # the properties below are optional
                            automation=connect.CfnEvaluationForm.EvaluationFormNumericQuestionAutomationProperty(
                                property_value=connect.CfnEvaluationForm.NumericQuestionPropertyValueAutomationProperty(
                                    label="label"
                                )
                            ),
                            options=[connect.CfnEvaluationForm.EvaluationFormNumericQuestionOptionProperty(
                                max_value=123,
                                min_value=123,
                
                                # the properties below are optional
                                automatic_fail=False,
                                score=123
                            )]
                        ),
                        single_select=connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionPropertiesProperty(
                            options=[connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionOptionProperty(
                                ref_id="refId",
                                text="text",
                
                                # the properties below are optional
                                automatic_fail=False,
                                score=123
                            )],
                
                            # the properties below are optional
                            automation=connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationProperty(
                                options=[connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationOptionProperty(
                                    rule_category=connect.CfnEvaluationForm.SingleSelectQuestionRuleCategoryAutomationProperty(
                                        category="category",
                                        condition="condition",
                                        option_ref_id="optionRefId"
                                    )
                                )],
                
                                # the properties below are optional
                                default_option_ref_id="defaultOptionRefId"
                            ),
                            display_as="displayAs"
                        )
                    ),
                    weight=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__76f87135992dba43e2709251a961f9661f40617cabeb04621ceba33e2e2a0831)
                check_type(argname="argument question_type", value=question_type, expected_type=type_hints["question_type"])
                check_type(argname="argument ref_id", value=ref_id, expected_type=type_hints["ref_id"])
                check_type(argname="argument title", value=title, expected_type=type_hints["title"])
                check_type(argname="argument instructions", value=instructions, expected_type=type_hints["instructions"])
                check_type(argname="argument not_applicable_enabled", value=not_applicable_enabled, expected_type=type_hints["not_applicable_enabled"])
                check_type(argname="argument question_type_properties", value=question_type_properties, expected_type=type_hints["question_type_properties"])
                check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "question_type": question_type,
                "ref_id": ref_id,
                "title": title,
            }
            if instructions is not None:
                self._values["instructions"] = instructions
            if not_applicable_enabled is not None:
                self._values["not_applicable_enabled"] = not_applicable_enabled
            if question_type_properties is not None:
                self._values["question_type_properties"] = question_type_properties
            if weight is not None:
                self._values["weight"] = weight

        @builtins.property
        def question_type(self) -> builtins.str:
            '''The type of the question.

            *Allowed values* : ``NUMERIC`` | ``SINGLESELECT`` | ``TEXT``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformquestion.html#cfn-connect-evaluationform-evaluationformquestion-questiontype
            '''
            result = self._values.get("question_type")
            assert result is not None, "Required property 'question_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def ref_id(self) -> builtins.str:
            '''The identifier of the question. An identifier must be unique within the evaluation form.

            *Length Constraints* : Minimum length of 1. Maximum length of 40.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformquestion.html#cfn-connect-evaluationform-evaluationformquestion-refid
            '''
            result = self._values.get("ref_id")
            assert result is not None, "Required property 'ref_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def title(self) -> builtins.str:
            '''The title of the question.

            *Length Constraints* : Minimum length of 1. Maximum length of 350.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformquestion.html#cfn-connect-evaluationform-evaluationformquestion-title
            '''
            result = self._values.get("title")
            assert result is not None, "Required property 'title' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def instructions(self) -> typing.Optional[builtins.str]:
            '''The instructions of the section.

            *Length Constraints* : Minimum length of 0. Maximum length of 1024.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformquestion.html#cfn-connect-evaluationform-evaluationformquestion-instructions
            '''
            result = self._values.get("instructions")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def not_applicable_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The flag to enable not applicable answers to the question.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformquestion.html#cfn-connect-evaluationform-evaluationformquestion-notapplicableenabled
            '''
            result = self._values.get("not_applicable_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def question_type_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormQuestionTypePropertiesProperty"]]:
            '''The properties of the type of question.

            Text questions do not have to define question type properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformquestion.html#cfn-connect-evaluationform-evaluationformquestion-questiontypeproperties
            '''
            result = self._values.get("question_type_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormQuestionTypePropertiesProperty"]], result)

        @builtins.property
        def weight(self) -> typing.Optional[jsii.Number]:
            '''The scoring weight of the section.

            *Minimum* : 0

            *Maximum* : 100

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformquestion.html#cfn-connect-evaluationform-evaluationformquestion-weight
            '''
            result = self._values.get("weight")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EvaluationFormQuestionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnEvaluationForm.EvaluationFormQuestionTypePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"numeric": "numeric", "single_select": "singleSelect"},
    )
    class EvaluationFormQuestionTypePropertiesProperty:
        def __init__(
            self,
            *,
            numeric: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEvaluationForm.EvaluationFormNumericQuestionPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            single_select: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEvaluationForm.EvaluationFormSingleSelectQuestionPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Information about properties for a question in an evaluation form.

            The question type properties must be either for a numeric question or a single select question.

            :param numeric: The properties of the numeric question.
            :param single_select: The properties of the numeric question.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformquestiontypeproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                evaluation_form_question_type_properties_property = connect.CfnEvaluationForm.EvaluationFormQuestionTypePropertiesProperty(
                    numeric=connect.CfnEvaluationForm.EvaluationFormNumericQuestionPropertiesProperty(
                        max_value=123,
                        min_value=123,
                
                        # the properties below are optional
                        automation=connect.CfnEvaluationForm.EvaluationFormNumericQuestionAutomationProperty(
                            property_value=connect.CfnEvaluationForm.NumericQuestionPropertyValueAutomationProperty(
                                label="label"
                            )
                        ),
                        options=[connect.CfnEvaluationForm.EvaluationFormNumericQuestionOptionProperty(
                            max_value=123,
                            min_value=123,
                
                            # the properties below are optional
                            automatic_fail=False,
                            score=123
                        )]
                    ),
                    single_select=connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionPropertiesProperty(
                        options=[connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionOptionProperty(
                            ref_id="refId",
                            text="text",
                
                            # the properties below are optional
                            automatic_fail=False,
                            score=123
                        )],
                
                        # the properties below are optional
                        automation=connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationProperty(
                            options=[connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationOptionProperty(
                                rule_category=connect.CfnEvaluationForm.SingleSelectQuestionRuleCategoryAutomationProperty(
                                    category="category",
                                    condition="condition",
                                    option_ref_id="optionRefId"
                                )
                            )],
                
                            # the properties below are optional
                            default_option_ref_id="defaultOptionRefId"
                        ),
                        display_as="displayAs"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9c2a28674a94b033e97fe7c1b9bbd46fbd0b917a1605152cbffbc509362bd288)
                check_type(argname="argument numeric", value=numeric, expected_type=type_hints["numeric"])
                check_type(argname="argument single_select", value=single_select, expected_type=type_hints["single_select"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if numeric is not None:
                self._values["numeric"] = numeric
            if single_select is not None:
                self._values["single_select"] = single_select

        @builtins.property
        def numeric(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormNumericQuestionPropertiesProperty"]]:
            '''The properties of the numeric question.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformquestiontypeproperties.html#cfn-connect-evaluationform-evaluationformquestiontypeproperties-numeric
            '''
            result = self._values.get("numeric")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormNumericQuestionPropertiesProperty"]], result)

        @builtins.property
        def single_select(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormSingleSelectQuestionPropertiesProperty"]]:
            '''The properties of the numeric question.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformquestiontypeproperties.html#cfn-connect-evaluationform-evaluationformquestiontypeproperties-singleselect
            '''
            result = self._values.get("single_select")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormSingleSelectQuestionPropertiesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EvaluationFormQuestionTypePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnEvaluationForm.EvaluationFormSectionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ref_id": "refId",
            "title": "title",
            "instructions": "instructions",
            "items": "items",
            "weight": "weight",
        },
    )
    class EvaluationFormSectionProperty:
        def __init__(
            self,
            *,
            ref_id: builtins.str,
            title: builtins.str,
            instructions: typing.Optional[builtins.str] = None,
            items: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEvaluationForm.EvaluationFormItemProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            weight: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Information about a section from an evaluation form.

            A section can contain sections and/or questions. Evaluation forms can only contain sections and subsections (two level nesting).

            :param ref_id: The identifier of the section. An identifier must be unique within the evaluation form. *Length Constraints* : Minimum length of 1. Maximum length of 40.
            :param title: The title of the section. *Length Constraints* : Minimum length of 1. Maximum length of 128.
            :param instructions: The instructions of the section.
            :param items: The items of the section. *Minimum* : 1
            :param weight: The scoring weight of the section. *Minimum* : 0 *Maximum* : 100

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsection.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                # evaluation_form_section_property_: connect.CfnEvaluationForm.EvaluationFormSectionProperty
                
                evaluation_form_section_property = connect.CfnEvaluationForm.EvaluationFormSectionProperty(
                    ref_id="refId",
                    title="title",
                
                    # the properties below are optional
                    instructions="instructions",
                    items=[connect.CfnEvaluationForm.EvaluationFormItemProperty(
                        question=connect.CfnEvaluationForm.EvaluationFormQuestionProperty(
                            question_type="questionType",
                            ref_id="refId",
                            title="title",
                
                            # the properties below are optional
                            instructions="instructions",
                            not_applicable_enabled=False,
                            question_type_properties=connect.CfnEvaluationForm.EvaluationFormQuestionTypePropertiesProperty(
                                numeric=connect.CfnEvaluationForm.EvaluationFormNumericQuestionPropertiesProperty(
                                    max_value=123,
                                    min_value=123,
                
                                    # the properties below are optional
                                    automation=connect.CfnEvaluationForm.EvaluationFormNumericQuestionAutomationProperty(
                                        property_value=connect.CfnEvaluationForm.NumericQuestionPropertyValueAutomationProperty(
                                            label="label"
                                        )
                                    ),
                                    options=[connect.CfnEvaluationForm.EvaluationFormNumericQuestionOptionProperty(
                                        max_value=123,
                                        min_value=123,
                
                                        # the properties below are optional
                                        automatic_fail=False,
                                        score=123
                                    )]
                                ),
                                single_select=connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionPropertiesProperty(
                                    options=[connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionOptionProperty(
                                        ref_id="refId",
                                        text="text",
                
                                        # the properties below are optional
                                        automatic_fail=False,
                                        score=123
                                    )],
                
                                    # the properties below are optional
                                    automation=connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationProperty(
                                        options=[connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationOptionProperty(
                                            rule_category=connect.CfnEvaluationForm.SingleSelectQuestionRuleCategoryAutomationProperty(
                                                category="category",
                                                condition="condition",
                                                option_ref_id="optionRefId"
                                            )
                                        )],
                
                                        # the properties below are optional
                                        default_option_ref_id="defaultOptionRefId"
                                    ),
                                    display_as="displayAs"
                                )
                            ),
                            weight=123
                        ),
                        section=evaluation_form_section_property_
                    )],
                    weight=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__016fd84ffa312050ab1787423e77775e0c40fb4835c07025e616e21af7a958db)
                check_type(argname="argument ref_id", value=ref_id, expected_type=type_hints["ref_id"])
                check_type(argname="argument title", value=title, expected_type=type_hints["title"])
                check_type(argname="argument instructions", value=instructions, expected_type=type_hints["instructions"])
                check_type(argname="argument items", value=items, expected_type=type_hints["items"])
                check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "ref_id": ref_id,
                "title": title,
            }
            if instructions is not None:
                self._values["instructions"] = instructions
            if items is not None:
                self._values["items"] = items
            if weight is not None:
                self._values["weight"] = weight

        @builtins.property
        def ref_id(self) -> builtins.str:
            '''The identifier of the section. An identifier must be unique within the evaluation form.

            *Length Constraints* : Minimum length of 1. Maximum length of 40.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsection.html#cfn-connect-evaluationform-evaluationformsection-refid
            '''
            result = self._values.get("ref_id")
            assert result is not None, "Required property 'ref_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def title(self) -> builtins.str:
            '''The title of the section.

            *Length Constraints* : Minimum length of 1. Maximum length of 128.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsection.html#cfn-connect-evaluationform-evaluationformsection-title
            '''
            result = self._values.get("title")
            assert result is not None, "Required property 'title' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def instructions(self) -> typing.Optional[builtins.str]:
            '''The instructions of the section.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsection.html#cfn-connect-evaluationform-evaluationformsection-instructions
            '''
            result = self._values.get("instructions")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def items(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormItemProperty"]]]]:
            '''The items of the section.

            *Minimum* : 1

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsection.html#cfn-connect-evaluationform-evaluationformsection-items
            '''
            result = self._values.get("items")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormItemProperty"]]]], result)

        @builtins.property
        def weight(self) -> typing.Optional[jsii.Number]:
            '''The scoring weight of the section.

            *Minimum* : 0

            *Maximum* : 100

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsection.html#cfn-connect-evaluationform-evaluationformsection-weight
            '''
            result = self._values.get("weight")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EvaluationFormSectionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationOptionProperty",
        jsii_struct_bases=[],
        name_mapping={"rule_category": "ruleCategory"},
    )
    class EvaluationFormSingleSelectQuestionAutomationOptionProperty:
        def __init__(
            self,
            *,
            rule_category: typing.Union[_IResolvable_da3f097b, typing.Union["CfnEvaluationForm.SingleSelectQuestionRuleCategoryAutomationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The automation options of the single select question.

            :param rule_category: The automation option based on a rule category for the single select question.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionautomationoption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                evaluation_form_single_select_question_automation_option_property = connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationOptionProperty(
                    rule_category=connect.CfnEvaluationForm.SingleSelectQuestionRuleCategoryAutomationProperty(
                        category="category",
                        condition="condition",
                        option_ref_id="optionRefId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e3628da3194346fb903c2da16aee6a4931544b13dac0a74d2857ffd14617e3af)
                check_type(argname="argument rule_category", value=rule_category, expected_type=type_hints["rule_category"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "rule_category": rule_category,
            }

        @builtins.property
        def rule_category(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.SingleSelectQuestionRuleCategoryAutomationProperty"]:
            '''The automation option based on a rule category for the single select question.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionautomationoption.html#cfn-connect-evaluationform-evaluationformsingleselectquestionautomationoption-rulecategory
            '''
            result = self._values.get("rule_category")
            assert result is not None, "Required property 'rule_category' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.SingleSelectQuestionRuleCategoryAutomationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EvaluationFormSingleSelectQuestionAutomationOptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "options": "options",
            "default_option_ref_id": "defaultOptionRefId",
        },
    )
    class EvaluationFormSingleSelectQuestionAutomationProperty:
        def __init__(
            self,
            *,
            options: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationOptionProperty", typing.Dict[builtins.str, typing.Any]]]]],
            default_option_ref_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about the automation configuration in single select questions.

            Automation options are evaluated in order, and the first matched option is applied. If no automation option matches, and there is a default option, then the default option is applied.

            :param options: The automation options of the single select question. *Minimum* : 1 *Maximum* : 20
            :param default_option_ref_id: The identifier of the default answer option, when none of the automation options match the criteria. *Length Constraints* : Minimum length of 1. Maximum length of 40.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionautomation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                evaluation_form_single_select_question_automation_property = connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationProperty(
                    options=[connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationOptionProperty(
                        rule_category=connect.CfnEvaluationForm.SingleSelectQuestionRuleCategoryAutomationProperty(
                            category="category",
                            condition="condition",
                            option_ref_id="optionRefId"
                        )
                    )],
                
                    # the properties below are optional
                    default_option_ref_id="defaultOptionRefId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fc97b2bfa6d5fb8da071bf0ca06feb3e4bb442b1422677cdb6c7ae776fc3629c)
                check_type(argname="argument options", value=options, expected_type=type_hints["options"])
                check_type(argname="argument default_option_ref_id", value=default_option_ref_id, expected_type=type_hints["default_option_ref_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "options": options,
            }
            if default_option_ref_id is not None:
                self._values["default_option_ref_id"] = default_option_ref_id

        @builtins.property
        def options(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationOptionProperty"]]]:
            '''The automation options of the single select question.

            *Minimum* : 1

            *Maximum* : 20

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionautomation.html#cfn-connect-evaluationform-evaluationformsingleselectquestionautomation-options
            '''
            result = self._values.get("options")
            assert result is not None, "Required property 'options' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationOptionProperty"]]], result)

        @builtins.property
        def default_option_ref_id(self) -> typing.Optional[builtins.str]:
            '''The identifier of the default answer option, when none of the automation options match the criteria.

            *Length Constraints* : Minimum length of 1. Maximum length of 40.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionautomation.html#cfn-connect-evaluationform-evaluationformsingleselectquestionautomation-defaultoptionrefid
            '''
            result = self._values.get("default_option_ref_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EvaluationFormSingleSelectQuestionAutomationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionOptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ref_id": "refId",
            "text": "text",
            "automatic_fail": "automaticFail",
            "score": "score",
        },
    )
    class EvaluationFormSingleSelectQuestionOptionProperty:
        def __init__(
            self,
            *,
            ref_id: builtins.str,
            text: builtins.str,
            automatic_fail: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            score: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Information about the automation configuration in single select questions.

            :param ref_id: The identifier of the answer option. An identifier must be unique within the question. *Length Constraints* : Minimum length of 1. Maximum length of 40.
            :param text: The title of the answer option. *Length Constraints* : Minimum length of 1. Maximum length of 128.
            :param automatic_fail: The flag to mark the option as automatic fail. If an automatic fail answer is provided, the overall evaluation gets a score of 0.
            :param score: The score assigned to the answer option. *Minimum* : 0 *Maximum* : 10

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionoption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                evaluation_form_single_select_question_option_property = connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionOptionProperty(
                    ref_id="refId",
                    text="text",
                
                    # the properties below are optional
                    automatic_fail=False,
                    score=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__511068b0668e9106d683cef742ddd4f219ab5e8b7872b9c6d3692faf6c91a2a2)
                check_type(argname="argument ref_id", value=ref_id, expected_type=type_hints["ref_id"])
                check_type(argname="argument text", value=text, expected_type=type_hints["text"])
                check_type(argname="argument automatic_fail", value=automatic_fail, expected_type=type_hints["automatic_fail"])
                check_type(argname="argument score", value=score, expected_type=type_hints["score"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "ref_id": ref_id,
                "text": text,
            }
            if automatic_fail is not None:
                self._values["automatic_fail"] = automatic_fail
            if score is not None:
                self._values["score"] = score

        @builtins.property
        def ref_id(self) -> builtins.str:
            '''The identifier of the answer option. An identifier must be unique within the question.

            *Length Constraints* : Minimum length of 1. Maximum length of 40.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionoption.html#cfn-connect-evaluationform-evaluationformsingleselectquestionoption-refid
            '''
            result = self._values.get("ref_id")
            assert result is not None, "Required property 'ref_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def text(self) -> builtins.str:
            '''The title of the answer option.

            *Length Constraints* : Minimum length of 1. Maximum length of 128.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionoption.html#cfn-connect-evaluationform-evaluationformsingleselectquestionoption-text
            '''
            result = self._values.get("text")
            assert result is not None, "Required property 'text' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def automatic_fail(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The flag to mark the option as automatic fail.

            If an automatic fail answer is provided, the overall evaluation gets a score of 0.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionoption.html#cfn-connect-evaluationform-evaluationformsingleselectquestionoption-automaticfail
            '''
            result = self._values.get("automatic_fail")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def score(self) -> typing.Optional[jsii.Number]:
            '''The score assigned to the answer option.

            *Minimum* : 0

            *Maximum* : 10

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionoption.html#cfn-connect-evaluationform-evaluationformsingleselectquestionoption-score
            '''
            result = self._values.get("score")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EvaluationFormSingleSelectQuestionOptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "options": "options",
            "automation": "automation",
            "display_as": "displayAs",
        },
    )
    class EvaluationFormSingleSelectQuestionPropertiesProperty:
        def __init__(
            self,
            *,
            options: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEvaluationForm.EvaluationFormSingleSelectQuestionOptionProperty", typing.Dict[builtins.str, typing.Any]]]]],
            automation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            display_as: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about the options in single select questions.

            :param options: The answer options of the single select question. *Minimum* : 2 *Maximum* : 256
            :param automation: The display mode of the single select question.
            :param display_as: The display mode of the single select question. *Allowed values* : ``DROPDOWN`` | ``RADIO``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                evaluation_form_single_select_question_properties_property = connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionPropertiesProperty(
                    options=[connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionOptionProperty(
                        ref_id="refId",
                        text="text",
                
                        # the properties below are optional
                        automatic_fail=False,
                        score=123
                    )],
                
                    # the properties below are optional
                    automation=connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationProperty(
                        options=[connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationOptionProperty(
                            rule_category=connect.CfnEvaluationForm.SingleSelectQuestionRuleCategoryAutomationProperty(
                                category="category",
                                condition="condition",
                                option_ref_id="optionRefId"
                            )
                        )],
                
                        # the properties below are optional
                        default_option_ref_id="defaultOptionRefId"
                    ),
                    display_as="displayAs"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__45e8b8c481c725b1ed84e34212cf426ea008289d40995f757fe99cb6f3130e54)
                check_type(argname="argument options", value=options, expected_type=type_hints["options"])
                check_type(argname="argument automation", value=automation, expected_type=type_hints["automation"])
                check_type(argname="argument display_as", value=display_as, expected_type=type_hints["display_as"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "options": options,
            }
            if automation is not None:
                self._values["automation"] = automation
            if display_as is not None:
                self._values["display_as"] = display_as

        @builtins.property
        def options(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormSingleSelectQuestionOptionProperty"]]]:
            '''The answer options of the single select question.

            *Minimum* : 2

            *Maximum* : 256

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionproperties.html#cfn-connect-evaluationform-evaluationformsingleselectquestionproperties-options
            '''
            result = self._values.get("options")
            assert result is not None, "Required property 'options' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormSingleSelectQuestionOptionProperty"]]], result)

        @builtins.property
        def automation(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationProperty"]]:
            '''The display mode of the single select question.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionproperties.html#cfn-connect-evaluationform-evaluationformsingleselectquestionproperties-automation
            '''
            result = self._values.get("automation")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationProperty"]], result)

        @builtins.property
        def display_as(self) -> typing.Optional[builtins.str]:
            '''The display mode of the single select question.

            *Allowed values* : ``DROPDOWN`` | ``RADIO``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-evaluationformsingleselectquestionproperties.html#cfn-connect-evaluationform-evaluationformsingleselectquestionproperties-displayas
            '''
            result = self._values.get("display_as")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EvaluationFormSingleSelectQuestionPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnEvaluationForm.NumericQuestionPropertyValueAutomationProperty",
        jsii_struct_bases=[],
        name_mapping={"label": "label"},
    )
    class NumericQuestionPropertyValueAutomationProperty:
        def __init__(self, *, label: builtins.str) -> None:
            '''Information about the property value used in automation of a numeric questions.

            :param label: The property label of the automation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-numericquestionpropertyvalueautomation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                numeric_question_property_value_automation_property = connect.CfnEvaluationForm.NumericQuestionPropertyValueAutomationProperty(
                    label="label"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5c2101c26bfd31e1208bce72ced73e086806ccc5e207eec345b38abde0b4647d)
                check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "label": label,
            }

        @builtins.property
        def label(self) -> builtins.str:
            '''The property label of the automation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-numericquestionpropertyvalueautomation.html#cfn-connect-evaluationform-numericquestionpropertyvalueautomation-label
            '''
            result = self._values.get("label")
            assert result is not None, "Required property 'label' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NumericQuestionPropertyValueAutomationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnEvaluationForm.ScoringStrategyProperty",
        jsii_struct_bases=[],
        name_mapping={"mode": "mode", "status": "status"},
    )
    class ScoringStrategyProperty:
        def __init__(self, *, mode: builtins.str, status: builtins.str) -> None:
            '''A scoring strategy of the evaluation form.

            :param mode: The scoring mode of the evaluation form. *Allowed values* : ``QUESTION_ONLY`` | ``SECTION_ONLY``
            :param status: The scoring status of the evaluation form. *Allowed values* : ``ENABLED`` | ``DISABLED``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-scoringstrategy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                scoring_strategy_property = connect.CfnEvaluationForm.ScoringStrategyProperty(
                    mode="mode",
                    status="status"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__36b59a77759bb952407e2a520298a2e8de054a6d394464d5d2df9e38f1efc2e3)
                check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "mode": mode,
                "status": status,
            }

        @builtins.property
        def mode(self) -> builtins.str:
            '''The scoring mode of the evaluation form.

            *Allowed values* : ``QUESTION_ONLY`` | ``SECTION_ONLY``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-scoringstrategy.html#cfn-connect-evaluationform-scoringstrategy-mode
            '''
            result = self._values.get("mode")
            assert result is not None, "Required property 'mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def status(self) -> builtins.str:
            '''The scoring status of the evaluation form.

            *Allowed values* : ``ENABLED`` | ``DISABLED``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-scoringstrategy.html#cfn-connect-evaluationform-scoringstrategy-status
            '''
            result = self._values.get("status")
            assert result is not None, "Required property 'status' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScoringStrategyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnEvaluationForm.SingleSelectQuestionRuleCategoryAutomationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "category": "category",
            "condition": "condition",
            "option_ref_id": "optionRefId",
        },
    )
    class SingleSelectQuestionRuleCategoryAutomationProperty:
        def __init__(
            self,
            *,
            category: builtins.str,
            condition: builtins.str,
            option_ref_id: builtins.str,
        ) -> None:
            '''Information about the automation option based on a rule category for a single select question.

            *Length Constraints* : Minimum length of 1. Maximum length of 50.

            :param category: The category name, as defined in Rules. *Minimum* : 1 *Maximum* : 50
            :param condition: The condition to apply for the automation option. If the condition is PRESENT, then the option is applied when the contact data includes the category. Similarly, if the condition is NOT_PRESENT, then the option is applied when the contact data does not include the category. *Allowed values* : ``PRESENT`` | ``NOT_PRESENT`` *Maximum* : 50
            :param option_ref_id: The identifier of the answer option. An identifier must be unique within the question. *Length Constraints* : Minimum length of 1. Maximum length of 40.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-singleselectquestionrulecategoryautomation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                single_select_question_rule_category_automation_property = connect.CfnEvaluationForm.SingleSelectQuestionRuleCategoryAutomationProperty(
                    category="category",
                    condition="condition",
                    option_ref_id="optionRefId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4b2bf16cb3e015cee3921d57ba3346d4fc6c93af2e79cdcf6d8dec3a5caee630)
                check_type(argname="argument category", value=category, expected_type=type_hints["category"])
                check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
                check_type(argname="argument option_ref_id", value=option_ref_id, expected_type=type_hints["option_ref_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "category": category,
                "condition": condition,
                "option_ref_id": option_ref_id,
            }

        @builtins.property
        def category(self) -> builtins.str:
            '''The category name, as defined in Rules.

            *Minimum* : 1

            *Maximum* : 50

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-singleselectquestionrulecategoryautomation.html#cfn-connect-evaluationform-singleselectquestionrulecategoryautomation-category
            '''
            result = self._values.get("category")
            assert result is not None, "Required property 'category' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def condition(self) -> builtins.str:
            '''The condition to apply for the automation option.

            If the condition is PRESENT, then the option is applied when the contact data includes the category. Similarly, if the condition is NOT_PRESENT, then the option is applied when the contact data does not include the category.

            *Allowed values* : ``PRESENT`` | ``NOT_PRESENT``

            *Maximum* : 50

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-singleselectquestionrulecategoryautomation.html#cfn-connect-evaluationform-singleselectquestionrulecategoryautomation-condition
            '''
            result = self._values.get("condition")
            assert result is not None, "Required property 'condition' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def option_ref_id(self) -> builtins.str:
            '''The identifier of the answer option. An identifier must be unique within the question.

            *Length Constraints* : Minimum length of 1. Maximum length of 40.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-evaluationform-singleselectquestionrulecategoryautomation.html#cfn-connect-evaluationform-singleselectquestionrulecategoryautomation-optionrefid
            '''
            result = self._values.get("option_ref_id")
            assert result is not None, "Required property 'option_ref_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SingleSelectQuestionRuleCategoryAutomationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnEvaluationFormProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "items": "items",
        "status": "status",
        "title": "title",
        "description": "description",
        "scoring_strategy": "scoringStrategy",
        "tags": "tags",
    },
)
class CfnEvaluationFormProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        items: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluationForm.EvaluationFormBaseItemProperty, typing.Dict[builtins.str, typing.Any]]]]],
        status: builtins.str,
        title: builtins.str,
        description: typing.Optional[builtins.str] = None,
        scoring_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluationForm.ScoringStrategyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEvaluationForm``.

        :param instance_arn: The identifier of the Amazon Connect instance.
        :param items: Items that are part of the evaluation form. The total number of sections and questions must not exceed 100 each. Questions must be contained in a section. *Minimum size* : 1 *Maximum size* : 100
        :param status: The status of the evaluation form. *Allowed values* : ``DRAFT`` | ``ACTIVE`` Default: - "DRAFT"
        :param title: A title of the evaluation form.
        :param description: The description of the evaluation form. *Length Constraints* : Minimum length of 0. Maximum length of 1024.
        :param scoring_strategy: A scoring strategy of the evaluation form.
        :param tags: The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-evaluationform.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            # evaluation_form_section_property_: connect.CfnEvaluationForm.EvaluationFormSectionProperty
            
            cfn_evaluation_form_props = connect.CfnEvaluationFormProps(
                instance_arn="instanceArn",
                items=[connect.CfnEvaluationForm.EvaluationFormBaseItemProperty(
                    section=connect.CfnEvaluationForm.EvaluationFormSectionProperty(
                        ref_id="refId",
                        title="title",
            
                        # the properties below are optional
                        instructions="instructions",
                        items=[connect.CfnEvaluationForm.EvaluationFormItemProperty(
                            question=connect.CfnEvaluationForm.EvaluationFormQuestionProperty(
                                question_type="questionType",
                                ref_id="refId",
                                title="title",
            
                                # the properties below are optional
                                instructions="instructions",
                                not_applicable_enabled=False,
                                question_type_properties=connect.CfnEvaluationForm.EvaluationFormQuestionTypePropertiesProperty(
                                    numeric=connect.CfnEvaluationForm.EvaluationFormNumericQuestionPropertiesProperty(
                                        max_value=123,
                                        min_value=123,
            
                                        # the properties below are optional
                                        automation=connect.CfnEvaluationForm.EvaluationFormNumericQuestionAutomationProperty(
                                            property_value=connect.CfnEvaluationForm.NumericQuestionPropertyValueAutomationProperty(
                                                label="label"
                                            )
                                        ),
                                        options=[connect.CfnEvaluationForm.EvaluationFormNumericQuestionOptionProperty(
                                            max_value=123,
                                            min_value=123,
            
                                            # the properties below are optional
                                            automatic_fail=False,
                                            score=123
                                        )]
                                    ),
                                    single_select=connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionPropertiesProperty(
                                        options=[connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionOptionProperty(
                                            ref_id="refId",
                                            text="text",
            
                                            # the properties below are optional
                                            automatic_fail=False,
                                            score=123
                                        )],
            
                                        # the properties below are optional
                                        automation=connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationProperty(
                                            options=[connect.CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationOptionProperty(
                                                rule_category=connect.CfnEvaluationForm.SingleSelectQuestionRuleCategoryAutomationProperty(
                                                    category="category",
                                                    condition="condition",
                                                    option_ref_id="optionRefId"
                                                )
                                            )],
            
                                            # the properties below are optional
                                            default_option_ref_id="defaultOptionRefId"
                                        ),
                                        display_as="displayAs"
                                    )
                                ),
                                weight=123
                            ),
                            section=evaluation_form_section_property_
                        )],
                        weight=123
                    )
                )],
                status="status",
                title="title",
            
                # the properties below are optional
                description="description",
                scoring_strategy=connect.CfnEvaluationForm.ScoringStrategyProperty(
                    mode="mode",
                    status="status"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b678e993288629444b4e1bc33b4631f7578a458c70203ec6ae7263a8aedc75ad)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument items", value=items, expected_type=type_hints["items"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument scoring_strategy", value=scoring_strategy, expected_type=type_hints["scoring_strategy"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_arn": instance_arn,
            "items": items,
            "status": status,
            "title": title,
        }
        if description is not None:
            self._values["description"] = description
        if scoring_strategy is not None:
            self._values["scoring_strategy"] = scoring_strategy
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The identifier of the Amazon Connect instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-evaluationform.html#cfn-connect-evaluationform-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def items(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEvaluationForm.EvaluationFormBaseItemProperty]]]:
        '''Items that are part of the evaluation form.

        The total number of sections and questions must not exceed 100 each. Questions must be contained in a section.

        *Minimum size* : 1

        *Maximum size* : 100

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-evaluationform.html#cfn-connect-evaluationform-items
        '''
        result = self._values.get("items")
        assert result is not None, "Required property 'items' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEvaluationForm.EvaluationFormBaseItemProperty]]], result)

    @builtins.property
    def status(self) -> builtins.str:
        '''The status of the evaluation form.

        *Allowed values* : ``DRAFT`` | ``ACTIVE``

        :default: - "DRAFT"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-evaluationform.html#cfn-connect-evaluationform-status
        '''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''A title of the evaluation form.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-evaluationform.html#cfn-connect-evaluationform-title
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the evaluation form.

        *Length Constraints* : Minimum length of 0. Maximum length of 1024.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-evaluationform.html#cfn-connect-evaluationform-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scoring_strategy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEvaluationForm.ScoringStrategyProperty]]:
        '''A scoring strategy of the evaluation form.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-evaluationform.html#cfn-connect-evaluationform-scoringstrategy
        '''
        result = self._values.get("scoring_strategy")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEvaluationForm.ScoringStrategyProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        For example, { "tags": {"key1":"value1", "key2":"value2"} }.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-evaluationform.html#cfn-connect-evaluationform-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEvaluationFormProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnHoursOfOperation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnHoursOfOperation",
):
    '''Specifies hours of operation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html
    :cloudformationResource: AWS::Connect::HoursOfOperation
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_hours_of_operation = connect.CfnHoursOfOperation(self, "MyCfnHoursOfOperation",
            config=[connect.CfnHoursOfOperation.HoursOfOperationConfigProperty(
                day="day",
                end_time=connect.CfnHoursOfOperation.HoursOfOperationTimeSliceProperty(
                    hours=123,
                    minutes=123
                ),
                start_time=connect.CfnHoursOfOperation.HoursOfOperationTimeSliceProperty(
                    hours=123,
                    minutes=123
                )
            )],
            instance_arn="instanceArn",
            name="name",
            time_zone="timeZone",
        
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
        id: builtins.str,
        *,
        config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnHoursOfOperation.HoursOfOperationConfigProperty", typing.Dict[builtins.str, typing.Any]]]]],
        instance_arn: builtins.str,
        name: builtins.str,
        time_zone: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param config: Configuration information for the hours of operation.
        :param instance_arn: The Amazon Resource Name (ARN) of the instance.
        :param name: The name for the hours of operation.
        :param time_zone: The time zone for the hours of operation.
        :param description: The description for the hours of operation.
        :param tags: The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da9a7b2f06b8b2d053fcfa26018be9202b48193f9ffb7fc1d9518391cd9b5afe)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnHoursOfOperationProps(
            config=config,
            instance_arn=instance_arn,
            name=name,
            time_zone=time_zone,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1892c64bc10c89577bb1c7c1cbafe5e7256d59298765e4d13fa8bc792aff27cb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e1be399a62772419844397558be775450dd4c2dc740a8864f61b03b483610073)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrHoursOfOperationArn")
    def attr_hours_of_operation_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the hours of operation.

        :cloudformationAttribute: HoursOfOperationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHoursOfOperationArn"))

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
    @jsii.member(jsii_name="config")
    def config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnHoursOfOperation.HoursOfOperationConfigProperty"]]]:
        '''Configuration information for the hours of operation.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnHoursOfOperation.HoursOfOperationConfigProperty"]]], jsii.get(self, "config"))

    @config.setter
    def config(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnHoursOfOperation.HoursOfOperationConfigProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__390986701d928ed3f41379b144a434426999d52505eaf487d066a0865f299c42)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "config", value)

    @builtins.property
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff371c180e62831feb4bd92859ad779161086fed20f40c5fcaec70aedbd1d950)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name for the hours of operation.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__314c5f51a2268bd65be9864b4a46c3d2279936b4a2675b16522bc736ba5fb373)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="timeZone")
    def time_zone(self) -> builtins.str:
        '''The time zone for the hours of operation.'''
        return typing.cast(builtins.str, jsii.get(self, "timeZone"))

    @time_zone.setter
    def time_zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__442605da8563582cbafb26c421377e100eaf1791f47f7f84657994d9d7347b8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeZone", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for the hours of operation.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__224611189f5992474af63688324a9a850ba31b7aad01b0eaae5a8fd63f4ea172)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3006704998781ab2276bf2b26481ef171277930dc1c09d1dcf2e54b8cd07b7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnHoursOfOperation.HoursOfOperationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"day": "day", "end_time": "endTime", "start_time": "startTime"},
    )
    class HoursOfOperationConfigProperty:
        def __init__(
            self,
            *,
            day: builtins.str,
            end_time: typing.Union[_IResolvable_da3f097b, typing.Union["CfnHoursOfOperation.HoursOfOperationTimeSliceProperty", typing.Dict[builtins.str, typing.Any]]],
            start_time: typing.Union[_IResolvable_da3f097b, typing.Union["CfnHoursOfOperation.HoursOfOperationTimeSliceProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Contains information about the hours of operation.

            :param day: The day that the hours of operation applies to.
            :param end_time: The end time that your contact center closes.
            :param start_time: The start time that your contact center opens.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                hours_of_operation_config_property = connect.CfnHoursOfOperation.HoursOfOperationConfigProperty(
                    day="day",
                    end_time=connect.CfnHoursOfOperation.HoursOfOperationTimeSliceProperty(
                        hours=123,
                        minutes=123
                    ),
                    start_time=connect.CfnHoursOfOperation.HoursOfOperationTimeSliceProperty(
                        hours=123,
                        minutes=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5ef26f457a53e548698c50361c4e334e5f633638af5ae2b9230dccc5fd5c1dd3)
                check_type(argname="argument day", value=day, expected_type=type_hints["day"])
                check_type(argname="argument end_time", value=end_time, expected_type=type_hints["end_time"])
                check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "day": day,
                "end_time": end_time,
                "start_time": start_time,
            }

        @builtins.property
        def day(self) -> builtins.str:
            '''The day that the hours of operation applies to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationconfig.html#cfn-connect-hoursofoperation-hoursofoperationconfig-day
            '''
            result = self._values.get("day")
            assert result is not None, "Required property 'day' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def end_time(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnHoursOfOperation.HoursOfOperationTimeSliceProperty"]:
            '''The end time that your contact center closes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationconfig.html#cfn-connect-hoursofoperation-hoursofoperationconfig-endtime
            '''
            result = self._values.get("end_time")
            assert result is not None, "Required property 'end_time' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnHoursOfOperation.HoursOfOperationTimeSliceProperty"], result)

        @builtins.property
        def start_time(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnHoursOfOperation.HoursOfOperationTimeSliceProperty"]:
            '''The start time that your contact center opens.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationconfig.html#cfn-connect-hoursofoperation-hoursofoperationconfig-starttime
            '''
            result = self._values.get("start_time")
            assert result is not None, "Required property 'start_time' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnHoursOfOperation.HoursOfOperationTimeSliceProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HoursOfOperationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnHoursOfOperation.HoursOfOperationTimeSliceProperty",
        jsii_struct_bases=[],
        name_mapping={"hours": "hours", "minutes": "minutes"},
    )
    class HoursOfOperationTimeSliceProperty:
        def __init__(self, *, hours: jsii.Number, minutes: jsii.Number) -> None:
            '''The start time or end time for an hours of operation.

            :param hours: The hours.
            :param minutes: The minutes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationtimeslice.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                hours_of_operation_time_slice_property = connect.CfnHoursOfOperation.HoursOfOperationTimeSliceProperty(
                    hours=123,
                    minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ca5c5b128d189787db53fa22c88668d84b3efd31f5b54320dcda0838372db008)
                check_type(argname="argument hours", value=hours, expected_type=type_hints["hours"])
                check_type(argname="argument minutes", value=minutes, expected_type=type_hints["minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "hours": hours,
                "minutes": minutes,
            }

        @builtins.property
        def hours(self) -> jsii.Number:
            '''The hours.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationtimeslice.html#cfn-connect-hoursofoperation-hoursofoperationtimeslice-hours
            '''
            result = self._values.get("hours")
            assert result is not None, "Required property 'hours' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def minutes(self) -> jsii.Number:
            '''The minutes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-hoursofoperation-hoursofoperationtimeslice.html#cfn-connect-hoursofoperation-hoursofoperationtimeslice-minutes
            '''
            result = self._values.get("minutes")
            assert result is not None, "Required property 'minutes' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HoursOfOperationTimeSliceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnHoursOfOperationProps",
    jsii_struct_bases=[],
    name_mapping={
        "config": "config",
        "instance_arn": "instanceArn",
        "name": "name",
        "time_zone": "timeZone",
        "description": "description",
        "tags": "tags",
    },
)
class CfnHoursOfOperationProps:
    def __init__(
        self,
        *,
        config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHoursOfOperation.HoursOfOperationConfigProperty, typing.Dict[builtins.str, typing.Any]]]]],
        instance_arn: builtins.str,
        name: builtins.str,
        time_zone: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnHoursOfOperation``.

        :param config: Configuration information for the hours of operation.
        :param instance_arn: The Amazon Resource Name (ARN) of the instance.
        :param name: The name for the hours of operation.
        :param time_zone: The time zone for the hours of operation.
        :param description: The description for the hours of operation.
        :param tags: The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_hours_of_operation_props = connect.CfnHoursOfOperationProps(
                config=[connect.CfnHoursOfOperation.HoursOfOperationConfigProperty(
                    day="day",
                    end_time=connect.CfnHoursOfOperation.HoursOfOperationTimeSliceProperty(
                        hours=123,
                        minutes=123
                    ),
                    start_time=connect.CfnHoursOfOperation.HoursOfOperationTimeSliceProperty(
                        hours=123,
                        minutes=123
                    )
                )],
                instance_arn="instanceArn",
                name="name",
                time_zone="timeZone",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66cef12b59765322de54d22fe6de568f262a635899fc46cbe6a5f5a97b848467)
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "config": config,
            "instance_arn": instance_arn,
            "name": name,
            "time_zone": time_zone,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnHoursOfOperation.HoursOfOperationConfigProperty]]]:
        '''Configuration information for the hours of operation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-config
        '''
        result = self._values.get("config")
        assert result is not None, "Required property 'config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnHoursOfOperation.HoursOfOperationConfigProperty]]], result)

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name for the hours of operation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def time_zone(self) -> builtins.str:
        '''The time zone for the hours of operation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-timezone
        '''
        result = self._values.get("time_zone")
        assert result is not None, "Required property 'time_zone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for the hours of operation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        For example, { "Tags": {"key1":"value1", "key2":"value2"} }.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-hoursofoperation.html#cfn-connect-hoursofoperation-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHoursOfOperationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnInstance(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnInstance",
):
    '''*This is a preview release for Amazon Connect . It is subject to change.*.

    Initiates an Amazon Connect instance with all the supported channels enabled. It does not attach any storage, such as Amazon Simple Storage Service (Amazon S3) or Amazon Kinesis.

    Amazon Connect enforces a limit on the total number of instances that you can create or delete in 30 days. If you exceed this limit, you will get an error message indicating there has been an excessive number of attempts at creating or deleting instances. You must wait 30 days before you can restart creating and deleting instances in your account.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instance.html
    :cloudformationResource: AWS::Connect::Instance
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_instance = connect.CfnInstance(self, "MyCfnInstance",
            attributes=connect.CfnInstance.AttributesProperty(
                inbound_calls=False,
                outbound_calls=False,
        
                # the properties below are optional
                auto_resolve_best_voices=False,
                contactflow_logs=False,
                contact_lens=False,
                early_media=False,
                use_custom_tts_voices=False
            ),
            identity_management_type="identityManagementType",
        
            # the properties below are optional
            directory_id="directoryId",
            instance_alias="instanceAlias",
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
        attributes: typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstance.AttributesProperty", typing.Dict[builtins.str, typing.Any]]],
        identity_management_type: builtins.str,
        directory_id: typing.Optional[builtins.str] = None,
        instance_alias: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param attributes: A toggle for an individual feature at the instance level.
        :param identity_management_type: The identity management type.
        :param directory_id: The identifier for the directory.
        :param instance_alias: The alias of instance. ``InstanceAlias`` is only required when ``IdentityManagementType`` is ``CONNECT_MANAGED`` or ``SAML`` . ``InstanceAlias`` is not required when ``IdentityManagementType`` is ``EXISTING_DIRECTORY`` .
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f291b6bb708a40e1a35dc95de4a38d5f9d8117683bed082183bd387f4848fef9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnInstanceProps(
            attributes=attributes,
            identity_management_type=identity_management_type,
            directory_id=directory_id,
            instance_alias=instance_alias,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e4dee5bd55d2c2f964814ca3e2747955315fb5bc8f0a80efc7cbad1ed39cbdc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__023c45bbafb1abf38373b2528d8531c6e7048604e4fabca7c6a4684feb4413d6)
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
        '''The Amazon Resource Name (ARN) of the instance.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''When the instance was created.

        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The identifier of the Amazon Connect instance.

        You can find the instanceId in the ARN of the instance.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrInstanceStatus")
    def attr_instance_status(self) -> builtins.str:
        '''The state of the instance.

        :cloudformationAttribute: InstanceStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrInstanceStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceRole")
    def attr_service_role(self) -> builtins.str:
        '''The service role of the instance.

        :cloudformationAttribute: ServiceRole
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceRole"))

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
    @jsii.member(jsii_name="attributes")
    def attributes(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnInstance.AttributesProperty"]:
        '''A toggle for an individual feature at the instance level.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnInstance.AttributesProperty"], jsii.get(self, "attributes"))

    @attributes.setter
    def attributes(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnInstance.AttributesProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15b81c5f62ba93ec0d3e48188cccf781d5861eac87dc5aa4a4038e6d2176145e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributes", value)

    @builtins.property
    @jsii.member(jsii_name="identityManagementType")
    def identity_management_type(self) -> builtins.str:
        '''The identity management type.'''
        return typing.cast(builtins.str, jsii.get(self, "identityManagementType"))

    @identity_management_type.setter
    def identity_management_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1723398c06ebefeb9e3f4e11e08b8929e713cae56a36abf11fae424fa1c0cea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityManagementType", value)

    @builtins.property
    @jsii.member(jsii_name="directoryId")
    def directory_id(self) -> typing.Optional[builtins.str]:
        '''The identifier for the directory.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryId"))

    @directory_id.setter
    def directory_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a002f21d50b37114edc464bd9143a0e1abc1702e5ff455644179b2ac7acbfbdd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryId", value)

    @builtins.property
    @jsii.member(jsii_name="instanceAlias")
    def instance_alias(self) -> typing.Optional[builtins.str]:
        '''The alias of instance.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceAlias"))

    @instance_alias.setter
    def instance_alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__225190f7b3c1545c436fe6b710e05a3a5b7d256f1ece21dcb8ad6ba49cf45c90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceAlias", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e8d8f5cd36a7297cd164f61b17e1e7ad86e005761d780299041506bff9d1f68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnInstance.AttributesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "inbound_calls": "inboundCalls",
            "outbound_calls": "outboundCalls",
            "auto_resolve_best_voices": "autoResolveBestVoices",
            "contactflow_logs": "contactflowLogs",
            "contact_lens": "contactLens",
            "early_media": "earlyMedia",
            "use_custom_tts_voices": "useCustomTtsVoices",
        },
    )
    class AttributesProperty:
        def __init__(
            self,
            *,
            inbound_calls: typing.Union[builtins.bool, _IResolvable_da3f097b],
            outbound_calls: typing.Union[builtins.bool, _IResolvable_da3f097b],
            auto_resolve_best_voices: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            contactflow_logs: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            contact_lens: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            early_media: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            use_custom_tts_voices: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''*This is a preview release for Amazon Connect .

            It is subject to change.*

            :param inbound_calls: Mandatory element which enables inbound calls on new instance.
            :param outbound_calls: Mandatory element which enables outbound calls on new instance.
            :param auto_resolve_best_voices: Boolean flag which enables AUTO_RESOLVE_BEST_VOICES on an instance.
            :param contactflow_logs: Boolean flag which enables CONTACTFLOW_LOGS on an instance.
            :param contact_lens: Boolean flag which enables CONTACT_LENS on an instance.
            :param early_media: Boolean flag which enables EARLY_MEDIA on an instance.
            :param use_custom_tts_voices: Boolean flag which enables USE_CUSTOM_TTS_VOICES on an instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instance-attributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                attributes_property = connect.CfnInstance.AttributesProperty(
                    inbound_calls=False,
                    outbound_calls=False,
                
                    # the properties below are optional
                    auto_resolve_best_voices=False,
                    contactflow_logs=False,
                    contact_lens=False,
                    early_media=False,
                    use_custom_tts_voices=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c40aedafdc4ea4fb2b717cc5c6ef0e2db4eb7490be99c35b78dc90f18526d068)
                check_type(argname="argument inbound_calls", value=inbound_calls, expected_type=type_hints["inbound_calls"])
                check_type(argname="argument outbound_calls", value=outbound_calls, expected_type=type_hints["outbound_calls"])
                check_type(argname="argument auto_resolve_best_voices", value=auto_resolve_best_voices, expected_type=type_hints["auto_resolve_best_voices"])
                check_type(argname="argument contactflow_logs", value=contactflow_logs, expected_type=type_hints["contactflow_logs"])
                check_type(argname="argument contact_lens", value=contact_lens, expected_type=type_hints["contact_lens"])
                check_type(argname="argument early_media", value=early_media, expected_type=type_hints["early_media"])
                check_type(argname="argument use_custom_tts_voices", value=use_custom_tts_voices, expected_type=type_hints["use_custom_tts_voices"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "inbound_calls": inbound_calls,
                "outbound_calls": outbound_calls,
            }
            if auto_resolve_best_voices is not None:
                self._values["auto_resolve_best_voices"] = auto_resolve_best_voices
            if contactflow_logs is not None:
                self._values["contactflow_logs"] = contactflow_logs
            if contact_lens is not None:
                self._values["contact_lens"] = contact_lens
            if early_media is not None:
                self._values["early_media"] = early_media
            if use_custom_tts_voices is not None:
                self._values["use_custom_tts_voices"] = use_custom_tts_voices

        @builtins.property
        def inbound_calls(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Mandatory element which enables inbound calls on new instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instance-attributes.html#cfn-connect-instance-attributes-inboundcalls
            '''
            result = self._values.get("inbound_calls")
            assert result is not None, "Required property 'inbound_calls' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def outbound_calls(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Mandatory element which enables outbound calls on new instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instance-attributes.html#cfn-connect-instance-attributes-outboundcalls
            '''
            result = self._values.get("outbound_calls")
            assert result is not None, "Required property 'outbound_calls' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def auto_resolve_best_voices(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Boolean flag which enables AUTO_RESOLVE_BEST_VOICES on an instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instance-attributes.html#cfn-connect-instance-attributes-autoresolvebestvoices
            '''
            result = self._values.get("auto_resolve_best_voices")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def contactflow_logs(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Boolean flag which enables CONTACTFLOW_LOGS on an instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instance-attributes.html#cfn-connect-instance-attributes-contactflowlogs
            '''
            result = self._values.get("contactflow_logs")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def contact_lens(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Boolean flag which enables CONTACT_LENS on an instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instance-attributes.html#cfn-connect-instance-attributes-contactlens
            '''
            result = self._values.get("contact_lens")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def early_media(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Boolean flag which enables EARLY_MEDIA on an instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instance-attributes.html#cfn-connect-instance-attributes-earlymedia
            '''
            result = self._values.get("early_media")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def use_custom_tts_voices(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Boolean flag which enables USE_CUSTOM_TTS_VOICES on an instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instance-attributes.html#cfn-connect-instance-attributes-usecustomttsvoices
            '''
            result = self._values.get("use_custom_tts_voices")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnInstanceProps",
    jsii_struct_bases=[],
    name_mapping={
        "attributes": "attributes",
        "identity_management_type": "identityManagementType",
        "directory_id": "directoryId",
        "instance_alias": "instanceAlias",
        "tags": "tags",
    },
)
class CfnInstanceProps:
    def __init__(
        self,
        *,
        attributes: typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.AttributesProperty, typing.Dict[builtins.str, typing.Any]]],
        identity_management_type: builtins.str,
        directory_id: typing.Optional[builtins.str] = None,
        instance_alias: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnInstance``.

        :param attributes: A toggle for an individual feature at the instance level.
        :param identity_management_type: The identity management type.
        :param directory_id: The identifier for the directory.
        :param instance_alias: The alias of instance. ``InstanceAlias`` is only required when ``IdentityManagementType`` is ``CONNECT_MANAGED`` or ``SAML`` . ``InstanceAlias`` is not required when ``IdentityManagementType`` is ``EXISTING_DIRECTORY`` .
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instance.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_instance_props = connect.CfnInstanceProps(
                attributes=connect.CfnInstance.AttributesProperty(
                    inbound_calls=False,
                    outbound_calls=False,
            
                    # the properties below are optional
                    auto_resolve_best_voices=False,
                    contactflow_logs=False,
                    contact_lens=False,
                    early_media=False,
                    use_custom_tts_voices=False
                ),
                identity_management_type="identityManagementType",
            
                # the properties below are optional
                directory_id="directoryId",
                instance_alias="instanceAlias",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67fdacfbc8ac4206df45637f43843e90e644b42387d3af9173f714ef095953b4)
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
            check_type(argname="argument identity_management_type", value=identity_management_type, expected_type=type_hints["identity_management_type"])
            check_type(argname="argument directory_id", value=directory_id, expected_type=type_hints["directory_id"])
            check_type(argname="argument instance_alias", value=instance_alias, expected_type=type_hints["instance_alias"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "attributes": attributes,
            "identity_management_type": identity_management_type,
        }
        if directory_id is not None:
            self._values["directory_id"] = directory_id
        if instance_alias is not None:
            self._values["instance_alias"] = instance_alias
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def attributes(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnInstance.AttributesProperty]:
        '''A toggle for an individual feature at the instance level.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instance.html#cfn-connect-instance-attributes
        '''
        result = self._values.get("attributes")
        assert result is not None, "Required property 'attributes' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnInstance.AttributesProperty], result)

    @builtins.property
    def identity_management_type(self) -> builtins.str:
        '''The identity management type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instance.html#cfn-connect-instance-identitymanagementtype
        '''
        result = self._values.get("identity_management_type")
        assert result is not None, "Required property 'identity_management_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def directory_id(self) -> typing.Optional[builtins.str]:
        '''The identifier for the directory.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instance.html#cfn-connect-instance-directoryid
        '''
        result = self._values.get("directory_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_alias(self) -> typing.Optional[builtins.str]:
        '''The alias of instance.

        ``InstanceAlias`` is only required when ``IdentityManagementType`` is ``CONNECT_MANAGED`` or ``SAML`` . ``InstanceAlias`` is not required when ``IdentityManagementType`` is ``EXISTING_DIRECTORY`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instance.html#cfn-connect-instance-instancealias
        '''
        result = self._values.get("instance_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instance.html#cfn-connect-instance-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnInstanceStorageConfig(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnInstanceStorageConfig",
):
    '''The storage configuration for the instance.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instancestorageconfig.html
    :cloudformationResource: AWS::Connect::InstanceStorageConfig
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_instance_storage_config = connect.CfnInstanceStorageConfig(self, "MyCfnInstanceStorageConfig",
            instance_arn="instanceArn",
            resource_type="resourceType",
            storage_type="storageType",
        
            # the properties below are optional
            kinesis_firehose_config=connect.CfnInstanceStorageConfig.KinesisFirehoseConfigProperty(
                firehose_arn="firehoseArn"
            ),
            kinesis_stream_config=connect.CfnInstanceStorageConfig.KinesisStreamConfigProperty(
                stream_arn="streamArn"
            ),
            kinesis_video_stream_config=connect.CfnInstanceStorageConfig.KinesisVideoStreamConfigProperty(
                encryption_config=connect.CfnInstanceStorageConfig.EncryptionConfigProperty(
                    encryption_type="encryptionType",
                    key_id="keyId"
                ),
                prefix="prefix",
                retention_period_hours=123
            ),
            s3_config=connect.CfnInstanceStorageConfig.S3ConfigProperty(
                bucket_name="bucketName",
                bucket_prefix="bucketPrefix",
        
                # the properties below are optional
                encryption_config=connect.CfnInstanceStorageConfig.EncryptionConfigProperty(
                    encryption_type="encryptionType",
                    key_id="keyId"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        instance_arn: builtins.str,
        resource_type: builtins.str,
        storage_type: builtins.str,
        kinesis_firehose_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceStorageConfig.KinesisFirehoseConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        kinesis_stream_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceStorageConfig.KinesisStreamConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        kinesis_video_stream_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceStorageConfig.KinesisVideoStreamConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        s3_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceStorageConfig.S3ConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_arn: The Amazon Resource Name (ARN) of the instance.
        :param resource_type: A valid resource type. Following are the valid resource types: ``CHAT_TRANSCRIPTS`` | ``CALL_RECORDINGS`` | ``SCHEDULED_REPORTS`` | ``MEDIA_STREAMS`` | ``CONTACT_TRACE_RECORDS`` | ``AGENT_EVENTS``
        :param storage_type: A valid storage type.
        :param kinesis_firehose_config: The configuration of the Kinesis Firehose delivery stream.
        :param kinesis_stream_config: The configuration of the Kinesis data stream.
        :param kinesis_video_stream_config: The configuration of the Kinesis video stream.
        :param s3_config: The S3 bucket configuration.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30c8e9e3ad538fac1acafd66e46e4e7a4f3893f93a8c6bb42ba1525f14973522)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnInstanceStorageConfigProps(
            instance_arn=instance_arn,
            resource_type=resource_type,
            storage_type=storage_type,
            kinesis_firehose_config=kinesis_firehose_config,
            kinesis_stream_config=kinesis_stream_config,
            kinesis_video_stream_config=kinesis_video_stream_config,
            s3_config=s3_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__047b8a3f497a61ecbf349954496260297e95ce2a4561a42f301589ab2cee4b2a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__64e208c0e80a04bb7be2d96f8d6f17f40b00cfff9d7822b7f4ecb07751859062)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAssociationId")
    def attr_association_id(self) -> builtins.str:
        '''The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.

        :cloudformationAttribute: AssociationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssociationId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb171c6a585c549bf0fad4d15990fc6ee838655cd803c3fd46739aba98a2a1d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''A valid resource type.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @resource_type.setter
    def resource_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ae5f517bee9d34ee21bd11e2d5f0247d46092ae2f3deb37dcf2893b2f798f14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceType", value)

    @builtins.property
    @jsii.member(jsii_name="storageType")
    def storage_type(self) -> builtins.str:
        '''A valid storage type.'''
        return typing.cast(builtins.str, jsii.get(self, "storageType"))

    @storage_type.setter
    def storage_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e576862f1e107b0e3735b4d183525ba16593162db67ddb46e8ca789a1af5850)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageType", value)

    @builtins.property
    @jsii.member(jsii_name="kinesisFirehoseConfig")
    def kinesis_firehose_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceStorageConfig.KinesisFirehoseConfigProperty"]]:
        '''The configuration of the Kinesis Firehose delivery stream.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceStorageConfig.KinesisFirehoseConfigProperty"]], jsii.get(self, "kinesisFirehoseConfig"))

    @kinesis_firehose_config.setter
    def kinesis_firehose_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceStorageConfig.KinesisFirehoseConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0c82cfbbde3b0d4520ea2bf1db2e6d9a0262e0c56473bd9769a65fc32f975a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kinesisFirehoseConfig", value)

    @builtins.property
    @jsii.member(jsii_name="kinesisStreamConfig")
    def kinesis_stream_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceStorageConfig.KinesisStreamConfigProperty"]]:
        '''The configuration of the Kinesis data stream.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceStorageConfig.KinesisStreamConfigProperty"]], jsii.get(self, "kinesisStreamConfig"))

    @kinesis_stream_config.setter
    def kinesis_stream_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceStorageConfig.KinesisStreamConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a364c6eb62a091d24f417f496838aa90b1e63e040b4dad6e12dd8288568f014)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kinesisStreamConfig", value)

    @builtins.property
    @jsii.member(jsii_name="kinesisVideoStreamConfig")
    def kinesis_video_stream_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceStorageConfig.KinesisVideoStreamConfigProperty"]]:
        '''The configuration of the Kinesis video stream.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceStorageConfig.KinesisVideoStreamConfigProperty"]], jsii.get(self, "kinesisVideoStreamConfig"))

    @kinesis_video_stream_config.setter
    def kinesis_video_stream_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceStorageConfig.KinesisVideoStreamConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f43628a93b9adb2e5341b48d5f226f90e92dc0574e63f1fabc8616c9c49b35ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kinesisVideoStreamConfig", value)

    @builtins.property
    @jsii.member(jsii_name="s3Config")
    def s3_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceStorageConfig.S3ConfigProperty"]]:
        '''The S3 bucket configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceStorageConfig.S3ConfigProperty"]], jsii.get(self, "s3Config"))

    @s3_config.setter
    def s3_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceStorageConfig.S3ConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e076b90fc0b5155e89233d8d5afcf24aea56049cea6a67a56da67867dd963c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Config", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnInstanceStorageConfig.EncryptionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"encryption_type": "encryptionType", "key_id": "keyId"},
    )
    class EncryptionConfigProperty:
        def __init__(
            self,
            *,
            encryption_type: builtins.str,
            key_id: builtins.str,
        ) -> None:
            '''The encryption configuration.

            :param encryption_type: The type of encryption.
            :param key_id: The full ARN of the encryption key. .. epigraph:: Be sure to provide the full ARN of the encryption key, not just the ID. Amazon Connect supports only KMS keys with the default key spec of ```SYMMETRIC_DEFAULT`` <https://docs.aws.amazon.com/kms/latest/developerguide/asymmetric-key-specs.html#key-spec-symmetric-default>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-encryptionconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                encryption_config_property = connect.CfnInstanceStorageConfig.EncryptionConfigProperty(
                    encryption_type="encryptionType",
                    key_id="keyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fc46269845c7184ad0679658c798d342839ec1fbf50541709790ef0d801dd540)
                check_type(argname="argument encryption_type", value=encryption_type, expected_type=type_hints["encryption_type"])
                check_type(argname="argument key_id", value=key_id, expected_type=type_hints["key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encryption_type": encryption_type,
                "key_id": key_id,
            }

        @builtins.property
        def encryption_type(self) -> builtins.str:
            '''The type of encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-encryptionconfig.html#cfn-connect-instancestorageconfig-encryptionconfig-encryptiontype
            '''
            result = self._values.get("encryption_type")
            assert result is not None, "Required property 'encryption_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_id(self) -> builtins.str:
            '''The full ARN of the encryption key.

            .. epigraph::

               Be sure to provide the full ARN of the encryption key, not just the ID.

               Amazon Connect supports only KMS keys with the default key spec of ```SYMMETRIC_DEFAULT`` <https://docs.aws.amazon.com/kms/latest/developerguide/asymmetric-key-specs.html#key-spec-symmetric-default>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-encryptionconfig.html#cfn-connect-instancestorageconfig-encryptionconfig-keyid
            '''
            result = self._values.get("key_id")
            assert result is not None, "Required property 'key_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnInstanceStorageConfig.KinesisFirehoseConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"firehose_arn": "firehoseArn"},
    )
    class KinesisFirehoseConfigProperty:
        def __init__(self, *, firehose_arn: builtins.str) -> None:
            '''Configuration information of a Kinesis Data Firehose delivery stream.

            :param firehose_arn: The Amazon Resource Name (ARN) of the delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisfirehoseconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                kinesis_firehose_config_property = connect.CfnInstanceStorageConfig.KinesisFirehoseConfigProperty(
                    firehose_arn="firehoseArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a572a34b9441880677e439712bb7b9dbc0a79fc55daf5839857f2041774e7c99)
                check_type(argname="argument firehose_arn", value=firehose_arn, expected_type=type_hints["firehose_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "firehose_arn": firehose_arn,
            }

        @builtins.property
        def firehose_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisfirehoseconfig.html#cfn-connect-instancestorageconfig-kinesisfirehoseconfig-firehosearn
            '''
            result = self._values.get("firehose_arn")
            assert result is not None, "Required property 'firehose_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisFirehoseConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnInstanceStorageConfig.KinesisStreamConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"stream_arn": "streamArn"},
    )
    class KinesisStreamConfigProperty:
        def __init__(self, *, stream_arn: builtins.str) -> None:
            '''Configuration information of a Kinesis data stream.

            :param stream_arn: The Amazon Resource Name (ARN) of the data stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisstreamconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                kinesis_stream_config_property = connect.CfnInstanceStorageConfig.KinesisStreamConfigProperty(
                    stream_arn="streamArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__198e237e2c62ec06cc78609686ceeb43aaecd21ba79e09b267cdd8be2c3743a1)
                check_type(argname="argument stream_arn", value=stream_arn, expected_type=type_hints["stream_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "stream_arn": stream_arn,
            }

        @builtins.property
        def stream_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the data stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisstreamconfig.html#cfn-connect-instancestorageconfig-kinesisstreamconfig-streamarn
            '''
            result = self._values.get("stream_arn")
            assert result is not None, "Required property 'stream_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisStreamConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnInstanceStorageConfig.KinesisVideoStreamConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption_config": "encryptionConfig",
            "prefix": "prefix",
            "retention_period_hours": "retentionPeriodHours",
        },
    )
    class KinesisVideoStreamConfigProperty:
        def __init__(
            self,
            *,
            encryption_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceStorageConfig.EncryptionConfigProperty", typing.Dict[builtins.str, typing.Any]]],
            prefix: builtins.str,
            retention_period_hours: jsii.Number,
        ) -> None:
            '''Configuration information of a Kinesis video stream.

            :param encryption_config: The encryption configuration.
            :param prefix: The prefix of the video stream.
            :param retention_period_hours: The number of hours data is retained in the stream. Kinesis Video Streams retains the data in a data store that is associated with the stream. The default value is 0, indicating that the stream does not persist data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisvideostreamconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                kinesis_video_stream_config_property = connect.CfnInstanceStorageConfig.KinesisVideoStreamConfigProperty(
                    encryption_config=connect.CfnInstanceStorageConfig.EncryptionConfigProperty(
                        encryption_type="encryptionType",
                        key_id="keyId"
                    ),
                    prefix="prefix",
                    retention_period_hours=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__52c9485c197abc64e1dbe93a9ffbdf11fda8b3df13bc67381180643da843a5b8)
                check_type(argname="argument encryption_config", value=encryption_config, expected_type=type_hints["encryption_config"])
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
                check_type(argname="argument retention_period_hours", value=retention_period_hours, expected_type=type_hints["retention_period_hours"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encryption_config": encryption_config,
                "prefix": prefix,
                "retention_period_hours": retention_period_hours,
            }

        @builtins.property
        def encryption_config(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnInstanceStorageConfig.EncryptionConfigProperty"]:
            '''The encryption configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisvideostreamconfig.html#cfn-connect-instancestorageconfig-kinesisvideostreamconfig-encryptionconfig
            '''
            result = self._values.get("encryption_config")
            assert result is not None, "Required property 'encryption_config' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnInstanceStorageConfig.EncryptionConfigProperty"], result)

        @builtins.property
        def prefix(self) -> builtins.str:
            '''The prefix of the video stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisvideostreamconfig.html#cfn-connect-instancestorageconfig-kinesisvideostreamconfig-prefix
            '''
            result = self._values.get("prefix")
            assert result is not None, "Required property 'prefix' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def retention_period_hours(self) -> jsii.Number:
            '''The number of hours data is retained in the stream.

            Kinesis Video Streams retains the data in a data store that is associated with the stream.

            The default value is 0, indicating that the stream does not persist data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-kinesisvideostreamconfig.html#cfn-connect-instancestorageconfig-kinesisvideostreamconfig-retentionperiodhours
            '''
            result = self._values.get("retention_period_hours")
            assert result is not None, "Required property 'retention_period_hours' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisVideoStreamConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnInstanceStorageConfig.S3ConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_name": "bucketName",
            "bucket_prefix": "bucketPrefix",
            "encryption_config": "encryptionConfig",
        },
    )
    class S3ConfigProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            bucket_prefix: builtins.str,
            encryption_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceStorageConfig.EncryptionConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Information about the Amazon Simple Storage Service (Amazon S3) storage type.

            :param bucket_name: The S3 bucket name.
            :param bucket_prefix: The S3 bucket prefix.
            :param encryption_config: The Amazon S3 encryption configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-s3config.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                s3_config_property = connect.CfnInstanceStorageConfig.S3ConfigProperty(
                    bucket_name="bucketName",
                    bucket_prefix="bucketPrefix",
                
                    # the properties below are optional
                    encryption_config=connect.CfnInstanceStorageConfig.EncryptionConfigProperty(
                        encryption_type="encryptionType",
                        key_id="keyId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7296a98085d62b3fe09acddef52fca10fedbaae666bc4512bfa543fd1ddcccab)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
                check_type(argname="argument encryption_config", value=encryption_config, expected_type=type_hints["encryption_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
                "bucket_prefix": bucket_prefix,
            }
            if encryption_config is not None:
                self._values["encryption_config"] = encryption_config

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''The S3 bucket name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-s3config.html#cfn-connect-instancestorageconfig-s3config-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bucket_prefix(self) -> builtins.str:
            '''The S3 bucket prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-s3config.html#cfn-connect-instancestorageconfig-s3config-bucketprefix
            '''
            result = self._values.get("bucket_prefix")
            assert result is not None, "Required property 'bucket_prefix' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def encryption_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceStorageConfig.EncryptionConfigProperty"]]:
            '''The Amazon S3 encryption configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-instancestorageconfig-s3config.html#cfn-connect-instancestorageconfig-s3config-encryptionconfig
            '''
            result = self._values.get("encryption_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceStorageConfig.EncryptionConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3ConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnInstanceStorageConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "resource_type": "resourceType",
        "storage_type": "storageType",
        "kinesis_firehose_config": "kinesisFirehoseConfig",
        "kinesis_stream_config": "kinesisStreamConfig",
        "kinesis_video_stream_config": "kinesisVideoStreamConfig",
        "s3_config": "s3Config",
    },
)
class CfnInstanceStorageConfigProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        resource_type: builtins.str,
        storage_type: builtins.str,
        kinesis_firehose_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceStorageConfig.KinesisFirehoseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        kinesis_stream_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceStorageConfig.KinesisStreamConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        kinesis_video_stream_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceStorageConfig.KinesisVideoStreamConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        s3_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceStorageConfig.S3ConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnInstanceStorageConfig``.

        :param instance_arn: The Amazon Resource Name (ARN) of the instance.
        :param resource_type: A valid resource type. Following are the valid resource types: ``CHAT_TRANSCRIPTS`` | ``CALL_RECORDINGS`` | ``SCHEDULED_REPORTS`` | ``MEDIA_STREAMS`` | ``CONTACT_TRACE_RECORDS`` | ``AGENT_EVENTS``
        :param storage_type: A valid storage type.
        :param kinesis_firehose_config: The configuration of the Kinesis Firehose delivery stream.
        :param kinesis_stream_config: The configuration of the Kinesis data stream.
        :param kinesis_video_stream_config: The configuration of the Kinesis video stream.
        :param s3_config: The S3 bucket configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instancestorageconfig.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_instance_storage_config_props = connect.CfnInstanceStorageConfigProps(
                instance_arn="instanceArn",
                resource_type="resourceType",
                storage_type="storageType",
            
                # the properties below are optional
                kinesis_firehose_config=connect.CfnInstanceStorageConfig.KinesisFirehoseConfigProperty(
                    firehose_arn="firehoseArn"
                ),
                kinesis_stream_config=connect.CfnInstanceStorageConfig.KinesisStreamConfigProperty(
                    stream_arn="streamArn"
                ),
                kinesis_video_stream_config=connect.CfnInstanceStorageConfig.KinesisVideoStreamConfigProperty(
                    encryption_config=connect.CfnInstanceStorageConfig.EncryptionConfigProperty(
                        encryption_type="encryptionType",
                        key_id="keyId"
                    ),
                    prefix="prefix",
                    retention_period_hours=123
                ),
                s3_config=connect.CfnInstanceStorageConfig.S3ConfigProperty(
                    bucket_name="bucketName",
                    bucket_prefix="bucketPrefix",
            
                    # the properties below are optional
                    encryption_config=connect.CfnInstanceStorageConfig.EncryptionConfigProperty(
                        encryption_type="encryptionType",
                        key_id="keyId"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__220fe9c269db6e3bcb651e492fae1b71e17d6b254dfd6b60c71dc0cda259419b)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            check_type(argname="argument storage_type", value=storage_type, expected_type=type_hints["storage_type"])
            check_type(argname="argument kinesis_firehose_config", value=kinesis_firehose_config, expected_type=type_hints["kinesis_firehose_config"])
            check_type(argname="argument kinesis_stream_config", value=kinesis_stream_config, expected_type=type_hints["kinesis_stream_config"])
            check_type(argname="argument kinesis_video_stream_config", value=kinesis_video_stream_config, expected_type=type_hints["kinesis_video_stream_config"])
            check_type(argname="argument s3_config", value=s3_config, expected_type=type_hints["s3_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_arn": instance_arn,
            "resource_type": resource_type,
            "storage_type": storage_type,
        }
        if kinesis_firehose_config is not None:
            self._values["kinesis_firehose_config"] = kinesis_firehose_config
        if kinesis_stream_config is not None:
            self._values["kinesis_stream_config"] = kinesis_stream_config
        if kinesis_video_stream_config is not None:
            self._values["kinesis_video_stream_config"] = kinesis_video_stream_config
        if s3_config is not None:
            self._values["s3_config"] = s3_config

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instancestorageconfig.html#cfn-connect-instancestorageconfig-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_type(self) -> builtins.str:
        '''A valid resource type.

        Following are the valid resource types: ``CHAT_TRANSCRIPTS`` | ``CALL_RECORDINGS`` | ``SCHEDULED_REPORTS`` | ``MEDIA_STREAMS`` | ``CONTACT_TRACE_RECORDS`` | ``AGENT_EVENTS``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instancestorageconfig.html#cfn-connect-instancestorageconfig-resourcetype
        '''
        result = self._values.get("resource_type")
        assert result is not None, "Required property 'resource_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_type(self) -> builtins.str:
        '''A valid storage type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instancestorageconfig.html#cfn-connect-instancestorageconfig-storagetype
        '''
        result = self._values.get("storage_type")
        assert result is not None, "Required property 'storage_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kinesis_firehose_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstanceStorageConfig.KinesisFirehoseConfigProperty]]:
        '''The configuration of the Kinesis Firehose delivery stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instancestorageconfig.html#cfn-connect-instancestorageconfig-kinesisfirehoseconfig
        '''
        result = self._values.get("kinesis_firehose_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstanceStorageConfig.KinesisFirehoseConfigProperty]], result)

    @builtins.property
    def kinesis_stream_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstanceStorageConfig.KinesisStreamConfigProperty]]:
        '''The configuration of the Kinesis data stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instancestorageconfig.html#cfn-connect-instancestorageconfig-kinesisstreamconfig
        '''
        result = self._values.get("kinesis_stream_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstanceStorageConfig.KinesisStreamConfigProperty]], result)

    @builtins.property
    def kinesis_video_stream_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstanceStorageConfig.KinesisVideoStreamConfigProperty]]:
        '''The configuration of the Kinesis video stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instancestorageconfig.html#cfn-connect-instancestorageconfig-kinesisvideostreamconfig
        '''
        result = self._values.get("kinesis_video_stream_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstanceStorageConfig.KinesisVideoStreamConfigProperty]], result)

    @builtins.property
    def s3_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstanceStorageConfig.S3ConfigProperty]]:
        '''The S3 bucket configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-instancestorageconfig.html#cfn-connect-instancestorageconfig-s3config
        '''
        result = self._values.get("s3_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstanceStorageConfig.S3ConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInstanceStorageConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnIntegrationAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnIntegrationAssociation",
):
    '''Specifies the association of an AWS resource such as Lex bot (both v1 and v2) and Lambda function with an Amazon Connect instance.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-integrationassociation.html
    :cloudformationResource: AWS::Connect::IntegrationAssociation
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_integration_association = connect.CfnIntegrationAssociation(self, "MyCfnIntegrationAssociation",
            instance_id="instanceId",
            integration_arn="integrationArn",
            integration_type="integrationType"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        instance_id: builtins.str,
        integration_arn: builtins.str,
        integration_type: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_id: The Amazon Resource Name (ARN) of the instance. *Minimum* : ``1`` *Maximum* : ``100``
        :param integration_arn: ARN of the integration being associated with the instance. *Minimum* : ``1`` *Maximum* : ``140``
        :param integration_type: Specifies the integration type to be associated with the instance. *Allowed Values* : ``LEX_BOT`` | ``LAMBDA_FUNCTION``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0623057688349069456f9eae4995faa9cd189f98024c1f76262706d5734b311e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnIntegrationAssociationProps(
            instance_id=instance_id,
            integration_arn=integration_arn,
            integration_type=integration_type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bb2bfc240169367a312e392a1f57215cf8d8c8079407283c69a1ce7b13f7f09)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c3d2595ec7f89aa2a00d106ed9c54cd5cee3b8f448483b246b960847d1347cd0)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrIntegrationAssociationId")
    def attr_integration_association_id(self) -> builtins.str:
        '''Identifier of the association with an Amazon Connect instance.

        :cloudformationAttribute: IntegrationAssociationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIntegrationAssociationId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7925af3a6409e56b03183e28600488914d5fe9b4e7accd90ff869ac4ba2618e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceId", value)

    @builtins.property
    @jsii.member(jsii_name="integrationArn")
    def integration_arn(self) -> builtins.str:
        '''ARN of the integration being associated with the instance.'''
        return typing.cast(builtins.str, jsii.get(self, "integrationArn"))

    @integration_arn.setter
    def integration_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cc0c68d9b0ec88ff8644cffd658aa26a913dcd92e1fc6ea4af9e71598d78538)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationArn", value)

    @builtins.property
    @jsii.member(jsii_name="integrationType")
    def integration_type(self) -> builtins.str:
        '''Specifies the integration type to be associated with the instance.'''
        return typing.cast(builtins.str, jsii.get(self, "integrationType"))

    @integration_type.setter
    def integration_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__beb9a11163321e5e540a87e2baf965475a45e960cf9aa4a424acc86dcad3feef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationType", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnIntegrationAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_id": "instanceId",
        "integration_arn": "integrationArn",
        "integration_type": "integrationType",
    },
)
class CfnIntegrationAssociationProps:
    def __init__(
        self,
        *,
        instance_id: builtins.str,
        integration_arn: builtins.str,
        integration_type: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnIntegrationAssociation``.

        :param instance_id: The Amazon Resource Name (ARN) of the instance. *Minimum* : ``1`` *Maximum* : ``100``
        :param integration_arn: ARN of the integration being associated with the instance. *Minimum* : ``1`` *Maximum* : ``140``
        :param integration_type: Specifies the integration type to be associated with the instance. *Allowed Values* : ``LEX_BOT`` | ``LAMBDA_FUNCTION``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-integrationassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_integration_association_props = connect.CfnIntegrationAssociationProps(
                instance_id="instanceId",
                integration_arn="integrationArn",
                integration_type="integrationType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe194aedf3230ea702915cbc89ea1228fbcd7507b4352cd6ca6f2c8b3d412d21)
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
            check_type(argname="argument integration_arn", value=integration_arn, expected_type=type_hints["integration_arn"])
            check_type(argname="argument integration_type", value=integration_type, expected_type=type_hints["integration_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_id": instance_id,
            "integration_arn": integration_arn,
            "integration_type": integration_type,
        }

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance.

        *Minimum* : ``1``

        *Maximum* : ``100``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-integrationassociation.html#cfn-connect-integrationassociation-instanceid
        '''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def integration_arn(self) -> builtins.str:
        '''ARN of the integration being associated with the instance.

        *Minimum* : ``1``

        *Maximum* : ``140``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-integrationassociation.html#cfn-connect-integrationassociation-integrationarn
        '''
        result = self._values.get("integration_arn")
        assert result is not None, "Required property 'integration_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def integration_type(self) -> builtins.str:
        '''Specifies the integration type to be associated with the instance.

        *Allowed Values* : ``LEX_BOT`` | ``LAMBDA_FUNCTION``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-integrationassociation.html#cfn-connect-integrationassociation-integrationtype
        '''
        result = self._values.get("integration_type")
        assert result is not None, "Required property 'integration_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIntegrationAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnPhoneNumber(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnPhoneNumber",
):
    '''Claims a phone number to the specified Amazon Connect instance or traffic distribution group.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html
    :cloudformationResource: AWS::Connect::PhoneNumber
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_phone_number = connect.CfnPhoneNumber(self, "MyCfnPhoneNumber",
            target_arn="targetArn",
        
            # the properties below are optional
            country_code="countryCode",
            description="description",
            prefix="prefix",
            source_phone_number_arn="sourcePhoneNumberArn",
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
        target_arn: builtins.str,
        country_code: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        source_phone_number_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param target_arn: The Amazon Resource Name (ARN) for Amazon Connect instances or traffic distribution group that phone numbers are claimed to.
        :param country_code: The ISO country code.
        :param description: The description of the phone number.
        :param prefix: The prefix of the phone number. If provided, it must contain ``+`` as part of the country code. *Pattern* : ``^\\\\+[0-9]{1,15}``
        :param source_phone_number_arn: The claimed phone number ARN that was previously imported from the external service, such as Amazon Pinpoint. If it is from Amazon Pinpoint, it looks like the ARN of the phone number that was imported from Amazon Pinpoint.
        :param tags: The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
        :param type: The type of phone number.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ec70d84fd2bda163d290722acbb6feca633b4ee134732d8b720c0b96701cb7b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPhoneNumberProps(
            target_arn=target_arn,
            country_code=country_code,
            description=description,
            prefix=prefix,
            source_phone_number_arn=source_phone_number_arn,
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
            type_hints = typing.get_type_hints(_typecheckingstub__ccee69f4a06306d444592cd5cf9588d2bb31a952c87c3487ff8ad82fc8c8cf94)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b523ee72d695f2e00f7a42b04d5ef172e9c4c9f850d546d7d54f31058efcbf64)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAddress")
    def attr_address(self) -> builtins.str:
        '''The phone number, in E.164 format.

        :cloudformationAttribute: Address
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAddress"))

    @builtins.property
    @jsii.member(jsii_name="attrPhoneNumberArn")
    def attr_phone_number_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the phone number.

        :cloudformationAttribute: PhoneNumberArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPhoneNumberArn"))

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
    @jsii.member(jsii_name="targetArn")
    def target_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for Amazon Connect instances or traffic distribution group that phone numbers are claimed to.'''
        return typing.cast(builtins.str, jsii.get(self, "targetArn"))

    @target_arn.setter
    def target_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aee914dbb9c13734690f391827e9cd37ca89f521141f3de61e900bfbbd902752)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetArn", value)

    @builtins.property
    @jsii.member(jsii_name="countryCode")
    def country_code(self) -> typing.Optional[builtins.str]:
        '''The ISO country code.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryCode"))

    @country_code.setter
    def country_code(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e8049a6bcb60451cb780647e8cad2360b140018c95db8d6b0e339ed0524e56f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "countryCode", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the phone number.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9949958c848f257cc25ceae67fe2e9cee4b1972f09d90ea4ed667dac758be40e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> typing.Optional[builtins.str]:
        '''The prefix of the phone number.

        If provided, it must contain ``+`` as part of the country code.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__572d2dd079d87f4a7578acddb0bc7dbcca5ec4c2fecd370ff662ac4d429ea5b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="sourcePhoneNumberArn")
    def source_phone_number_arn(self) -> typing.Optional[builtins.str]:
        '''The claimed phone number ARN that was previously imported from the external service, such as Amazon Pinpoint.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourcePhoneNumberArn"))

    @source_phone_number_arn.setter
    def source_phone_number_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__300c4efa19cbb74af0cd0af8daf0ae0f9cc8bdc0b5b372ff32bd5afa5fec8cb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourcePhoneNumberArn", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0910286729f650a764036086fb0fc5a1d117b7068e7085b28b8314456bcd893)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of phone number.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0868299e1426aef01fcea4843c3c28737fa3b7614cce2aa77e978bfa8976f8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnPhoneNumberProps",
    jsii_struct_bases=[],
    name_mapping={
        "target_arn": "targetArn",
        "country_code": "countryCode",
        "description": "description",
        "prefix": "prefix",
        "source_phone_number_arn": "sourcePhoneNumberArn",
        "tags": "tags",
        "type": "type",
    },
)
class CfnPhoneNumberProps:
    def __init__(
        self,
        *,
        target_arn: builtins.str,
        country_code: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        source_phone_number_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnPhoneNumber``.

        :param target_arn: The Amazon Resource Name (ARN) for Amazon Connect instances or traffic distribution group that phone numbers are claimed to.
        :param country_code: The ISO country code.
        :param description: The description of the phone number.
        :param prefix: The prefix of the phone number. If provided, it must contain ``+`` as part of the country code. *Pattern* : ``^\\\\+[0-9]{1,15}``
        :param source_phone_number_arn: The claimed phone number ARN that was previously imported from the external service, such as Amazon Pinpoint. If it is from Amazon Pinpoint, it looks like the ARN of the phone number that was imported from Amazon Pinpoint.
        :param tags: The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
        :param type: The type of phone number.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_phone_number_props = connect.CfnPhoneNumberProps(
                target_arn="targetArn",
            
                # the properties below are optional
                country_code="countryCode",
                description="description",
                prefix="prefix",
                source_phone_number_arn="sourcePhoneNumberArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                type="type"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9b6cbf832a5409fafc1645b1b1a1567ef5e6d173dfed6d56cae08b977fd4b95)
            check_type(argname="argument target_arn", value=target_arn, expected_type=type_hints["target_arn"])
            check_type(argname="argument country_code", value=country_code, expected_type=type_hints["country_code"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument source_phone_number_arn", value=source_phone_number_arn, expected_type=type_hints["source_phone_number_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_arn": target_arn,
        }
        if country_code is not None:
            self._values["country_code"] = country_code
        if description is not None:
            self._values["description"] = description
        if prefix is not None:
            self._values["prefix"] = prefix
        if source_phone_number_arn is not None:
            self._values["source_phone_number_arn"] = source_phone_number_arn
        if tags is not None:
            self._values["tags"] = tags
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def target_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for Amazon Connect instances or traffic distribution group that phone numbers are claimed to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html#cfn-connect-phonenumber-targetarn
        '''
        result = self._values.get("target_arn")
        assert result is not None, "Required property 'target_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def country_code(self) -> typing.Optional[builtins.str]:
        '''The ISO country code.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html#cfn-connect-phonenumber-countrycode
        '''
        result = self._values.get("country_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the phone number.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html#cfn-connect-phonenumber-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''The prefix of the phone number. If provided, it must contain ``+`` as part of the country code.

        *Pattern* : ``^\\\\+[0-9]{1,15}``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html#cfn-connect-phonenumber-prefix
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_phone_number_arn(self) -> typing.Optional[builtins.str]:
        '''The claimed phone number ARN that was previously imported from the external service, such as Amazon Pinpoint.

        If it is from Amazon Pinpoint, it looks like the ARN of the phone number that was imported from Amazon Pinpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html#cfn-connect-phonenumber-sourcephonenumberarn
        '''
        result = self._values.get("source_phone_number_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        For example, { "tags": {"key1":"value1", "key2":"value2"} }.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html#cfn-connect-phonenumber-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of phone number.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-phonenumber.html#cfn-connect-phonenumber-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPhoneNumberProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPredefinedAttribute(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnPredefinedAttribute",
):
    '''Textual or numeric value that describes an attribute.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-predefinedattribute.html
    :cloudformationResource: AWS::Connect::PredefinedAttribute
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_predefined_attribute = connect.CfnPredefinedAttribute(self, "MyCfnPredefinedAttribute",
            instance_arn="instanceArn",
            name="name",
            values=connect.CfnPredefinedAttribute.ValuesProperty(
                string_list=["stringList"]
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        instance_arn: builtins.str,
        name: builtins.str,
        values: typing.Union[_IResolvable_da3f097b, typing.Union["CfnPredefinedAttribute.ValuesProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_arn: The Amazon Resource Name (ARN) of the instance.
        :param name: The name of the predefined attribute.
        :param values: The values of a predefined attribute.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aae8251f3c38f12791d918a121eabea35a0fd76a17fe96a45e59fab899ce5ec7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPredefinedAttributeProps(
            instance_arn=instance_arn, name=name, values=values
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__399a78b10dff53c13a30343d41faca3a437720451fa5b68f2b8d10fbf1f63c2c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d3a759424fc31959ddf27d6e257a5b1b335f7d9b1e4ad4bd7184517c6deb90f0)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedRegion")
    def attr_last_modified_region(self) -> builtins.str:
        '''Last modified region.

        :cloudformationAttribute: LastModifiedRegion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModifiedRegion"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> _IResolvable_da3f097b:
        '''Last modified time.

        :cloudformationAttribute: LastModifiedTime
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrLastModifiedTime"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e72a0435a6a506b8daa0226ab38a3801d43c7ac4e15dd134ff74a68575297e08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the predefined attribute.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__505c1fe18f355a3c8343fc74e29b578ea13ba483aa5951da1f12eba81893b852)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnPredefinedAttribute.ValuesProperty"]:
        '''The values of a predefined attribute.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnPredefinedAttribute.ValuesProperty"], jsii.get(self, "values"))

    @values.setter
    def values(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnPredefinedAttribute.ValuesProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08003c8bd2407db8849ebc9b0c31a79805d1a0f97f0579e4ac977dfa6a2fd356)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnPredefinedAttribute.ValuesProperty",
        jsii_struct_bases=[],
        name_mapping={"string_list": "stringList"},
    )
    class ValuesProperty:
        def __init__(
            self,
            *,
            string_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The values of a predefined attribute.

            :param string_list: Predefined attribute values of type string list.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-predefinedattribute-values.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                values_property = connect.CfnPredefinedAttribute.ValuesProperty(
                    string_list=["stringList"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__209d9d991e492e56e0ff65e3395c0553be43e6389f1d983bccebb7b1e86208f0)
                check_type(argname="argument string_list", value=string_list, expected_type=type_hints["string_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if string_list is not None:
                self._values["string_list"] = string_list

        @builtins.property
        def string_list(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Predefined attribute values of type string list.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-predefinedattribute-values.html#cfn-connect-predefinedattribute-values-stringlist
            '''
            result = self._values.get("string_list")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ValuesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnPredefinedAttributeProps",
    jsii_struct_bases=[],
    name_mapping={"instance_arn": "instanceArn", "name": "name", "values": "values"},
)
class CfnPredefinedAttributeProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        name: builtins.str,
        values: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPredefinedAttribute.ValuesProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnPredefinedAttribute``.

        :param instance_arn: The Amazon Resource Name (ARN) of the instance.
        :param name: The name of the predefined attribute.
        :param values: The values of a predefined attribute.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-predefinedattribute.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_predefined_attribute_props = connect.CfnPredefinedAttributeProps(
                instance_arn="instanceArn",
                name="name",
                values=connect.CfnPredefinedAttribute.ValuesProperty(
                    string_list=["stringList"]
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e67db40db23ebfe580f504576f3022c3cb9338c26c6aa02862725f1ecadacc4d)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_arn": instance_arn,
            "name": name,
            "values": values,
        }

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-predefinedattribute.html#cfn-connect-predefinedattribute-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the predefined attribute.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-predefinedattribute.html#cfn-connect-predefinedattribute-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnPredefinedAttribute.ValuesProperty]:
        '''The values of a predefined attribute.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-predefinedattribute.html#cfn-connect-predefinedattribute-values
        '''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnPredefinedAttribute.ValuesProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPredefinedAttributeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnPrompt(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnPrompt",
):
    '''Creates a prompt for the specified Amazon Connect instance.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-prompt.html
    :cloudformationResource: AWS::Connect::Prompt
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_prompt = connect.CfnPrompt(self, "MyCfnPrompt",
            instance_arn="instanceArn",
            name="name",
        
            # the properties below are optional
            description="description",
            s3_uri="s3Uri",
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
        instance_arn: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        s3_uri: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_arn: The identifier of the Amazon Connect instance.
        :param name: The name of the prompt.
        :param description: The description of the prompt.
        :param s3_uri: The URI for the S3 bucket where the prompt is stored. This property is required when you create a prompt.
        :param tags: The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__683007bdfb211b27a1db29f576ae38fe5ce650e538e8600382be8cd908344f85)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPromptProps(
            instance_arn=instance_arn,
            name=name,
            description=description,
            s3_uri=s3_uri,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__082bb671ea7d466d02fa1596c6cdcfaf4437ac98f010da0ad9653442f009294a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d29b20ca0171050cd3cbd4d3f240f943d1113931a9994c764036f857a492c5a0)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrPromptArn")
    def attr_prompt_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the prompt.

        :cloudformationAttribute: PromptArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPromptArn"))

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
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The identifier of the Amazon Connect instance.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e57a8b746d04374a6f0e38aaadf23a714511218b7101e02e1c4bbbbc1b114343)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the prompt.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d4bf73898e39f9d3f8ceed6fed7eb213a1a0832a0548e822d8d7b1852b52d00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the prompt.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39c216e96fc64af4ced4806125e9bb517bf8afb21c9527d9140168a800149593)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="s3Uri")
    def s3_uri(self) -> typing.Optional[builtins.str]:
        '''The URI for the S3 bucket where the prompt is stored.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3Uri"))

    @s3_uri.setter
    def s3_uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__155bb4a41abbed9be485f4a84dd2dff42cbadb5390d2f8e657348892f5e2ec15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Uri", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b88b3999e96c364888f1b8a2f9495a78cd1b725cf709724ac78279658d35ced)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnPromptProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "name": "name",
        "description": "description",
        "s3_uri": "s3Uri",
        "tags": "tags",
    },
)
class CfnPromptProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        s3_uri: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPrompt``.

        :param instance_arn: The identifier of the Amazon Connect instance.
        :param name: The name of the prompt.
        :param description: The description of the prompt.
        :param s3_uri: The URI for the S3 bucket where the prompt is stored. This property is required when you create a prompt.
        :param tags: The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-prompt.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_prompt_props = connect.CfnPromptProps(
                instance_arn="instanceArn",
                name="name",
            
                # the properties below are optional
                description="description",
                s3_uri="s3Uri",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de9fba0f83321ee92a8e37f03749f2012ea66a3d9d17e7a5b3d12208f718130d)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument s3_uri", value=s3_uri, expected_type=type_hints["s3_uri"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_arn": instance_arn,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if s3_uri is not None:
            self._values["s3_uri"] = s3_uri
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The identifier of the Amazon Connect instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-prompt.html#cfn-connect-prompt-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the prompt.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-prompt.html#cfn-connect-prompt-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the prompt.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-prompt.html#cfn-connect-prompt-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_uri(self) -> typing.Optional[builtins.str]:
        '''The URI for the S3 bucket where the prompt is stored.

        This property is required when you create a prompt.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-prompt.html#cfn-connect-prompt-s3uri
        '''
        result = self._values.get("s3_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        For example, { "tags": {"key1":"value1", "key2":"value2"} }.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-prompt.html#cfn-connect-prompt-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPromptProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnQueue(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnQueue",
):
    '''Contains information about a queue.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-queue.html
    :cloudformationResource: AWS::Connect::Queue
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_queue = connect.CfnQueue(self, "MyCfnQueue",
            hours_of_operation_arn="hoursOfOperationArn",
            instance_arn="instanceArn",
            name="name",
        
            # the properties below are optional
            description="description",
            max_contacts=123,
            outbound_caller_config=connect.CfnQueue.OutboundCallerConfigProperty(
                outbound_caller_id_name="outboundCallerIdName",
                outbound_caller_id_number_arn="outboundCallerIdNumberArn",
                outbound_flow_arn="outboundFlowArn"
            ),
            quick_connect_arns=["quickConnectArns"],
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
        hours_of_operation_arn: builtins.str,
        instance_arn: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        max_contacts: typing.Optional[jsii.Number] = None,
        outbound_caller_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnQueue.OutboundCallerConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        quick_connect_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param hours_of_operation_arn: The Amazon Resource Name (ARN) of the hours of operation.
        :param instance_arn: The identifier of the Amazon Connect instance.
        :param name: The name of the queue.
        :param description: The description of the queue.
        :param max_contacts: The maximum number of contacts that can be in the queue before it is considered full.
        :param outbound_caller_config: The outbound caller ID name, number, and outbound whisper flow.
        :param quick_connect_arns: The Amazon Resource Names (ARN) of the of the quick connects available to agents who are working the queue.
        :param status: The status of the queue.
        :param tags: The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__305bba43cd31a2f9d719dec6a726b64cb46f6b33b3b631880aa85047c7056f75)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnQueueProps(
            hours_of_operation_arn=hours_of_operation_arn,
            instance_arn=instance_arn,
            name=name,
            description=description,
            max_contacts=max_contacts,
            outbound_caller_config=outbound_caller_config,
            quick_connect_arns=quick_connect_arns,
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
            type_hints = typing.get_type_hints(_typecheckingstub__f93be61e7812e4853e82b359f9f56dddced567e8b8bd359c20e0fd75ddeb08ba)
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
            type_hints = typing.get_type_hints(_typecheckingstub__810d3f06ac22f06b625c2807da1ff7874cd5dbdf46e30800ef339329bb22f755)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrQueueArn")
    def attr_queue_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the queue.

        :cloudformationAttribute: QueueArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrQueueArn"))

    @builtins.property
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''The type of queue.

        :cloudformationAttribute: Type
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

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
    @jsii.member(jsii_name="hoursOfOperationArn")
    def hours_of_operation_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the hours of operation.'''
        return typing.cast(builtins.str, jsii.get(self, "hoursOfOperationArn"))

    @hours_of_operation_arn.setter
    def hours_of_operation_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7d30f6e0e4ce3aa26db7bed186df9948879475e9d65d78ad7d2b1b1561e43bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hoursOfOperationArn", value)

    @builtins.property
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The identifier of the Amazon Connect instance.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b2cc069db010e8833f184babb5c99b72c3a0167b7f941763fde2016f183c90f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the queue.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27bc5019f6be77ed53ba7b862aca0ea738158dec243027976b99cd8fd7d156cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the queue.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01334cc773db27a1a528393f9dae2d25072dea3e9175e44003dc6d7b729dc1ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="maxContacts")
    def max_contacts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of contacts that can be in the queue before it is considered full.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxContacts"))

    @max_contacts.setter
    def max_contacts(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ef18f4767eb9b75cc12f1f22292b0dac9bb3c25561c4f2dc0a503d0bda1b02b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxContacts", value)

    @builtins.property
    @jsii.member(jsii_name="outboundCallerConfig")
    def outbound_caller_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQueue.OutboundCallerConfigProperty"]]:
        '''The outbound caller ID name, number, and outbound whisper flow.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQueue.OutboundCallerConfigProperty"]], jsii.get(self, "outboundCallerConfig"))

    @outbound_caller_config.setter
    def outbound_caller_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQueue.OutboundCallerConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efe056b6b273a9bf8a7269bd77e79f2001945bafc023aed9da6eba0851a70a6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outboundCallerConfig", value)

    @builtins.property
    @jsii.member(jsii_name="quickConnectArns")
    def quick_connect_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon Resource Names (ARN) of the of the quick connects available to agents who are working the queue.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "quickConnectArns"))

    @quick_connect_arns.setter
    def quick_connect_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__028ca5a74d47f38a105a56baa46c7e52d7fe78d25b30fceb95452700dd3fddaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "quickConnectArns", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the queue.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cda75a5d23f16160f73ce61f8cebb27b0821ddfea0cc766b3fb59137ce1d3f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4404046d9df0429c6f43ab2ee542dc80ea4102b8e0802875f2dc57d2dd561b4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnQueue.OutboundCallerConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "outbound_caller_id_name": "outboundCallerIdName",
            "outbound_caller_id_number_arn": "outboundCallerIdNumberArn",
            "outbound_flow_arn": "outboundFlowArn",
        },
    )
    class OutboundCallerConfigProperty:
        def __init__(
            self,
            *,
            outbound_caller_id_name: typing.Optional[builtins.str] = None,
            outbound_caller_id_number_arn: typing.Optional[builtins.str] = None,
            outbound_flow_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The outbound caller ID name, number, and outbound whisper flow.

            :param outbound_caller_id_name: The caller ID name.
            :param outbound_caller_id_number_arn: The Amazon Resource Name (ARN) of the outbound caller ID number. .. epigraph:: Only use the phone number ARN format that doesn't contain ``instance`` in the path, for example, ``arn:aws:connect:us-east-1:1234567890:phone-number/uuid`` . This is the same ARN format that is returned when you create a phone number using CloudFormation , or when you call the `ListPhoneNumbersV2 <https://docs.aws.amazon.com/connect/latest/APIReference/API_ListPhoneNumbersV2.html>`_ API.
            :param outbound_flow_arn: The Amazon Resource Name (ARN) of the outbound flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-queue-outboundcallerconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                outbound_caller_config_property = connect.CfnQueue.OutboundCallerConfigProperty(
                    outbound_caller_id_name="outboundCallerIdName",
                    outbound_caller_id_number_arn="outboundCallerIdNumberArn",
                    outbound_flow_arn="outboundFlowArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d2f8c0fdd30542f9e64ba3ad4c32832636467651ad5236b756c53590ecabed33)
                check_type(argname="argument outbound_caller_id_name", value=outbound_caller_id_name, expected_type=type_hints["outbound_caller_id_name"])
                check_type(argname="argument outbound_caller_id_number_arn", value=outbound_caller_id_number_arn, expected_type=type_hints["outbound_caller_id_number_arn"])
                check_type(argname="argument outbound_flow_arn", value=outbound_flow_arn, expected_type=type_hints["outbound_flow_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if outbound_caller_id_name is not None:
                self._values["outbound_caller_id_name"] = outbound_caller_id_name
            if outbound_caller_id_number_arn is not None:
                self._values["outbound_caller_id_number_arn"] = outbound_caller_id_number_arn
            if outbound_flow_arn is not None:
                self._values["outbound_flow_arn"] = outbound_flow_arn

        @builtins.property
        def outbound_caller_id_name(self) -> typing.Optional[builtins.str]:
            '''The caller ID name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-queue-outboundcallerconfig.html#cfn-connect-queue-outboundcallerconfig-outboundcalleridname
            '''
            result = self._values.get("outbound_caller_id_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def outbound_caller_id_number_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the outbound caller ID number.

            .. epigraph::

               Only use the phone number ARN format that doesn't contain ``instance`` in the path, for example, ``arn:aws:connect:us-east-1:1234567890:phone-number/uuid`` . This is the same ARN format that is returned when you create a phone number using CloudFormation , or when you call the `ListPhoneNumbersV2 <https://docs.aws.amazon.com/connect/latest/APIReference/API_ListPhoneNumbersV2.html>`_ API.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-queue-outboundcallerconfig.html#cfn-connect-queue-outboundcallerconfig-outboundcalleridnumberarn
            '''
            result = self._values.get("outbound_caller_id_number_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def outbound_flow_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the outbound flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-queue-outboundcallerconfig.html#cfn-connect-queue-outboundcallerconfig-outboundflowarn
            '''
            result = self._values.get("outbound_flow_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutboundCallerConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnQueueProps",
    jsii_struct_bases=[],
    name_mapping={
        "hours_of_operation_arn": "hoursOfOperationArn",
        "instance_arn": "instanceArn",
        "name": "name",
        "description": "description",
        "max_contacts": "maxContacts",
        "outbound_caller_config": "outboundCallerConfig",
        "quick_connect_arns": "quickConnectArns",
        "status": "status",
        "tags": "tags",
    },
)
class CfnQueueProps:
    def __init__(
        self,
        *,
        hours_of_operation_arn: builtins.str,
        instance_arn: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        max_contacts: typing.Optional[jsii.Number] = None,
        outbound_caller_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnQueue.OutboundCallerConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        quick_connect_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnQueue``.

        :param hours_of_operation_arn: The Amazon Resource Name (ARN) of the hours of operation.
        :param instance_arn: The identifier of the Amazon Connect instance.
        :param name: The name of the queue.
        :param description: The description of the queue.
        :param max_contacts: The maximum number of contacts that can be in the queue before it is considered full.
        :param outbound_caller_config: The outbound caller ID name, number, and outbound whisper flow.
        :param quick_connect_arns: The Amazon Resource Names (ARN) of the of the quick connects available to agents who are working the queue.
        :param status: The status of the queue.
        :param tags: The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-queue.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_queue_props = connect.CfnQueueProps(
                hours_of_operation_arn="hoursOfOperationArn",
                instance_arn="instanceArn",
                name="name",
            
                # the properties below are optional
                description="description",
                max_contacts=123,
                outbound_caller_config=connect.CfnQueue.OutboundCallerConfigProperty(
                    outbound_caller_id_name="outboundCallerIdName",
                    outbound_caller_id_number_arn="outboundCallerIdNumberArn",
                    outbound_flow_arn="outboundFlowArn"
                ),
                quick_connect_arns=["quickConnectArns"],
                status="status",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baa26a31f9cdaa2c1ff32bcd44e00a08477582db0c01e27c9e1a60c3e96a8bce)
            check_type(argname="argument hours_of_operation_arn", value=hours_of_operation_arn, expected_type=type_hints["hours_of_operation_arn"])
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument max_contacts", value=max_contacts, expected_type=type_hints["max_contacts"])
            check_type(argname="argument outbound_caller_config", value=outbound_caller_config, expected_type=type_hints["outbound_caller_config"])
            check_type(argname="argument quick_connect_arns", value=quick_connect_arns, expected_type=type_hints["quick_connect_arns"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hours_of_operation_arn": hours_of_operation_arn,
            "instance_arn": instance_arn,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if max_contacts is not None:
            self._values["max_contacts"] = max_contacts
        if outbound_caller_config is not None:
            self._values["outbound_caller_config"] = outbound_caller_config
        if quick_connect_arns is not None:
            self._values["quick_connect_arns"] = quick_connect_arns
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def hours_of_operation_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the hours of operation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-queue.html#cfn-connect-queue-hoursofoperationarn
        '''
        result = self._values.get("hours_of_operation_arn")
        assert result is not None, "Required property 'hours_of_operation_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The identifier of the Amazon Connect instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-queue.html#cfn-connect-queue-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the queue.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-queue.html#cfn-connect-queue-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the queue.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-queue.html#cfn-connect-queue-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_contacts(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of contacts that can be in the queue before it is considered full.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-queue.html#cfn-connect-queue-maxcontacts
        '''
        result = self._values.get("max_contacts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def outbound_caller_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnQueue.OutboundCallerConfigProperty]]:
        '''The outbound caller ID name, number, and outbound whisper flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-queue.html#cfn-connect-queue-outboundcallerconfig
        '''
        result = self._values.get("outbound_caller_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnQueue.OutboundCallerConfigProperty]], result)

    @builtins.property
    def quick_connect_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon Resource Names (ARN) of the of the quick connects available to agents who are working the queue.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-queue.html#cfn-connect-queue-quickconnectarns
        '''
        result = self._values.get("quick_connect_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the queue.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-queue.html#cfn-connect-queue-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        For example, { "Tags": {"key1":"value1", "key2":"value2"} }.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-queue.html#cfn-connect-queue-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQueueProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnQuickConnect(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnQuickConnect",
):
    '''Specifies a quick connect for an Amazon Connect instance.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html
    :cloudformationResource: AWS::Connect::QuickConnect
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_quick_connect = connect.CfnQuickConnect(self, "MyCfnQuickConnect",
            instance_arn="instanceArn",
            name="name",
            quick_connect_config=connect.CfnQuickConnect.QuickConnectConfigProperty(
                quick_connect_type="quickConnectType",
        
                # the properties below are optional
                phone_config=connect.CfnQuickConnect.PhoneNumberQuickConnectConfigProperty(
                    phone_number="phoneNumber"
                ),
                queue_config=connect.CfnQuickConnect.QueueQuickConnectConfigProperty(
                    contact_flow_arn="contactFlowArn",
                    queue_arn="queueArn"
                ),
                user_config=connect.CfnQuickConnect.UserQuickConnectConfigProperty(
                    contact_flow_arn="contactFlowArn",
                    user_arn="userArn"
                )
            ),
        
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
        id: builtins.str,
        *,
        instance_arn: builtins.str,
        name: builtins.str,
        quick_connect_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnQuickConnect.QuickConnectConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_arn: The Amazon Resource Name (ARN) of the instance.
        :param name: The name of the quick connect.
        :param quick_connect_config: Contains information about the quick connect.
        :param description: The description of the quick connect.
        :param tags: The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44121049328c061f99076678805110a34e47bc31097d43b030f388eca53234e9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnQuickConnectProps(
            instance_arn=instance_arn,
            name=name,
            quick_connect_config=quick_connect_config,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac17b042f7cf408478c49ac00f219efb0ede78bbe556a5ec55b66c5025bf6198)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2a25858c0bb7501da609f58db5989e1c4593c28fa68b47618b9ed5533379f506)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrQuickConnectArn")
    def attr_quick_connect_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the quick connect.

        :cloudformationAttribute: QuickConnectArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrQuickConnectArn"))

    @builtins.property
    @jsii.member(jsii_name="attrQuickConnectType")
    def attr_quick_connect_type(self) -> builtins.str:
        '''The type of quick connect.

        In the Amazon Connect admin website, when you create a quick connect, you are prompted to assign one of the following types: Agent (USER), External (PHONE_NUMBER), or Queue (QUEUE).

        :cloudformationAttribute: QuickConnectType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrQuickConnectType"))

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
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f4d649c9007065ac09a0caa875fd618788a773aab62e76f33a48ae54d5284ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the quick connect.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03d7d088ec5e9e804f349ff7c9f716ab0de501abdb1561144e8cba5e16ae351d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="quickConnectConfig")
    def quick_connect_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnQuickConnect.QuickConnectConfigProperty"]:
        '''Contains information about the quick connect.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnQuickConnect.QuickConnectConfigProperty"], jsii.get(self, "quickConnectConfig"))

    @quick_connect_config.setter
    def quick_connect_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnQuickConnect.QuickConnectConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf95cf02ae05236caa122a481ca15ec758f528b67ca083a27c0d64c2c3c7f4d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "quickConnectConfig", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the quick connect.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f4633c9c2a7464e4f507d168aa19eee91126aef113fdfcb12ab23fe37d443cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d25a4810179e086fcbdd720e6235f81b481124650b66e395c9bc34b2d357fb46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnQuickConnect.PhoneNumberQuickConnectConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"phone_number": "phoneNumber"},
    )
    class PhoneNumberQuickConnectConfigProperty:
        def __init__(self, *, phone_number: builtins.str) -> None:
            '''Contains information about a phone number for a quick connect.

            :param phone_number: The phone number in E.164 format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-phonenumberquickconnectconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                phone_number_quick_connect_config_property = connect.CfnQuickConnect.PhoneNumberQuickConnectConfigProperty(
                    phone_number="phoneNumber"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8c594b9d59e37b885f89d8bea8817c96760d7982a4ec30c3cec4c9d6620f0690)
                check_type(argname="argument phone_number", value=phone_number, expected_type=type_hints["phone_number"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "phone_number": phone_number,
            }

        @builtins.property
        def phone_number(self) -> builtins.str:
            '''The phone number in E.164 format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-phonenumberquickconnectconfig.html#cfn-connect-quickconnect-phonenumberquickconnectconfig-phonenumber
            '''
            result = self._values.get("phone_number")
            assert result is not None, "Required property 'phone_number' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PhoneNumberQuickConnectConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnQuickConnect.QueueQuickConnectConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"contact_flow_arn": "contactFlowArn", "queue_arn": "queueArn"},
    )
    class QueueQuickConnectConfigProperty:
        def __init__(
            self,
            *,
            contact_flow_arn: builtins.str,
            queue_arn: builtins.str,
        ) -> None:
            '''Contains information about a queue for a quick connect.

            The flow must be of type Transfer to Queue.

            :param contact_flow_arn: The Amazon Resource Name (ARN) of the flow.
            :param queue_arn: The Amazon Resource Name (ARN) of the queue.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-queuequickconnectconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                queue_quick_connect_config_property = connect.CfnQuickConnect.QueueQuickConnectConfigProperty(
                    contact_flow_arn="contactFlowArn",
                    queue_arn="queueArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f7632a33b2bc55f259222d21532508c7c3f8f6ef77e1098e16a144fdb3514616)
                check_type(argname="argument contact_flow_arn", value=contact_flow_arn, expected_type=type_hints["contact_flow_arn"])
                check_type(argname="argument queue_arn", value=queue_arn, expected_type=type_hints["queue_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "contact_flow_arn": contact_flow_arn,
                "queue_arn": queue_arn,
            }

        @builtins.property
        def contact_flow_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-queuequickconnectconfig.html#cfn-connect-quickconnect-queuequickconnectconfig-contactflowarn
            '''
            result = self._values.get("contact_flow_arn")
            assert result is not None, "Required property 'contact_flow_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def queue_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the queue.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-queuequickconnectconfig.html#cfn-connect-quickconnect-queuequickconnectconfig-queuearn
            '''
            result = self._values.get("queue_arn")
            assert result is not None, "Required property 'queue_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QueueQuickConnectConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnQuickConnect.QuickConnectConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "quick_connect_type": "quickConnectType",
            "phone_config": "phoneConfig",
            "queue_config": "queueConfig",
            "user_config": "userConfig",
        },
    )
    class QuickConnectConfigProperty:
        def __init__(
            self,
            *,
            quick_connect_type: builtins.str,
            phone_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnQuickConnect.PhoneNumberQuickConnectConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            queue_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnQuickConnect.QueueQuickConnectConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            user_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnQuickConnect.UserQuickConnectConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains configuration settings for a quick connect.

            :param quick_connect_type: The type of quick connect. In the Amazon Connect console, when you create a quick connect, you are prompted to assign one of the following types: Agent (USER), External (PHONE_NUMBER), or Queue (QUEUE).
            :param phone_config: The phone configuration. This is required only if QuickConnectType is PHONE_NUMBER.
            :param queue_config: The queue configuration. This is required only if QuickConnectType is QUEUE.
            :param user_config: The user configuration. This is required only if QuickConnectType is USER.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                quick_connect_config_property = connect.CfnQuickConnect.QuickConnectConfigProperty(
                    quick_connect_type="quickConnectType",
                
                    # the properties below are optional
                    phone_config=connect.CfnQuickConnect.PhoneNumberQuickConnectConfigProperty(
                        phone_number="phoneNumber"
                    ),
                    queue_config=connect.CfnQuickConnect.QueueQuickConnectConfigProperty(
                        contact_flow_arn="contactFlowArn",
                        queue_arn="queueArn"
                    ),
                    user_config=connect.CfnQuickConnect.UserQuickConnectConfigProperty(
                        contact_flow_arn="contactFlowArn",
                        user_arn="userArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5a5ffbc184bff7cbc8cc0dd5bf20c11b8676ca18d518a33d4b7ae2d76891f05d)
                check_type(argname="argument quick_connect_type", value=quick_connect_type, expected_type=type_hints["quick_connect_type"])
                check_type(argname="argument phone_config", value=phone_config, expected_type=type_hints["phone_config"])
                check_type(argname="argument queue_config", value=queue_config, expected_type=type_hints["queue_config"])
                check_type(argname="argument user_config", value=user_config, expected_type=type_hints["user_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "quick_connect_type": quick_connect_type,
            }
            if phone_config is not None:
                self._values["phone_config"] = phone_config
            if queue_config is not None:
                self._values["queue_config"] = queue_config
            if user_config is not None:
                self._values["user_config"] = user_config

        @builtins.property
        def quick_connect_type(self) -> builtins.str:
            '''The type of quick connect.

            In the Amazon Connect console, when you create a quick connect, you are prompted to assign one of the following types: Agent (USER), External (PHONE_NUMBER), or Queue (QUEUE).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html#cfn-connect-quickconnect-quickconnectconfig-quickconnecttype
            '''
            result = self._values.get("quick_connect_type")
            assert result is not None, "Required property 'quick_connect_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def phone_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQuickConnect.PhoneNumberQuickConnectConfigProperty"]]:
            '''The phone configuration.

            This is required only if QuickConnectType is PHONE_NUMBER.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html#cfn-connect-quickconnect-quickconnectconfig-phoneconfig
            '''
            result = self._values.get("phone_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQuickConnect.PhoneNumberQuickConnectConfigProperty"]], result)

        @builtins.property
        def queue_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQuickConnect.QueueQuickConnectConfigProperty"]]:
            '''The queue configuration.

            This is required only if QuickConnectType is QUEUE.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html#cfn-connect-quickconnect-quickconnectconfig-queueconfig
            '''
            result = self._values.get("queue_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQuickConnect.QueueQuickConnectConfigProperty"]], result)

        @builtins.property
        def user_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQuickConnect.UserQuickConnectConfigProperty"]]:
            '''The user configuration.

            This is required only if QuickConnectType is USER.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-quickconnectconfig.html#cfn-connect-quickconnect-quickconnectconfig-userconfig
            '''
            result = self._values.get("user_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnQuickConnect.UserQuickConnectConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QuickConnectConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnQuickConnect.UserQuickConnectConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"contact_flow_arn": "contactFlowArn", "user_arn": "userArn"},
    )
    class UserQuickConnectConfigProperty:
        def __init__(
            self,
            *,
            contact_flow_arn: builtins.str,
            user_arn: builtins.str,
        ) -> None:
            '''Contains information about the quick connect configuration settings for a user.

            The contact flow must be of type Transfer to Agent.

            :param contact_flow_arn: The Amazon Resource Name (ARN) of the flow.
            :param user_arn: The Amazon Resource Name (ARN) of the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-userquickconnectconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                user_quick_connect_config_property = connect.CfnQuickConnect.UserQuickConnectConfigProperty(
                    contact_flow_arn="contactFlowArn",
                    user_arn="userArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7730396d4c494428f6ddd636283d9d5c17ba3fbc6013f1c545a8788d686e0fc1)
                check_type(argname="argument contact_flow_arn", value=contact_flow_arn, expected_type=type_hints["contact_flow_arn"])
                check_type(argname="argument user_arn", value=user_arn, expected_type=type_hints["user_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "contact_flow_arn": contact_flow_arn,
                "user_arn": user_arn,
            }

        @builtins.property
        def contact_flow_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-userquickconnectconfig.html#cfn-connect-quickconnect-userquickconnectconfig-contactflowarn
            '''
            result = self._values.get("contact_flow_arn")
            assert result is not None, "Required property 'contact_flow_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def user_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-quickconnect-userquickconnectconfig.html#cfn-connect-quickconnect-userquickconnectconfig-userarn
            '''
            result = self._values.get("user_arn")
            assert result is not None, "Required property 'user_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserQuickConnectConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnQuickConnectProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "name": "name",
        "quick_connect_config": "quickConnectConfig",
        "description": "description",
        "tags": "tags",
    },
)
class CfnQuickConnectProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        name: builtins.str,
        quick_connect_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnQuickConnect.QuickConnectConfigProperty, typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnQuickConnect``.

        :param instance_arn: The Amazon Resource Name (ARN) of the instance.
        :param name: The name of the quick connect.
        :param quick_connect_config: Contains information about the quick connect.
        :param description: The description of the quick connect.
        :param tags: The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_quick_connect_props = connect.CfnQuickConnectProps(
                instance_arn="instanceArn",
                name="name",
                quick_connect_config=connect.CfnQuickConnect.QuickConnectConfigProperty(
                    quick_connect_type="quickConnectType",
            
                    # the properties below are optional
                    phone_config=connect.CfnQuickConnect.PhoneNumberQuickConnectConfigProperty(
                        phone_number="phoneNumber"
                    ),
                    queue_config=connect.CfnQuickConnect.QueueQuickConnectConfigProperty(
                        contact_flow_arn="contactFlowArn",
                        queue_arn="queueArn"
                    ),
                    user_config=connect.CfnQuickConnect.UserQuickConnectConfigProperty(
                        contact_flow_arn="contactFlowArn",
                        user_arn="userArn"
                    )
                ),
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d4ffda8775de853a0509cc15bc43b59e37fc8f6d1d2c110c1202c4192841fbd)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument quick_connect_config", value=quick_connect_config, expected_type=type_hints["quick_connect_config"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_arn": instance_arn,
            "name": name,
            "quick_connect_config": quick_connect_config,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the quick connect.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def quick_connect_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnQuickConnect.QuickConnectConfigProperty]:
        '''Contains information about the quick connect.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-quickconnectconfig
        '''
        result = self._values.get("quick_connect_config")
        assert result is not None, "Required property 'quick_connect_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnQuickConnect.QuickConnectConfigProperty], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the quick connect.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        For example, { "Tags": {"key1":"value1", "key2":"value2"} }.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-quickconnect.html#cfn-connect-quickconnect-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnQuickConnectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnRoutingProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnRoutingProfile",
):
    '''Creates a new routing profile.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-routingprofile.html
    :cloudformationResource: AWS::Connect::RoutingProfile
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_routing_profile = connect.CfnRoutingProfile(self, "MyCfnRoutingProfile",
            default_outbound_queue_arn="defaultOutboundQueueArn",
            description="description",
            instance_arn="instanceArn",
            media_concurrencies=[connect.CfnRoutingProfile.MediaConcurrencyProperty(
                channel="channel",
                concurrency=123,
        
                # the properties below are optional
                cross_channel_behavior=connect.CfnRoutingProfile.CrossChannelBehaviorProperty(
                    behavior_type="behaviorType"
                )
            )],
            name="name",
        
            # the properties below are optional
            agent_availability_timer="agentAvailabilityTimer",
            queue_configs=[connect.CfnRoutingProfile.RoutingProfileQueueConfigProperty(
                delay=123,
                priority=123,
                queue_reference=connect.CfnRoutingProfile.RoutingProfileQueueReferenceProperty(
                    channel="channel",
                    queue_arn="queueArn"
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
        default_outbound_queue_arn: builtins.str,
        description: builtins.str,
        instance_arn: builtins.str,
        media_concurrencies: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRoutingProfile.MediaConcurrencyProperty", typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        agent_availability_timer: typing.Optional[builtins.str] = None,
        queue_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRoutingProfile.RoutingProfileQueueConfigProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param default_outbound_queue_arn: The Amazon Resource Name (ARN) of the default outbound queue for the routing profile.
        :param description: The description of the routing profile.
        :param instance_arn: The identifier of the Amazon Connect instance.
        :param media_concurrencies: The channels agents can handle in the Contact Control Panel (CCP) for this routing profile.
        :param name: The name of the routing profile.
        :param agent_availability_timer: Whether agents with this routing profile will have their routing order calculated based on *time since their last inbound contact* or *longest idle time* .
        :param queue_configs: The inbound queues associated with the routing profile. If no queue is added, the agent can make only outbound calls.
        :param tags: The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca1360ef7fc87b491018629ca5fc6a3c13fcbdd97e4a14461038caf03b1040c0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRoutingProfileProps(
            default_outbound_queue_arn=default_outbound_queue_arn,
            description=description,
            instance_arn=instance_arn,
            media_concurrencies=media_concurrencies,
            name=name,
            agent_availability_timer=agent_availability_timer,
            queue_configs=queue_configs,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3c1d126bf93606617799bec9e1085a17ff1901adee1bb2566a46664aeeffd67)
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
            type_hints = typing.get_type_hints(_typecheckingstub__77b9ba58a5ab39723e5daa4d5e1269a1daa90368ec1224849b55a6cf80a38104)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrRoutingProfileArn")
    def attr_routing_profile_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the routing profile.

        :cloudformationAttribute: RoutingProfileArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRoutingProfileArn"))

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
    @jsii.member(jsii_name="defaultOutboundQueueArn")
    def default_outbound_queue_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the default outbound queue for the routing profile.'''
        return typing.cast(builtins.str, jsii.get(self, "defaultOutboundQueueArn"))

    @default_outbound_queue_arn.setter
    def default_outbound_queue_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50c110c7acb8febfc7d34536a1febea6502492baf2f6ee1037837dedbd70168e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultOutboundQueueArn", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''The description of the routing profile.'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__637b45a967f46a44a1c52dafa5bd595123bfb6815a0445ab0a79199a378934f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The identifier of the Amazon Connect instance.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba893df3049c142580fe563c14e51066d4293c46c9f36efe1bf670ae56ea1164)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="mediaConcurrencies")
    def media_concurrencies(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRoutingProfile.MediaConcurrencyProperty"]]]:
        '''The channels agents can handle in the Contact Control Panel (CCP) for this routing profile.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRoutingProfile.MediaConcurrencyProperty"]]], jsii.get(self, "mediaConcurrencies"))

    @media_concurrencies.setter
    def media_concurrencies(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRoutingProfile.MediaConcurrencyProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98acf5c62560e25441ec8acb2ae6f5177c36faf800e0f559ad291e27bc924a1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mediaConcurrencies", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the routing profile.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87262b051e4ac4dbfbde0cabebd7e31eeed71edd46cdaec4b306d89ac256b8ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="agentAvailabilityTimer")
    def agent_availability_timer(self) -> typing.Optional[builtins.str]:
        '''Whether agents with this routing profile will have their routing order calculated based on *time since their last inbound contact* or *longest idle time* .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "agentAvailabilityTimer"))

    @agent_availability_timer.setter
    def agent_availability_timer(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d19931b4ff72cc897b92c5bddb17158eb5a7dd2de0061c85498c43c4b38eabbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentAvailabilityTimer", value)

    @builtins.property
    @jsii.member(jsii_name="queueConfigs")
    def queue_configs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRoutingProfile.RoutingProfileQueueConfigProperty"]]]]:
        '''The inbound queues associated with the routing profile.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRoutingProfile.RoutingProfileQueueConfigProperty"]]]], jsii.get(self, "queueConfigs"))

    @queue_configs.setter
    def queue_configs(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRoutingProfile.RoutingProfileQueueConfigProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59e5612a464f7993fc5802b7496378e9f43c22ddbfdd66a4769b7dd34e2ad014)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queueConfigs", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce9959c28e0025c6a6c1956401b24d22cd16b9aa7621c46b183e63ed78f3ba65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnRoutingProfile.CrossChannelBehaviorProperty",
        jsii_struct_bases=[],
        name_mapping={"behavior_type": "behaviorType"},
    )
    class CrossChannelBehaviorProperty:
        def __init__(self, *, behavior_type: builtins.str) -> None:
            '''Defines the cross-channel routing behavior that allows an agent working on a contact in one channel to be offered a contact from a different channel.

            :param behavior_type: Specifies the other channels that can be routed to an agent handling their current channel.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-crosschannelbehavior.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                cross_channel_behavior_property = connect.CfnRoutingProfile.CrossChannelBehaviorProperty(
                    behavior_type="behaviorType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4be673a3765322ed5a02245be092441abde0c8425aaa9c81e6a49ca1ef5eecdd)
                check_type(argname="argument behavior_type", value=behavior_type, expected_type=type_hints["behavior_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "behavior_type": behavior_type,
            }

        @builtins.property
        def behavior_type(self) -> builtins.str:
            '''Specifies the other channels that can be routed to an agent handling their current channel.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-crosschannelbehavior.html#cfn-connect-routingprofile-crosschannelbehavior-behaviortype
            '''
            result = self._values.get("behavior_type")
            assert result is not None, "Required property 'behavior_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CrossChannelBehaviorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnRoutingProfile.MediaConcurrencyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "channel": "channel",
            "concurrency": "concurrency",
            "cross_channel_behavior": "crossChannelBehavior",
        },
    )
    class MediaConcurrencyProperty:
        def __init__(
            self,
            *,
            channel: builtins.str,
            concurrency: jsii.Number,
            cross_channel_behavior: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRoutingProfile.CrossChannelBehaviorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains information about which channels are supported, and how many contacts an agent can have on a channel simultaneously.

            :param channel: The channels that agents can handle in the Contact Control Panel (CCP).
            :param concurrency: The number of contacts an agent can have on a channel simultaneously. Valid Range for ``VOICE`` : Minimum value of 1. Maximum value of 1. Valid Range for ``CHAT`` : Minimum value of 1. Maximum value of 10. Valid Range for ``TASK`` : Minimum value of 1. Maximum value of 10.
            :param cross_channel_behavior: Defines the cross-channel routing behavior for each channel that is enabled for this Routing Profile. For example, this allows you to offer an agent a different contact from another channel when they are currently working with a contact from a Voice channel.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-mediaconcurrency.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                media_concurrency_property = connect.CfnRoutingProfile.MediaConcurrencyProperty(
                    channel="channel",
                    concurrency=123,
                
                    # the properties below are optional
                    cross_channel_behavior=connect.CfnRoutingProfile.CrossChannelBehaviorProperty(
                        behavior_type="behaviorType"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c169890f0c9845b73f64645c0d362ee0a7e26614d464148fd2a80b60082b10e5)
                check_type(argname="argument channel", value=channel, expected_type=type_hints["channel"])
                check_type(argname="argument concurrency", value=concurrency, expected_type=type_hints["concurrency"])
                check_type(argname="argument cross_channel_behavior", value=cross_channel_behavior, expected_type=type_hints["cross_channel_behavior"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "channel": channel,
                "concurrency": concurrency,
            }
            if cross_channel_behavior is not None:
                self._values["cross_channel_behavior"] = cross_channel_behavior

        @builtins.property
        def channel(self) -> builtins.str:
            '''The channels that agents can handle in the Contact Control Panel (CCP).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-mediaconcurrency.html#cfn-connect-routingprofile-mediaconcurrency-channel
            '''
            result = self._values.get("channel")
            assert result is not None, "Required property 'channel' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def concurrency(self) -> jsii.Number:
            '''The number of contacts an agent can have on a channel simultaneously.

            Valid Range for ``VOICE`` : Minimum value of 1. Maximum value of 1.

            Valid Range for ``CHAT`` : Minimum value of 1. Maximum value of 10.

            Valid Range for ``TASK`` : Minimum value of 1. Maximum value of 10.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-mediaconcurrency.html#cfn-connect-routingprofile-mediaconcurrency-concurrency
            '''
            result = self._values.get("concurrency")
            assert result is not None, "Required property 'concurrency' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def cross_channel_behavior(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRoutingProfile.CrossChannelBehaviorProperty"]]:
            '''Defines the cross-channel routing behavior for each channel that is enabled for this Routing Profile.

            For example, this allows you to offer an agent a different contact from another channel when they are currently working with a contact from a Voice channel.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-mediaconcurrency.html#cfn-connect-routingprofile-mediaconcurrency-crosschannelbehavior
            '''
            result = self._values.get("cross_channel_behavior")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRoutingProfile.CrossChannelBehaviorProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MediaConcurrencyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnRoutingProfile.RoutingProfileQueueConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delay": "delay",
            "priority": "priority",
            "queue_reference": "queueReference",
        },
    )
    class RoutingProfileQueueConfigProperty:
        def __init__(
            self,
            *,
            delay: jsii.Number,
            priority: jsii.Number,
            queue_reference: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRoutingProfile.RoutingProfileQueueReferenceProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Contains information about the queue and channel for which priority and delay can be set.

            :param delay: The delay, in seconds, a contact should be in the queue before they are routed to an available agent. For more information, see `Queues: priority and delay <https://docs.aws.amazon.com/connect/latest/adminguide/concepts-routing-profiles-priority.html>`_ in the *Amazon Connect Administrator Guide* .
            :param priority: The order in which contacts are to be handled for the queue. For more information, see `Queues: priority and delay <https://docs.aws.amazon.com/connect/latest/adminguide/concepts-routing-profiles-priority.html>`_ .
            :param queue_reference: Contains information about a queue resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-routingprofilequeueconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                routing_profile_queue_config_property = connect.CfnRoutingProfile.RoutingProfileQueueConfigProperty(
                    delay=123,
                    priority=123,
                    queue_reference=connect.CfnRoutingProfile.RoutingProfileQueueReferenceProperty(
                        channel="channel",
                        queue_arn="queueArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__032843b9e197335b76e0e3de0555493b80a1e7b395828aefda71c8150ea0a063)
                check_type(argname="argument delay", value=delay, expected_type=type_hints["delay"])
                check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
                check_type(argname="argument queue_reference", value=queue_reference, expected_type=type_hints["queue_reference"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "delay": delay,
                "priority": priority,
                "queue_reference": queue_reference,
            }

        @builtins.property
        def delay(self) -> jsii.Number:
            '''The delay, in seconds, a contact should be in the queue before they are routed to an available agent.

            For more information, see `Queues: priority and delay <https://docs.aws.amazon.com/connect/latest/adminguide/concepts-routing-profiles-priority.html>`_ in the *Amazon Connect Administrator Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-routingprofilequeueconfig.html#cfn-connect-routingprofile-routingprofilequeueconfig-delay
            '''
            result = self._values.get("delay")
            assert result is not None, "Required property 'delay' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def priority(self) -> jsii.Number:
            '''The order in which contacts are to be handled for the queue.

            For more information, see `Queues: priority and delay <https://docs.aws.amazon.com/connect/latest/adminguide/concepts-routing-profiles-priority.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-routingprofilequeueconfig.html#cfn-connect-routingprofile-routingprofilequeueconfig-priority
            '''
            result = self._values.get("priority")
            assert result is not None, "Required property 'priority' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def queue_reference(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnRoutingProfile.RoutingProfileQueueReferenceProperty"]:
            '''Contains information about a queue resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-routingprofilequeueconfig.html#cfn-connect-routingprofile-routingprofilequeueconfig-queuereference
            '''
            result = self._values.get("queue_reference")
            assert result is not None, "Required property 'queue_reference' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRoutingProfile.RoutingProfileQueueReferenceProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RoutingProfileQueueConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnRoutingProfile.RoutingProfileQueueReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={"channel": "channel", "queue_arn": "queueArn"},
    )
    class RoutingProfileQueueReferenceProperty:
        def __init__(self, *, channel: builtins.str, queue_arn: builtins.str) -> None:
            '''Contains the channel and queue identifier for a routing profile.

            :param channel: The channels agents can handle in the Contact Control Panel (CCP) for this routing profile.
            :param queue_arn: The Amazon Resource Name (ARN) of the queue.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-routingprofilequeuereference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                routing_profile_queue_reference_property = connect.CfnRoutingProfile.RoutingProfileQueueReferenceProperty(
                    channel="channel",
                    queue_arn="queueArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__57ccd007831b09a96896ef1c31704165fa1cc179777c86f32ce6de29dce25a9a)
                check_type(argname="argument channel", value=channel, expected_type=type_hints["channel"])
                check_type(argname="argument queue_arn", value=queue_arn, expected_type=type_hints["queue_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "channel": channel,
                "queue_arn": queue_arn,
            }

        @builtins.property
        def channel(self) -> builtins.str:
            '''The channels agents can handle in the Contact Control Panel (CCP) for this routing profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-routingprofilequeuereference.html#cfn-connect-routingprofile-routingprofilequeuereference-channel
            '''
            result = self._values.get("channel")
            assert result is not None, "Required property 'channel' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def queue_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the queue.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-routingprofile-routingprofilequeuereference.html#cfn-connect-routingprofile-routingprofilequeuereference-queuearn
            '''
            result = self._values.get("queue_arn")
            assert result is not None, "Required property 'queue_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RoutingProfileQueueReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnRoutingProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "default_outbound_queue_arn": "defaultOutboundQueueArn",
        "description": "description",
        "instance_arn": "instanceArn",
        "media_concurrencies": "mediaConcurrencies",
        "name": "name",
        "agent_availability_timer": "agentAvailabilityTimer",
        "queue_configs": "queueConfigs",
        "tags": "tags",
    },
)
class CfnRoutingProfileProps:
    def __init__(
        self,
        *,
        default_outbound_queue_arn: builtins.str,
        description: builtins.str,
        instance_arn: builtins.str,
        media_concurrencies: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRoutingProfile.MediaConcurrencyProperty, typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        agent_availability_timer: typing.Optional[builtins.str] = None,
        queue_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRoutingProfile.RoutingProfileQueueConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRoutingProfile``.

        :param default_outbound_queue_arn: The Amazon Resource Name (ARN) of the default outbound queue for the routing profile.
        :param description: The description of the routing profile.
        :param instance_arn: The identifier of the Amazon Connect instance.
        :param media_concurrencies: The channels agents can handle in the Contact Control Panel (CCP) for this routing profile.
        :param name: The name of the routing profile.
        :param agent_availability_timer: Whether agents with this routing profile will have their routing order calculated based on *time since their last inbound contact* or *longest idle time* .
        :param queue_configs: The inbound queues associated with the routing profile. If no queue is added, the agent can make only outbound calls.
        :param tags: The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-routingprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_routing_profile_props = connect.CfnRoutingProfileProps(
                default_outbound_queue_arn="defaultOutboundQueueArn",
                description="description",
                instance_arn="instanceArn",
                media_concurrencies=[connect.CfnRoutingProfile.MediaConcurrencyProperty(
                    channel="channel",
                    concurrency=123,
            
                    # the properties below are optional
                    cross_channel_behavior=connect.CfnRoutingProfile.CrossChannelBehaviorProperty(
                        behavior_type="behaviorType"
                    )
                )],
                name="name",
            
                # the properties below are optional
                agent_availability_timer="agentAvailabilityTimer",
                queue_configs=[connect.CfnRoutingProfile.RoutingProfileQueueConfigProperty(
                    delay=123,
                    priority=123,
                    queue_reference=connect.CfnRoutingProfile.RoutingProfileQueueReferenceProperty(
                        channel="channel",
                        queue_arn="queueArn"
                    )
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c352ac5c14b7a76c3094c7e1595be9aaa093440801508c4780610a6d26b66aa7)
            check_type(argname="argument default_outbound_queue_arn", value=default_outbound_queue_arn, expected_type=type_hints["default_outbound_queue_arn"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument media_concurrencies", value=media_concurrencies, expected_type=type_hints["media_concurrencies"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument agent_availability_timer", value=agent_availability_timer, expected_type=type_hints["agent_availability_timer"])
            check_type(argname="argument queue_configs", value=queue_configs, expected_type=type_hints["queue_configs"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_outbound_queue_arn": default_outbound_queue_arn,
            "description": description,
            "instance_arn": instance_arn,
            "media_concurrencies": media_concurrencies,
            "name": name,
        }
        if agent_availability_timer is not None:
            self._values["agent_availability_timer"] = agent_availability_timer
        if queue_configs is not None:
            self._values["queue_configs"] = queue_configs
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def default_outbound_queue_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the default outbound queue for the routing profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-routingprofile.html#cfn-connect-routingprofile-defaultoutboundqueuearn
        '''
        result = self._values.get("default_outbound_queue_arn")
        assert result is not None, "Required property 'default_outbound_queue_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> builtins.str:
        '''The description of the routing profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-routingprofile.html#cfn-connect-routingprofile-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The identifier of the Amazon Connect instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-routingprofile.html#cfn-connect-routingprofile-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def media_concurrencies(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRoutingProfile.MediaConcurrencyProperty]]]:
        '''The channels agents can handle in the Contact Control Panel (CCP) for this routing profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-routingprofile.html#cfn-connect-routingprofile-mediaconcurrencies
        '''
        result = self._values.get("media_concurrencies")
        assert result is not None, "Required property 'media_concurrencies' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRoutingProfile.MediaConcurrencyProperty]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the routing profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-routingprofile.html#cfn-connect-routingprofile-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def agent_availability_timer(self) -> typing.Optional[builtins.str]:
        '''Whether agents with this routing profile will have their routing order calculated based on *time since their last inbound contact* or *longest idle time* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-routingprofile.html#cfn-connect-routingprofile-agentavailabilitytimer
        '''
        result = self._values.get("agent_availability_timer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def queue_configs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRoutingProfile.RoutingProfileQueueConfigProperty]]]]:
        '''The inbound queues associated with the routing profile.

        If no queue is added, the agent can make only outbound calls.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-routingprofile.html#cfn-connect-routingprofile-queueconfigs
        '''
        result = self._values.get("queue_configs")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRoutingProfile.RoutingProfileQueueConfigProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        For example, { "Tags": {"key1":"value1", "key2":"value2"} }.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-routingprofile.html#cfn-connect-routingprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRoutingProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnRule",
):
    '''Creates a rule for the specified Amazon Connect instance.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-rule.html
    :cloudformationResource: AWS::Connect::Rule
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        # assign_contact_category_actions: Any
        # empty_value: Any
        # end_associated_tasks_actions: Any
        
        cfn_rule = connect.CfnRule(self, "MyCfnRule",
            actions=connect.CfnRule.ActionsProperty(
                assign_contact_category_actions=[assign_contact_category_actions],
                create_case_actions=[connect.CfnRule.CreateCaseActionProperty(
                    fields=[connect.CfnRule.FieldProperty(
                        id="id",
                        value=connect.CfnRule.FieldValueProperty(
                            boolean_value=False,
                            double_value=123,
                            empty_value=empty_value,
                            string_value="stringValue"
                        )
                    )],
                    template_id="templateId"
                )],
                end_associated_tasks_actions=[end_associated_tasks_actions],
                event_bridge_actions=[connect.CfnRule.EventBridgeActionProperty(
                    name="name"
                )],
                send_notification_actions=[connect.CfnRule.SendNotificationActionProperty(
                    content="content",
                    content_type="contentType",
                    delivery_method="deliveryMethod",
                    recipient=connect.CfnRule.NotificationRecipientTypeProperty(
                        user_arns=["userArns"],
                        user_tags={
                            "user_tags_key": "userTags"
                        }
                    ),
        
                    # the properties below are optional
                    subject="subject"
                )],
                task_actions=[connect.CfnRule.TaskActionProperty(
                    contact_flow_arn="contactFlowArn",
                    name="name",
        
                    # the properties below are optional
                    description="description",
                    references={
                        "references_key": connect.CfnRule.ReferenceProperty(
                            type="type",
                            value="value"
                        )
                    }
                )],
                update_case_actions=[connect.CfnRule.UpdateCaseActionProperty(
                    fields=[connect.CfnRule.FieldProperty(
                        id="id",
                        value=connect.CfnRule.FieldValueProperty(
                            boolean_value=False,
                            double_value=123,
                            empty_value=empty_value,
                            string_value="stringValue"
                        )
                    )]
                )]
            ),
            function="function",
            instance_arn="instanceArn",
            name="name",
            publish_status="publishStatus",
            trigger_event_source=connect.CfnRule.RuleTriggerEventSourceProperty(
                event_source_name="eventSourceName",
        
                # the properties below are optional
                integration_association_arn="integrationAssociationArn"
            ),
        
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
        actions: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.ActionsProperty", typing.Dict[builtins.str, typing.Any]]],
        function: builtins.str,
        instance_arn: builtins.str,
        name: builtins.str,
        publish_status: builtins.str,
        trigger_event_source: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.RuleTriggerEventSourceProperty", typing.Dict[builtins.str, typing.Any]]],
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param actions: A list of actions to be run when the rule is triggered.
        :param function: The conditions of the rule.
        :param instance_arn: The Amazon Resource Name (ARN) of the instance.
        :param name: The name of the rule.
        :param publish_status: The publish status of the rule. *Allowed values* : ``DRAFT`` | ``PUBLISHED``
        :param trigger_event_source: The event source to trigger the rule.
        :param tags: The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__999d5f7971fc0ea0f693e0f9a61faf62317d493403a6d249ca1db6bc52d61e6f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRuleProps(
            actions=actions,
            function=function,
            instance_arn=instance_arn,
            name=name,
            publish_status=publish_status,
            trigger_event_source=trigger_event_source,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa852f8205e0acaca3e6361c61c512ea090fe504a708495d2b5bdadc81b30809)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f8f82a813645b192cb4d0a6df6a35e9ffe4fe072375390e4d29ebb42555752ad)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrRuleArn")
    def attr_rule_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the rule.

        :cloudformationAttribute: RuleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRuleArn"))

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
    @jsii.member(jsii_name="actions")
    def actions(self) -> typing.Union[_IResolvable_da3f097b, "CfnRule.ActionsProperty"]:
        '''A list of actions to be run when the rule is triggered.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRule.ActionsProperty"], jsii.get(self, "actions"))

    @actions.setter
    def actions(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnRule.ActionsProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bdf3e9c3a73f02992b32c967f3457b7eeade7d3dfa554da9d661f54924ad9a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actions", value)

    @builtins.property
    @jsii.member(jsii_name="function")
    def function(self) -> builtins.str:
        '''The conditions of the rule.'''
        return typing.cast(builtins.str, jsii.get(self, "function"))

    @function.setter
    def function(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85af4feedf296e30da787ccf9bc61e248b9a97c21a29fd8fbf38621d5d654fdd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "function", value)

    @builtins.property
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec5da44206c20fbb184f7443ea185123d28ab75d447650604f654e3fe336b233)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the rule.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6699a016b8fc3ffcc40b2227c32c82c77dcef5f7a74d28bea7e181707fb33bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="publishStatus")
    def publish_status(self) -> builtins.str:
        '''The publish status of the rule.'''
        return typing.cast(builtins.str, jsii.get(self, "publishStatus"))

    @publish_status.setter
    def publish_status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__464a87f0223cf9d2bd4ca32eeb79cbb74d44d9fead6bf2a81a1db65870834bf2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publishStatus", value)

    @builtins.property
    @jsii.member(jsii_name="triggerEventSource")
    def trigger_event_source(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnRule.RuleTriggerEventSourceProperty"]:
        '''The event source to trigger the rule.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRule.RuleTriggerEventSourceProperty"], jsii.get(self, "triggerEventSource"))

    @trigger_event_source.setter
    def trigger_event_source(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnRule.RuleTriggerEventSourceProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a752b13b9a86d9caa3ed642e2b19a8ac6db9d24515c76f729c8ad704d664388)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggerEventSource", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7ff60d02ce44f26fb689403f0b8615b44a5b305d316fb9e80298948590ae2d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnRule.ActionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "assign_contact_category_actions": "assignContactCategoryActions",
            "create_case_actions": "createCaseActions",
            "end_associated_tasks_actions": "endAssociatedTasksActions",
            "event_bridge_actions": "eventBridgeActions",
            "send_notification_actions": "sendNotificationActions",
            "task_actions": "taskActions",
            "update_case_actions": "updateCaseActions",
        },
    )
    class ActionsProperty:
        def __init__(
            self,
            *,
            assign_contact_category_actions: typing.Optional[typing.Union[typing.Sequence[typing.Any], _IResolvable_da3f097b]] = None,
            create_case_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.CreateCaseActionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            end_associated_tasks_actions: typing.Optional[typing.Union[typing.Sequence[typing.Any], _IResolvable_da3f097b]] = None,
            event_bridge_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.EventBridgeActionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            send_notification_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.SendNotificationActionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            task_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.TaskActionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            update_case_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.UpdateCaseActionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''A list of actions to be run when the rule is triggered.

            :param assign_contact_category_actions: Information about the contact category action. The syntax can be empty, for example, ``{}`` .
            :param create_case_actions: This action will create a case when a rule is triggered.
            :param end_associated_tasks_actions: This action will end associated tasks when a rule is triggered.
            :param event_bridge_actions: Information about the EventBridge action.
            :param send_notification_actions: Information about the send notification action.
            :param task_actions: Information about the task action. This field is required if ``TriggerEventSource`` is one of the following values: ``OnZendeskTicketCreate`` | ``OnZendeskTicketStatusUpdate`` | ``OnSalesforceCaseCreate``
            :param update_case_actions: This action will update a case when a rule is triggered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-actions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                # assign_contact_category_actions: Any
                # empty_value: Any
                # end_associated_tasks_actions: Any
                
                actions_property = connect.CfnRule.ActionsProperty(
                    assign_contact_category_actions=[assign_contact_category_actions],
                    create_case_actions=[connect.CfnRule.CreateCaseActionProperty(
                        fields=[connect.CfnRule.FieldProperty(
                            id="id",
                            value=connect.CfnRule.FieldValueProperty(
                                boolean_value=False,
                                double_value=123,
                                empty_value=empty_value,
                                string_value="stringValue"
                            )
                        )],
                        template_id="templateId"
                    )],
                    end_associated_tasks_actions=[end_associated_tasks_actions],
                    event_bridge_actions=[connect.CfnRule.EventBridgeActionProperty(
                        name="name"
                    )],
                    send_notification_actions=[connect.CfnRule.SendNotificationActionProperty(
                        content="content",
                        content_type="contentType",
                        delivery_method="deliveryMethod",
                        recipient=connect.CfnRule.NotificationRecipientTypeProperty(
                            user_arns=["userArns"],
                            user_tags={
                                "user_tags_key": "userTags"
                            }
                        ),
                
                        # the properties below are optional
                        subject="subject"
                    )],
                    task_actions=[connect.CfnRule.TaskActionProperty(
                        contact_flow_arn="contactFlowArn",
                        name="name",
                
                        # the properties below are optional
                        description="description",
                        references={
                            "references_key": connect.CfnRule.ReferenceProperty(
                                type="type",
                                value="value"
                            )
                        }
                    )],
                    update_case_actions=[connect.CfnRule.UpdateCaseActionProperty(
                        fields=[connect.CfnRule.FieldProperty(
                            id="id",
                            value=connect.CfnRule.FieldValueProperty(
                                boolean_value=False,
                                double_value=123,
                                empty_value=empty_value,
                                string_value="stringValue"
                            )
                        )]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0ef20a75dbfc13161d3fff13ec1c4969adde44c34f62addd27e480514ce92395)
                check_type(argname="argument assign_contact_category_actions", value=assign_contact_category_actions, expected_type=type_hints["assign_contact_category_actions"])
                check_type(argname="argument create_case_actions", value=create_case_actions, expected_type=type_hints["create_case_actions"])
                check_type(argname="argument end_associated_tasks_actions", value=end_associated_tasks_actions, expected_type=type_hints["end_associated_tasks_actions"])
                check_type(argname="argument event_bridge_actions", value=event_bridge_actions, expected_type=type_hints["event_bridge_actions"])
                check_type(argname="argument send_notification_actions", value=send_notification_actions, expected_type=type_hints["send_notification_actions"])
                check_type(argname="argument task_actions", value=task_actions, expected_type=type_hints["task_actions"])
                check_type(argname="argument update_case_actions", value=update_case_actions, expected_type=type_hints["update_case_actions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if assign_contact_category_actions is not None:
                self._values["assign_contact_category_actions"] = assign_contact_category_actions
            if create_case_actions is not None:
                self._values["create_case_actions"] = create_case_actions
            if end_associated_tasks_actions is not None:
                self._values["end_associated_tasks_actions"] = end_associated_tasks_actions
            if event_bridge_actions is not None:
                self._values["event_bridge_actions"] = event_bridge_actions
            if send_notification_actions is not None:
                self._values["send_notification_actions"] = send_notification_actions
            if task_actions is not None:
                self._values["task_actions"] = task_actions
            if update_case_actions is not None:
                self._values["update_case_actions"] = update_case_actions

        @builtins.property
        def assign_contact_category_actions(
            self,
        ) -> typing.Optional[typing.Union[typing.List[typing.Any], _IResolvable_da3f097b]]:
            '''Information about the contact category action.

            The syntax can be empty, for example, ``{}`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-actions.html#cfn-connect-rule-actions-assigncontactcategoryactions
            '''
            result = self._values.get("assign_contact_category_actions")
            return typing.cast(typing.Optional[typing.Union[typing.List[typing.Any], _IResolvable_da3f097b]], result)

        @builtins.property
        def create_case_actions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.CreateCaseActionProperty"]]]]:
            '''This action will create a case when a rule is triggered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-actions.html#cfn-connect-rule-actions-createcaseactions
            '''
            result = self._values.get("create_case_actions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.CreateCaseActionProperty"]]]], result)

        @builtins.property
        def end_associated_tasks_actions(
            self,
        ) -> typing.Optional[typing.Union[typing.List[typing.Any], _IResolvable_da3f097b]]:
            '''This action will end associated tasks when a rule is triggered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-actions.html#cfn-connect-rule-actions-endassociatedtasksactions
            '''
            result = self._values.get("end_associated_tasks_actions")
            return typing.cast(typing.Optional[typing.Union[typing.List[typing.Any], _IResolvable_da3f097b]], result)

        @builtins.property
        def event_bridge_actions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.EventBridgeActionProperty"]]]]:
            '''Information about the EventBridge action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-actions.html#cfn-connect-rule-actions-eventbridgeactions
            '''
            result = self._values.get("event_bridge_actions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.EventBridgeActionProperty"]]]], result)

        @builtins.property
        def send_notification_actions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.SendNotificationActionProperty"]]]]:
            '''Information about the send notification action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-actions.html#cfn-connect-rule-actions-sendnotificationactions
            '''
            result = self._values.get("send_notification_actions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.SendNotificationActionProperty"]]]], result)

        @builtins.property
        def task_actions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.TaskActionProperty"]]]]:
            '''Information about the task action.

            This field is required if ``TriggerEventSource`` is one of the following values: ``OnZendeskTicketCreate`` | ``OnZendeskTicketStatusUpdate`` | ``OnSalesforceCaseCreate``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-actions.html#cfn-connect-rule-actions-taskactions
            '''
            result = self._values.get("task_actions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.TaskActionProperty"]]]], result)

        @builtins.property
        def update_case_actions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.UpdateCaseActionProperty"]]]]:
            '''This action will update a case when a rule is triggered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-actions.html#cfn-connect-rule-actions-updatecaseactions
            '''
            result = self._values.get("update_case_actions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.UpdateCaseActionProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnRule.CreateCaseActionProperty",
        jsii_struct_bases=[],
        name_mapping={"fields": "fields", "template_id": "templateId"},
    )
    class CreateCaseActionProperty:
        def __init__(
            self,
            *,
            fields: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.FieldProperty", typing.Dict[builtins.str, typing.Any]]]]],
            template_id: builtins.str,
        ) -> None:
            '''The definition for create case action.

            :param fields: An array of case fields.
            :param template_id: The Id of template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-createcaseaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                # empty_value: Any
                
                create_case_action_property = connect.CfnRule.CreateCaseActionProperty(
                    fields=[connect.CfnRule.FieldProperty(
                        id="id",
                        value=connect.CfnRule.FieldValueProperty(
                            boolean_value=False,
                            double_value=123,
                            empty_value=empty_value,
                            string_value="stringValue"
                        )
                    )],
                    template_id="templateId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ab1813f0f35711195f55dc6283bd2d1a984f7c2f7e37efe287a6d2d847cd6d86)
                check_type(argname="argument fields", value=fields, expected_type=type_hints["fields"])
                check_type(argname="argument template_id", value=template_id, expected_type=type_hints["template_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "fields": fields,
                "template_id": template_id,
            }

        @builtins.property
        def fields(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.FieldProperty"]]]:
            '''An array of case fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-createcaseaction.html#cfn-connect-rule-createcaseaction-fields
            '''
            result = self._values.get("fields")
            assert result is not None, "Required property 'fields' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.FieldProperty"]]], result)

        @builtins.property
        def template_id(self) -> builtins.str:
            '''The Id of template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-createcaseaction.html#cfn-connect-rule-createcaseaction-templateid
            '''
            result = self._values.get("template_id")
            assert result is not None, "Required property 'template_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CreateCaseActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnRule.EventBridgeActionProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name"},
    )
    class EventBridgeActionProperty:
        def __init__(self, *, name: builtins.str) -> None:
            '''The EventBridge action definition.

            :param name: The name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-eventbridgeaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                event_bridge_action_property = connect.CfnRule.EventBridgeActionProperty(
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__037f7c36eff1515bc6e2d8e67f9b2bac8beade9773e2103dd3b8b5ca5405e447)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-eventbridgeaction.html#cfn-connect-rule-eventbridgeaction-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventBridgeActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnRule.FieldProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id", "value": "value"},
    )
    class FieldProperty:
        def __init__(
            self,
            *,
            id: builtins.str,
            value: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.FieldValueProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The field of the case.

            :param id: The Id of the field.
            :param value: The value of the field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-field.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                # empty_value: Any
                
                field_property = connect.CfnRule.FieldProperty(
                    id="id",
                    value=connect.CfnRule.FieldValueProperty(
                        boolean_value=False,
                        double_value=123,
                        empty_value=empty_value,
                        string_value="stringValue"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b6c57d9892877040d89a2aed4e1afb5e5eb027cb36bc0f8392074bd7cd8d8323)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
                "value": value,
            }

        @builtins.property
        def id(self) -> builtins.str:
            '''The Id of the field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-field.html#cfn-connect-rule-field-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnRule.FieldValueProperty"]:
            '''The value of the field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-field.html#cfn-connect-rule-field-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRule.FieldValueProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnRule.FieldValueProperty",
        jsii_struct_bases=[],
        name_mapping={
            "boolean_value": "booleanValue",
            "double_value": "doubleValue",
            "empty_value": "emptyValue",
            "string_value": "stringValue",
        },
    )
    class FieldValueProperty:
        def __init__(
            self,
            *,
            boolean_value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            double_value: typing.Optional[jsii.Number] = None,
            empty_value: typing.Any = None,
            string_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Object for case field values.

            :param boolean_value: 
            :param double_value: 
            :param empty_value: 
            :param string_value: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-fieldvalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                # empty_value: Any
                
                field_value_property = connect.CfnRule.FieldValueProperty(
                    boolean_value=False,
                    double_value=123,
                    empty_value=empty_value,
                    string_value="stringValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b775c6c3e6b1c930720eb9500ebf63cc475488f7c2d8ed565fb6a0294ff1e652)
                check_type(argname="argument boolean_value", value=boolean_value, expected_type=type_hints["boolean_value"])
                check_type(argname="argument double_value", value=double_value, expected_type=type_hints["double_value"])
                check_type(argname="argument empty_value", value=empty_value, expected_type=type_hints["empty_value"])
                check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if boolean_value is not None:
                self._values["boolean_value"] = boolean_value
            if double_value is not None:
                self._values["double_value"] = double_value
            if empty_value is not None:
                self._values["empty_value"] = empty_value
            if string_value is not None:
                self._values["string_value"] = string_value

        @builtins.property
        def boolean_value(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-fieldvalue.html#cfn-connect-rule-fieldvalue-booleanvalue
            '''
            result = self._values.get("boolean_value")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def double_value(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-fieldvalue.html#cfn-connect-rule-fieldvalue-doublevalue
            '''
            result = self._values.get("double_value")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def empty_value(self) -> typing.Any:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-fieldvalue.html#cfn-connect-rule-fieldvalue-emptyvalue
            '''
            result = self._values.get("empty_value")
            return typing.cast(typing.Any, result)

        @builtins.property
        def string_value(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-fieldvalue.html#cfn-connect-rule-fieldvalue-stringvalue
            '''
            result = self._values.get("string_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnRule.NotificationRecipientTypeProperty",
        jsii_struct_bases=[],
        name_mapping={"user_arns": "userArns", "user_tags": "userTags"},
    )
    class NotificationRecipientTypeProperty:
        def __init__(
            self,
            *,
            user_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
            user_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        ) -> None:
            '''The type of notification recipient.

            :param user_arns: The Amazon Resource Name (ARN) of the user account.
            :param user_tags: The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }. Amazon Connect users with the specified tags will be notified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-notificationrecipienttype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                notification_recipient_type_property = connect.CfnRule.NotificationRecipientTypeProperty(
                    user_arns=["userArns"],
                    user_tags={
                        "user_tags_key": "userTags"
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4d577395a2866fe40fdf75bbcc932da0701cd7985bbb4de4e2ef65243ba9d387)
                check_type(argname="argument user_arns", value=user_arns, expected_type=type_hints["user_arns"])
                check_type(argname="argument user_tags", value=user_tags, expected_type=type_hints["user_tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if user_arns is not None:
                self._values["user_arns"] = user_arns
            if user_tags is not None:
                self._values["user_tags"] = user_tags

        @builtins.property
        def user_arns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The Amazon Resource Name (ARN) of the user account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-notificationrecipienttype.html#cfn-connect-rule-notificationrecipienttype-userarns
            '''
            result = self._values.get("user_arns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def user_tags(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''The tags used to organize, track, or control access for this resource.

            For example, { "tags": {"key1":"value1", "key2":"value2"} }. Amazon Connect users with the specified tags will be notified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-notificationrecipienttype.html#cfn-connect-rule-notificationrecipienttype-usertags
            '''
            result = self._values.get("user_tags")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotificationRecipientTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnRule.ReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "value": "value"},
    )
    class ReferenceProperty:
        def __init__(self, *, type: builtins.str, value: builtins.str) -> None:
            '''Information about the reference when the ``referenceType`` is ``URL`` .

            Otherwise, null. (Supports variable injection in the ``Value`` field.)

            :param type: The type of the reference. ``DATE`` must be of type Epoch timestamp. *Allowed values* : ``URL`` | ``ATTACHMENT`` | ``NUMBER`` | ``STRING`` | ``DATE`` | ``EMAIL``
            :param value: A valid value for the reference. For example, for a URL reference, a formatted URL that is displayed to an agent in the Contact Control Panel (CCP).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-reference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                reference_property = connect.CfnRule.ReferenceProperty(
                    type="type",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d6a9deeefd8de7f6bdabd5dee0827f879a4b6911d8516976e0492403b3a4724a)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
                "value": value,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of the reference. ``DATE`` must be of type Epoch timestamp.

            *Allowed values* : ``URL`` | ``ATTACHMENT`` | ``NUMBER`` | ``STRING`` | ``DATE`` | ``EMAIL``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-reference.html#cfn-connect-rule-reference-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''A valid value for the reference.

            For example, for a URL reference, a formatted URL that is displayed to an agent in the Contact Control Panel (CCP).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-reference.html#cfn-connect-rule-reference-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnRule.RuleTriggerEventSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "event_source_name": "eventSourceName",
            "integration_association_arn": "integrationAssociationArn",
        },
    )
    class RuleTriggerEventSourceProperty:
        def __init__(
            self,
            *,
            event_source_name: builtins.str,
            integration_association_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The name of the event source.

            :param event_source_name: The name of the event source.
            :param integration_association_arn: The Amazon Resource Name (ARN) of the integration association. ``IntegrationAssociationArn`` is required if ``TriggerEventSource`` is one of the following values: ``OnZendeskTicketCreate`` | ``OnZendeskTicketStatusUpdate`` | ``OnSalesforceCaseCreate``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-ruletriggereventsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                rule_trigger_event_source_property = connect.CfnRule.RuleTriggerEventSourceProperty(
                    event_source_name="eventSourceName",
                
                    # the properties below are optional
                    integration_association_arn="integrationAssociationArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__16bc3686835833422d3f82ede42c0b9acf288c30c14f9b3b761db32339bbd1f5)
                check_type(argname="argument event_source_name", value=event_source_name, expected_type=type_hints["event_source_name"])
                check_type(argname="argument integration_association_arn", value=integration_association_arn, expected_type=type_hints["integration_association_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "event_source_name": event_source_name,
            }
            if integration_association_arn is not None:
                self._values["integration_association_arn"] = integration_association_arn

        @builtins.property
        def event_source_name(self) -> builtins.str:
            '''The name of the event source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-ruletriggereventsource.html#cfn-connect-rule-ruletriggereventsource-eventsourcename
            '''
            result = self._values.get("event_source_name")
            assert result is not None, "Required property 'event_source_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def integration_association_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the integration association.

            ``IntegrationAssociationArn`` is required if ``TriggerEventSource`` is one of the following values: ``OnZendeskTicketCreate`` | ``OnZendeskTicketStatusUpdate`` | ``OnSalesforceCaseCreate``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-ruletriggereventsource.html#cfn-connect-rule-ruletriggereventsource-integrationassociationarn
            '''
            result = self._values.get("integration_association_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleTriggerEventSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnRule.SendNotificationActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "content": "content",
            "content_type": "contentType",
            "delivery_method": "deliveryMethod",
            "recipient": "recipient",
            "subject": "subject",
        },
    )
    class SendNotificationActionProperty:
        def __init__(
            self,
            *,
            content: builtins.str,
            content_type: builtins.str,
            delivery_method: builtins.str,
            recipient: typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.NotificationRecipientTypeProperty", typing.Dict[builtins.str, typing.Any]]],
            subject: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about the send notification action.

            :param content: Notification content. Supports variable injection. For more information, see `JSONPath reference <https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html>`_ in the *Amazon Connect Administrators Guide* .
            :param content_type: Content type format. *Allowed value* : ``PLAIN_TEXT``
            :param delivery_method: Notification delivery method. *Allowed value* : ``EMAIL``
            :param recipient: Notification recipient.
            :param subject: The subject of the email if the delivery method is ``EMAIL`` . Supports variable injection. For more information, see `JSONPath reference <https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html>`_ in the *Amazon Connect Administrators Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-sendnotificationaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                send_notification_action_property = connect.CfnRule.SendNotificationActionProperty(
                    content="content",
                    content_type="contentType",
                    delivery_method="deliveryMethod",
                    recipient=connect.CfnRule.NotificationRecipientTypeProperty(
                        user_arns=["userArns"],
                        user_tags={
                            "user_tags_key": "userTags"
                        }
                    ),
                
                    # the properties below are optional
                    subject="subject"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__199075d61da7aee6c24aad33a7023d6a679853ff216c051fe322418490e5e9e4)
                check_type(argname="argument content", value=content, expected_type=type_hints["content"])
                check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
                check_type(argname="argument delivery_method", value=delivery_method, expected_type=type_hints["delivery_method"])
                check_type(argname="argument recipient", value=recipient, expected_type=type_hints["recipient"])
                check_type(argname="argument subject", value=subject, expected_type=type_hints["subject"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "content": content,
                "content_type": content_type,
                "delivery_method": delivery_method,
                "recipient": recipient,
            }
            if subject is not None:
                self._values["subject"] = subject

        @builtins.property
        def content(self) -> builtins.str:
            '''Notification content.

            Supports variable injection. For more information, see `JSONPath reference <https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html>`_ in the *Amazon Connect Administrators Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-sendnotificationaction.html#cfn-connect-rule-sendnotificationaction-content
            '''
            result = self._values.get("content")
            assert result is not None, "Required property 'content' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def content_type(self) -> builtins.str:
            '''Content type format.

            *Allowed value* : ``PLAIN_TEXT``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-sendnotificationaction.html#cfn-connect-rule-sendnotificationaction-contenttype
            '''
            result = self._values.get("content_type")
            assert result is not None, "Required property 'content_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def delivery_method(self) -> builtins.str:
            '''Notification delivery method.

            *Allowed value* : ``EMAIL``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-sendnotificationaction.html#cfn-connect-rule-sendnotificationaction-deliverymethod
            '''
            result = self._values.get("delivery_method")
            assert result is not None, "Required property 'delivery_method' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def recipient(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnRule.NotificationRecipientTypeProperty"]:
            '''Notification recipient.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-sendnotificationaction.html#cfn-connect-rule-sendnotificationaction-recipient
            '''
            result = self._values.get("recipient")
            assert result is not None, "Required property 'recipient' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnRule.NotificationRecipientTypeProperty"], result)

        @builtins.property
        def subject(self) -> typing.Optional[builtins.str]:
            '''The subject of the email if the delivery method is ``EMAIL`` .

            Supports variable injection. For more information, see `JSONPath reference <https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html>`_ in the *Amazon Connect Administrators Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-sendnotificationaction.html#cfn-connect-rule-sendnotificationaction-subject
            '''
            result = self._values.get("subject")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SendNotificationActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnRule.TaskActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "contact_flow_arn": "contactFlowArn",
            "name": "name",
            "description": "description",
            "references": "references",
        },
    )
    class TaskActionProperty:
        def __init__(
            self,
            *,
            contact_flow_arn: builtins.str,
            name: builtins.str,
            description: typing.Optional[builtins.str] = None,
            references: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.ReferenceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Information about the task action.

            This field is required if ``TriggerEventSource`` is one of the following values: ``OnZendeskTicketCreate`` | ``OnZendeskTicketStatusUpdate`` | ``OnSalesforceCaseCreate``

            :param contact_flow_arn: The Amazon Resource Name (ARN) of the flow.
            :param name: The name. Supports variable injection. For more information, see `JSONPath reference <https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html>`_ in the *Amazon Connect Administrators Guide* .
            :param description: The description. Supports variable injection. For more information, see `JSONPath reference <https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html>`_ in the *Amazon Connect Administrators Guide* .
            :param references: Information about the reference when the ``referenceType`` is ``URL`` . Otherwise, null. ``URL`` is the only accepted type. (Supports variable injection in the ``Value`` field.)

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-taskaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                task_action_property = connect.CfnRule.TaskActionProperty(
                    contact_flow_arn="contactFlowArn",
                    name="name",
                
                    # the properties below are optional
                    description="description",
                    references={
                        "references_key": connect.CfnRule.ReferenceProperty(
                            type="type",
                            value="value"
                        )
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__36d4ac91ef6fb71bdda5474ed1cbe12228c8f5caa3aec2778c4c6642b1ab6b3b)
                check_type(argname="argument contact_flow_arn", value=contact_flow_arn, expected_type=type_hints["contact_flow_arn"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument references", value=references, expected_type=type_hints["references"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "contact_flow_arn": contact_flow_arn,
                "name": name,
            }
            if description is not None:
                self._values["description"] = description
            if references is not None:
                self._values["references"] = references

        @builtins.property
        def contact_flow_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-taskaction.html#cfn-connect-rule-taskaction-contactflowarn
            '''
            result = self._values.get("contact_flow_arn")
            assert result is not None, "Required property 'contact_flow_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name.

            Supports variable injection. For more information, see `JSONPath reference <https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html>`_ in the *Amazon Connect Administrators Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-taskaction.html#cfn-connect-rule-taskaction-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description.

            Supports variable injection. For more information, see `JSONPath reference <https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-variable-injection.html>`_ in the *Amazon Connect Administrators Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-taskaction.html#cfn-connect-rule-taskaction-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def references(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnRule.ReferenceProperty"]]]]:
            '''Information about the reference when the ``referenceType`` is ``URL`` .

            Otherwise, null. ``URL`` is the only accepted type. (Supports variable injection in the ``Value`` field.)

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-taskaction.html#cfn-connect-rule-taskaction-references
            '''
            result = self._values.get("references")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnRule.ReferenceProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TaskActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnRule.UpdateCaseActionProperty",
        jsii_struct_bases=[],
        name_mapping={"fields": "fields"},
    )
    class UpdateCaseActionProperty:
        def __init__(
            self,
            *,
            fields: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRule.FieldProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''The definition for update case action.

            :param fields: An array of case fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-updatecaseaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                # empty_value: Any
                
                update_case_action_property = connect.CfnRule.UpdateCaseActionProperty(
                    fields=[connect.CfnRule.FieldProperty(
                        id="id",
                        value=connect.CfnRule.FieldValueProperty(
                            boolean_value=False,
                            double_value=123,
                            empty_value=empty_value,
                            string_value="stringValue"
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__172e88a6af9428a8608ec5ab094e800f6fbe7460bbec91c4a3347cc987a420e5)
                check_type(argname="argument fields", value=fields, expected_type=type_hints["fields"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "fields": fields,
            }

        @builtins.property
        def fields(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.FieldProperty"]]]:
            '''An array of case fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-rule-updatecaseaction.html#cfn-connect-rule-updatecaseaction-fields
            '''
            result = self._values.get("fields")
            assert result is not None, "Required property 'fields' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRule.FieldProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UpdateCaseActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "actions": "actions",
        "function": "function",
        "instance_arn": "instanceArn",
        "name": "name",
        "publish_status": "publishStatus",
        "trigger_event_source": "triggerEventSource",
        "tags": "tags",
    },
)
class CfnRuleProps:
    def __init__(
        self,
        *,
        actions: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.ActionsProperty, typing.Dict[builtins.str, typing.Any]]],
        function: builtins.str,
        instance_arn: builtins.str,
        name: builtins.str,
        publish_status: builtins.str,
        trigger_event_source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.RuleTriggerEventSourceProperty, typing.Dict[builtins.str, typing.Any]]],
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRule``.

        :param actions: A list of actions to be run when the rule is triggered.
        :param function: The conditions of the rule.
        :param instance_arn: The Amazon Resource Name (ARN) of the instance.
        :param name: The name of the rule.
        :param publish_status: The publish status of the rule. *Allowed values* : ``DRAFT`` | ``PUBLISHED``
        :param trigger_event_source: The event source to trigger the rule.
        :param tags: The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-rule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            # assign_contact_category_actions: Any
            # empty_value: Any
            # end_associated_tasks_actions: Any
            
            cfn_rule_props = connect.CfnRuleProps(
                actions=connect.CfnRule.ActionsProperty(
                    assign_contact_category_actions=[assign_contact_category_actions],
                    create_case_actions=[connect.CfnRule.CreateCaseActionProperty(
                        fields=[connect.CfnRule.FieldProperty(
                            id="id",
                            value=connect.CfnRule.FieldValueProperty(
                                boolean_value=False,
                                double_value=123,
                                empty_value=empty_value,
                                string_value="stringValue"
                            )
                        )],
                        template_id="templateId"
                    )],
                    end_associated_tasks_actions=[end_associated_tasks_actions],
                    event_bridge_actions=[connect.CfnRule.EventBridgeActionProperty(
                        name="name"
                    )],
                    send_notification_actions=[connect.CfnRule.SendNotificationActionProperty(
                        content="content",
                        content_type="contentType",
                        delivery_method="deliveryMethod",
                        recipient=connect.CfnRule.NotificationRecipientTypeProperty(
                            user_arns=["userArns"],
                            user_tags={
                                "user_tags_key": "userTags"
                            }
                        ),
            
                        # the properties below are optional
                        subject="subject"
                    )],
                    task_actions=[connect.CfnRule.TaskActionProperty(
                        contact_flow_arn="contactFlowArn",
                        name="name",
            
                        # the properties below are optional
                        description="description",
                        references={
                            "references_key": connect.CfnRule.ReferenceProperty(
                                type="type",
                                value="value"
                            )
                        }
                    )],
                    update_case_actions=[connect.CfnRule.UpdateCaseActionProperty(
                        fields=[connect.CfnRule.FieldProperty(
                            id="id",
                            value=connect.CfnRule.FieldValueProperty(
                                boolean_value=False,
                                double_value=123,
                                empty_value=empty_value,
                                string_value="stringValue"
                            )
                        )]
                    )]
                ),
                function="function",
                instance_arn="instanceArn",
                name="name",
                publish_status="publishStatus",
                trigger_event_source=connect.CfnRule.RuleTriggerEventSourceProperty(
                    event_source_name="eventSourceName",
            
                    # the properties below are optional
                    integration_association_arn="integrationAssociationArn"
                ),
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86228e744389fdc43748e3523fb391089cfd59a98fc3cac55a6aff07ca243441)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument function", value=function, expected_type=type_hints["function"])
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument publish_status", value=publish_status, expected_type=type_hints["publish_status"])
            check_type(argname="argument trigger_event_source", value=trigger_event_source, expected_type=type_hints["trigger_event_source"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "actions": actions,
            "function": function,
            "instance_arn": instance_arn,
            "name": name,
            "publish_status": publish_status,
            "trigger_event_source": trigger_event_source,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def actions(self) -> typing.Union[_IResolvable_da3f097b, CfnRule.ActionsProperty]:
        '''A list of actions to be run when the rule is triggered.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-rule.html#cfn-connect-rule-actions
        '''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnRule.ActionsProperty], result)

    @builtins.property
    def function(self) -> builtins.str:
        '''The conditions of the rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-rule.html#cfn-connect-rule-function
        '''
        result = self._values.get("function")
        assert result is not None, "Required property 'function' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-rule.html#cfn-connect-rule-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-rule.html#cfn-connect-rule-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publish_status(self) -> builtins.str:
        '''The publish status of the rule.

        *Allowed values* : ``DRAFT`` | ``PUBLISHED``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-rule.html#cfn-connect-rule-publishstatus
        '''
        result = self._values.get("publish_status")
        assert result is not None, "Required property 'publish_status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def trigger_event_source(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnRule.RuleTriggerEventSourceProperty]:
        '''The event source to trigger the rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-rule.html#cfn-connect-rule-triggereventsource
        '''
        result = self._values.get("trigger_event_source")
        assert result is not None, "Required property 'trigger_event_source' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnRule.RuleTriggerEventSourceProperty], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        For example, { "tags": {"key1":"value1", "key2":"value2"} }.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-rule.html#cfn-connect-rule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSecurityKey(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnSecurityKey",
):
    '''The security key for the instance.

    .. epigraph::

       Only two security keys are allowed per Amazon Connect instance.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securitykey.html
    :cloudformationResource: AWS::Connect::SecurityKey
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_security_key = connect.CfnSecurityKey(self, "MyCfnSecurityKey",
            instance_id="instanceId",
            key="key"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        instance_id: builtins.str,
        key: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_id: The Amazon Resource Name (ARN) of the instance. *Minimum* : ``1`` *Maximum* : ``100``
        :param key: A valid security key in PEM format. For example:. ``"-----BEGIN PUBLIC KEY-----\\ [a lot of characters] ----END PUBLIC KEY-----"`` *Minimum* : ``1`` *Maximum* : ``1024``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eec1c8c6bb56659ae557c882f85d373b6d643a7be8fd81d7dcb8e28a45f3d99e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSecurityKeyProps(instance_id=instance_id, key=key)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23c2e847b86bfc09195d252c47aea6a4403071968a249a46d9beca03100b5358)
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
            type_hints = typing.get_type_hints(_typecheckingstub__324830fb8488f0e9a9d62f4765f4824a32ded877f4766d2c34ea20eef4c4a506)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAssociationId")
    def attr_association_id(self) -> builtins.str:
        '''An ``AssociationId`` is automatically generated when a storage config is associated with an instance.

        :cloudformationAttribute: AssociationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssociationId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a94821c1bb0576049b170e315ebfd7632b76a9c0cbe46f78111e960033839544)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceId", value)

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        '''A valid security key in PEM format.

        For example:.
        '''
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bae1fd3a5ae97acd56284508ad71af29fda88e415500606aed041d91bc4fe256)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnSecurityKeyProps",
    jsii_struct_bases=[],
    name_mapping={"instance_id": "instanceId", "key": "key"},
)
class CfnSecurityKeyProps:
    def __init__(self, *, instance_id: builtins.str, key: builtins.str) -> None:
        '''Properties for defining a ``CfnSecurityKey``.

        :param instance_id: The Amazon Resource Name (ARN) of the instance. *Minimum* : ``1`` *Maximum* : ``100``
        :param key: A valid security key in PEM format. For example:. ``"-----BEGIN PUBLIC KEY-----\\ [a lot of characters] ----END PUBLIC KEY-----"`` *Minimum* : ``1`` *Maximum* : ``1024``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securitykey.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_security_key_props = connect.CfnSecurityKeyProps(
                instance_id="instanceId",
                key="key"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__328945501d2d11db9e341c31e7f88f7eaea8695d95d7c557b2d470e619744f5e)
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_id": instance_id,
            "key": key,
        }

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance.

        *Minimum* : ``1``

        *Maximum* : ``100``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securitykey.html#cfn-connect-securitykey-instanceid
        '''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key(self) -> builtins.str:
        '''A valid security key in PEM format. For example:.

        ``"-----BEGIN PUBLIC KEY-----\\ [a lot of characters] ----END PUBLIC KEY-----"``

        *Minimum* : ``1``

        *Maximum* : ``1024``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securitykey.html#cfn-connect-securitykey-key
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSecurityKeyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnSecurityProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnSecurityProfile",
):
    '''Creates a security profile.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securityprofile.html
    :cloudformationResource: AWS::Connect::SecurityProfile
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_security_profile = connect.CfnSecurityProfile(self, "MyCfnSecurityProfile",
            instance_arn="instanceArn",
            security_profile_name="securityProfileName",
        
            # the properties below are optional
            allowed_access_control_hierarchy_group_id="allowedAccessControlHierarchyGroupId",
            allowed_access_control_tags=[CfnTag(
                key="key",
                value="value"
            )],
            applications=[connect.CfnSecurityProfile.ApplicationProperty(
                application_permissions=["applicationPermissions"],
                namespace="namespace"
            )],
            description="description",
            hierarchy_restricted_resources=["hierarchyRestrictedResources"],
            permissions=["permissions"],
            tag_restricted_resources=["tagRestrictedResources"],
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
        instance_arn: builtins.str,
        security_profile_name: builtins.str,
        allowed_access_control_hierarchy_group_id: typing.Optional[builtins.str] = None,
        allowed_access_control_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        applications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSecurityProfile.ApplicationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        hierarchy_restricted_resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tag_restricted_resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_arn: The identifier of the Amazon Connect instance.
        :param security_profile_name: The name for the security profile.
        :param allowed_access_control_hierarchy_group_id: The identifier of the hierarchy group that a security profile uses to restrict access to resources in Amazon Connect.
        :param allowed_access_control_tags: The list of tags that a security profile uses to restrict access to resources in Amazon Connect.
        :param applications: A list of third-party applications that the security profile will give access to.
        :param description: The description of the security profile.
        :param hierarchy_restricted_resources: The list of resources that a security profile applies hierarchy restrictions to in Amazon Connect. Following are acceptable ResourceNames: ``User`` .
        :param permissions: Permissions assigned to the security profile. For a list of valid permissions, see `List of security profile permissions <https://docs.aws.amazon.com/connect/latest/adminguide/security-profile-list.html>`_ .
        :param tag_restricted_resources: The list of resources that a security profile applies tag restrictions to in Amazon Connect.
        :param tags: The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e088a4b4379aab0e18ddc67fbe352d07789383efb957a27db08764dcdee196a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSecurityProfileProps(
            instance_arn=instance_arn,
            security_profile_name=security_profile_name,
            allowed_access_control_hierarchy_group_id=allowed_access_control_hierarchy_group_id,
            allowed_access_control_tags=allowed_access_control_tags,
            applications=applications,
            description=description,
            hierarchy_restricted_resources=hierarchy_restricted_resources,
            permissions=permissions,
            tag_restricted_resources=tag_restricted_resources,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf7ea5325498e645df3e40abc7a8ec22af3f2070f980c201bde99a31fb5e9805)
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
            type_hints = typing.get_type_hints(_typecheckingstub__69dbb65308ae1fdccfd085529afb7d2cc546578e610bfdd8d165cc1e97b00616)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedRegion")
    def attr_last_modified_region(self) -> builtins.str:
        '''The AWS Region where this resource was last modified.

        :cloudformationAttribute: LastModifiedRegion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModifiedRegion"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> _IResolvable_da3f097b:
        '''The timestamp when this resource was last modified.

        :cloudformationAttribute: LastModifiedTime
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrLastModifiedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrSecurityProfileArn")
    def attr_security_profile_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the security profile.

        :cloudformationAttribute: SecurityProfileArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSecurityProfileArn"))

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
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The identifier of the Amazon Connect instance.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__087aa3bcfd02d89880b7d9764f65e87379f1aba419654d2b14f144a060eb34de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="securityProfileName")
    def security_profile_name(self) -> builtins.str:
        '''The name for the security profile.'''
        return typing.cast(builtins.str, jsii.get(self, "securityProfileName"))

    @security_profile_name.setter
    def security_profile_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c494cc473b7dcb10d47e5e6898ba1be788ee0a6eeb210dae180c62e7baffddb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityProfileName", value)

    @builtins.property
    @jsii.member(jsii_name="allowedAccessControlHierarchyGroupId")
    def allowed_access_control_hierarchy_group_id(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The identifier of the hierarchy group that a security profile uses to restrict access to resources in Amazon Connect.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allowedAccessControlHierarchyGroupId"))

    @allowed_access_control_hierarchy_group_id.setter
    def allowed_access_control_hierarchy_group_id(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b0f82dacb2707268147290732f6c1267555107e35b8b506a336b00a5f030de1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedAccessControlHierarchyGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="allowedAccessControlTags")
    def allowed_access_control_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]]:
        '''The list of tags that a security profile uses to restrict access to resources in Amazon Connect.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]], jsii.get(self, "allowedAccessControlTags"))

    @allowed_access_control_tags.setter
    def allowed_access_control_tags(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__077ab92a2b57c565722ae2a0fff7719378cf0f3194b2c2b620c43393660a0fd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedAccessControlTags", value)

    @builtins.property
    @jsii.member(jsii_name="applications")
    def applications(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSecurityProfile.ApplicationProperty"]]]]:
        '''A list of third-party applications that the security profile will give access to.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSecurityProfile.ApplicationProperty"]]]], jsii.get(self, "applications"))

    @applications.setter
    def applications(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnSecurityProfile.ApplicationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e31297c3c201035cd5629befaf1f09da3be8968c605549607b25f17835315261)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applications", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the security profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__590e303d4355b23e0035628d91db2ef4ef87c1c2276e23fdbfacd943d8c73472)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="hierarchyRestrictedResources")
    def hierarchy_restricted_resources(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of resources that a security profile applies hierarchy restrictions to in Amazon Connect.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "hierarchyRestrictedResources"))

    @hierarchy_restricted_resources.setter
    def hierarchy_restricted_resources(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22084b5a71b43e42e57329a03ca71f28eb99ce1b07c6cc58e4c267579b7c017d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hierarchyRestrictedResources", value)

    @builtins.property
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Permissions assigned to the security profile.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6057e31a0dc905719aff4c2ffcf4e2eb667ddbf01175ba8a63d9c849c1d9fc7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissions", value)

    @builtins.property
    @jsii.member(jsii_name="tagRestrictedResources")
    def tag_restricted_resources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of resources that a security profile applies tag restrictions to in Amazon Connect.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagRestrictedResources"))

    @tag_restricted_resources.setter
    def tag_restricted_resources(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c35bbd26a4cc24dc3500d939114ad0b31f11493ddfb760fb0bfb7dd5f994a7c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagRestrictedResources", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78637aba17fc3177a3492b596a6faf951a63fa4d3e768396f5b976aea7257655)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnSecurityProfile.ApplicationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "application_permissions": "applicationPermissions",
            "namespace": "namespace",
        },
    )
    class ApplicationProperty:
        def __init__(
            self,
            *,
            application_permissions: typing.Sequence[builtins.str],
            namespace: builtins.str,
        ) -> None:
            '''This API is in preview release for Amazon Connect and is subject to change.

            A third-party application's metadata.

            :param application_permissions: The permissions that the agent is granted on the application. Only the ``ACCESS`` permission is supported.
            :param namespace: Namespace of the application that you want to give access to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-securityprofile-application.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                application_property = connect.CfnSecurityProfile.ApplicationProperty(
                    application_permissions=["applicationPermissions"],
                    namespace="namespace"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b880e1a466e4d120081a7c103809b59a07385a4cee88474da2f4f00bae13c71a)
                check_type(argname="argument application_permissions", value=application_permissions, expected_type=type_hints["application_permissions"])
                check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "application_permissions": application_permissions,
                "namespace": namespace,
            }

        @builtins.property
        def application_permissions(self) -> typing.List[builtins.str]:
            '''The permissions that the agent is granted on the application.

            Only the ``ACCESS`` permission is supported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-securityprofile-application.html#cfn-connect-securityprofile-application-applicationpermissions
            '''
            result = self._values.get("application_permissions")
            assert result is not None, "Required property 'application_permissions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def namespace(self) -> builtins.str:
            '''Namespace of the application that you want to give access to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-securityprofile-application.html#cfn-connect-securityprofile-application-namespace
            '''
            result = self._values.get("namespace")
            assert result is not None, "Required property 'namespace' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnSecurityProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "security_profile_name": "securityProfileName",
        "allowed_access_control_hierarchy_group_id": "allowedAccessControlHierarchyGroupId",
        "allowed_access_control_tags": "allowedAccessControlTags",
        "applications": "applications",
        "description": "description",
        "hierarchy_restricted_resources": "hierarchyRestrictedResources",
        "permissions": "permissions",
        "tag_restricted_resources": "tagRestrictedResources",
        "tags": "tags",
    },
)
class CfnSecurityProfileProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        security_profile_name: builtins.str,
        allowed_access_control_hierarchy_group_id: typing.Optional[builtins.str] = None,
        allowed_access_control_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        applications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityProfile.ApplicationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        hierarchy_restricted_resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tag_restricted_resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSecurityProfile``.

        :param instance_arn: The identifier of the Amazon Connect instance.
        :param security_profile_name: The name for the security profile.
        :param allowed_access_control_hierarchy_group_id: The identifier of the hierarchy group that a security profile uses to restrict access to resources in Amazon Connect.
        :param allowed_access_control_tags: The list of tags that a security profile uses to restrict access to resources in Amazon Connect.
        :param applications: A list of third-party applications that the security profile will give access to.
        :param description: The description of the security profile.
        :param hierarchy_restricted_resources: The list of resources that a security profile applies hierarchy restrictions to in Amazon Connect. Following are acceptable ResourceNames: ``User`` .
        :param permissions: Permissions assigned to the security profile. For a list of valid permissions, see `List of security profile permissions <https://docs.aws.amazon.com/connect/latest/adminguide/security-profile-list.html>`_ .
        :param tag_restricted_resources: The list of resources that a security profile applies tag restrictions to in Amazon Connect.
        :param tags: The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securityprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_security_profile_props = connect.CfnSecurityProfileProps(
                instance_arn="instanceArn",
                security_profile_name="securityProfileName",
            
                # the properties below are optional
                allowed_access_control_hierarchy_group_id="allowedAccessControlHierarchyGroupId",
                allowed_access_control_tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                applications=[connect.CfnSecurityProfile.ApplicationProperty(
                    application_permissions=["applicationPermissions"],
                    namespace="namespace"
                )],
                description="description",
                hierarchy_restricted_resources=["hierarchyRestrictedResources"],
                permissions=["permissions"],
                tag_restricted_resources=["tagRestrictedResources"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a8ad9faa5e934c4966c739f0b5e3756a03460ba17b7caf0aca4e26118e04c95)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument security_profile_name", value=security_profile_name, expected_type=type_hints["security_profile_name"])
            check_type(argname="argument allowed_access_control_hierarchy_group_id", value=allowed_access_control_hierarchy_group_id, expected_type=type_hints["allowed_access_control_hierarchy_group_id"])
            check_type(argname="argument allowed_access_control_tags", value=allowed_access_control_tags, expected_type=type_hints["allowed_access_control_tags"])
            check_type(argname="argument applications", value=applications, expected_type=type_hints["applications"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument hierarchy_restricted_resources", value=hierarchy_restricted_resources, expected_type=type_hints["hierarchy_restricted_resources"])
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
            check_type(argname="argument tag_restricted_resources", value=tag_restricted_resources, expected_type=type_hints["tag_restricted_resources"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_arn": instance_arn,
            "security_profile_name": security_profile_name,
        }
        if allowed_access_control_hierarchy_group_id is not None:
            self._values["allowed_access_control_hierarchy_group_id"] = allowed_access_control_hierarchy_group_id
        if allowed_access_control_tags is not None:
            self._values["allowed_access_control_tags"] = allowed_access_control_tags
        if applications is not None:
            self._values["applications"] = applications
        if description is not None:
            self._values["description"] = description
        if hierarchy_restricted_resources is not None:
            self._values["hierarchy_restricted_resources"] = hierarchy_restricted_resources
        if permissions is not None:
            self._values["permissions"] = permissions
        if tag_restricted_resources is not None:
            self._values["tag_restricted_resources"] = tag_restricted_resources
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The identifier of the Amazon Connect instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securityprofile.html#cfn-connect-securityprofile-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_profile_name(self) -> builtins.str:
        '''The name for the security profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securityprofile.html#cfn-connect-securityprofile-securityprofilename
        '''
        result = self._values.get("security_profile_name")
        assert result is not None, "Required property 'security_profile_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_access_control_hierarchy_group_id(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The identifier of the hierarchy group that a security profile uses to restrict access to resources in Amazon Connect.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securityprofile.html#cfn-connect-securityprofile-allowedaccesscontrolhierarchygroupid
        '''
        result = self._values.get("allowed_access_control_hierarchy_group_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def allowed_access_control_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]]:
        '''The list of tags that a security profile uses to restrict access to resources in Amazon Connect.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securityprofile.html#cfn-connect-securityprofile-allowedaccesscontroltags
        '''
        result = self._values.get("allowed_access_control_tags")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]], result)

    @builtins.property
    def applications(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSecurityProfile.ApplicationProperty]]]]:
        '''A list of third-party applications that the security profile will give access to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securityprofile.html#cfn-connect-securityprofile-applications
        '''
        result = self._values.get("applications")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSecurityProfile.ApplicationProperty]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the security profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securityprofile.html#cfn-connect-securityprofile-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hierarchy_restricted_resources(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of resources that a security profile applies hierarchy restrictions to in Amazon Connect.

        Following are acceptable ResourceNames: ``User`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securityprofile.html#cfn-connect-securityprofile-hierarchyrestrictedresources
        '''
        result = self._values.get("hierarchy_restricted_resources")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def permissions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Permissions assigned to the security profile.

        For a list of valid permissions, see `List of security profile permissions <https://docs.aws.amazon.com/connect/latest/adminguide/security-profile-list.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securityprofile.html#cfn-connect-securityprofile-permissions
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tag_restricted_resources(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of resources that a security profile applies tag restrictions to in Amazon Connect.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securityprofile.html#cfn-connect-securityprofile-tagrestrictedresources
        '''
        result = self._values.get("tag_restricted_resources")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        For example, { "Tags": {"key1":"value1", "key2":"value2"} }.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-securityprofile.html#cfn-connect-securityprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSecurityProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnTaskTemplate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnTaskTemplate",
):
    '''Specifies a task template for a Amazon Connect instance.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html
    :cloudformationResource: AWS::Connect::TaskTemplate
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        # constraints: Any
        
        cfn_task_template = connect.CfnTaskTemplate(self, "MyCfnTaskTemplate",
            instance_arn="instanceArn",
        
            # the properties below are optional
            client_token="clientToken",
            constraints=constraints,
            contact_flow_arn="contactFlowArn",
            defaults=[connect.CfnTaskTemplate.DefaultFieldValueProperty(
                default_value="defaultValue",
                id=connect.CfnTaskTemplate.FieldIdentifierProperty(
                    name="name"
                )
            )],
            description="description",
            fields=[connect.CfnTaskTemplate.FieldProperty(
                id=connect.CfnTaskTemplate.FieldIdentifierProperty(
                    name="name"
                ),
                type="type",
        
                # the properties below are optional
                description="description",
                single_select_options=["singleSelectOptions"]
            )],
            name="name",
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
        instance_arn: builtins.str,
        client_token: typing.Optional[builtins.str] = None,
        constraints: typing.Any = None,
        contact_flow_arn: typing.Optional[builtins.str] = None,
        defaults: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTaskTemplate.DefaultFieldValueProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTaskTemplate.FieldProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        name: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_arn: The Amazon Resource Name (ARN) of the Amazon Connect instance.
        :param client_token: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
        :param constraints: Constraints that are applicable to the fields listed. The values can be represented in either JSON or YAML format. For an example of the JSON configuration, see *Examples* at the bottom of this page.
        :param contact_flow_arn: The Amazon Resource Name (ARN) of the flow that runs by default when a task is created by referencing this template. ``ContactFlowArn`` is not required when there is a field with ``fieldType`` = ``QUICK_CONNECT`` .
        :param defaults: The default values for fields when a task is created by referencing this template.
        :param description: The description of the task template.
        :param fields: Fields that are part of the template. A template requires at least one field that has type ``Name`` .
        :param name: The name of the task template.
        :param status: The status of the task template.
        :param tags: The tags used to organize, track, or control access for this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e55cf6106eb4919ab3d57f42477e52e40f628476ec3364c5bf5b40089c4746bc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTaskTemplateProps(
            instance_arn=instance_arn,
            client_token=client_token,
            constraints=constraints,
            contact_flow_arn=contact_flow_arn,
            defaults=defaults,
            description=description,
            fields=fields,
            name=name,
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
            type_hints = typing.get_type_hints(_typecheckingstub__46cdd562656d586fa446b953fbbb0484300c8ed5d89c5bdf38b9ee2a994cd465)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a527f307b10d7d5baa2def0fbd31d398ac1b585ebbd7f3a9ba7d38d25d6829e7)
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
        '''The Amazon Resource Name (ARN) of the task template.

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
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon Connect instance.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9540278151bed9f69d9f399c73f9a40e63e164ba823222a94733e2f75af92d07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="clientToken")
    def client_token(self) -> typing.Optional[builtins.str]:
        '''A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientToken"))

    @client_token.setter
    def client_token(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bbd2064bc52aa0f530521bac3bae9c5f12656b7d845175af66583e2c4478aff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientToken", value)

    @builtins.property
    @jsii.member(jsii_name="constraints")
    def constraints(self) -> typing.Any:
        '''Constraints that are applicable to the fields listed.'''
        return typing.cast(typing.Any, jsii.get(self, "constraints"))

    @constraints.setter
    def constraints(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a898069ebffaab98fcbaee0053da25444060ad49ffcbfe6f0368eff95f5b200)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "constraints", value)

    @builtins.property
    @jsii.member(jsii_name="contactFlowArn")
    def contact_flow_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the flow that runs by default when a task is created by referencing this template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contactFlowArn"))

    @contact_flow_arn.setter
    def contact_flow_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6b4de1aedec1ca589ae0fc007dad4a4b2bd2d8d34fc17ea98b736695f7ce943)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactFlowArn", value)

    @builtins.property
    @jsii.member(jsii_name="defaults")
    def defaults(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTaskTemplate.DefaultFieldValueProperty"]]]]:
        '''The default values for fields when a task is created by referencing this template.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTaskTemplate.DefaultFieldValueProperty"]]]], jsii.get(self, "defaults"))

    @defaults.setter
    def defaults(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTaskTemplate.DefaultFieldValueProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8763e4dc1a72bd2993b2130ce895c2796dd673f1913cef1346294ad7cdfb3f84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaults", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the task template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8feafa724c930c70f39fc9a4f2b3943981c6c26d175bdeef9ccc7a3dddb78a19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="fields")
    def fields(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTaskTemplate.FieldProperty"]]]]:
        '''Fields that are part of the template.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTaskTemplate.FieldProperty"]]]], jsii.get(self, "fields"))

    @fields.setter
    def fields(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTaskTemplate.FieldProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__445eadfb11465e7ab28af66fe2e12f9b6e2c4693cde068247ac72a5db1d0f8bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fields", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the task template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__536360af8980f014d8658d43741c6a3560607c1550e93deaec8025ead2486e33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the task template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd486363bb52c46e2e9463e955a4ed4c9ffc963b921dce5f0a41124a306b893e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__217384ce686fd8324204da16685901c284bbe5fbe2fb6c28185fac52084c57ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnTaskTemplate.ConstraintsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "invisible_fields": "invisibleFields",
            "read_only_fields": "readOnlyFields",
            "required_fields": "requiredFields",
        },
    )
    class ConstraintsProperty:
        def __init__(
            self,
            *,
            invisible_fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTaskTemplate.InvisibleFieldInfoProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            read_only_fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTaskTemplate.ReadOnlyFieldInfoProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            required_fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTaskTemplate.RequiredFieldInfoProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Describes constraints that apply to the template fields.

            :param invisible_fields: Lists the fields that are invisible to agents.
            :param read_only_fields: Lists the fields that are read-only to agents, and cannot be edited.
            :param required_fields: Lists the fields that are required to be filled by agents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-constraints.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                constraints_property = connect.CfnTaskTemplate.ConstraintsProperty(
                    invisible_fields=[connect.CfnTaskTemplate.InvisibleFieldInfoProperty(
                        id=connect.CfnTaskTemplate.FieldIdentifierProperty(
                            name="name"
                        )
                    )],
                    read_only_fields=[connect.CfnTaskTemplate.ReadOnlyFieldInfoProperty(
                        id=connect.CfnTaskTemplate.FieldIdentifierProperty(
                            name="name"
                        )
                    )],
                    required_fields=[connect.CfnTaskTemplate.RequiredFieldInfoProperty(
                        id=connect.CfnTaskTemplate.FieldIdentifierProperty(
                            name="name"
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f8ebbf1d682cf676accdf4695ae9748eb71839e0255117fb6c27fe1391e7e7cc)
                check_type(argname="argument invisible_fields", value=invisible_fields, expected_type=type_hints["invisible_fields"])
                check_type(argname="argument read_only_fields", value=read_only_fields, expected_type=type_hints["read_only_fields"])
                check_type(argname="argument required_fields", value=required_fields, expected_type=type_hints["required_fields"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if invisible_fields is not None:
                self._values["invisible_fields"] = invisible_fields
            if read_only_fields is not None:
                self._values["read_only_fields"] = read_only_fields
            if required_fields is not None:
                self._values["required_fields"] = required_fields

        @builtins.property
        def invisible_fields(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTaskTemplate.InvisibleFieldInfoProperty"]]]]:
            '''Lists the fields that are invisible to agents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-constraints.html#cfn-connect-tasktemplate-constraints-invisiblefields
            '''
            result = self._values.get("invisible_fields")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTaskTemplate.InvisibleFieldInfoProperty"]]]], result)

        @builtins.property
        def read_only_fields(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTaskTemplate.ReadOnlyFieldInfoProperty"]]]]:
            '''Lists the fields that are read-only to agents, and cannot be edited.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-constraints.html#cfn-connect-tasktemplate-constraints-readonlyfields
            '''
            result = self._values.get("read_only_fields")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTaskTemplate.ReadOnlyFieldInfoProperty"]]]], result)

        @builtins.property
        def required_fields(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTaskTemplate.RequiredFieldInfoProperty"]]]]:
            '''Lists the fields that are required to be filled by agents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-constraints.html#cfn-connect-tasktemplate-constraints-requiredfields
            '''
            result = self._values.get("required_fields")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnTaskTemplate.RequiredFieldInfoProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConstraintsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnTaskTemplate.DefaultFieldValueProperty",
        jsii_struct_bases=[],
        name_mapping={"default_value": "defaultValue", "id": "id"},
    )
    class DefaultFieldValueProperty:
        def __init__(
            self,
            *,
            default_value: builtins.str,
            id: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTaskTemplate.FieldIdentifierProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Describes a default field and its corresponding value.

            :param default_value: Default value for the field.
            :param id: Identifier of a field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-defaultfieldvalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                default_field_value_property = connect.CfnTaskTemplate.DefaultFieldValueProperty(
                    default_value="defaultValue",
                    id=connect.CfnTaskTemplate.FieldIdentifierProperty(
                        name="name"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b7e2fbafd545cd91d979ca1524a9207544758d59734dcb28e71382c3e329623f)
                check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "default_value": default_value,
                "id": id,
            }

        @builtins.property
        def default_value(self) -> builtins.str:
            '''Default value for the field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-defaultfieldvalue.html#cfn-connect-tasktemplate-defaultfieldvalue-defaultvalue
            '''
            result = self._values.get("default_value")
            assert result is not None, "Required property 'default_value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def id(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTaskTemplate.FieldIdentifierProperty"]:
            '''Identifier of a field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-defaultfieldvalue.html#cfn-connect-tasktemplate-defaultfieldvalue-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTaskTemplate.FieldIdentifierProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DefaultFieldValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnTaskTemplate.FieldIdentifierProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name"},
    )
    class FieldIdentifierProperty:
        def __init__(self, *, name: builtins.str) -> None:
            '''The identifier of the task template field.

            :param name: The name of the task template field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-fieldidentifier.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                field_identifier_property = connect.CfnTaskTemplate.FieldIdentifierProperty(
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__56cfea0cc2f28aaee625e6baeef27a54e4f0441cc4cb1502475522d9e1c29e4e)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the task template field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-fieldidentifier.html#cfn-connect-tasktemplate-fieldidentifier-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldIdentifierProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnTaskTemplate.FieldProperty",
        jsii_struct_bases=[],
        name_mapping={
            "id": "id",
            "type": "type",
            "description": "description",
            "single_select_options": "singleSelectOptions",
        },
    )
    class FieldProperty:
        def __init__(
            self,
            *,
            id: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTaskTemplate.FieldIdentifierProperty", typing.Dict[builtins.str, typing.Any]]],
            type: builtins.str,
            description: typing.Optional[builtins.str] = None,
            single_select_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Describes a single task template field.

            :param id: The unique identifier for the field.
            :param type: Indicates the type of field. Following are the valid field types: ``NAME`` ``DESCRIPTION`` | ``SCHEDULED_TIME`` | ``QUICK_CONNECT`` | ``URL`` | ``NUMBER`` | ``TEXT`` | ``TEXT_AREA`` | ``DATE_TIME`` | ``BOOLEAN`` | ``SINGLE_SELECT`` | ``EMAIL``
            :param description: The description of the field.
            :param single_select_options: A list of options for a single select field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-field.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                field_property = connect.CfnTaskTemplate.FieldProperty(
                    id=connect.CfnTaskTemplate.FieldIdentifierProperty(
                        name="name"
                    ),
                    type="type",
                
                    # the properties below are optional
                    description="description",
                    single_select_options=["singleSelectOptions"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7d065a4a87520f8d3b9711b85f794e75a7c06a4b21d323c419a06f25c134bcaf)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument single_select_options", value=single_select_options, expected_type=type_hints["single_select_options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
                "type": type,
            }
            if description is not None:
                self._values["description"] = description
            if single_select_options is not None:
                self._values["single_select_options"] = single_select_options

        @builtins.property
        def id(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTaskTemplate.FieldIdentifierProperty"]:
            '''The unique identifier for the field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-field.html#cfn-connect-tasktemplate-field-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTaskTemplate.FieldIdentifierProperty"], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''Indicates the type of field.

            Following are the valid field types: ``NAME`` ``DESCRIPTION`` | ``SCHEDULED_TIME`` | ``QUICK_CONNECT`` | ``URL`` | ``NUMBER`` | ``TEXT`` | ``TEXT_AREA`` | ``DATE_TIME`` | ``BOOLEAN`` | ``SINGLE_SELECT`` | ``EMAIL``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-field.html#cfn-connect-tasktemplate-field-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description of the field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-field.html#cfn-connect-tasktemplate-field-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def single_select_options(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of options for a single select field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-field.html#cfn-connect-tasktemplate-field-singleselectoptions
            '''
            result = self._values.get("single_select_options")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnTaskTemplate.InvisibleFieldInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id"},
    )
    class InvisibleFieldInfoProperty:
        def __init__(
            self,
            *,
            id: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTaskTemplate.FieldIdentifierProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A field that is invisible to an agent.

            :param id: Identifier of the invisible field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-invisiblefieldinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                invisible_field_info_property = connect.CfnTaskTemplate.InvisibleFieldInfoProperty(
                    id=connect.CfnTaskTemplate.FieldIdentifierProperty(
                        name="name"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4d784f103d652729901e9c8a241de453a38a7535564f57cdea8070b407515bff)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
            }

        @builtins.property
        def id(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTaskTemplate.FieldIdentifierProperty"]:
            '''Identifier of the invisible field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-invisiblefieldinfo.html#cfn-connect-tasktemplate-invisiblefieldinfo-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTaskTemplate.FieldIdentifierProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InvisibleFieldInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnTaskTemplate.ReadOnlyFieldInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id"},
    )
    class ReadOnlyFieldInfoProperty:
        def __init__(
            self,
            *,
            id: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTaskTemplate.FieldIdentifierProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Indicates a field that is read-only to an agent.

            :param id: Identifier of the read-only field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-readonlyfieldinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                read_only_field_info_property = connect.CfnTaskTemplate.ReadOnlyFieldInfoProperty(
                    id=connect.CfnTaskTemplate.FieldIdentifierProperty(
                        name="name"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f99f25935a58d0e69a63e663c70e9233ab3f544824e97f26f01abba7a02906b9)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
            }

        @builtins.property
        def id(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTaskTemplate.FieldIdentifierProperty"]:
            '''Identifier of the read-only field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-readonlyfieldinfo.html#cfn-connect-tasktemplate-readonlyfieldinfo-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTaskTemplate.FieldIdentifierProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReadOnlyFieldInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnTaskTemplate.RequiredFieldInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id"},
    )
    class RequiredFieldInfoProperty:
        def __init__(
            self,
            *,
            id: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTaskTemplate.FieldIdentifierProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Information about a required field.

            :param id: The unique identifier for the field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-requiredfieldinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                required_field_info_property = connect.CfnTaskTemplate.RequiredFieldInfoProperty(
                    id=connect.CfnTaskTemplate.FieldIdentifierProperty(
                        name="name"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__04c2c12eb06cef0a8d595c1a918e7fea99c1d59c019fe5a92fb573ffc0dd280d)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
            }

        @builtins.property
        def id(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnTaskTemplate.FieldIdentifierProperty"]:
            '''The unique identifier for the field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-tasktemplate-requiredfieldinfo.html#cfn-connect-tasktemplate-requiredfieldinfo-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTaskTemplate.FieldIdentifierProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RequiredFieldInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnTaskTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "client_token": "clientToken",
        "constraints": "constraints",
        "contact_flow_arn": "contactFlowArn",
        "defaults": "defaults",
        "description": "description",
        "fields": "fields",
        "name": "name",
        "status": "status",
        "tags": "tags",
    },
)
class CfnTaskTemplateProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        client_token: typing.Optional[builtins.str] = None,
        constraints: typing.Any = None,
        contact_flow_arn: typing.Optional[builtins.str] = None,
        defaults: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTaskTemplate.DefaultFieldValueProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTaskTemplate.FieldProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        name: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTaskTemplate``.

        :param instance_arn: The Amazon Resource Name (ARN) of the Amazon Connect instance.
        :param client_token: A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
        :param constraints: Constraints that are applicable to the fields listed. The values can be represented in either JSON or YAML format. For an example of the JSON configuration, see *Examples* at the bottom of this page.
        :param contact_flow_arn: The Amazon Resource Name (ARN) of the flow that runs by default when a task is created by referencing this template. ``ContactFlowArn`` is not required when there is a field with ``fieldType`` = ``QUICK_CONNECT`` .
        :param defaults: The default values for fields when a task is created by referencing this template.
        :param description: The description of the task template.
        :param fields: Fields that are part of the template. A template requires at least one field that has type ``Name`` .
        :param name: The name of the task template.
        :param status: The status of the task template.
        :param tags: The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            # constraints: Any
            
            cfn_task_template_props = connect.CfnTaskTemplateProps(
                instance_arn="instanceArn",
            
                # the properties below are optional
                client_token="clientToken",
                constraints=constraints,
                contact_flow_arn="contactFlowArn",
                defaults=[connect.CfnTaskTemplate.DefaultFieldValueProperty(
                    default_value="defaultValue",
                    id=connect.CfnTaskTemplate.FieldIdentifierProperty(
                        name="name"
                    )
                )],
                description="description",
                fields=[connect.CfnTaskTemplate.FieldProperty(
                    id=connect.CfnTaskTemplate.FieldIdentifierProperty(
                        name="name"
                    ),
                    type="type",
            
                    # the properties below are optional
                    description="description",
                    single_select_options=["singleSelectOptions"]
                )],
                name="name",
                status="status",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffa2d0f88c266e5f2522dfd1af262def0d3061b82ebb529283e7afc28ef8b7bb)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument client_token", value=client_token, expected_type=type_hints["client_token"])
            check_type(argname="argument constraints", value=constraints, expected_type=type_hints["constraints"])
            check_type(argname="argument contact_flow_arn", value=contact_flow_arn, expected_type=type_hints["contact_flow_arn"])
            check_type(argname="argument defaults", value=defaults, expected_type=type_hints["defaults"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument fields", value=fields, expected_type=type_hints["fields"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_arn": instance_arn,
        }
        if client_token is not None:
            self._values["client_token"] = client_token
        if constraints is not None:
            self._values["constraints"] = constraints
        if contact_flow_arn is not None:
            self._values["contact_flow_arn"] = contact_flow_arn
        if defaults is not None:
            self._values["defaults"] = defaults
        if description is not None:
            self._values["description"] = description
        if fields is not None:
            self._values["fields"] = fields
        if name is not None:
            self._values["name"] = name
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon Connect instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_token(self) -> typing.Optional[builtins.str]:
        '''A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-clienttoken
        '''
        result = self._values.get("client_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def constraints(self) -> typing.Any:
        '''Constraints that are applicable to the fields listed.

        The values can be represented in either JSON or YAML format. For an example of the JSON configuration, see *Examples* at the bottom of this page.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-constraints
        '''
        result = self._values.get("constraints")
        return typing.cast(typing.Any, result)

    @builtins.property
    def contact_flow_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the flow that runs by default when a task is created by referencing this template.

        ``ContactFlowArn`` is not required when there is a field with ``fieldType`` = ``QUICK_CONNECT`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-contactflowarn
        '''
        result = self._values.get("contact_flow_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def defaults(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTaskTemplate.DefaultFieldValueProperty]]]]:
        '''The default values for fields when a task is created by referencing this template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-defaults
        '''
        result = self._values.get("defaults")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTaskTemplate.DefaultFieldValueProperty]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the task template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fields(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTaskTemplate.FieldProperty]]]]:
        '''Fields that are part of the template.

        A template requires at least one field that has type ``Name`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-fields
        '''
        result = self._values.get("fields")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTaskTemplate.FieldProperty]]]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the task template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the task template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-tasktemplate.html#cfn-connect-tasktemplate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTaskTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnTrafficDistributionGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnTrafficDistributionGroup",
):
    '''Information about a traffic distribution group.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-trafficdistributiongroup.html
    :cloudformationResource: AWS::Connect::TrafficDistributionGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_traffic_distribution_group = connect.CfnTrafficDistributionGroup(self, "MyCfnTrafficDistributionGroup",
            instance_arn="instanceArn",
            name="name",
        
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
        id: builtins.str,
        *,
        instance_arn: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_arn: The Amazon Resource Name (ARN).
        :param name: The name of the traffic distribution group.
        :param description: The description of the traffic distribution group.
        :param tags: The tags used to organize, track, or control access for this resource. For example, {"tags": {"key1":"value1", "key2":"value2"} }.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca487c7b5364a4f5551b0a2850374d278ea9b277effd6a5a44ae511b77c2a5a6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTrafficDistributionGroupProps(
            instance_arn=instance_arn, name=name, description=description, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4f6c13df7129e219cbf36228095876149e60b246cf354ab6fe83b9652428171)
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
            type_hints = typing.get_type_hints(_typecheckingstub__56435f5b52b8efc49bb468ce5e0a5186a2a9b25811e4c4afdcec0fc162bc4d8a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrIsDefault")
    def attr_is_default(self) -> _IResolvable_da3f097b:
        '''Describes whether this is the default traffic distribution group.

        :cloudformationAttribute: IsDefault
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrIsDefault"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the traffic distribution group.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrTrafficDistributionGroupArn")
    def attr_traffic_distribution_group_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the traffic distribution group.

        :cloudformationAttribute: TrafficDistributionGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTrafficDistributionGroupArn"))

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
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN).'''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__690e0c359cfbbb997d8caca7bbd988977f9ed96a29fcc7e76700b71ccfdbd3d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the traffic distribution group.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05f7e41c371bdd41842327789f2f3c741a118f7cd054f968517e0e9194f92a8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the traffic distribution group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90cd95785072e927554dbc62f58aa26e2908aa348f84906a5179c37696b83bc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d10b0c268d645112c426bfa20ffc2365e5a9d7fb89c5ef9a7288bd68b8772881)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnTrafficDistributionGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "name": "name",
        "description": "description",
        "tags": "tags",
    },
)
class CfnTrafficDistributionGroupProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTrafficDistributionGroup``.

        :param instance_arn: The Amazon Resource Name (ARN).
        :param name: The name of the traffic distribution group.
        :param description: The description of the traffic distribution group.
        :param tags: The tags used to organize, track, or control access for this resource. For example, {"tags": {"key1":"value1", "key2":"value2"} }.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-trafficdistributiongroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_traffic_distribution_group_props = connect.CfnTrafficDistributionGroupProps(
                instance_arn="instanceArn",
                name="name",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__399ed170d743f73906db5f85382e2ff094eded44d1c9ecad71243420bd137725)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_arn": instance_arn,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-trafficdistributiongroup.html#cfn-connect-trafficdistributiongroup-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the traffic distribution group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-trafficdistributiongroup.html#cfn-connect-trafficdistributiongroup-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the traffic distribution group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-trafficdistributiongroup.html#cfn-connect-trafficdistributiongroup-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for this resource.

        For example, {"tags": {"key1":"value1", "key2":"value2"} }.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-trafficdistributiongroup.html#cfn-connect-trafficdistributiongroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTrafficDistributionGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnUser(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnUser",
):
    '''Specifies a user account for an Amazon Connect instance.

    For information about how to create user accounts using the Amazon Connect console, see `Add Users <https://docs.aws.amazon.com/connect/latest/adminguide/user-management.html>`_ in the *Amazon Connect Administrator Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html
    :cloudformationResource: AWS::Connect::User
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_user = connect.CfnUser(self, "MyCfnUser",
            instance_arn="instanceArn",
            phone_config=connect.CfnUser.UserPhoneConfigProperty(
                phone_type="phoneType",
        
                # the properties below are optional
                after_contact_work_time_limit=123,
                auto_accept=False,
                desk_phone_number="deskPhoneNumber"
            ),
            routing_profile_arn="routingProfileArn",
            security_profile_arns=["securityProfileArns"],
            username="username",
        
            # the properties below are optional
            directory_user_id="directoryUserId",
            hierarchy_group_arn="hierarchyGroupArn",
            identity_info=connect.CfnUser.UserIdentityInfoProperty(
                email="email",
                first_name="firstName",
                last_name="lastName",
                mobile="mobile",
                secondary_email="secondaryEmail"
            ),
            password="password",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            user_proficiencies=[connect.CfnUser.UserProficiencyProperty(
                attribute_name="attributeName",
                attribute_value="attributeValue",
                level=123
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        instance_arn: builtins.str,
        phone_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnUser.UserPhoneConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        routing_profile_arn: builtins.str,
        security_profile_arns: typing.Sequence[builtins.str],
        username: builtins.str,
        directory_user_id: typing.Optional[builtins.str] = None,
        hierarchy_group_arn: typing.Optional[builtins.str] = None,
        identity_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnUser.UserIdentityInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        password: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        user_proficiencies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnUser.UserProficiencyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_arn: The Amazon Resource Name (ARN) of the instance.
        :param phone_config: Information about the phone configuration for the user.
        :param routing_profile_arn: The Amazon Resource Name (ARN) of the user's routing profile.
        :param security_profile_arns: The Amazon Resource Name (ARN) of the user's security profile.
        :param username: The user name assigned to the user account.
        :param directory_user_id: The identifier of the user account in the directory used for identity management.
        :param hierarchy_group_arn: The Amazon Resource Name (ARN) of the user's hierarchy group.
        :param identity_info: Information about the user identity.
        :param password: The user's password.
        :param tags: The tags.
        :param user_proficiencies: One or more predefined attributes assigned to a user, with a numeric value that indicates how their level of skill in a specified area.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05b3c171d418de057737855a6729454df2138450ce49f656f47804ab286addf6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnUserProps(
            instance_arn=instance_arn,
            phone_config=phone_config,
            routing_profile_arn=routing_profile_arn,
            security_profile_arns=security_profile_arns,
            username=username,
            directory_user_id=directory_user_id,
            hierarchy_group_arn=hierarchy_group_arn,
            identity_info=identity_info,
            password=password,
            tags=tags,
            user_proficiencies=user_proficiencies,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__868e9d73ebd6da6bc01f1a454c28b6ce77bb38b7722cc539dee5d631af8ab7a1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a8a7ab4c4c68abf101e561bdcaa3fccf82a51680bd75b6060ffd85b7b39cee53)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrUserArn")
    def attr_user_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the user.

        :cloudformationAttribute: UserArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUserArn"))

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
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f39c63e5bec20724a75b863eaf92b750aa2b43e84007f59f8101f109aded4b62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="phoneConfig")
    def phone_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnUser.UserPhoneConfigProperty"]:
        '''Information about the phone configuration for the user.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnUser.UserPhoneConfigProperty"], jsii.get(self, "phoneConfig"))

    @phone_config.setter
    def phone_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnUser.UserPhoneConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f182c7afc61ebf14606fef1a70e2527bc3c149561eed985aa3c521e419741e73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "phoneConfig", value)

    @builtins.property
    @jsii.member(jsii_name="routingProfileArn")
    def routing_profile_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the user's routing profile.'''
        return typing.cast(builtins.str, jsii.get(self, "routingProfileArn"))

    @routing_profile_arn.setter
    def routing_profile_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53ec4c5274e442b13ba6263b0a0699bceadb2d594cb4553cf3256514da5ba718)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routingProfileArn", value)

    @builtins.property
    @jsii.member(jsii_name="securityProfileArns")
    def security_profile_arns(self) -> typing.List[builtins.str]:
        '''The Amazon Resource Name (ARN) of the user's security profile.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityProfileArns"))

    @security_profile_arns.setter
    def security_profile_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f59f37aa37416b07a1920b9fb28c6db10aa7091b532298ff46eddb3200c94afd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityProfileArns", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        '''The user name assigned to the user account.'''
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0d3c1f0374209b5f9480c6b6571b89c26495747acd0440d47b7b3d3a95f28f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="directoryUserId")
    def directory_user_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the user account in the directory used for identity management.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryUserId"))

    @directory_user_id.setter
    def directory_user_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f09389f8f59128c5950972d770de7815f263ca9cf4c25735591417ea4b72939)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryUserId", value)

    @builtins.property
    @jsii.member(jsii_name="hierarchyGroupArn")
    def hierarchy_group_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the user's hierarchy group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hierarchyGroupArn"))

    @hierarchy_group_arn.setter
    def hierarchy_group_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f855d98db219c907988e531c32926bf279294c9a15359f1bf876ac28120857f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hierarchyGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="identityInfo")
    def identity_info(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnUser.UserIdentityInfoProperty"]]:
        '''Information about the user identity.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnUser.UserIdentityInfoProperty"]], jsii.get(self, "identityInfo"))

    @identity_info.setter
    def identity_info(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnUser.UserIdentityInfoProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01c0b838f75f47cfedc3da42d9842c603514aa585b6a8bdfd39ab14e8a57d5ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityInfo", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        '''The user's password.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97a2c5140ffd2e76246aa4b882ace6caee9e3c89751b5c2dc0c27a7d20caf26d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e4428cb05b6e362886b1adc91882b21e8cb39137a29037b9728d57b3a622dbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="userProficiencies")
    def user_proficiencies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnUser.UserProficiencyProperty"]]]]:
        '''One or more predefined attributes assigned to a user, with a numeric value that indicates how their level of skill in a specified area.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnUser.UserProficiencyProperty"]]]], jsii.get(self, "userProficiencies"))

    @user_proficiencies.setter
    def user_proficiencies(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnUser.UserProficiencyProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18a40ddd47b7e62a1ca5a21d2261e587a5eca592d22947adb5caefa3724093e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userProficiencies", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnUser.UserIdentityInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "email": "email",
            "first_name": "firstName",
            "last_name": "lastName",
            "mobile": "mobile",
            "secondary_email": "secondaryEmail",
        },
    )
    class UserIdentityInfoProperty:
        def __init__(
            self,
            *,
            email: typing.Optional[builtins.str] = None,
            first_name: typing.Optional[builtins.str] = None,
            last_name: typing.Optional[builtins.str] = None,
            mobile: typing.Optional[builtins.str] = None,
            secondary_email: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about the identity of a user.

            .. epigraph::

               For Amazon Connect instances that are created with the ``EXISTING_DIRECTORY`` identity management type, ``FirstName`` , ``LastName`` , and ``Email`` cannot be updated from within Amazon Connect because they are managed by the directory.

            :param email: The email address. If you are using SAML for identity management and include this parameter, an error is returned.
            :param first_name: The first name. This is required if you are using Amazon Connect or SAML for identity management.
            :param last_name: The last name. This is required if you are using Amazon Connect or SAML for identity management.
            :param mobile: The user's mobile number.
            :param secondary_email: The user's secondary email address. If you provide a secondary email, the user receives email notifications -- other than password reset notifications -- to this email address instead of to their primary email address. *Pattern* : ``(?=^.{0,265}$)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,63}``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-useridentityinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                user_identity_info_property = connect.CfnUser.UserIdentityInfoProperty(
                    email="email",
                    first_name="firstName",
                    last_name="lastName",
                    mobile="mobile",
                    secondary_email="secondaryEmail"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__675484167c56516574409f5f87a82bc61f2bd18d297494deb996e1e0a0c63262)
                check_type(argname="argument email", value=email, expected_type=type_hints["email"])
                check_type(argname="argument first_name", value=first_name, expected_type=type_hints["first_name"])
                check_type(argname="argument last_name", value=last_name, expected_type=type_hints["last_name"])
                check_type(argname="argument mobile", value=mobile, expected_type=type_hints["mobile"])
                check_type(argname="argument secondary_email", value=secondary_email, expected_type=type_hints["secondary_email"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if email is not None:
                self._values["email"] = email
            if first_name is not None:
                self._values["first_name"] = first_name
            if last_name is not None:
                self._values["last_name"] = last_name
            if mobile is not None:
                self._values["mobile"] = mobile
            if secondary_email is not None:
                self._values["secondary_email"] = secondary_email

        @builtins.property
        def email(self) -> typing.Optional[builtins.str]:
            '''The email address.

            If you are using SAML for identity management and include this parameter, an error is returned.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-useridentityinfo.html#cfn-connect-user-useridentityinfo-email
            '''
            result = self._values.get("email")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def first_name(self) -> typing.Optional[builtins.str]:
            '''The first name.

            This is required if you are using Amazon Connect or SAML for identity management.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-useridentityinfo.html#cfn-connect-user-useridentityinfo-firstname
            '''
            result = self._values.get("first_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def last_name(self) -> typing.Optional[builtins.str]:
            '''The last name.

            This is required if you are using Amazon Connect or SAML for identity management.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-useridentityinfo.html#cfn-connect-user-useridentityinfo-lastname
            '''
            result = self._values.get("last_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mobile(self) -> typing.Optional[builtins.str]:
            '''The user's mobile number.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-useridentityinfo.html#cfn-connect-user-useridentityinfo-mobile
            '''
            result = self._values.get("mobile")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secondary_email(self) -> typing.Optional[builtins.str]:
            '''The user's secondary email address.

            If you provide a secondary email, the user receives email notifications -- other than password reset notifications -- to this email address instead of to their primary email address.

            *Pattern* : ``(?=^.{0,265}$)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,63}``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-useridentityinfo.html#cfn-connect-user-useridentityinfo-secondaryemail
            '''
            result = self._values.get("secondary_email")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserIdentityInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnUser.UserPhoneConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "phone_type": "phoneType",
            "after_contact_work_time_limit": "afterContactWorkTimeLimit",
            "auto_accept": "autoAccept",
            "desk_phone_number": "deskPhoneNumber",
        },
    )
    class UserPhoneConfigProperty:
        def __init__(
            self,
            *,
            phone_type: builtins.str,
            after_contact_work_time_limit: typing.Optional[jsii.Number] = None,
            auto_accept: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            desk_phone_number: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about the phone configuration settings for a user.

            :param phone_type: The phone type.
            :param after_contact_work_time_limit: The After Call Work (ACW) timeout setting, in seconds. This parameter has a minimum value of 0 and a maximum value of 2,000,000 seconds (24 days). Enter 0 if you don't want to allocate a specific amount of ACW time. It essentially means an indefinite amount of time. When the conversation ends, ACW starts; the agent must choose Close contact to end ACW. .. epigraph:: When returned by a ``SearchUsers`` call, ``AfterContactWorkTimeLimit`` is returned in milliseconds.
            :param auto_accept: The Auto accept setting.
            :param desk_phone_number: The phone number for the user's desk phone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userphoneconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                user_phone_config_property = connect.CfnUser.UserPhoneConfigProperty(
                    phone_type="phoneType",
                
                    # the properties below are optional
                    after_contact_work_time_limit=123,
                    auto_accept=False,
                    desk_phone_number="deskPhoneNumber"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e774e2d87fa8144ee9994624937d62ce4393d565b8e6982f7d2e1c5bf0c9ca67)
                check_type(argname="argument phone_type", value=phone_type, expected_type=type_hints["phone_type"])
                check_type(argname="argument after_contact_work_time_limit", value=after_contact_work_time_limit, expected_type=type_hints["after_contact_work_time_limit"])
                check_type(argname="argument auto_accept", value=auto_accept, expected_type=type_hints["auto_accept"])
                check_type(argname="argument desk_phone_number", value=desk_phone_number, expected_type=type_hints["desk_phone_number"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "phone_type": phone_type,
            }
            if after_contact_work_time_limit is not None:
                self._values["after_contact_work_time_limit"] = after_contact_work_time_limit
            if auto_accept is not None:
                self._values["auto_accept"] = auto_accept
            if desk_phone_number is not None:
                self._values["desk_phone_number"] = desk_phone_number

        @builtins.property
        def phone_type(self) -> builtins.str:
            '''The phone type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userphoneconfig.html#cfn-connect-user-userphoneconfig-phonetype
            '''
            result = self._values.get("phone_type")
            assert result is not None, "Required property 'phone_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def after_contact_work_time_limit(self) -> typing.Optional[jsii.Number]:
            '''The After Call Work (ACW) timeout setting, in seconds.

            This parameter has a minimum value of 0 and a maximum value of 2,000,000 seconds (24 days). Enter 0 if you don't want to allocate a specific amount of ACW time. It essentially means an indefinite amount of time. When the conversation ends, ACW starts; the agent must choose Close contact to end ACW.
            .. epigraph::

               When returned by a ``SearchUsers`` call, ``AfterContactWorkTimeLimit`` is returned in milliseconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userphoneconfig.html#cfn-connect-user-userphoneconfig-aftercontactworktimelimit
            '''
            result = self._values.get("after_contact_work_time_limit")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def auto_accept(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The Auto accept setting.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userphoneconfig.html#cfn-connect-user-userphoneconfig-autoaccept
            '''
            result = self._values.get("auto_accept")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def desk_phone_number(self) -> typing.Optional[builtins.str]:
            '''The phone number for the user's desk phone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userphoneconfig.html#cfn-connect-user-userphoneconfig-deskphonenumber
            '''
            result = self._values.get("desk_phone_number")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserPhoneConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_connect.CfnUser.UserProficiencyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attribute_name": "attributeName",
            "attribute_value": "attributeValue",
            "level": "level",
        },
    )
    class UserProficiencyProperty:
        def __init__(
            self,
            *,
            attribute_name: builtins.str,
            attribute_value: builtins.str,
            level: jsii.Number,
        ) -> None:
            '''.. epigraph::

   A predefined attribute must be created before using ``UserProficiencies`` in the Cloudformation *User* template.

            For more information, see `Predefined attributes <https://docs.aws.amazon.com/connect/latest/adminguide/predefined-attributes.html>`_ .

            Proficiency of a user.

            :param attribute_name: The name of user’s proficiency. You must use a predefined attribute name that is present in the Amazon Connect instance.
            :param attribute_value: The value of user’s proficiency. You must use a predefined attribute value that is present in the Amazon Connect instance.
            :param level: The level of the proficiency. The valid values are 1, 2, 3, 4 and 5.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userproficiency.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_connect as connect
                
                user_proficiency_property = connect.CfnUser.UserProficiencyProperty(
                    attribute_name="attributeName",
                    attribute_value="attributeValue",
                    level=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__345901e38de5207bac37cf2e70717ae293249c5093817f351ddab16523ebf96a)
                check_type(argname="argument attribute_name", value=attribute_name, expected_type=type_hints["attribute_name"])
                check_type(argname="argument attribute_value", value=attribute_value, expected_type=type_hints["attribute_value"])
                check_type(argname="argument level", value=level, expected_type=type_hints["level"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "attribute_name": attribute_name,
                "attribute_value": attribute_value,
                "level": level,
            }

        @builtins.property
        def attribute_name(self) -> builtins.str:
            '''The name of user’s proficiency.

            You must use a predefined attribute name that is present in the Amazon Connect instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userproficiency.html#cfn-connect-user-userproficiency-attributename
            '''
            result = self._values.get("attribute_name")
            assert result is not None, "Required property 'attribute_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def attribute_value(self) -> builtins.str:
            '''The value of user’s proficiency.

            You must use a predefined attribute value that is present in the Amazon Connect instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userproficiency.html#cfn-connect-user-userproficiency-attributevalue
            '''
            result = self._values.get("attribute_value")
            assert result is not None, "Required property 'attribute_value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def level(self) -> jsii.Number:
            '''The level of the proficiency.

            The valid values are 1, 2, 3, 4 and 5.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-connect-user-userproficiency.html#cfn-connect-user-userproficiency-level
            '''
            result = self._values.get("level")
            assert result is not None, "Required property 'level' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserProficiencyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnUserHierarchyGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnUserHierarchyGroup",
):
    '''Specifies a new user hierarchy group.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html
    :cloudformationResource: AWS::Connect::UserHierarchyGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_user_hierarchy_group = connect.CfnUserHierarchyGroup(self, "MyCfnUserHierarchyGroup",
            instance_arn="instanceArn",
            name="name",
        
            # the properties below are optional
            parent_group_arn="parentGroupArn",
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
        instance_arn: builtins.str,
        name: builtins.str,
        parent_group_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_arn: The Amazon Resource Name (ARN) of the user hierarchy group.
        :param name: The name of the user hierarchy group.
        :param parent_group_arn: The Amazon Resource Name (ARN) of the parent group.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ee71292692b3a4ed0bb1ecb030ac42cd8de9fe7fd30c25bca5b2f1eaaa6bb48)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnUserHierarchyGroupProps(
            instance_arn=instance_arn,
            name=name,
            parent_group_arn=parent_group_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__752f8fce7f90c25285d3743bf24f50aec111d37047ee0c4af63a38e966735a03)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ac67c3ecd95bbbc55bc130d457e245f00decbc275854bb8b407db1329f860025)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrUserHierarchyGroupArn")
    def attr_user_hierarchy_group_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the user hierarchy group.

        :cloudformationAttribute: UserHierarchyGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUserHierarchyGroupArn"))

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
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the user hierarchy group.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8fb77dfbead9199eb5f47ecaa078f50ea02c5ce873fd226cd349a59b527fb3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the user hierarchy group.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d0815b3361eabab5affbe2f0e2d26f64eecd0bba911c06147e98f374796565c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parentGroupArn")
    def parent_group_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the parent group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentGroupArn"))

    @parent_group_arn.setter
    def parent_group_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec2be8f8330a2a7250df106f290a4e8ddeda8715a95a83b481ae76d8ac2d2d8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parentGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d964880cee57a50d651477affc39220cab9a8575f6e5da757f56a627d3121f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnUserHierarchyGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "name": "name",
        "parent_group_arn": "parentGroupArn",
        "tags": "tags",
    },
)
class CfnUserHierarchyGroupProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        name: builtins.str,
        parent_group_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnUserHierarchyGroup``.

        :param instance_arn: The Amazon Resource Name (ARN) of the user hierarchy group.
        :param name: The name of the user hierarchy group.
        :param parent_group_arn: The Amazon Resource Name (ARN) of the parent group.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_user_hierarchy_group_props = connect.CfnUserHierarchyGroupProps(
                instance_arn="instanceArn",
                name="name",
            
                # the properties below are optional
                parent_group_arn="parentGroupArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51f9a797f445ffc1deaff140a69a030bdb25f3fa135ef233a56621cf7d99867c)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parent_group_arn", value=parent_group_arn, expected_type=type_hints["parent_group_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_arn": instance_arn,
            "name": name,
        }
        if parent_group_arn is not None:
            self._values["parent_group_arn"] = parent_group_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the user hierarchy group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html#cfn-connect-userhierarchygroup-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the user hierarchy group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html#cfn-connect-userhierarchygroup-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parent_group_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the parent group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html#cfn-connect-userhierarchygroup-parentgrouparn
        '''
        result = self._values.get("parent_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-userhierarchygroup.html#cfn-connect-userhierarchygroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserHierarchyGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnUserProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "phone_config": "phoneConfig",
        "routing_profile_arn": "routingProfileArn",
        "security_profile_arns": "securityProfileArns",
        "username": "username",
        "directory_user_id": "directoryUserId",
        "hierarchy_group_arn": "hierarchyGroupArn",
        "identity_info": "identityInfo",
        "password": "password",
        "tags": "tags",
        "user_proficiencies": "userProficiencies",
    },
)
class CfnUserProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        phone_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnUser.UserPhoneConfigProperty, typing.Dict[builtins.str, typing.Any]]],
        routing_profile_arn: builtins.str,
        security_profile_arns: typing.Sequence[builtins.str],
        username: builtins.str,
        directory_user_id: typing.Optional[builtins.str] = None,
        hierarchy_group_arn: typing.Optional[builtins.str] = None,
        identity_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUser.UserIdentityInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        password: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        user_proficiencies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUser.UserProficiencyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnUser``.

        :param instance_arn: The Amazon Resource Name (ARN) of the instance.
        :param phone_config: Information about the phone configuration for the user.
        :param routing_profile_arn: The Amazon Resource Name (ARN) of the user's routing profile.
        :param security_profile_arns: The Amazon Resource Name (ARN) of the user's security profile.
        :param username: The user name assigned to the user account.
        :param directory_user_id: The identifier of the user account in the directory used for identity management.
        :param hierarchy_group_arn: The Amazon Resource Name (ARN) of the user's hierarchy group.
        :param identity_info: Information about the user identity.
        :param password: The user's password.
        :param tags: The tags.
        :param user_proficiencies: One or more predefined attributes assigned to a user, with a numeric value that indicates how their level of skill in a specified area.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_user_props = connect.CfnUserProps(
                instance_arn="instanceArn",
                phone_config=connect.CfnUser.UserPhoneConfigProperty(
                    phone_type="phoneType",
            
                    # the properties below are optional
                    after_contact_work_time_limit=123,
                    auto_accept=False,
                    desk_phone_number="deskPhoneNumber"
                ),
                routing_profile_arn="routingProfileArn",
                security_profile_arns=["securityProfileArns"],
                username="username",
            
                # the properties below are optional
                directory_user_id="directoryUserId",
                hierarchy_group_arn="hierarchyGroupArn",
                identity_info=connect.CfnUser.UserIdentityInfoProperty(
                    email="email",
                    first_name="firstName",
                    last_name="lastName",
                    mobile="mobile",
                    secondary_email="secondaryEmail"
                ),
                password="password",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                user_proficiencies=[connect.CfnUser.UserProficiencyProperty(
                    attribute_name="attributeName",
                    attribute_value="attributeValue",
                    level=123
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__494987ef0f9b905c50c1efbd53f96fb396b7f25b5354dfbb4027a32dbf61b9b1)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument phone_config", value=phone_config, expected_type=type_hints["phone_config"])
            check_type(argname="argument routing_profile_arn", value=routing_profile_arn, expected_type=type_hints["routing_profile_arn"])
            check_type(argname="argument security_profile_arns", value=security_profile_arns, expected_type=type_hints["security_profile_arns"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument directory_user_id", value=directory_user_id, expected_type=type_hints["directory_user_id"])
            check_type(argname="argument hierarchy_group_arn", value=hierarchy_group_arn, expected_type=type_hints["hierarchy_group_arn"])
            check_type(argname="argument identity_info", value=identity_info, expected_type=type_hints["identity_info"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument user_proficiencies", value=user_proficiencies, expected_type=type_hints["user_proficiencies"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_arn": instance_arn,
            "phone_config": phone_config,
            "routing_profile_arn": routing_profile_arn,
            "security_profile_arns": security_profile_arns,
            "username": username,
        }
        if directory_user_id is not None:
            self._values["directory_user_id"] = directory_user_id
        if hierarchy_group_arn is not None:
            self._values["hierarchy_group_arn"] = hierarchy_group_arn
        if identity_info is not None:
            self._values["identity_info"] = identity_info
        if password is not None:
            self._values["password"] = password
        if tags is not None:
            self._values["tags"] = tags
        if user_proficiencies is not None:
            self._values["user_proficiencies"] = user_proficiencies

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def phone_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnUser.UserPhoneConfigProperty]:
        '''Information about the phone configuration for the user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-phoneconfig
        '''
        result = self._values.get("phone_config")
        assert result is not None, "Required property 'phone_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnUser.UserPhoneConfigProperty], result)

    @builtins.property
    def routing_profile_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the user's routing profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-routingprofilearn
        '''
        result = self._values.get("routing_profile_arn")
        assert result is not None, "Required property 'routing_profile_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_profile_arns(self) -> typing.List[builtins.str]:
        '''The Amazon Resource Name (ARN) of the user's security profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-securityprofilearns
        '''
        result = self._values.get("security_profile_arns")
        assert result is not None, "Required property 'security_profile_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def username(self) -> builtins.str:
        '''The user name assigned to the user account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-username
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def directory_user_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the user account in the directory used for identity management.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-directoryuserid
        '''
        result = self._values.get("directory_user_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hierarchy_group_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the user's hierarchy group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-hierarchygrouparn
        '''
        result = self._values.get("hierarchy_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_info(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnUser.UserIdentityInfoProperty]]:
        '''Information about the user identity.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-identityinfo
        '''
        result = self._values.get("identity_info")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnUser.UserIdentityInfoProperty]], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The user's password.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-password
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def user_proficiencies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnUser.UserProficiencyProperty]]]]:
        '''One or more predefined attributes assigned to a user, with a numeric value that indicates how their level of skill in a specified area.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-user.html#cfn-connect-user-userproficiencies
        '''
        result = self._values.get("user_proficiencies")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnUser.UserProficiencyProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnView(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnView",
):
    '''Creates a customer-managed view in the published state within the specified instance.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-view.html
    :cloudformationResource: AWS::Connect::View
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        # template: Any
        
        cfn_view = connect.CfnView(self, "MyCfnView",
            actions=["actions"],
            instance_arn="instanceArn",
            name="name",
            template=template,
        
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
        id: builtins.str,
        *,
        actions: typing.Sequence[builtins.str],
        instance_arn: builtins.str,
        name: builtins.str,
        template: typing.Any,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param actions: A list of actions possible from the view.
        :param instance_arn: The Amazon Resource Name (ARN) of the instance.
        :param name: The name of the view.
        :param template: The view template representing the structure of the view.
        :param description: The description of the view.
        :param tags: The tags associated with the view resource (not specific to view version).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94b4f2f620952c31a829f98f6f735cb6b2bcb05a7aeec0d58a9bf353e42283a3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnViewProps(
            actions=actions,
            instance_arn=instance_arn,
            name=name,
            template=template,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4f4d449c39fb674cb2aee4444da15965f7a738d317d39c5795787870d91cb90)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2f51d9f515dc52e659fd588b6b7c69855667a4bcb91e66e6243fb55b7ce6e6d6)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrViewArn")
    def attr_view_arn(self) -> builtins.str:
        '''The unqualified Amazon Resource Name (ARN) of the view.

        For example:

        ``arn:<partition>:connect:<region>:<accountId>:instance/00000000-0000-0000-0000-000000000000/view/00000000-0000-0000-0000-000000000000``

        :cloudformationAttribute: ViewArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrViewArn"))

    @builtins.property
    @jsii.member(jsii_name="attrViewContentSha256")
    def attr_view_content_sha256(self) -> builtins.str:
        '''Indicates the checksum value of the latest published view content.

        :cloudformationAttribute: ViewContentSha256
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrViewContentSha256"))

    @builtins.property
    @jsii.member(jsii_name="attrViewId")
    def attr_view_id(self) -> builtins.str:
        '''The identifier of the view.

        :cloudformationAttribute: ViewId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrViewId"))

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
    @jsii.member(jsii_name="actions")
    def actions(self) -> typing.List[builtins.str]:
        '''A list of actions possible from the view.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "actions"))

    @actions.setter
    def actions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfc5249082c6d5a1446f72b2d7f603dfd56182e6160353b7c1af6ee5d04cf427)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actions", value)

    @builtins.property
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a93c4cb77702281173c334c90fe993226032e3fd88c9b905c29b88b91bf0506e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the view.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9119d3cb209dab8ae6d5b5cc8cb241d94d81d58771bb72d5e73cd8c92938990b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="template")
    def template(self) -> typing.Any:
        '''The view template representing the structure of the view.'''
        return typing.cast(typing.Any, jsii.get(self, "template"))

    @template.setter
    def template(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86e1abb3b53b3f5681b7c0d196d86154b11fafceba7b897bc6536e6d6ed70a4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "template", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the view.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4d4478679794ad5547e519ea6378b504c947ae3ba33c144dbfbd6a02f41c523)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags associated with the view resource (not specific to view version).'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c8717b700734d2f2ffa968661ed869e26cd339beb41934a1e4fb19cf006b80e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnViewProps",
    jsii_struct_bases=[],
    name_mapping={
        "actions": "actions",
        "instance_arn": "instanceArn",
        "name": "name",
        "template": "template",
        "description": "description",
        "tags": "tags",
    },
)
class CfnViewProps:
    def __init__(
        self,
        *,
        actions: typing.Sequence[builtins.str],
        instance_arn: builtins.str,
        name: builtins.str,
        template: typing.Any,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnView``.

        :param actions: A list of actions possible from the view.
        :param instance_arn: The Amazon Resource Name (ARN) of the instance.
        :param name: The name of the view.
        :param template: The view template representing the structure of the view.
        :param description: The description of the view.
        :param tags: The tags associated with the view resource (not specific to view version).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-view.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            # template: Any
            
            cfn_view_props = connect.CfnViewProps(
                actions=["actions"],
                instance_arn="instanceArn",
                name="name",
                template=template,
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f907c1817accd77cdb1d6d91c707e676a4ecb33911eb5e958e9ef56a1cda0cbd)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "actions": actions,
            "instance_arn": instance_arn,
            "name": name,
            "template": template,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def actions(self) -> typing.List[builtins.str]:
        '''A list of actions possible from the view.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-view.html#cfn-connect-view-actions
        '''
        result = self._values.get("actions")
        assert result is not None, "Required property 'actions' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-view.html#cfn-connect-view-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the view.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-view.html#cfn-connect-view-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template(self) -> typing.Any:
        '''The view template representing the structure of the view.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-view.html#cfn-connect-view-template
        '''
        result = self._values.get("template")
        assert result is not None, "Required property 'template' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the view.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-view.html#cfn-connect-view-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags associated with the view resource (not specific to view version).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-view.html#cfn-connect-view-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnViewProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnViewVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_connect.CfnViewVersion",
):
    '''Creates a version for the specified customer-managed view within the specified instance.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-viewversion.html
    :cloudformationResource: AWS::Connect::ViewVersion
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_connect as connect
        
        cfn_view_version = connect.CfnViewVersion(self, "MyCfnViewVersion",
            view_arn="viewArn",
        
            # the properties below are optional
            version_description="versionDescription",
            view_content_sha256="viewContentSha256"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        view_arn: builtins.str,
        version_description: typing.Optional[builtins.str] = None,
        view_content_sha256: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param view_arn: The unqualified Amazon Resource Name (ARN) of the view. For example: ``arn:<partition>:connect:<region>:<accountId>:instance/00000000-0000-0000-0000-000000000000/view/00000000-0000-0000-0000-000000000000``
        :param version_description: The description of the view version.
        :param view_content_sha256: Indicates the checksum value of the latest published view content.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c352cc20d21de3ffee67568db6d5f70cd6bd44413ffa25ab4bc4e5003607525b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnViewVersionProps(
            view_arn=view_arn,
            version_description=version_description,
            view_content_sha256=view_content_sha256,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ef9e1adb9742a5b6528d05803eabeacc107cda0e7efd2b616937827060f15dc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3d2a010c19b8e9477becc17b769517ffe7c4a777f027b14b967df4e38557bdb8)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrVersion")
    def attr_version(self) -> jsii.Number:
        '''Current version of the view.

        :cloudformationAttribute: Version
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrViewVersionArn")
    def attr_view_version_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the view version.

        :cloudformationAttribute: ViewVersionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrViewVersionArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="viewArn")
    def view_arn(self) -> builtins.str:
        '''The unqualified Amazon Resource Name (ARN) of the view.'''
        return typing.cast(builtins.str, jsii.get(self, "viewArn"))

    @view_arn.setter
    def view_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__454401f63226a9befa6bffaf911f023a073fd0c5eae570a9b29be7d3f7ff94af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "viewArn", value)

    @builtins.property
    @jsii.member(jsii_name="versionDescription")
    def version_description(self) -> typing.Optional[builtins.str]:
        '''The description of the view version.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionDescription"))

    @version_description.setter
    def version_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__640f2264538b9f6d41074375157692bd7450e4e39efbea1384afb1f1f12d0b44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionDescription", value)

    @builtins.property
    @jsii.member(jsii_name="viewContentSha256")
    def view_content_sha256(self) -> typing.Optional[builtins.str]:
        '''Indicates the checksum value of the latest published view content.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "viewContentSha256"))

    @view_content_sha256.setter
    def view_content_sha256(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5c8aa5e5d6802692a03611724808d85ab729895ff6180601dee7f8b5c3cbc23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "viewContentSha256", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_connect.CfnViewVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "view_arn": "viewArn",
        "version_description": "versionDescription",
        "view_content_sha256": "viewContentSha256",
    },
)
class CfnViewVersionProps:
    def __init__(
        self,
        *,
        view_arn: builtins.str,
        version_description: typing.Optional[builtins.str] = None,
        view_content_sha256: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnViewVersion``.

        :param view_arn: The unqualified Amazon Resource Name (ARN) of the view. For example: ``arn:<partition>:connect:<region>:<accountId>:instance/00000000-0000-0000-0000-000000000000/view/00000000-0000-0000-0000-000000000000``
        :param version_description: The description of the view version.
        :param view_content_sha256: Indicates the checksum value of the latest published view content.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-viewversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_connect as connect
            
            cfn_view_version_props = connect.CfnViewVersionProps(
                view_arn="viewArn",
            
                # the properties below are optional
                version_description="versionDescription",
                view_content_sha256="viewContentSha256"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__625c576cd29cfea7eb8a7d7197edcd80462fd0eac7870bac9066ac9fee2ad619)
            check_type(argname="argument view_arn", value=view_arn, expected_type=type_hints["view_arn"])
            check_type(argname="argument version_description", value=version_description, expected_type=type_hints["version_description"])
            check_type(argname="argument view_content_sha256", value=view_content_sha256, expected_type=type_hints["view_content_sha256"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "view_arn": view_arn,
        }
        if version_description is not None:
            self._values["version_description"] = version_description
        if view_content_sha256 is not None:
            self._values["view_content_sha256"] = view_content_sha256

    @builtins.property
    def view_arn(self) -> builtins.str:
        '''The unqualified Amazon Resource Name (ARN) of the view.

        For example:

        ``arn:<partition>:connect:<region>:<accountId>:instance/00000000-0000-0000-0000-000000000000/view/00000000-0000-0000-0000-000000000000``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-viewversion.html#cfn-connect-viewversion-viewarn
        '''
        result = self._values.get("view_arn")
        assert result is not None, "Required property 'view_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version_description(self) -> typing.Optional[builtins.str]:
        '''The description of the view version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-viewversion.html#cfn-connect-viewversion-versiondescription
        '''
        result = self._values.get("version_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def view_content_sha256(self) -> typing.Optional[builtins.str]:
        '''Indicates the checksum value of the latest published view content.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-viewversion.html#cfn-connect-viewversion-viewcontentsha256
        '''
        result = self._values.get("view_content_sha256")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnViewVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApprovedOrigin",
    "CfnApprovedOriginProps",
    "CfnContactFlow",
    "CfnContactFlowModule",
    "CfnContactFlowModuleProps",
    "CfnContactFlowProps",
    "CfnEvaluationForm",
    "CfnEvaluationFormProps",
    "CfnHoursOfOperation",
    "CfnHoursOfOperationProps",
    "CfnInstance",
    "CfnInstanceProps",
    "CfnInstanceStorageConfig",
    "CfnInstanceStorageConfigProps",
    "CfnIntegrationAssociation",
    "CfnIntegrationAssociationProps",
    "CfnPhoneNumber",
    "CfnPhoneNumberProps",
    "CfnPredefinedAttribute",
    "CfnPredefinedAttributeProps",
    "CfnPrompt",
    "CfnPromptProps",
    "CfnQueue",
    "CfnQueueProps",
    "CfnQuickConnect",
    "CfnQuickConnectProps",
    "CfnRoutingProfile",
    "CfnRoutingProfileProps",
    "CfnRule",
    "CfnRuleProps",
    "CfnSecurityKey",
    "CfnSecurityKeyProps",
    "CfnSecurityProfile",
    "CfnSecurityProfileProps",
    "CfnTaskTemplate",
    "CfnTaskTemplateProps",
    "CfnTrafficDistributionGroup",
    "CfnTrafficDistributionGroupProps",
    "CfnUser",
    "CfnUserHierarchyGroup",
    "CfnUserHierarchyGroupProps",
    "CfnUserProps",
    "CfnView",
    "CfnViewProps",
    "CfnViewVersion",
    "CfnViewVersionProps",
]

publication.publish()

def _typecheckingstub__44955422cb4c00b338f45e52a0d4136fdcdb94c8e433595b636f468d589e514a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_id: builtins.str,
    origin: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15b611bd9c5a92c253c2e2b0cba97b9f73bad0cfc8494953acb694fda143bba2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc2ef7b8d5a06b007fe66bb9f5b0208e869ed47a6e5af0d6bf354f4df2d4d6c8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fd219e5b157d40fbc4254297a9308245796269c824a72c0b9db3bad7013261c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49fb9b02cf4a1b22d6433eac9cb35377d1877512b477dbf9c030fec47fb54f75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__437fb8bad3e7665288233ec7ee3b4db6669d85ab53efddb888b5d729979a4e2f(
    *,
    instance_id: builtins.str,
    origin: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bacec198fd7006a7e922c6b62694383eb7200d23c3f8da491f520191bdc8353f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    content: builtins.str,
    instance_arn: builtins.str,
    name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aca14ea5542ff9acc3dc06746c7580c88c1e0b75d66bf0ac0a8cd785404cc173(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4b3abb60d405603981215ec7d659c3d8939dbf9b5de879c8d56dfd0631f9d5b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a517102f202efaced50f937df38d5374d2d8ae33c5659296852d677cbe73e2a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20f6a7aacca6b49f3791bf907484b7af427677a1079ea79db9a45489b963b9d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76f576a62faffae972ec30039ac3019bddb9b613e8dd2dce2b52723ba8a64dbc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__213719edbc55495f331c0d1f51b7ab8a359f2c5cc563f3fa97077760121c6aa9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e4573df3b75ab7b2ea3d0cba32ff3c515f11f6cbec43c0885d9ee30d25616a0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7b6f72cf71dca93b2b2baae1d002d73d66de8e16bec7709efdb45c4bb811336(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22bc442433d76b98a1dae3304e1215f20c67d932bbfc6f02619483fbdb5d808d(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__008a6ee0ce6447d7f5f7c62774a959e253bc4a69cef26848e6d3f74cf2381193(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    content: builtins.str,
    instance_arn: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82176173dbe238b7a4715d8a94792d3696ada52a4372f823ab10f4c590c6193f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f3e317a83e30b22f766c5d65c8451e4d9e5ffcd6510573aa22d0063860e7b99(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1701812aa93a58317265edab1cd66b5a843fc9845a1aed0b81f83c4f738b5b0e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68b9231af4bcfc40233b3b8fbbd6acd02fe21a59b2f962738d2ce93d6ffa7fa7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e18e7239d9aefba3afcb9b93bf7f3ec9f6e4f173d51f91e93f5543efe25658a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c1841af03e44ad4a3c471a24f30aa57c457ec766515db087b0745fb9a6a68d9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25db523d57560a8813a16f507ae8c09c28625a53b6a24b5744ca978282ff51a3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47de1c508f0616d427a0546578e35f062250082b28649c8985770019609a4881(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84f0f2ba3fd7010e7e0bb6aaa71b591e31e6d4c4ad736e9c4e08be6f11de0102(
    *,
    content: builtins.str,
    instance_arn: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0555b19a226cc1a8bd054951921ffd23e0c635fe29a3d69a330d8262710a7d8(
    *,
    content: builtins.str,
    instance_arn: builtins.str,
    name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    state: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67672e07b9b284918b4f61d0c04df64749fd2f5f1f5a07e093b1e338fae6f20d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_arn: builtins.str,
    items: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluationForm.EvaluationFormBaseItemProperty, typing.Dict[builtins.str, typing.Any]]]]],
    status: builtins.str,
    title: builtins.str,
    description: typing.Optional[builtins.str] = None,
    scoring_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluationForm.ScoringStrategyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8420425768038ffe2547f9ff300fef6a49b05240841e0c7ad3e44c95c4ab5725(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c7ab1fa85562638f3f809a803e50bdd9d399a8c4e22aad540db331656c5a7e4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e8c997caf14ee62e4089ac89d3358aef59cbdf6698b52bd57527b1af0ea2ebb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24592bd80085495fe88d36be53b16b2dc291afc06a041b2135eb47206f64c9d4(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEvaluationForm.EvaluationFormBaseItemProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__989b0b560f041388bf986f0dcb8487074564673bc25c4ffe3be8bbfd6e1a74b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fe499614d5f5501fca8c029af605f671cdbfd45404bbcf2cb1dca048ab19e45(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b9daef123f8c8ba72731239424846e3251f3e39a09700e6514170d316f71293(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8ab41606e6f4148f72499568c63a3750f38b857a5fc25e01a04fcefb15350c9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEvaluationForm.ScoringStrategyProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec087e4492b70f062d224ca25c2f0d81dc78704ad8d957b26ed60e8e67176df5(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f23a880d7bbcb8fab0eba70189a52c3eb1d392f5651dc0f0a2fe54cf4df27d7(
    *,
    section: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluationForm.EvaluationFormSectionProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ed93558b58ad3642a506969313dd38d56ce0f003f808635135ccaf5c8c578e4(
    *,
    question: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluationForm.EvaluationFormQuestionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    section: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluationForm.EvaluationFormSectionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b81afcd26ca2b7f7f360e53cfff837a4d204082391c2522686bc1415137d9bb0(
    *,
    property_value: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluationForm.NumericQuestionPropertyValueAutomationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b52418aba140bb56125771f8a631543b2ff66b57a21d4994b919cafe548ec537(
    *,
    max_value: jsii.Number,
    min_value: jsii.Number,
    automatic_fail: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    score: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fdebefe553e70e8e484dd5dc1c652ee40882ca2d19bc3a12aa677060f0c897d(
    *,
    max_value: jsii.Number,
    min_value: jsii.Number,
    automation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluationForm.EvaluationFormNumericQuestionAutomationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluationForm.EvaluationFormNumericQuestionOptionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76f87135992dba43e2709251a961f9661f40617cabeb04621ceba33e2e2a0831(
    *,
    question_type: builtins.str,
    ref_id: builtins.str,
    title: builtins.str,
    instructions: typing.Optional[builtins.str] = None,
    not_applicable_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    question_type_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluationForm.EvaluationFormQuestionTypePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c2a28674a94b033e97fe7c1b9bbd46fbd0b917a1605152cbffbc509362bd288(
    *,
    numeric: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluationForm.EvaluationFormNumericQuestionPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    single_select: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluationForm.EvaluationFormSingleSelectQuestionPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__016fd84ffa312050ab1787423e77775e0c40fb4835c07025e616e21af7a958db(
    *,
    ref_id: builtins.str,
    title: builtins.str,
    instructions: typing.Optional[builtins.str] = None,
    items: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluationForm.EvaluationFormItemProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3628da3194346fb903c2da16aee6a4931544b13dac0a74d2857ffd14617e3af(
    *,
    rule_category: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluationForm.SingleSelectQuestionRuleCategoryAutomationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc97b2bfa6d5fb8da071bf0ca06feb3e4bb442b1422677cdb6c7ae776fc3629c(
    *,
    options: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationOptionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    default_option_ref_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__511068b0668e9106d683cef742ddd4f219ab5e8b7872b9c6d3692faf6c91a2a2(
    *,
    ref_id: builtins.str,
    text: builtins.str,
    automatic_fail: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    score: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45e8b8c481c725b1ed84e34212cf426ea008289d40995f757fe99cb6f3130e54(
    *,
    options: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluationForm.EvaluationFormSingleSelectQuestionOptionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    automation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluationForm.EvaluationFormSingleSelectQuestionAutomationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    display_as: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c2101c26bfd31e1208bce72ced73e086806ccc5e207eec345b38abde0b4647d(
    *,
    label: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36b59a77759bb952407e2a520298a2e8de054a6d394464d5d2df9e38f1efc2e3(
    *,
    mode: builtins.str,
    status: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b2bf16cb3e015cee3921d57ba3346d4fc6c93af2e79cdcf6d8dec3a5caee630(
    *,
    category: builtins.str,
    condition: builtins.str,
    option_ref_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b678e993288629444b4e1bc33b4631f7578a458c70203ec6ae7263a8aedc75ad(
    *,
    instance_arn: builtins.str,
    items: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluationForm.EvaluationFormBaseItemProperty, typing.Dict[builtins.str, typing.Any]]]]],
    status: builtins.str,
    title: builtins.str,
    description: typing.Optional[builtins.str] = None,
    scoring_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluationForm.ScoringStrategyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da9a7b2f06b8b2d053fcfa26018be9202b48193f9ffb7fc1d9518391cd9b5afe(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHoursOfOperation.HoursOfOperationConfigProperty, typing.Dict[builtins.str, typing.Any]]]]],
    instance_arn: builtins.str,
    name: builtins.str,
    time_zone: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1892c64bc10c89577bb1c7c1cbafe5e7256d59298765e4d13fa8bc792aff27cb(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1be399a62772419844397558be775450dd4c2dc740a8864f61b03b483610073(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__390986701d928ed3f41379b144a434426999d52505eaf487d066a0865f299c42(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnHoursOfOperation.HoursOfOperationConfigProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff371c180e62831feb4bd92859ad779161086fed20f40c5fcaec70aedbd1d950(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__314c5f51a2268bd65be9864b4a46c3d2279936b4a2675b16522bc736ba5fb373(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__442605da8563582cbafb26c421377e100eaf1791f47f7f84657994d9d7347b8c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__224611189f5992474af63688324a9a850ba31b7aad01b0eaae5a8fd63f4ea172(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3006704998781ab2276bf2b26481ef171277930dc1c09d1dcf2e54b8cd07b7c(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ef26f457a53e548698c50361c4e334e5f633638af5ae2b9230dccc5fd5c1dd3(
    *,
    day: builtins.str,
    end_time: typing.Union[_IResolvable_da3f097b, typing.Union[CfnHoursOfOperation.HoursOfOperationTimeSliceProperty, typing.Dict[builtins.str, typing.Any]]],
    start_time: typing.Union[_IResolvable_da3f097b, typing.Union[CfnHoursOfOperation.HoursOfOperationTimeSliceProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca5c5b128d189787db53fa22c88668d84b3efd31f5b54320dcda0838372db008(
    *,
    hours: jsii.Number,
    minutes: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66cef12b59765322de54d22fe6de568f262a635899fc46cbe6a5f5a97b848467(
    *,
    config: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHoursOfOperation.HoursOfOperationConfigProperty, typing.Dict[builtins.str, typing.Any]]]]],
    instance_arn: builtins.str,
    name: builtins.str,
    time_zone: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f291b6bb708a40e1a35dc95de4a38d5f9d8117683bed082183bd387f4848fef9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    attributes: typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.AttributesProperty, typing.Dict[builtins.str, typing.Any]]],
    identity_management_type: builtins.str,
    directory_id: typing.Optional[builtins.str] = None,
    instance_alias: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e4dee5bd55d2c2f964814ca3e2747955315fb5bc8f0a80efc7cbad1ed39cbdc(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__023c45bbafb1abf38373b2528d8531c6e7048604e4fabca7c6a4684feb4413d6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15b81c5f62ba93ec0d3e48188cccf781d5861eac87dc5aa4a4038e6d2176145e(
    value: typing.Union[_IResolvable_da3f097b, CfnInstance.AttributesProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1723398c06ebefeb9e3f4e11e08b8929e713cae56a36abf11fae424fa1c0cea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a002f21d50b37114edc464bd9143a0e1abc1702e5ff455644179b2ac7acbfbdd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__225190f7b3c1545c436fe6b710e05a3a5b7d256f1ece21dcb8ad6ba49cf45c90(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e8d8f5cd36a7297cd164f61b17e1e7ad86e005761d780299041506bff9d1f68(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c40aedafdc4ea4fb2b717cc5c6ef0e2db4eb7490be99c35b78dc90f18526d068(
    *,
    inbound_calls: typing.Union[builtins.bool, _IResolvable_da3f097b],
    outbound_calls: typing.Union[builtins.bool, _IResolvable_da3f097b],
    auto_resolve_best_voices: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    contactflow_logs: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    contact_lens: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    early_media: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    use_custom_tts_voices: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67fdacfbc8ac4206df45637f43843e90e644b42387d3af9173f714ef095953b4(
    *,
    attributes: typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstance.AttributesProperty, typing.Dict[builtins.str, typing.Any]]],
    identity_management_type: builtins.str,
    directory_id: typing.Optional[builtins.str] = None,
    instance_alias: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30c8e9e3ad538fac1acafd66e46e4e7a4f3893f93a8c6bb42ba1525f14973522(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_arn: builtins.str,
    resource_type: builtins.str,
    storage_type: builtins.str,
    kinesis_firehose_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceStorageConfig.KinesisFirehoseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kinesis_stream_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceStorageConfig.KinesisStreamConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kinesis_video_stream_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceStorageConfig.KinesisVideoStreamConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceStorageConfig.S3ConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__047b8a3f497a61ecbf349954496260297e95ce2a4561a42f301589ab2cee4b2a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64e208c0e80a04bb7be2d96f8d6f17f40b00cfff9d7822b7f4ecb07751859062(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb171c6a585c549bf0fad4d15990fc6ee838655cd803c3fd46739aba98a2a1d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ae5f517bee9d34ee21bd11e2d5f0247d46092ae2f3deb37dcf2893b2f798f14(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e576862f1e107b0e3735b4d183525ba16593162db67ddb46e8ca789a1af5850(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0c82cfbbde3b0d4520ea2bf1db2e6d9a0262e0c56473bd9769a65fc32f975a8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstanceStorageConfig.KinesisFirehoseConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a364c6eb62a091d24f417f496838aa90b1e63e040b4dad6e12dd8288568f014(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstanceStorageConfig.KinesisStreamConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f43628a93b9adb2e5341b48d5f226f90e92dc0574e63f1fabc8616c9c49b35ef(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstanceStorageConfig.KinesisVideoStreamConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e076b90fc0b5155e89233d8d5afcf24aea56049cea6a67a56da67867dd963c3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstanceStorageConfig.S3ConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc46269845c7184ad0679658c798d342839ec1fbf50541709790ef0d801dd540(
    *,
    encryption_type: builtins.str,
    key_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a572a34b9441880677e439712bb7b9dbc0a79fc55daf5839857f2041774e7c99(
    *,
    firehose_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__198e237e2c62ec06cc78609686ceeb43aaecd21ba79e09b267cdd8be2c3743a1(
    *,
    stream_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52c9485c197abc64e1dbe93a9ffbdf11fda8b3df13bc67381180643da843a5b8(
    *,
    encryption_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceStorageConfig.EncryptionConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    prefix: builtins.str,
    retention_period_hours: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7296a98085d62b3fe09acddef52fca10fedbaae666bc4512bfa543fd1ddcccab(
    *,
    bucket_name: builtins.str,
    bucket_prefix: builtins.str,
    encryption_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceStorageConfig.EncryptionConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__220fe9c269db6e3bcb651e492fae1b71e17d6b254dfd6b60c71dc0cda259419b(
    *,
    instance_arn: builtins.str,
    resource_type: builtins.str,
    storage_type: builtins.str,
    kinesis_firehose_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceStorageConfig.KinesisFirehoseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kinesis_stream_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceStorageConfig.KinesisStreamConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kinesis_video_stream_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceStorageConfig.KinesisVideoStreamConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceStorageConfig.S3ConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0623057688349069456f9eae4995faa9cd189f98024c1f76262706d5734b311e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_id: builtins.str,
    integration_arn: builtins.str,
    integration_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bb2bfc240169367a312e392a1f57215cf8d8c8079407283c69a1ce7b13f7f09(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3d2595ec7f89aa2a00d106ed9c54cd5cee3b8f448483b246b960847d1347cd0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7925af3a6409e56b03183e28600488914d5fe9b4e7accd90ff869ac4ba2618e4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cc0c68d9b0ec88ff8644cffd658aa26a913dcd92e1fc6ea4af9e71598d78538(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beb9a11163321e5e540a87e2baf965475a45e960cf9aa4a424acc86dcad3feef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe194aedf3230ea702915cbc89ea1228fbcd7507b4352cd6ca6f2c8b3d412d21(
    *,
    instance_id: builtins.str,
    integration_arn: builtins.str,
    integration_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ec70d84fd2bda163d290722acbb6feca633b4ee134732d8b720c0b96701cb7b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    target_arn: builtins.str,
    country_code: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
    source_phone_number_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccee69f4a06306d444592cd5cf9588d2bb31a952c87c3487ff8ad82fc8c8cf94(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b523ee72d695f2e00f7a42b04d5ef172e9c4c9f850d546d7d54f31058efcbf64(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aee914dbb9c13734690f391827e9cd37ca89f521141f3de61e900bfbbd902752(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e8049a6bcb60451cb780647e8cad2360b140018c95db8d6b0e339ed0524e56f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9949958c848f257cc25ceae67fe2e9cee4b1972f09d90ea4ed667dac758be40e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__572d2dd079d87f4a7578acddb0bc7dbcca5ec4c2fecd370ff662ac4d429ea5b5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__300c4efa19cbb74af0cd0af8daf0ae0f9cc8bdc0b5b372ff32bd5afa5fec8cb5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0910286729f650a764036086fb0fc5a1d117b7068e7085b28b8314456bcd893(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0868299e1426aef01fcea4843c3c28737fa3b7614cce2aa77e978bfa8976f8f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9b6cbf832a5409fafc1645b1b1a1567ef5e6d173dfed6d56cae08b977fd4b95(
    *,
    target_arn: builtins.str,
    country_code: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    prefix: typing.Optional[builtins.str] = None,
    source_phone_number_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aae8251f3c38f12791d918a121eabea35a0fd76a17fe96a45e59fab899ce5ec7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_arn: builtins.str,
    name: builtins.str,
    values: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPredefinedAttribute.ValuesProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__399a78b10dff53c13a30343d41faca3a437720451fa5b68f2b8d10fbf1f63c2c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3a759424fc31959ddf27d6e257a5b1b335f7d9b1e4ad4bd7184517c6deb90f0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e72a0435a6a506b8daa0226ab38a3801d43c7ac4e15dd134ff74a68575297e08(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__505c1fe18f355a3c8343fc74e29b578ea13ba483aa5951da1f12eba81893b852(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08003c8bd2407db8849ebc9b0c31a79805d1a0f97f0579e4ac977dfa6a2fd356(
    value: typing.Union[_IResolvable_da3f097b, CfnPredefinedAttribute.ValuesProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__209d9d991e492e56e0ff65e3395c0553be43e6389f1d983bccebb7b1e86208f0(
    *,
    string_list: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e67db40db23ebfe580f504576f3022c3cb9338c26c6aa02862725f1ecadacc4d(
    *,
    instance_arn: builtins.str,
    name: builtins.str,
    values: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPredefinedAttribute.ValuesProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__683007bdfb211b27a1db29f576ae38fe5ce650e538e8600382be8cd908344f85(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_arn: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    s3_uri: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__082bb671ea7d466d02fa1596c6cdcfaf4437ac98f010da0ad9653442f009294a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d29b20ca0171050cd3cbd4d3f240f943d1113931a9994c764036f857a492c5a0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e57a8b746d04374a6f0e38aaadf23a714511218b7101e02e1c4bbbbc1b114343(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d4bf73898e39f9d3f8ceed6fed7eb213a1a0832a0548e822d8d7b1852b52d00(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39c216e96fc64af4ced4806125e9bb517bf8afb21c9527d9140168a800149593(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__155bb4a41abbed9be485f4a84dd2dff42cbadb5390d2f8e657348892f5e2ec15(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b88b3999e96c364888f1b8a2f9495a78cd1b725cf709724ac78279658d35ced(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de9fba0f83321ee92a8e37f03749f2012ea66a3d9d17e7a5b3d12208f718130d(
    *,
    instance_arn: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    s3_uri: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__305bba43cd31a2f9d719dec6a726b64cb46f6b33b3b631880aa85047c7056f75(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    hours_of_operation_arn: builtins.str,
    instance_arn: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    max_contacts: typing.Optional[jsii.Number] = None,
    outbound_caller_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnQueue.OutboundCallerConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    quick_connect_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f93be61e7812e4853e82b359f9f56dddced567e8b8bd359c20e0fd75ddeb08ba(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__810d3f06ac22f06b625c2807da1ff7874cd5dbdf46e30800ef339329bb22f755(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7d30f6e0e4ce3aa26db7bed186df9948879475e9d65d78ad7d2b1b1561e43bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b2cc069db010e8833f184babb5c99b72c3a0167b7f941763fde2016f183c90f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27bc5019f6be77ed53ba7b862aca0ea738158dec243027976b99cd8fd7d156cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01334cc773db27a1a528393f9dae2d25072dea3e9175e44003dc6d7b729dc1ee(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ef18f4767eb9b75cc12f1f22292b0dac9bb3c25561c4f2dc0a503d0bda1b02b(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efe056b6b273a9bf8a7269bd77e79f2001945bafc023aed9da6eba0851a70a6c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnQueue.OutboundCallerConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__028ca5a74d47f38a105a56baa46c7e52d7fe78d25b30fceb95452700dd3fddaf(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cda75a5d23f16160f73ce61f8cebb27b0821ddfea0cc766b3fb59137ce1d3f8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4404046d9df0429c6f43ab2ee542dc80ea4102b8e0802875f2dc57d2dd561b4d(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2f8c0fdd30542f9e64ba3ad4c32832636467651ad5236b756c53590ecabed33(
    *,
    outbound_caller_id_name: typing.Optional[builtins.str] = None,
    outbound_caller_id_number_arn: typing.Optional[builtins.str] = None,
    outbound_flow_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baa26a31f9cdaa2c1ff32bcd44e00a08477582db0c01e27c9e1a60c3e96a8bce(
    *,
    hours_of_operation_arn: builtins.str,
    instance_arn: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    max_contacts: typing.Optional[jsii.Number] = None,
    outbound_caller_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnQueue.OutboundCallerConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    quick_connect_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44121049328c061f99076678805110a34e47bc31097d43b030f388eca53234e9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_arn: builtins.str,
    name: builtins.str,
    quick_connect_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnQuickConnect.QuickConnectConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac17b042f7cf408478c49ac00f219efb0ede78bbe556a5ec55b66c5025bf6198(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a25858c0bb7501da609f58db5989e1c4593c28fa68b47618b9ed5533379f506(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f4d649c9007065ac09a0caa875fd618788a773aab62e76f33a48ae54d5284ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03d7d088ec5e9e804f349ff7c9f716ab0de501abdb1561144e8cba5e16ae351d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf95cf02ae05236caa122a481ca15ec758f528b67ca083a27c0d64c2c3c7f4d2(
    value: typing.Union[_IResolvable_da3f097b, CfnQuickConnect.QuickConnectConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f4633c9c2a7464e4f507d168aa19eee91126aef113fdfcb12ab23fe37d443cc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d25a4810179e086fcbdd720e6235f81b481124650b66e395c9bc34b2d357fb46(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c594b9d59e37b885f89d8bea8817c96760d7982a4ec30c3cec4c9d6620f0690(
    *,
    phone_number: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7632a33b2bc55f259222d21532508c7c3f8f6ef77e1098e16a144fdb3514616(
    *,
    contact_flow_arn: builtins.str,
    queue_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a5ffbc184bff7cbc8cc0dd5bf20c11b8676ca18d518a33d4b7ae2d76891f05d(
    *,
    quick_connect_type: builtins.str,
    phone_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnQuickConnect.PhoneNumberQuickConnectConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    queue_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnQuickConnect.QueueQuickConnectConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnQuickConnect.UserQuickConnectConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7730396d4c494428f6ddd636283d9d5c17ba3fbc6013f1c545a8788d686e0fc1(
    *,
    contact_flow_arn: builtins.str,
    user_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d4ffda8775de853a0509cc15bc43b59e37fc8f6d1d2c110c1202c4192841fbd(
    *,
    instance_arn: builtins.str,
    name: builtins.str,
    quick_connect_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnQuickConnect.QuickConnectConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca1360ef7fc87b491018629ca5fc6a3c13fcbdd97e4a14461038caf03b1040c0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    default_outbound_queue_arn: builtins.str,
    description: builtins.str,
    instance_arn: builtins.str,
    media_concurrencies: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRoutingProfile.MediaConcurrencyProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    agent_availability_timer: typing.Optional[builtins.str] = None,
    queue_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRoutingProfile.RoutingProfileQueueConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3c1d126bf93606617799bec9e1085a17ff1901adee1bb2566a46664aeeffd67(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77b9ba58a5ab39723e5daa4d5e1269a1daa90368ec1224849b55a6cf80a38104(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50c110c7acb8febfc7d34536a1febea6502492baf2f6ee1037837dedbd70168e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__637b45a967f46a44a1c52dafa5bd595123bfb6815a0445ab0a79199a378934f0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba893df3049c142580fe563c14e51066d4293c46c9f36efe1bf670ae56ea1164(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98acf5c62560e25441ec8acb2ae6f5177c36faf800e0f559ad291e27bc924a1d(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRoutingProfile.MediaConcurrencyProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87262b051e4ac4dbfbde0cabebd7e31eeed71edd46cdaec4b306d89ac256b8ee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d19931b4ff72cc897b92c5bddb17158eb5a7dd2de0061c85498c43c4b38eabbf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59e5612a464f7993fc5802b7496378e9f43c22ddbfdd66a4769b7dd34e2ad014(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRoutingProfile.RoutingProfileQueueConfigProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce9959c28e0025c6a6c1956401b24d22cd16b9aa7621c46b183e63ed78f3ba65(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4be673a3765322ed5a02245be092441abde0c8425aaa9c81e6a49ca1ef5eecdd(
    *,
    behavior_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c169890f0c9845b73f64645c0d362ee0a7e26614d464148fd2a80b60082b10e5(
    *,
    channel: builtins.str,
    concurrency: jsii.Number,
    cross_channel_behavior: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRoutingProfile.CrossChannelBehaviorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__032843b9e197335b76e0e3de0555493b80a1e7b395828aefda71c8150ea0a063(
    *,
    delay: jsii.Number,
    priority: jsii.Number,
    queue_reference: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRoutingProfile.RoutingProfileQueueReferenceProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57ccd007831b09a96896ef1c31704165fa1cc179777c86f32ce6de29dce25a9a(
    *,
    channel: builtins.str,
    queue_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c352ac5c14b7a76c3094c7e1595be9aaa093440801508c4780610a6d26b66aa7(
    *,
    default_outbound_queue_arn: builtins.str,
    description: builtins.str,
    instance_arn: builtins.str,
    media_concurrencies: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRoutingProfile.MediaConcurrencyProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    agent_availability_timer: typing.Optional[builtins.str] = None,
    queue_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRoutingProfile.RoutingProfileQueueConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__999d5f7971fc0ea0f693e0f9a61faf62317d493403a6d249ca1db6bc52d61e6f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    actions: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.ActionsProperty, typing.Dict[builtins.str, typing.Any]]],
    function: builtins.str,
    instance_arn: builtins.str,
    name: builtins.str,
    publish_status: builtins.str,
    trigger_event_source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.RuleTriggerEventSourceProperty, typing.Dict[builtins.str, typing.Any]]],
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa852f8205e0acaca3e6361c61c512ea090fe504a708495d2b5bdadc81b30809(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8f82a813645b192cb4d0a6df6a35e9ffe4fe072375390e4d29ebb42555752ad(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bdf3e9c3a73f02992b32c967f3457b7eeade7d3dfa554da9d661f54924ad9a2(
    value: typing.Union[_IResolvable_da3f097b, CfnRule.ActionsProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85af4feedf296e30da787ccf9bc61e248b9a97c21a29fd8fbf38621d5d654fdd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec5da44206c20fbb184f7443ea185123d28ab75d447650604f654e3fe336b233(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6699a016b8fc3ffcc40b2227c32c82c77dcef5f7a74d28bea7e181707fb33bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__464a87f0223cf9d2bd4ca32eeb79cbb74d44d9fead6bf2a81a1db65870834bf2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a752b13b9a86d9caa3ed642e2b19a8ac6db9d24515c76f729c8ad704d664388(
    value: typing.Union[_IResolvable_da3f097b, CfnRule.RuleTriggerEventSourceProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7ff60d02ce44f26fb689403f0b8615b44a5b305d316fb9e80298948590ae2d2(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ef20a75dbfc13161d3fff13ec1c4969adde44c34f62addd27e480514ce92395(
    *,
    assign_contact_category_actions: typing.Optional[typing.Union[typing.Sequence[typing.Any], _IResolvable_da3f097b]] = None,
    create_case_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.CreateCaseActionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    end_associated_tasks_actions: typing.Optional[typing.Union[typing.Sequence[typing.Any], _IResolvable_da3f097b]] = None,
    event_bridge_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.EventBridgeActionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    send_notification_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.SendNotificationActionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    task_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.TaskActionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    update_case_actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.UpdateCaseActionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab1813f0f35711195f55dc6283bd2d1a984f7c2f7e37efe287a6d2d847cd6d86(
    *,
    fields: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.FieldProperty, typing.Dict[builtins.str, typing.Any]]]]],
    template_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__037f7c36eff1515bc6e2d8e67f9b2bac8beade9773e2103dd3b8b5ca5405e447(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6c57d9892877040d89a2aed4e1afb5e5eb027cb36bc0f8392074bd7cd8d8323(
    *,
    id: builtins.str,
    value: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.FieldValueProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b775c6c3e6b1c930720eb9500ebf63cc475488f7c2d8ed565fb6a0294ff1e652(
    *,
    boolean_value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    double_value: typing.Optional[jsii.Number] = None,
    empty_value: typing.Any = None,
    string_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d577395a2866fe40fdf75bbcc932da0701cd7985bbb4de4e2ef65243ba9d387(
    *,
    user_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    user_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6a9deeefd8de7f6bdabd5dee0827f879a4b6911d8516976e0492403b3a4724a(
    *,
    type: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16bc3686835833422d3f82ede42c0b9acf288c30c14f9b3b761db32339bbd1f5(
    *,
    event_source_name: builtins.str,
    integration_association_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__199075d61da7aee6c24aad33a7023d6a679853ff216c051fe322418490e5e9e4(
    *,
    content: builtins.str,
    content_type: builtins.str,
    delivery_method: builtins.str,
    recipient: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.NotificationRecipientTypeProperty, typing.Dict[builtins.str, typing.Any]]],
    subject: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36d4ac91ef6fb71bdda5474ed1cbe12228c8f5caa3aec2778c4c6642b1ab6b3b(
    *,
    contact_flow_arn: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    references: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.ReferenceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__172e88a6af9428a8608ec5ab094e800f6fbe7460bbec91c4a3347cc987a420e5(
    *,
    fields: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.FieldProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86228e744389fdc43748e3523fb391089cfd59a98fc3cac55a6aff07ca243441(
    *,
    actions: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.ActionsProperty, typing.Dict[builtins.str, typing.Any]]],
    function: builtins.str,
    instance_arn: builtins.str,
    name: builtins.str,
    publish_status: builtins.str,
    trigger_event_source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRule.RuleTriggerEventSourceProperty, typing.Dict[builtins.str, typing.Any]]],
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eec1c8c6bb56659ae557c882f85d373b6d643a7be8fd81d7dcb8e28a45f3d99e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_id: builtins.str,
    key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23c2e847b86bfc09195d252c47aea6a4403071968a249a46d9beca03100b5358(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__324830fb8488f0e9a9d62f4765f4824a32ded877f4766d2c34ea20eef4c4a506(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a94821c1bb0576049b170e315ebfd7632b76a9c0cbe46f78111e960033839544(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bae1fd3a5ae97acd56284508ad71af29fda88e415500606aed041d91bc4fe256(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__328945501d2d11db9e341c31e7f88f7eaea8695d95d7c557b2d470e619744f5e(
    *,
    instance_id: builtins.str,
    key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e088a4b4379aab0e18ddc67fbe352d07789383efb957a27db08764dcdee196a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_arn: builtins.str,
    security_profile_name: builtins.str,
    allowed_access_control_hierarchy_group_id: typing.Optional[builtins.str] = None,
    allowed_access_control_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    applications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityProfile.ApplicationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    hierarchy_restricted_resources: typing.Optional[typing.Sequence[builtins.str]] = None,
    permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
    tag_restricted_resources: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf7ea5325498e645df3e40abc7a8ec22af3f2070f980c201bde99a31fb5e9805(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69dbb65308ae1fdccfd085529afb7d2cc546578e610bfdd8d165cc1e97b00616(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__087aa3bcfd02d89880b7d9764f65e87379f1aba419654d2b14f144a060eb34de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c494cc473b7dcb10d47e5e6898ba1be788ee0a6eeb210dae180c62e7baffddb6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b0f82dacb2707268147290732f6c1267555107e35b8b506a336b00a5f030de1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__077ab92a2b57c565722ae2a0fff7719378cf0f3194b2c2b620c43393660a0fd5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, _CfnTag_f6864754]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e31297c3c201035cd5629befaf1f09da3be8968c605549607b25f17835315261(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnSecurityProfile.ApplicationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__590e303d4355b23e0035628d91db2ef4ef87c1c2276e23fdbfacd943d8c73472(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22084b5a71b43e42e57329a03ca71f28eb99ce1b07c6cc58e4c267579b7c017d(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6057e31a0dc905719aff4c2ffcf4e2eb667ddbf01175ba8a63d9c849c1d9fc7e(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c35bbd26a4cc24dc3500d939114ad0b31f11493ddfb760fb0bfb7dd5f994a7c3(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78637aba17fc3177a3492b596a6faf951a63fa4d3e768396f5b976aea7257655(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b880e1a466e4d120081a7c103809b59a07385a4cee88474da2f4f00bae13c71a(
    *,
    application_permissions: typing.Sequence[builtins.str],
    namespace: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a8ad9faa5e934c4966c739f0b5e3756a03460ba17b7caf0aca4e26118e04c95(
    *,
    instance_arn: builtins.str,
    security_profile_name: builtins.str,
    allowed_access_control_hierarchy_group_id: typing.Optional[builtins.str] = None,
    allowed_access_control_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    applications: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityProfile.ApplicationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    hierarchy_restricted_resources: typing.Optional[typing.Sequence[builtins.str]] = None,
    permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
    tag_restricted_resources: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e55cf6106eb4919ab3d57f42477e52e40f628476ec3364c5bf5b40089c4746bc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_arn: builtins.str,
    client_token: typing.Optional[builtins.str] = None,
    constraints: typing.Any = None,
    contact_flow_arn: typing.Optional[builtins.str] = None,
    defaults: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTaskTemplate.DefaultFieldValueProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTaskTemplate.FieldProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    name: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46cdd562656d586fa446b953fbbb0484300c8ed5d89c5bdf38b9ee2a994cd465(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a527f307b10d7d5baa2def0fbd31d398ac1b585ebbd7f3a9ba7d38d25d6829e7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9540278151bed9f69d9f399c73f9a40e63e164ba823222a94733e2f75af92d07(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bbd2064bc52aa0f530521bac3bae9c5f12656b7d845175af66583e2c4478aff(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a898069ebffaab98fcbaee0053da25444060ad49ffcbfe6f0368eff95f5b200(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6b4de1aedec1ca589ae0fc007dad4a4b2bd2d8d34fc17ea98b736695f7ce943(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8763e4dc1a72bd2993b2130ce895c2796dd673f1913cef1346294ad7cdfb3f84(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTaskTemplate.DefaultFieldValueProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8feafa724c930c70f39fc9a4f2b3943981c6c26d175bdeef9ccc7a3dddb78a19(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__445eadfb11465e7ab28af66fe2e12f9b6e2c4693cde068247ac72a5db1d0f8bf(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTaskTemplate.FieldProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__536360af8980f014d8658d43741c6a3560607c1550e93deaec8025ead2486e33(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd486363bb52c46e2e9463e955a4ed4c9ffc963b921dce5f0a41124a306b893e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__217384ce686fd8324204da16685901c284bbe5fbe2fb6c28185fac52084c57ae(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8ebbf1d682cf676accdf4695ae9748eb71839e0255117fb6c27fe1391e7e7cc(
    *,
    invisible_fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTaskTemplate.InvisibleFieldInfoProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    read_only_fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTaskTemplate.ReadOnlyFieldInfoProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    required_fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTaskTemplate.RequiredFieldInfoProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7e2fbafd545cd91d979ca1524a9207544758d59734dcb28e71382c3e329623f(
    *,
    default_value: builtins.str,
    id: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTaskTemplate.FieldIdentifierProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56cfea0cc2f28aaee625e6baeef27a54e4f0441cc4cb1502475522d9e1c29e4e(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d065a4a87520f8d3b9711b85f794e75a7c06a4b21d323c419a06f25c134bcaf(
    *,
    id: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTaskTemplate.FieldIdentifierProperty, typing.Dict[builtins.str, typing.Any]]],
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    single_select_options: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d784f103d652729901e9c8a241de453a38a7535564f57cdea8070b407515bff(
    *,
    id: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTaskTemplate.FieldIdentifierProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f99f25935a58d0e69a63e663c70e9233ab3f544824e97f26f01abba7a02906b9(
    *,
    id: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTaskTemplate.FieldIdentifierProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04c2c12eb06cef0a8d595c1a918e7fea99c1d59c019fe5a92fb573ffc0dd280d(
    *,
    id: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTaskTemplate.FieldIdentifierProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffa2d0f88c266e5f2522dfd1af262def0d3061b82ebb529283e7afc28ef8b7bb(
    *,
    instance_arn: builtins.str,
    client_token: typing.Optional[builtins.str] = None,
    constraints: typing.Any = None,
    contact_flow_arn: typing.Optional[builtins.str] = None,
    defaults: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTaskTemplate.DefaultFieldValueProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTaskTemplate.FieldProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    name: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca487c7b5364a4f5551b0a2850374d278ea9b277effd6a5a44ae511b77c2a5a6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_arn: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4f6c13df7129e219cbf36228095876149e60b246cf354ab6fe83b9652428171(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56435f5b52b8efc49bb468ce5e0a5186a2a9b25811e4c4afdcec0fc162bc4d8a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__690e0c359cfbbb997d8caca7bbd988977f9ed96a29fcc7e76700b71ccfdbd3d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05f7e41c371bdd41842327789f2f3c741a118f7cd054f968517e0e9194f92a8d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90cd95785072e927554dbc62f58aa26e2908aa348f84906a5179c37696b83bc3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d10b0c268d645112c426bfa20ffc2365e5a9d7fb89c5ef9a7288bd68b8772881(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__399ed170d743f73906db5f85382e2ff094eded44d1c9ecad71243420bd137725(
    *,
    instance_arn: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05b3c171d418de057737855a6729454df2138450ce49f656f47804ab286addf6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_arn: builtins.str,
    phone_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnUser.UserPhoneConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    routing_profile_arn: builtins.str,
    security_profile_arns: typing.Sequence[builtins.str],
    username: builtins.str,
    directory_user_id: typing.Optional[builtins.str] = None,
    hierarchy_group_arn: typing.Optional[builtins.str] = None,
    identity_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUser.UserIdentityInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    password: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_proficiencies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUser.UserProficiencyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__868e9d73ebd6da6bc01f1a454c28b6ce77bb38b7722cc539dee5d631af8ab7a1(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8a7ab4c4c68abf101e561bdcaa3fccf82a51680bd75b6060ffd85b7b39cee53(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f39c63e5bec20724a75b863eaf92b750aa2b43e84007f59f8101f109aded4b62(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f182c7afc61ebf14606fef1a70e2527bc3c149561eed985aa3c521e419741e73(
    value: typing.Union[_IResolvable_da3f097b, CfnUser.UserPhoneConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53ec4c5274e442b13ba6263b0a0699bceadb2d594cb4553cf3256514da5ba718(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f59f37aa37416b07a1920b9fb28c6db10aa7091b532298ff46eddb3200c94afd(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0d3c1f0374209b5f9480c6b6571b89c26495747acd0440d47b7b3d3a95f28f5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f09389f8f59128c5950972d770de7815f263ca9cf4c25735591417ea4b72939(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f855d98db219c907988e531c32926bf279294c9a15359f1bf876ac28120857f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01c0b838f75f47cfedc3da42d9842c603514aa585b6a8bdfd39ab14e8a57d5ec(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnUser.UserIdentityInfoProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97a2c5140ffd2e76246aa4b882ace6caee9e3c89751b5c2dc0c27a7d20caf26d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e4428cb05b6e362886b1adc91882b21e8cb39137a29037b9728d57b3a622dbe(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18a40ddd47b7e62a1ca5a21d2261e587a5eca592d22947adb5caefa3724093e4(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnUser.UserProficiencyProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__675484167c56516574409f5f87a82bc61f2bd18d297494deb996e1e0a0c63262(
    *,
    email: typing.Optional[builtins.str] = None,
    first_name: typing.Optional[builtins.str] = None,
    last_name: typing.Optional[builtins.str] = None,
    mobile: typing.Optional[builtins.str] = None,
    secondary_email: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e774e2d87fa8144ee9994624937d62ce4393d565b8e6982f7d2e1c5bf0c9ca67(
    *,
    phone_type: builtins.str,
    after_contact_work_time_limit: typing.Optional[jsii.Number] = None,
    auto_accept: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    desk_phone_number: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__345901e38de5207bac37cf2e70717ae293249c5093817f351ddab16523ebf96a(
    *,
    attribute_name: builtins.str,
    attribute_value: builtins.str,
    level: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ee71292692b3a4ed0bb1ecb030ac42cd8de9fe7fd30c25bca5b2f1eaaa6bb48(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_arn: builtins.str,
    name: builtins.str,
    parent_group_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__752f8fce7f90c25285d3743bf24f50aec111d37047ee0c4af63a38e966735a03(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac67c3ecd95bbbc55bc130d457e245f00decbc275854bb8b407db1329f860025(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8fb77dfbead9199eb5f47ecaa078f50ea02c5ce873fd226cd349a59b527fb3c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d0815b3361eabab5affbe2f0e2d26f64eecd0bba911c06147e98f374796565c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec2be8f8330a2a7250df106f290a4e8ddeda8715a95a83b481ae76d8ac2d2d8e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d964880cee57a50d651477affc39220cab9a8575f6e5da757f56a627d3121f3(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51f9a797f445ffc1deaff140a69a030bdb25f3fa135ef233a56621cf7d99867c(
    *,
    instance_arn: builtins.str,
    name: builtins.str,
    parent_group_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__494987ef0f9b905c50c1efbd53f96fb396b7f25b5354dfbb4027a32dbf61b9b1(
    *,
    instance_arn: builtins.str,
    phone_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnUser.UserPhoneConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    routing_profile_arn: builtins.str,
    security_profile_arns: typing.Sequence[builtins.str],
    username: builtins.str,
    directory_user_id: typing.Optional[builtins.str] = None,
    hierarchy_group_arn: typing.Optional[builtins.str] = None,
    identity_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUser.UserIdentityInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    password: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_proficiencies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUser.UserProficiencyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94b4f2f620952c31a829f98f6f735cb6b2bcb05a7aeec0d58a9bf353e42283a3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    actions: typing.Sequence[builtins.str],
    instance_arn: builtins.str,
    name: builtins.str,
    template: typing.Any,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4f4d449c39fb674cb2aee4444da15965f7a738d317d39c5795787870d91cb90(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f51d9f515dc52e659fd588b6b7c69855667a4bcb91e66e6243fb55b7ce6e6d6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfc5249082c6d5a1446f72b2d7f603dfd56182e6160353b7c1af6ee5d04cf427(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a93c4cb77702281173c334c90fe993226032e3fd88c9b905c29b88b91bf0506e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9119d3cb209dab8ae6d5b5cc8cb241d94d81d58771bb72d5e73cd8c92938990b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86e1abb3b53b3f5681b7c0d196d86154b11fafceba7b897bc6536e6d6ed70a4d(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4d4478679794ad5547e519ea6378b504c947ae3ba33c144dbfbd6a02f41c523(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c8717b700734d2f2ffa968661ed869e26cd339beb41934a1e4fb19cf006b80e(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f907c1817accd77cdb1d6d91c707e676a4ecb33911eb5e958e9ef56a1cda0cbd(
    *,
    actions: typing.Sequence[builtins.str],
    instance_arn: builtins.str,
    name: builtins.str,
    template: typing.Any,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c352cc20d21de3ffee67568db6d5f70cd6bd44413ffa25ab4bc4e5003607525b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    view_arn: builtins.str,
    version_description: typing.Optional[builtins.str] = None,
    view_content_sha256: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ef9e1adb9742a5b6528d05803eabeacc107cda0e7efd2b616937827060f15dc(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d2a010c19b8e9477becc17b769517ffe7c4a777f027b14b967df4e38557bdb8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__454401f63226a9befa6bffaf911f023a073fd0c5eae570a9b29be7d3f7ff94af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__640f2264538b9f6d41074375157692bd7450e4e39efbea1384afb1f1f12d0b44(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5c8aa5e5d6802692a03611724808d85ab729895ff6180601dee7f8b5c3cbc23(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__625c576cd29cfea7eb8a7d7197edcd80462fd0eac7870bac9066ac9fee2ad619(
    *,
    view_arn: builtins.str,
    version_description: typing.Optional[builtins.str] = None,
    view_content_sha256: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
