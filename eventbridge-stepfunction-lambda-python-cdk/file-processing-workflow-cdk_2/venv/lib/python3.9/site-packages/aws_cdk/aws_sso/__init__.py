'''
# AWS::SSO Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_sso as sso
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for SSO construct libraries](https://constructs.dev/search?q=sso)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::SSO resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SSO.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::SSO](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SSO.html).

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


@jsii.implements(_IInspectable_c2943556)
class CfnAssignment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sso.CfnAssignment",
):
    '''Assigns access to a Principal for a specified AWS account using a specified permission set.

    .. epigraph::

       The term *principal* here refers to a user or group that is defined in IAM Identity Center .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_sso as sso
        
        cfn_assignment = sso.CfnAssignment(self, "MyCfnAssignment",
            instance_arn="instanceArn",
            permission_set_arn="permissionSetArn",
            principal_id="principalId",
            principal_type="principalType",
            target_id="targetId",
            target_type="targetType"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        instance_arn: builtins.str,
        permission_set_arn: builtins.str,
        principal_id: builtins.str,
        principal_type: builtins.str,
        target_id: builtins.str,
        target_type: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .
        :param permission_set_arn: The ARN of the permission set.
        :param principal_id: An identifier for an object in IAM Identity Center, such as a user or group. PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in IAM Identity Center, see the `IAM Identity Center Identity Store API Reference <https://docs.aws.amazon.com//singlesignon/latest/IdentityStoreAPIReference/welcome.html>`_ .
        :param principal_type: The entity type for which the assignment will be created.
        :param target_id: TargetID is an AWS account identifier, (For example, 123456789012).
        :param target_type: The entity type for which the assignment will be created.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebef8d250e1dbc37b65303c039a5211da7116d20618441b3967d658d6503e2f7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAssignmentProps(
            instance_arn=instance_arn,
            permission_set_arn=permission_set_arn,
            principal_id=principal_id,
            principal_type=principal_type,
            target_id=target_id,
            target_type=target_type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4498cc8fea0c97daa31af89de3f9064e1df7f1b3b2653d46b31fae4287c164c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5488690a5d03065e9d831a867c6d3f7449e711f5e04ccd2e4dd4dea7ca2ba062)
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
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The ARN of the IAM Identity Center instance under which the operation will be executed.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17b623ed0ec409c3a71b2b1b8cf18292a2895708cc1d2c53fa253b69ad8a53a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="permissionSetArn")
    def permission_set_arn(self) -> builtins.str:
        '''The ARN of the permission set.'''
        return typing.cast(builtins.str, jsii.get(self, "permissionSetArn"))

    @permission_set_arn.setter
    def permission_set_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b072b296fcdca1fa35643b12cfd3604849aa9d27f63f391f25f57164791ded77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionSetArn", value)

    @builtins.property
    @jsii.member(jsii_name="principalId")
    def principal_id(self) -> builtins.str:
        '''An identifier for an object in IAM Identity Center, such as a user or group.'''
        return typing.cast(builtins.str, jsii.get(self, "principalId"))

    @principal_id.setter
    def principal_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c490e4155227ea07d5c9d9bcf224a24225f358240ac2bd91930762202bbc3c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principalId", value)

    @builtins.property
    @jsii.member(jsii_name="principalType")
    def principal_type(self) -> builtins.str:
        '''The entity type for which the assignment will be created.'''
        return typing.cast(builtins.str, jsii.get(self, "principalType"))

    @principal_type.setter
    def principal_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__619026097393449b13624a247638924ced09bc52d9bded17b98c0a9cd00f4f68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principalType", value)

    @builtins.property
    @jsii.member(jsii_name="targetId")
    def target_id(self) -> builtins.str:
        '''TargetID is an AWS account identifier, (For example, 123456789012).'''
        return typing.cast(builtins.str, jsii.get(self, "targetId"))

    @target_id.setter
    def target_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5d7c01434a58be26f030bbbb4c4bac0441e711f4c1b954e921cff5db2a357eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetId", value)

    @builtins.property
    @jsii.member(jsii_name="targetType")
    def target_type(self) -> builtins.str:
        '''The entity type for which the assignment will be created.'''
        return typing.cast(builtins.str, jsii.get(self, "targetType"))

    @target_type.setter
    def target_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d31c013e59de3e5493f34c329933cda7b9c6ded610ef1e183427cd7d14cfe8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetType", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sso.CfnAssignmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "permission_set_arn": "permissionSetArn",
        "principal_id": "principalId",
        "principal_type": "principalType",
        "target_id": "targetId",
        "target_type": "targetType",
    },
)
class CfnAssignmentProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        permission_set_arn: builtins.str,
        principal_id: builtins.str,
        principal_type: builtins.str,
        target_id: builtins.str,
        target_type: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnAssignment``.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .
        :param permission_set_arn: The ARN of the permission set.
        :param principal_id: An identifier for an object in IAM Identity Center, such as a user or group. PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in IAM Identity Center, see the `IAM Identity Center Identity Store API Reference <https://docs.aws.amazon.com//singlesignon/latest/IdentityStoreAPIReference/welcome.html>`_ .
        :param principal_type: The entity type for which the assignment will be created.
        :param target_id: TargetID is an AWS account identifier, (For example, 123456789012).
        :param target_type: The entity type for which the assignment will be created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_sso as sso
            
            cfn_assignment_props = sso.CfnAssignmentProps(
                instance_arn="instanceArn",
                permission_set_arn="permissionSetArn",
                principal_id="principalId",
                principal_type="principalType",
                target_id="targetId",
                target_type="targetType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af8b1b897ea9ab77a0f2e4bab0d57a02afda473ba2e2680b392d3403bd006adb)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument permission_set_arn", value=permission_set_arn, expected_type=type_hints["permission_set_arn"])
            check_type(argname="argument principal_id", value=principal_id, expected_type=type_hints["principal_id"])
            check_type(argname="argument principal_type", value=principal_type, expected_type=type_hints["principal_type"])
            check_type(argname="argument target_id", value=target_id, expected_type=type_hints["target_id"])
            check_type(argname="argument target_type", value=target_type, expected_type=type_hints["target_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_arn": instance_arn,
            "permission_set_arn": permission_set_arn,
            "principal_id": principal_id,
            "principal_type": principal_type,
            "target_id": target_id,
            "target_type": target_type,
        }

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The ARN of the IAM Identity Center instance under which the operation will be executed.

        For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def permission_set_arn(self) -> builtins.str:
        '''The ARN of the permission set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-permissionsetarn
        '''
        result = self._values.get("permission_set_arn")
        assert result is not None, "Required property 'permission_set_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal_id(self) -> builtins.str:
        '''An identifier for an object in IAM Identity Center, such as a user or group.

        PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in IAM Identity Center, see the `IAM Identity Center Identity Store API Reference <https://docs.aws.amazon.com//singlesignon/latest/IdentityStoreAPIReference/welcome.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-principalid
        '''
        result = self._values.get("principal_id")
        assert result is not None, "Required property 'principal_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal_type(self) -> builtins.str:
        '''The entity type for which the assignment will be created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-principaltype
        '''
        result = self._values.get("principal_type")
        assert result is not None, "Required property 'principal_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_id(self) -> builtins.str:
        '''TargetID is an AWS account identifier, (For example, 123456789012).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-targetid
        '''
        result = self._values.get("target_id")
        assert result is not None, "Required property 'target_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_type(self) -> builtins.str:
        '''The entity type for which the assignment will be created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-targettype
        '''
        result = self._values.get("target_type")
        assert result is not None, "Required property 'target_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssignmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnInstanceAccessControlAttributeConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sso.CfnInstanceAccessControlAttributeConfiguration",
):
    '''Enables the attribute-based access control (ABAC) feature for the specified IAM Identity Center instance.

    You can also specify new attributes to add to your ABAC configuration during the enabling process. For more information about ABAC, see `Attribute-Based Access Control <https://docs.aws.amazon.com//singlesignon/latest/userguide/abac.html>`_ in the *IAM Identity Center User Guide* .
    .. epigraph::

       The ``InstanceAccessControlAttributeConfiguration`` property has been deprecated but is still supported for backwards compatibility purposes. We recommend that you use the ``AccessControlAttributes`` property instead.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_sso as sso
        
        cfn_instance_access_control_attribute_configuration = sso.CfnInstanceAccessControlAttributeConfiguration(self, "MyCfnInstanceAccessControlAttributeConfiguration",
            instance_arn="instanceArn",
        
            # the properties below are optional
            access_control_attributes=[sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty(
                key="key",
                value=sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty(
                    source=["source"]
                )
            )],
            instance_access_control_attribute_configuration=sso.CfnInstanceAccessControlAttributeConfiguration.InstanceAccessControlAttributeConfigurationProperty(
                access_control_attributes=[sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty(
                    key="key",
                    value=sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty(
                        source=["source"]
                    )
                )]
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        instance_arn: builtins.str,
        access_control_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        instance_access_control_attribute_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceAccessControlAttributeConfiguration.InstanceAccessControlAttributeConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation will be executed.
        :param access_control_attributes: Lists the attributes that are configured for ABAC in the specified IAM Identity Center instance.
        :param instance_access_control_attribute_configuration: (deprecated) The InstanceAccessControlAttributeConfiguration property has been deprecated but is still supported for backwards compatibility purposes. We recomend that you use AccessControlAttributes property instead.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f7a7752ad192f44dab8a4f16ca8392acad24cb912eaff617dbf10c8149c7542)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnInstanceAccessControlAttributeConfigurationProps(
            instance_arn=instance_arn,
            access_control_attributes=access_control_attributes,
            instance_access_control_attribute_configuration=instance_access_control_attribute_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c48b94299d1ffa1f7049b0b5d63f78b836162a06a724a75f0c82d165e2c138b6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea6a2ed55e2a55ee0c5d3955b4f881b8cf8aadf484955c56c4224ebeed434953)
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
    @jsii.member(jsii_name="instanceArn")
    def instance_arn(self) -> builtins.str:
        '''The ARN of the IAM Identity Center instance under which the operation will be executed.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8794fbca8fffc39a5bb8822215af2d986460d2139e6f7f6b8518fe0b4f77389)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="accessControlAttributes")
    def access_control_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty"]]]]:
        '''Lists the attributes that are configured for ABAC in the specified IAM Identity Center instance.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty"]]]], jsii.get(self, "accessControlAttributes"))

    @access_control_attributes.setter
    def access_control_attributes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59b30bff10a4ad495a4848654c3d5cc319a787641db9697ed37a6ff4afa259b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessControlAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="instanceAccessControlAttributeConfiguration")
    def instance_access_control_attribute_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceAccessControlAttributeConfiguration.InstanceAccessControlAttributeConfigurationProperty"]]:
        '''(deprecated) The InstanceAccessControlAttributeConfiguration property has been deprecated but is still supported for backwards compatibility purposes.

        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceAccessControlAttributeConfiguration.InstanceAccessControlAttributeConfigurationProperty"]], jsii.get(self, "instanceAccessControlAttributeConfiguration"))

    @instance_access_control_attribute_configuration.setter
    def instance_access_control_attribute_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnInstanceAccessControlAttributeConfiguration.InstanceAccessControlAttributeConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f70c314997f8ad880ed6373ea4fdd6e57467d1c9f2a6df1941fcce50c8b74442)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceAccessControlAttributeConfiguration", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class AccessControlAttributeProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            value: typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''These are IAM Identity Center identity store attributes that you can configure for use in attributes-based access control (ABAC).

            You can create permissions policies that determine who can access your AWS resources based upon the configured attribute values. When you enable ABAC and specify ``AccessControlAttributes`` , IAM Identity Center passes the attribute values of the authenticated user into IAM for use in policy evaluation.

            :param key: The name of the attribute associated with your identities in your identity source. This is used to map a specified attribute in your identity source with an attribute in IAM Identity Center .
            :param value: The value used for mapping a specified attribute to an identity source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sso as sso
                
                access_control_attribute_property = sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty(
                    key="key",
                    value=sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty(
                        source=["source"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3186d8e26bd7fcbe036cbc3233a43b4bf3854aa2190d5888364286ed51720381)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The name of the attribute associated with your identities in your identity source.

            This is used to map a specified attribute in your identity source with an attribute in IAM Identity Center .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty"]:
            '''The value used for mapping a specified attribute to an identity source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattribute-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessControlAttributeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty",
        jsii_struct_bases=[],
        name_mapping={"source": "source"},
    )
    class AccessControlAttributeValueProperty:
        def __init__(self, *, source: typing.Sequence[builtins.str]) -> None:
            '''The value used for mapping a specified attribute to an identity source.

            :param source: The identity source to use when mapping a specified attribute to IAM Identity Center .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sso as sso
                
                access_control_attribute_value_property = sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty(
                    source=["source"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2820ec077bbb0783624f9db7c803955332448280274edfd9bfda9ad015b81967)
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "source": source,
            }

        @builtins.property
        def source(self) -> typing.List[builtins.str]:
            '''The identity source to use when mapping a specified attribute to IAM Identity Center .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributevalue-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessControlAttributeValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sso.CfnInstanceAccessControlAttributeConfiguration.InstanceAccessControlAttributeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"access_control_attributes": "accessControlAttributes"},
    )
    class InstanceAccessControlAttributeConfigurationProperty:
        def __init__(
            self,
            *,
            access_control_attributes: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''The InstanceAccessControlAttributeConfiguration property has been deprecated but is still supported for backwards compatibility purposes.

            We recomend that you use  AccessControlAttributes property instead.

            :param access_control_attributes: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-instanceaccesscontrolattributeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sso as sso
                
                instance_access_control_attribute_configuration_property = sso.CfnInstanceAccessControlAttributeConfiguration.InstanceAccessControlAttributeConfigurationProperty(
                    access_control_attributes=[sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty(
                        key="key",
                        value=sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty(
                            source=["source"]
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1ef22662569985de541e712d397e178367db6e4386936c4b934aaa6392c6aa3b)
                check_type(argname="argument access_control_attributes", value=access_control_attributes, expected_type=type_hints["access_control_attributes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "access_control_attributes": access_control_attributes,
            }

        @builtins.property
        def access_control_attributes(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty"]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-instanceaccesscontrolattributeconfiguration-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-instanceaccesscontrolattributeconfiguration-accesscontrolattributes
            '''
            result = self._values.get("access_control_attributes")
            assert result is not None, "Required property 'access_control_attributes' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceAccessControlAttributeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sso.CfnInstanceAccessControlAttributeConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "access_control_attributes": "accessControlAttributes",
        "instance_access_control_attribute_configuration": "instanceAccessControlAttributeConfiguration",
    },
)
class CfnInstanceAccessControlAttributeConfigurationProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        access_control_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        instance_access_control_attribute_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceAccessControlAttributeConfiguration.InstanceAccessControlAttributeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnInstanceAccessControlAttributeConfiguration``.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation will be executed.
        :param access_control_attributes: Lists the attributes that are configured for ABAC in the specified IAM Identity Center instance.
        :param instance_access_control_attribute_configuration: (deprecated) The InstanceAccessControlAttributeConfiguration property has been deprecated but is still supported for backwards compatibility purposes. We recomend that you use AccessControlAttributes property instead.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_sso as sso
            
            cfn_instance_access_control_attribute_configuration_props = sso.CfnInstanceAccessControlAttributeConfigurationProps(
                instance_arn="instanceArn",
            
                # the properties below are optional
                access_control_attributes=[sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty(
                    key="key",
                    value=sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty(
                        source=["source"]
                    )
                )],
                instance_access_control_attribute_configuration=sso.CfnInstanceAccessControlAttributeConfiguration.InstanceAccessControlAttributeConfigurationProperty(
                    access_control_attributes=[sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty(
                        key="key",
                        value=sso.CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty(
                            source=["source"]
                        )
                    )]
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__814fa18856a1f832fbf758087fb132fbc281321791aa0253818b3fa514682b45)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument access_control_attributes", value=access_control_attributes, expected_type=type_hints["access_control_attributes"])
            check_type(argname="argument instance_access_control_attribute_configuration", value=instance_access_control_attribute_configuration, expected_type=type_hints["instance_access_control_attribute_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_arn": instance_arn,
        }
        if access_control_attributes is not None:
            self._values["access_control_attributes"] = access_control_attributes
        if instance_access_control_attribute_configuration is not None:
            self._values["instance_access_control_attribute_configuration"] = instance_access_control_attribute_configuration

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The ARN of the IAM Identity Center instance under which the operation will be executed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_control_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty]]]]:
        '''Lists the attributes that are configured for ABAC in the specified IAM Identity Center instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-accesscontrolattributes
        '''
        result = self._values.get("access_control_attributes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty]]]], result)

    @builtins.property
    def instance_access_control_attribute_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstanceAccessControlAttributeConfiguration.InstanceAccessControlAttributeConfigurationProperty]]:
        '''(deprecated) The InstanceAccessControlAttributeConfiguration property has been deprecated but is still supported for backwards compatibility purposes.

        We recomend that you use  AccessControlAttributes property instead.

        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-instanceaccesscontrolattributeconfiguration
        :stability: deprecated
        '''
        result = self._values.get("instance_access_control_attribute_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstanceAccessControlAttributeConfiguration.InstanceAccessControlAttributeConfigurationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInstanceAccessControlAttributeConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnPermissionSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sso.CfnPermissionSet",
):
    '''Specifies a permission set within a specified IAM Identity Center instance.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_sso as sso
        
        # inline_policy: Any
        
        cfn_permission_set = sso.CfnPermissionSet(self, "MyCfnPermissionSet",
            instance_arn="instanceArn",
            name="name",
        
            # the properties below are optional
            customer_managed_policy_references=[sso.CfnPermissionSet.CustomerManagedPolicyReferenceProperty(
                name="name",
        
                # the properties below are optional
                path="path"
            )],
            description="description",
            inline_policy=inline_policy,
            managed_policies=["managedPolicies"],
            permissions_boundary=sso.CfnPermissionSet.PermissionsBoundaryProperty(
                customer_managed_policy_reference=sso.CfnPermissionSet.CustomerManagedPolicyReferenceProperty(
                    name="name",
        
                    # the properties below are optional
                    path="path"
                ),
                managed_policy_arn="managedPolicyArn"
            ),
            relay_state_type="relayStateType",
            session_duration="sessionDuration",
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
        customer_managed_policy_references: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPermissionSet.CustomerManagedPolicyReferenceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        inline_policy: typing.Any = None,
        managed_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        permissions_boundary: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPermissionSet.PermissionsBoundaryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        relay_state_type: typing.Optional[builtins.str] = None,
        session_duration: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .
        :param name: The name of the permission set.
        :param customer_managed_policy_references: Specifies the names and paths of the customer managed policies that you have attached to your permission set.
        :param description: The description of the ``PermissionSet`` .
        :param inline_policy: The inline policy that is attached to the permission set. .. epigraph:: For ``Length Constraints`` , if a valid ARN is provided for a permission set, it is possible for an empty inline policy to be returned.
        :param managed_policies: A structure that stores the details of the AWS managed policy.
        :param permissions_boundary: Specifies the configuration of the AWS managed or customer managed policy that you want to set as a permissions boundary. Specify either ``CustomerManagedPolicyReference`` to use the name and path of a customer managed policy, or ``ManagedPolicyArn`` to use the ARN of an AWS managed policy. A permissions boundary represents the maximum permissions that any policy can grant your role. For more information, see `Permissions boundaries for IAM entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`_ in the *IAM User Guide* . .. epigraph:: Policies used as permissions boundaries don't provide permissions. You must also attach an IAM policy to the role. To learn how the effective permissions for a role are evaluated, see `IAM JSON policy evaluation logic <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html>`_ in the *IAM User Guide* .
        :param relay_state_type: Used to redirect users within the application during the federation authentication process.
        :param session_duration: The length of time that the application user sessions are valid for in the ISO-8601 standard.
        :param tags: The tags to attach to the new ``PermissionSet`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29742c4712f9aeed238f180c9db8677986b9e95f63644b8358d20bbe6f9f8c9d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPermissionSetProps(
            instance_arn=instance_arn,
            name=name,
            customer_managed_policy_references=customer_managed_policy_references,
            description=description,
            inline_policy=inline_policy,
            managed_policies=managed_policies,
            permissions_boundary=permissions_boundary,
            relay_state_type=relay_state_type,
            session_duration=session_duration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41af3694bf258cce2eec00f3796e70405f43f39c22f5563c380367005e925825)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cacdbbe8633389e9abfb49528d132366b3e7cd1904ca9b9142ff94e947907357)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrPermissionSetArn")
    def attr_permission_set_arn(self) -> builtins.str:
        '''The permission set ARN of the permission set, such as ``arn:aws:sso:::permissionSet/ins-instanceid/ps-permissionsetid`` .

        :cloudformationAttribute: PermissionSetArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPermissionSetArn"))

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
        '''The ARN of the IAM Identity Center instance under which the operation will be executed.'''
        return typing.cast(builtins.str, jsii.get(self, "instanceArn"))

    @instance_arn.setter
    def instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f097006770b4dc8eb39790dbe3afd4885f8cf745ad922489ed434c6f02ba81cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the permission set.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9317633963da92f7e1e0f006966e8f9bfb827bca42dd01644d334d1607ac85f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="customerManagedPolicyReferences")
    def customer_managed_policy_references(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPermissionSet.CustomerManagedPolicyReferenceProperty"]]]]:
        '''Specifies the names and paths of the customer managed policies that you have attached to your permission set.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPermissionSet.CustomerManagedPolicyReferenceProperty"]]]], jsii.get(self, "customerManagedPolicyReferences"))

    @customer_managed_policy_references.setter
    def customer_managed_policy_references(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnPermissionSet.CustomerManagedPolicyReferenceProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__003c123796d7c694a79f8c7ad67b2fdbcc38205eea6b333607e6795f42a8faaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerManagedPolicyReferences", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the ``PermissionSet`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e4059542e846ae4c1d4339af76208fc61018d99e88230b62c542d5e0263c56b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="inlinePolicy")
    def inline_policy(self) -> typing.Any:
        '''The inline policy that is attached to the permission set.'''
        return typing.cast(typing.Any, jsii.get(self, "inlinePolicy"))

    @inline_policy.setter
    def inline_policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfd17901eb138e14f182c4ab844dcd8717832f68c8170268869c64b310c7eb34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inlinePolicy", value)

    @builtins.property
    @jsii.member(jsii_name="managedPolicies")
    def managed_policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A structure that stores the details of the AWS managed policy.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "managedPolicies"))

    @managed_policies.setter
    def managed_policies(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a618b557b82a65ffd9b341061046eb4df83fe05a3fc4a6fa60588b53bb48c767)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedPolicies", value)

    @builtins.property
    @jsii.member(jsii_name="permissionsBoundary")
    def permissions_boundary(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPermissionSet.PermissionsBoundaryProperty"]]:
        '''Specifies the configuration of the AWS managed or customer managed policy that you want to set as a permissions boundary.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPermissionSet.PermissionsBoundaryProperty"]], jsii.get(self, "permissionsBoundary"))

    @permissions_boundary.setter
    def permissions_boundary(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPermissionSet.PermissionsBoundaryProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69e904509d69f8800277fa40e8b25cf92e223e7d126204001c65d9cd604910e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionsBoundary", value)

    @builtins.property
    @jsii.member(jsii_name="relayStateType")
    def relay_state_type(self) -> typing.Optional[builtins.str]:
        '''Used to redirect users within the application during the federation authentication process.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "relayStateType"))

    @relay_state_type.setter
    def relay_state_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70ffbaa6a5c797e7df5761098bd320efba28ea5faaa7c03d6978b7247009f362)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "relayStateType", value)

    @builtins.property
    @jsii.member(jsii_name="sessionDuration")
    def session_duration(self) -> typing.Optional[builtins.str]:
        '''The length of time that the application user sessions are valid for in the ISO-8601 standard.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sessionDuration"))

    @session_duration.setter
    def session_duration(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2f12d6109ebb8487bcde9da42e50f6362e3d27fa5f21ba8e4c9f5b81e351dcb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionDuration", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to attach to the new ``PermissionSet`` .'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7544016af765ff22f84936a0567273904ad2dfbeaf6338678ee91dbe144ac8df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sso.CfnPermissionSet.CustomerManagedPolicyReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "path": "path"},
    )
    class CustomerManagedPolicyReferenceProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the name and path of a customer managed policy.

            You must have an IAM policy that matches the name and path in each AWS account where you want to deploy your permission set.

            :param name: The name of the IAM policy that you have configured in each account where you want to deploy your permission set.
            :param path: The path to the IAM policy that you have configured in each account where you want to deploy your permission set. The default is ``/`` . For more information, see `Friendly names and paths <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names>`_ in the *IAM User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-customermanagedpolicyreference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sso as sso
                
                customer_managed_policy_reference_property = sso.CfnPermissionSet.CustomerManagedPolicyReferenceProperty(
                    name="name",
                
                    # the properties below are optional
                    path="path"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ea3280a736055861ef340265a02a46a37b9bcc72b4391912b8950ca8e1b74981)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if path is not None:
                self._values["path"] = path

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the IAM policy that you have configured in each account where you want to deploy your permission set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-customermanagedpolicyreference.html#cfn-sso-permissionset-customermanagedpolicyreference-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def path(self) -> typing.Optional[builtins.str]:
            '''The path to the IAM policy that you have configured in each account where you want to deploy your permission set.

            The default is ``/`` . For more information, see `Friendly names and paths <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-friendly-names>`_ in the *IAM User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-customermanagedpolicyreference.html#cfn-sso-permissionset-customermanagedpolicyreference-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomerManagedPolicyReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sso.CfnPermissionSet.PermissionsBoundaryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "customer_managed_policy_reference": "customerManagedPolicyReference",
            "managed_policy_arn": "managedPolicyArn",
        },
    )
    class PermissionsBoundaryProperty:
        def __init__(
            self,
            *,
            customer_managed_policy_reference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPermissionSet.CustomerManagedPolicyReferenceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            managed_policy_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the configuration of the AWS managed or customer managed policy that you want to set as a permissions boundary.

            Specify either ``CustomerManagedPolicyReference`` to use the name and path of a customer managed policy, or ``ManagedPolicyArn`` to use the ARN of an AWS managed policy. A permissions boundary represents the maximum permissions that any policy can grant your role. For more information, see `Permissions boundaries for IAM entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`_ in the *IAM User Guide* .
            .. epigraph::

               Policies used as permissions boundaries don't provide permissions. You must also attach an IAM policy to the role. To learn how the effective permissions for a role are evaluated, see `IAM JSON policy evaluation logic <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html>`_ in the *IAM User Guide* .

            :param customer_managed_policy_reference: Specifies the name and path of a customer managed policy. You must have an IAM policy that matches the name and path in each AWS account where you want to deploy your permission set.
            :param managed_policy_arn: The AWS managed policy ARN that you want to attach to a permission set as a permissions boundary.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-permissionsboundary.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sso as sso
                
                permissions_boundary_property = sso.CfnPermissionSet.PermissionsBoundaryProperty(
                    customer_managed_policy_reference=sso.CfnPermissionSet.CustomerManagedPolicyReferenceProperty(
                        name="name",
                
                        # the properties below are optional
                        path="path"
                    ),
                    managed_policy_arn="managedPolicyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3c2d8d05593bb4e7d39ec67bed0cc26753709cc6922b06793024dbd9a5dc0390)
                check_type(argname="argument customer_managed_policy_reference", value=customer_managed_policy_reference, expected_type=type_hints["customer_managed_policy_reference"])
                check_type(argname="argument managed_policy_arn", value=managed_policy_arn, expected_type=type_hints["managed_policy_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if customer_managed_policy_reference is not None:
                self._values["customer_managed_policy_reference"] = customer_managed_policy_reference
            if managed_policy_arn is not None:
                self._values["managed_policy_arn"] = managed_policy_arn

        @builtins.property
        def customer_managed_policy_reference(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPermissionSet.CustomerManagedPolicyReferenceProperty"]]:
            '''Specifies the name and path of a customer managed policy.

            You must have an IAM policy that matches the name and path in each AWS account where you want to deploy your permission set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-permissionsboundary.html#cfn-sso-permissionset-permissionsboundary-customermanagedpolicyreference
            '''
            result = self._values.get("customer_managed_policy_reference")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPermissionSet.CustomerManagedPolicyReferenceProperty"]], result)

        @builtins.property
        def managed_policy_arn(self) -> typing.Optional[builtins.str]:
            '''The AWS managed policy ARN that you want to attach to a permission set as a permissions boundary.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sso-permissionset-permissionsboundary.html#cfn-sso-permissionset-permissionsboundary-managedpolicyarn
            '''
            result = self._values.get("managed_policy_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PermissionsBoundaryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sso.CfnPermissionSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "name": "name",
        "customer_managed_policy_references": "customerManagedPolicyReferences",
        "description": "description",
        "inline_policy": "inlinePolicy",
        "managed_policies": "managedPolicies",
        "permissions_boundary": "permissionsBoundary",
        "relay_state_type": "relayStateType",
        "session_duration": "sessionDuration",
        "tags": "tags",
    },
)
class CfnPermissionSetProps:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        name: builtins.str,
        customer_managed_policy_references: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPermissionSet.CustomerManagedPolicyReferenceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        inline_policy: typing.Any = None,
        managed_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        permissions_boundary: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPermissionSet.PermissionsBoundaryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        relay_state_type: typing.Optional[builtins.str] = None,
        session_duration: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPermissionSet``.

        :param instance_arn: The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .
        :param name: The name of the permission set.
        :param customer_managed_policy_references: Specifies the names and paths of the customer managed policies that you have attached to your permission set.
        :param description: The description of the ``PermissionSet`` .
        :param inline_policy: The inline policy that is attached to the permission set. .. epigraph:: For ``Length Constraints`` , if a valid ARN is provided for a permission set, it is possible for an empty inline policy to be returned.
        :param managed_policies: A structure that stores the details of the AWS managed policy.
        :param permissions_boundary: Specifies the configuration of the AWS managed or customer managed policy that you want to set as a permissions boundary. Specify either ``CustomerManagedPolicyReference`` to use the name and path of a customer managed policy, or ``ManagedPolicyArn`` to use the ARN of an AWS managed policy. A permissions boundary represents the maximum permissions that any policy can grant your role. For more information, see `Permissions boundaries for IAM entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`_ in the *IAM User Guide* . .. epigraph:: Policies used as permissions boundaries don't provide permissions. You must also attach an IAM policy to the role. To learn how the effective permissions for a role are evaluated, see `IAM JSON policy evaluation logic <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html>`_ in the *IAM User Guide* .
        :param relay_state_type: Used to redirect users within the application during the federation authentication process.
        :param session_duration: The length of time that the application user sessions are valid for in the ISO-8601 standard.
        :param tags: The tags to attach to the new ``PermissionSet`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_sso as sso
            
            # inline_policy: Any
            
            cfn_permission_set_props = sso.CfnPermissionSetProps(
                instance_arn="instanceArn",
                name="name",
            
                # the properties below are optional
                customer_managed_policy_references=[sso.CfnPermissionSet.CustomerManagedPolicyReferenceProperty(
                    name="name",
            
                    # the properties below are optional
                    path="path"
                )],
                description="description",
                inline_policy=inline_policy,
                managed_policies=["managedPolicies"],
                permissions_boundary=sso.CfnPermissionSet.PermissionsBoundaryProperty(
                    customer_managed_policy_reference=sso.CfnPermissionSet.CustomerManagedPolicyReferenceProperty(
                        name="name",
            
                        # the properties below are optional
                        path="path"
                    ),
                    managed_policy_arn="managedPolicyArn"
                ),
                relay_state_type="relayStateType",
                session_duration="sessionDuration",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f756abcc5c1aa2acf7ae657bd2a8618f372584120d70c190b245e0a01f835d13)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument customer_managed_policy_references", value=customer_managed_policy_references, expected_type=type_hints["customer_managed_policy_references"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument inline_policy", value=inline_policy, expected_type=type_hints["inline_policy"])
            check_type(argname="argument managed_policies", value=managed_policies, expected_type=type_hints["managed_policies"])
            check_type(argname="argument permissions_boundary", value=permissions_boundary, expected_type=type_hints["permissions_boundary"])
            check_type(argname="argument relay_state_type", value=relay_state_type, expected_type=type_hints["relay_state_type"])
            check_type(argname="argument session_duration", value=session_duration, expected_type=type_hints["session_duration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_arn": instance_arn,
            "name": name,
        }
        if customer_managed_policy_references is not None:
            self._values["customer_managed_policy_references"] = customer_managed_policy_references
        if description is not None:
            self._values["description"] = description
        if inline_policy is not None:
            self._values["inline_policy"] = inline_policy
        if managed_policies is not None:
            self._values["managed_policies"] = managed_policies
        if permissions_boundary is not None:
            self._values["permissions_boundary"] = permissions_boundary
        if relay_state_type is not None:
            self._values["relay_state_type"] = relay_state_type
        if session_duration is not None:
            self._values["session_duration"] = session_duration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The ARN of the IAM Identity Center instance under which the operation will be executed.

        For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-instancearn
        '''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the permission set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def customer_managed_policy_references(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPermissionSet.CustomerManagedPolicyReferenceProperty]]]]:
        '''Specifies the names and paths of the customer managed policies that you have attached to your permission set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-customermanagedpolicyreferences
        '''
        result = self._values.get("customer_managed_policy_references")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPermissionSet.CustomerManagedPolicyReferenceProperty]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the ``PermissionSet`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inline_policy(self) -> typing.Any:
        '''The inline policy that is attached to the permission set.

        .. epigraph::

           For ``Length Constraints`` , if a valid ARN is provided for a permission set, it is possible for an empty inline policy to be returned.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-inlinepolicy
        '''
        result = self._values.get("inline_policy")
        return typing.cast(typing.Any, result)

    @builtins.property
    def managed_policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A structure that stores the details of the AWS managed policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-managedpolicies
        '''
        result = self._values.get("managed_policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def permissions_boundary(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPermissionSet.PermissionsBoundaryProperty]]:
        '''Specifies the configuration of the AWS managed or customer managed policy that you want to set as a permissions boundary.

        Specify either ``CustomerManagedPolicyReference`` to use the name and path of a customer managed policy, or ``ManagedPolicyArn`` to use the ARN of an AWS managed policy. A permissions boundary represents the maximum permissions that any policy can grant your role. For more information, see `Permissions boundaries for IAM entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html>`_ in the *IAM User Guide* .
        .. epigraph::

           Policies used as permissions boundaries don't provide permissions. You must also attach an IAM policy to the role. To learn how the effective permissions for a role are evaluated, see `IAM JSON policy evaluation logic <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html>`_ in the *IAM User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-permissionsboundary
        '''
        result = self._values.get("permissions_boundary")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPermissionSet.PermissionsBoundaryProperty]], result)

    @builtins.property
    def relay_state_type(self) -> typing.Optional[builtins.str]:
        '''Used to redirect users within the application during the federation authentication process.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-relaystatetype
        '''
        result = self._values.get("relay_state_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_duration(self) -> typing.Optional[builtins.str]:
        '''The length of time that the application user sessions are valid for in the ISO-8601 standard.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-sessionduration
        '''
        result = self._values.get("session_duration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to attach to the new ``PermissionSet`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPermissionSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAssignment",
    "CfnAssignmentProps",
    "CfnInstanceAccessControlAttributeConfiguration",
    "CfnInstanceAccessControlAttributeConfigurationProps",
    "CfnPermissionSet",
    "CfnPermissionSetProps",
]

