'''
# AWS::Proton Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_proton as proton
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Proton construct libraries](https://constructs.dev/search?q=proton)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Proton resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Proton.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Proton](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Proton.html).

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
    ITaggable as _ITaggable_36806126,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnEnvironmentAccountConnection(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_proton.CfnEnvironmentAccountConnection",
):
    '''Detailed data of an AWS Proton environment account connection resource.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-environmentaccountconnection.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_proton as proton
        
        cfn_environment_account_connection = proton.CfnEnvironmentAccountConnection(self, "MyCfnEnvironmentAccountConnection",
            codebuild_role_arn="codebuildRoleArn",
            component_role_arn="componentRoleArn",
            environment_account_id="environmentAccountId",
            environment_name="environmentName",
            management_account_id="managementAccountId",
            role_arn="roleArn",
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
        codebuild_role_arn: typing.Optional[builtins.str] = None,
        component_role_arn: typing.Optional[builtins.str] = None,
        environment_account_id: typing.Optional[builtins.str] = None,
        environment_name: typing.Optional[builtins.str] = None,
        management_account_id: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param codebuild_role_arn: The Amazon Resource Name (ARN) of an IAM service role in the environment account. AWS Proton uses this role to provision infrastructure resources using CodeBuild-based provisioning in the associated environment account.
        :param component_role_arn: The Amazon Resource Name (ARN) of the IAM service role that AWS Proton uses when provisioning directly defined components in the associated environment account. It determines the scope of infrastructure that a component can provision in the account. The environment account connection must have a ``componentRoleArn`` to allow directly defined components to be associated with any environments running in the account. For more information about components, see `AWS Proton components <https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html>`_ in the *AWS Proton User Guide* .
        :param environment_account_id: The environment account that's connected to the environment account connection.
        :param environment_name: The name of the environment that's associated with the environment account connection.
        :param management_account_id: The ID of the management account that's connected to the environment account connection.
        :param role_arn: The IAM service role that's associated with the environment account connection.
        :param tags: An optional list of metadata items that you can associate with the AWS Proton environment account connection. A tag is a key-value pair. For more information, see `AWS Proton resources and tagging <https://docs.aws.amazon.com/proton/latest/userguide/resources.html>`_ in the *AWS Proton User Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__826262668de499159f2330eeadab45eb7cc0e3ce5dab7cadd5a4853b4856820b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnvironmentAccountConnectionProps(
            codebuild_role_arn=codebuild_role_arn,
            component_role_arn=component_role_arn,
            environment_account_id=environment_account_id,
            environment_name=environment_name,
            management_account_id=management_account_id,
            role_arn=role_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b30ec85df499b3f87a92d53ab1648560e2495ee044a1fb86faf3008181494293)
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
            type_hints = typing.get_type_hints(_typecheckingstub__470395ff1b3bc54712f215fb1b2f6214bb182bd963a863176e86d9a96c0f1972)
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
        '''Returns the environment account connection ARN.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Returns the environment account connection ID.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''Returns the environment account connection status.

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
    @jsii.member(jsii_name="codebuildRoleArn")
    def codebuild_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of an IAM service role in the environment account.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "codebuildRoleArn"))

    @codebuild_role_arn.setter
    def codebuild_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47f4e15b8378b0030dc5e8be607efef26d4e7bc41f9bc4d16a82239ecce2af2e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "codebuildRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="componentRoleArn")
    def component_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the IAM service role that AWS Proton uses when provisioning directly defined components in the associated environment account.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "componentRoleArn"))

    @component_role_arn.setter
    def component_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b976b51e7ad9d2668f5e11057b8add49417ccb62f9ec6ee2a16bfdf2cb4dab1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "componentRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="environmentAccountId")
    def environment_account_id(self) -> typing.Optional[builtins.str]:
        '''The environment account that's connected to the environment account connection.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentAccountId"))

    @environment_account_id.setter
    def environment_account_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36ad911396cde9a5836f2bf5c2178028454c62766b60ac3747357e9c24e96de8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="environmentName")
    def environment_name(self) -> typing.Optional[builtins.str]:
        '''The name of the environment that's associated with the environment account connection.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentName"))

    @environment_name.setter
    def environment_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d94be46146198fddc9c899c0dade14c643b597a9839643b3cc6c9f144935c502)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentName", value)

    @builtins.property
    @jsii.member(jsii_name="managementAccountId")
    def management_account_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the management account that's connected to the environment account connection.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managementAccountId"))

    @management_account_id.setter
    def management_account_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cbf14273aade064dc4e71967934b15a396069e1c949a15c0436c98dd68e54c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managementAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The IAM service role that's associated with the environment account connection.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37b19867aae52947f0d449ddee0fce5ac822cd037dbd498834aaf9268ddd0cf1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional list of metadata items that you can associate with the AWS Proton environment account connection.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__952d5d229754748fd9299ff4728f53f331581c6208e0c33caa4616b211155911)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_proton.CfnEnvironmentAccountConnectionProps",
    jsii_struct_bases=[],
    name_mapping={
        "codebuild_role_arn": "codebuildRoleArn",
        "component_role_arn": "componentRoleArn",
        "environment_account_id": "environmentAccountId",
        "environment_name": "environmentName",
        "management_account_id": "managementAccountId",
        "role_arn": "roleArn",
        "tags": "tags",
    },
)
class CfnEnvironmentAccountConnectionProps:
    def __init__(
        self,
        *,
        codebuild_role_arn: typing.Optional[builtins.str] = None,
        component_role_arn: typing.Optional[builtins.str] = None,
        environment_account_id: typing.Optional[builtins.str] = None,
        environment_name: typing.Optional[builtins.str] = None,
        management_account_id: typing.Optional[builtins.str] = None,
        role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEnvironmentAccountConnection``.

        :param codebuild_role_arn: The Amazon Resource Name (ARN) of an IAM service role in the environment account. AWS Proton uses this role to provision infrastructure resources using CodeBuild-based provisioning in the associated environment account.
        :param component_role_arn: The Amazon Resource Name (ARN) of the IAM service role that AWS Proton uses when provisioning directly defined components in the associated environment account. It determines the scope of infrastructure that a component can provision in the account. The environment account connection must have a ``componentRoleArn`` to allow directly defined components to be associated with any environments running in the account. For more information about components, see `AWS Proton components <https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html>`_ in the *AWS Proton User Guide* .
        :param environment_account_id: The environment account that's connected to the environment account connection.
        :param environment_name: The name of the environment that's associated with the environment account connection.
        :param management_account_id: The ID of the management account that's connected to the environment account connection.
        :param role_arn: The IAM service role that's associated with the environment account connection.
        :param tags: An optional list of metadata items that you can associate with the AWS Proton environment account connection. A tag is a key-value pair. For more information, see `AWS Proton resources and tagging <https://docs.aws.amazon.com/proton/latest/userguide/resources.html>`_ in the *AWS Proton User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-environmentaccountconnection.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_proton as proton
            
            cfn_environment_account_connection_props = proton.CfnEnvironmentAccountConnectionProps(
                codebuild_role_arn="codebuildRoleArn",
                component_role_arn="componentRoleArn",
                environment_account_id="environmentAccountId",
                environment_name="environmentName",
                management_account_id="managementAccountId",
                role_arn="roleArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92e78bba789de6e71f9d7f961684f6363d8564ac5afaa6e8f54209b72039e284)
            check_type(argname="argument codebuild_role_arn", value=codebuild_role_arn, expected_type=type_hints["codebuild_role_arn"])
            check_type(argname="argument component_role_arn", value=component_role_arn, expected_type=type_hints["component_role_arn"])
            check_type(argname="argument environment_account_id", value=environment_account_id, expected_type=type_hints["environment_account_id"])
            check_type(argname="argument environment_name", value=environment_name, expected_type=type_hints["environment_name"])
            check_type(argname="argument management_account_id", value=management_account_id, expected_type=type_hints["management_account_id"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if codebuild_role_arn is not None:
            self._values["codebuild_role_arn"] = codebuild_role_arn
        if component_role_arn is not None:
            self._values["component_role_arn"] = component_role_arn
        if environment_account_id is not None:
            self._values["environment_account_id"] = environment_account_id
        if environment_name is not None:
            self._values["environment_name"] = environment_name
        if management_account_id is not None:
            self._values["management_account_id"] = management_account_id
        if role_arn is not None:
            self._values["role_arn"] = role_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def codebuild_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of an IAM service role in the environment account.

        AWS Proton uses this role to provision infrastructure resources using CodeBuild-based provisioning in the associated environment account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-environmentaccountconnection.html#cfn-proton-environmentaccountconnection-codebuildrolearn
        '''
        result = self._values.get("codebuild_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def component_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the IAM service role that AWS Proton uses when provisioning directly defined components in the associated environment account.

        It determines the scope of infrastructure that a component can provision in the account.

        The environment account connection must have a ``componentRoleArn`` to allow directly defined components to be associated with any environments running in the account.

        For more information about components, see `AWS Proton components <https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html>`_ in the *AWS Proton User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-environmentaccountconnection.html#cfn-proton-environmentaccountconnection-componentrolearn
        '''
        result = self._values.get("component_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_account_id(self) -> typing.Optional[builtins.str]:
        '''The environment account that's connected to the environment account connection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-environmentaccountconnection.html#cfn-proton-environmentaccountconnection-environmentaccountid
        '''
        result = self._values.get("environment_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_name(self) -> typing.Optional[builtins.str]:
        '''The name of the environment that's associated with the environment account connection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-environmentaccountconnection.html#cfn-proton-environmentaccountconnection-environmentname
        '''
        result = self._values.get("environment_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def management_account_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the management account that's connected to the environment account connection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-environmentaccountconnection.html#cfn-proton-environmentaccountconnection-managementaccountid
        '''
        result = self._values.get("management_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_arn(self) -> typing.Optional[builtins.str]:
        '''The IAM service role that's associated with the environment account connection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-environmentaccountconnection.html#cfn-proton-environmentaccountconnection-rolearn
        '''
        result = self._values.get("role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional list of metadata items that you can associate with the AWS Proton environment account connection.

        A tag is a key-value pair.

        For more information, see `AWS Proton resources and tagging <https://docs.aws.amazon.com/proton/latest/userguide/resources.html>`_ in the *AWS Proton User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-environmentaccountconnection.html#cfn-proton-environmentaccountconnection-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentAccountConnectionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnEnvironmentTemplate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_proton.CfnEnvironmentTemplate",
):
    '''Create an environment template for AWS Proton .

    For more information, see `Environment Templates <https://docs.aws.amazon.com/proton/latest/userguide/ag-templates.html>`_ in the *AWS Proton User Guide* .

    You can create an environment template in one of the two following ways:

    - Register and publish a *standard* environment template that instructs AWS Proton to deploy and manage environment infrastructure.
    - Register and publish a *customer managed* environment template that connects AWS Proton to your existing provisioned infrastructure that you manage. AWS Proton *doesn't* manage your existing provisioned infrastructure. To create an environment template for customer provisioned and managed infrastructure, include the ``provisioning`` parameter and set the value to ``CUSTOMER_MANAGED`` . For more information, see `Register and publish an environment template <https://docs.aws.amazon.com/proton/latest/userguide/template-create.html>`_ in the *AWS Proton User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-environmenttemplate.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_proton as proton
        
        cfn_environment_template = proton.CfnEnvironmentTemplate(self, "MyCfnEnvironmentTemplate",
            description="description",
            display_name="displayName",
            encryption_key="encryptionKey",
            name="name",
            provisioning="provisioning",
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
        display_name: typing.Optional[builtins.str] = None,
        encryption_key: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        provisioning: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param description: A description of the environment template.
        :param display_name: The name of the environment template as displayed in the developer interface.
        :param encryption_key: The customer provided encryption key for the environment template.
        :param name: The name of the environment template.
        :param provisioning: When included, indicates that the environment template is for customer provisioned and managed infrastructure.
        :param tags: An optional list of metadata items that you can associate with the AWS Proton environment template. A tag is a key-value pair. For more information, see `AWS Proton resources and tagging <https://docs.aws.amazon.com/proton/latest/userguide/resources.html>`_ in the *AWS Proton User Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e2a73b7ee2bc44761231bdcbade4acc70c394d7d8995376813f113ef4e809ec)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnvironmentTemplateProps(
            description=description,
            display_name=display_name,
            encryption_key=encryption_key,
            name=name,
            provisioning=provisioning,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c118627efd9b4abeb2a81482dbdd168c0ed3de3481e90e77b6982f37546b8212)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a8c572648613df63aa9379805f0276d23c54d34eb19338cf9c9de723b569d15f)
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
        '''Returns the ARN of the environment template.

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
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the environment template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c3017cb6246cb9b1fe1441e75a361d9145673aca82d81b693f48652d3ee0034)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The name of the environment template as displayed in the developer interface.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a105de5a3476c047601994ddc235a4b0cf038e8636251a999d458aa8e4b3992a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> typing.Optional[builtins.str]:
        '''The customer provided encryption key for the environment template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionKey"))

    @encryption_key.setter
    def encryption_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__648690061d04f2544cc466a9b6faca374b4eef43d22368f21efa181a05f42f75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionKey", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the environment template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ee300b7f87a2421c12b7d331e829f25f35ed6418d094e0f5ab731ef5da504b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="provisioning")
    def provisioning(self) -> typing.Optional[builtins.str]:
        '''When included, indicates that the environment template is for customer provisioned and managed infrastructure.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "provisioning"))

    @provisioning.setter
    def provisioning(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13952344f4d05193e39ff94d2fe43c6b776745f5813718f927150d1f906c748e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisioning", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional list of metadata items that you can associate with the AWS Proton environment template.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a718c60c41780a6528ba1366f7802aa96b0bdb2f952b5fce603cf2d6cbc88470)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_proton.CfnEnvironmentTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "display_name": "displayName",
        "encryption_key": "encryptionKey",
        "name": "name",
        "provisioning": "provisioning",
        "tags": "tags",
    },
)
class CfnEnvironmentTemplateProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        encryption_key: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        provisioning: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEnvironmentTemplate``.

        :param description: A description of the environment template.
        :param display_name: The name of the environment template as displayed in the developer interface.
        :param encryption_key: The customer provided encryption key for the environment template.
        :param name: The name of the environment template.
        :param provisioning: When included, indicates that the environment template is for customer provisioned and managed infrastructure.
        :param tags: An optional list of metadata items that you can associate with the AWS Proton environment template. A tag is a key-value pair. For more information, see `AWS Proton resources and tagging <https://docs.aws.amazon.com/proton/latest/userguide/resources.html>`_ in the *AWS Proton User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-environmenttemplate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_proton as proton
            
            cfn_environment_template_props = proton.CfnEnvironmentTemplateProps(
                description="description",
                display_name="displayName",
                encryption_key="encryptionKey",
                name="name",
                provisioning="provisioning",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbf81c286262c5ad8217a04b316bb2f0b0282d1464ba5d63a1b97caa00e8a493)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument provisioning", value=provisioning, expected_type=type_hints["provisioning"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if display_name is not None:
            self._values["display_name"] = display_name
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if name is not None:
            self._values["name"] = name
        if provisioning is not None:
            self._values["provisioning"] = provisioning
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the environment template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-environmenttemplate.html#cfn-proton-environmenttemplate-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The name of the environment template as displayed in the developer interface.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-environmenttemplate.html#cfn-proton-environmenttemplate-displayname
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[builtins.str]:
        '''The customer provided encryption key for the environment template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-environmenttemplate.html#cfn-proton-environmenttemplate-encryptionkey
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the environment template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-environmenttemplate.html#cfn-proton-environmenttemplate-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provisioning(self) -> typing.Optional[builtins.str]:
        '''When included, indicates that the environment template is for customer provisioned and managed infrastructure.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-environmenttemplate.html#cfn-proton-environmenttemplate-provisioning
        '''
        result = self._values.get("provisioning")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional list of metadata items that you can associate with the AWS Proton environment template.

        A tag is a key-value pair.

        For more information, see `AWS Proton resources and tagging <https://docs.aws.amazon.com/proton/latest/userguide/resources.html>`_ in the *AWS Proton User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-environmenttemplate.html#cfn-proton-environmenttemplate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnServiceTemplate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_proton.CfnServiceTemplate",
):
    '''Create a service template.

    The administrator creates a service template to define standardized infrastructure and an optional CI/CD service pipeline. Developers, in turn, select the service template from AWS Proton . If the selected service template includes a service pipeline definition, they provide a link to their source code repository. AWS Proton then deploys and manages the infrastructure defined by the selected service template. For more information, see `AWS Proton templates <https://docs.aws.amazon.com/proton/latest/userguide/ag-templates.html>`_ in the *AWS Proton User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-servicetemplate.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_proton as proton
        
        cfn_service_template = proton.CfnServiceTemplate(self, "MyCfnServiceTemplate",
            description="description",
            display_name="displayName",
            encryption_key="encryptionKey",
            name="name",
            pipeline_provisioning="pipelineProvisioning",
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
        display_name: typing.Optional[builtins.str] = None,
        encryption_key: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        pipeline_provisioning: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param description: A description of the service template.
        :param display_name: The service template name as displayed in the developer interface.
        :param encryption_key: The customer provided service template encryption key that's used to encrypt data.
        :param name: The name of the service template.
        :param pipeline_provisioning: If ``pipelineProvisioning`` is ``true`` , a service pipeline is included in the service template. Otherwise, a service pipeline *isn't* included in the service template.
        :param tags: An object that includes the template bundle S3 bucket path and name for the new version of a service template.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9d6f7fcd45fb9a242859806053d250bd07d7040cbeda48256287882ff9564a8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServiceTemplateProps(
            description=description,
            display_name=display_name,
            encryption_key=encryption_key,
            name=name,
            pipeline_provisioning=pipeline_provisioning,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddd527106465752977c49de51e5880dae732ab3e117d6705c7481fc03c0ec62b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec2b71dfda419a5086df44379f403384ee3f47ccf9f3b99eb029356df0b301fe)
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
        '''Returns the service template ARN.

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
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the service template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b28073324900aad1ec4b48a24ca1cf7e536969fe8e585a9db1b04de8f5a5660)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The service template name as displayed in the developer interface.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ccab56f5c5641a51957cc5cd6204b54532f81019d2e3f2d8745c6352de7449d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionKey")
    def encryption_key(self) -> typing.Optional[builtins.str]:
        '''The customer provided service template encryption key that's used to encrypt data.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionKey"))

    @encryption_key.setter
    def encryption_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25d39f44b2de597ffe7248d3c35113c03029f9bbd75f232945e9d667d800d759)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionKey", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the service template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ba71e7bd226dd89a72bb66f2008917e40b5588ceb1f0fbf3dda8348cd9d0004)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="pipelineProvisioning")
    def pipeline_provisioning(self) -> typing.Optional[builtins.str]:
        '''If ``pipelineProvisioning`` is ``true`` , a service pipeline is included in the service template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pipelineProvisioning"))

    @pipeline_provisioning.setter
    def pipeline_provisioning(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c2d95b068209ade2ec58e4e7f9bdd418805321ebcfc007e6491b07ceb0b8fd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pipelineProvisioning", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An object that includes the template bundle S3 bucket path and name for the new version of a service template.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00e30d2907243dab58015f5d20dd35d6a72df42367b8c6db016733a72ca69953)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_proton.CfnServiceTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "display_name": "displayName",
        "encryption_key": "encryptionKey",
        "name": "name",
        "pipeline_provisioning": "pipelineProvisioning",
        "tags": "tags",
    },
)
class CfnServiceTemplateProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        encryption_key: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        pipeline_provisioning: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnServiceTemplate``.

        :param description: A description of the service template.
        :param display_name: The service template name as displayed in the developer interface.
        :param encryption_key: The customer provided service template encryption key that's used to encrypt data.
        :param name: The name of the service template.
        :param pipeline_provisioning: If ``pipelineProvisioning`` is ``true`` , a service pipeline is included in the service template. Otherwise, a service pipeline *isn't* included in the service template.
        :param tags: An object that includes the template bundle S3 bucket path and name for the new version of a service template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-servicetemplate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_proton as proton
            
            cfn_service_template_props = proton.CfnServiceTemplateProps(
                description="description",
                display_name="displayName",
                encryption_key="encryptionKey",
                name="name",
                pipeline_provisioning="pipelineProvisioning",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89231d286a017b3eab9ec8b8264aba07ec6ccebcb08bae53e0a07ad0b4990eca)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument pipeline_provisioning", value=pipeline_provisioning, expected_type=type_hints["pipeline_provisioning"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if display_name is not None:
            self._values["display_name"] = display_name
        if encryption_key is not None:
            self._values["encryption_key"] = encryption_key
        if name is not None:
            self._values["name"] = name
        if pipeline_provisioning is not None:
            self._values["pipeline_provisioning"] = pipeline_provisioning
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the service template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-servicetemplate.html#cfn-proton-servicetemplate-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The service template name as displayed in the developer interface.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-servicetemplate.html#cfn-proton-servicetemplate-displayname
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_key(self) -> typing.Optional[builtins.str]:
        '''The customer provided service template encryption key that's used to encrypt data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-servicetemplate.html#cfn-proton-servicetemplate-encryptionkey
        '''
        result = self._values.get("encryption_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the service template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-servicetemplate.html#cfn-proton-servicetemplate-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pipeline_provisioning(self) -> typing.Optional[builtins.str]:
        '''If ``pipelineProvisioning`` is ``true`` , a service pipeline is included in the service template.

        Otherwise, a service pipeline *isn't* included in the service template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-servicetemplate.html#cfn-proton-servicetemplate-pipelineprovisioning
        '''
        result = self._values.get("pipeline_provisioning")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An object that includes the template bundle S3 bucket path and name for the new version of a service template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-proton-servicetemplate.html#cfn-proton-servicetemplate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServiceTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnEnvironmentAccountConnection",
    "CfnEnvironmentAccountConnectionProps",
    "CfnEnvironmentTemplate",
    "CfnEnvironmentTemplateProps",
    "CfnServiceTemplate",
    "CfnServiceTemplateProps",
]

publication.publish()

def _typecheckingstub__826262668de499159f2330eeadab45eb7cc0e3ce5dab7cadd5a4853b4856820b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    codebuild_role_arn: typing.Optional[builtins.str] = None,
    component_role_arn: typing.Optional[builtins.str] = None,
    environment_account_id: typing.Optional[builtins.str] = None,
    environment_name: typing.Optional[builtins.str] = None,
    management_account_id: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b30ec85df499b3f87a92d53ab1648560e2495ee044a1fb86faf3008181494293(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__470395ff1b3bc54712f215fb1b2f6214bb182bd963a863176e86d9a96c0f1972(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47f4e15b8378b0030dc5e8be607efef26d4e7bc41f9bc4d16a82239ecce2af2e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b976b51e7ad9d2668f5e11057b8add49417ccb62f9ec6ee2a16bfdf2cb4dab1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36ad911396cde9a5836f2bf5c2178028454c62766b60ac3747357e9c24e96de8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d94be46146198fddc9c899c0dade14c643b597a9839643b3cc6c9f144935c502(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cbf14273aade064dc4e71967934b15a396069e1c949a15c0436c98dd68e54c3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37b19867aae52947f0d449ddee0fce5ac822cd037dbd498834aaf9268ddd0cf1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__952d5d229754748fd9299ff4728f53f331581c6208e0c33caa4616b211155911(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92e78bba789de6e71f9d7f961684f6363d8564ac5afaa6e8f54209b72039e284(
    *,
    codebuild_role_arn: typing.Optional[builtins.str] = None,
    component_role_arn: typing.Optional[builtins.str] = None,
    environment_account_id: typing.Optional[builtins.str] = None,
    environment_name: typing.Optional[builtins.str] = None,
    management_account_id: typing.Optional[builtins.str] = None,
    role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e2a73b7ee2bc44761231bdcbade4acc70c394d7d8995376813f113ef4e809ec(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    encryption_key: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    provisioning: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c118627efd9b4abeb2a81482dbdd168c0ed3de3481e90e77b6982f37546b8212(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8c572648613df63aa9379805f0276d23c54d34eb19338cf9c9de723b569d15f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c3017cb6246cb9b1fe1441e75a361d9145673aca82d81b693f48652d3ee0034(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a105de5a3476c047601994ddc235a4b0cf038e8636251a999d458aa8e4b3992a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__648690061d04f2544cc466a9b6faca374b4eef43d22368f21efa181a05f42f75(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ee300b7f87a2421c12b7d331e829f25f35ed6418d094e0f5ab731ef5da504b5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13952344f4d05193e39ff94d2fe43c6b776745f5813718f927150d1f906c748e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a718c60c41780a6528ba1366f7802aa96b0bdb2f952b5fce603cf2d6cbc88470(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbf81c286262c5ad8217a04b316bb2f0b0282d1464ba5d63a1b97caa00e8a493(
    *,
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    encryption_key: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    provisioning: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9d6f7fcd45fb9a242859806053d250bd07d7040cbeda48256287882ff9564a8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    encryption_key: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    pipeline_provisioning: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddd527106465752977c49de51e5880dae732ab3e117d6705c7481fc03c0ec62b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec2b71dfda419a5086df44379f403384ee3f47ccf9f3b99eb029356df0b301fe(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b28073324900aad1ec4b48a24ca1cf7e536969fe8e585a9db1b04de8f5a5660(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ccab56f5c5641a51957cc5cd6204b54532f81019d2e3f2d8745c6352de7449d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25d39f44b2de597ffe7248d3c35113c03029f9bbd75f232945e9d667d800d759(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ba71e7bd226dd89a72bb66f2008917e40b5588ceb1f0fbf3dda8348cd9d0004(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c2d95b068209ade2ec58e4e7f9bdd418805321ebcfc007e6491b07ceb0b8fd3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00e30d2907243dab58015f5d20dd35d6a72df42367b8c6db016733a72ca69953(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89231d286a017b3eab9ec8b8264aba07ec6ccebcb08bae53e0a07ad0b4990eca(
    *,
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    encryption_key: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    pipeline_provisioning: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
