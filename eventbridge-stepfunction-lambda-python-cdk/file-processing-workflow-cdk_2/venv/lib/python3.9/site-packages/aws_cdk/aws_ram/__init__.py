'''
# AWS Resource Access Manager Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_ram as ram
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for RAM construct libraries](https://constructs.dev/search?q=ram)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::RAM resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RAM.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::RAM](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RAM.html).

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
class CfnPermission(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ram.CfnPermission",
):
    '''Creates a customer managed permission for a specified resource type that you can attach to resource shares.

    It is created in the AWS Region in which you call the operation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-permission.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ram as ram
        
        # policy_template: Any
        
        cfn_permission = ram.CfnPermission(self, "MyCfnPermission",
            name="name",
            policy_template=policy_template,
            resource_type="resourceType",
        
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
        name: builtins.str,
        policy_template: typing.Any,
        resource_type: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: Specifies the name of the customer managed permission. The name must be unique within the AWS Region .
        :param policy_template: A string in JSON format string that contains the following elements of a resource-based policy:. - *Effect* : must be set to ``ALLOW`` . - *Action* : specifies the actions that are allowed by this customer managed permission. The list must contain only actions that are supported by the specified resource type. For a list of all actions supported by each resource type, see `Actions, resources, and condition keys for AWS services <https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html>`_ in the *AWS Identity and Access Management User Guide* . - *Condition* : (optional) specifies conditional parameters that must evaluate to true when a user attempts an action for that action to be allowed. For more information about the Condition element, see `IAM policies: Condition element <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html>`_ in the *AWS Identity and Access Management User Guide* . This template can't include either the ``Resource`` or ``Principal`` elements. Those are both filled in by AWS RAM when it instantiates the resource-based policy on each resource shared using this managed permission. The ``Resource`` comes from the ARN of the specific resource that you are sharing. The ``Principal`` comes from the list of identities added to the resource share.
        :param resource_type: Specifies the name of the resource type that this customer managed permission applies to. The format is ``*<service-code>* : *<resource-type>*`` and is not case sensitive. For example, to specify an Amazon EC2 Subnet, you can use the string ``ec2:subnet`` . To see the list of valid values for this parameter, query the `ListResourceTypes <https://docs.aws.amazon.com/ram/latest/APIReference/API_ListResourceTypes.html>`_ operation.
        :param tags: Specifies a list of one or more tag key and value pairs to attach to the permission.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e6fe3eae2e441449bee4fa9cdbdbd3fa3faa77d6312d1d0b6173f4ab5e4f62c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPermissionProps(
            name=name,
            policy_template=policy_template,
            resource_type=resource_type,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d951b94e05f47918844ee4c94dafebba369732ccc302f7ad923dca32b5000fc7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b815722571219a975ded0c832e480c433d1106c5c3874c31f41a623df4840bef)
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
        '''The Amazon Resource Name (ARN) of the new permission.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrIsResourceTypeDefault")
    def attr_is_resource_type_default(self) -> _IResolvable_da3f097b:
        '''Specifies whether this permission is the default for new resource shares that include resources of the associated resource type.

        :cloudformationAttribute: IsResourceTypeDefault
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrIsResourceTypeDefault"))

    @builtins.property
    @jsii.member(jsii_name="attrPermissionType")
    def attr_permission_type(self) -> builtins.str:
        '''The type of managed permission. This can be one of the following values:.

        - *AWS_MANAGED_PERMISSION* – AWS created and manages this managed permission. You can associate it with your resource shares, but you can't modify it.
        - *CUSTOMER_MANAGED_PERMISSION* – You, or another principal in your account created this managed permission. You can associate it with your resource shares and create new versions that have different permissions.

        :cloudformationAttribute: PermissionType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPermissionType"))

    @builtins.property
    @jsii.member(jsii_name="attrVersion")
    def attr_version(self) -> builtins.str:
        '''The version number for this version of the permission.

        :cloudformationAttribute: Version
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVersion"))

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
        '''Specifies the name of the customer managed permission.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__952aaf926012eb44626e889296cc608af4a071943b783cc37c41445ba67cacbd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="policyTemplate")
    def policy_template(self) -> typing.Any:
        '''A string in JSON format string that contains the following elements of a resource-based policy:.'''
        return typing.cast(typing.Any, jsii.get(self, "policyTemplate"))

    @policy_template.setter
    def policy_template(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d786ce0393d6d5e9b23b457d7d296ea4e1b64dde74cbe0351155d84dbe06a21b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        '''Specifies the name of the resource type that this customer managed permission applies to.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @resource_type.setter
    def resource_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d012bd3d642b7557eafa85e0a130a59f59fd9bf570abb055165847be25a9e515)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceType", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies a list of one or more tag key and value pairs to attach to the permission.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e38f5af40d9dfeea4630580bc03fc46db30f305dafe61dc85a0a22e71eb103d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ram.CfnPermissionProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "policy_template": "policyTemplate",
        "resource_type": "resourceType",
        "tags": "tags",
    },
)
class CfnPermissionProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        policy_template: typing.Any,
        resource_type: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPermission``.

        :param name: Specifies the name of the customer managed permission. The name must be unique within the AWS Region .
        :param policy_template: A string in JSON format string that contains the following elements of a resource-based policy:. - *Effect* : must be set to ``ALLOW`` . - *Action* : specifies the actions that are allowed by this customer managed permission. The list must contain only actions that are supported by the specified resource type. For a list of all actions supported by each resource type, see `Actions, resources, and condition keys for AWS services <https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html>`_ in the *AWS Identity and Access Management User Guide* . - *Condition* : (optional) specifies conditional parameters that must evaluate to true when a user attempts an action for that action to be allowed. For more information about the Condition element, see `IAM policies: Condition element <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html>`_ in the *AWS Identity and Access Management User Guide* . This template can't include either the ``Resource`` or ``Principal`` elements. Those are both filled in by AWS RAM when it instantiates the resource-based policy on each resource shared using this managed permission. The ``Resource`` comes from the ARN of the specific resource that you are sharing. The ``Principal`` comes from the list of identities added to the resource share.
        :param resource_type: Specifies the name of the resource type that this customer managed permission applies to. The format is ``*<service-code>* : *<resource-type>*`` and is not case sensitive. For example, to specify an Amazon EC2 Subnet, you can use the string ``ec2:subnet`` . To see the list of valid values for this parameter, query the `ListResourceTypes <https://docs.aws.amazon.com/ram/latest/APIReference/API_ListResourceTypes.html>`_ operation.
        :param tags: Specifies a list of one or more tag key and value pairs to attach to the permission.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-permission.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ram as ram
            
            # policy_template: Any
            
            cfn_permission_props = ram.CfnPermissionProps(
                name="name",
                policy_template=policy_template,
                resource_type="resourceType",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9e72a90559f1f4c0f547098b5369dbfeed98afe29faf887a6f20cad208db7e3)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument policy_template", value=policy_template, expected_type=type_hints["policy_template"])
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "policy_template": policy_template,
            "resource_type": resource_type,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''Specifies the name of the customer managed permission.

        The name must be unique within the AWS Region .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-permission.html#cfn-ram-permission-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_template(self) -> typing.Any:
        '''A string in JSON format string that contains the following elements of a resource-based policy:.

        - *Effect* : must be set to ``ALLOW`` .
        - *Action* : specifies the actions that are allowed by this customer managed permission. The list must contain only actions that are supported by the specified resource type. For a list of all actions supported by each resource type, see `Actions, resources, and condition keys for AWS services <https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html>`_ in the *AWS Identity and Access Management User Guide* .
        - *Condition* : (optional) specifies conditional parameters that must evaluate to true when a user attempts an action for that action to be allowed. For more information about the Condition element, see `IAM policies: Condition element <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html>`_ in the *AWS Identity and Access Management User Guide* .

        This template can't include either the ``Resource`` or ``Principal`` elements. Those are both filled in by AWS RAM when it instantiates the resource-based policy on each resource shared using this managed permission. The ``Resource`` comes from the ARN of the specific resource that you are sharing. The ``Principal`` comes from the list of identities added to the resource share.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-permission.html#cfn-ram-permission-policytemplate
        '''
        result = self._values.get("policy_template")
        assert result is not None, "Required property 'policy_template' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def resource_type(self) -> builtins.str:
        '''Specifies the name of the resource type that this customer managed permission applies to.

        The format is ``*<service-code>* : *<resource-type>*`` and is not case sensitive. For example, to specify an Amazon EC2 Subnet, you can use the string ``ec2:subnet`` . To see the list of valid values for this parameter, query the `ListResourceTypes <https://docs.aws.amazon.com/ram/latest/APIReference/API_ListResourceTypes.html>`_ operation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-permission.html#cfn-ram-permission-resourcetype
        '''
        result = self._values.get("resource_type")
        assert result is not None, "Required property 'resource_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies a list of one or more tag key and value pairs to attach to the permission.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-permission.html#cfn-ram-permission-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPermissionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnResourceShare(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ram.CfnResourceShare",
):
    '''Creates a resource share.

    You can provide a list of the Amazon Resource Names (ARNs) for the resources that you want to share, a list of principals you want to share the resources with, and the permissions to grant those principals.
    .. epigraph::

       Sharing a resource makes it available for use by principals outside of the AWS account that created the resource. Sharing doesn't change any permissions or quotas that apply to the resource in the account that created it.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ram as ram
        
        cfn_resource_share = ram.CfnResourceShare(self, "MyCfnResourceShare",
            name="name",
        
            # the properties below are optional
            allow_external_principals=False,
            permission_arns=["permissionArns"],
            principals=["principals"],
            resource_arns=["resourceArns"],
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
        allow_external_principals: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        permission_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        principals: typing.Optional[typing.Sequence[builtins.str]] = None,
        resource_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: Specifies the name of the resource share.
        :param allow_external_principals: Specifies whether principals outside your organization in AWS Organizations can be associated with a resource share. A value of ``true`` lets you share with individual AWS accounts that are *not* in your organization. A value of ``false`` only has meaning if your account is a member of an AWS Organization. The default value is ``true`` .
        :param permission_arns: Specifies the `Amazon Resource Names (ARNs) <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ of the AWS RAM permission to associate with the resource share. If you do not specify an ARN for the permission, AWS RAM automatically attaches the default version of the permission for each resource type. You can associate only one permission with each resource type included in the resource share.
        :param principals: Specifies the principals to associate with the resource share. The possible values are:. - An AWS account ID - An Amazon Resource Name (ARN) of an organization in AWS Organizations - An ARN of an organizational unit (OU) in AWS Organizations - An ARN of an IAM role - An ARN of an IAM user .. epigraph:: Not all resource types can be shared with IAM roles and users. For more information, see the column *Can share with IAM roles and users* in the tables on `Shareable AWS resources <https://docs.aws.amazon.com/ram/latest/userguide/shareable.html>`_ in the *AWS Resource Access Manager User Guide* .
        :param resource_arns: Specifies a list of one or more ARNs of the resources to associate with the resource share.
        :param tags: Specifies one or more tags to attach to the resource share itself. It doesn't attach the tags to the resources associated with the resource share.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fea9cca1996f068f8dde2c34bf4c41d370ee8638f9da1d855f8b0022d75af5d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourceShareProps(
            name=name,
            allow_external_principals=allow_external_principals,
            permission_arns=permission_arns,
            principals=principals,
            resource_arns=resource_arns,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8defbc280b992fb09ff90651c627ce1c4211d498c66f7c4b62a4b3a5285f92d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e124e85df525ca5d702f0b9a2b5bb739a12519bf552f8ea08a9f673f4077d696)
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
        '''The Amazon Resource Name (ARN) of the resource share.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''Specifies the name of the resource share.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb76bd909afa4dee66debdd78e087883e909ff481a0f08820b4aee17388a74e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="allowExternalPrincipals")
    def allow_external_principals(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether principals outside your organization in AWS Organizations can be associated with a resource share.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "allowExternalPrincipals"))

    @allow_external_principals.setter
    def allow_external_principals(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a8ac8ee18a992b418a8b6fc421772eee1a5d5b0b675ccfe6c0ce0c7f18b40e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowExternalPrincipals", value)

    @builtins.property
    @jsii.member(jsii_name="permissionArns")
    def permission_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the `Amazon Resource Names (ARNs) <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ of the AWS RAM permission to associate with the resource share. If you do not specify an ARN for the permission, AWS RAM automatically attaches the default version of the permission for each resource type. You can associate only one permission with each resource type included in the resource share.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "permissionArns"))

    @permission_arns.setter
    def permission_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__411d88d3990f34296ef5770eb3cb3792a55b6b7805c6e7381207750e8fa15042)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionArns", value)

    @builtins.property
    @jsii.member(jsii_name="principals")
    def principals(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the principals to associate with the resource share.

        The possible values are:.
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "principals"))

    @principals.setter
    def principals(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27e4971e92d1679357249799c9998f6cde7d19d4a39eec3a7d952e11f95d0b64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principals", value)

    @builtins.property
    @jsii.member(jsii_name="resourceArns")
    def resource_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of one or more ARNs of the resources to associate with the resource share.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceArns"))

    @resource_arns.setter
    def resource_arns(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebcfa059a044b9468256f95fd1dc2d90bce40e3d6d96d59d1755b38b7d15db67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArns", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies one or more tags to attach to the resource share itself.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e8df76745e5c0758e8b5233e879c50ee5a6f6f817a0850af55da2744c10ef55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ram.CfnResourceShareProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "allow_external_principals": "allowExternalPrincipals",
        "permission_arns": "permissionArns",
        "principals": "principals",
        "resource_arns": "resourceArns",
        "tags": "tags",
    },
)
class CfnResourceShareProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        allow_external_principals: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        permission_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        principals: typing.Optional[typing.Sequence[builtins.str]] = None,
        resource_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnResourceShare``.

        :param name: Specifies the name of the resource share.
        :param allow_external_principals: Specifies whether principals outside your organization in AWS Organizations can be associated with a resource share. A value of ``true`` lets you share with individual AWS accounts that are *not* in your organization. A value of ``false`` only has meaning if your account is a member of an AWS Organization. The default value is ``true`` .
        :param permission_arns: Specifies the `Amazon Resource Names (ARNs) <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ of the AWS RAM permission to associate with the resource share. If you do not specify an ARN for the permission, AWS RAM automatically attaches the default version of the permission for each resource type. You can associate only one permission with each resource type included in the resource share.
        :param principals: Specifies the principals to associate with the resource share. The possible values are:. - An AWS account ID - An Amazon Resource Name (ARN) of an organization in AWS Organizations - An ARN of an organizational unit (OU) in AWS Organizations - An ARN of an IAM role - An ARN of an IAM user .. epigraph:: Not all resource types can be shared with IAM roles and users. For more information, see the column *Can share with IAM roles and users* in the tables on `Shareable AWS resources <https://docs.aws.amazon.com/ram/latest/userguide/shareable.html>`_ in the *AWS Resource Access Manager User Guide* .
        :param resource_arns: Specifies a list of one or more ARNs of the resources to associate with the resource share.
        :param tags: Specifies one or more tags to attach to the resource share itself. It doesn't attach the tags to the resources associated with the resource share.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ram as ram
            
            cfn_resource_share_props = ram.CfnResourceShareProps(
                name="name",
            
                # the properties below are optional
                allow_external_principals=False,
                permission_arns=["permissionArns"],
                principals=["principals"],
                resource_arns=["resourceArns"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a74e87907f43c8b632de2f93b4560b166f51134fc5a47c6f4892e716a268961a)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument allow_external_principals", value=allow_external_principals, expected_type=type_hints["allow_external_principals"])
            check_type(argname="argument permission_arns", value=permission_arns, expected_type=type_hints["permission_arns"])
            check_type(argname="argument principals", value=principals, expected_type=type_hints["principals"])
            check_type(argname="argument resource_arns", value=resource_arns, expected_type=type_hints["resource_arns"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if allow_external_principals is not None:
            self._values["allow_external_principals"] = allow_external_principals
        if permission_arns is not None:
            self._values["permission_arns"] = permission_arns
        if principals is not None:
            self._values["principals"] = principals
        if resource_arns is not None:
            self._values["resource_arns"] = resource_arns
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''Specifies the name of the resource share.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html#cfn-ram-resourceshare-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_external_principals(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether principals outside your organization in AWS Organizations can be associated with a resource share.

        A value of ``true`` lets you share with individual AWS accounts that are *not* in your organization. A value of ``false`` only has meaning if your account is a member of an AWS Organization. The default value is ``true`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html#cfn-ram-resourceshare-allowexternalprincipals
        '''
        result = self._values.get("allow_external_principals")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def permission_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the `Amazon Resource Names (ARNs) <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ of the AWS RAM permission to associate with the resource share. If you do not specify an ARN for the permission, AWS RAM automatically attaches the default version of the permission for each resource type. You can associate only one permission with each resource type included in the resource share.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html#cfn-ram-resourceshare-permissionarns
        '''
        result = self._values.get("permission_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def principals(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the principals to associate with the resource share. The possible values are:.

        - An AWS account ID
        - An Amazon Resource Name (ARN) of an organization in AWS Organizations
        - An ARN of an organizational unit (OU) in AWS Organizations
        - An ARN of an IAM role
        - An ARN of an IAM user

        .. epigraph::

           Not all resource types can be shared with IAM roles and users. For more information, see the column *Can share with IAM roles and users* in the tables on `Shareable AWS resources <https://docs.aws.amazon.com/ram/latest/userguide/shareable.html>`_ in the *AWS Resource Access Manager User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html#cfn-ram-resourceshare-principals
        '''
        result = self._values.get("principals")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def resource_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies a list of one or more ARNs of the resources to associate with the resource share.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html#cfn-ram-resourceshare-resourcearns
        '''
        result = self._values.get("resource_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies one or more tags to attach to the resource share itself.

        It doesn't attach the tags to the resources associated with the resource share.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html#cfn-ram-resourceshare-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourceShareProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnPermission",
    "CfnPermissionProps",
    "CfnResourceShare",
    "CfnResourceShareProps",
]

publication.publish()

def _typecheckingstub__4e6fe3eae2e441449bee4fa9cdbdbd3fa3faa77d6312d1d0b6173f4ab5e4f62c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    policy_template: typing.Any,
    resource_type: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d951b94e05f47918844ee4c94dafebba369732ccc302f7ad923dca32b5000fc7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b815722571219a975ded0c832e480c433d1106c5c3874c31f41a623df4840bef(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__952aaf926012eb44626e889296cc608af4a071943b783cc37c41445ba67cacbd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d786ce0393d6d5e9b23b457d7d296ea4e1b64dde74cbe0351155d84dbe06a21b(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d012bd3d642b7557eafa85e0a130a59f59fd9bf570abb055165847be25a9e515(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e38f5af40d9dfeea4630580bc03fc46db30f305dafe61dc85a0a22e71eb103d(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9e72a90559f1f4c0f547098b5369dbfeed98afe29faf887a6f20cad208db7e3(
    *,
    name: builtins.str,
    policy_template: typing.Any,
    resource_type: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fea9cca1996f068f8dde2c34bf4c41d370ee8638f9da1d855f8b0022d75af5d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    allow_external_principals: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    permission_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    principals: typing.Optional[typing.Sequence[builtins.str]] = None,
    resource_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8defbc280b992fb09ff90651c627ce1c4211d498c66f7c4b62a4b3a5285f92d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e124e85df525ca5d702f0b9a2b5bb739a12519bf552f8ea08a9f673f4077d696(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb76bd909afa4dee66debdd78e087883e909ff481a0f08820b4aee17388a74e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a8ac8ee18a992b418a8b6fc421772eee1a5d5b0b675ccfe6c0ce0c7f18b40e7(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__411d88d3990f34296ef5770eb3cb3792a55b6b7805c6e7381207750e8fa15042(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27e4971e92d1679357249799c9998f6cde7d19d4a39eec3a7d952e11f95d0b64(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebcfa059a044b9468256f95fd1dc2d90bce40e3d6d96d59d1755b38b7d15db67(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e8df76745e5c0758e8b5233e879c50ee5a6f6f817a0850af55da2744c10ef55(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a74e87907f43c8b632de2f93b4560b166f51134fc5a47c6f4892e716a268961a(
    *,
    name: builtins.str,
    allow_external_principals: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    permission_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    principals: typing.Optional[typing.Sequence[builtins.str]] = None,
    resource_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