publication.publish()

def _typecheckingstub__ebef8d250e1dbc37b65303c039a5211da7116d20618441b3967d658d6503e2f7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_arn: builtins.str,
    permission_set_arn: builtins.str,
    principal_id: builtins.str,
    principal_type: builtins.str,
    target_id: builtins.str,
    target_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4498cc8fea0c97daa31af89de3f9064e1df7f1b3b2653d46b31fae4287c164c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5488690a5d03065e9d831a867c6d3f7449e711f5e04ccd2e4dd4dea7ca2ba062(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17b623ed0ec409c3a71b2b1b8cf18292a2895708cc1d2c53fa253b69ad8a53a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b072b296fcdca1fa35643b12cfd3604849aa9d27f63f391f25f57164791ded77(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c490e4155227ea07d5c9d9bcf224a24225f358240ac2bd91930762202bbc3c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__619026097393449b13624a247638924ced09bc52d9bded17b98c0a9cd00f4f68(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5d7c01434a58be26f030bbbb4c4bac0441e711f4c1b954e921cff5db2a357eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d31c013e59de3e5493f34c329933cda7b9c6ded610ef1e183427cd7d14cfe8e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af8b1b897ea9ab77a0f2e4bab0d57a02afda473ba2e2680b392d3403bd006adb(
    *,
    instance_arn: builtins.str,
    permission_set_arn: builtins.str,
    principal_id: builtins.str,
    principal_type: builtins.str,
    target_id: builtins.str,
    target_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f7a7752ad192f44dab8a4f16ca8392acad24cb912eaff617dbf10c8149c7542(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_arn: builtins.str,
    access_control_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    instance_access_control_attribute_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceAccessControlAttributeConfiguration.InstanceAccessControlAttributeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c48b94299d1ffa1f7049b0b5d63f78b836162a06a724a75f0c82d165e2c138b6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea6a2ed55e2a55ee0c5d3955b4f881b8cf8aadf484955c56c4224ebeed434953(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8794fbca8fffc39a5bb8822215af2d986460d2139e6f7f6b8518fe0b4f77389(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59b30bff10a4ad495a4848654c3d5cc319a787641db9697ed37a6ff4afa259b3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f70c314997f8ad880ed6373ea4fdd6e57467d1c9f2a6df1941fcce50c8b74442(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInstanceAccessControlAttributeConfiguration.InstanceAccessControlAttributeConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3186d8e26bd7fcbe036cbc3233a43b4bf3854aa2190d5888364286ed51720381(
    *,
    key: builtins.str,
    value: typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeValueProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2820ec077bbb0783624f9db7c803955332448280274edfd9bfda9ad015b81967(
    *,
    source: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ef22662569985de541e712d397e178367db6e4386936c4b934aaa6392c6aa3b(
    *,
    access_control_attributes: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__814fa18856a1f832fbf758087fb132fbc281321791aa0253818b3fa514682b45(
    *,
    instance_arn: builtins.str,
    access_control_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceAccessControlAttributeConfiguration.AccessControlAttributeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    instance_access_control_attribute_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInstanceAccessControlAttributeConfiguration.InstanceAccessControlAttributeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29742c4712f9aeed238f180c9db8677986b9e95f63644b8358d20bbe6f9f8c9d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    instance_arn: builtins.str,
    name: builtins.str,
    customer_managed_policy_references: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPermissionSet.CustomerManagedPolicyReferenceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    inline_policy: typing.Any = None,
    managed_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    permissions_boundary: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPermissionSet.PermissionsBoundaryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    relay_state_type: typing.Optional[builtins.str] = None,
    session_duration: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41af3694bf258cce2eec00f3796e70405f43f39c22f5563c380367005e925825(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cacdbbe8633389e9abfb49528d132366b3e7cd1904ca9b9142ff94e947907357(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f097006770b4dc8eb39790dbe3afd4885f8cf745ad922489ed434c6f02ba81cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9317633963da92f7e1e0f006966e8f9bfb827bca42dd01644d334d1607ac85f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__003c123796d7c694a79f8c7ad67b2fdbcc38205eea6b333607e6795f42a8faaf(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPermissionSet.CustomerManagedPolicyReferenceProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e4059542e846ae4c1d4339af76208fc61018d99e88230b62c542d5e0263c56b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfd17901eb138e14f182c4ab844dcd8717832f68c8170268869c64b310c7eb34(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a618b557b82a65ffd9b341061046eb4df83fe05a3fc4a6fa60588b53bb48c767(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69e904509d69f8800277fa40e8b25cf92e223e7d126204001c65d9cd604910e0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPermissionSet.PermissionsBoundaryProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70ffbaa6a5c797e7df5761098bd320efba28ea5faaa7c03d6978b7247009f362(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2f12d6109ebb8487bcde9da42e50f6362e3d27fa5f21ba8e4c9f5b81e351dcb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7544016af765ff22f84936a0567273904ad2dfbeaf6338678ee91dbe144ac8df(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea3280a736055861ef340265a02a46a37b9bcc72b4391912b8950ca8e1b74981(
    *,
    name: builtins.str,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c2d8d05593bb4e7d39ec67bed0cc26753709cc6922b06793024dbd9a5dc0390(
    *,
    customer_managed_policy_reference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPermissionSet.CustomerManagedPolicyReferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    managed_policy_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f756abcc5c1aa2acf7ae657bd2a8618f372584120d70c190b245e0a01f835d13(
    *,
    instance_arn: builtins.str,
    name: builtins.str,
    customer_managed_policy_references: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPermissionSet.CustomerManagedPolicyReferenceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    inline_policy: typing.Any = None,
    managed_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
    permissions_boundary: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPermissionSet.PermissionsBoundaryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    relay_state_type: typing.Optional[builtins.str] = None,
    session_duration: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
